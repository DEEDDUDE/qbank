---
course: molecular-genetics
tab: quizzes
questions: 65
tiers: claimed 64 | open 1
forms: mcq 65
disputed: 6
needs-eye: 2
next-id: MGEN-Q-066
---

<!-- RUN-PLAN row 4 — raw/quizzes/molecular-2024/, molecular-2023/, molecular-previous/
  only. The other two quizzes subfolders (genetics-2021, genetics-2024-ch4) are row 5,
  a separate session, not covered here.

  Three separate quiz sittings, treated per RUN-PLAN's own framing:

  molecular-2024 (MGEN-Q-001-014) — "Quiz 1 - DNA metabolism (10/10)", two models
  (نموذج ١, نموذج ٢), 6 pages each, merged via the models: mechanism. Not a strict
  reshuffle of one 10-question pool: 10 unique stems came from model 1, 4 more only
  ever appeared in model 2 (14 unique total). Every stem seen in both models agreed
  on the answer — zero disputes in this sitting. One filename typo caused Stage 0 to
  mis-classify نموذج ١'s PDF as "unrecognized-file-type" (the raw filename has a
  stray space before the extension, "...١ . pdf" instead of "...١.pdf") — fixed in
  scripts/prep.py (classify_file now strips internal whitespace from the suffix
  before matching); the raw file itself was left untouched per CLAUDE.md.

  molecular-2023 (MGEN-Q-015-034, plus MGEN-Q-023 shared with molecular-previous
  below) — "Protein 1&2 + techniques", two models. نموذج 1 is a clean 5-page,
  10-question capture. نموذج 2 (17 pages) turned out to itself be a compilation of
  at least five different students' independent attempts at the same quiz —
  different UI language (English/Arabic), different devices, different option
  order, pages not in question-number order — not one continuous capture. Matched
  everything by stem text rather than trusting page order or question number, per
  job-a-extract.md's own rule for exactly this situation. 20 unique stems total (10
  shared with model 1, 10 more only in model 2's compiled set). 4 disputes surfaced
  within this sitting alone (MGEN-Q-015, 016, 017, 029); MGEN-Q-017 (glycosylation)
  has three independent data points, not two — model 1's own page carries two
  disagreeing hand/UI marks (a Moodle radio and a separate red-pen checkmark on a
  different option), and model 2's independent capture agrees with the checkmark,
  not the Moodle radio.

  molecular-previous (MGEN-Q-035-045, plus MGEN-Q-023 shared with molecular-2023
  above) — 11 loose jpeg photos, "Fall 2020/2021", "Molecular biology & Genetics -
  Section 3 - 2201", "Molecular Quiz 1" per the captured breadcrumb — a genuinely
  different sitting from molecular-2023, not another model of it, despite RUN-PLAN's
  framing of this folder as one Arabic-UI capture. In practice it's several
  students' attempts compiled together (Arabic and English UI both appear; at least
  two distinct question-9/10 pairs; filenames are Messenger image IDs, not capture
  timestamps, so folder order does not reflect quiz order). One question
  (MGEN-Q-036, the Sanger-gel True/False item) is genuinely image-dependent — five
  independent captures of it were found, only one of which happened to scroll far
  enough to include the gel autoradiogram itself; that crop is saved to
  flagged/MGEN-Q-036.jpg regardless of the other four not needing it, per the img:
  rule. One question (MGEN-Q-044) references sample lanes 1-5 by number with no
  supporting figure anywhere in this raw set — confirmed by checking the
  full-resolution original directly, not just the downscaled prep — a genuine
  source gap, not a Job A miss; recorded needs-eye.

  Cross-sitting overlap: molecular-2023 and molecular-previous each independently
  ask "Reverse transcriptase PCR uses" with the identical five-option list — the
  same shared-bank pattern seen elsewhere in this project (pharmacology's
  2020-2021/2023-2024 finals). Merged into one entry (MGEN-Q-023) with two disputed
  claims tagged by sitting, not by models: — molecular-previous is not a model of
  the molecular-2023 exam, just a different sitting that happens to draw on the
  same question bank for this one item. No other cross-sitting stem matches were
  found; molecular-2024's DNA-metabolism content and the other two sittings'
  protein/techniques content don't otherwise overlap.

  All 45 questions are tier claimed or open — zero official tier anywhere in this
  batch, consistent with CLAUDE.md's course-level note that darwish-keys (midterm
  tab) is the only official-tier material in this whole course. -->

