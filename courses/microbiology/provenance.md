# microbiology — provenance

How `raw/` and `slides/` map back to the original `microbiology/` folder as it arrived
from Google Drive, and what a folder name alone no longer tells you. `raw/` and `slides/`
are gitignored, so this file is the only committed record of any of it.

Subfolder structure was preserved under each tab rather than flattened — several source
folders reuse filenames (`1.jpg`, `2.jpg`, `11.jpg`–`20.jpg`), and a flat copy would have
silently overwritten files.

## raw/quizzes/ — 29 files

- `2022-2023-Quiz/` ← `Previuos Exams/2022-2023/Quiz/` — 27 Moodle jpg captures.
- `2023-2024-Quizzes/` ← `Previuos Exams/2023-2024/Quizzes/` — 2 image-only PDFs
  (Pathogenesis Quiz, Virology Quiz).

## raw/midterm/ — 101 files

- `2022-2023-Midterm/`, `2023-2024-Midterm/` — as named.
- `before2020-dina/`, `before2020-murad/` ← `Before 2020/midterm/dina|مراد/`.
- `MICRO-EXAMS-murad/` ← `Before 2020/MICRO EXAMS murad/`. **Placement inferred, not
  labelled.** This folder sat at the top level of `Before 2020/` with no tab name. Its
  files are byte-identical (sha1) to files already filed under
  `Before 2020/midterm/مراد/` — `1.jpg`, `2.jpg`, `micro second/1–6.jpg`,
  `exam-A2015.pdf`, `micro exam.doc` all match. Filed as midterm on that evidence.
- `Unknown-Midterm-Micro/` ← `Previuos Exams/Unknown/Midterm Micro/`. 32 images, one
  question per image, already tightly cropped, each carrying a **printed** `ANSWER:`
  line — this is the cheapest, highest-confidence material in the whole pile (tier
  `official`, no vision recovery, no page stitching needed). Year/exam model unknown —
  hence the original "Unknown" label — but the content is unambiguously midterm-style
  single questions, not a comprehensive final.

## raw/finals/ — 249 files

- `2020-2021-Final/`, `2023-2024-Finals/` — as named. `2023-2024-Finals/` holds both
  Dentistry and Medicine exam models (`نموذج 1`, `نموذج 3`, `نموذج 4`, `نموذج ٥`, `نموذج ٦`)
  — different exam models for different programs, same final.
- `before2020-MICRO-FINAL/` ← `Before 2020/MICRO FINAL/` — largest single pile (132
  files), itself a nest of per-student folders (Micro, Microbiology 1–4, dina 1st 2nd
  final, etc.) kept intact.
- `before2020-2018-course/` ← `Before 2020/2018/course/`. **Placement inferred.** Labelled
  only "course", not by exam type. Filed as finals because `Before 2020/2018/Lab/` sits
  as its sibling and is unambiguously lab material — "course" is read as the
  lecture-course counterpart, i.e. the main exam, not the lab exam. Not confirmed by
  content; worth a second look during Job A if the material reads as midterm-length
  rather than final-length.
- `before2020-resit-ekmal/` ← `Before 2020/اكمال/` (14 files) — a **resit/makeup exam**
  ("اكمال" = completion/resit), not a first-sitting final. Filed under finals per your
  instruction, noted here as a resit.
- `before2020-resit-2017/` ← `Before 2020/Reset 2017/` (16 files) — also a **resit**. The
  folder name is misleading: the screenshots' own header reads `اكمال-2017`, matching the
  folder above rather than describing a "reset" of anything. One screenshot is captioned
  "7 of 17" while the folder holds only 16 files total — **a page may be missing** from
  this document. Flag for Job A's count-reconciliation check.
- `Unknown-Final-Micro/` ← `Previuos Exams/Unknown/Final Micro/` (39 files) — year and
  exam model unknown, content reads as final-length (comprehensive, sterilization through
  mycology).

## raw/microlab/ — 12 files

A fourth tab, added because Lab is taught and examined separately from the lecture
course. `2023-2024-Finals/Dentistry|Medicine`, `Quizzes-2022/`, `Quizzes-2023/`, and
`before2020-2018-Lab/` ← `Before 2020/2018/Lab/`. IDs on this tab use `MICRO-LAB-NNN`,
and it routes to `source.lab.index.md` first, falling back to `source.index.md` when the
lab index has no supporting chapter — see CLAUDE.md's Routing entry.

