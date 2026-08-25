#!/usr/bin/env python3
"""
Site build — courses/*/out/*.md -> site/dist/data.json (+ copied img/ crops).

No dependencies beyond the standard library. Never writes into git-tracked
territory; site/dist/ is gitignored and regenerated from the batch files
every time.

    py site/build.py

Fails loudly (nonzero exit) if a batch file's parsed question count or
per-status tallies don't match its own frontmatter — the same arithmetic
self-check the pipeline itself uses, applied one more time at hand-off to
the site so a parsing bug can't quietly ship a wrong bank.
"""
import sys
import json
import re
import shutil
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = REPO_ROOT / "courses"
DIST_DIR = Path(__file__).resolve().parent / "dist"

ID_HEADING_RE = re.compile(r"^## (\S+)\s*$", re.M)
OPTION_RE = re.compile(r"^([a-z])\)\s?(.*)$")
OPTION_CONT_RE = re.compile(r"^   (.*)$")  # 3-space continuation, per the batch format
# Key text can carry mixed case and parens -- "note (Job A):" -- so the charset
# has to allow both; matching is then done case-insensitively against META_KEYS.
KEY_LINE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 ()]*):\s?(.*)$")

# Metadata keys recorded per question, in the order job-d-build.md writes them.
# Anything else on a line before the blank separator is treated as a stray
# continuation of the previous key (matches how the batch files actually wrap).
META_KEYS = {
    "status", "form", "type", "answer", "claimed", "basis", "evidence",
    "img", "note", "note (job a)", "seen",
}


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter block found")
    lines = m.group(1).split("\n")
    fm = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^([a-z_]+):\s?(.*)$", line)
        if not km:
            i += 1
            continue
        key, val = km.group(1), km.group(2).strip()
        i += 1
        cont = []
        while i < len(lines) and lines[i].startswith("  "):
            cont.append(lines[i].strip())
            i += 1
        if cont:
            val = " ".join([val] + cont) if val else " ".join(cont)
        fm[key] = val.strip('"')
    return fm, text[m.end():]


def parse_question_block(qid: str, block: str):
    """block is everything after the '## ID' heading line, up to (not
    including) the next heading. Returns (meta_dict, stem, options_list)."""
    lines = block.split("\n")
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    meta = {}
    last_key = None
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            i += 1
            break
        km = KEY_LINE_RE.match(line)
        key_lower = km.group(1).lower() if km else None
        if km and key_lower in META_KEYS:
            last_key = key_lower
            meta[last_key] = km.group(2).strip()
        elif line.startswith("  ") and last_key:
            meta[last_key] = (meta[last_key] + " " + line.strip()).strip()
        else:
            # Not a recognized key and not a continuation: metadata section
            # is over (defensive — shouldn't happen in a well-formed batch).
            break
        i += 1
    body_lines = lines[i:]
    while body_lines and body_lines[0].strip() == "":
        body_lines.pop(0)

    stem_lines = []
    options = []
    cur_letter = None
    for line in body_lines:
        om = OPTION_RE.match(line)
        if om:
            cur_letter = om.group(1)
            options.append([cur_letter, om.group(2)])
            continue
        cm = OPTION_CONT_RE.match(line) if cur_letter else None
        if cm:
            options[-1][1] = (options[-1][1] + " " + cm.group(1)).strip()
            continue
        if cur_letter is None:
            stem_lines.append(line)
        # else: stray blank/trailing line after options — dropped intentionally

    stem = "\n".join(stem_lines).strip("\n")
    opts = [{"letter": l, "text": t} for l, t in options]
    return meta, stem, opts