### MGEN-Q-001
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2]
What is the primary function of a nucleosome in eukaryotic cells?
a) Initiating DNA replication
b) Facilitating the repair of damaged DNA
c) Binding to promoters to initiate transcription
d) Regulating the synthesis of ribosomal RNA
e) Packaging DNA into a compact structure

### MGEN-Q-002
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2]
Which protein is NOT necessary to initiate DNA replication in E. coli?
a) All of them are necessary.
b) helicases
c) DnaA proteins
d) primases
e) topoisomerases

### MGEN-Q-003
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
note: Leading "8-" is printed exactly as it appears in the source.
8-What is the function of the OriC region in bacterial DNA replication?
a) Serving as the origin of replication where DNA unwinding begins
b) Facilitating the repair of mismatched nucleotides
c) Regulating the transcription of nearby genes
d) Binding single-stranded DNA-binding proteins
e) Terminating DNA replication

### MGEN-Q-004
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
What do MOST bacterial DNA ligases use for phosphodiester bond formation?
a) CTP
b) NAD+
c) TTP
d) GTP
e) ATP

### MGEN-Q-005
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
What is the correct function of telomeres?
a) All of them are true.
b) Maintain the stability of eukaryotic chromosome
c) Allowing for complete chromosomal replication
d) Protecting the ends of the DNA from binding to one another and to itself.
e) serving as a molecular timer by controlling the lifespan of an eukaryotic cell.

### MGEN-Q-006
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2]
Which of the following statements correctly describes a distinguishing feature of A-DNA, B-DNA, and Z-DNA?
a) A-DNA, B-DNA, and Z-DNA all have right-handed helices with varying nucleotide stretches per turn.
b) A-DNA and B-DNA have a left-handed helix, while Z-DNA has a right-handed helix.
c) Z-DNA has a left-handed helix, whereas A-DNA and B-DNA have a right-handed helix.
d) A-DNA is more tightly packed with 12 base pairs per turn, while B-DNA has 10, and Z-DNA has 11 base pairs per turn in a left-handed helix.

### MGEN-Q-007
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2]
Which of the following statements accurately describes the role of the H1 histone in the nucleosome structure?
a) H1 stabilizes the DNA wrapped around the nucleosome core by binding to linker DNA.
b) H1 binds directly to DNA within the nucleosome core.
c) H1 replaces one of the core histones (H2A, H2B, H3, H4) in the nucleosome.
d) H1 is part of the histone octamer within the nucleosome core.

### MGEN-Q-008
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2]
What is the meaning of semiconservative DNA replication?
a) Half the DNA is replicated.
b) Both DNA molecules have strands that is newly synthesized.
c) The produced DNA molecule is identical to the original molecule and both strands are newly synthesized.
d) The produced DNA molecule is identical to the original molecule but one strand is original and the other is newly synthesized.

### MGEN-Q-009
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
note: Option b's "II and II" is printed exactly as it appears in the source
  (likely meant "II and III"). The arrow in options a and b renders as a missing
  glyph in the source PDF's own font — transcribed here as "→", its clear intent.
In E. coli, the 3 DNA polymerases differ in:
a) Polymerase III is the only enzyme that has 5' → 3' exonuclease activity.
b) Polymerase I has 3' → 5' exonuclease proof reading while II and II do not.
c) Polymerase III has the lowest processivity.
d) Polymerase I is the only enzyme that has 5' → 3' exonuclease activity.

### MGEN-Q-010
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2]
Processivity is defined as:
a) the rate at which nucleotides are added to the DNA.
b) which DNA polymerase is performing the elongation.
c) the number of DNA polymerases bound to one DNA molecule.
d) how many errors are incorporated into the DNA per 1,000 bases.
e) the average number of nucleotides added before a polymerase dissociates.

### MGEN-Q-011
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
What type of bond must be made between Okazaki fragments in order to make a complete DNA strand?
a) phosphodiester
b) hydrogen
c) ester
d) ionic
e) disulfide

