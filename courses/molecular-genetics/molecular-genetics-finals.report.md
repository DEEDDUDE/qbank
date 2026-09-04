# molecular-genetics / finals — 225 questions

verified 185 · conflict 13 · external 25 · not-in-source 1 · needs-eye 1

Zero `official` tier anywhere in this tab (no printed answer key ever surfaced
across the 2023-2024 sitting, the 2020-2021 sitting, or the genetics-70q
export) — every question was either independently verified against
`source.md` or answered from outside knowledge, never passed through
untouched.

---

## Conflicts — the circulating claims are wrong on these 13

| ID | Circulating claim | Source-supported answer | Why |
|---|---|---|---|
| MGEN-F-034 | c — X-linked recessive exclusively mothers→sons | a — equal-prevalence vs. male-skewed prevalence is the real test | Source's actual distinguishing feature is autosomal-recessive (equal M/F) vs. X-linked-recessive (more common in males), not the claimed transmission pattern, which also overstates "exclusively." |
| MGEN-F-035 | d — absence of individual chromosomes | a — change in the number of individual chromosomes | Source contrasts aneuploidy (individual-chromosome change, includes both monosomy and trisomy) against polyploidy (whole-set change); d covers only the monosomy half. |
| MGEN-F-082 | a — paternal meiosis I | d — paternal meiosis II | Source's own YY-sperm route to Klinefelter requires the two Y sister chromatids to fail to separate, which is a meiosis II event, not meiosis I. |
| MGEN-F-108 | c — "none of the choices" (i.e. all correct) | e — pseudodominance statement is reversed | Source: pseudodominance means the recessive allele on the intact homolog becomes unmasked (expressed); option e says the opposite. |
| MGEN-F-116 | e — 8bp deletion (in-frame, -3) | a — 12bp insertion (+1, true frameshift) | Source's own frameshift rule is "not divisible by 3"; e's -3bp change is in-frame, a's +1bp change is not. |
| MGEN-F-123 | c — "reciprocal translocation can be balanced or unbalanced" flagged as the exception | d — chromosome 14/21 fusion direction is reversed | Source states a 21→14 segment transfer; option d reverses it (14→21). c is directly true per the source, not the exception. |
| MGEN-F-127 | b — cyclin D1 as proto-oncogene flagged as the exception | c — mislabels cyclin D1 as a tumor-suppressor gene | Source states cyclin D1 IS a proto-oncogene that stimulates progression when expressed (exactly option b) — c is what actually contradicts the source. |
| MGEN-F-128 | d — 1-base deletion in the 3'UTR | e — 2-base insertion at a splice site | A 3'UTR deletion falls outside the coding sequence (translation has already ended); a splice-site indel not divisible by 3 disrupts both splicing and reading frame. |
| MGEN-F-133 | d — bell curve, "most people dominant for all the alleles" | b — controlled by multiple non-allelic genes | Source's clean definition matches b directly; d's added claim about the bell curve's peak is backwards (the peak is the intermediate combination, not the all-dominant extreme). |
| MGEN-F-139 | b — nondisjunction occurs "but not in mitosis" | c — autosomal trisomies more severe than sex-chromosome trisomies | Source explicitly states mitotic nondisjunction can also happen, directly contradicting b. |
| MGEN-F-149 | c — exonuclease I or X | a — exonuclease VII | Working the source's own 5′/3′ mismatch-repair directionality rule for a methyl group at the 5′ position gives exonuclease VII, not I/X (which fits the reverse arrangement). |
| MGEN-F-152 | b — "all of them are correct" (X-linked dominant transmission) | d — heterozygous female passes to half her sons and daughters | Source directly contradicts two of the other three statements (a: an affected father CAN pass to daughters; c describes X-linked recessive, not dominant), so "all of them" is false. |
| MGEN-F-153 | d — flagged as the exception | c — chaperones expressed only under high stress | Source shows many chaperones (e.g. GroEL/GroES) function constitutively, not only under stress — only the heat-shock-protein subset is stress-inducible. Option d is a standard, true definition. |

Several other questions arrived as **disputed** input (two or more competing
claims from Job A, either across capture attempts or within one attempt) —
those are resolved in-place in the verify file with a `note:` explaining
which claim won, not counted in the conflict tally above (per
job-c-verify.md, a disputed question that resolves to one of its own claims
is `verified`, not `conflict`): MGEN-F-002, 021, 044, 052, 083, 096, 122.

## Not in source — 1

