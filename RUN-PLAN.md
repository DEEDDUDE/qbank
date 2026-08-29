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
| 6 | C+D | quizzes verify **and** build `out/pharmacology-quizzes-01.md` | TBD, small | done | 63 Q, 52 verified · 2 conflict · 7 external · 1 not-in-source · 1 needs-eye, committed. RUN-PLAN row 5's own "official tier" assumption stayed wrong all the way through — 0 official in the final build, matching what row 5 already found. Both conflicts (PHARM-Q-038, 043) are real: circulating claims contradicted by the source's own penicillin classification. 3 of Job A's disputed questions all resolved cleanly to a source-backed answer (none stayed disputed in the output). 2 of the 3 open-tier graph questions were answered directly from their figure (never claimed by any capture); the third's late claim was independently confirmed by calculating from the figure rather than trusted at face value. **Also created `courses/pharmacology/.ledger.json`, which never existed before this row** — row 2's practice-tab extraction was never ledgered either; worth a follow-up check before that tab's own C+D row (13-14) runs, though it isn't blocking |
| 7 | A | `raw/midterm/2023/` — نموذج ١، ٢، ٣ | 49 vision pages | done | 49 Q extracted (PHARM-M-001–049) → `pharmacology-midterm.extract.md`, all claimed tier (no key anywhere). Treated as reshuffled models of one exam: 30 of 49 questions confirmed across 2-3 models (same stem, same claimed answer), 19 single-model. Model 1's photos are consistently cut off at the right edge — every truncated stem/option was fully recovered by cross-matching models 2/3's full-width screenshots, so 0 needs-eye. 2 genuinely disputed (different models' students picked different answers to the same question): PHARM-M-015 (enteric-coated drug pH/absorption site, 2-vs-1) and PHARM-M-035 (what increases Vd, 1-vs-1). 3 graph-dependent questions, crops saved to `flagged/` |
| 8 | A | `raw/midterm/2018/` + `raw/midterm/2022 (الاجابات صحيحة)/` | 22 vision pages | done | 104 Q extracted (PHARM-M-050–153) → `pharmacology-midterm.extract.md`, both batches tier official. **This row's own pre-flight badly undersold the material**: the "22 vision pages, below-floor 2018 photos" framing suggested a small, partly-unreadable haul — instead every page was legible and both folders turned out to hold full printed answer keys (2022: 50 Q, Nov 2022 Al-Quds midterm; 2018: 54 of 60 Q from a Nov 2018 Al-Quds midterm, Q19–24 never photographed in this raw set — a genuine source gap, not a loss here). 102 official, 2 open/`needs-eye` (one key cell is illegible arithmetic scratch, PHARM-M-133; one is a smudged B-vs-C letter, PHARM-M-147 — both crops in `flagged/`). 5 more questions have an answer-bearing graph in the stem, cropped to `flagged/` per the img: rule even though already answered from the key. One answer (PHARM-M-104, "sugar coated tablet" for sustained delivery) reads oddly against its own option list but is confirmed by both the printed key and the student's own circle on the source page — kept as printed, not corrected. All answers cross-verified against the exam's own pharmacology logic before writing; a first draft had a copy-paste slip on PHARM-M-073 caught and fixed during review. Nothing committed to the ledger yet — that happens at row 9 (Job C+D) |
| 9 | C+D | midterm verify **and** build `out/pharmacology-midterm-01.md` | 153 Q | done | 153 Q, 148 verified · 2 conflict · 3 external · 0 not-in-source · 0 needs-eye, committed. The 102 official-tier questions (batch 02) passed through untouched per Job C's own rule — no source lookup spent on those. The 49 claimed-tier questions (batch 01) plus both of Job A's open/`needs-eye` questions got full independent verification: PHARM-M-133's illegible-key clearance question resolved cleanly to `verified` (independently computing CL from the source's own half-life formula lands exactly on option c); PHARM-M-147's smudged-key physiological-antagonist question resolved to `external` (the term isn't in `source.md` at all — standard pharmacology settles the smudge in favor of c over b). 2 real conflicts: PHARM-M-023 (bioavailability comparison is AUC-only per source, not "all of them") and PHARM-M-039 (IV, not oral, is the source-backed antidote route for acute overdose). Both of batch 01's disputed questions resolved with a clear source-backed winner (PHARM-M-015, PHARM-M-035). Ch. 2 (Pharmacokinetics) dominates chapter coverage; Ch. 4–8 (antimicrobial-specific) essentially untested — this exam is general-principles/PK-calculation heavy. `pharmacology-midterm.report.md` + `.verify.md` written; `.ledger.json` gained a `midterm-01` batch entry covering the 22 batch-02 raw files (batch 01's 2023 files were already ledgered at extraction) |
| 10 | A | practice bank p47–66 | 96 Q extracted (PHARM-P-175–270) | done | Row's own "No answers in either" turned out wrong for both halves — same kind of survey miss as rows 2, 5, 8. "Pharmacology TEST BANK" (p47–59, Ola Nwafleh & Hamza Ja'areh): 45 Q, numbered `1.`–`45.`, no inline answers but a printed key spans p57-59 covering all 45 → tier official. Q12 is a two-part question keyed "(A) C (B) A" off one four-drug graph, split into two `qa` entries (PHARM-P-186/187) sharing one flagged image rather than inventing mcq options. Dental students 2022/2023 (p60–66, Dr. Abdulraheem Jabr): 50 Q, numbered `1)`–`50)`, no inline answers but a printed key at p66 covering every question except #24 (genuinely blank in the source's own key) → 49 official, 1 open. 4 embedded graphs load-bearing, saved to `flagged/` |
| 11 | A | practice bank p67–115 | 138 Q extracted (PHARM-P-271–408) | done | "Pharma020" section, credited to Mohanad Al-ahmad (p115). Two separately-numbered lists, both restarting at 1: "Intro & Pharmacodynamics" (p68-75, 28 Q, inline `ans:`/`Ans:`, tier claimed except 5 genuinely unanswered — #23-27 — left open) and "Pharmacokinetics" (p76-115, 110 Q, inline `Answer:`, tier claimed throughout — student-compiled, not an instructor key). Q1 of the second list is a match-the-following question, rendered as one `qa` entry rather than invented mcq options; Q11 has a malformed option (e) ("e) Answer: A" with no option text of its own) transcribed blank rather than filled in. 4 embedded graphs load-bearing (clinical-vignette PK questions), saved to `flagged/`. Off-syllabus material (adrenergics, morphine, anaesthesia, insulin, aspirin) extracted as-is per plan — Job C will decide what routes |
| 12 | A | practice bank p116–134 | 73 Q extracted (PHARM-P-409–481) | done | Credited to Mohanad Al-ahmad (p134) — same author as row 11's second list, a separate compiled set. Numbered `1)`–`74)`, inline `ANS:`, tier claimed throughout. One real gap: #6 never appears in the source (numbering jumps 5→7, confirmed against the raw page, not a Job A drop) — no PHARM-P entry for it. Q8 is answered entirely from a photo ("This picture represent which Route?" — an intradermal-injection wheal), saved to `flagged/` |
| 13 | C | practice verify | 481 Q (rows 2, 10, 11, 12 combined) | doing | **Two sessions done, row 2's whole batch now finished.** Session 1: PHARM-P-001–099 (Fawzi/Malik's open-tier set) — 93 verified, 6 external, 0 conflict. Session 2 (this one): PHARM-P-100–174 (Rama/Sana's claimed-tier set) — 55 verified, 10 external, 0 conflict, 10 not-in-source (six off-syllabus autonomic-pharmacology questions, PHARM-P-123–125/127–129, plus PHARM-P-101/106/141/169). **Zero conflicts across all 75 claimed questions checked this session** — unlike the midterm tab's batch 01 (2 conflicts in 49). Combined so far: PHARM-P-001–174, 148 verified · 16 external · 0 conflict · 10 not-in-source · 0 needs-eye. Two graph questions (PHARM-P-104, PHARM-P-122) confirmed from their figures. Written to `pharmacology-practice.verify.md` + `.report.md` (both updated in place, `scope:` field still marks this as partial). **Resume at PHARM-P-175** — rows 10–11's material (PHARM-P-175–408: TEST BANK, dental students, Pharma020), then row 12's (PHARM-P-409–481). **A meaningful chunk will not route to `source.md`** — rows 10 and 11 carry material this course never taught (off-syllabus autonomics, opioids, adrenergics, morphine, anaesthesia, insulin, aspirin). That is `not-in-source`, which is a real status, not a failure. Before defaulting to it, try `slides/_reference/Pharmacology___Toxicology_-_3rd_Ed..pdf` as an external authority → `external` tier, the way microbiology's finals batch resolved 7 |
| 14 | D | `out/pharmacology-practice-01.md` | 481 Q | todo | kept separate from #13 — the conversation is long by the time C finishes this many |
| 15 | A | `raw/finals/2020-2021/` (folders 1 + 2 + 3) | 55 vision pages after hash dedupe | todo | **three separate captures of one sitting** — a scanned pdf, a Messenger photo set, a camera roll. `prep.py` drops the 4 exact-hash dups inside folder `3`, but the cross-folder overlap is different bytes of the same pages: dedupe by stem, the way microbiology's نموذج 1/5 were reconciled |
| 16 | A | `raw/finals/2023-2024/Medicine/1.pdf` + `2.pdf` | 51 vision pages | todo | models 1 and 2 of 6 |
| 17 | A | `raw/finals/2023-2024/Medicine/3.pdf` + `6.pdf` | 52 vision pages | todo | |
| 18 | A | `raw/finals/2023-2024/Medicine/4.pdf` | 41 vision pages | todo | longest single model |
| 19 | A | `raw/finals/2023-2024/Medicine/5/` | 27 vision pages | todo | model 5 is a photo set, not a pdf |
| 20 | A | `raw/finals/2023-2024/Dentistry/` | 20 vision pages | todo | **different programme** — same course, dentistry sitting. Keep it, and tag it so it stays distinguishable from the Medicine models |
| 21 | C | finals verify | TBD, large | todo | expect heavy cross-model stem overlap from rows 15–20 |
| 22 | D | `out/pharmacology-finals-01.md` | TBD | todo | |

**Tab summary:** quizzes done (63 Q, see row 6) · midterm extraction done (153 Q,
rows 7-8; row 9's C+D still open) · practice tab extraction fully done (481 Q
total: 174 from row 2 + 307 from rows 10-12, all beating their own estimates —
row 10's "no answers in either" was wrong for both halves, matching the pattern
from rows 2, 5, 8). 368 vision pages across quizzes / midterm / finals · 357
canonical slide pages for Job B.

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