### MGEN-Q-012
tier: claimed
form: mcq
type: single
claimed: e
models: [2]
What is the primary function of DNA ligase during DNA replication?
a) Unwinding the DNA double helix
b) Synthesizing new DNA strands by adding nucleotides
c) Removing RNA primers from the newly synthesized DNA strands
d) Stabilizing single-stranded DNA during replication
e) Sealing nicks between Okazaki fragments on the lagging strand

### MGEN-Q-013
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
Circular DNA strands replicate and finish as two rings linked together, as in a chain. How are they separated?
a) using one of the functions of helicase
b) using one of the functions of DNA primase
c) using the exonuclease function of DNA polymerase
d) using topoisomerase IV

### MGEN-Q-014
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
Which of the following characteristics is true regarding heterochromatin?
a) Heterochromatin contains a high density of genes that are actively expressed.
b) Heterochromatin is usually densely packed and transcriptionally inactive.
c) Heterochromatin is less condensed than euchromatin.
d) Heterochromatin is typically associated with active gene transcription.

### MGEN-Q-015
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: molecular-2023 model 1
    answer: d (It generates a staggered cut)
  - source: molecular-2023 model 2 (Arabic-UI capture)
    answer: a (They are independent of the DNA sequence recognized by the enzyme)
models: [1, 2]
Which of the following is true for sticky-end cuts by restriction enzymes?
a) They are independent of the DNA sequence recognized by the enzyme
b) They always produce circular DNA fragments
c) The cut is flush, with no overhang
d) It generates a staggered cut
e) They create blunt ends

### MGEN-Q-016
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: molecular-2023 model 1
    answer: a (It is the site of amino acid attachment.)
  - source: molecular-2023 model 2 (badge read "Not yet answered" but the radio
      was filled — recorded per the filled-radio rule)
    answer: d (It performs no function.)
note: The same stem recurs at least twice more within model 2's own compiled
  captures — once with the radio obscured by a glare/reflection artifact (no
  claim extractable), once cut off before its options render. Neither adds a
  new value.
models: [1, 2]
The 3' end of a tRNA performs the following function:
a) It is the site of amino acid attachment.
b) It forms one of the loops of the cloverleaf structures.
c) It is the anti-codon.
d) It performs no function.

### MGEN-Q-017
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: molecular-2023 model 1, Moodle radio (badge read "Not yet answered",
      radio filled)
    answer: d (N-linked glycosylation occurs on serine and threonine residues,
      while O-linked glycosylation occurs on asparagine residues.)
  - source: molecular-2023 model 1, hand-drawn red checkmark over a different
      option than the filled radio
    answer: b (N-linked glycosylation occurs on asparagine residues, while
      O-linked glycosylation occurs on serine and threonine residues.)
  - source: molecular-2023 model 2 (clean "Answer saved", no stale badge)
    answer: b (N-linked glycosylation occurs on asparagine residues, while
      O-linked glycosylation occurs on serine and threonine residues.)
note: Two independent mark systems on model 1's own page disagree with each
  other; model 2's independent capture agrees with the hand-drawn checkmark,
  not model 1's own Moodle radio.
models: [1, 2]
Which of the following statements is true regarding glycosylation in proteins?
a) Most of N-linked glycosylation occurs in the Golgi apparatus or in the cytosol
b) N-linked glycosylation occurs on asparagine residues, while O-linked glycosylation occurs on serine and threonine residues.
c) Both N-linked and O-linked glycosylation occur on Golgi apparatus.
d) N-linked glycosylation occurs on serine and threonine residues, while O-linked glycosylation occurs on asparagine residues.

### MGEN-Q-018
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
How does the core oligosaccharide build up in the endoplasmic reticulum?
a) The sugar residues are added to dolichol-phosphate in the membrane of ER, forming the core oligosaccharide in a stepwise manner.
b) The core oligosaccharide is synthesized in cytoplasm and then transported to the endoplasmic reticulum for attachment to dolichol-phosphate.
c) Enzymes in the Golgi apparatus synthesize the core oligosaccharide directly.
d) The oligosaccharide core is assembled simultaneously on various locations within endoplasmic reticulum.

### MGEN-Q-019
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
The ribosome is involved in all of the following except:
a) Peptide bond formation
b) Binding of protein factors during elongation
c) Aminoacylation of t-RNA
d) Binding of aminoacyl-tRNA to mRNA
e) Binding of mRNA at an initiation codon.

