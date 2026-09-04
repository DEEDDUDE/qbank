# pharmacology / finals — 234 questions

verified 208 · conflict 6 · external 15 · not-in-source 4 · needs-eye 1

Zero `official` tier in this tab (no printed answer key ever surfaced across the
2020-2021 sitting, the 6-model 2023-2024 Medicine sitting, or the Dentistry
sitting) — every question was either independently verified or answered from
outside knowledge, not passed through untouched.

---

## Conflicts — the circulating claims are wrong on these 6

| ID | Circulating claim | Source-supported answer | Why |
|---|---|---|---|
| PHARM-F-049 | b — "all cephalosporins cross BBB, usable for meningitis" | e — Cephalexin (the exception) | Only 3rd-gen cephalosporins achieve therapeutic CSF levels; cephalexin is 1st-gen. |
| PHARM-F-053 | "Moxifloxacin and ciprofloxacin" | Moxifloxacin alone | Ciprofloxacin is the most potent fluoroquinolone for UTI/*Pseudomonas* — the opposite of "ineffective in UTI." |
| PHARM-F-056 | Gentamycin | Trimethoprim | Job A's own note already flagged this claim as suspicious; gentamicin is a protein-synthesis inhibitor, unrelated to folate synthesis. |
| PHARM-F-061 | a — Staphylococcus aureus | c — Clostridium difficile | Clindamycin-associated colitis is explicitly attributed to *C. difficile* overgrowth. |
| PHARM-F-063 | c — Bioavailability | e — Elimination half-life | For an IV infusion, bioavailability isn't a variable (F=100%); time to steady state depends on t½. |
| PHARM-F-137 | b — True (fluconazole a classic strong CYP3A4 inhibitor) | a — False | Source's own inhibitor list names ketoconazole, not fluconazole. |

Several other questions (PHARM-F-025, PHARM-F-029, PHARM-F-031, PHARM-F-039,
PHARM-F-059, PHARM-F-107, PHARM-F-131) arrived as **disputed** input (two-or-more competing
claims from Job A) rather than a single wrong claim — those are resolved
in-place in the verify file with a `note:` explaining which side won, not
counted in the conflict tally above (per job-c-verify.md, a disputed question
that resolves to one of its own claims is `verified`, not `conflict`).

## Not in source — 4

- **PHARM-F-102** (Tmax independent of dose *and* bioavailability?) — a genuine
  PK nuance the source doesn't detail deeply enough to confirm or contradict.
- **PHARM-F-121** (terminal slope "always" reflective of ke?) — the "always"
  qualifier makes this debatable in multi-compartment kinetics; source doesn't
  address the exception case.
- **PHARM-F-224** (tetracycline uses "may NOT include") — genuinely ambiguous
  question structure; three of four options are confirmed valid tetracycline
  uses and the fourth is a meta-statement, not a specific exception.
- **PHARM-F-230** (which macrolide beats others vs. *H. influenzae*) — source
  names clarithromycin and azithromycin together for this, without ranking
  one over the other.

## Needs-eye — 1

- **PHARM-F-065** — carried over unchanged from Job A. Both 2020-2021 captures
  cut off before the option list; no options exist to verify against.

## External — 15

Two clusters:

1. **NSAID/analgesic questions (8)** — PHARM-F-222, 227, 229, 231, 233, 234,
   plus F-046/F-213 (see below). This course's source material is entirely
   antimicrobial/antiviral/antifungal-focused (8 chapters, no NSAID or general
   analgesic chapter) — the Dentistry sitting in particular leans on
   aspirin/acetaminophen/COX-2 content the slides never cover. All answered
   from standard, settled pharmacology (protamine sulfate = heparin antidote
   not paracetamol's; COX-2 selective inhibitors' cardiovascular risk;
   Reye's/acetaminophen; aspirin's antiplatelet mechanism).
2. **Definitional/PK terms not in this source's own vocabulary (4)** —
   PHARM-F-046 and PHARM-F-213 ("selective toxicity"), PHARM-F-082
   ("physiological antagonism" — source defines competitive/noncompetitive/
   inverse agonist but not this category), PHARM-F-088 (Cmax's role in
   bioequivalence rate assessment).
3. **Everything else (3)** — PHARM-F-060 (mutation/selection mechanics of
   resistance emergence), PHARM-F-066 (fluoroquinolone-calcium chelation,
   detailed for tetracyclines but not quinolones in this source), PHARM-F-071
   (semisynthetic vs. synthetic definition), PHARM-F-120 (ampicillin+
   gentamicin as the *first-line*, not just resistant-case, enterococcal
   combination), PHARM-F-182 (antibiotic-course-completion stewardship
   principle).

## Chapter coverage

Ch. 4 (Cell Wall Inhibitors) heaviest by far — 71 citations, unsurprising
given six full Medicine-model reshuffles plus Dentistry all draw on the same
penicillin/cephalosporin/vancomycin-heavy core. Ch. 5 (Protein Synthesis
Inhibitors) close behind at 65. Ch. 6 (Antimetabolites/DNA Synthesis) at 36.
Ch. 2 (Pharmacokinetics) at 21 — every bioequivalence/Cmax/AUC/clearance
question in this tab routes here. Ch. 8 (Antifungals) at 19. Ch. 7
(Antivirals) at 9 — lightly tested relative to its own slide-deck size. Ch. 1
(Intro) at 6, Ch. 3 (Pharmacodynamics) at 4 — both thin, consistent with this
being a finals sitting weighted toward antimicrobial pharmacology over
general principles.

## A note on the "filled radio despite Not yet answered" claims (model 5)

Six claims recorded by Job A from model 5's anomalous late-exam radio state
(PHARM-F-037's Cotrimoxazole reinforcement, PHARM-F-134, PHARM-F-143,
PHARM-F-153, PHARM-F-189, and new PHARM-F-203) were all verified same as any
other claim — decide from source first, then compare. All six turned out
source-consistent (none conflicted), which is itself a small corroborating
data point for Job A's decision to trust that radio state over the stale
badge text.
