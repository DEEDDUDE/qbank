# RUN-PLAN

Single source of truth for what's done and what's next, across every course.
Every session starts by reading this file, does exactly one row, then updates
that row before ending (see CLAUDE.md → "Working style").

**Status values:** `todo` (not started) · `doing` (a session started it and
stopped early — resume this one before picking a new `todo` row) · `done`.

**Job column:** `A` extract · `B` source · `C` verify · `D` build. A `sort` row
is `/subjectstart`'s own read-only-survey-then-move step, not a pipeline job.

---

## microbiology

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `raw/` (all 5 tabs) + `slides/` | — | done | sorted from an earlier Drive export, pre-dates `/subjectstart` |
| 2 | B | `slides/` → `source.md` + `source.lab.md` | ~10 lecture PDFs/PPTX + lab manual | done | both source files + `source.index.md` + `source.lab.index.md` built |
| 3 | A | `raw/microlab/` | 12 files | done | 90 Q extracted → `microbiology-microlab.extract.md` |
| 4 | C | microlab verify | 90 Q | done | verified against `source.lab.md` |
| 5 | D | `out/microbiology-microlab-01.md` | 90 Q | done | 90 Q, 2 conflicts, committed |
| 6 | A | `raw/quizzes/` | 29 files | done | 54 Q extracted |
| 7 | C | quizzes verify | 54 Q | done | verified |
| 8 | D | `out/microbiology-quizzes-01.md` | 54 Q | done | 54 Q, 5 conflicts, committed |
| 9 | A | `raw/midterm/` | 101 files | done | 421 Q extracted. ~13 files (mostly `before2020-murad/فيرست مراد` and `مراد سكند` photos, one `.doc`) aren't referenced in `.ledger.json` — likely duplicates of already-processed murad photos, unconfirmed. Worth a quick check, not blocking. |
| 10 | C | midterm verify | 421 Q | done | verified |
| 11 | D | `out/microbiology-midterm-01.md` | 421 Q | done | 421 Q, 25 conflicts, committed |
| 12 | A | `raw/practice/` | 8 files | done | 244 Q extracted |
| 13 | C | practice verify | 244 Q | done | verified |
| 14 | D | `out/microbiology-practice-01.md` | 244 Q | done | 244 Q, 1 conflict, committed |
| 15 | A | `raw/finals/2023-2024-Finals/Medicine/` — نموذج ٥ (full) + نموذج 1 (Q1-16 of 50) | 2 of 5 models | done | 58 Q extracted (MICRO-F-001–058) |
| 16 | C | finals verify batch 01 | 58 Q | done | 50 verified, 1 conflict, 7 external |
| 17 | D | `out/microbiology-finals-01.md` | 58 Q | done | 58 Q, 1 conflict, committed. Header says `complete: false` — this is only a slice of the finals tab. |
| 18 | A | `raw/finals/2023-2024-Finals/Medicine/نموذج 1.pdf` — remainder, Q17-50 | 1 file (already read) | done | 34 more claims matched against extract.md: 16 matched existing نموذج ٥ entries by stem (now `models: [1,5]`), 18 are new (MICRO-F-059–076). Appended to `microbiology-finals.extract.md` (now 76 Q). **Not yet run through Job C or D.** |
| 19 | C | finals verify batch 02 — MICRO-F-059 through MICRO-F-076 | 18 Q | todo | |
| 20 | D | rebuild finals out file to include batch 02 | 76 Q total once done | todo | depends on #19 |
| 21 | A | `raw/finals/2023-2024-Finals/Medicine/نموذج 3.pdf` | 1 file | todo | one of the 3 remaining models of the 2023-2024 Medicine final (نموذج 2 was never captured) |
| 22 | A | `raw/finals/2023-2024-Finals/Medicine/نموذج 4.pdf` | 1 file | todo | |
| 23 | A | `raw/finals/2023-2024-Finals/Medicine/نموذج ٦.pdf` | 1 file | todo | |
| 24 | A | `raw/finals/before2020-MICRO-FINAL/` — part 1 | ~65 of 132 files (125 jpg + 1 pdf + 4 png + 2 txt total) | todo | split: over ~60 vision pages. Confirm actual page count with `prep.py` Stage 0 before committing to the split point. |
| 25 | A | `raw/finals/before2020-MICRO-FINAL/` — part 2 | remainder | todo | |
| 26 | A | `raw/finals/Unknown-Final-Micro/` | 39 jpg | todo | |
| 27 | A | `raw/finals/2020-2021-Final/` | 30 jpeg | todo | |
| 28 | A | `raw/finals/before2020-resit-2017/` | 16 jpg | todo | |
| 29 | A | `raw/finals/before2020-resit-ekmal/` | 14 jpeg | todo | |
| 30 | A | `raw/finals/before2020-2018-course/` | 12 jpg | todo | |
| 31 | C | finals verify — everything from rows 21-30 | TBD | todo | one session once all finals extraction lands; may need to split if large |
| 32 | D | rebuild finals out file, final pass | TBD | todo | last row for this tab — mark `complete: true` in the header when done |

**Tab summary:** quizzes done · midterm done · practice done · microlab done ·
finals in progress (58 of an unknown-but-large total committed; rows 19-32 remain).

---

## pharmacology

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `downloads/2nd Year/1st Semester/General Pharmacology/` (159 files, unsurveyed) | — | todo | run `/subjectstart pharmacology` |

## public-health

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `downloads/2nd Year/1st Semester/Public Health/` (97 files, unsurveyed) | — | todo | run `/subjectstart public-health` |

## molecular-genetics

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `downloads/2nd Year/1st Semester/Molecular Biology & Genetics/` (223 files, unsurveyed) | — | todo | run `/subjectstart molecular-genetics` |

## metabolic-biochem

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `downloads/2nd Year/1st Semester/Metabolic Biochemistry/` (376 files, unsurveyed) | — | todo | run `/subjectstart metabolic-biochem` |

## pathology

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `downloads/2nd Year/1st Semester/General Pathology/` (340 files, unsurveyed) | — | todo | run `/subjectstart pathology` |

---

*File counts above are raw counts under `downloads/`, not page counts — vision-page
splitting only gets decided once `/subjectstart` runs `prep.py` Stage 0 on real
material. `downloads/1st Year/` currently has no files in either semester folder.*