### MGEN-Q-020
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
note: Model 2's own capture of this same question was left unanswered ("Not
  yet answered", no radio filled) — no second claim.
How are DNA fragments separated in Sanger sequencing?
a) Gel electrophoresis
b) Reverse transcription
c) PCR amplification
d) Magnetic bead separation
e) Southern blotting

### MGEN-Q-021
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2]
What is the primary function of ubiquitination in cellular processes?
a) To facilitate the correction of misfolded protein by chaperones.
b) To facilitate protein synthesis in the ribosomes.
c) To mark proteins for degradation by the lysosome
d) To mark proteins for degradation by the proteasome.

### MGEN-Q-022
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2]
note: Option a's "the there are" is printed exactly as it appears in the source.
Which of the following is not a true statement concerning the genetic code
a) the there are no gaps between successive codons in an mRNA (i.e. it is commaless)
b) all 64 possible triplet sequences code for amino acids
c) each codon is composed of a nucleotide triplet
d) some amino acids are coded for by more than one triplet
e) the code is non-overlapping in an mRNA

### MGEN-Q-023
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: molecular-2023 model 1
    answer: d (RNA as a template to form ssDNA)
  - source: molecular-previous (Fall 2020/2021 "Molecular Quiz 1")
    answer: a (mRNA as a template to form cDNA)
note: Same stem and same option set recur in two different quiz sittings (a
  shared techniques question, not a reshuffled model) — see this file's own
  header comment.
Reverse transcriptase PCR uses
a) mRNA as a template to form cDNA
b) none of them
c) tRNA as a template to form cDNA
d) RNA as a template to form ssDNA
e) DNA as a template to form RNA

### MGEN-Q-024
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
note: Stem's "aquatics" is printed exactly as it appears in the source
  (presumably meant "aquaticus").
Thermus aquatics is the source of __________.
a) Taq polymerase
b) Vent polymerase
c) Two choices are correct
d) Primase enzyme
e) None of the choices

### MGEN-Q-025
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
Which one of the following is correct about PCR?
a) None of the choices
b) All choices are correct
c) Millions to billions of desired DNA copies can be produced from microgram quantities of DNA
d) Automated PCR machines are called thermal cyclers
e) A thermostable DNA polymerase is required

### MGEN-Q-026
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
What is the primary signal sequence responsible for directing eukaryotic proteins to the endoplasmic reticulum (ER)?
a) Signal Recognition sequence
b) Endoplasmic Reticulum Targeting Signal
c) Nuclear Localization Signal
d) Peptide Signal sequence

### MGEN-Q-027
tier: claimed
form: mcq
type: single
claimed: c
models: [2]
Which of the following best describes the recognition site for a restriction enzyme?
a) The site of DNA replication
b) A region rich in adenine and thymine
c) A specific DNA sequence that acts as a binding site
d) A region with a high GC content
e) Any location along the DNA strand

### MGEN-Q-028
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
Which of the following mechanisms is responsible for sorting acid hydrolase in the Golgi apparatus and facilitating its transport to lysosome?
a) Addition of Mannose-6-phosphate (M6P)
b) Binding of importin protein with Nuclear Localization Signal
c) Binding of SRP with Peptide Signal sequence
d) N-linked glycosylation of asparagine residues in the endoplasmic reticulum

### MGEN-Q-029
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: molecular-2023 model 2, English-UI capture ("Answer saved")
    answer: d (eIF4B scans the 5' mRNA for initiation codon.)
  - source: molecular-2023 model 2, Arabic-UI capture (سؤال 9)
    answer: e (Initiation usually begins at an AUC codon)
note: Both captures are filed under model 2 — this is a dispute between two of
  model 2's own compiled attempts, not model 1 vs. model 2 (model 1 never asks
  this question).
models: [2]
Which of the following is true regarding the machinery of translation?
a) tRNAs released from the ribosome are degraded
b) Termination is at inverted repeats and requires release factors.
c) Eukaryotes have nuclear ribosomes
d) eIF4B scans the 5' mRNA for initiation codon.
e) Initiation usually begins at an AUC codon

### MGEN-Q-030
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
What is the purpose of incorporating dideoxynucleotides (ddNTPs) in Sanger sequencing?
a) To amplify DNA
b) To terminate DNA synthesis at specific bases
c) To enhance DNA replication
d) To introduce mutations
e) To increase the accuracy of DNA synthesis

