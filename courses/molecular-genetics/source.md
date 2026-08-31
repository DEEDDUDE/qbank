# molecular-genetics — source

Built from `slides/2024-canonical/` — the `molecular/` subfolder (Ch. 1–9, 9 decks,
331 pages) and the `genetics/` subfolder (Ch. 10–16, 7 decks, 306 pages), both by
Dr. Suheir Ereqat, 2020-2025. Chapter numbers throughout are **ours**, not the
source's — each deck becomes one chapter, in deck order. The `molecular/` decks
themselves cite Lehninger *Principles of Biochemistry* chapter numbers inconsistently
(DNA metabolism decks reference "Chapter 25", RNA metabolism decks "Chapter 26",
Protein metabolism decks "Chapter 27"; the Techniques deck cites none) — those
Lehninger numbers are noted per chapter below but are not used as our anchors, since
no single Lehninger chapter maps cleanly to one deck. The `genetics/` decks (Ch.
10–16) cite no external textbook chapter numbers of their own; several borrow figure/
table numbers from an unnamed genetics textbook (e.g. "Fig. 8.1", "Table 18.2") which
are reproduced as printed, not renumbered.

Several slides carry almost no extractable text — just a diagram or table image and a
"Dr. Suheir Ereqat" footer. Every one of these was individually reviewed at full
resolution; all 17 found this way turned out to carry real, substantive content
(textbook tables, mechanism diagrams, a chemical structure) and are transcribed in
place below, tagged `[figure]`. None were decorative. Several also carry handwritten
annotations added on top of the printed slide (corrections, mnemonics, extra labels) —
these are part of the source as captured and are transcribed too, tagged `[handwritten]`.

---

## Ch. 1 — DNA Structure and the Rules of Replication {#ch01}

*Source: "DNA metabolism-1.pdf" (60p). Lehninger Ch. 25 territory.*

### 1.1 Central dogma {#ch01-1}
DNA → RNA → protein.

### 1.2 What is DNA {#ch01-2}
Deoxyribonucleic acid: a complex molecule containing all the information necessary to
build and maintain an organism (specifies structure and function of living things).
The primary unit of heredity in organisms of all types.

### 1.3 DNA structure — three hierarchical levels {#ch01-3}
- **Primary structure** — the nucleotide sequence.
- **Secondary structure** — the double-stranded helix.
- **Tertiary structure** — higher-order folding that allows DNA to be packed.

**Nucleotide anatomy.** All nucleotides share a common structure: a nitrogenous base
(A, G, C, or T) bonded to C1 of the sugar, a pentose sugar (deoxyribose in DNA,
ribose in RNA), and a phosphate group attached via the 5' carbon. Nitrogen 9 of
purines and nitrogen 1 of pyrimidines bond to C1 of the sugar. Carbon numbering:
C1′–C4′ around the ring, C5′ the exocyclic carbon carrying the phosphate.

**Bases.**
- Pyrimidines (single ring): Cytosine (C), Thymine (T) — or Uracil (U) in RNA instead
  of Thymine.
- Purines (double ring): Adenine (A), Guanine (G).

**The double helix.** Two strands coiled into a double helix. Sides made of
deoxyribose bonded to phosphate groups by phosphodiester bonds. Center made of
nitrogen bases bonded together by weak hydrogen bonds.

**Polynucleotide linkage.** Nucleotide subunits are linked by phosphodiester bonds:
the 5′-phosphate group of one nucleotide joins the 3′-hydroxyl group of the next. A
nucleic acid chain is represented 5′→3′, left to right (e.g. 5′-C-A-G-3′) — a 5′
phosphate group on the 5′ carbon of the sugar and a 3′ hydroxyl on the 3′ carbon.

**Watson and Crick** provided the three-dimensional model of DNA structure.

**Native DNA** is a double helix of complementary, antiparallel chains held together
by (1) hydrogen bonding between complementary base pairs (A–T or G–C) and (2)
hydrophobic interactions between stacked adjacent bases. This base stacking
contributes to the stability of the double helix.

**Ladder analogy.** Nitrogenous bases (A, T, G, C) = "rungs of the ladder"; phosphate
& sugar backbone = "legs of the ladder".

### 1.4 Helical forms — B, A, and Z DNA {#ch01-4}
DNA coils into a double helix, with both strands coiling around an axis. At neutral
pH and physiological salt, three forms are described:

| | B DNA | A DNA | Z DNA |
|---|---|---|---|
| Helix sense | Right-handed | right | left |
| Mean bp/turn | 10.5 | ~~10~~ **[handwritten correction] 11** | 12 |

`[handwritten]` next to the table: "Mean base pairs/turn" (clarifying the row label);
under B DNA, "present in living cells / optimal"; under A DNA, "compressed"; under Z
DNA, "stretched". The 3D space-filling models are additionally annotated with "Tilt"
and "Tilt Angle" labels pointing at the base-pair stacking in each form. B-DNA's
helical rise per turn is marked 3.6 nm on its model. The printed "10" for A DNA's
mean bp/turn is struck through by hand and corrected to 11 in the source — kept as
struck-through-and-corrected, not silently replaced, per this source's own edit.

B-form is the most stable DNA form and is the form Watson and Crick's replication
model uses — right-handed DNA.

### 1.5 DNA melting and hybridization {#ch01-5}
Tm = the temperature at which half the DNA is present as separated single strands.
Tm depends on GC content, at fixed pH and ionic strength (higher GC = higher Tm, more
H-bonds and stacking). DNA denaturation and renaturation is the basis of nucleic acid
hybridization and PCR — a powerful molecular biology technique.

### 1.6 Eukaryotic vs. prokaryotic DNA {#ch01-6}
**Prokaryotic DNA:** found freely in the cytoplasm (in a region called the
nucleoid); naked (not bound to proteins, so no chromatin); genomes compact (little
repetitive DNA, no introns); may contain extra-chromosomal plasmids; circular in
shape.

**Eukaryotic DNA:** contained within a nucleus; bound to histone proteins; genomes
contain large amounts of non-coding and repetitive DNA (including introns); do not
contain plasmids (though organelles like mitochondria may carry their own
chromosomes); linear in shape.

### 1.7 Packing DNA into the nucleus {#ch01-7}
A human cell contains about 2 m of DNA; the human body has on the order of 10¹³
cells (2×10¹³ m total) — enough to stretch to the sun and back 50 times. The
question the slide poses rhetorically: how does 2 m of a 0.006 nm-diameter molecule
fit inside the nucleus?

**Hierarchy:** cell → nucleus → chromosome → gene → DNA → base pair. Eukaryotic
chromosomes have two important special-function repetitive DNA sequences:
**centromeres** (attachment points for the mitotic spindle) and **telomeres**
(located at the ends of chromosomes).

- **Centromere:** functions during cell division as an attachment point during
  mitosis; an A=T-rich sequence.
- **Telomere:** sequence at the end of chromosomes that helps stabilize the
  chromosome.

### 1.8 Genes, introns, exons {#ch01-8}
**Gene** — a portion of a chromosome that determines a single specific
character/phenotype/visible property; a segment of genetic material that codes for a
protein/enzyme. Classic formulation: one gene–one enzyme → one gene–one polypeptide.
Modern biochemical definition: all the DNA that encodes the primary sequence of some
final gene product (polypeptide or RNA).

- **Introns:** intervening sequences — nontranslated DNA segments within genes.
- **Exons:** regions of DNA within a gene that are transcribed into the final mRNA,
  rather than spliced out from the transcribed RNA.

**Repetitive sequence classes in the human genome:**
- **SINEs** (short interspersed elements) — 100–300 bp.
- **LINEs** (long interspersed elements) — 6–8 kbp, encode a few genes that catalyze
  transposition.
- **SSR** (simple sequence repeats) — <10 bp, repeated millions of times per cell.

### 1.9 DNA supercoiling and topoisomerases {#ch01-9}
**Supercoiling** — coiling of the helical axis upon itself; also called superhelix.
DNA can be relaxed or supercoiled.

**Topoisomers** — DNAs that differ only in linking number (Lk). **Topoisomerases**
are enzymes that underwind/relax DNA; the degree of supercoiling in the cell is
controlled by topoisomerases.

Advantage of controlled underwinding: it permits DNA to be transiently and locally
melted so the enzymes of DNA replication and transcription can copy/synthesize new
DNA or RNA.

Two classes:
- **Type 1 topoisomerases**
- **Type 2 topoisomerases** (DNA gyrase in *E. coli*)

Cellular DNA is underwound; any deviation from this relaxed state increases the
energy of the DNA molecule ("topological bond"). To change the linking number, a
bond in one of the two DNA strands must be broken.

**Twist and writhe:** Twist = number of helical turns = Lk (relaxed). Writhe = the
number of times the double helix crosses over on itself. L = T + W (linking number =
twist + writhe). The linking number defines the number of times a strand of DNA
winds in the right-handed direction around the helix axis.

Positive vs. negative supercoiling exist as distinct states.

- In **prokaryotes**, plectonemic supercoils predominate (circular chromosome, small
  amount of genetic material).
- In **eukaryotes**, both plectonemic and solenoidal forms are present, but
  solenoidal supercoiling is most effective for compacting DNA.

### 1.10 Chromatin packing {#ch01-10}
Many different orders of chromatin packing give rise to the highly condensed
metaphase chromosome.

**Nucleosomes** are the fundamental organizational units of chromatin. Histone
proteins are rich in positively charged amino acids (20–30% Arg + Lys) and bind DNA
mostly via electrostatic interactions with the phosphodiester backbone. `[figure]`
A possible nucleosome structure diagram shows a clamp-like element acting around the
nucleosome octamer (after Peter J. Russell, *iGenetics*, Fig. 8.17).

**Euchromatin vs. heterochromatin.** Relaxed, transcriptionally active DNA =
euchromatin. Condensed (tightly packed) DNA = heterochromatin.

**Histone acetylation/deacetylation** — histones are acetylated/deacetylated on
lysine residues in the N-terminal tail as part of gene regulation, by "histone
acetyltransferase" (HAT) or "histone deacetylase" (HDAC). The acetyl-group source for
histone acetylation is acetyl-CoA; the acceptor of the acetyl group in deacetylation
is CoA. Acetylation adds a negative charge, neutralizing the positive charge on
histones and decreasing the interaction of histone N-termini with the negatively
charged phosphate backbone of DNA.

### 1.11 DNA Metabolism / DNA Replication — fundamental rules {#ch01-11}
`[figure]` Immediately after the "DNA Metabolism" section title, a full-page circular
map of the *E. coli* chromosome is shown, plotting the map positions (in min, 0–100)
of every major DNA-metabolism gene: *mutL* (mismatch repair), *ssb* (SSB), *uvrA*
(DNA repair), *dnaB* (helicase), *rpoB*/*rpoC* (RNA polymerase subunits), *polA* (DNA
pol I), *uvrD* (helicase/mismatch repair), *mutU*, *dnaP*, *rep* (helicase 3′→5′),
*oriC* (replication origin), *dnaN*/*dnaA* (replication initiation), *recF*
(recombinational repair), *gyrB* (DNA gyrase subunit), *priA* (primosome assembly),
*dam* (methylation), *rpoA*/*rpoD* (RNA pol subunits), *dnaG* (primase), *mutH*/*mutS*
(mismatch repair), *recC*/*recB*/*recD* (recombination), *recA* (recombination),
*ung* (uracil glycosylase), *lig* (DNA ligase), *recO* (recombinational repair),
*gyrA* (DNA gyrase subunit), *nfo* (AP endonuclease), *sbcB* (exonuclease I), *uvrC*
(DNA repair), *ruvA*/*ruvB*/*ruvC* (recombination and recombinational repair),
*holE*/*holA*/*holB*/*holC*/*holD* (DNA pol III subunits), *xthA* (AP endonuclease),
*Ter* (replication termination), *ogt* (O⁶-G alkyltransferase), *umuC*/*umuD* (DNA
pol V), *phr* (DNA photolyase), *dinB* (DNA pol IV), *polB* (DNA pol II), *dnaJ*/
*dnaK*, *polC* (= *dnaE*, DNA pol III subunit), *mutT*, *mutT*. `[handwritten]`
annotation on the figure: "E. coli (Prokaryote) why? ⇒ Circular DNA", and "nucleotide
genes" labeling the gene list.

**Rule 1 — DNA replication is semiconservative.** Idea from Watson & Crick: DNA acts
as a template for replication and transmission of genetic information. The two
strands of the parental molecule separate, each acting as a template for a new
complementary strand. New DNA consists of 1 parental (original) strand + 1 new
strand.

**The Meselson–Stahl experiment** confirmed this: (a) cells grown for many
generations in medium containing only heavy nitrogen (¹⁵N) show a single heavy band
on CsCl density-gradient centrifugation; (b) after transfer to medium with only light
nitrogen (¹⁴N), DNA isolated after one generation equilibrates at a higher position
(hybrid, purple band); (c) a second generation of replication yields two hybrid DNAs
and two light DNAs (confirming semiconservative replication).

**Rule 2 — Replication begins at an origin and proceeds bidirectionally.** The parent
strands are simultaneously unwound and replicated. `[figure]` A diagram directly
illustrates bidirectional vs. unidirectional replication: in the bidirectional case
two replication forks move outward in opposite directions from the origin; in the
unidirectional case one fork moves in a single direction from the origin. An inset
"Key Differences" table compares them:

| Feature | Bidirectional Replication | Unidirectional Replication |
|---|---|---|
| Number of Forks | Two forks moving in opposite directions | One fork moving in a single direction |
| Speed | Faster, due to simultaneous synthesis in two directions | Slower, due to synthesis in one direction |
| Examples | Eukaryotic cells, most bacteria | Plasmids, some phages |

