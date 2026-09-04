# pharmacology / practice — 481 questions (built)

> verified 362 · external 97 · conflict 8 · not-in-source 13 · needs-eye 1

RUN-PLAN rows 13 (verify) and 14 (build) are both done. `out/pharmacology-practice-01.md`
holds the whole tab in one batch — all four Job A extraction rounds (rows 2, 10,
11, 12) merged from a single source PDF, `Pharmacology PYQ and Bank Questions.pdf`
(134 pages, fully consumed), now recorded in `.ledger.json` for the first time
(it was never ledgered at extraction — see row 6's note).

**Conflicts (8)** — the circulating claims are wrong on each; source wins:

- **PHARM-P-272** — claimed the competitive-antagonism dose-response curve
  shifts left; the source's own diagram says right.
- **PHARM-P-274** — claimed tolerance increases therapeutic index; the
  source's tolerance definition (decreased response → need a higher dose)
  points to increased effective dose instead.
- **PHARM-P-353** — claimed oral drugs enter systemic circulation directly;
  directly contradicted by the source's first-pass description.
- **PHARM-P-364** and **PHARM-P-397** — both claimed "anaphylaxis" for a
  rapidly-diminishing-response phenomenon; the source's own tachyphylaxis
  definition fits, anaphylaxis doesn't. The same claim-vs-source pattern
  appearing twice, independently, in different parts of the bank.
- **PHARM-P-376** — claimed "conjugation" means drug reduction by enzymes;
  the source defines conjugation as coupling with an endogenous substrate
  (Phase II), not reduction (Phase I).
- **PHARM-P-414** — claimed neither IV nor rectal routes can be used in
  unconscious patients; the source explicitly lists rectal as "good for
  unconscious patients."
- **PHARM-P-433** — claimed loading dose is affected by clearance and
  maintenance dose by volume of distribution; the source's own formulas have
  it the other way around.

**Needs your eyes (1)** — **PHARM-P-271**: references "the figure below," but
no image was ever captured during Job A extraction — the only graph question
in this batch missing its crop. Left unresolved; a follow-up Job A patch
against the raw PDF (page range covering row 11's start, p67-75) could
recover it.

**Not in source (13)** — six off-syllabus autonomic-pharmacology questions
(alpha-blockers, dopamine, adrenergic receptor subtypes, muscarinic
receptors, atropine, pilocarpine — PHARM-P-123/124/125/127/128/129), plus
PHARM-P-101 (receptor up/down-regulation, undefined by the source, and a
qa-form item with no preserved option list to check against), PHARM-P-106
(a garbled, unparseable stem), PHARM-P-141 (nitrofurantoin terminology too
underspecified to judge), PHARM-P-169 (clinical misuse patterns not
discussed), PHARM-P-344 and PHARM-P-348 (numeric calculations that don't
reproduce any offered option under reasonable assumptions), and PHARM-P-460
(no offered option is a defensible true statement).

**A quiet extraction anomaly, not a verification failure:** PHARM-P-373's
claimed answer letter (e) doesn't correspond to any of its four listed
options (a-d) — flagged rather than force-matched, and answered
independently from the source instead.

**97 external-tier answers** lean on standard pharmacology this particular
`source.md` doesn't happen to state — pKa/ionization calculations
(Henderson-Hasselbalch), half-life and steady-state arithmetic, clinical
vignettes (drug overdose, geriatric dosing, neonatal PK), and a handful of
named-drug facts (ACE inhibitors, clinical trial phases) the 8-deck slide
source never covers. Six of these disagreed with their claim on outside
reasoning rather than literal source text (see PHARM-P-291, 309, 322, 323,
343 in `pharmacology-practice.verify.md` for the detail) — recorded as
`external` with the disagreement noted, not `conflict`, since source.md
itself is silent on each.

**Graph-dependent questions** — nine carry an `img:` crop: PHARM-P-104 (route
identification from a plasma-concentration curve shape), PHARM-P-122
(therapeutic-window/dose-response overlay), PHARM-P-177/179/180/181/186/187
(official-tier, six more dose-response and potency/efficacy figures from row
10's TEST BANK), and PHARM-P-403/405/406/408 (clinical-vignette PK curves
from row 11's Pharmacokinetics list). PHARM-P-271 is the tenth graph
question but has no crop — see needs-eye above.

**Chapter coverage across the whole tab** — heavily Ch. 1–3 (routes, PK
formulas, receptor pharmacology). Only row 2's Rama/Sana section
(PHARM-P-130–174) gives real Ch. 4–6 (antimicrobial) coverage; everything
else in this tab restates general principles and PK calculations, many of
them exact or near-exact duplicates of questions already seen on the
quizzes and midterm tabs (naproxen/ibuprofen potency, digoxin therapeutic
index, first-order half-life calculations) with different option lettering.

**Notable finds, not corrections:**
- PHARM-P-075/303 — a duplicated question missing the word "Low" in one
  option, recovered from the other copy's complete wording.
- PHARM-P-082, 091 — source-side formatting defects (a skipped option
  letter; a formula option truncated by a PDF page wrap).
- PHARM-P-094 — the compiler's own "not certain" Arabic annotation on what
  turned out, on verification, to be the correct answer.
- PHARM-P-309/420 — the same weak-base ionization calculation appears twice
  with different numbers; one claim has the ionized/nonionized fraction
  reversed (PHARM-P-309, recorded as external-with-disagreement), the other
  is correct (PHARM-P-420).

---

Full per-question resolutions: [pharmacology-practice.verify.md](pharmacology-practice.verify.md)