### MGEN-Q-031
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
The concept of "wobble" involves:
a) none of the sentences are correct
b) base pairing between the first (5') base of the codon and the third (3') base of the anticodon
c) base pairing between the first base of the codon and the first base of the anticodon
d) base pairing between the third base of the codon and the first base of the anticodon
e) base pairing between the third base of the codon and the third base of the anticodon

### MGEN-Q-032
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
Primers are generally __________.
a) taken according to the amount available
b) as long as the template is
c) None of the choices
d) 20-30 nucleotides long
e) 40-50 nucleotides long

### MGEN-Q-033
tier: open
form: mcq
type: single
models: [2]
The GC content of the primer (GACTCGAGCATCCTGACACG) is:
a) 55%
b) 50%
c) 45%
d) 60%
e) 65%

### MGEN-Q-034
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
During elongation, the charged tRNA enters the ribosome at the:
a) Q site
b) P site
c) E site
d) A site

### MGEN-Q-035
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
Automated DNA sequencing is an improvement of Sanger's method where
a) fluorescent labeled ddNTPs are used for chain termination
b) Restriction enzymes are used for chain termination
c) P32 labeled dNTPs are used for chain termination
d) fluorescent labeled dNTPs are used for chain termination
e) None of them

### MGEN-Q-036
tier: claimed
form: mcq
type: single
disputed: true
img: flagged/MGEN-Q-036.jpg
claims:
  - source: molecular-previous, capture 1 (badge "Not answered yet", radio filled)
    answer: a (True)
  - source: molecular-previous, capture 2 ("Answer saved")
    answer: b (False)
  - source: molecular-previous, capture 3 ("Answer saved")
    answer: b (False)
  - source: molecular-previous, capture 4 (badge "Not answered yet", radio filled)
    answer: a (True)
  - source: molecular-previous, capture 5 ("Answer saved" — the only one of the
      five whose screenshot scrolled far enough to include the gel ladder
      figure itself)
    answer: b (False)
note: Five independent captures of the same question, split 2 True / 3 False.
  The gel autoradiogram the answer depends on is only visible in capture 5's
  screenshot — the other four scrolled past it, which is why this crop is
  saved to flagged/ even though four of five captures transcribe cleanly
  without it.
The sequence of the DNA template if the sanger method gave us the result shown below is 5'- GTACCCGAAATCAGGA-3' [figure: Sanger sequencing gel autoradiogram, lanes G/A/T/C]
a) True
b) False

### MGEN-Q-037
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
note: Three independent captures all agree.
Taq polymerase
a) synthesize DNA in 5'->3' direction
b) synthesize DNA in 3'->5' direction
c) require ATP to function
d) replicate RNA

### MGEN-Q-038
tier: claimed
form: mcq
type: single
claimed: d
source: molecular-previous
From the following list of reagents, which one will you use to prepare a PCR?
a) Mg2+, Taq polymerase, dNTPs, primers
b) Taq polymerase, target DNA, primers, deoxyribonuclease.
c) RNA template, primers, Taq polymerase, dNTPs
d) Primers, Taq polymerase, dNTPs, Mg2+, DNA template

### MGEN-Q-039
tier: claimed
form: mcq
type: single
claimed: d
source: molecular-previous
note: Distinct stem from MGEN-Q-023 ("Reverse transcriptase PCR uses") — not
  merged with it.
RT-PCR is used for
a) amplifying proteins
b) detecting the DNA of a specific gene
c) reverse transcribing DNA into RNA
d) Detecting the RNA level of a gene
e) amplification of DNA

### MGEN-Q-040
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
What is the process of binding of primer to the denatured strand called?
a) Annealing
b) Renaturation
c) Denaturation
d) None of them

### MGEN-Q-041
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
In DNA footprinting method, the DNA bound to a protein is protected at the binding site from cleavage by nucleases:
a) False
b) True

### MGEN-Q-042
tier: claimed
form: mcq
type: single
claimed: c
source: molecular-previous
__________ Primer used for the process of polymerase chain reaction are
a) Double stranded RNA oligonucleotide
b) Double stranded DNA oligonucleotide
c) Single stranded DNA oligonucleotide
d) Single stranded RNA oligonucleotide

