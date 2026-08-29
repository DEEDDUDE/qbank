# pharmacology / practice — 481 questions (complete)

> verified 362 · external 97 · conflict 8 · not-in-source 13 · needs-eye 1

RUN-PLAN row 13 is done — this covers every question extracted across rows 2,
10, 11, and 12. Four sessions:

- **Session 1** (PHARM-P-001–099, open tier): 93 verified · 6 external.
- **Session 2** (PHARM-P-100–174, claimed tier): 55 verified · 10 external ·
  10 not-in-source · **0 conflict** across 75 claimed questions.
- **Session 3** (PHARM-P-175–270, 95 of 96 official tier): 96 verified at
  near-zero cost — passed through untouched per Job C's own rule.
- **Session 4** (PHARM-P-271–481, claimed tier, this session): 118 verified ·
  81 external · 3 not-in-source · 1 needs-eye · **8 conflict**.

**Conflicts (8), all in session 4** — the circulating claims are wrong on
each; source (or, where noted, standard pharmacology the source doesn't
literally state but the claim directly contradicts) wins:

- **PHARM-P-272** — claimed the competitive-antagonism dose-response curve
  shifts left; the source's own diagram says right.
- **PHARM-P-274** — claimed tolerance increases therapeutic index; the
  source's tolerance definition (decreased response → need a higher dose)
  points to increased *effective dose* instead.
- **PHARM-P-353** — claimed oral drugs enter systemic circulation directly;
  directly contradicted by the source's first-pass description.
- **PHARM-P-364** and **PHARM-P-397** — both claimed "anaphylaxis" for a
  rapidly-diminishing-response phenomenon; the source's own tachyphylaxis
  definition fits, anaphylaxis (an allergic reaction) doesn't. Same
  claim-vs-source pattern appearing twice independently.
- **PHARM-P-376** — claimed "conjugation" means drug reduction by enzymes;
  the source defines conjugation as coupling with an endogenous substrate
  (a Phase II reaction), not reduction (Phase I).
- **PHARM-P-414** — claimed neither IV nor rectal routes can be used in
  unconscious patients; the source explicitly lists rectal as "good for
  unconscious patients."
- **PHARM-P-433** — claimed loading dose is affected by clearance and
  maintenance dose by volume of distribution; the source's own formulas have
  it the other way around.

Six more numeric/clinical-reasoning items disagreed with their claim using
outside pharmacology knowledge rather than source.md itself (recorded as
`external` with the disagreement noted, not `conflict`, since the source
doesn't cover the specific fact): PHARM-P-291 (Kd vs. EC50 — the source
never defines Kd), PHARM-P-309 (a Henderson-Hasselbalch calculation where
the claim appears to have ionized/nonionized reversed), PHARM-P-322
(digoxin's Vd tracks lean body mass, not edema fluid), PHARM-P-323 (BBB
penetration difficulty is anatomical — absent pores — not explained by high
lipid solubility, which would ease penetration), PHARM-P-343 (a precise
half-life calculation matching option 3.3, not the claimed 3.0), and
PHARM-P-380 (a liver-cirrhosis/analgesic-overdose vignette pointing to
acetaminophen, directly listed as an option, when the claim picked "none of
the above").

**Needs-eye (1)** — **PHARM-P-271**: the stem references "the figure below"
but no image was captured during Job A extraction, unlike every other graph
question in this batch. Left unresolved; worth a follow-up Job A patch to
recover the missing figure from the raw PDF.

**Not in source (3)** — **PHARM-P-344** (a maintenance-dose calculation that
doesn't specify a dosing interval, so no reasonable assumption reproduces
any of the four options), **PHARM-P-348** (a hepatic-extraction-ratio
calculation whose independent recomputation, ER≈0.664, doesn't closely match
any option), **PHARM-P-460** (none of the offered "similarities" between
first-order and zero-order kinetics is actually true).

**Session 2's 10 not-in-source questions** (recapped from the prior report):
six off-syllabus autonomic-pharmacology questions (alpha-blockers, dopamine,
adrenergic receptor subtypes, muscarinic receptors, atropine, pilocarpine)
plus PHARM-P-101, 106, 141, 169 — see the session-2 notes in
`pharmacology-practice.verify.md` for detail.

**A quiet, useful cross-check:** two questions in this practice bank
(PHARM-P-373, "entirely microsomal") had a claimed answer letter (e) that
doesn't correspond to any of the four listed options (a-d) — flagged rather
than force-matched, and answered independently from the source instead.

**Graph-dependent questions in session 4** — nine total, four (PHARM-P-403,
405, 406, 408) from clinical-vignette figures. All confirmed from their
image except PHARM-P-271 (see needs-eye above): PHARM-P-403 (a
glucuronidation-rate saturation curve — the transition to zero-order
kinetics), PHARM-P-404 (aminoglycoside Vd, no image but tied to the drug
class's known charge properties), PHARM-P-405 (peak/trough levels at two
dosing intervals — more frequent dosing lowers peaks), PHARM-P-406 (neonate
vs. adult plasma levels — higher neonatal body water dilutes a hydrophilic
drug), PHARM-P-408 (two NSAID formulations — a later, broader peak signals
delayed absorption).

**Chapter coverage across the whole tab** — heavily Ch. 1-3 (routes, PK
formulas, receptor pharmacology) throughout sessions 1-2 and 4; session 3's
TEST BANK/dental sets stayed in the same territory. Session 2 was the one
stretch with real Ch. 4-6 (antimicrobial) coverage — sessions 1, 3, and 4
are almost entirely general-principles and PK-calculation questions, several
of them exact or near-exact duplicates of items already seen on the quizzes
and midterm tabs (naproxen/ibuprofen potency, digoxin therapeutic index,
first-order half-life calculations, and the like) restated with different
option lettering.

**Notable finds carried from earlier sessions:**
- PHARM-P-075/303 — a duplicated question missing the word "Low" in one
  option, recovered from the other copy's complete wording.
- PHARM-P-082, 091 — source-side formatting defects (skipped option letter;
  a formula option truncated by a PDF page wrap).
- PHARM-P-094 — the compiler's own "not certain" annotation on what turned
  out, on verification, to be the correct answer.

---

Full per-question resolutions: [pharmacology-practice.verify.md](pharmacology-practice.verify.md)
