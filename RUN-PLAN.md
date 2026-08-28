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
| 19 | C | finals verify batch 02 — MICRO-F-059 through MICRO-F-076 | 18 Q | done | all 18 verified, every claim correct — no conflicts, no external, no not-in-source. Ch.3 touched for the first time in this tab (MICRO-F-072) |
| 20 | D | rebuild finals out file to include batch 02 | 76 Q total once done | done | `out/microbiology-finals-01.md` now 76 Q, 68 verified · 1 conflict · 7 external, `complete: false` (still only نموذج 1 + ٥ of 5 models). Appended the 18 new MICRO-F-059–076 blocks and updated the 16 pre-existing entries whose `models:` grew to `[1,5]` (their `seen:` line now reads "model 1, model 5"). No new ledger entry needed — `finals-01`/`finals-02` already recorded both source files' hashes at extraction time. `report.md`/`verify.md` were already current for all 76 from row 19, untouched here |
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
finals in progress (76 of an unknown-but-large total committed — نموذج 1 and ٥
of 5 models; rows 21-32 remain).

---

## pharmacology

IDs use the `PHARM` prefix — `PHARM-Q-001`, `PHARM-M-001`, `PHARM-F-001`,
`PHARM-P-001`. No `microlab` tab: this course has no lab material.

Every exam capture in this course is **image-only, zero text layer** — all 368
exam pages go through Job A's vision path. The practice bank is the exception and
is free. No question here depends on reading a photo, so no `flagged/` crops are
expected.

**Why C and D pair up on some tabs and not others.** Job D writes
`out/<course>-<tab>-NN.md` — the tab is in the filename, so there is one D per tab
no matter what; they cannot be merged into a single end-of-course build. Job C is
split per tab for a different reason: it emits a verdict, a citation and often
generated options *per question*, and this course is heading for ~900–1100
questions. Microbiology's largest single C session was 421 Q — that is the
demonstrated ceiling, and one C row for all four tabs would be far past it. Where a
tab is small, C and D run in **one** session (rows 6, 9): Job D decides nothing that
C didn't already decide, so a separate D session only pays to re-read the file C
just wrote. Where a tab is large (practice, finals) they stay split, because by the
time C finishes those the conversation is long and that is the real cost driver.