### MGEN-Q-043
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
The following describe the polymerase chain reaction (PCR):
a) A technique that can routinely amplify up to 100 kb of DNA
b) A process that uses a heat-sensitive DNA polymerase
c) A very sensitive method of amplifying DNA that can be prone to contamination
d) A method of amplifying genes that requires no prior sequence knowledge

### MGEN-Q-044
tier: claimed
form: mcq
type: single
needs-eye: true
claimed: a
source: molecular-previous
note: Options are bare sample numbers referencing a gel/digest-pattern figure
  that is never captured anywhere in this raw set — confirmed by checking the
  full-resolution original directly, not just the downscaled prep copy. A
  genuine source gap, not a Job A miss. The claim (option a, "1") is recorded
  as transcribed but is unverifiable without the missing figure.
A fragment of DNA was amplified and digested by EcoR1, a mutation in the nucleotide sequence creates EcoR1 site which of the following samples is normal
a) 1
b) 5
c) 3
d) 4
e) 2

### MGEN-Q-045
tier: claimed
form: mcq
type: single
claimed: a
source: molecular-previous
note: Stem's trailing "5" is printed exactly as it appears in the source
  (visually inline with the sentence, not obviously separable from it —
  transcribed as-is per hard rule 2 rather than silently dropped).
RFLP analysis is a technique that 5
a) Uses restriction enzymes to detect a specific mutation in a targeted DNA fragment
b) is used to determine whether a gene is transcribed in specific cells
c) is used to detect proteins
d) is used to amplify genes for producing useful products

<!-- batch 02 (RUN-PLAN row 5) — raw/quizzes/genetics-2021/ + genetics-2024-ch4/.

  genetics-2021 (MGEN-Q-046-055) — 10 loose jpeg photos (IMG-20210909-WA0019
  through WA0028), all below the 1000px floor, one Moodle attempt, "Marked out
  of 1" throughout. Every single question in this sitting is pedigree-dependent
  — not just Q1 as RUN-PLAN's own pre-flight note anticipated — so all ten get a
  flagged/ crop, not a subset. Filenames are sequential capture order but do NOT
  match question order (files landed as Q1, Q4, Q6, Q10, Q5, Q2, Q3, Q9, [no
  header], Q7) — matched to question number from each screenshot's own
  "Question N" badge, not file order. One file (WA0027) never captured its own
  header — inferred as Q8 by elimination, since the other nine numbers 1-7, 9,
  10 were all independently seen elsewhere in this same 10-file set; recorded
  needs-eye both for the inferred number and because its option list stops at
  (c) with only 3 options where every sibling "mode of heredity" question in
  this sitting has 5 — likely cut off by the photo's own framing, not a Job A
  read failure. Two more of this sitting's own answer lists carry a duplicate
  option text under two different letters (MGEN-Q-050's b/d both "Aa",
  MGEN-Q-051's a/e both "Dd") — preserved exactly as printed per hard rule 2,
  not corrected. All ten questions are tier claimed; several show "Not yet
  answered" badges with a filled radio (the same filled-radio-under-stale-badge
  pattern established elsewhere in this project) and are recorded as claims per
  that precedent.

  genetics-2024-ch4 (MGEN-Q-056-065) — one PDF, "Quiz chapter 4", 8 vision
  pages / 10 questions, one clean Moodle attempt, "Marked out of 1" throughout,
  zero vision cost issues. 3 of its 10 questions are pedigree-dependent
  (MGEN-Q-059, 062, 065) and get their own flagged/ crop; the other 7 are plain
  text MCQs. MGEN-Q-065's pedigree is the same family-tree figure as
  MGEN-Q-050's from the genetics-2021 sitting above (identical shape and fill
  pattern) — a shared textbook figure reused across two unrelated quiz
  sittings with two different questions asked about it, not a duplicate
  question; no merge applies since the stems differ. All ten questions are
  tier claimed, all cleanly "Answer saved".

  No cross-sitting stem overlap found between these two sittings, and neither
  overlaps molecular-2024/2023/previous from batch 01 above (different topic:
  Mendelian/pedigree genetics vs. molecular biology techniques). -->

