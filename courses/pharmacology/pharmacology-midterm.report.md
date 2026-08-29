# pharmacology / midterm — 153 questions

verified 148 · conflict 2 · external 3 · not-in-source 0 · needs-eye 0

**Two tiers, two very different verification jobs.** Batch 01 (PHARM-M-001–049,
the 2023 reshuffled-model exam) is all claimed tier — every one of those 49 was
independently re-derived from `source.md` before the circulating claim was even
looked at, per Job C's "answer first" rule. Batch 02 (PHARM-M-050–153, the 2022
and 2018 exams) is 102 official-tier questions from printed answer keys, passed
through untouched per Job C's own rules — those cost nothing here, no source
lookup performed, no independent re-derivation. The two open/needs-eye questions
Job A couldn't resolve (illegible or ambiguous key cells) got the full
independent-verification treatment instead, same as any claimed question — see
below.

**Conflicts (2)** — the circulating claims are wrong on both; source wins:

- **PHARM-M-023** — claimed "All of them" (elimination rate constant, peak
  concentration, and AUC together determine relative bioavailability); the
  source ties bioavailability specifically and only to the AUC ratio
  (`BA = AUC_po / AUC_iv × 100`) — elimination rate constant and peak
  concentration are never part of that comparison → AUCs alone.
- **PHARM-M-039** — claimed "Orally" is the desirable route for an emergency
  antidote after acute overdose; the source names IV specifically for
  "circumstances requiring rapid onset," and oral is comparatively slow →
  IV.

**External (3)** — settled facts the slides don't happen to state:

- **PHARM-M-021** — nonlinear (saturation) kinetics causing the apparent
  half-life to lengthen as dose increases; the source only names that
  zero-order kinetics exists (aspirin at high doses) without detailing the
  property.
- **PHARM-M-022** — the maintenance-dose formula (Css × CL / F); the source
  gives the paired loading-dose formula (Vd × Css / F) but not this one.
- **PHARM-M-147** — "physiological (functional) antagonist"; Ch. 3 defines
  competitive/noncompetitive antagonism and inverse agonists but never this
  term. This was one of Job A's two open/needs-eye questions (smudged key,
  read as b or c) — resolved here from standard pharmacology (physiological
  antagonism = two agonists on different receptors with opposing effects),
  which lands on c and settles the smudge in its favor.

**The other open/needs-eye question resolved to `verified`, not `external`:**
**PHARM-M-133** (the illegible-key clearance calculation) came back clean —
independently computing CL = 0.69 × Vd / t½ from the source's own half-life
formula, using the question's own numbers, lands exactly on option c) 0.43 L/h.
Job A was right not to guess; Job C didn't need to.

**Two disputes from Job A, both resolved with a clear winner:**

- **PHARM-M-015** (enteric-coated drug: which pH sensitivity, absorbed where)
  — models 1 and 2 both claimed "Acidic; Small intestine" (different letters,
  same content); model 3 claimed "Acidic; Stomach." The source's own
  description of enteric coating — protects the drug from stomach acid so it
  can dissolve in the intestine — confirms models 1/2 and contradicts model 3.
- **PHARM-M-035** (what increases Vd) — model 2 claimed "high plasma protein
  binding," model 3 claimed "high tissue protein binding." The source is
  explicit that plasma binding traps a drug in the small plasma compartment
  (shrinking Vd), while tissue binding is what enlarges the apparent Vd —
  model 3 confirmed, model 2 wrong.

**Graph-dependent questions** — three in batch 01 (PHARM-M-008 digoxin
therapeutic window, PHARM-M-029 nephron reabsorption site, PHARM-M-042
ceftriaxone dosing curve) were verified by reading the actual figure in
`flagged/` alongside the matching source section, not by trusting the claim at
face value. Five more in batch 02 (PHARM-M-121, 138, 150, 151, 153) are
official tier with the answer already known from the printed key, but still
got a `flagged/` crop per the img: rule since the graph is what the question is
actually asking about.

**Two small, deliberately-preserved oddities carried through from Job A,
neither corrected:**

- **PHARM-M-072** — option d) is a literal fragment duplicating the tail of
  option c)'s text (a typesetting glitch in the original 2022 exam), kept
  exactly as printed.
- **PHARM-M-104** — the official answer is "Sugar coated tablet" for
  "sustained drug delivery with prolonged duration of action," which reads
  oddly against "Transdermal patches" sitting right there as another option.
  Both the printed key and the student's own pen circle on the source page
  independently agree on it, so it's kept as printed rather than second-
  guessed.

**Chapter coverage** — Ch. 2 (Pharmacokinetics) overwhelmingly heaviest — this
tab is almost entirely PK principles and calculations. Ch. 1 (Introduction:
routes, first-pass, prescription basics) and Ch. 3 (Pharmacodynamics:
receptors, agonism/antagonism, dose-response) both get solid coverage. Ch. 4–8
(the antimicrobial-specific chapters) are essentially untouched — this exam
tests general pharmacology principles, not drug-class detail; only
PHARM-M-010 (chloramphenicol/neonates) brushes a named drug, and even that
resolves from Ch. 2's general metabolism section rather than Ch. 5's
chloramphenicol-specific one.

---

Full per-question resolutions: [pharmacology-midterm.verify.md](pharmacology-midterm.verify.md)