| # | Job | Target | Size | Status | Note |
|---|-----|--------|------|--------|------|
| 1 | sort | `raw/` (4 tabs) + `slides/` | 159 files | done | surveyed and moved from `downloads/…/General Pharmacology/` |
| 2 | A | `raw/practice/Pharmacology PYQ and Bank Questions.pdf` p1–46 | 174 Q extracted (vs. ~121 estimated) | done | probe confirmed the OCR-text path works. **Real count beat the estimate by 53** — the original skim only caught Fawzi/Malik's 99 + Rama/Sana's 22 numbered "Midterm collected" questions; it missed a second, unnumbered "Final collected Questions" list (52 more) that a plain digit-prefix scan can't see. Also found a 174th question (PHARM-P-122) that exists only as an embedded image on p29 — invisible to any text-layer read, caught only by checking every page for embedded images. 3 of 5 embedded images turned out load-bearing and are saved to `flagged/`; 2 (a title-page photo, an untied decay graph) were decorative and discarded. 99 open-tier (Fawzi/Malik, no answers anywhere), 75 claimed-tier (Rama/Sana, `Ans:`/`ANSWER:`/`AMSWER:` lines). Output: `pharmacology-practice.extract.md` |
| 3 | B | `slides/Slides/` — 8 numbered decks → `source.md` | 357p (310 text / 47 vision, re-measured — beats the row's own 279/78 estimate) | done | `source.md` (8 chapters, `{#ch01}`–`{#ch08}`) + `source.index.md` built. All 47 vision pages read via `prep.py` patch mode, none illegible. 4 passages flagged in the source's own "Source gaps and flagged passages" section (an antagonist-definition inconsistency, two divergent cephalosporin-generation drug lists kept side by side, one empty "Linezolid: Mechanism of Action" slide, one likely-mistranscribed pancreatitis attribution) — none corrected, per hard rule 4 |
| 4 | B | gap-fill `source.md` from `slides/2023 slides/Dr.Hussain/` | 271p folder total; 81p actually ingested (66 text / 15 vision) across the 3 gap-fill decks | done | folded into Ch. 4 (new `{#ch04-4}` cephalosporin/carbapenem/vancomycin supplement, new `{#ch04-5}` antibiotic-selection-by-infection-site) and Ch. 6 (new `{#ch06-4}` quinolone/sulfonamide supplement + antiprotozoal/metronidazole, plus a note added to `{#ch06-3}`). `source.index.md` updated to match. All 15 vision pages readable. Two new flagged items (two CNS/skin-soft-tissue header-only slides; a nitrofurantoin adverse-effect-list discrepancy between the numbered deck and this one) added to source's own gaps section. The other 4 decks in this folder (`Antimicrobial 1`, `Pharmacodynamics`, `Protein Synthsis inhibitors`, `antifungal (1)`) were not ingested — confirmed as restating topics row 3 already covers |
| 5 | A | `raw/quizzes/` — whole tab | 51 vision pages, 24 files | done | 63 Q extracted (PHARM-Q-001–063) → `pharmacology-quizzes.extract.md`. **Both of this row's own pre-flight assumptions were wrong once the pages were opened**: `Quiz.pdf`/`Quiz(1).pdf` are two *different* quizzes (parenteral admin vs. antibiotic resistance), not two exports of one; and none of the four files carry a printed/official key — every capture in this tab shows plain Moodle "Answer saved" state, so tier is claimed/open throughout, zero official. The `Quiz 1`/`Quiz 2` raw folder names are also swapped relative to their actual Moodle quiz titles (folder "Quiz 1" ↔ real "Quiz 2" and vice versa) — noted in the extract's own header comment, not corrected in the folder names. Found 3 verbatim-duplicate question pools spanning otherwise-unrelated files (up to 3 independent sources agreeing on one question), merged into single entries. `نموذج ١`/`نموذج ٢` are not simple reshuffled models of one exam — model 2 is a much larger multi-reload capture of a shared bank, only partly overlapping model 1 — handled as ordinary stem-dedup, not the `models:` mechanism. 3 disputed (conflicting claims across attempts), 2 needs-eye. 8 crops saved to `flagged/` total: 6 graph/diagram-dependent questions plus the 2 needs-eye items' evidence. Nothing has been committed to the ledger yet — that happens at row 6 (Job D) |
| 6 | C+D | quizzes verify **and** build `out/pharmacology-quizzes-01.md` | TBD, small | todo | depends on #3. Small enough to verify and build in one session |
| 7 | A | `raw/midterm/2023/` — نموذج ١، ٢، ٣ | 49 vision pages | todo | no key; claimed/open tier throughout |
| 8 | A | `raw/midterm/2018/` + `raw/midterm/2022 (الاجابات صحيحة)/` | 22 vision pages | todo | 2022 has `Answers.jpg` → official. **2018 photos are 405–867 px, below `prep.py`'s 1000 px floor** — expect pages that can't be read; give those a status, never a guess |
| 9 | C+D | midterm verify **and** build `out/pharmacology-midterm-01.md` | TBD | todo | split into two rows if #7–8 land more than ~250 Q |
| 10 | A | practice bank p47–66 | ~98 Q, free | todo | "Pharmacology TEST BANK" (p47–59) + dental students 2022/2023 (p60–66). No answers in either. **p47–59 is partly off-syllabus** — autonomics, opioids, epinephrine — none of which the 8 canonical decks cover; expect `not-in-source` |
| 11 | A | practice bank p67–115 | ~139 Q, free | todo | "Pharma020" section — numbered `Q1)` not `1.`, answers present on only some. **The most off-syllabus section of the bank** — adrenergics, morphine, anaesthesia, insulin, aspirin all appear. Extract it all regardless; Job C decides what routes |
| 12 | A | practice bank p116–134 | ~73 Q, free | todo | every question carries an `Ans:` line. Cleanly on-syllabus |
| 13 | C | practice verify | ~430 Q | todo | **~150 of the 430 will not route to `source.md`** — rows 10 and 11 carry material this course never taught. That is `not-in-source`, which is a real status, not a failure. Before defaulting to it, try `slides/_reference/Pharmacology___Toxicology_-_3rd_Ed..pdf` as an external authority → `external` tier, the way microbiology's finals batch resolved 7. Likely needs splitting into 2–3 sessions |
| 14 | D | `out/pharmacology-practice-01.md` | ~430 Q | todo | kept separate from #13 — the conversation is long by the time C finishes this many |
| 15 | A | `raw/finals/2020-2021/` (folders 1 + 2 + 3) | 55 vision pages after hash dedupe | todo | **three separate captures of one sitting** — a scanned pdf, a Messenger photo set, a camera roll. `prep.py` drops the 4 exact-hash dups inside folder `3`, but the cross-folder overlap is different bytes of the same pages: dedupe by stem, the way microbiology's نموذج 1/5 were reconciled |
| 16 | A | `raw/finals/2023-2024/Medicine/1.pdf` + `2.pdf` | 51 vision pages | todo | models 1 and 2 of 6 |
| 17 | A | `raw/finals/2023-2024/Medicine/3.pdf` + `6.pdf` | 52 vision pages | todo | |
| 18 | A | `raw/finals/2023-2024/Medicine/4.pdf` | 41 vision pages | todo | longest single model |
| 19 | A | `raw/finals/2023-2024/Medicine/5/` | 27 vision pages | todo | model 5 is a photo set, not a pdf |
| 20 | A | `raw/finals/2023-2024/Dentistry/` | 20 vision pages | todo | **different programme** — same course, dentistry sitting. Keep it, and tag it so it stays distinguishable from the Medicine models |
| 21 | C | finals verify | TBD, large | todo | expect heavy cross-model stem overlap from rows 15–20 |
| 22 | D | `out/pharmacology-finals-01.md` | TBD | todo | |

**Tab summary:** practice p1–46 done (174 Q, see row 2 — beat its own estimate by
53; rows 10–12's "~98/~139/~73" estimates likely undercount the same way and
should be treated as floors, not ceilings). 368 vision pages across quizzes /
midterm / finals · 357 canonical slide pages for Job B.

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