- **MGEN-F-134** (eukaryotic NER component list — Uvr proteins + which
  polymerase/helicase) — the source gives bacterial UvrABC and separately the
  eukaryotic XP disease-gene names, but never lists a matching eukaryotic NER
  enzyme roster to check any of the four near-identical option lists against.

## Needs-eye — 1

- **MGEN-F-106** — a genuine Job A capture gap (raw file skips from the bare
  "Question 36" header straight to a mid-option-list fragment). No stem, no
  first option, uncertain lettering — nothing to verify.

## External — 25

Answered from standard genetics/molecular-biology knowledge because the
assigned chapter(s) don't cover the topic, most concentrated in two areas:

**Mitochondrial genetics** (not a chapter of its own in this source) —
MGEN-F-130 (endosymbiotic origin evidence), 135 (LHON, maternal
inheritance), 141 (Barr-body-negative → Turner), 173 (heteroplasmy/threshold
effect), 196 (mitochondrial disease characteristics), 211 (MERRF), 218
(human mitochondrial inheritance), 156 (chloroplast/mitochondria
comparison).

**Topics genuinely outside the 16-chapter source** — MGEN-F-012 (genetic
counselling indications), 137 & 142 (gene therapy vectors/history), 146
(human protein-coding gene count), 189 (epigenetics-vs-mutation
categorization), 201 & 213 (lac operon regulation), 217 (X vs. Y gene
density).

**Smaller individual gaps** — MGEN-F-042 (DNA-polymorphism
nondisjunction-timing reasoning), 145 (GT-AG intron boundary rule), 162
(meiosis I→II, no S-phase), 168 (nondisjunction scope, low confidence), 171
(Fragile X mechanism), 176 (asexual-reproduction variation sources), 193
(sperm chromosome content — genuinely ambiguous between two options), 207
(why trisomy 21 outnumbers trisomy 3/16), 223 (human chromosome 2's
evolutionary origin).

*(Five questions — MGEN-F-006, 024, 080, 088, 090 — straddle two chapters
each; every one was checked against both, and both sides' independent
readings agreed on the same answer in all five cases. Each is recorded
`verified` against whichever chapter gave the more direct citation (Ch. 16
for 006/024/088/090, Ch. 15 for 080), not counted twice and not left in
this external list.)*

## Chapter coverage

Ch. 15 (Chromosomal Disorders) and Ch. 16 (Genetics of Cancer) are the
heaviest, 36 and 34 citations respectively — expected, given this exam
leans hard on chromosomal syndromes and cancer genetics. Ch. 11 (Mendelian
Genetics) and Ch. 13 (Modes of Heredity) follow at 23 each. Ch. 7 (Genetic
Code / Aminoacyl-tRNA Synthesis) is lightest at 2 citations — barely tested
on its own, mostly folded into translation-fidelity questions routed to
Ch. 8 instead.

| Chapter | Citations |
|---|---|
| Ch.01 — DNA Structure/Replication Rules | 5 |
| Ch.02 — Replication: Init/Elong/Term | 3 |
| Ch.03 — DNA Repair | 5 |
| Ch.04 — DNA Recombination | 4 |
| Ch.05 — RNA Synthesis (Transcription) | 5 |
| Ch.06 — RNA Processing | 8 |
| Ch.07 — Genetic Code/Aminoacyl-tRNA | 2 |
| Ch.08 — Translation/Post-Translation | 7 |
| Ch.09 — Molecular Techniques | 5 |
| Ch.10 — Introduction to Genetics | 4 |
| Ch.11 — Mendelian Genetics | 23 |
| Ch.12 — Non-Mendelian Genetics | 14 |
| Ch.13 — Modes of Heredity | 23 |
| Ch.14 — Gene Disorders | 20 |
| Ch.15 — Chromosomal Disorders | 36 |
| Ch.16 — Genetics of Cancer | 34 |

## Method note

Verification for this tab was split across seven parallel passes, one per
chapter-group (Ch.1-4, Ch.5-9, Ch.10-12, Ch.13, Ch.14, Ch.15, Ch.16), each
run independently against only its assigned chapter(s) of `source.md`,
following the answer-first-then-compare rule throughout. Five questions
straddling two chapters (MGEN-F-006, 024, 080, 088, 090) were checked by
both relevant passes; all five reconciled to the same answer from both
sides, and the more directly on-topic chapter's citation was kept. Two
image-dependent questions (MGEN-F-019, 073) were resolved by reading their
`flagged/` crops directly rather than from chapter text alone.