### MGEN-Q-046
tier: claimed
form: mcq
type: single
claimed: c
source: genetics-2021
img: flagged/MGEN-Q-046.jpg
the pedigree above shows the following mode of heredity? [figure: 3-generation pedigree]
a) Autosomal recessive
b) Y-linked
c) Autosomal dominant
d) X-linked dominant
e) X-linked recessive

### MGEN-Q-047
tier: claimed
form: mcq
type: single
claimed: d
source: genetics-2021
img: flagged/MGEN-Q-047.jpg
the pedigree above shows the following mode of heredity? [figure: 4-generation pedigree]
a) X-linked dominant
b) Autosomal dominant
c) Y-linked
d) Autosomal recessive
e) X-linked recessive

### MGEN-Q-048
tier: claimed
form: mcq
type: single
claimed: c
source: genetics-2021
img: flagged/MGEN-Q-048.jpg
What is the pattern / mode of heredity for the above pedigree? [figure: 3-generation pedigree]
a) X-linked dominant
b) Autosomal recessive
c) Autosomal dominant
d) Y linked
e) X-linked recessive

### MGEN-Q-049
tier: claimed
form: mcq
type: single
claimed: c
source: genetics-2021
img: flagged/MGEN-Q-049.jpg
the pedigree above shows the following mode of heredity? [figure: 3-generation pedigree, individuals numbered 1-15]
a) Autosomal dominant
b) Y-linked
c) X-linked recessive
d) X-linked dominant
e) Autosomal recessive

### MGEN-Q-050
tier: claimed
form: mcq
type: single
claimed: b
source: genetics-2021
img: flagged/MGEN-Q-050.jpg
note: Options b and d are both printed "Aa" — preserved exactly as printed,
  not corrected.
What is the genotype of individual I-1? [figure: 3-generation pedigree, individuals numbered]
a) XAY
b) Aa
c) XaY
d) Aa
e) AA

### MGEN-Q-051
tier: claimed
form: mcq
type: single
claimed: d
source: genetics-2021
img: flagged/MGEN-Q-051.jpg
note: Options a and e are both printed "Dd" — preserved exactly as printed,
  not corrected.
Having dimples is an autosomal dominant trait, What is the phenotype of individual III-5? [figure: 3-generation pedigree, individuals numbered; III-2 is shown with a distinct shaded/hatched fill, not solid black]
a) Dd
b) No dimples
c) DD
d) Dimples
e) Dd

### MGEN-Q-052
tier: claimed
form: mcq
type: single
claimed: c
source: genetics-2021
img: flagged/MGEN-Q-052.jpg
note: Each option is printed with an extra leading letter before its own
  position letter (e.g. "a. D. This is a Y linked disease") — preserved
  exactly as printed; likely an artifact of how the source re-lettered a
  shuffled option list.
What is the mode of inheritance in the pedigree shown below: [figure: 3-generation pedigree, individuals numbered]
a) D. This is a Y linked disease
b) C. This is an autosomal dominant disease.
c) A. If individual III-1 marries an unaffected, non-carrier female, none of their offspring will have the disease.
d) B. This is an X linked dominant disease.

### MGEN-Q-053
tier: claimed
form: mcq
type: single
needs-eye: true
claimed: a
source: genetics-2021
img: flagged/MGEN-Q-053.jpg
note: Question number inferred as 8 by elimination — this capture's own
  header (question number and Answer-saved badge) was never photographed,
  and every other number 1-7, 9, 10 in this ten-file sitting was
  independently seen elsewhere. Only 3 options were captured (a-c) where
  every sibling "mode of heredity" question in this sitting has 5 — most
  likely cut off by the photo's own framing rather than a genuine 3-option
  question; options d/e (if any) are not recoverable from this raw set.
which of the following sentences is true about the pedigree above? [figure: 5-generation pedigree, individuals unnumbered]
a) An example of a dominant trait with incomplete penetrance in III-3 who passes the disease for her daughter but is herself unaffected
b) An example of an X-linked dominant trait
c) An example of an X-linked recessive trait

### MGEN-Q-054
tier: claimed
form: mcq
type: single
claimed: e
source: genetics-2021
img: flagged/MGEN-Q-054.jpg
The genotype for III- 1 is ? [figure: 3-generation pedigree, individuals numbered]
a) aa or XaY
b) XaY
c) a or b
d) Aa
e) aa

