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

IDs use the `PHARM` prefix — `PHARM-Q-001`, `PHARM-M-001`, `PHARM-F-001`,
`PHARM-P-001`. No `microlab` tab: this course has no lab material.

Every exam capture in this course is **image-only, zero text layer** — all 368
exam pages go through Job A's vision path. The practice bank is the exception and
is free. No question here depends on reading a photo, so no `flagged/` crops are
expected.

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `raw/` (4 tabs) + `slides/` | 159 files | done | surveyed and moved from `downloads/…/General Pharmacology/` |
| 2 | B | `slides/Slides/` — 8 numbered decks → `source.md` | 357p (279 text / 78 vision) | todo | the canonical, complete deck set. Skip `All slides.pdf` — it is those same 8 decks concatenated. Do **not** ingest `slides/_reference/`. `slides/2024 Slides/` and `slides/2023 slides/Dr.Afnan/` are duplicates/near-duplicates of this set — 3 files in `2024 Slides/` are zero-byte |
| 3 | B | gap-fill `source.md` from `slides/2023 slides/Dr.Hussain/` | 271p, 7 pdf | todo | only the 3 decks with no counterpart in the numbered set: `Cephalosporins`, `Infection site antibiotics`, `(7) Quinolone_Sulfonamides`. The other 4 restate topics row 2 already covers |
| 4 | A | `raw/quizzes/` — whole tab | 51 vision pages, 24 files | todo | confirmed by `prep.py` Stage 0. `2024 Quizzes/` (both files) and `Quiz(1).pdf` carry printed keys → official tier. `Quiz.pdf` and `Quiz(1).pdf` are two exports of one quiz; only `(1)` has the answers |
| 5 | C | quizzes verify | TBD | todo | depends on #2 |
| 6 | D | `out/pharmacology-quizzes-01.md` | TBD | todo | |
| 7 | A | `raw/midterm/2023/` — نموذج ١، ٢، ٣ | 49 vision pages | todo | no key; claimed/open tier throughout |
| 8 | A | `raw/midterm/2018/` + `raw/midterm/2022 (الاجابات صحيحة)/` | 22 vision pages | todo | 2022 has `Answers.jpg` → official. **2018 photos are 405–867 px, below `prep.py`'s 1000 px floor** — expect pages that can't be read; give those a status, never a guess |
| 9 | C | midterm verify | TBD | todo | |
| 10 | D | `out/pharmacology-midterm-01.md` | TBD | todo | |
| 11 | A | `raw/practice/Pharmacology PYQ and Bank Questions.pdf` p1–46 | ~121 Q, text layer (free) | todo | Fawzi/Malik section (p1–26) has no answers → open tier; Rama/Sana "PAST PAPER" (p27–46) has `Ans:` lines → claimed. **The text layer is OCR, not native** (`B.Faise`, `Phase!`, `(Va)` for Vd) — transcribe what the page says, don't correct drug names. Numbering is discontinuous in the source itself (53 sits between 5 and 6; 19–24 and 27 absent) — the continuity check will fire and that is not a dropped question |
| 12 | A | practice bank p47–66 | ~98 Q, free | todo | "Pharmacology TEST BANK" (p47–59) + dental students 2022/2023 (p60–66). No answers in either |
| 13 | A | practice bank p67–115 | ~139 Q, free | todo | "Pharma020" section — numbered `Q1)` not `1.`, answers present on only some |
| 14 | A | practice bank p116–134 | ~73 Q, free | todo | every question carries an `Ans:` line |
| 15 | C | practice verify | TBD | todo | ~430 Q across rows 11–14; likely needs splitting into 2–3 sessions |
| 16 | D | `out/pharmacology-practice-01.md` | TBD | todo | |
| 17 | A | `raw/finals/2020-2021/` (folders 1 + 2 + 3) | 55 vision pages after hash dedupe | todo | **three separate captures of one sitting** — a scanned pdf, a Messenger photo set, a camera roll. `prep.py` drops the 4 exact-hash dups inside folder `3`, but the cross-folder overlap is different bytes of the same pages: dedupe by stem, the way microbiology's نموذج 1/5 were reconciled |
| 18 | A | `raw/finals/2023-2024/Medicine/1.pdf` + `2.pdf` | 51 vision pages | todo | models 1 and 2 of 6 |
| 19 | A | `raw/finals/2023-2024/Medicine/3.pdf` + `6.pdf` | 52 vision pages | todo | |
| 20 | A | `raw/finals/2023-2024/Medicine/4.pdf` | 41 vision pages | todo | longest single model |
| 21 | A | `raw/finals/2023-2024/Medicine/5/` | 27 vision pages | todo | model 5 is a photo set, not a pdf |
| 22 | A | `raw/finals/2023-2024/Dentistry/` | 20 vision pages | todo | **different programme** — same course, dentistry sitting. Keep it, and tag it so it stays distinguishable from the Medicine models |
| 23 | C | finals verify | TBD | todo | expect heavy cross-model stem overlap from rows 17–22 |
| 24 | D | `out/pharmacology-finals-01.md` | TBD | todo | |

**Tab summary:** nothing extracted yet. 368 vision pages across quizzes / midterm /
finals · ~430 free text-layer questions in practice · 357 canonical slide pages for
Job B.

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

*File counts for the still-unsurveyed courses above are raw counts under
`downloads/`, not page counts — vision-page splitting only gets decided once
`/subjectstart` surveys the real material. Microbiology and pharmacology are past
that point and their `Size` columns are real page counts.
`downloads/1st Year/` currently has no files in either semester folder.*