**Replication forks** are dynamic points where parent DNA is unwound and the
separated strands are quickly replicated. For circular DNA molecules, the two
replication forks meet at a point on the side of the circle opposite the origin. DNA
can be selectively denatured at sequences unusually rich in A=T base pairs,
generating a reproducible pattern of single-strand bubbles; replication loops always
initiate at a unique point, termed an origin.

**Rule 3 — DNA synthesis proceeds 5′→3′ and is semicontinuous.** The new DNA strand
is synthesized while the template is read in the opposite (3′→5′) direction.
Elongation starts at the free 3′-hydroxyl of a primer.

- **Leading strand** — synthesized continuously as a single strand from the origin
  toward the opening replication fork.
- **Lagging strand** — synthesized discontinuously, against the overall direction of
  replication, in many short segments (Okazaki fragments), replicated from the
  replication fork back toward the origin.

### 1.12 DNA polymerases {#ch01-12}
DNA is synthesized by DNA polymerases, releasing inorganic pyrophosphate; the growing
duplex is stabilized by base pairing and base stacking.

DNA polymerase activity requires a single unpaired template strand and a primer
strand (an RNA segment complementary to the template) providing a free 3′-hydroxyl
to which a new nucleotide unit is added. Each incoming nucleotide is selected in part
by base pairing to the appropriate template nucleotide; the reaction product has a
new free 3′-hydroxyl, allowing addition of the next nucleotide. The polymerization
reaction is guided by base pairing.

**Fidelity.** Replication is very accurate — in *E. coli*, a mistake occurs roughly
once per 10⁹–10¹⁰ nucleotides against a genome of 4.6×10⁶ bp. Discrimination between
correct and incorrect nucleotides comes from (1) hydrogen bonding (base selection)
and (2) the common geometry of standard A-T and G-C pairs — the polymerase active
site accommodates the correct geometry, and incorrect bases are rejected before a
phosphodiester bond forms. This alone doesn't fully account for replication's high
fidelity — hence **proofreading**: an incorrect nucleotide may hydrogen-bond to the
template base but generally will not fit the active site; the 3′→5′ exonuclease
activity of DNA polymerase removes a mispaired nucleotide (double-check), and the
polymerase resumes.

**E. coli has at least five DNA polymerases.**

