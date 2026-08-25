#!/usr/bin/env python3
"""
Job A, Stage 0 — local prep. No model calls, no tokens spent.

    py scripts/prep.py <course> <tab> [subpath]

Reads courses/<course>/raw/<tab>/[subpath] recursively. Writes prepped pages
to courses/<course>/.prep/<tab>/[subpath] plus a manifest.json, and prints a
pre-flight report (also written to .../preflight.md). subpath scopes a run to
one folder within a tab (e.g. one exam's subfolder) without disturbing the
tab-level prep output a later full-tab run would use — the shared
.ledger.json is still consulted either way, so nothing gets double-processed.

    py scripts/prep.py <course> --file <path under courses/<course>/> --pages 1,2,3 [--out label] [--color]

Patch mode, for Job B: prep specific known pages of one slide deck (e.g. a
handful of diagram-only pages whose caption text a first pass couldn't
extract) without re-running the whole deck. Bypasses the raw/ ledger — this
is slides/, not exam captures. Output goes to
courses/<course>/.prep/slides-patch/<label>/.

--color skips the grayscale step. Default grayscale is correct for Job A
exam captures (the answer is which radio is filled, not what color it is)
but wrong for a slide whose diagnostic content IS color — a plate photo
distinguished by a colored sheen or pigment, a stained-slide comparison.
Use --color when the fact being patched in is itself a color.

Never writes to, renames, or deletes anything under raw/.

Steps, per CLAUDE.md and job-a-extract.md:
  1. Walk and hash every input file (sha1).
  2. Skip anything already recorded in courses/<course>/.ledger.json — except a
     file recorded with "partial": true, which is never skipped, since a partial
     entry means only some of its pages were consumed and the rest still need
     Stage 0.
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
            # A file marked partial was only part-consumed by that batch — record
            # of work done, never a reason to skip. Suppressing it here would make
            # its unextracted remainder invisible to every future run.
            if "sha1" in f and not f.get("partial"):
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


DARK_PIXEL = 60          # near-black; a status/nav bar or letterbox fill
# A phone status/nav bar is mostly-dark, not uniformly dark — light clock text,
# battery and signal icons punch dozens of rows below a near-100% threshold even
# though the row is still clearly bar, not content. A real content row (question
# text on a light background) sits far below this: text glyphs are sparse enough
# against the background that its dark fraction stays near 0. 0.5 sits well
# clear of both populations.
DARK_EDGE_FRACTION = 0.5
MIN_TRIMMED_PX = 150    # degenerate-result floor for trim_dark_border, in pixels


def _walk_edge(n, is_dark, tolerance=8):
    """How far a dark border region extends from index 0, tolerating up to
    `tolerance` consecutive non-dark rows/cols before giving up — the outer
    white-margin crop leaves a couple of antialiased fringe pixels right at its
    own edge, and without this a single light row there would stop the walk
    before it ever reaches the real bar. A page with no dark border at all
    (first row already light) exceeds tolerance immediately and returns 0, so
    this still can't trim a page that has none."""
    border_end = 0
    gap = 0
    for i in range(n):
        if is_dark(i):
            gap = 0
            border_end = i + 1
        else:
            gap += 1
            if gap > tolerance:
                break
    return border_end


