#!/usr/bin/env python3
"""
Job A, Stage 0 — local prep. No model calls, no tokens spent.

    py scripts/prep.py <course> <tab>

Reads courses/<course>/raw/<tab>/ recursively. Writes prepped pages to
courses/<course>/.prep/<tab>/ plus a manifest.json, and prints a pre-flight
report (also written to courses/<course>/.prep/<tab>/preflight.md).

Never writes to, renames, or deletes anything under raw/.

Steps, per CLAUDE.md and job-a-extract.md:
  1. Walk and hash every input file (sha1).
  2. Skip anything already recorded in courses/<course>/.ledger.json.
  3. Dedupe by hash within this run — first path by capture order wins,
     the rest are recorded as duplicates, never deleted.
  4. Classify: image / pdf-with-text-layer / pdf-image-only / document.
  5. PDFs: per-page text-layer check via PyMuPDF; text pages are extracted
     as text (free), image-only pages render at 200 dpi.
  6. Images: EXIF auto-rotate -> crop to content -> grayscale -> downscale
     to a 1000px long edge -> JPEG q85. Never upscale, never push a page
     that's already below the 1000px floor further down.
  7. Order pages by filename timestamp, then name.
  8. Report: page count, free-via-text-layer vs needs-vision, below-floor
     count, duplicates dropped, flagged pages, token estimate.
"""
import sys
import os
import json
import hashlib
import re
import io
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from PIL import Image, ImageOps, ImageFilter

try:
    import pymupdf as fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF is required: py -m pip install pymupdf", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
DOC_EXTS = {".docx", ".doc", ".txt", ".md"}
FLOOR_PX = 1000
JPEG_QUALITY = 85
DPI = 200

# Crop safety valve: never trust a crop that throws away more than this
# fraction of the page, or leaves a box smaller than this fraction of
# either original dimension.
MAX_CROP_AREA_LOSS = 0.60
MIN_CROP_FRACTION = 0.40