- **DNA pol I** — the Klenow fragment retains 5′→3′ polymerase activity and 3′→5′
  exonuclease (proofreading) activity but loses 5′→3′ exonuclease activity. Intact
  DNA pol I's 5′→3′ exonuclease activity can replace a segment of DNA (or RNA)
  paired to the template strand — **nick translation**: DNA synthesis begins at a
  nick (a broken phosphodiester bond leaving a free 3′-OH and free 5′-phosphate);
  pol I extends the non-template strand and moves the nick along the DNA. A nick
  remains where pol I dissociates, later sealed by another enzyme. This activity
  serves both DNA repair and removal of RNA primers during replication (the strand
  being removed — DNA or RNA — is degraded by the 5′→3′ exonuclease while the same
  enzyme's polymerase activity replaces it).
- **DNA pol III** — the replicative polymerase; part of a five-subunit
  clamp-loading complex and a dimer of the β subunit (see Table 25-2 below).

`[figure]` **Table 25-2 — Subunits of DNA Polymerase III of *E. coli***:

| Subunit | Copies/holoenzyme | Mr | Gene | Function |
|---|---|---|---|---|
| α | 2 | 129,900 | *polC* (*dnaE*) | Polymerization activity (mainly) |
| ε | 2 | 27,500 | *dnaQ* (*mutD*) | 3′→5′ proofreading exonuclease |
| θ | 2 | 8,600 | *holE* | Stabilization of ε subunit |
| τ | 2 | 71,100 | *dnaX* | Stable template binding; core enzyme dimerization |
| γ | 1 | 47,500 | *dnaX** | Clamp loader |
| δ | 1 | 38,700 | *holA* | Clamp opener |
| δ′ | 1 | 36,900 | *holB* | Clamp loader |
| χ | 1 | 16,600 | *holC* | Interaction with SSB |
| ψ | 1 | 15,200 | *holD* | Interaction with γ and χ |
| β | 4 | 40,600 | *dnaN* | DNA clamp required for optimal processivity |

α, ε, θ together form the **core polymerase**. The **clamp-loading (γ) complex**
loads β subunits onto the lagging strand at each Okazaki fragment. The γ subunit is
encoded by a portion of the gene for the τ subunit — the amino-terminal 66% of τ has
the same amino acid sequence as γ, generated by a translational frameshifting
mechanism that causes premature translational termination. `[handwritten]`
annotations on this table: "mainly" next to α's polymerization function; a bracket
linking "β-clamp" and "pol III"; a boxed note reading "Clamp-loading (γ) complex that
loads β subunits on lagging strand at each Okazaki fragment"; and an Arabic
annotation reading "عشان ما تفلت" (roughly, "so it doesn't slip off" — describing why
the clamp holds the polymerase on the DNA).

**Enzymes/factors required for DNA replication:**
- **Helicases** — move along DNA and separate the strands, using chemical energy
  from ATP.
- **Topoisomerases** — release the topological stress created by strand separation.
- **Single-strand DNA-binding protein (SSB)** — stabilizes separated strands.
- **Primases** — synthesize the RNA primer segment.
- **DNA ligases** — seal the nick left as a broken phosphodiester bond in the DNA
  backbone.
- **DNA pol I** — removes the RNA primer and replaces it with DNA.

Synthesis of DNA is divided into 3 stages: Initiation, Elongation, Termination.

---

## Ch. 2 — Replication: Initiation, Elongation, Termination; Topoisomerases; Telomeres {#ch02}

*Source: "DNA metabolism-2.pdf" (41p). Continues Lehninger Ch. 25.*

### 2.1 Initiation at the E. coli origin, oriC {#ch02-1}
`[figure]` Table 25-3 — **Proteins Required to Initiate Replication at the E. coli
Origin**:

| Protein | Mr | Subunits | Function |
|---|---|---|---|
| DnaA protein | 52,000 | 1 | Recognizes ori sequence; opens duplex at specific sites in origin |
| DnaB protein (helicase) | 300,000 | 6* | Unwinds DNA |
| DnaC protein | 174,000 | 6* | Required for DnaB binding at origin |
| HU | 19,000 | 2 | Histonelike protein; DNA-binding protein; stimulates initiation |
| FIS | 22,500 | 2* | DNA-binding protein; stimulates initiation |
| IHF | 22,000 | 2 | DNA-binding protein; stimulates initiation |
| Primase (DnaG protein) | 60,000 | 1 | Synthesizes RNA primers |
| Single-stranded DNA-binding protein (SSB) | 75,600 | 4* | Binds single-stranded DNA |
| DNA gyrase (DNA topoisomerase II) | 400,000 | 4 | Relieves torsional strain generated by DNA unwinding |
| Dam methylase | 32,000 | 1 | Methylates (5′)GATC sequences at oriC |

The *E. coli* replication origin (oriC) has an arrangement of sequences including a
**DNA unwinding element (DUE)**.

**Steps of initiation:**
1. Four to five DnaA protein molecules bind to the five 9-bp repeats in the origin;
   then about 20 DnaA molecules (each with a bound ATP) bind and form a protein
   complex, wrapping the DNA around it.
2. The three A-T-rich 13-bp repeats are denatured sequentially.
3. Hexamers of the DnaB protein bind each strand, with the aid of DnaC protein.
4. DnaB's helicase activity further unwinds the DNA in preparation for priming and
   DNA synthesis.

### 2.2 Elongation {#ch02-2}
The **primosome** assembles at this stage.

**Topoisomers** differ in degree of supercoiling — i.e., differ in Lk.

`[figure]` **Mode of action of Type I and Type II topoisomerases.** (A) A Type I
topoisomerase makes a nick in one strand of DNA, passes the intact strand through the
nick, and reseals the gap. (B) A Type II topoisomerase makes a double-stranded break
in the double helix, creating a gate through which a second segment of the helix is
passed.

**Clinical relevance of topoisomerases:** inhibitors of human topoisomerases are used
as chemotherapeutic agents in cancer treatment; bacterial topoisomerase inhibitors
(quinolone antibiotics) treat bacterial infections.

**DNA polymerase III holoenzyme** — additional components enhance its function
(beyond the core polymerase and clamp described in Ch. 1).

### 2.3 Summary — DNA replication {#ch02-3}
1. Parent DNA is first unwound by DNA helicases; the resulting topological stress is
   relieved by topoisomerases.
2. Each separated strand is stabilized by SSB. From here, leading- and lagging-strand
   synthesis diverge sharply.
3. Leading-strand synthesis begins with primase (DnaG) synthesizing a short (10–60
   nt) RNA primer at the origin.
4. Deoxyribonucleotides are added to this primer by DNA pol III; leading-strand
   synthesis proceeds continuously.
5. Lagging-strand synthesis occurs in short Okazaki fragments: an RNA primer is
   synthesized by primase, then DNA pol III adds deoxyribonucleotides. Both strands
   are produced by a single asymmetric DNA pol III dimer, accomplished by looping the
   lagging-strand DNA to bring together the two points of polymerization.

**Final steps in synthesizing lagging-strand segments (prokaryotes):** using the
5′→3′ exonuclease activity (of DNA pol I) to remove RNA primers and fill the gaps.

- **Exonucleases** degrade nucleic acids from one end of the molecule; many operate
  only 5′→3′ or only 3′→5′, removing nucleotides one at a time from a strand's end.
- **Endonucleases** begin degrading at internal sites within a nucleic acid strand,
  reducing it to progressively smaller fragments.

**DNA ligase** catalyzes formation of a phosphodiester bond between a 3′-hydroxyl at
the end of one DNA strand and a 5′-phosphate at the end of another. The phosphate
must first be activated by adenylylation. DNA ligases from viruses and eukaryotes use
ATP; bacterial DNA ligases use NAD.

### 2.4 Termination {#ch02-4}
Binding sites for a protein called **Tus** (terminus utilization substance) halt a
fork on reaching the Tus-Ter complex; the other fork halts when it meets the first
(arrested) fork. The mechanism completing replication of the last segment is
described as not fully known ("replicated by unknown mechanism"). The two daughter
circles can end up **catenated** — topologically interlinked circles.

### 2.5 Eukaryotic replication is more complex {#ch02-5}
- Origins of replication: **autonomously replicating sequences (ARS)**, or
  replicators.
- Several polymerases:
  - **DNA polymerase α** — no 3′→5′ exonuclease activity; synthesizes short primers
    (primase-like role).
  - **DNA polymerase δ** — extends primers; has 3′→5′ exonuclease activity
    (functionally analogous to bacterial pol III).
  - **DNA polymerase ε** — removes the primers of Okazaki fragments on the lagging
    strand (functionally analogous to bacterial pol I).
- **RPA** (replication protein A) is the eukaryotic single-stranded DNA-binding
  protein, analogous to SSB.
- Termination involves synthesis of telomeres.

In the mammalian replication fork, DNA polymerase α (with its primase activity)
synthesizes RNA/DNA primers while DNA polymerase δ is the main extending polymerase;
RPA coats single-stranded DNA.

### 2.6 The end-replication problem and telomeres {#ch02-6}
**The end-replication problem:** telomeres shorten with each S phase, because the
lagging strand cannot be fully primed all the way to the chromosome end.

**Telomeres** are the ends of linear chromosomes; they form a "capped" end that
protects the chromosome end from deterioration. Telomeric repeat sequence:
5′-(T$_x$G$_y$)$_n$-3′ / 3′-(A$_x$C$_y$)$_n$-5′. Telomeres "cap" chromosome ends;
electron microscopy shows a **T-loop** structure at chromosome ends, bound by
telomere-specific proteins including **TRF1** and **TRF2** (telomere repeat binding
factors).

**Importance of telomeres:** they let cells distinguish chromosome ends from broken
DNA — a broken end (mistaken for damage) triggers cell-cycle arrest ("repair or
die").

**Telomeres as a molecular clock.** Cell divisions are finite for normal ("mortal")
cells and effectively infinite for "immortal" cells (a proliferative-capacity
concept). The **Hayflick limit** is the number of times a normal human cell
population will divide before division stops.

How telomeres link to aging: once telomeres shrink to a critical length, cellular
senescence (growth arrest) occurs. Healthy human cells are mortal — they divide a
finite number of times, aging with each division; metabolism slows, the cell ages and
dies (senescence). Telomere length functions as a clock for cellular longevity —
telomere shortening may count the number of times a cell has divided.

**Telomerase** "replenishes" the telomere cap of the DNA. Telomerase (a reverse
transcriptase) is a ribonucleoprotein complex composed of a protein component and an
RNA primer sequence that protects chromosome ends — this RNA template solves the
end-replication problem.

Laboratory evidence: cells in tissue culture given introduced telomerase extended
their telomere length and divided for 250 generations past when they would normally
stop, continuing to divide normally with a normal chromosome number.

Most normal cells do not express telomerase (it is "off") and lose telomeres with
each division. Telomerase is expressed in germ cells, early embryonic cells, stem
cells, epidermal skin cells, and follicular hair cells. Cancer cells do not age
because they switch on telomerase, keeping telomeres intact — expressed by 80–90% of
cancer cells; other cancers use **ALT** (alternative lengthening of telomeres)
mechanisms instead. Clinical telomerase research focuses on accurate cancer diagnosis
and anti-telomerase cancer therapeutics.

In most somatic tissues telomerase is expressed at very low levels or not at all — as
cells divide, telomeres shorten (telomerase and senescence). Short telomeres: the
cell may detect this "uncapping" as DNA damage and then stop growing, enter cellular
senescence, or begin apoptosis (programmed cell death). Telomerase's presence in
cancer cells lets them maintain telomere length while proliferating. Inducers of
cellular senescence include short telomeres (from cell proliferation), DNA damage,
and oncogenes — potential cancer-causing events.

**Telomerase — biomedical uses:** (A) expanding cells for replacement therapies
(burns, joint replacements, etc.); (B) telomerase inhibitors to selectively kill
cancer cells.

---

## Ch. 3 — DNA Repair {#ch03}

*Source: "DNA metabolism-3.pdf" (31p). Lehninger Ch. 25.*

### 3.1 Sources of DNA damage {#ch03-1}
- **Endogenous:** attack by reactive oxygen species (ROS), replication errors.
- **Exogenous:** UV light, x-rays and gamma rays, plant toxins, human-made mutagenic
  chemicals (DNA-intercalating agents, alkylating agents), viruses.

### 3.2 Mutation {#ch03-2}
A permanent change in the nucleotide sequence. Categorized by:
- **(A) Nature of the change:** substitution mutation (transition or transversion);
  insertion or deletion mutation.
- **(B) Effect on the coding sequence:** silent (doesn't alter the amino acid
  encoded); missense (changes the amino acid encoded); nonsense (creates a stop
  codon).

**Transitions** (purine↔purine or pyrimidine↔pyrimidine) vs. **transversions**
(purine↔pyrimidine) are the two classes of base substitution.

### 3.3 Mutations and cancer — the Ames test {#ch03-3}
The **Ames test** measures a chemical's potential to induce mutations in bacteria
(as a proxy for carcinogenicity, based on mutagenicity). A strain of *Salmonella
typhimurium* carrying a mutation that inactivates an enzyme of the histidine
biosynthetic pathway is plated on histidine-free medium — few cells grow. The few
small colonies that do grow on the histidine-free plate (a) carry spontaneous
back-mutations restoring the histidine pathway.

Three identical nutrient plates (b, c, d), inoculated with an equal number of cells,
each receive a filter-paper disk soaked in progressively lower concentrations of a
mutagen. The mutagen greatly increases the back-mutation rate and hence the colony
count. The clear area around the disk marks where mutagen concentration is high
enough to be lethal; as the mutagen diffuses outward it dilutes to sublethal
concentrations that promote back-mutation instead. Mutagens can be compared by their
effect on mutation rate.

### 3.4 Fidelity of DNA replication {#ch03-4}
Maintained by (1) base selection by the polymerase, (2) the 3′→5′ proofreading
exonuclease activity of most DNA polymerases, and (3) specific repair systems for
mismatches left after replication.

**Deamination** reactions that damage bases: deamination of C → uracil; deamination
of A → hypoxanthine; deamination of G → xanthine.

### 3.5 Methyl-directed mismatch repair {#ch03-5}
Newly synthesized (unmethylated) DNA is distinguished from the template by **Dam
methylase** tagging at 5′-GATC (a palindromic sequence — a sequence on
double-stranded DNA where the 5′→3′ reading on one strand matches the 5′→3′ reading
on the complementary strand).

Mechanism: the **MutL** protein forms a complex with **MutS** at the mismatch
(lesion). **MutH** protein binds to MutL and to GATC sequences encountered by the
MutL–MutS complex; DNA on both sides of the mismatch is threaded through the
MutL–MutS complex, forming a DNA loop.

- Mismatch on the 5′ side of the cleavage site → degradation proceeds 3′→5′.
- Mismatch on the 3′ side of the cleavage site → degradation proceeds 5′→3′.
- (Degradation can also proceed in both directions.)

**Eukaryotes:** homologous system — **MSH2** (MutS homolog 2), MSH3, MSH6 are MutS
homologs; MutL homologs are predominantly a heterodimer of **MLH1** (MutL homolog 1)
and **PMS1** (post-meiotic segregation), which bind and stabilize the MSH complexes.
Mutated in cancer → increased mutation rate. Many details of eukaryotic mismatch
repair remain unresolved — in particular, the mechanism identifying the
newly-synthesized strand is unknown, though it does not involve GATC sequences (no
Dam-methylase equivalent).

### 3.6 Base-excision repair {#ch03-6}
Cleaves the N-glycosyl bond, producing an abasic (AP) site. Example: deamination of
cytosine to uracil — uracil is removed by **uracil DNA glycosylases** (4 human forms,
UNG etc.). Repair synthesis then initiates from the free 3′-OH at the resulting nick,
removing (via 5′→3′ exonuclease activity) and replacing the damaged portion of the
strand. This pathway recognizes and repairs damage caused by environmental agents.

### 3.7 Nucleotide excision repair {#ch03-7}
A **dual incision** mechanism: two specific endonucleolytic cleavages bracket a
bulky lesion, creating a nick, then a gap. Three subunits — **UvrA, UvrB, UvrC** —
recognize and remove bulky lesions and pyrimidine dimers.

This pathway is the primary route for repairing many lesion types: pyrimidine dimers
(thymine dimers) and base adducts such as benzo[a]pyrene-guanine (a DNA adduct formed
by cigarette smoke).

**Xeroderma pigmentosum (XP):** a rare inherited disease (pigmented skin lesions,
skin cancer, also neurological abnormalities) due to mutations in genes *XPA–XPG* of
the nucleotide excision repair system — the sole repair pathway for pyrimidine dimers
in humans.

**HNPCC** (hereditary non-polyposis colorectal cancer): an autosomal dominant genetic
disease caused by a mismatch-repair defect. Presents with rectal bleeding, stomach
pain, and cancer-related symptoms (unexplained weight loss, fatigue). Most prevalent
defects: **hMLH1** (human MutL homolog 1) and **hMSH2** (human MutS homolog 2).

**Mutagenic consequence:** O⁶-methylguanine tends to pair with thymine rather than
cytosine during replication, causing G-C → A-T mutations.

### 3.8 Direct repair {#ch03-8}
Repair with no excision/removal of a base or nucleotide.

**(a) Photoreactivation.** Pyrimidine dimers result from a UV-induced reaction;
photolyases use energy from absorbed light to reverse the damage. `[figure]` A
diagram shows a **T-C dimer**: thymine (T) plus cytosine (C), each drawn as their
pyrimidine ring structures, joined by UV light into a cyclobutane-linked dimer (T^C),
reversible by "PR" (photoreactivation).

Mechanism, in order: (1) UV light strikes one of two adjacent pyrimidines, creating a
dimer; DNA photolyases recognize the resulting "kink" in the DNA and bind the site.
(2) When excited by blue light (350–500 nm), the photolyases change conformation,
breaking apart the dimer. The photolyase genes are called *phr* genes. `[figure]` A
detailed 5-step mechanism diagram of photoreactivation (via MTHFpolyGlu and FADH⁻
cofactors) is shown: ① a blue-light photon (300–500 nm) is absorbed by
MTHFpolyGlu, exciting it (*MTHFpolyGlu); ② the excitation energy passes to FADH⁻ in
the active site, producing the excited flavin *FADH⁻; ③ the excited flavin donates an
electron to the cyclobutane pyrimidine dimer, generating an unstable dimer radical
and the flavin radical FADH•; ④ electron rearrangement restores monomeric
pyrimidines (splitting the cyclobutane ring); ⑤ an electron is transferred back to
the flavin radical to regenerate FADH⁻, yielding monomeric pyrimidines in repaired
DNA.

**(b) Repair of alkylation damage.** Direct transfer of the methyl group to the
enzyme's own cysteine residue.

**(c) Direct repair — oxidative demethylation of alkylated nucleotides by the AlkB
protein.** AlkB couples oxidative decarboxylation of α-ketoglutarate to hydroxylation
of the methylated base, directly reverting it to the unmodified base and releasing
formaldehyde (demethylation by AlkB is accompanied by release of CO₂, succinate, and
formaldehyde). There are nine human homologs of AlkB: **ALKBH1–ALKBH8** and **FTO**.

### 3.9 Replication forks meeting DNA damage — the SOS response {#ch03-9}
Most DNA damage is repaired by BER/NER, but a replication fork traveling from origin
to terminus can encounter double-strand breaks/lesions that DNA pol III cannot
continue past — requiring **recombinational DNA repair**. Repair must draw on the
homologous chromosome.

`[figure]` **SOS Repair diagram.** Under normal conditions (no DNA damage), **LexA**
protein represses the SOS operon by binding the "Olex" operator upstream of *lexA*
itself (the repressed SOS operon). A cell-distress signal (DNA damage) induces
**RecA** protease function; RecA inactivates LexA protein. With LexA inactivated, the
SOS DNA repair genes that LexA had repressed are freed for expression (the active SOS
operon) — including genes for error-free DNA repair (e.g. driven by an Olex-*uvrA*
arrangement) and error-prone DNA repair (e.g. an Olex-*umuD* arrangement).

**Two SOS repair outcomes:**
1. **Recombinational DNA repair.**
2. **Error-prone translesion DNA synthesis (TLS).** The UmuD′–UmuC complex (DNA pol
   V) replicates past many lesions that would otherwise block replication; DNA pol
   IV, also induced under the SOS response, is likewise highly error-prone. Proper
   base pairing is nearly impossible under TLS, giving inaccurate repair and a high
   mutation rate. SOS activates UmuD′+UmuC only when all replication forks are
   blocked (the result of extensive DNA damage). Bacterial DNA polymerases IV and V
   belong to a family of TLS polymerases found in all organisms; these enzymes lack
   proofreading exonuclease activity and so have low fidelity. Eukaryotes have other
   TLS polymerases including **pol eta** and **pol iota**.

`[figure]` **Table 25-6 — Genes Induced as Part of the SOS Response in *E. coli***:

*Genes of known function:*

| Gene | Protein encoded / role |
|---|---|
| *polB* (*dinA*) | Polymerization subunit of DNA polymerase II, required for replication restart in recombinational DNA repair |
| *uvrA*, *uvrB* | Encode ABC excinuclease subunits UvrA and UvrB |
| *umuC*, *umuD* | Encode DNA polymerase V |
| *sulA* | Encodes a protein that inhibits cell division, possibly to allow time for DNA repair |
| *recA* | Encodes RecA protein, required for error-prone repair and recombinational repair |
| *dinB* | Encodes DNA polymerase IV |
| *ssb* | Encodes single-stranded DNA-binding protein (SSB) |
| *himA* | Encodes a subunit of integration host factor (IHF), involved in site-specific recombination, replication, transposition, and regulation of gene expression |

*Genes involved in DNA metabolism, role in DNA repair unknown:*

| Gene | Protein encoded / role |
|---|---|
| *uvrD* | Encodes DNA helicase II (DNA-unwinding protein) |
| *recN* | Required for recombinational repair |

---

## Ch. 4 — DNA Recombination {#ch04}

*Source: "DNA metabolism-4.pdf" (23p). Lehninger Ch. 25.*

### 4.1 Overview {#ch04-1}
DNA recombination = rearrangement of genetic information within and among DNA
molecules.

1. **Homologous / general recombination (DNA crossover)** — genetic exchange between
   any two DNA molecules/segments sharing nearly identical sequence.
2. **Site-specific recombination** — exchange occurs only at a particular DNA
   sequence.
3. **Transpositional recombination** — a short DNA segment moves from one
   chromosomal location to another.

**Functions of genetic recombination systems:** (1) specialized DNA repair systems;
(2) maintenance of genetic diversity; (3) regulation of gene expression and promotion
of programmed DNA rearrangements in embryonic development.

### 4.2 Recombination during meiosis {#ch04-2}
**Crossing over** — exchange of genetic information between homologous chromosomes,
via breakage and rejoining. **Spo11** makes a targeted double-strand break in DNA at
intergenic promoter regions (occurring "like a group of four" — i.e. among the four
chromatids of a homologous pair).

`[figure]` A micrograph (with a companion line diagram) shows intertwined sister
chromatids from a mitotic chromosome, labeling **centromeres** and **chromatids** —
illustrating how sister chromatids remain physically linked/intertwined, the
structural backdrop against which crossing-over and recombination occur (electron
micrograph, scale bar 2 µm).

In the recombination pathway during meiosis, the DNA flanking the region containing
the hybrid DNA is not itself recombined. **Branch migration** — the ability of a DNA
strand partially paired with its complement in a duplex to extend that pairing by
displacing the resident strand with which it is homologous — is blocked when it
meets a nonidentical sequence.

**Double-strand break repair model — four key features:**
1. Homologous chromosomes are aligned.
2. A double-strand break in a DNA molecule is enlarged by an exonuclease, leaving a
   single-strand extension with a free 3′-OH at the broken end.
3. The exposed 3′ ends invade the intact duplex DNA of the homolog; this is followed
   by branch migration and/or replication to create a pair of crossover structures
   called **Holliday intermediates** (4-stranded DNA).
4. Cleavage of the two crossovers by resolvase enzymes creates one of two possible
   pairs of complete recombinant products.

**RecA-mediated DNA strand exchange:** RecA forms a filament on single-stranded DNA;
one strand is transferred to the RecA-bound single strand, the other strand is
displaced, and a new duplex forms within the filament (also demonstrated
*in vitro*).

**Non-identical homologs.** The two homologous chromosomes undergoing recombination
need not be identical — the linear array of genes may match, but base sequences in
some genes may differ slightly between alleles. Worked example: one chromosome
carries the hemoglobin A (normal) allele, the other hemoglobin S (sickle cell
anemia) — a difference of one bp among millions. The A→T substitution causes
glutamic acid to be replaced by valine.

**Recombinational repair of stalled/blocked replication forks.** Most DNA damage is
repaired by BER/NER, but a replication fork can encounter double-strand
breaks/lesions that DNA pol III cannot continue past. **Origin-independent restart of
replication** uses a complex of 7 proteins (PriA, PriC, DnaB, DnaC, DnaG, DnaT) plus
DNA pol II — repair of the stalled/blocked fork transitions from replication →
recombinational repair → replication.

### 4.3 Site-specific recombination {#ch04-3}
Limited to specific sequences. Steps: (1) recombinase subunits bind to a specific
sequence, the recombination site; (2) the nucleophile is the –OH group of an
active-site Tyr residue, forming a phospho-Tyr link between protein and DNA; (3) the
cleaved strands join new partners, producing a Holliday intermediate; the first two
steps then repeat. **Recombinase** functions as an endonuclease and ligase in one
package.

A characteristic feature of "classical" site-specific recombination: the strand
breaking/rejoining reactions are **conservative** — they require no DNA synthesis or
degradation, and no enzyme cofactors.

### 4.4 Transpositional recombination {#ch04-4}
Allows movement of transposable elements (transposons) from one chromosomal location
(the donor site) to another, on the same or a different chromosome (the target
site).

**Bacterial transposable genetic elements:**
- **Simple transposons** — contain only the sequence required for transposition (the
  gene for transposase).
- **Complex transposons** — contain one or more genes in addition to those needed
  for transposition, e.g. genes conferring antibiotic resistance.

A **staggered cut** (not directly across from each other on the two strands)
produces short **direct repeats** flanking the inserted element. Two general
pathways for transposition exist. A **cointegrate** intermediate contains two
complete copies of the transposon.

**Eukaryotic transpositional recombination — two classes:**
- **Class I:** retrotransposons.
- **Class II:** DNA transposons.

`[figure]` The deck's final page diagrams the mechanism of a Class II (DNA)
transposon insertion step by step: target DNA is cut by transposase in a
**sticky-end cut** (staggered, leaving short single-stranded overhangs); the
intermediate (transposon) DNA is ligated in by transposase; the remaining gaps are
filled by DNA polymerase; the result leaves short **direct repeats** flanking the
inserted element on both sides — the same staggered-cut/direct-repeat mechanism
described above, shown in full structural detail.

---

## Ch. 5 — RNA Synthesis (Transcription) {#ch05}

*Source: "RNA metabolism-1.pdf" (33p). Lehninger Ch. 26.*

### 5.1 The three roles of RNA in protein synthesis {#ch05-1}
- **mRNA** — encodes the amino acid sequence of one or more polypeptides specified
  by a gene or set of genes.
- **tRNA** — reads the information encoded in mRNA and transfers the appropriate
  amino acid to a growing polypeptide chain during protein synthesis.
- **rRNA** — constituents of ribosomes.

### 5.2 RNA polymerase mechanism {#ch05-2}
RNA is synthesized by DNA-dependent RNA polymerase. The 3′-OH of the growing chain
acts as a nucleophile attacking the phosphate of the incoming rNTP; pyrophosphate
"peels off".

**Transcription vs. replication — similarities:** (1) polarity (direction of
synthesis) and use of a template; (2) both have initiation, elongation, and
termination phases.

**Transcription vs. replication — differences:** (1) transcription does not require
a primer and generally involves only limited segments of a DNA molecule; (2) within
a transcribed segment, only one DNA strand serves as template.

Only particular genes or groups of genes are transcribed at any one time; some
portions of the genome are never transcribed. Initiation starts at a **promoter**,
followed by elongation, then termination.

Reaction: (NMP)ₙ + NTP → (NMP)ₙ₊₁ + PPi.

### 5.3 The transcription bubble {#ch05-3}
1. The DNA duplex must unwind over a short distance, forming a transcription
   "bubble" (about 17 bp unwound).
2. An 8-bp RNA–DNA hybrid forms within this unwound region.
3. Elongation of a transcript by *E. coli* RNA polymerase proceeds at 50–90
   nucleotides/second.
4. Movement of the transcription bubble requires considerable strand rotation of the
   nucleic acid molecules.
5. The moving RNA polymerase generates waves of positive supercoiling ahead of the
   bubble and negative supercoiling behind it.
6. The topological problems created by transcription are relieved by
   topoisomerases.

The RNA transcript is synthesized on the **template strand** and is identical in
sequence (with U replacing T) to the non-template strand, or **coding strand**. The
coding strand for a particular gene may be located on either strand of a given
chromosome (illustrated via the organization of coding information in the adenovirus
genome).

### 5.4 E. coli RNA polymerase and promoters {#ch05-4}
RNA polymerase **holoenzyme** = five core subunits + a **sigma (σ) factor**, which
directs the enzyme to specific binding sites on DNA; the core subunits are constant,
sigma is variable. RNA polymerase lacks 3′→5′ proofreading activity. Different sigma
factors direct transcription of different gene sets — e.g. σ⁷⁰ (housekeeping genes),
σ³² (heat-shock proteins), etc.

**E. coli promoters** carry several recognition sequences: the **-10 region**, the
**-35 region**, and (not present in all bacteria) the **UP element**. Position +1 is
the first nucleotide encoding the RNA transcript; the promoter region extends
roughly from -70 to +30. Variations in the consensus sequence affect RNA polymerase
binding efficiency and transcription-initiation efficiency — the promoter sequence
sets a basal expression level that varies greatly gene to gene.

**Initiation mechanism:** promoter DNA is first stably bound but not unwound; a
12–15 bp region within the -10 region to position +2/+3 is then unwound. Once the σ
subunit is released and the polymerase leaves the promoter, it becomes committed to
RNA elongation — the movement of the transcription complex away from the promoter
marks initiated transcription ("hybrid" formation, the RNA-DNA hybrid within the
bubble).

### 5.5 Termination of transcription in E. coli {#ch05-5}
Two mechanisms:
1. **Rho-independent** — produces an RNA transcript with self-complementary
   sequences, permitting formation of a stem-and-loop (hairpin) structure. This
   occurs at characteristic sequences: a hairpin followed by a run of repeated A
   residues in the template strand (giving a U-rich run in the transcript). The
   resulting A•U hybrid region at the 3′ end of the new transcript is relatively
   unstable, so the RNA dissociates completely, terminating transcription.
2. **Rho (ρ)-dependent** — Rho is an ATP-dependent helicase; the Rho protein
   associates with the RNA at specific binding sites and migrates 5′→3′ until it
   reaches the transcription complex paused at a termination site. `[figure]` A
   step-by-step diagram of **Rho-dependent termination** shows: RNA polymerase
   transcribes DNA; Rho attaches to a recognition site on the nascent RNA; Rho moves
   along the RNA, following RNA polymerase; RNA polymerase pauses at the terminator
   and Rho catches up; Rho unwinds the DNA–RNA hybrid in the transcription bubble;
   termination follows — RNA polymerase, Rho, and the RNA transcript are all
   released. Rho-dependent terminators lack the repeated-A-residue sequence found in
   rho-independent terminators. Rho's ATP-dependent RNA–DNA helicase activity
   promotes its own translocation along the RNA, hydrolyzing ATP during termination.

### 5.6 Eukaryotic RNA polymerases {#ch05-6}
Three types:
- **RNA pol I** — synthesizes pre-rRNA, the precursor containing 18S, 5.8S, and 28S
  rRNAs.
- **RNA pol II** — synthesizes mRNAs; requires an array of additional proteins
  (transcription factors) to form the active transcription complex.
- **RNA pol III** — makes tRNAs, 5S rRNA, and some other small specialized RNAs.

**Eukaryotic promoters** feature the **TATA box** and an **Inr** (initiator) element
(a pyrimidine, then any nucleotide, at the position marking transcription start).

**RNA pol II** is a huge, 12-subunit enzyme: RPB1 (≈ bacterial β′), RPB2 (≈ bacterial
β), RPB3…RPB11 (two of which resemble the two bacterial α subunits). RPB1 carries a
**carboxyl-terminal domain (CTD)**.

**Transcription at RNA pol II promoters — mechanism:**
1. Sequential assembly of TBP (often with TFIIA), TFIIB, TFIIF plus Pol II, TFIIE,
   and TFIIH — forming a **closed complex**.
2. Within the complex, DNA is unwound at the Inr region by the helicase activity of
   TFIIH (and perhaps TFIIE) — forming an **open complex**.
3. The CTD of the Pol II subunit is phosphorylated by TFIIH (a kinase activity of
   TFIIH), producing a conformational change that initiates transcription.
4. The polymerase escapes the promoter and begins elongation, accompanied by release
   of many transcription factors and enhanced by elongation factors.
5. After termination, Pol II is released, dephosphorylated, and recycled.

**Genetic loss of certain TFIIH subunits causes xeroderma pigmentosum (XP)** — TFIIH
is not only involved in open-complex formation but, when RNA pol II halts at a DNA
lesion, can interact with the lesion and recruit the entire nucleotide-excision
repair complex.

### 5.7 mRNA modification in eukaryotes — overview {#ch05-7}
1. **Capping** — the 5′ cap is added before synthesis of the primary transcript is
   complete.
2. **Splicing** — introns are removed from the primary transcript and exons are
   joined into a continuous sequence, yielding a functional polypeptide; alternative
   splicing has regulatory significance.
3. **Polyadenylation** — the 3′ end of the mRNA is cleaved, and 80–250 A residues are
   added to create a poly(A) tail.

Splicing can occur either before or after the cleavage-and-polyadenylation steps.

### 5.8 Selective inhibition of RNA polymerase {#ch05-8}
- **Intercalating agents** — intercalate into the double helix, deforming the DNA
  and inhibiting RNA elongation. `[figure]` **Actinomycin** is shown intercalated
  between DNA bases, wedged into the backbone.
- **Rifampicin** inhibits bacterial RNA synthesis by binding the β subunit of
  bacterial RNA polymerase, preventing the promoter-clearance step of transcription.

### 5.9 DNA footprinting {#ch05-9}
Identifies the DNA sequences bound by a particular protein, typically using **DNase**
protection — RNA polymerase, for instance, leaves its own footprint on a promoter.

---

## Ch. 6 — RNA Processing {#ch06}

*Source: "RNA metabolism-2.pdf" (34p). Lehninger Ch. 26.*

### 6.1 5′ capping of mRNA {#ch06-1}
The 5′ cap has an unusual 5′,5′-triphosphate linkage. Functions: protects mRNA from
ribonucleases; participates in binding the mRNA to the ribosome to initiate
translation (promotes translation); regulates nuclear export.

**Cap-synthesizing enzymes:** phosphohydrolase, guanylyltransferase,
guanine-7-methyltransferase, 2′-O-methyltransferase. The methyl donor is
S-adenosylmethionine (releasing S-adenosylhomocysteine). All these reactions occur
very early in transcription, after the first 20–30 nucleotides of the transcript
have been added.

The capping enzymes and the transcript's 5′ end stay associated with the RNA pol II
CTD until the cap is synthesized; the capped 5′ end is then released from the
capping enzymes and bound by the cap-binding complex.

### 6.2 RNA splicing {#ch06-2}
Four classes of introns:
- **Group I and Group II** — self-splicing, can be found in bacteria. Group I uses a
  guanosine cofactor. Neither group requires protein or a cofactor such as ATP for
  splicing; both mechanisms involve two transesterification reaction steps.
  - Group I introns occur in nuclear, mitochondrial genes coding for rRNAs, mRNAs,
    and tRNAs.
  - Group II introns are generally found in the primary transcripts of mitochondrial
    mRNAs.
- **Group III (spliceosomal introns)** — the largest class, found in nuclear mRNA
  primary transcripts, processed by the **spliceosome** — a large complex of
  specialized RNA-protein complexes called **small nuclear ribonucleoproteins
  (snRNPs)**. Each snRNP contains one of the **small nuclear RNAs (snRNAs)**: U1, U2,
  U4, U5, U6.
- **Class four (tRNA)** — the only class spliced by enzymes. The splicing reaction
  requires ATP and an endonuclease: the splicing endonuclease cleaves the
  phosphodiester bonds at both intron ends, and the two exons are joined by a
  mechanism resembling the DNA ligase reaction.

**Transesterification** — a ribose 2′- or 3′-hydroxyl group makes a nucleophilic
attack on a phosphorus, forming a new phosphodiester bond at the expense of the old
one, maintaining the energy balance.

**Group I introns:** splicing uses GTP/GDP/GMP as a guanine nucleoside cofactor,
forming a 3′,5′-phosphodiester bond to yield the mature RNA — intron-mediated, no
protein enzyme, no spliceosome required.

**Group II introns:** splicing proceeds via a **branch point**, forming a lariat
intermediate to yield the mature RNA.

**Group III (spliceosomal) introns:** small nuclear sequences mark the splice sites.
U1 snRNP has a 5′-end sequence complementary to the 5′ splice site of the intron; U2
snRNP pairs with the intron at a position encompassing the branch-point A residue.
ATP is required for spliceosome assembly (not for the cleavage chemistry itself).
Internal rearrangements convert this assembly into an active spliceosome in which U1
and U4 have been expelled and U6 is paired with both the 5′ splice site and U2,
producing the lariat intermediate and mature mRNA. Coordination of splicing and
transcription provides a mechanism for bringing the two splice sites together.

### 6.3 Polyadenylation {#ch06-3}
The RNA is cleaved by an endonuclease 10–30 nucleotides downstream of the sequence
**AAUAAA**. This cleavage-signal sequence is bound by an enzyme complex that includes
the endonuclease and a polyadenylate polymerase. The polyadenylate polymerase
synthesizes a poly(A) tail 80–250 nucleotides long, starting at the cleavage site;
this enzyme requires no template but does require the cleaved mRNA as a primer.

### 6.4 Alternative processing {#ch06-4}
Alternative processing of complex eukaryotic transcripts (determined by processing
factors) allows a single gene to encode multiple proteins, via alternative
cleavage/polyadenylation patterns and alternative splicing patterns. Worked example:
the **calcitonin gene transcript in rats** — the primary transcript has two poly(A)
sites; one predominates in the brain, the other in the thyroid. In the thyroid,
splicing eliminates the calcitonin exon (exon 4, "exon skipping"); in the brain, exon
4 is retained and the transcript instead produces **CGRP** (calcitonin-gene-related
peptide).

### 6.5 Gene regulation basics {#ch06-5}
Each cell expresses only a fraction of its genes; the rest are repressed. This
on/off process is gene regulation. **Housekeeping genes** are expressed
constitutively, essential for basic cell replication/growth processes.
**Inducible genes** are expressed only when activated by inducers or cellular
factors. (Regulatory elements: promoters, enhancers, silencers, etc.)

### 6.6 RNA degradation {#ch06-6}
RNA concentration depends on (1) rate of synthesis and (2) rate of degradation
(ensuring mRNA doesn't build up in the cell).
- **Prokaryotes:** endoribonucleases and 3′→5′ exoribonucleases.
- **Eukaryotes:** shortening of the poly(A) tail and decapping the 5′ end, then
  3′→5′ exoribonuclease activity (about 10 types, forming the **exosome**); in lower
  eukaryotes a 5′→3′ exoribonuclease also contributes.

### 6.7 Processing of rRNAs and tRNAs {#ch06-7}
tRNA processing occurs in both bacteria and eukaryotes; splicing of an intron is
found in some eukaryotic tRNAs, catalyzed by a **ribozyme**.

Some modified bases of rRNAs and tRNAs are produced by post-transcriptional
reactions — the most common nucleoside modifications. One such modified nucleoside
is commonly found in tRNA, associated with thymidine and cytosine in the TΨC arm,
one of the invariant regions of tRNA; its precise function is unclear.

**rRNA processing in prokaryotes:** all rRNA and some tRNA arise from a single 30S
RNA precursor of about 6,500 nucleotides, processed by **RNase III, RNase P, and
RNase E**.

`[figure]` A composite diagram compares **bacterial (70S) vs. eukaryotic (80S)
ribosome** composition:

| | Bacterial ribosome | Eukaryotic ribosome |
|---|---|---|
| Whole | 70S, Mr 2.7×10⁶ | 80S, Mr 4.2×10⁶ |
| Large subunit | 50S, Mr 1.8×10⁶ — 5S rRNA (120 nt), 23S rRNA (3,200 nt), 36 proteins | 60S, Mr 2.8×10⁶ — 5S rRNA (120 nt), 28S rRNA (4,700 nt), 5.8S rRNA (160 nt), ~49 proteins |
| Small subunit | 30S, Mr 0.9×10⁶ — 16S rRNA (1,540 nt), 21 proteins | 40S, Mr 1.4×10⁶ — 18S rRNA (1,900 nt), ~33 proteins |

### 6.8 Ribozymes {#ch06-8}
**Ribozymes** (ribonucleic acid enzymes) = catalytic RNA, defined by the minimal
sequence required for catalysis. Classified into **natural** and **artificial**
ribozymes.
- **Natural ribozymes** include: peptidyl transferase (23S rRNA), RNase P, Group I
  and Group II introns, the hammerhead ribozyme.
- **Artificial ribozymes** are synthesized in the lab, exploiting RNA's dual nature
  as catalyst and informational polymer.

The **hammerhead ribozyme** (found in plant virus/viroid RNAs) promotes
site-specific self-cleavage; it is a metalloenzyme requiring Mg²⁺ ions. Ribozymes are
inactivated by heating above their melting temperature or by denaturing agents /
complementary oligonucleotides that disrupt normal base pairing.

### 6.9 RNA-dependent RNA replication and reverse transcription {#ch06-9}
Some viral RNAs are replicated by **RNA-dependent RNA polymerase** (= replicase).
Retroviruses and telomerase both use RNA-templated (reverse-transcriptase-type)
synthesis.

**Reverse transcriptase** produces DNA from viral RNA. In retroviral infection of a
mammalian cell, an **integrase** inserts the resulting DNA into the host genome.

**Retrovirus genes:**
- ***gag*** (group-associated antigen) — encodes a long polypeptide cleaved into six
  smaller proteins forming the viral core.
- ***pol*** (polymerase) — encodes the protease that cleaves the long polypeptide,
  the reverse transcriptase, and an integrase (to insert viral DNA into the host
  genome).
- ***env*** (envelope) — encodes the viral envelope proteins.
- **Long terminal repeat (LTR)** — facilitates integration of the viral genome into
  host DNA and contains promoters for viral gene expression.

**HIV and cancer/AIDS:** retroviruses can cause cancer (via oncogenes causing
unregulated cell division, e.g. through a tyrosine kinase) and AIDS. The HIV genome
carries genes that kill the host cell (mostly T lymphocytes), suppressing the immune
system. HIV-encoded reverse transcriptase is unusually error-prone (like RNA
polymerases, it lacks 3′→5′ proofreading).

**Fighting AIDS — reverse transcriptase inhibitors.** **AZT** is a structural analog
of deoxythymidine. AZT is taken up by T lymphocytes and converted to AZT
triphosphate, which competitively inhibits dTTP binding to HIV reverse transcriptase.
AZT is added to the 3′ end of the growing DNA strand, prematurely terminating viral
DNA synthesis because it lacks a 3′-hydroxyl. AZT affects HIV reverse transcription
but not most cellular DNA replication.

---

## Ch. 7 — The Genetic Code and Aminoacyl-tRNA Synthesis {#ch07}

*Source: "Protein metabolism-1.pdf" (31p). Lehninger Ch. 27.*

### 7.1 Transcription and translation, prokaryotes vs. eukaryotes {#ch07-1}
Introductory comparison of the two processes' physical coupling: in prokaryotes,
translation can begin on an mRNA still being transcribed (no nuclear membrane
separating the two processes); in eukaryotes, transcription (nucleus) and
translation (cytoplasm) are physically and temporally separated.

### 7.2 The genetic code {#ch07-2}
The four code letters of DNA encode 20 amino acids via **codons** (triplets of
nucleotides) — 64 possible combinations. There is no punctuation between codons for
successive amino acid residues. tRNAs act as **adaptors** between codon and amino
acid.

Translation requires adaptor molecules (tRNAs); a minimum of 32 tRNAs are required
to translate all 61 sense codons (31 to encode the amino acids, plus 1 for
initiation).

The code is **non-overlapping**. **Reading frame:** all mRNAs have three potential
reading frames (sets of 3 nucleotides read as a codon); only one reading frame is
correct for encoding the intended amino acid sequence. A reading frame free of a
termination codon for 50 or more codons is called an **open reading frame (ORF)**.

**Cracking the genetic code — Marshall Nirenberg** identified the codon specifying
each amino acid, using synthetic RNA molecules of a single repeated nucleotide and
of specific 3-base sequences to determine which amino acid each codon encodes; the
amino acids encoded by all 61 sense codons were determined this way. **Polynucleotide
phosphorylase** (which does not need a template) catalyzes (NMP)ₙ + NDP ↔ (NMP)ₙ₊₁ +
Pi, producing the synthetic mRNAs used in these experiments (the base sequences of
codons were deduced from experiments with synthetic mRNAs of known composition and
sequence).

**Properties of the genetic code:**
- **Triplet codons** code for a single amino acid (e.g. UUU = Phe).
- **The code is commaless** (e.g. AUGUUU reads as Met-Phe with no separator).
- Only Met and Trp have a single codon each; all other amino acids have 2–6 triplet
  codons (e.g. Ser: UCU, UCA, UCG, UCC — differing at the "wobble" position).
- The dictionary of codon assignments is fixed — UUU is *always* Phe, never
  sometimes.
- **Nonsense codons** (UAA, UAG, UGA) are stop points.
- The genetic code is **nearly universal**. Exception: mitochondria contain their
  own DNA and use a slightly different code — e.g. UGA encodes Trp in vertebrate
  mtDNA (instead of acting as a stop codon).
- **AUG** is the initiation codon — the most common signal for beginning a
  polypeptide in all cells.
- The code is **degenerate**: multiple codons exist for almost every amino acid.

### 7.3 tRNA structure {#ch07-3}
tRNAs (76–90 nucleotides) fold into a characteristic **cloverleaf** secondary
structure, featuring the D arm (named for the modified base **dihydrouridine**) and
other conserved features (e.g. methylguanylate). A tRNA can carry a specific amino
acid esterified via its carboxyl group to the 2′- or 3′-hydroxyl of the terminal A
residue at the tRNA's 3′ end. The anticodon loop interacts with the large subunit
rRNA (during decoding). tRNA's actual three-dimensional structure is an L-shape (the
cloverleaf is only the 2D secondary-structure representation).

Some of the most common nucleoside modifications occurring post-transcriptionally in
tRNAs include conversion to **hypoxanthine** (forming inosine).

### 7.4 The wobble hypothesis {#ch07-4}
1. The first two bases of the mRNA codon establish strong Watson-Crick pairing with
   the corresponding tRNA anticodon bases, providing the primary coding specificity.
2. The **first base of the anticodon** (pairing with the codon's third, "wobble"
   position) determines how many codons a given tRNA can recognize: C or A is
   specific for one codon; U or G allows recognition of two different codons;
   **inosine (I)** permits recognition of three codons.
3. A minimum of 32 tRNAs is needed to translate all 61 codons (31 for amino acids, 1
   for initiation) — consistent with §7.2 above.

### 7.5 Ribosomes and cellular location {#ch07-5}
Translation of mRNA into protein is carried out by ribosomes. In eukaryotes,
translation may occur on free cytoplasmic ribosomes or on ribosomes of the rough
endoplasmic reticulum (RER).

**Protein synthesis proceeds in 5 stages** (named on a section-divider slide; the
stages are activation, initiation, elongation, termination, and post-translational
processing/folding — the last of these covered in Ch. 8).

### 7.6 Activation of the amino acid — aminoacyl-tRNA synthetases {#ch07-6}
Reaction: amino acid + tRNA + ATP + Mg²⁺ → aminoacyl-tRNA + AMP + PPi. This reaction
takes place in the cytosol, not on the ribosome.

**Charging of tRNA** proceeds via an **aminoacyl-AMP** intermediate that remains
bound to the synthetase's active site; the amino acid is then transferred onto the
tRNA to form aminoacyl-tRNA, releasing AMP. The ester linkage both activates the
amino acid and joins it to the tRNA.

Two classes of synthetase differ in how they attach the amino acid:
- **Class I** — transfers the aminoacyl group to the 2′-OH of the terminal A residue
  first, then it moves to the 3′-OH.
- **Class II** — transfers the aminoacyl group directly to the 3′-OH of the terminal
  A residue.

`[figure]` **Table 27-7 — The Two Classes of Aminoacyl-tRNA Synthetases**:

| Class I | | Class II | |
|---|---|---|---|
| Arg | Leu | Ala | Lys |
| Cys | Met | Asn | Phe |
| Gln | Trp | Asp | Pro |
| Glu | Tyr | Gly | Ser |
| Ile | Val | His | Thr |

**Proofreading by aminoacyl-tRNA synthetase.** The identity of the amino acid
attached to a tRNA is not re-checked on the ribosome — protein-synthesis fidelity
therefore relies heavily on the accuracy of the charging reaction itself. Example:
isoleucyl-tRNA synthetase prefers Ile over the similarly-shaped Val by a factor of
200.

**The "second genetic code."** Synthetase specificity is not just for a single
amino acid but also for the correct cognate tRNA — via specific recognition points
on the tRNA read by the synthetase. This tRNA/synthetase interaction is critical to
accurate reading of the genetic code. A short synthetic RNA "minihelix" corresponding
to tRNA^Ala can be charged by its synthetase with the same efficiency as the complete
tRNA — showing the recognition determinants can be quite localized.

### 7.7 Initiator tRNA and the start codon {#ch07-7}
All organisms have two distinct tRNAs for methionine: one used exclusively when
(5′)AUG is the initiation codon for protein synthesis, the other used to code for an
internal Met residue elsewhere in a polypeptide.

In **prokaryotes**, addition of an **N-formyl group** to methionine's amino group
(by transformylase) prevents fMet from entering interior positions in a polypeptide,
while also allowing fMet-tRNA$^{fMet}$ to bind a specific ribosomal initiation site
that accepts neither Met-tRNA$^{Met}$ nor any other aminoacyl-tRNA.

How the single AUG codon determines whether an N-formylmethionine/methionine start
or an internal Met is inserted is resolved by mRNA context, not the codon alone —
specifically the **Shine-Dalgarno sequence**: the mRNA binds the 30S subunit, and the
initiating (5′)AUG is guided to its correct position by this consensus sequence (the
initiation signal).

---

## Ch. 8 — Translation and Post-Translational Processing {#ch08}

*Source: "Protein metabolism-2.pdf" (37p). Lehninger Ch. 27.*

### 8.1 Charging of tRNA (recap) {#ch08-1}
Linking amino acids to their correct tRNAs is catalyzed by aminoacyl-tRNA
synthetases (20 different synthetases, one per amino acid), coupling an amino acid
to its cognate tRNA. Fidelity of coupling depends on the specificity of these 20
enzymes. Two steps: activation of the amino acid, then transfer of the amino acid to
the tRNA.

### 8.2 Initiation (prokaryotes) {#ch08-2}
Initiation of translation requires formation of the **initiation complex**,
including: an initiator tRNA charged with N-formylmethionine, the small and large
ribosomal subunits, and the mRNA strand. The ribosome-binding sequence of the mRNA
is complementary to part of the rRNA (the Shine-Dalgarno interaction, Ch. 7).

**Ribosomal tRNA-binding sites:**
- **P site** — binds the tRNA attached to the growing peptide chain.
- **A site** — binds the tRNA carrying the next amino acid.
- **E site** — binds uncharged (deacylated) tRNA before it leaves the ribosome.

**Formation of the initiation complex:** the A and P sites can bind aminoacyl-tRNAs;
the initiating AUG is positioned at the P site, the only site to which
fMet-tRNA$^{fMet}$ can bind (all other aminoacyl-tRNAs enter via the A site). The E
site is where "uncharged" tRNAs leave during elongation. The large ribosomal subunit
then joins.

`[figure]` **Table 27-8 — Protein Factors Required for Initiation of Translation in
Bacterial and Eukaryotic Cells**:

*Bacterial:*

| Factor | Function |
|---|---|
| IF-1 | Prevents premature binding of tRNAs to the A site |
| IF-2 | Facilitates binding of fMet-tRNA$^{fMet}$ to the 30S ribosomal subunit |
| IF-3 | Binds to the 30S subunit; prevents premature association of the 50S subunit; enhances specificity of the P site for fMet-tRNA$^{fMet}$ |

*Eukaryotic:*

| Factor | Function |
|---|---|
| eIF2 | Facilitates binding of initiating Met-tRNA$^{Met}$ to the 40S ribosomal subunit |
| eIF2B, eIF3 | First factors to bind the 40S subunit; facilitate subsequent steps |
| eIF4A | RNA helicase activity removes mRNA secondary structure to permit binding to the 40S subunit; part of the eIF4F complex |
| eIF4B | Binds mRNA; facilitates scanning of mRNA to locate the first AUG |
| eIF4E | Binds the 5′ cap of mRNA; part of the eIF4F complex |
| eIF4G | Binds eIF4E and poly(A)-binding protein (PAB); part of the eIF4F complex |
| eIF5 | Promotes dissociation of several other initiation factors from the 40S subunit, as a prelude to association of the 60S subunit to form the 80S initiation complex |
| eIF6 | Facilitates dissociation of the inactive 80S ribosome into 40S and 60S subunits |

### 8.3 Elongation {#ch08-3}
Three steps, repeated per residue: (1) codon recognition, (2) peptide bond
formation, (3) translocation. A second aminoacyl-tRNA binds the A site (an event
involving **GTPase activity**, i.e. EF-Tu/GTP delivering the tRNA).

The α-amino group of the amino acid in the A site acts as a nucleophile, displacing
the tRNA in the P site to form the peptide bond — producing a dipeptidyl-tRNA in the
A site; the uncharged tRNA remains (briefly) bound at the P site. The peptide bond is
formed by **peptidyl transferase**, itself a **ribozyme** (an RNA-catalyzed
reaction, not protein-catalyzed).

**Translocation:** the ribosome moves one codon toward the 3′ end of the mRNA — the
tRNA carrying the (now two-residue) peptide moves from the A site to the P site, the
deacylated tRNA moves toward/through the E site, and a new aminoacylated tRNA enters
the A site by anticodon-codon pairing.

**Elongation, restated:** a charged tRNA binds the A site if its anticodon is
complementary to the A-site codon; peptidyl transferase forms the peptide bond; the
ribosome moves down the mRNA 5′→3′.

### 8.4 Termination {#ch08-4}
There is no tRNA for a stop codon. When a stop codon (UAA, UAG, or UGA) reaches the
A site, a **release factor** (RF-1, RF-2, RF-3 in bacteria) binds the A site instead
of a tRNA and: hydrolyzes the terminal peptide–tRNA bond; releases the peptide and
tRNA from the ribosome; causes the ribosomal subunits to dissociate, so initiation
can begin again.

### 8.5 Eukaryotic initiation and elongation {#ch08-5}
**Eukaryotic initiation:** the 3′ and 5′ ends of eukaryotic mRNAs are linked by a
complex of proteins including several initiation factors. The initiating (5′)AUG is
detected by scanning the mRNA from the 5′ end until the first AUG is encountered,
signaling the start of the reading frame. The **eIF4F complex** is involved in this
scanning, using the RNA helicase activity of eIF4A to eliminate secondary structure
in the 5′ untranslated region (5′ UTR, also called the leader sequence; the
downstream non-coding region after the stop codon is the trailer sequence).

**Eukaryotic elongation** is similar to bacteria's, using three elongation factors —
eEF1α, eEF1βγ, eEF2 — analogous to the bacterial EF-Tu, EF-Ts, EF-G respectively.
Eukaryotic ribosomes have no E site; the uncharged tRNA is expelled directly from the
P site.

### 8.6 Polysomes {#ch08-6}
A **polysome** is several ribosomes translating one eukaryotic mRNA molecule
simultaneously, moving from the 5′ end to the 3′ end of the mRNA and synthesizing a
polypeptide from its amino terminus to its carboxyl terminus. Typically an mRNA has
roughly one attached ribosome every 30–40 codons. Polysomes let the cell make several
copies of a polypeptide very quickly. (mRNA is read 5′→3′; the polypeptide grows
amino→carboxyl terminus.)

**Keep in mind:** accurate translation depends on (1) the correct match between
tRNA and amino acid (set by aminoacyl-tRNA synthetase) and (2) the correct match
between the tRNA anticodon and the mRNA codon.

### 8.7 Puromycin and inhibitors of translation {#ch08-7}
**Puromycin** disrupts peptide bond formation: its structure closely resembles the
3′ end of an aminoacyl-tRNA, letting it bind the ribosomal A site and participate in
peptide bond formation, producing **peptidyl-puromycin** — which then falls off the
ribosome, prematurely terminating the growing chain.

`[figure]` **Table 6-4 — Inhibitors of Protein or RNA Synthesis**:

*Acting only on bacteria:*

| Inhibitor | Specific effect |
|---|---|
| Tetracycline | Blocks binding of aminoacyl-tRNA to the A site of the ribosome |
| Streptomycin | Prevents the transition from translation initiation to chain elongation, and also causes miscoding |
| Chloramphenicol | Blocks the peptidyl transferase reaction on ribosomes |
| Erythromycin | Binds in the exit channel of the ribosome, inhibiting elongation of the peptide chain |
| Rifamycin | Blocks initiation of RNA chains by binding RNA polymerase (prevents RNA synthesis) |

*Acting on bacteria and eukaryotes:*

| Inhibitor | Specific effect |
|---|---|
| Puromycin | Causes premature release of nascent polypeptide chains by adding itself to the growing chain end |
| Actinomycin D | Binds DNA and blocks movement of RNA polymerase (prevents RNA synthesis) |

*Acting on eukaryotes but not bacteria:*

| Inhibitor | Specific effect |
|---|---|
| Cycloheximide | Blocks the translocation reaction on ribosomes |
| Anisomycin | Blocks the peptidyl transferase reaction on ribosomes |
| α-Amanitin | Blocks mRNA synthesis by binding preferentially to RNA polymerase II |

Note on this table: ribosomes of eukaryotic mitochondria (and chloroplasts) often
resemble bacterial ribosomes in their sensitivity to inhibitors — so some of these
"bacteria-only" antibiotics can still have deleterious effects on human mitochondria.

### 8.8 Post-translational modification {#ch08-8}
Newly synthesized polypeptide chains undergo folding and processing.

**Categories of post-translational modification:**
- **Proteolytic cleavage** — activation of an inactive hormone (e.g. proinsulin →
  insulin); activation of a zymogen enzyme (e.g. trypsinogen → trypsin); removal of
  a signal sequence (in the ER).
- **Amino acid modification / group addition** — glucosylation (glycoproteins),
  acetylation, phosphorylation (by kinases), hydroxylation (of Pro), methylation,
  addition of a prosthetic group (heme, biotin), addition of an isoprenyl group.
- **Targeting** to the appropriate cell compartment; folding of the polypeptide;
  formation of disulfide (S-S) bonds.

**Glycosylation** occurs mostly in the ER (a small amount of O-glycosylation) but
mostly in the Golgi complex or cytosol for O-glycosylation. A 14-residue core
oligosaccharide is built stepwise, then transferred from a dolichol-phosphate donor
to certain Asn residues in the protein (N-glycosylation); a small-molecule mimic of
UDP-GlcNAc can block this first step.

**Phosphorylation** adds negative charges to polypeptides. Examples: casein is
phosphorylated on serine (P-Ser), which binds Ca²⁺; phosphorylation also serves as an
activation mechanism for regulatory proteins (via ATP).

**Carboxylation and methylation.** The blood-clotting protein **prothrombin**
contains a number of γ-carboxyglutamate residues — extra carboxyl groups added to Glu
residues, allowing it to bind Ca²⁺ (a related mechanism to how calmodulin binds
Ca²⁺).

**Cleavage of the signal sequence:** the **C-peptide** is a short 31-amino-acid
polypeptide connecting insulin's A-chain to its B-chain within proinsulin.

**Chaperones in protein folding** prevent newly synthesized polypeptide chains from
aggregating into nonfunctional structures. **Heat-shock proteins** (e.g. Hsp60) are
expressed in response to elevated temperature and assist folding in an ADP/ATP cycle.

### 8.9 Protein targeting {#ch08-9}
Newly synthesized proteins are targeted to different cellular locations via: a
peptide signal sequence (usually at the amino terminus); the **signal recognition
particle (SRP)**, which binds the signal peptide; modification in the ER; further
modification and sorting in the Golgi complex.

The amino-terminal signal sequence directing translocation into the ER typically
carries 10–15 hydrophobic amino acids plus 1–2 basic/positively charged amino acids.
Mechanistically: SRP brings the signal peptide and its attached ribosome to the ER;
SRP helps direct the ribosome to the ER and is later recycled.

Lysosomal acid hydrolases are sorted in the Golgi complex based on the chemical
marker **mannose-6-phosphate** — first attached in the ER, with the phosphate added
in the Golgi.

**Nuclear import** (signal not cleaved) applies to proteins such as ribosomal
proteins, directed by a **nuclear localization signal**.

### 8.10 Protein degradation {#ch08-10}
Protein degradation prevents buildup of abnormal/unwanted proteins and permits
recycling of amino acids. Regulated by: the **N-end rule**, the **lysosome**, and
**ubiquitination**.

**N-end rule:** the identity of the first residue remaining after removal of the
amino-terminal Met residue (and any further post-translational proteolytic
processing of the amino terminus) has a profound influence on the protein's
half-life.

**Ubiquitin-proteasome pathway:** **ubiquitin** is a small, 76-amino-acid protein
that tags proteins for degradation by the **26S proteasome**, composed of a **19S
regulatory particle** (at each end) and a **20S core particle**.

---

## Ch. 9 — Molecular Techniques (PCR, Restriction Enzymes, DNA Sequencing) {#ch09}

*Source: "Techniques.pdf" (41p). No textbook chapter cited in the source.*

### 9.1 Transposition mechanisms {#ch09-1}
Section divider only, pointing to external video resources on transposition
mechanisms (no additional transcribable content on this slide itself — see Ch. 4 for
the transposition mechanism as covered in the lecture material proper).

### 9.2 Polymerase Chain Reaction (PCR) {#ch09-2}
PCR amplifies a particular piece of DNA — making numerous copies of a DNA segment.
PCR can make billions of copies of a target DNA sequence in a few hours. Invented in
1984 to make numerous copies of DNA fragments in the laboratory; now an integral
part of molecular biology, with vast applications.

**PCR vs. DNA replication.** PCR is a laboratory ("*in vitro*", i.e. in a test tube)
version of DNA replication in cells ("*in vivo*", occurring in a living cell).

**Key enzymes involved in (cellular) DNA replication** (for comparison): DNA
polymerase, DNA ligase, primase, helicase, topoisomerase, single-strand binding
protein.

**Components needed for PCR:**
1. DNA of interest, containing the target sequence to be copied.
2. A heat-stable DNA polymerase (e.g. Taq polymerase).
3. All four nucleotide triphosphates (dNTPs).
4. Buffer + MgCl₂.
5. Two short single-stranded DNA primers.
6. Thin-walled tubes.
7. A thermal cycler (rapidly changes temperature).

All components (DNA, polymerase, buffer, dNTPs, primers) are combined in a
thin-walled tube, placed in the PCR thermal cycler.

**The three main PCR steps**, repeated 20–40 times per reaction (25 cycles typically
takes ~2 hours and amplifies the target DNA fragment ~100,000-fold):
1. **Denature DNA** — at 95°C, the two DNA strands separate (mimics helicase
   function in the cell).
2. **Primers anneal** — at 40–65°C, primers bind their complementary sequences on
   the single DNA strands.
3. **Extension** — at 72°C, DNA polymerase extends the DNA chain by adding
   nucleotides to the 3′ ends of the primers, in the 5′→3′ direction.

**Heat-stable DNA polymerase.** Because PCR involves very high temperatures, it
requires a heat-stable DNA polymerase — most DNA polymerases would denature (and
lose function) at PCR's high temperatures. **Taq DNA polymerase** was purified from
the hot-springs bacterium *Thermus aquaticus* in 1976; it has maximal enzymatic
activity at 75–80°C, with substantially reduced activity at lower temperatures.

**Primer annealing.** Primers bind complementary sequences on the target DNA. One
primer (forward) is complementary to one strand at one end of the target sequence;
the other (reverse) is complementary to the other strand at the target sequence's
other end.

**Fragment size** is determined by primer placement: the PCR reaction amplifies the
DNA section lying between the two primers. Given a known DNA sequence, primers can
be designed to amplify any piece of an organism's DNA; optimal amplicon size for
general applications is 300–1000 bp.

**More about primers:**
- Short, single-stranded DNA molecules, 18–30 bp, manufactured commercially to match
  any DNA sequence; sequence-specific (bind a particular genomic sequence).
- Longer primers (18→30 bp) are more selective.
- DNA polymerase requires primers to initiate replication.
- Design guidelines: G/C content 40–60%; avoid complementary sequences within/between
  primers (especially at the 3′ end); avoid mismatches at the 3′ end; avoid 3 or more
  G/C residues at the 3′ end; avoid a 3′-terminal T.

**Extension step, in detail:** DNA polymerase catalyzes strand extension in the
5′→3′ direction, starting at the primers, adding the appropriate complementary
nucleotide (A-T, C-G pairing). The next PCR cycle begins by denaturing the new DNA
strands formed in the previous cycle.

**Exponential amplification.** The DNA of interest is amplified by a power of 2 each
PCR cycle — 5 cycles of PCR give 2⁵ (64) copies; 40 cycles give 2⁴⁰ copies.

A **DNA ladder** is a solution of DNA molecules of varying, known lengths, used
predominantly in gel electrophoresis (as a size reference for the PCR product).

**PCR applications:** diagnosis, genetic counseling, forensic medicine (STR typing
and genetic fingerprinting, including paternity testing).

### 9.3 RT-PCR {#ch09-3}
Used to determine the expression level of target genes. **Conversion of mRNA to
cDNA by reverse transcription:** an oligo-dT primer binds the mRNA's poly(A) tail;
reverse transcriptase (RT) copies the first cDNA strand; RT then digests and
displaces the mRNA and copies the second cDNA strand, yielding double-stranded cDNA.
This cDNA can then be PCR-amplified using the standard denature (96°C) → anneal
(50°C) → Taq-polymerase-extend (72°C) cycle.

### 9.4 Restriction enzymes {#ch09-4}
Also called **restriction endonucleases** — "molecular scissors" discovered in
bacteria in 1962. Bacteria use restriction enzymes to kill invading viruses, cutting
viral DNA into useless fragments. About 3,000 restriction enzymes have been
identified; many are purified and available commercially.

**Methylation** protects a bacterium's own DNA from its own restriction enzymes
(the enzyme's recognition sequence in the host genome is methylated, blocking
cleavage there) — this is the answer to why bacteria don't destroy their own DNA.

**Recognition sites have symmetry (palindromic).** Example — the **BamHI** site:
5′-GGATCC-3′ / 3′-CCTAGG-5′. Enzymes recognize specific 4–8 bp sequences.
- Some enzymes cut in a staggered fashion, producing **"sticky ends"** (cohesive
  ends) — e.g. **EcoRI**: 5′…GAATTC…3′ / 3′…CTTAAG…5′.
- Some enzymes cut directly across, producing **"blunt ends"** — e.g. **PvuII**:
  5′…CAGCTG…3′ / 3′…GTCGAC…5′.

### 9.5 Restriction Fragment Length Polymorphism (RFLP) {#ch09-5}
**RFLP protocol** (as given): (1) combine, in order — PCR reaction mixture (10 µl,
~0.1–0.5 µg DNA), nuclease-free water (16–17 µl), 10X restriction-enzyme buffer,
restriction enzyme (1–2 µl, 10–20 U), total volume 30 µl; (2) mix gently and spin
down briefly; (3) incubate at the optimal reaction temperature for 1–16 hours.

**RFLP concept.** Restriction-site recognition detects the presence of a sequence
change — e.g. a G→A change that creates an EcoRI site. On an agarose gel, "U" =
uncut, "C" = cut; comparing uncut/cut band patterns across a normal (NL) sequence, a
homozygous mutant (Mut), and a heterozygote (Het) reveals the genotype. This is a
general method for **detection of mutations** via RFLP.

**Worked clinical example:** agarose gel electrophoresis for the **VKORC1 G>A**
polymorphism, detected by PCR-RFLP using the restriction enzyme **MspI**. Lanes 1 and
4: AA (homozygous mutant); lane 3: AG (heterozygous); lane 2: GG (homozygous wild
type).

### 9.6 DNA sequencing — the Sanger (dideoxy) method {#ch09-6}
Also called **chain-termination sequencing**.

**Four steps:** (1) denaturation; (2) primer attachment and extension of bases; (3)
termination (via ddNTP incorporation); (4) gel electrophoresis.

**Mechanism.** A normal nucleotide's 3′-OH can be used to form the next
phosphodiester bond; a **ddNTP** (2′,3′-dideoxynucleotide) has no 3′-hydroxyl, so DNA
synthesis terminates wherever one is incorporated. Enough ddNTP is added so that each
one is randomly and completely incorporated at each possible base position across a
population of template molecules, producing a nested set of fragments of every
possible length.

`[figure]` A diagram walks through the classical 4-tube Sanger reaction: a
primer/template pair is combined with DNA polymerase and all 4 dNTPs (100 µM), then
split across four tubes, each spiked with one dideoxynucleotide at low concentration
(1 µM): +ddATP, +ddGTP, +ddTTP, +ddCTP. Each tube produces a ladder of
fragments all terminating in the same base (A, G, T, or C respectively, shown
stacked as "…etc" ladders under each tube) — the products are then denatured and
separated by electrophoresis.

**The four reaction tubes, restated:**
- "G" tube — all four dNTPs + ddGTP + DNA polymerase.
- "A" tube — all four dNTPs + ddATP + DNA polymerase.
- "T" tube — all four dNTPs + ddTTP + DNA polymerase.
- "C" tube — all four dNTPs + ddCTP + DNA polymerase.

Each tube yields a mixture of fragments of different lengths, all ending in that
tube's specific base; larger fragments migrate less far, shorter fragments migrate
further on the gel. **The gel is read from bottom to top** (shortest fragment = most
5′ position, read first).

**Automated DNA sequencing** uses four different fluorescent ddNTPs, allowing
simultaneous detection of all four reactions in a single sample/lane (rather than 4
separate lanes).

---

## Ch. 10 — Introduction to Genetics {#ch10}

*Source: "1.Introduction to Genetics.pdf" (30p).*

### 10.1 What is genetics {#ch10-1}
**Genetics** = the scientific study of heredity, the process by which a parent
passes certain genes onto their children. Children inherit their biological
parents' genes, which express specific traits — physical characteristics and
genetic disorders among them.

The cell is the smallest unit of life: all life is composed of cells, and cells
arise only from cells.

### 10.2 Chromosomes and karyotypes {#ch10-2}
A pair of **homologous chromosomes** shares a **locus** (the position of a gene)
and carries **alleles** (alternative forms of a gene) at that locus.

`[figure]` A functional chromosome diagram: at times a chromosome consists of a
single chromatid, at other times (after replication) of two sister chromatids
joined at the **centromere**, each ending in a **telomere** (the stable end of the
chromosome). At the centromere, **kinetochores** form and **spindle microtubules**
attach.

**Karyotype** — a display or photomicrograph of an individual's somatic-cell
metaphase chromosomes, arranged in a standard sequence (usually by number, size,
and type).

**Preparing a karyotype:** dividing cells are first cultured → colcemide arrests
cells in metaphase → hypotonic treatment (0.075 M KCl) → fixation → Giemsa staining
→ chromosomes photographed (harvest, M:A ratio 3:1).

`[figure]` An unsorted metaphase spread of Giemsa-stained chromosomes next to a
numbered grid (1-22, X, Y) captioned "Organize the chromosomes into a karyotype!" —
illustrating that raw metaphase chromosomes must be matched up and arranged into
this standard numbered layout.

**Identifying chromosomes — three key features:**
- **Size** — the easiest way to tell two different chromosomes apart.
- **Banding pattern** — the size and location of Giemsa bands make each
  chromosome pair unique.
- **Centromere position** — centromeres appear as a constriction.

Using these features, scientists match up the 23 pairs.

**Centromere position classes:** metacentric (centromere near the center);
submetacentric (centromere off-center, one arm longer than the other); acrocentric
(centromere very near one end — chromosomes 13, 14, 15, 21, 22); telocentric
(centromere at the very end).

**G-banding.** A dye gives chromosomes a striped appearance by staining regions of
DNA rich in adenine (A) and thymine (T) base pairs. The active-gene density is
higher in the G-light regions, which are less compact.

**Chromosome "address" notation.** The combination of numbers and letters gives a
gene's address on a chromosome — e.g. 14q21 = position 21 on the long arm (q) of
chromosome 14; 14q21 is closer to the centromere than 14q22.

`[figure]` "Fig. 8.1 G-Banded Metaphase Chromosomes" — a full G-banded karyotype
image (autosomes 1-22 plus X and Y), illustrating the banding-pattern identification
principle above.

Karyotypes distinguish **autosomes** from **sex chromosomes**.

**The karyotype notation.** A normal male chromosome pattern is described as
**46,XY**: 46 = total chromosome number; XY = sex chromosome constitution (XY =
male, XX = female). Any further description refers to abnormalities or variants
found.

**Indications for a karyotype:**
- Problems of early growth and development (failure to thrive, developmental
  delay, short stature).
- Stillbirth and neonatal death.
- Fertility problems (infertility history, multiple pregnancy loss).
- Family history (a known/suspected chromosomal abnormality in a first-degree
  relative).
- Pregnancy in a woman of advanced age (>35 years).

### 10.3 Genotype vs. phenotype {#ch10-3}
**Genotype** — the genetic makeup, symbolized with letters (e.g. Tt or TT, tt);
homozygous or heterozygous.

**Phenotype** — the physical appearance of the organism; the expression of the
trait (shape, size, color — short, tall, yellow, smooth, etc.).

Many phenotypes are influenced by the environment: phenotype results from the
interaction of genotype (total genetic makeup) with the environment. The most
common phenotype in a natural population is the **wildtype**.

`[figure]` A Venn diagram of two overlapping circles, "Genes" and "Environment" —
their overlap is labelled "You", with an arrow up to "Phenotype": phenotype is the
product of genes and environment together.

**The Himalayan rabbit example.** This rabbit has white fur with black fur on its
ears, nose, and tail. Himalayan rabbits carry temperature-sensitive tyrosinase
genes that control fur pigmentation. Extremities are usually coldest (less blood
flow), so the temperature-induced gene is activated there, producing darker fur.
Black pigment is deposited in fur when temperature falls; when hair is shaved and
an ice pack placed on the area, the new fur grows in black.

### 10.4 Genes, gene expression, and gene number {#ch10-4}
**Gene** — the hereditary unit transmitted from generation to generation. Genes →
protein → traits.

Each cell expresses (turns on) only a fraction of its genes; the rest are
repressed (turned off) — this process is **gene regulation**. Regulation involves
**histone acetylases** and **histone deacetylases** acting through chromatin
remodeling complexes.

"How many genes do we have?" is almost a meaningless question, because: each gene
can give rise to several proteins by alternative splicing; each protein can be
further modified in multiple ways (phosphorylation, methylation, acetylation,
glycosylation, etc.); and these modified proteins can further take part in
different protein complexes.

All cells in an organism share the same DNA, but not all genes in the genome are
expressed the same way in every cell — this is **epigenetics**: heritable changes
in gene expression that operate outside of changes in the DNA sequence itself.

**Mutation causes** (listed on a summary slide): smoking, radiation, viruses, sun
exposure, chemicals; also spontaneous mutation at a low background rate.

### 10.5 Glossary (Ch. 10) {#ch10-5}
`[figure]` "Table 3.1 — Summary of important genetic terms": **Gene** — a genetic
factor (region of DNA) that helps determine a characteristic. **Allele** — one of
two or more alternate forms of a gene. **Locus** — the specific place on a
chromosome occupied by an allele. **Genotype** — the set of alleles possessed by an
individual organism. **Heterozygote** — an individual possessing two different
alleles at a locus. **Homozygote** — an individual possessing two of the same
alleles at a locus. **Phenotype or trait** — the appearance or manifestation of a
character.

`[figure]` "Table 1.1 — Early concepts of heredity", listing historical theories
and whether each is correct or incorrect: **Pangenesis** (genetic information
travels from different parts of the body to reproductive organs) — Incorrect.
**Inheritance of acquired characteristics** (acquired traits become incorporated
into hereditary information) — Incorrect. **Preformationism** (a miniature organism
resides in sex cells, and all traits are inherited from one parent) — Incorrect.
**Blending inheritance** (genes blend and mix) — Incorrect. **Germ-plasm theory**
(all cells contain a complete set of genetic information) — Correct. **Cell theory**
(all life is composed of cells, and cells arise only from cells) — Correct.
**Mendelian inheritance** (traits are inherited in accord with defined principles)
— Correct.

---

## Ch. 11 — Mendelian Genetics {#ch11}

*Source: "2.Mendelian Genetics.pdf" (30p).*

### 11.1 Gregor Mendel {#ch11-1}
Born 1822 in Czechoslovakia (historical Austrian Empire territory, as the deck
states it). Became a monk at a monastery in 1843; had interests in statistics.
Between 1856 and 1863 he grew and tested over 28,000 pea plants.

### 11.2 The blending theory of inheritance {#ch11-2}
Mendel's experiments tested the **blending theory of heredity**, which viewed
offspring traits as a mixture of the parental traits. Under this theory, a black
cat crossed with a white one would produce gray kittens, and the black/white
traits would never reappear if the gray kittens were crossed to each other.

**Why peas?** Easy to grow; easily identifiable traits; can work with large
numbers of samples.

### 11.3 Fertilization and pure-breeding strains {#ch11-3}
`[figure]` **Self fertilization** diagram: fertilization (anther/pollen ♂ +
ovule/egg ♀) → seed development → mature seeds → germination → plant growth →
plant maturation/flower development → back to fertilization, forming the pea
plant's self-fertilizing life cycle.

`[figure]` **Cross fertilization** diagram: emasculate purple flowers by removing
their own anthers (♂) → transfer pollen from a white flower's anthers (♂) to the
purple flower's ovule (♀) → fertilization occurs → seeds develop → seeds planted,
plants grow, traits recorded across multiple resulting offspring plants.

Mendel took two years before beginning his experiments to establish **pure-breeding
(true-breeding)** strains — strains that consistently produce the same phenotype.
Each experiment began with crosses between two pure-breeding parental-generation
plants (**P generation**) that produced offspring called **F1** (first filial
generation). True-breeding = pure-breeding = pure line.

### 11.4 Monohybrid crosses and the Law of Segregation {#ch11-4}
Mendel crossed plants showing contrasting traits. A **monohybrid cross** reveals
the principle of segregation and the concept of dominance.

**Mendel's Law of Segregation:**
1. Plant traits are handed down through "hereditary factors" in the pollen and
   egg.
2. Because offspring obtain hereditary factors from both parents, each plant must
   contain two factors for every trait.
3. The factors in a pair segregate (separate) during the formation of sex cells,
   and each pollen or egg receives only one member of the pair.

**Dominant and recessive traits.** The trait shown by F1 offspring = the
**dominant phenotype** (e.g. purple flower). The trait not apparent in F1 = the
**recessive phenotype** (e.g. white flower). When F1 were crossed, 75% of the
resulting F2 had the dominant trait, but the recessive trait reappeared in the
other 25%.

**Modern terminology.** The "factors" controlling traits are **genes**; different
forms of a gene are **alleles**. Alleles that mask or hide other alleles (e.g. the
"round" allele) are **dominant**. A **recessive** allele (e.g. the wrinkle allele)
is masked whenever the dominant allele is present. The modern term for "purebred"
is **homozygous** (identical alleles); the offspring of crosses between parents
with contrasting traits are **hybrids** = **heterozygous**.

Dominant trait = a trait that shows in a heterozygote. Recessive trait = a trait
that is hidden in a heterozygote.

### 11.5 Replicate, reciprocal, and test crosses {#ch11-5}
Mendel made many **replicate crosses**, producing hundreds or thousands of
progeny by repeating each cross several times. He performed **reciprocal
crosses**, in which the same genotypes are crossed but the sexes of the parents
are reversed. He also performed **test crosses**.

`[figure]` Reciprocal-cross diagram: pure-breeding pollen (GG) × pure-breeding egg
(gg) → F1 Gg, alongside the reverse cross, pure-breeding pollen (gg) × pure-breeding
egg (GG) → F1 Gg — both yielding identical F1 results, illustrating "reciprocal
crosses between pure-breeding parents produce identical results."

**Test cross** — a cross between an individual of unknown genotype and a
homozygous recessive genotype.

`[figure]` Test-cross diagram: genotype-unknown individual (R–) × pure-breeding
recessive (rr) → artificial cross-fertilization. A 1:1 ratio of dominant to
recessive is expected if the round-seed parent is heterozygous (Rr); all progeny
are dominant if the round-seed parent is homozygous (RR).

### 11.6 Dihybrid crosses and the Law of Independent Assortment {#ch11-6}
A **dihybrid cross** reveals the principle of independent assortment. Example:
RrYy × RrYy gives a 9:3:3:1 ratio — 9 round/yellow : 3 round/green : 3
wrinkled/yellow : 1 wrinkled/green. The probability of round yellow seeds = 9/16.

**Mendel's Law of Independent Assortment (second law):** alleles at different
loci separate independently during the formation of gametes. The donation of one
allele from each pair is independent of any other pair — e.g. if a plant donates
the yellow-seed allele, that does not determine whether it also donates the
yellow-pod allele.

### 11.7 Meiosis, gamete number, and linkage {#ch11-7}
`[figure]` A cell-cycle/mitosis table (numbered "2.12"): across G1, S, G2,
prophase/prometaphase, metaphase, anaphase, and telophase/cytokinesis, the number
of chromosomes per cell (4→4→4→4→4→8→4) and the number of DNA molecules per cell
(4→4→8→8→8→8→4) are tracked. Chromosome number per cell = number of functional
centromeres; DNA-molecule number per cell = chromosome number when unreplicated,
doubling when sister chromatids are present. *(This mitosis-tracking table appears
in the Mendelian Genetics deck alongside meiosis content — transcribed here per
its actual placement in the source.)*

`[figure]` A meiosis diagram showing two alternative arrangements of homologs at
metaphase I (from one interphase cell carrying alleles A/a and B/b) — Arrangement I
and Arrangement II — each proceeding through metaphase II to four gamete types in
equal (¼) proportions: ¼ AB, ¼ ab (Arrangement I) and ¼ Ab, ¼ aB (Arrangement II),
illustrating independent assortment at the chromosome level.

**Genetic variation** arises from (I) crossing over and (II) random separation of
homologous chromosomes — possible combinations = 2 to the power n.

**Genotype vs. gamete.** A genotype contains two copies of the gene (e.g. AaBB); a
gamete contains only one copy of the gene (e.g. AB). Number of possible gametes =
2ⁿ, where n = number of heterozygous genes (e.g. CCDdee and AABbCcdd each have a
specific number of possible gamete types by this rule).

**Gene linkage.** Morgan found that many genes are linked together — it was
determined that **chromosomes**, not genes, assort independently during meiosis.
**Linked genes** are carried on the same chromosome, linked during transmission
from parent to offspring and inherited like single genes; recombination can break
linkage. Genes close together on the same chromosome belong to the same **linkage
group**.

---

## Ch. 12 — Non-Mendelian Genetics {#ch12}

*Source: "3.Non mendelian genetics.pdf" (32p).*

### 12.1 The molecular basis of dominance {#ch12-1}
The terms dominant and recessive have a phenotypic basis, but the dominance of
one allele over another is determined by the protein product of that allele. The
overall phenotype is the consequence of the activities of the protein products of
the gene's alleles.

Topics in this chapter: incomplete dominance, codominance, multiple alleles,
polygenic traits, penetrance and expressivity.

**Exceptions to Mendel's principles (gene interaction):** some alleles are
neither dominant nor recessive; there may be more than two alleles for a given
locus (multiple alleles); many traits are controlled by more than one gene
(polygenic traits); the expression of a trait may depend on the interaction of
more than one gene and/or genes with non-genic (environmental) factors.

### 12.2 Polygenic traits {#ch12-2}
Traits controlled by two or more genes — examples: human height, eye and skin
color. Diet and health are strong environmental factors in expressing genetic
potential for height.

Polygenic traits are continuously varying — e.g. skin color: the contribution of
many genes creates a gradient of colors, producing a bell-shaped curve.

`[figure]` "Polygenic inheritance" — a dihybrid-style Punnett square (parents
AaBb × AaBb) whose 16 offspring boxes are illustrated as eyes shaded across a
gradient (AABB → light blue; combinations with three capital alleles → deep
blue/green; two capital alleles → light or medium brown; one or zero capital
alleles → dark brown/black), showing how two genes' worth of allele dosage
produces a continuous phenotype gradient — the two-gene analogue of the
skin-color example above.

**Pleiotropic inheritance** — one gene, different (multiple) phenotypes.

`[figure]` A 2×2 diagram set distinguishing four gene-to-effect relationships:
(top-left) each gene has a distinct biological effect (one-to-one arrows);
(top-right) polygenic trait — many genes contribute to a single effect
(convergent arrows); (bottom-left) pleiotropy — a gene has multiple effects
(divergent arrows from one gene); (bottom-right) polygenic traits and pleiotropy
combined (a fully cross-connected many-to-many arrow network).

### 12.3 Incomplete dominance {#ch12-3}
A situation in which neither allele is dominant — when both alleles are present,
a "new" phenotype results. Heterozygous individuals display intermediate
phenotypes between either homozygous type. (By convention here, alleles are
represented by capital letters only.)

**Japanese four-o'clock flowers example.** Red flower genotype = RR; white
flower genotype = WW; pink flower genotype = RW. Crossing red × white: under
simple Mendelian dominance one would expect some white and some red, or all
offspring red or white — instead, all F1 are pink. When a trait exhibits
incomplete dominance, a cross between two heterozygotes produces a 1:2:1
genotypic **and** phenotypic ratio in the progeny.

`[figure]` "Explain…" — a worked incomplete-dominance cross diagram (fish
example, labelled "Codominance" in the image but illustrating the incomplete
dominance pattern in context): red RR × white rr → F1 pink Rr (gametes ½R, ½F) →
F2 generation showing red RR : pink Rr : pink rR : white rr (a standard 1:2:1
monohybrid Punnett square). A second panel on the same slide shows an LDL-receptor
genotype/phenotype example: HH (homozygous, able to make LDL receptors) = normal;
Hh (heterozygous) = mild disease; hh (homozygous, unable to make LDL receptors) =
severe disease — illustrating incomplete dominance at the level of receptor
number/phenotype severity.

### 12.4 Codominance {#ch12-4}
Codominance produces heterozygotes with a phenotype different from that of
either homozygote; there is detectable expression of both alleles in the
heterozygote.

**Roan cattle example.** Cattle can be red (RR — all red hairs), white (WW — all
white hairs), or roan (RW — red and white hairs together, each individual hair
being either fully red or fully white). Notice: no pink, no blend — each hair is
either red or white.

### 12.5 Multiple alleles — ABO blood types {#ch12-5}
Multiple allele inheritance = when two or more alleles contribute to the
phenotype. Human blood types: A, B, O, and AB. A and B are codominant to each
other; both A and B are dominant over O.

**ABO dominance relationships.** Four blood types result from different
combinations of three alleles: I^A, I^B, and i. I^A and I^B are completely
dominant over i but codominant with each other. Type A involves one antigen on
the blood cell surface; type B a different antigen. Type AB has both antigens;
type O has neither.

`[figure]` Two related "Blood Types (A, B, AB, O)" slides work through the
ABO system: the genotype-to-phenotype mapping (I^AI^A/I^Ai → A; I^BI^B/I^Bi → B;
I^AI^B → AB; ii → O) and the count of possible genotypes — 6 genotypes for 3
alleles at one locus, via the formula **n(n+1)/2** where n = number of alleles at
a locus (worked example: 5 alleles at a locus → 15 possible genotypes).

**Sample problem (posed, not answered in the source):** a man with type AB blood
marries a woman with type B blood whose father has type O blood — what are the
chances of a child with type A blood? Type AB?

### 12.6 Lethal alleles {#ch12-6}
Some single-gene mutations are so detrimental they cause death in the organism —
**lethal mutations**, inherited as recessive alleles (only homozygotes die).

**Yellow coat color in mice example.** Wild-type mice have dark pigmentation
coats; the yellow mutant has a lighter coat color. A yellow mouse is heterozygous
for the yellow allele (A^Y), and A^Y is dominant for color. Crossing a yellow
mouse × wild-type mouse (A^Y/A × A/A) gives a 1:1 yellow:wild-type ratio (50%
A^Y/A yellow, 50% A/A wild-type).

Crossing yellow × yellow (A^Y/A × A^Y/A) gives 50% A^Y/A yellow : 25% A/A
wild-type : 25% A^Y/A^Y **lethal** — an observed 2:1 (yellow:wild-type) ratio
among survivors rather than the naively expected 3:1, because the A^Y/A^Y class
dies. A^Y is dominant for color but **recessive lethal**.

`[figure]` A molecular diagram of the underlying mutation: the wild-type A
allele carries both a Raly promoter/Raly gene and an Agouti promoter/Agouti gene;
chromosomes carrying the wild-type A allele produce Raly protein (required for
mouse embryonic development) and a moderate amount of yellow pigment. A 120,000
base-pair deletion removes the Raly gene and its promoter, producing the A^Y
allele, which retains only the Raly promoter directly driving the Agouti gene:
chromosomes carrying A^Y produce no Raly protein (hence embryonic lethality when
homozygous) and a very high level of yellow pigment (hence the dominant color
phenotype).

**Pleiotropic mutation** — a mutation that affects multiple characters (the A^Y
allele affects both coat color and embryonic viability, i.e. it is pleiotropic).

### 12.7 Penetrance and expressivity {#ch12-7}
**Penetrance** — the percent of individuals with a given allele that show the
phenotype of that allele; <100% penetrance can result from epistasis,
suppressors, or environmental conditions.

**Expressivity** — the extent to which an allele is expressed at the phenotypic
level; affected by genetic background and environment.

These phenomena make pedigree analysis and genetic counseling more difficult.

**Epistasis** — the alleles of one gene modify or prevent the expression of
alleles of another gene.

An organism is **penetrant** for a trait when the phenotype is consistent with
the genotype; an organism that does not produce the phenotype generally
associated with its genotype is **nonpenetrant**. Traits for which nonpenetrant
individuals routinely occur display **incomplete penetrance**.

**Polydactyly example.** An autosomal dominant condition in which affected
individuals have more than 5 fingers and toes; the dominant allele is
nonpenetrant in about 25-30% of individuals carrying it.

`[figure]` Two clinical photographs of polydactyly: a partially-formed extra
digit between the thumb and index finger on both hands of one patient, and a
fully-formed extra (sixth) finger on the ulnar side of another patient's hand —
illustrating variable expressivity of the same condition.

`[figure]` "Penetrance and expressivity" — three rows of shaded/unshaded ovals,
each oval representing one individual's phenotypic expression: **variable
penetrance** (some individuals with the genotype show no phenotype at all —
alternating filled and empty ovals); **variable expressivity** (every individual
shows some phenotype, but the shade/intensity varies continuously); **variable
penetrance and expressivity combined** (some ovals empty, the rest varying in
shade).

### 12.8 Glossary (Ch. 12) {#ch12-8}
`[figure]` "Table 5.1 — Differences between dominance, incomplete dominance, and
codominance": **Dominance** — phenotype of the heterozygote is the same as the
phenotype of one of the homozygotes. **Incomplete dominance** — phenotype of the
heterozygote is intermediate (falls within the range) between the phenotypes of
the two homozygotes. **Codominance** — phenotype of the heterozygote includes the
phenotypes of both homozygotes.

---

## Source gaps and flagged passages

None. Every page reviewed — whether from its text layer or, for the 18 near-blank
pages, from a rendered image — carried transcribable content. No illegible text, no
genuinely content-free (purely decorative) figure, and no internal contradiction in
the source requiring a flag were found in this batch. The one apparent numeric
discrepancy (DNA-1 p.15's A-DNA "10" bp/turn) turned out to be the source's own
handwritten correction to 11, not an extraction error — recorded as such in §1.4
above rather than silently "fixed" or flagged as wrong.