### MGEN-Q-055
tier: claimed
form: mcq
type: single
claimed: e
source: genetics-2021
img: flagged/MGEN-Q-055.jpg
the pedigree above shows the following mode of heredity? [figure: 3-generation pedigree]
a) Autosomal recessive
b) X-linked recessive
c) X-linked dominant
d) Autosomal dominant
e) Y-linked

### MGEN-Q-056
tier: claimed
form: mcq
type: single
claimed: b
source: genetics-2024-ch4
If both parents are carriers of the defective Phenylalanine Hydroxylase gene, what is the probability that their child will inherit one defective allele?
a) 25%
b) 50%
c) 100%
d) 75%

### MGEN-Q-057
tier: claimed
form: mcq
type: single
claimed: a
source: genetics-2024-ch4
Which of the following statements about albinism is TRUE?
a) Parents of children with albinism are usually carriers.
b) Albinism is caused by a dominant gene mutation.
c) All of them are true
d) Albinism cannot skip generations.

### MGEN-Q-058
tier: claimed
form: mcq
type: single
claimed: a
source: genetics-2024-ch4
Which inheritance pattern is most likely when a trait consistently skips generations and appears equally in males and females?
a) Autosomal recessive
b) X-linked recessive
c) Autosomal dominant
d) X-linked dominant
e) Y-linked

### MGEN-Q-059
tier: claimed
form: mcq
type: single
claimed: e
source: genetics-2024-ch4
img: flagged/MGEN-Q-059.jpg
For the following pedigree, give the most likely mode of inheritance, assuming that the trait is rare. [figure: 4-generation pedigree, individuals numbered, affected symbols shown in gray/shaded fill]
a) X-linked dominant
b) X-linked recessive
c) Autosomal recessive
d) Y-linked
e) Autosomal dominant

### MGEN-Q-060
tier: claimed
form: mcq
type: single
claimed: d
source: genetics-2024-ch4
Which of the following scenarios for the inheritance of hemophilia is not possible?
a) A carrier mother and a normal father have a son who is hemophilic
b) A carrier mother and a hemophilic father have a daughter who is hemophilic
c) A hemophilic mother and a normal father have a daughter who is a carrier for the disease.
d) A normal mother and a hemophilic father have a son who is also hemophilic

### MGEN-Q-061
tier: claimed
form: mcq
type: single
claimed: d
source: genetics-2024-ch4
Which of the following is NOT seen in autosomal recessive pedigrees
a) Affected persons must be homozygous for the disease allele
b) The parents are more likely to be relatives
c) Both males and females can be affected
d) Affected persons have at least one affected parent

### MGEN-Q-062
tier: claimed
form: mcq
type: single
claimed: a
source: genetics-2024-ch4
img: flagged/MGEN-Q-062.jpg
What is the mode of inheritance in the pedigree shown below: [figure: 3-generation pedigree, individuals numbered]
a) Autosomal dominant
b) X linked recessive
c) Y linked
d) X linked dominant

### MGEN-Q-063
tier: claimed
form: mcq
type: single
claimed: b
source: genetics-2024-ch4
Which inheritance pattern is most likely if a trait appears in every generation, affects both sexes equally, and each affected individual has an affected parent?
a) Y-linked
b) Autosomal dominant
c) X-linked recessive
d) Autosomal recessive
e) X-linked dominant

### MGEN-Q-064
tier: claimed
form: mcq
type: single
claimed: d
source: genetics-2024-ch4
In individuals with PKU, the deficiency or absence of the PAH enzyme leads to the buildup of a toxic substance in the blood and brain when consuming foods that contain protein. What does the PAH enzyme normally do?
a) Breaks down proteins into amino acids
b) Converts tyrosine to tryptophan
c) Converts glutamine to glutamate
d) Converts phenylalanine to tyrosine

### MGEN-Q-065
tier: claimed
form: mcq
type: single
claimed: b
source: genetics-2024-ch4
img: flagged/MGEN-Q-065.jpg
This pedigree tracks the presence of attached earlobes through a family's generations. Having attached earlobes is an autosomal recessive trait. What is the genotype of individual II-3? [figure: 3-generation pedigree, individuals numbered; same underlying family-tree figure as MGEN-Q-050, reused for a different question]
a) XeY
b) Ee
c) EE
d) XEY
e) ee
