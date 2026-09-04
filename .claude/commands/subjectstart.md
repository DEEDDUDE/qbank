---
description: Survey a course's raw material in downloads/, sort it into courses/<course>/, and plan RUN-PLAN.md rows. Plans only — runs no pipeline jobs.
argument-hint: <course>
---

Read `CLAUDE.md` at the repo root first, plus `RUN-PLAN.md`. The course slug is
`$1` — it must be one of: `microbiology`, `pharmacology`, `public-health`,
`molecular-genetics`, `metabolic-biochem`, `pathology`. If `$1` is missing or
not one of these, stop and ask.

This command does three things, in order. **It is read-only survey and planning
until step 2's move — no Job A/B/C/D pipeline work runs here.**

## Step 1 — Survey

Find this course's material under `downloads/`. It won't be filed under the
slug — match by subject name (e.g. `pharmacology` → a folder literally named
something like `General Pharmacology`; `molecular-genetics` → `Molecular
Biology & Genetics`). Search all of `downloads/`, not just one year/semester
folder — don't assume the current layout (`2nd Year/1st Semester/...`) is the
only place a course's material will ever land. If you find more than one
plausible folder, or none, stop and show the user what you found instead of
guessing.

For everything under that folder, report:

- File and page counts (use `scripts/prep.py`'s text-layer detection where it
  applies — don't render pages into context just to count them)
- Text-layer vs. scan-only vs. photo, per file or per batch
- Duplicates (same content, different filename/export) — Arabic filenames from
  Drive zips often arrive mangled (`#U0646...`); repair the encoding before
  comparing, don't rename by hand
- Distinct sittings/exam instances (same course, different sessions — quizzes
  vs. midterm vs. finals vs. practice/worksheets vs. lab)
- Rough question count per sitting, if it's skimmable without deep reading
- Slide/lecture material, separate from exam captures
- Anything that's neither slides nor a captured exam (announcements, syllabi,
  admin PDFs) — flag it, don't silently drop it or silently file it
- Any exam page where an image looks like it's part of the question itself
  (a zone-of-inhibition photo, a stained slide, a labeled diagram the student
  has to read) — these will need Job A's vision path later, flag them now so
  the later session isn't surprised

## Step 2 — Sort

Based on the survey, propose a move plan: which files go to
`courses/<course>/raw/<tab>/` (tab = quizzes / midterm / finals / microlab /
practice — infer tab from what the sitting actually is) and which go to
`courses/<course>/slides/`. **Show the full plan and get the user's agreement
before moving anything.** Once agreed, move the files (git mv if already
tracked, otherwise a plain move — `raw/` and `slides/` are gitignored per
CLAUDE.md, so these moves are local, not commits).

## Step 3 — Plan RUN-PLAN.md

Replace this course's single `todo` sort row in `RUN-PLAN.md` with real session
rows, following the same shape as the microbiology table: one row per Job
A/B/C/D session, `Target` naming the actual folder or file, `Size` from the
real counts you just gathered, `Status: todo`, and a `Note` with anything a
future session should know before starting (e.g. "answer key present", "no
official key, all claimed-tier").

**Split any single Job A session over ~60 vision pages into multiple rows** —
this mirrors the real cost driver called out in CLAUDE.md ("cost tracks
conversation length, not page count"): a session that reads more than that in
one sitting is doing Job A work at a worse rate than starting fresh. Job B
(source) is normally one row unless the slide deck is unusually large. Job C
and D rows can wait until their upstream A/B rows are done — write them in as
`todo` with `Target: TBD` if you don't yet know the batch size, and fill it in
when you get there.

Do not run any of these rows now. Report the updated table to the user and
stop.