def _trim_dark_axis(im: Image.Image, rows: bool):
    """One axis of trim_dark_border. Must run on an image whose OTHER axis is
    already trimmed of its own bars — a full-width top/bottom bar makes every
    column look mostly-dark when evaluated over the untrimmed height, and
    trims columns that were never actually part of a bar. Rows before columns,
    each on the previous stage's output, keeps every dark-fraction measurement
    restricted to the dimension it's actually testing."""
    w, h = im.size
    if w == 0 or h == 0:
        return im, False
    gray = im if im.mode == "L" else ImageOps.grayscale(im)
    px = gray.load()
    n = h if rows else w
    step = max(1, (w if rows else h) // 200)

    def dark_frac(i):
        if rows:
            vals = [px[x, i] for x in range(0, w, step)]
        else:
            vals = [px[i, y] for y in range(0, h, step)]
        return sum(1 for v in vals if v < DARK_PIXEL) / len(vals)

    def is_dark(i):
        return dark_frac(i) >= DARK_EDGE_FRACTION

    start = _walk_edge(n, is_dark)
    end = n - _walk_edge(n, lambda i: is_dark(n - 1 - i))
    if end < start:
        end = start
    if start == 0 and end == n:
        return im, False
    if end - start < MIN_TRIMMED_PX:
        return im, False

    box = (0, start, w, end) if rows else (start, 0, end, h)
    return im.crop(box), True


def trim_dark_border(im: Image.Image):
    """Trim uniformly dark letterbox bars — a phone screenshot pasted into a page
    keeps its own black status/nav bars, which content_bbox's not-near-white
    threshold treats as content and safe_crop therefore leaves in place. Call this
    AFTER safe_crop (or on an already content-cropped image): detecting a dark
    edge-to-edge run requires the white page margin already gone, otherwise a
    bar's dark-pixel fraction is diluted by that margin and never crosses
    threshold. Returns (image, trimmed_bool); a no-op — same image back — on any
    page with no such bar, which is why it cannot regress a page that's already
    all white/gray background."""
    trimmed_rows, row_hit = _trim_dark_axis(im, rows=True)
    trimmed_both, col_hit = _trim_dark_axis(trimmed_rows, rows=False)
    if not (row_hit or col_hit):
        return im, False
    return trimmed_both, True


def prep_image(path: Path, out_path: Path) -> dict:
    info = {"below_floor": False, "cropped": False, "trimmed": False, "flag": None}
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

        im, trimmed = trim_dark_border(im)
        info["trimmed"] = trimmed

        im = ImageOps.grayscale(im)
        long_edge = max(im.size)
        if long_edge > FLOOR_PX:
            scale = FLOOR_PX / float(long_edge)
            new_size = (max(1, int(im.width * scale)), max(1, int(im.height * scale)))
            im = im.resize(new_size, Image.LANCZOS)
        im.convert("L").save(out_path, "JPEG", quality=JPEG_QUALITY)
    return info


def prep_pdf(path: Path, out_dir: Path, stem: str, only_pages: set = None, grayscale: bool = True) -> dict:
    """Returns per-page results: list of dicts with keys
    {page, mode: text|image, chars, out_path, below_floor}.
    only_pages, if given, is a set of 1-indexed page numbers — every other
    page is skipped entirely (used for patching specific known-diagram pages
    rather than re-processing a whole deck). grayscale=False preserves color
    for pages whose diagnostic content is itself a color."""
    results = []
    doc = fitz.open(str(path))
    for i, page in enumerate(doc, start=1):
        if only_pages is not None and i not in only_pages:
            continue
        text = page.get_text("text")
        chars = len(text.strip())
        if chars >= 20:  # a real text layer, not stray OCR noise/watermark
            results.append({"page": i, "mode": "text", "chars": chars, "out_path": None})
            continue

        pix = page.get_pixmap(dpi=DPI)
        img_bytes = pix.tobytes("png")
        im = Image.open(io.BytesIO(img_bytes))

        # A rendered PDF page never got safe_crop's white-margin crop before —
        # only images from prep_image did. A phone screenshot pasted into a page
        # (its own black status/nav bars, white A4 margin around it) needs both
        # passes to reach true content resolution: crop the white margin, then
        # trim the dark bars that survive that crop as "content".
        cropped_ok = False
        cropped, _reason = safe_crop(im)
        if cropped is not None:
            im = cropped
            cropped_ok = True
        im, trimmed_ok = trim_dark_border(im)

        orig_long = max(im.size)
        out_path = out_dir / f"{stem}__p{i:03d}.jpg"

        below_floor = orig_long <= FLOOR_PX
        if not below_floor:
            im2 = ImageOps.grayscale(im) if grayscale else im
            scale = FLOOR_PX / float(orig_long)
            new_size = (max(1, int(im2.width * scale)), max(1, int(im2.height * scale)))
            im2 = im2.resize(new_size, Image.LANCZOS)
            im2.convert("L" if grayscale else "RGB").save(out_path, "JPEG", quality=JPEG_QUALITY)
        else:
            im.convert("RGB").save(out_path, "JPEG", quality=JPEG_QUALITY)

        results.append({
            "page": i, "mode": "image", "chars": chars,
            "out_path": str(out_path), "below_floor": below_floor,
            "cropped": cropped_ok, "trimmed": trimmed_ok,
        })
    doc.close()
    return results


def estimate_tokens(vision_pages: int, text_chars: int) -> tuple:
    # Rough Stage-1 read budget: ~1500 tokens/vision page (image + surrounding
    # transcription overhead), ~0.3 tokens/char for text-layer content.
    low = int(vision_pages * 1300 + text_chars * 0.25)
    high = int(vision_pages * 1900 + text_chars * 0.35)
    return low, high


def patch_file(course: str, file_arg: str, pages_arg: str, out_label: str = None, color: bool = False):
    course_dir = REPO_ROOT / "courses" / course
    src_path = course_dir / file_arg
    if not src_path.exists():
        print(f"no such file: {src_path}", file=sys.stderr)
        sys.exit(1)

    only_pages = {int(p) for p in pages_arg.split(",") if p.strip()}
    label = out_label or re.sub(r"[^A-Za-z0-9._-]", "_", src_path.stem)
    prep_dir = course_dir / ".prep" / "slides-patch" / label
    prep_dir.mkdir(parents=True, exist_ok=True)

    stem = re.sub(r"[^A-Za-z0-9._-]", "_", src_path.stem)
    page_results = prep_pdf(src_path, prep_dir, stem, only_pages=only_pages, grayscale=not color)

    manifest = {
        "course": course, "mode": "patch", "file": file_arg,
        "requested_pages": sorted(only_pages),
        "generated": datetime.now().isoformat(timespec="seconds"),
        "pages": page_results,
    }
    (prep_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    found = {pr["page"] for pr in page_results}
    missing = sorted(only_pages - found)
    print(f"# {course} — patch: {file_arg}")
    print(f"- requested pages: {sorted(only_pages)}")
    print(f"- found: {sorted(found)}")
    if missing:
        print(f"- MISSING (out of range for this PDF): {missing}")
    for pr in page_results:
        if pr["mode"] == "text":
            print(f"  p{pr['page']:03d}: text layer ({pr['chars']} chars) — no vision needed")
        else:
            print(f"  p{pr['page']:03d}: image -> {pr['out_path']}")


def main():
    if "--file" in sys.argv:
        course = sys.argv[1]
        args = sys.argv[2:]
        opts = {}
        i = 0
        BOOL_FLAGS = {"color"}
        while i < len(args):
            if args[i].startswith("--"):
                key = args[i][2:]
                if key in BOOL_FLAGS:
                    opts[key] = True
                    i += 1
                else:
                    opts[key] = args[i + 1]
                    i += 2
            else:
                i += 1
        if "file" not in opts or "pages" not in opts:
            print("usage: py scripts/prep.py <course> --file <path> --pages 1,2,3 [--out label] [--color]", file=sys.stderr)
            sys.exit(1)
        patch_file(course, opts["file"], opts["pages"], opts.get("out"), color=("color" in opts))
        return

    if len(sys.argv) not in (3, 4):
        print("usage: py scripts/prep.py <course> <tab> [subpath]", file=sys.stderr)
        sys.exit(1)
    course, tab = sys.argv[1], sys.argv[2]
    subpath = sys.argv[3] if len(sys.argv) == 4 else None

    course_dir = REPO_ROOT / "courses" / course
    raw_dir = course_dir / "raw" / tab / subpath if subpath else course_dir / "raw" / tab
    prep_dir = course_dir / ".prep" / tab / subpath if subpath else course_dir / ".prep" / tab
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
        "course": course, "tab": tab, "subpath": subpath,
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
    claimed_out_paths = set()
    collided_out_paths = []

    for p, h in new_files:
        rel = str(p.relative_to(raw_dir))
        kind = classify_file(p)
        entry = {"path": rel, "sha1": h, "kind": kind, "pages": []}

        if kind == "image":
            rel_stem = re.sub(r"[^A-Za-z0-9._-]", "_", str(Path(rel).with_suffix("")))
            stem = f"{rel_stem}-{h[:8]}"
            out_path = prep_dir / f"{stem}.jpg"
            if str(out_path) in claimed_out_paths:
                collided_out_paths.append(str(out_path))
            claimed_out_paths.add(str(out_path))
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
            rel_stem = re.sub(r"[^A-Za-z0-9._-]", "_", str(Path(rel).with_suffix("")))
            stem = f"{rel_stem}-{h[:8]}"
            try:
                page_results = prep_pdf(p, prep_dir, stem)
            except Exception as e:
                flagged.append({"file": rel, "page": None, "reason": f"pdf-open-failed: {e}"})
                manifest["files"].append(entry)
                continue
            for pr in page_results:
                total_pages += 1
                if pr.get("out_path"):
                    if pr["out_path"] in claimed_out_paths:
                        collided_out_paths.append(pr["out_path"])
                    claimed_out_paths.add(pr["out_path"])
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

    # Anti-loss check: every vision page must have claimed a unique output path.
    # A repeat here means one page's file silently overwrote another's on disk —
    # exactly the failure mode that lost 45 midterm pages before out_path stems
    # carried a sha1 suffix. Surface it instead of writing a clean-looking report
    # over a lossy run.
    unique_out_paths = len(claimed_out_paths)
    output_name_collisions = len(collided_out_paths)
    if output_name_collisions:
        for cp in collided_out_paths:
            flagged.append({"file": None, "page": None, "reason": f"output-path-collision: {cp}"})

    manifest["summary"] = {
        "new_files": len(new_files),
        "total_pages": total_pages,
        "text_layer_pages": text_pages,
        "vision_pages": vision_pages,
        "below_floor_pages": below_floor_pages,
        "documents": documents,
        "flagged": len(flagged),
        "unique_out_paths": unique_out_paths,
        "output_name_collisions": output_name_collisions,
    }
    manifest["flags"] = flagged

    assert unique_out_paths == vision_pages, (
        f"Stage 0 output-path collision: {vision_pages} vision pages claimed but only "
        f"{unique_out_paths} unique out_paths written. {output_name_collisions} page(s) "
        f"overwrote another page's file. See manifest.json 'flags' for the colliding paths."
    )

    manifest_path = prep_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    tok_low, tok_high = estimate_tokens(vision_pages, total_text_chars)
    batches = max(1, -(-vision_pages // 7))  # ceil div, ~6-8 pages/batch

    label = f"{tab}/{subpath}" if subpath else tab
    report_lines = [
        f"# {course} / {label} — Stage 0 pre-flight",
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
        f"- output-path collisions: {output_name_collisions}",
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