**Renamed from `raw/lab/`.** A folder appeared at the repo root as `microlab/`, meant as
a fourth tab of lab captures. All 10 of its files were byte-identical (sha1) to files
already here — this tab already existed under the name `lab`, just not the name asked
for. Since nothing had been extracted yet (no `out/`, no `.ledger.json`), the tab was
renamed to `microlab` rather than duplicated: the two extra files this tab already held
(`before2020-2018-Lab/`, absent from the root drop) were kept, and the redundant root
copy was deleted after a hash-by-hash check confirmed every one of its files was already
present here. If another copy of this material surfaces again, check hashes against this
tab before assuming it's new — it likely isn't.

## raw/practice/ — 8 files

Question-bearing material that was never sat as one of your own exams. Kept off the
`quizzes`/`midterm`/`finals` tabs on purpose, so it is never mistaken for a past paper
during verification or study.

- `External-MCQ_S/` ← `2023-2024/External MCQ_S/` — 3 PDFs from an external MCQ bank.
  These do carry real text layers (confirmed: `Virology.pdf` = 9,553 chars over 10 pages),
  so they cost nothing to extract even though they aren't a past paper.
- `Worksheets/` ← 4 of the 5 files in `Worksheets/Worksheets and others/` — the
  professor's own practice worksheets. (The 5th file, `2-2-Pictures - Bacterial Cell.pdf`,
  is figures rather than worksheet questions and went to `slides/` instead.)
- `student-predictions/Short Essay Q_s- Odi.docx` ← `2022-2023/`. Title in full:
  *"SHORT ESSAY POSSIBLE MIDTERM Q's — By Odi Sec1 Repre"*. A student representative's
  **predicted** questions, not a real exam. Filing this as a past midterm would be
  exactly the failure this project exists to prevent.

Not moved anywhere: `Before 2020/midterm/مراد/Micro test bank for murad مهم.docx`. Opened
and checked — it contains no questions, only a hyperlink to indiabix.com. Left with the
rest of its folder in `raw/midterm/before2020-murad/`; Job A will find it empty on read.

## slides/ — 61 files

- `2023-slides/`, `2024-slides/` ← `Slides/2023 slides|2024 Slides/`.
- `previous-slides/` ← `Slides/Previous slides/` (Dr. Ibrahim's and Dr. Murad's decks,
  kept as their own subtrees).
- `MicroLab-Slides-inner/` ← `MicroLab Slides/`.
- `bacteria-table/` ← `Microbiology bacteria -الجدول المعتمد للحفظ_/`. Its `Flow Chart.pdf`
  is byte-identical (sha1) to the flagged `Summaries/Bacterial Classification .pdf` —
  only this copy was kept in the pipeline; the flagged one is a duplicate, not a
  different document.
- `Outline/Course outline 2023_2024.pdf`.
- `2-2-Pictures - Bacterial Cell.pdf` ← pulled out of `Worksheets/Worksheets and others/`
  as source figures rather than a worksheet.

**Four generations of the same lecture deck exist**: 2024, 2023, Dr. Ibrahim, Dr. Murad —
all covering the same numbered lectures under different names. Job B needs to pick ONE
as the spine for `source.md`, or it will produce duplicate chapters. Not decided here —
flagging for Job B. Candidate: 2023 is the only complete set (lectures 1–10); 2024 is
newer but is missing Sterilization and Parasitology.

## Left in place, NOT moved — 30 files, ~1.29 GB

Still sitting in `microbiology/slides and other stuff/`, pending a decision:

- `Textbooks/` — Sherris 7th Ed., BRS 6th Ed. (147 MB). Third-party textbooks, not your
  lecturer's material — including them in `source.md` risks answering questions your
  exam never asked.
- `Public_Health___Microbiology_-_3rd_Ed.pdf` (18 MB) — a textbook, and `public-health`
  is a separate course in `CLAUDE.md`. Wrong course folder regardless of the textbook
  question.
- `Summaries/` (~1.13 GB: Noor Khuffash 18 files, Dr. Dina 4, Lab Summaries 4, Bacterial
  Classification 1) — student-written summaries. Hard rule 4 (`CLAUDE.md`) says the
  source outranks the students; if these became part of `source.md`, a student's notes
  would become the authority Job C verifies claimed answers against, which inverts the
  whole point of Job C. Also expensive to process: one file alone is 355 MB, and Dr.
  Dina's summaries are image-only scans needing OCR throughout.

## Reconciliation

395 exam files + 95 slide files = 490 originally.
399 raw/ (395 exam files + 4 worksheets that carry questions) + 61 slides/ + 30 flagged
= 490. Every file accounted for — none renamed, none deleted.