def parse_batch_file(path: Path, course_dir: Path):
    text = path.read_text(encoding="utf-8")
    fm, rest = parse_frontmatter(text)

    heading_matches = list(ID_HEADING_RE.finditer(rest))
    questions = []
    for idx, hm in enumerate(heading_matches):
        qid = hm.group(1)
        start = hm.end()
        end = heading_matches[idx + 1].start() if idx + 1 < len(heading_matches) else len(rest)
        block = rest[start:end]
        meta, stem, options = parse_question_block(qid, block)

        img_field = meta.get("img", "")
        images = []
        if img_field:
            for raw_path in img_field.split(","):
                raw_path = raw_path.strip()
                if not raw_path:
                    continue
                src = course_dir / raw_path
                images.append(raw_path)

        q = {
            "id": qid,
            "status": meta.get("status", ""),
            "form": meta.get("form", "mcq"),
            "type": meta.get("type", ""),
            "stem": stem,
            "options": options,
            "answer": meta.get("answer", ""),
            "claimed": meta.get("claimed", ""),
            "basis": meta.get("basis", ""),
            "evidence": meta.get("evidence", ""),
            "note": meta.get("note", ""),
            "noteJobA": meta.get("note (job a)", ""),
            "seen": meta.get("seen", ""),
            "images": images,
        }
        questions.append(q)

    # --- self-check: parsed reality must match the frontmatter's own claim ---
    errors = []
    declared_n = int(fm.get("questions", -1))
    if declared_n != len(questions):
        errors.append(f"{path.name}: frontmatter says questions={declared_n}, parsed {len(questions)}")

    status_line = fm.get("verified", "") or fm.get("verified ", "")
    # status counts are on a line like "verified: 52 | conflict: 2 | ..."
    # find that line in the raw frontmatter text directly, since keys repeat "status"-ish words
    fm_block = re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)
    counts_line = next((l for l in fm_block.split("\n") if l.startswith("verified:")), None)
    if counts_line:
        declared_counts = {}
        for part in counts_line.split("|"):
            k, _, v = part.strip().partition(":")
            k = k.strip()
            v = v.strip()
            if k and v:
                declared_counts[k] = int(v)
        actual_counts = {}
        for q in questions:
            actual_counts[q["status"]] = actual_counts.get(q["status"], 0) + 1
        for k, v in declared_counts.items():
            if actual_counts.get(k, 0) != v:
                errors.append(
                    f"{path.name}: frontmatter says {k}={v}, parsed {actual_counts.get(k, 0)}"
                )
        for k, v in actual_counts.items():
            if k not in declared_counts:
                errors.append(f"{path.name}: parsed status '{k}'={v} not declared in frontmatter at all")

    if errors:
        for e in errors:
            print("BUILD FAILED:", e, file=sys.stderr)
        sys.exit(1)

    return {
        "course": fm.get("course", ""),
        "tab": fm.get("tab", ""),
        "batch": fm.get("batch", ""),
        "built": fm.get("built", ""),
        "questions_count": declared_n,
        "complete": fm.get("complete", "true") == "true",
        "covers": fm.get("covers", ""),
        "source": fm.get("source", ""),
        "counts": actual_counts if counts_line else {},
        "questions": questions,
    }


def main():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)
    (DIST_DIR / "img").mkdir()

    courses = {}
    total_questions = 0

    out_files = sorted(COURSES_DIR.glob("*/out/*.md"))
    if not out_files:
        print("BUILD FAILED: no batch files found under courses/*/out/", file=sys.stderr)
        sys.exit(1)

    for batch_path in out_files:
        course_dir = batch_path.parent.parent
        batch = parse_batch_file(batch_path, course_dir)
        course_id = batch["course"]
        tab_id = batch["tab"]
        total_questions += len(batch["questions"])

        # copy every referenced image once, rewriting question["images"] to
        # dist-relative paths
        img_out_dir = DIST_DIR / "img" / course_id
        img_out_dir.mkdir(parents=True, exist_ok=True)
        for q in batch["questions"]:
            rewritten = []
            for rel in q["images"]:
                src = course_dir / rel
                if not src.exists():
                    print(f"BUILD FAILED: {batch_path.name} {q['id']} references missing image {src}", file=sys.stderr)
                    sys.exit(1)
                dest_name = Path(rel).name
                dest = img_out_dir / dest_name
                if not dest.exists():
                    shutil.copy2(src, dest)
                rewritten.append(f"img/{course_id}/{dest_name}")
            q["images"] = rewritten

        courses.setdefault(course_id, {"id": course_id, "tabs": {}})
        courses[course_id]["tabs"].setdefault(tab_id, []).append(batch)

    # flatten tabs: merge batches within a tab (site-level accumulation,
    # per job-d-build.md — "cross-batch duplicate merging happens there, not
    # in the pipeline"; v1 just concatenates, since no tab has >1 batch yet)
    data = {"courses": []}
    for course_id, cdata in sorted(courses.items()):
        tabs_out = []
        for tab_id, batches in sorted(cdata["tabs"].items()):
            all_questions = []
            for b in batches:
                all_questions.extend(b["questions"])
            tabs_out.append({
                "id": tab_id,
                "batches": [
                    {k: v for k, v in b.items() if k != "questions"} for b in batches
                ],
                "complete": all(b["complete"] for b in batches),
                "covers": next((b["covers"] for b in batches if b["covers"]), ""),
                "counts": {
                    status: sum(b["counts"].get(status, 0) for b in batches)
                    for status in set().union(*(b["counts"].keys() for b in batches))
                },
                "questions": all_questions,
            })
        data["courses"].append({"id": course_id, "tabs": tabs_out})

    (DIST_DIR / "data.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    for asset in ("index.html", "app.js", "app.css"):
        shutil.copy2(Path(__file__).parent / asset, DIST_DIR / asset)

    print(f"Built {DIST_DIR}/data.json — {len(out_files)} batch file(s), {total_questions} questions total.")
    for course in data["courses"]:
        for tab in course["tabs"]:
            print(f"  {course['id']}/{tab['id']}: {len(tab['questions'])} questions, complete={tab['complete']}")


if __name__ == "__main__":
    main()