def sha1_of(path: Path) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_ledger(course_dir: Path) -> set:
    ledger_path = course_dir / ".ledger.json"
    if not ledger_path.exists():
        return set()
    try:
        data = json.loads(ledger_path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    seen = set()
    for batch in data.get("batches", []):
        for f in batch.get("files", []):
            if "sha1" in f:
                seen.add(f["sha1"])
    return seen


TIMESTAMP_RE = re.compile(r"(\d{4}-\d{2}-\d{2}[-_]\d{2}[-_]\d{2}[-_]\d{2})")
DIGITS_RE = re.compile(r"\d+")


def capture_order_key(path: Path):
    """Order by any embedded timestamp first, else by leading/embedded
    numeric run, else lexically. Filenames carry capture order — never
    renamed, so this key has to make sense of whatever pattern shows up."""
    name = path.name
    m = TIMESTAMP_RE.search(name)
    if m:
        return (0, m.group(1), name)
    nums = DIGITS_RE.findall(name)
    if nums:
        return (1, [int(n) for n in nums], name)
    return (2, [], name)


def classify_file(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext == ".pdf":
        return "pdf"
    if ext in DOC_EXTS:
        return "document"
    return "other"


def content_bbox(im: Image.Image):
    """Pure-Pillow content detection (no numpy/OpenCV available here):
    grayscale -> autocontrast -> threshold -> bounding box of non-background
    pixels. Returns None if nothing usable is found."""
    gray = ImageOps.grayscale(im)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    # Background is usually near-white; threshold to find the content region.
    thresh = gray.point(lambda p: 255 if p < 245 else 0)
    thresh = thresh.filter(ImageFilter.MaxFilter(5))  # close small gaps
    return thresh.getbbox()


def safe_crop(im: Image.Image):
    """Returns (cropped_image_or_None, reason). None means: don't crop,
    ship the page as-is and flag why."""
    w, h = im.size
    bbox = content_bbox(im)
    if bbox is None:
        return None, "no-content-detected"
    bx0, by0, bx1, by1 = bbox
    bw, bh = bx1 - bx0, by1 - by0
    if bw <= 0 or bh <= 0:
        return None, "degenerate-bbox"
    area_kept = (bw * bh) / float(w * h)
    frac_w = bw / float(w)
    frac_h = bh / float(h)
    if area_kept < (1 - MAX_CROP_AREA_LOSS):
        return None, f"crop-would-discard-{int((1-area_kept)*100)}pct"
    if frac_w < MIN_CROP_FRACTION or frac_h < MIN_CROP_FRACTION:
        return None, "crop-box-too-small"
    return im.crop(bbox), None


def prep_image(path: Path, out_path: Path) -> dict:
    info = {"below_floor": False, "cropped": False, "flag": None}
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)  # auto-rotate via EXIF
        orig_long = max(im.size)

        if orig_long <= FLOOR_PX:
            # Already at or under the floor: pass through untouched.
            info["below_floor"] = True
            im.convert("RGB").save(out_path, "JPEG", quality=JPEG_QUALITY)
            return info

        cropped, reason = safe_crop(im)
        if cropped is not None:
            im = cropped
            info["cropped"] = True
        else:
            info["flag"] = reason

        im = ImageOps.grayscale(im)
        long_edge = max(im.size)
        if long_edge > FLOOR_PX:
            scale = FLOOR_PX / float(long_edge)
            new_size = (max(1, int(im.width * scale)), max(1, int(im.height * scale)))
            im = im.resize(new_size, Image.LANCZOS)
        im.convert("L").save(out_path, "JPEG", quality=JPEG_QUALITY)
    return info


def prep_pdf(path: Path, out_dir: Path, stem: str) -> dict:
    """Returns per-page results: list of dicts with keys
    {page, mode: text|image, chars, out_path, below_floor}."""
    results = []
    doc = fitz.open(str(path))
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        chars = len(text.strip())
        if chars >= 20:  # a real text layer, not stray OCR noise/watermark
            results.append({"page": i, "mode": "text", "chars": chars, "out_path": None})
            continue

        pix = page.get_pixmap(dpi=DPI)
        img_bytes = pix.tobytes("png")
        im = Image.open(io.BytesIO(img_bytes))
        orig_long = max(im.size)
        out_path = out_dir / f"{stem}__p{i:03d}.jpg"

        below_floor = orig_long <= FLOOR_PX
        if not below_floor:
            im2 = ImageOps.grayscale(im)
            scale = FLOOR_PX / float(orig_long)
            new_size = (max(1, int(im2.width * scale)), max(1, int(im2.height * scale)))
            im2 = im2.resize(new_size, Image.LANCZOS)
            im2.convert("L").save(out_path, "JPEG", quality=JPEG_QUALITY)
        else:
            im.convert("RGB").save(out_path, "JPEG", quality=JPEG_QUALITY)

        results.append({
            "page": i, "mode": "image", "chars": chars,
            "out_path": str(out_path), "below_floor": below_floor,
        })
    doc.close()
    return results


def estimate_tokens(vision_pages: int, text_chars: int) -> tuple:
    # Rough Stage-1 read budget: ~1500 tokens/vision page (image + surrounding
    # transcription overhead), ~0.3 tokens/char for text-layer content.
    low = int(vision_pages * 1300 + text_chars * 0.25)
    high = int(vision_pages * 1900 + text_chars * 0.35)
    return low, high


def main():
    if len(sys.argv) != 3:
        print("usage: py scripts/prep.py <course> <tab>", file=sys.stderr)
        sys.exit(1)
    course, tab = sys.argv[1], sys.argv[2]

    course_dir = REPO_ROOT / "courses" / course
    raw_dir = course_dir / "raw" / tab
    prep_dir = course_dir / ".prep" / tab
    if not raw_dir.exists():
        print(f"no such folder: {raw_dir}", file=sys.stderr)
        sys.exit(1)
    prep_dir.mkdir(parents=True, exist_ok=True)

    ledger_hashes = load_ledger(course_dir)

    all_files = [p for p in raw_dir.rglob("*") if p.is_file()]
    all_files.sort(key=capture_order_key)

    hash_to_first = {}
    duplicates = []      # (path, of_path)
    already_ledgered = []
    new_files = []

    for p in all_files:
        h = sha1_of(p)
        if h in ledger_hashes:
            already_ledgered.append((p, h))
            continue
        if h in hash_to_first:
            duplicates.append((p, hash_to_first[h], h))
            continue
        hash_to_first[h] = p
        new_files.append((p, h))

    manifest = {
        "course": course, "tab": tab,
        "generated": datetime.now().isoformat(timespec="seconds"),
        "inputs": len(all_files),
        "already_in_ledger": len(already_ledgered),
        "duplicates_dropped": len(duplicates),
        "duplicate_pairs": [
            {"duplicate": str(p.relative_to(raw_dir)), "of": str(orig.relative_to(raw_dir)), "sha1": h}
            for p, orig, h in duplicates
        ],
        "files": [],
    }

    total_pages = 0
    text_pages = 0
    vision_pages = 0
    below_floor_pages = 0
    documents = 0
    flagged = []
    total_text_chars = 0

    for p, h in new_files:
        rel = str(p.relative_to(raw_dir))
        kind = classify_file(p)
        entry = {"path": rel, "sha1": h, "kind": kind, "pages": []}

        if kind == "image":
            stem = re.sub(r"[^A-Za-z0-9._-]", "_", p.stem)
            out_path = prep_dir / f"{stem}.jpg"
            info = prep_image(p, out_path)
            total_pages += 1
            vision_pages += 1
            if info["below_floor"]:
                below_floor_pages += 1
            if info["flag"]:
                flagged.append({"file": rel, "page": 1, "reason": info["flag"]})
            entry["pages"].append({
                "page": 1, "mode": "image", "out_path": str(out_path),
                "below_floor": info["below_floor"], "cropped": info["cropped"],
                "flag": info["flag"],
            })

        elif kind == "pdf":
            stem = re.sub(r"[^A-Za-z0-9._-]", "_", p.stem)
            try:
                page_results = prep_pdf(p, prep_dir, stem)
            except Exception as e:
                flagged.append({"file": rel, "page": None, "reason": f"pdf-open-failed: {e}"})
                manifest["files"].append(entry)
                continue
            for pr in page_results:
                total_pages += 1
                if pr["mode"] == "text":
                    text_pages += 1
                    total_text_chars += pr["chars"]
                else:
                    vision_pages += 1
                    if pr.get("below_floor"):
                        below_floor_pages += 1
                entry["pages"].append(pr)

        elif kind == "document":
            documents += 1
            entry["pages"].append({"mode": "document-passthrough"})

        else:
            flagged.append({"file": rel, "page": None, "reason": "unrecognized-file-type"})

        manifest["files"].append(entry)

    manifest["summary"] = {
        "new_files": len(new_files),
        "total_pages": total_pages,
        "text_layer_pages": text_pages,
        "vision_pages": vision_pages,
        "below_floor_pages": below_floor_pages,
        "documents": documents,
        "flagged": len(flagged),
    }
    manifest["flags"] = flagged

    manifest_path = prep_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    tok_low, tok_high = estimate_tokens(vision_pages, total_text_chars)
    batches = max(1, -(-vision_pages // 7))  # ceil div, ~6-8 pages/batch

    report_lines = [
        f"# {course} / {tab} — Stage 0 pre-flight",
        "",
        f"- inputs: {len(all_files)}",
        f"- already in ledger (skipped): {len(already_ledgered)}",
        f"- duplicates dropped (kept as duplicate record, not deleted): {len(duplicates)}",
        f"- new since ledger: {len(new_files)}",
        f"- documents (text/docx, read directly): {documents}",
        f"- total pages: {total_pages}",
        f"- free via text layer: {text_pages}",
        f"- need vision: {vision_pages}",
        f"- below 1000px floor (passed through untouched): {below_floor_pages}",
        f"- flagged: {len(flagged)}",
        f"- estimated Stage 1 read: ~{tok_low//1000}k-{tok_high//1000}k tokens across {batches} batches of 6-8 pages",
    ]
    if flagged:
        report_lines.append("")
        report_lines.append("## Flagged")
        for f in flagged:
            page_str = f"p{f['page']}" if f["page"] else "-"
            report_lines.append(f"- {f['file']} [{page_str}]: {f['reason']}")
    if duplicates:
        report_lines.append("")
        report_lines.append("## Duplicates (not moved, not deleted, excluded from this batch)")
        for p, orig, h in duplicates:
            report_lines.append(f"- {p.relative_to(raw_dir)}  (same as {orig.relative_to(raw_dir)})")

    report = "\n".join(report_lines) + "\n"
    (prep_dir / "preflight.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
