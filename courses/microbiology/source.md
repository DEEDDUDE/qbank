# Microbiology — Source

Built by Job B from the lecture and lab spines documented in
[provenance.md](provenance.md) and the chapter-list plan approved before this file was
written. Two tracks, kept separate so a citation can never mix a lecture chapter with a
lab chapter:

- **Lecture chapters** (this file, Ch. 1–16): spine is `slides/2023-slides/`, complete
  and full-text-layer. `slides/2024-slides/` is applied only where content genuinely
  differs — measured by direct text comparison, not by year — which turned out to be a
  single topic, Viral Replication (Ch. 12), where 2024 adds detail without dropping
  content 2023 covers. Chapter names and order follow `slides/Outline/Course outline
  2023_2024.pdf`; where the outline is silent (Ch. 16) or ambiguous (Ch. 7/8), that is
  stated in the chapter itself.
- **Lab chapters**: [source.lab.md](source.lab.md), spine is
  `slides/MicroLab-Slides-inner/`, based on Dina M. Bitar's official `Manual.pdf`. Built
  separately, indexed by [source.lab.index.md](source.lab.index.md).

Excluded from both, per the reasoning already on record: `bacteria-table/` and
`2-2-Pictures - Bacterial Cell.pdf` (scanned textbook material, not lecturer content, and
this repo is published), all student notes, all third-party textbooks.

Nothing here is invented. Where the material states something that looks incomplete,
inconsistent, or hard to verify, it is preserved as written and flagged rather than
corrected — see the notes inline.

---

## Ch. 1 — Introduction to the Microbial World {#ch01}

> **Source:** 2023-slides, `1_ Medical Microbiology slides first chapters.pdf`, pp. 1–6.
> Outline week 1.

### Classification of pathogenic microorganisms {#ch01-1}

Human infectious diseases belong to five major groups of organisms:

| Kingdom | Pathogenic microorganisms | Type of cells |
|---|---|---|
| Animal | Helminths (worms) | Eukaryotic |
| Protists | Protozoa | Eukaryotic |
| Fungi | Fungi (yeasts and molds) | Eukaryotic |
| Prokaryote | Bacteria | Prokaryotic |
| — | Viruses | Noncellular |

The five groups: bacteria, fungi, protozoa, helminths, viruses.

### Comparison of medically important organisms {#ch01-2}

| Characteristic | Viruses | Bacteria | Fungi | Protozoa and Helminths |
|---|---|---|---|---|
| Cells | No | Yes | Yes | Yes |
| Approximate diameter (μm) | 0.02–0.2 | 1–5 | 3–10 (yeasts) | 15–25 (trophozoites) |
| Nucleic acid | Either DNA or RNA | Both DNA and RNA | Both DNA and RNA | Both DNA and RNA |
| Type of nucleus | None | Prokaryotic | Eukaryotic | Eukaryotic |
| Ribosomes | Absent | 70S | 80S | 80S |
| Mitochondria | Absent | Absent | Present | Present |
| Nature of outer surface | Protein capsid and lipoprotein envelope | Rigid wall containing peptidoglycan | Rigid wall containing chitin | Flexible membrane |
| Motility | None | Some | None | Most |
| Method of replication | Not binary fission | Binary fission | Budding or mitosis | Mitosis |

### Three main differential criteria {#ch01-3}

1. **Structure** — Cells have a nucleus or nucleoid containing DNA, surrounded by
   cytoplasm within which proteins are synthesized and energy is generated. Viruses have
   genetic material (DNA or RNA) but no cytoplasm, so they depend on host cells for the
   machinery of protein synthesis and energy generation.
2. **Method of replication** — Cells replicate by binary fission or mitosis, in which one
   parent cell divides into two progeny cells while retaining its cellular structure.
   Prokaryotic cells (e.g., bacteria) replicate by binary fission; eukaryotic cells by
   mitosis. Viruses disassemble, produce many copies of their nucleic acid and protein,
   then reassemble into multiple progeny viruses.
3. **Nature of the nucleic acid** — Cells contain both DNA and RNA; viruses contain
   either DNA or RNA, never both.

### Eukaryotes and prokaryotes {#ch01-4}

The eukaryotic cell has a true nucleus with multiple chromosomes surrounded by a nuclear
membrane, and uses a mitotic apparatus to ensure equal allocation of chromosomes to
progeny cells. The nucleoid of a prokaryotic cell is a single circular molecule of
loosely organized DNA, lacking a nuclear membrane and mitotic apparatus.

| Characteristic | Prokaryotic bacterial cells | Eukaryotic human cells |
|---|---|---|
| DNA within a nuclear membrane | No | Yes |
| Mitotic division | No | Yes |
| DNA associated with histones | No | Yes |
| Chromosome number | One | More than one |
| Membrane-bound organelles (e.g., mitochondria, lysosomes) | No | Yes |
| Size of ribosome | 70S | 80S |
| Cell wall containing peptidoglycan | Yes | No |

- Eukaryotic cells contain organelles (mitochondria, lysosomes) and larger (80S)
  ribosomes; prokaryotic cells contain no organelles and smaller (70S) ribosomes.
- Most prokaryotes have a rigid external cell wall containing peptidoglycan. Eukaryotes
  do not contain peptidoglycan — they are bound by a flexible cell membrane, or, in the
  case of fungi, have a rigid cell wall with chitin.
- The eukaryotic cell membrane contains sterols; no prokaryote has sterols in its
  membrane except the wall-less *Mycoplasma*.

### Terminology and classification {#ch01-5}

- Bacteria, fungi, protozoa, and helminths are named by the binomial Linnean system
  (genus and species). Viruses have single names.
- Examples: *Escherichia coli* (genus *Escherichia*, species *coli*); *Candida albicans*
  (genus *Candida*, species *albicans*); viruses — poliovirus, measles virus, rabies
  virus; two-part virus names — herpes simplex virus.

---

## Ch. 2 — Bacterial Cell — Structure and Function {#ch02}

> **Source:** 2023-slides, `1_ Medical Microbiology slides first chapters.pdf`, pp. 7–49.
> Outline week 2.

### Structure and shape {#ch02-1}

Bacteria are classified by shape: 1) cocci, 2) bacilli, 3) spirochetes. Some bacteria are
variable in shape and are called pleomorphic (many-shaped). Microscopic appearance is one
of the most important criteria used in bacterial identification.

- Cocci in clusters (e.g., *Staphylococcus*); chains (e.g., *Streptococcus*); pairs with
  pointed ends (e.g., *Streptococcus pneumoniae*); pairs with kidney-bean shape (e.g.,
  *Neisseria*).
- Rods (bacilli) with square ends (e.g., *Bacillus*); rounded ends (e.g., *Salmonella*);
  club-shaped (e.g., *Corynebacterium*); fusiform (e.g., *Fusobacterium*); comma-shaped
  (e.g., *Vibrio*).
- Spirochetes: relaxed coil (e.g., *Borrelia*); tightly coiled (e.g., *Treponema*).

**Arrangement:** certain cocci occur in pairs (diplococci), some in chains
(streptococci), others in grapelike clusters (staphylococci) — determined by the
orientation and degree of attachment at the time of cell division. Arrangement of rods
and spirochetes is medically less important.

**Bacteria size:** ranges about 0.2 to 5 μm. The smallest bacteria (*Mycoplasma*) are
about the same size as the largest viruses (poxviruses). The longest bacterial rods are
the size of some yeasts and human red blood cells (7 μm).

### Cell wall {#ch02-2}

Outermost component of the bacterial cell. *Mycoplasma* species are bounded by a cell
membrane and have no cell wall. Some bacteria have surface features such as a capsule,
flagella, and pili. The cell wall is composed of peptidoglycan, which provides structural
support and maintains the characteristic cell shape.

**Comparison of Gram-positive and Gram-negative cell walls:**

| Component | Gram-positive cells | Gram-negative cells |
|---|---|---|
| Peptidoglycan | Thicker; multilayer | Thinner; single layer |
| Teichoic acids | Yes | No |
| Lipopolysaccharide (endotoxin) | No | Yes |

- Peptidoglycan is much thicker in Gram-positive than Gram-negative bacteria.
- Only Gram-negative bacteria have an outer membrane containing endotoxin (LPS).
- Gram-negative bacteria have a periplasmic space where β-lactamases are found (relevant
  to the use of inhibitors).
- Several important Gram-positive bacteria (staphylococci, streptococci) have teichoic
  acids.
- Gram-negative bacteria have a complex outer layer of lipopolysaccharide, lipoprotein,
  and phospholipid. Between the outer-membrane layer and the cytoplasmic membrane is the
  periplasmic space — in some species the site of β-lactamases, which degrade penicillins
  and other β-lactam drugs.

**Other important properties of the Gram-negative cell wall:**
- Contains endotoxin (a lipopolysaccharide).
- Its polysaccharides and proteins are antigens useful in laboratory identification.
- Porin proteins facilitate passage of small hydrophilic molecules into the cell —
  sugars, amino acids, vitamins, metals, and many antimicrobial drugs such as
  penicillins.

**Cell wall of *Mycobacterium tuberculosis*:** layers of mycolic acid and arabinoglycan
are present in *Mycobacterium* but not in most other bacterial genera.

**Three important components of the cell wall:** 1) peptidoglycan, 2) lipopolysaccharide,
3) teichoic acid.

**Peptidoglycan** is found only in bacterial cell walls. It provides rigid support,
maintains characteristic cell shape, and lets the cell withstand low-osmotic-pressure
media such as water. Derived from peptides and sugars (glycan); synonyms are murein and
mucopeptide. Structure: a glycan chain (NAM and NAG), a tetrapeptide chain, and a
cross-link (peptide interbridge) — NAG = N-acetylglucosamine, NAM = N-acetylmuramic acid.
In the cell wall, peptidoglycan forms a multilayered, three-dimensional structure.

**Teichoic acid:** fibers in the outer layer of the Gram-positive cell wall, composed of
polymers of glycerol phosphate or ribitol phosphate. Some glycerol teichoic acid polymers
penetrate the peptidoglycan layer and are covalently linked to membrane lipid (called
lipoteichoic acid); others anchor to the muramic acid of the peptidoglycan. Medical
importance: ability to induce inflammation and septic shock in certain Gram-positive
infections, activating the same pathways as endotoxin (LPS) does in Gram-negative
bacteria. Teichoic acids also mediate attachment of staphylococci to mucosal cells.

### Gram stain {#ch02-3}

Developed in 1884 by the Danish physician Christian Gram. Separates most bacteria into
two groups: Gram-positive (stain blue) and Gram-negative (stain red). Four steps:

1. Crystal violet dye stains all cells blue/purple.
2. Iodine solution forms a crystal violet–iodine complex.
3. Decolorization by acetone or ethanol extracts the blue dye complex from the
   lipid-rich, thin-walled Gram-negative bacteria to a greater degree than from the
   lipid-poor, thick-walled Gram-positive bacteria.
4. Red dye safranin stains the decolorized Gram-negative cells red/pink; Gram-positive
   bacteria remain blue.

Useful in two ways: 1) identification of many bacteria; 2) influences antibiotic choice —
Gram-positive bacteria are generally more susceptible to penicillin G than Gram-negative
bacteria.

**Medically important bacteria that cannot be seen in the Gram stain:**

| Name | Reason | Alternative microscopic approach |
|---|---|---|
| Mycobacteria, including *M. tuberculosis* | Too much lipid in cell wall so dye cannot penetrate | Acid-fast stain |
| *Treponema pallidum* | Too thin to see | Dark-field microscopy or fluorescent antibody |
| *Mycoplasma pneumoniae* | No cell wall; very small | None |
| *Legionella pneumophila* | Poor uptake of red counterstain | Prolong time of counterstain |
| Chlamydiae, including *C. trachomatis* | Intracellular; very small | Inclusion bodies in cytoplasm |
| Rickettsiae | Intracellular; very small | Giemsa or other tissue stains |

**Cell walls of acid-fast bacteria:** mycobacteria (e.g., *M. tuberculosis*) have an
unusual cell wall and cannot be Gram-stained. They are acid-fast because they resist
decolorization with acid–alcohol after staining with carbolfuchsin — related to a high
concentration of lipids (mycolic acids) in the cell wall.

**Lysozyme:** an enzyme in human tears, mucus, and saliva that cleaves the peptidoglycan
backbone by breaking its glycosyl bonds — part of innate immunity (natural host
resistance to microbial infection). Lysozyme-treated bacteria may swell and rupture from
water entering the cell (high internal osmotic pressure); in isotonic solution they can
survive as spherical forms called protoplasts, surrounded only by a cytoplasmic membrane.

### Bacterial structures — essential components {#ch02-4}

| Structure | Chemical composition | Function |
|---|---|---|
| Cell wall — peptidoglycan | Glycan (sugar) backbone with cross-linked peptide side chains | Rigid support, protects against osmotic pressure, site of action of penicillins and cephalosporins, degraded by lysozyme |
| Outer membrane (Gram-negative) — Lipid A | Toxic component of endotoxin | — |
| Outer membrane (Gram-negative) — Polysaccharide | — | Major surface antigen, frequently used in laboratory diagnosis |
| Surface fibers (Gram-positive) — Teichoic acid | — | Major surface antigen, rarely used in laboratory diagnosis |
| Plasma membrane | Lipoprotein bilayer without sterols | Site of oxidative and transport enzymes |
| Ribosome | RNA and protein in 50S and 30S subunits | Protein synthesis; site of action of aminoglycosides, erythromycin, tetracyclines, chloramphenicol |
| Nucleoid | DNA | Genetic material |
| Mesosome | Invagination of plasma membrane | Participates in cell division and secretion |
| Periplasm | Space between plasma membrane and outer membrane | Contains many hydrolytic enzymes, including β-lactamases |

**Cytoplasmic membrane:** a phospholipid bilayer, microscopically similar to eukaryotic
membranes. Eukaryotic membranes contain sterols; prokaryotes generally do not — the only
prokaryotes with membrane sterols are *Mycoplasma*. Four functions: 1) active transport
of molecules into the cell; 2) energy generation by oxidative phosphorylation;
3) synthesis of cell wall precursors; 4) secretion of enzymes and toxins.

**Ribosomes:** site of protein synthesis. Bacterial ribosomes are 70S (50S + 30S
subunits); eukaryotic ribosomes are 80S (60S + 40S subunits). Differences in ribosomal
RNAs and proteins are the basis for selective action of several antibiotics that inhibit
bacterial but not human protein synthesis.

**Granules:** different types that serve as nutrient storage areas; stainable with
certain dyes.

**Nucleoid:** the area of cytoplasm where DNA is located. Prokaryotic DNA is a single,
circular molecule of about 2000 genes. No nuclear membrane, no nucleolus, no mitotic
spindle, no histones — little resemblance to the eukaryotic nucleus. Bacterial DNA has no
introns; eukaryotic DNA does.

### Bacterial structures — nonessential components {#ch02-5}

| Structure | Chemical composition | Function |
|---|---|---|
| Capsule | Polysaccharide | Protects against phagocytosis |
| Pilus or fimbria | Glycoprotein | Two types: (1) mediates attachment to cell surfaces; (2) sex pilus mediates attachment of two bacteria during conjugation |
| Flagellum | Protein | Motility |
| Spore | Keratin-like coat, dipicolinic acid | Provides resistance to dehydration, heat, and chemicals |
| Plasmid | DNA | Contains genes for antibiotic resistance and toxins |
| Granule | Glycogen, lipids, polyphosphates | Site of nutrients in cytoplasm |
| Glycocalyx | Polysaccharide | Mediates adherence to surfaces |

### Plasmids {#ch02-6}

Extrachromosomal, double-stranded, circular DNA molecules capable of replicating
independently of the bacterial chromosome. Occur in both Gram-positive and Gram-negative
bacteria; several different plasmid types can exist in one cell.

- **Transmissible plasmids** can be transferred cell to cell by conjugation. Large (MW
  40–100 million), containing about a dozen genes for sex-pilus synthesis and transfer
  enzymes. Usually 1–3 copies per cell.
- **Nontransmissible plasmids** are small (MW 3–20 million), lack transfer genes,
  frequently present in 10–60 copies per cell.

**Plasmid genes serve:**
1. Antibiotic resistance — mediated by enzymes such as the β-lactamase of *S. aureus*,
   *E. coli*, and *K. pneumoniae*.
2. Exotoxins — e.g., the enterotoxins of *E. coli*, anthrax toxin of *B. anthracis*,
   tetanus toxin of *C. tetani*.
3. Pili (fimbriae), mediating bacterial adherence to epithelial cells.
4. Resistance to ultraviolet light, mediated by DNA repair enzymes (photolyase, DNA
   glycolase, and others).

**Other plasmid-encoded products — bacteriocins:** toxic proteins produced by certain
bacteria, lethal for other bacteria. Two mechanisms: 1) degradation of bacterial cell
membranes by producing pores; 2) degradation of bacterial DNA by DNase. Examples: colicins
(*E. coli*), pyocins (*Pseudomonas aeruginosa*). May be useful in treating infections
caused by antibiotic-resistant bacteria. A variety of degradative enzymes (plasmid-coded)
produced by *Pseudomonas* can clean up environmental hazards such as oil spills and toxic
chemical waste sites.

### Transposons {#ch02-7}

Pieces of DNA that move readily from one site to another, within or between the DNAs of
bacteria, plasmids, and bacteriophages — nicknamed "jumping genes." Can code for
drug-resistance enzymes, toxins, or various metabolic enzymes, and can cause mutations or
alter expression of nearby genes.

**Four identifiable domains** of a drug-resistance-carrying transposon: at each end, a
short DNA sequence of inverted repeats (IR), involved in integration into recipient DNA;
the gene for transposase, the enzyme mediating excision and integration; the gene for the
repressor regulating synthesis of both transposase and the fourth domain's protein, which
in many cases is an enzyme mediating antibiotic resistance.

### Structures outside the cell wall {#ch02-8}

**1) Capsule** — a gelatinous layer covering the entire bacterium, composed of
polysaccharide, except the anthrax bacillus, whose capsule is polymerized D-glutamic
acid. The sugar components vary by species and often determine serologic type (serotype)
within a species — there are 84 different serotypes of *Streptococcus pneumoniae*,
distinguished by antigenic differences in the capsular polysaccharide sugars.

Importance of the capsule:
1. Determinant of virulence for many bacteria — limits phagocyte engulfment; negative
   charges on the capsular polysaccharide repel the negatively charged neutrophil cell
   membrane, preventing ingestion.
2. Specific identification using antiserum against the capsular polysaccharide (Quellung
   reaction).
3. Capsular polysaccharides are used as antigens in certain vaccines, capable of
   eliciting protective antibodies.
4. May play a role in bacterial adherence to human tissues, an important initial step in
   infection.

Capsules are antiphagocytic — they limit neutrophils' ability to engulf bacteria.
Antibodies against the capsule neutralize the antiphagocytic effect, allowing engulfment.
Opsonization is the process by which antibodies enhance phagocytosis of bacteria.

**2) Flagella** — long, whiplike appendages that move bacteria toward nutrients and other
attractants (chemotaxis). Composed of many subunits of a single protein, flagellin,
arranged in intertwined chains. Energy for movement (proton motive force) is provided by
ATP, derived from ion passage across the membrane. Flagellated bacteria have a
characteristic number and location of flagella; many rods have flagella, but most cocci
do not and are nonmotile.

Medical importance of flagella: motile species (e.g., *E. coli*, *Proteus*) commonly
cause urinary tract infections — flagella may propel bacteria up the urethra into the
bladder. Some species (e.g., *Salmonella*) are identified clinically by specific
antibodies against flagellar proteins.

**3) Pili (fimbriae)** — hair-like filaments extending from the cell surface, shorter and
straighter than flagella, composed of subunits of pilin, arranged in helical strands.
Found mainly on Gram-negative organisms. Mediate attachment of bacteria to specific
receptors on human cell surfaces, a necessary step in initiating infection for some
organisms — mutants of *Neisseria gonorrhoeae* lacking pili are nonpathogenic. A
specialized pilus, the sex pilus, is used in conjugation.

**4) Glycocalyx (slime layer)** — a polysaccharide coating secreted by many bacteria,
covering surfaces like a film and allowing firm adherence to structures (skin, heart
valves, prosthetic joints, catheters). An important component of biofilms. Medical
importance: glycocalyx-producing *P. aeruginosa* strains cause respiratory infections in
cystic fibrosis patients; glycocalyx-producing *Staphylococcus epidermidis* and viridans
streptococci cause endocarditis; glycocalyx also mediates adherence of *Streptococcus
mutans* to tooth surfaces, important in plaque formation, the precursor of dental caries.

### Bacterial spores {#ch02-9}

Highly resistant structures formed in response to hard/adverse conditions, mainly by
Gram-positive rods: genus *Bacillus* (including the agent of anthrax) and genus
*Clostridium* (including the agents of tetanus). Sporulation occurs when nutrients are
depleted. The spore forms inside the cell with a thick, keratin-like coat giving
resistance to heat, dehydration, radiation, and chemicals. Resistance is mediated by
dipicolinic acid (pyridine-2,6-dicarboxylic acid), a calcium ion chelator found only in
spores. The spore has no metabolic activity and can remain dormant for many years.

The spore contains the entire DNA genome of the bacterium, surrounded by a thick,
resistant coat. Because of this resistance to heat, sterilization cannot be achieved by
boiling — steam heating under pressure (autoclaving) at 121°C for at least 15 minutes is
required to ensure sterility of medical products.

**Important features of spores and their medical implications:**

| Feature | Medical implication |
|---|---|
| Highly resistant to heating — not killed by boiling (100°C) | Medical supplies must be heated to 121°C for at least 15 minutes to be sterilized |
| Highly resistant to many chemicals, including most disinfectants, due to the thick, keratin-like coat | Sporicidal solutions are used to kill spores |
| Can survive for many years, especially in soil | Wounds contaminated with soil can be infected — e.g., tetanus (*C. tetani*), gas gangrene (*C. perfringens*) |
| No measurable metabolic activity | Antibiotics are ineffective — the coat is impermeable to antibiotics |

---

## Ch. 4 — Classification of Bacteria and Diagnostic Methods {#ch04}

> **Source:** 2023-slides, `1_ Medical Microbiology slides first chapters.pdf`, pp. 50-95.
> Outline week 4.

### Classification of medically important bacteria {#ch04-1}

Based on morphologic and biochemical characteristics; only medically important bacteria
are discussed. Gram-negative rods are divided into three categories: respiratory
organisms, zoonotic organisms, enteric and related organisms.

The initial classification criterion is the nature of the cell wall: rigid, flexible, or
absent.
- Bacteria with rigid, thick walls subdivide into: 1) free-living bacteria, which can
  grow on laboratory medium without human or other animal cells; 2) non-free-living
  bacteria, which are obligate intracellular organisms.
- Free-living organisms are further subdivided by shape (cocci and rods), Gram stain,
  oxygen requirements, and spore-forming ability.
- Bacteria with flexible, thin walls (spirochetes) and those without cell walls
  (mycoplasmas) form separate units.
- Many bacteria can be readily classified into genus and species this way (DNA-based
  classification also applies).

**Classification table:**

| Characteristics | Genus | Representative diseases |
|---|---|---|
| I. Rigid, thick-walled cells - A. Free-living (extracellular) | | |
| 1. Gram-positive - a. Cocci | *Streptococcus* | Pneumonia, pharyngitis, cellulitis |
| | *Staphylococcus* | Abscess of skin and other organs |
| 1. Gram-positive - b. Spore-forming rods (1) Aerobic | *Bacillus* | Anthrax |
| 1. Gram-positive - b. Spore-forming rods (2) Anaerobic | *Clostridium* | Tetanus, gas gangrene, botulism |
| 1. Gram-positive - c. Non-spore-forming rods (1) Nonfilamentous | *Corynebacterium* | Diphtheria |
| | *Listeria* | Meningitis |
| 1. Gram-positive - c. Non-spore-forming rods (2) Filamentous | *Actinomyces* | Actinomycosis |
| | *Nocardia* | Nocardiosis |
| 2. Gram-negative - a. Cocci | *Neisseria* | Gonorrhea, meningitis |
| 2. Gram-negative - b. Rods (1) Facultative (a) Straight (i) Respiratory | *Haemophilus* | Meningitis |
| | *Bordetella* | Whooping cough |
| | *Legionella* | Pneumonia |
| 2. Gram-negative - b. Rods (1) Facultative (a) Straight (ii) Zoonotic | *Brucella* | Brucellosis |
| | *Francisella* | Tularemia |
| | *Pasteurella* | Cellulitis |
| | *Yersinia* | Plague |
| 2. Gram-negative - b. Rods (1) Facultative (a) Straight (iii) Enteric and related | *Escherichia* | Urinary tract infection, diarrhea |
| | *Enterobacter* | Urinary tract infection |
| | *Serratia* | Pneumonia |
| | *Klebsiella* | Pneumonia, urinary tract infection |
| | *Salmonella* | Enterocolitis, typhoid fever |
| | *Shigella* | Enterocolitis |
| | *Proteus* | Urinary tract infection |
| 2. Gram-negative - b. Rods (1) Facultative (b) Curved | *Campylobacter* | Enterocolitis |
| | *Helicobacter* | Gastritis, peptic ulcer |
| | *Vibrio* | Cholera |
| 2. Gram-negative - b. Rods (2) Aerobic | *Pseudomonas* | Pneumonia, urinary tract infection |
| 2. Gram-negative - b. Rods (3) Anaerobic | *Bacteroides* | Peritonitis |
| 3. Acid-fast | *Mycobacterium* | Tuberculosis, leprosy |
| B. Non-free-living (obligate intracellular parasites) | *Rickettsia* | Rocky Mountain spotted fever, typhus, Q fever |
| | *Chlamydia* | Urethritis, trachoma, psittacosis |
| II. Flexible, thin-walled cells (spirochetes) | *Treponema* | Syphilis |
| | *Borrelia* | Lyme disease |
| | *Leptospira* | Leptospirosis |
| III. Wall-less cells | *Mycoplasma* | Pneumonia |

### Laboratory diagnosis {#ch04-2}

Two main approaches: 1) bacteriologic (staining and culturing the organism); 2)
immunologic/serologic (detecting antibodies against the organism in patient serum).

Points to consider in the bacteriologic approach: 1) choosing the appropriate specimen;
2) obtaining the specimen properly to avoid contamination from normal flora;
3) transporting the specimen promptly to the laboratory; 4) providing essential
information to guide laboratory personnel.

**General approach to diagnosing a bacterial infection:**
1. Obtain a specimen from the infected site.
2. Stain the specimen (Gram stain or acid-fast stain); identify shape, type, mixed or pure.
3. Culture the specimen on appropriate media.
4. Identify the organism with appropriate tests (sugar fermentation, DNA probes,
   antibody-based tests); note special features such as hemolysis and pigment formation.
5. Perform antibiotic susceptibility tests.

**If the culture is negative:**
1. Detect antibody in patient serum - IgM indicates current infection; a fourfold or
   greater rise in antibody titer between the acute sample and a sample 10-14 days later
   also indicates current infection. A single IgG titer is difficult to interpret since
   it is unclear whether it represents a current or previous infection.
2. Detect antigen in the patient specimen, using known antibody.
3. Detect nucleic acids in the patient specimen.

**Culturing bacteria on agar plates:** blood agar is the first choice - supports growth
of many bacteria and hemolysis type can be observed. Viruses and obligate intracellular
bacteria (*Chlamydia*, *Rickettsia*) will not grow on blood agar. Blood agar must be
heated to support growth of *Neisseria* and *Haemophilus* (cooked blood agar / chocolate
agar).

- **Alpha-hemolytic:** oxidizes iron in hemoglobin, turning it dark green.
- **Beta-hemolytic:** completely ruptures red blood cells, causing a halo in culture.
- **Gamma-hemolytic/non-hemolytic:** species rarely cause illness.

**Commonly used bacteriologic agars:**

| Agar | Bacteria isolated | Function/properties |
|---|---|---|
| Blood | Various bacteria | Detect hemolysis |
| Charcoal-yeast extract | *Legionella pneumophila* | Increased iron and cysteine concentration allows growth |
| Chocolate | *N. meningitidis*, *N. gonorrhoeae* | Heating the blood inactivates growth inhibitors |
| Chocolate + X and V factors | *Haemophilus influenzae* | X and V factors required for growth |
| Egg yolk | *Clostridium perfringens* | Lecithinase produced by the organism degrades egg yolk |
| Eosin-Methylene Blue | Various enteric Gram-negative rods | Selects against Gram-positive bacteria; differentiates lactose fermenters from nonfermenters |
| MacConkey | Various enteric Gram-negative rods | Same as above |
| Triple sugar iron (TSI) | Various enteric Gram-negative rods | Distinguishes lactose fermenters from nonfermenters and H2S producers from nonproducers |

**Organisms by specimen type:**

| Specimen | Organisms | Notes |
|---|---|---|
| Blood | *S. aureus*, *S. pneumoniae*, *E. coli*, *K. pneumoniae*, *P. aeruginosa* | - |
| Throat culture | *Streptococcus pyogenes* (group A beta-hemolytic), *N. gonorrhoeae*, *Candida* | - |
| Sputum | *Mycoplasma*, *S. pneumoniae*, *K. pneumoniae*, *P. aeruginosa*, *S. aureus*, *M. tuberculosis* | General cause: hospital-acquired infection (HAI)/nosocomial |
| Spinal fluid | *N. meningitidis*, *S. pneumoniae*, *H. influenzae*, *M. tuberculosis*, *Cryptococcus neoformans* (fungi) | Meningitis / subacute meningitis |
| Stool | *Shigella*, *Salmonella*, *Campylobacter*, *E. coli* O157 | Enterocolitis / diarrhea |
| Urine | *E. coli* (most common), *Enterobacter*, *Proteus*, *Enterococcus faecalis* | Pyelonephritis / cystitis |
| Genital tract | *N. gonorrhoeae*, *Chlamydia trachomatis*, *Treponema pallidum* | Syphilis |
| Wound & abscess | Many organisms - *Bacteroides fragilis*, *S. aureus*, *Clostridium perfringens*, *Pasteurella multocida* | Soil flora / surgical-wound / dog or cat bites |

### Bacteriologic methods {#ch04-3}

**Blood cultures:** performed when sepsis, endocarditis, osteomyelitis, meningitis, or
pneumonia is suspected. Most frequently isolated: two Gram-positive cocci (*S. aureus*,
*S. pneumoniae*) and three Gram-negative rods (*E. coli*, *K. pneumoniae*,
*P. aeruginosa*). Collect at least three 10-mL blood samples in a 24-hour period. Clean
the venipuncture site with 2% iodine to prevent contamination by *S. epidermidis*. Blood
is added to 100 mL of rich growth medium. If two bottles are used, one is kept anaerobic,
the other not. Cultures are held 14 days when infective endocarditis, fungemia, or slow
growers (e.g., *Brucella*) are suspected.

**Throat cultures:** primarily to detect group A beta-hemolytic streptococci (*S.
pyogenes*), a major cause of pharyngitis. Also used when diphtheria, gonococcal
pharyngitis, or thrush (*Candida*) is suspected. Swab the posterior pharynx and both
tonsils. Inoculate onto blood agar, streak for single colonies. If beta-hemolytic
streptococcus colonies appear after 24 hours, use a bacitracin disk - growth inhibition
around the disk indicates group A streptococcus; no inhibition indicates non-group A.

**Sputum cultures:** needed when pneumonia or tuberculosis is suspected. Most frequent
cause of community-acquired pneumonia is *S. pneumoniae*; *S. aureus* and Gram-negative
rods (*K. pneumoniae*, *P. aeruginosa*) commonly cause hospital-acquired pneumonia. Use
blood agar, serologic or biochemical tests. *Mycoplasma* cultures are infrequent -
diagnosis is usually by rising antibody titer. If TB is suspected, do an acid-fast stain.
Anaerobic cultures are important.

**Spinal fluid cultures:** performed when meningitis is suspected (lumbar puncture). Most
important causes of acute bacterial meningitis: three encapsulated organisms - *N.
meningitidis*, *S. pneumoniae*, *H. influenzae*. Treated as STAT. The Gram-stained smear
of centrifuged sediment guides immediate empirical treatment. If organisms resembling
these three are seen, use serological testing (Quellung test).

**CSF specimen collection:** routinely collected via lumbar puncture between the 3rd,
4th, or 5th lumbar vertebra under sterile conditions.

In subacute meningitis, *M. tuberculosis* and *Cryptococcus neoformans* are the most
common organisms. Acid-fast stains of spinal fluid should be performed (6-week culture).
Immunologic tests detecting capsular antigen in spinal fluid can identify *N.
meningitidis*, *S. pneumoniae*, *H. influenzae*, group B streptococci, *E. coli*, and
*C. neoformans*.

**Stool cultures:** performed for enterocolitis. Most common species: *Shigella*,
*Salmonella*, *Campylobacter*; *E. coli* O157 strains also important. Direct microscopy:
1) methylene blue staining showing many leukocytes indicates an invasive rather than
toxigenic organism; 2) Gram stain may reveal large numbers of organisms such as
staphylococci, clostridia, or campylobacters. Gram stain of stool is not usually done
because of the large normal-flora bacterial population of the colon.

**Urine cultures:** done when pyelonephritis or cystitis is suspected. Most frequent
cause of UTI is *E. coli*; other common agents are *Enterobacter*, *Proteus*, and
*Enterococcus faecalis*. Bladder urine in a healthy person is sterile but acquires normal
flora organisms passing through the distal urethra. A midstream specimen is used;
suprapubic aspiration or catheterization are alternatives.

**Genital tract cultures:** one of the most important genital pathogens is *N.
gonorrhoeae* - diagnosed by microscopic examination of a Gram-stained smear and culture.
Specimens obtained by swabbing the urethral canal (men), cervix (women), or anal canal
(both). Nongonococcal urethritis and cervicitis are also extremely common - most frequent
cause is *Chlamydia trachomatis*, which cannot grow on artificial medium and must be
grown in living cells; use serological methods or DNA-based assays. *Treponema
pallidum* (syphilis) cannot be cultured - diagnosis is by microscopy and serology; motile
spirochetes with typical morphology seen by dark-field microscopy of fluid from a
painless genital lesion is sufficient for diagnosis.

**Wound & abscess cultures:** a great variety of organisms involved. Lung and abdominal
abscesses frequently caused by anaerobes (*Bacteroides fragilis*) and Gram-positive cocci
(*S. aureus*, *S. pyogenes*). Traumatic open-wound infections mainly from soil flora
(*Clostridium perfringens*). Surgical-wound infections from *S. aureus*. Dog or cat bite
infections from *Pasteurella multocida*. Because many such infections involve multiple
organisms, including mixtures of anaerobes and nonanaerobes, culture on several media
under different atmospheric conditions is important. The Gram stain provides valuable
information.

### Immunologic methods {#ch04-4}

Two basic approaches: 1) using known antibody to identify the microorganism; 2) using
known antigens to detect antibodies in patient serum.

**1) Capsular swelling (Quellung) reaction:** based on microscopic observation of capsule
swelling in the presence of homologous antiserum. Antisera available against: all
serotypes of *S. pneumoniae* (Omniserum: pooled polyvalent sera), *H. influenzae* type b,
*N. meningitidis* groups A and C (six main pathogenic subtypes: A, B, C, W135, X, Y).

**2) Slide agglutination test:** antisera identify *Salmonella* and *Shigella* by causing
agglutination of the unknown organism - antisera against cell wall O antigens of
*Salmonella* and *Shigella*, and against flagellar H antigens and capsular Vi antigen of
*Salmonella*.

**3) Latex agglutination test:** latex beads coated with specific antibody agglutinate in
the presence of homologous bacteria or antigen. Used to detect capsular antigen of *H.
influenzae*, *N. meningitidis*, and species of streptococci.

**4) Counter-immunoelectrophoresis test:** bacterial antigen and known specific antibody
move toward each other in an electrical field; a precipitate forms in the agar matrix if
homologous. Used to detect capsular antigens of *H. influenzae*, *N. meningitidis*, *S.
pneumoniae*, and group B streptococci (important in newborns) in spinal fluid.

**5) Enzyme-Linked Immunosorbent Assay (ELISA):** a specific antibody linked to an
easily-assayed enzyme detects the presence of homologous antigen.

**6) Fluorescent antibody tests:** bacteria identified by exposure to known antibody
labeled with fluorescent dye, detected visually by fluorescent microscope.

**Identification of serum antibodies with known antigens - slide or tube agglutination
test:** serial two-fold dilutions of patient serum are mixed with standard bacterial
antigen. The highest dilution still agglutinating the bacteria is the antibody titer. At
least a fourfold rise in antibody titer is needed to demonstrate infection (cut-off
value). Used in diagnosing typhoid fever, brucellosis, tularemia, plague, leptospirosis,
and rickettsial diseases.

**Serologic tests for syphilis:** based on detecting antibody in patient serum, since *T.
pallidum* does not grow on laboratory media. Two kinds:
1. **Nontreponemal antigen tests** (lipids extracted from beef heart) - agglutination
   occurs in the presence of antibody to *T. pallidum*. Also known as VDRL (Venereal
   Disease Research Laboratory test) and RPR (rapid plasma reagin) test. Used as
   screening tests; disadvantage - not specific.
2. **Treponemal tests** use *T. pallidum* as the antigen:
   - **FTA-ABS:** fluorescent-labeled antibodies against adsorbed human IgG (patient
     serum adsorbed against a non-*T. pallidum* antigen) detect bound human IgG to
     nonviable *T. pallidum* on a slide.
   - **MHA-TP (microhemagglutination-*Treponema pallidum*):** patient serum reacted with
     sheep erythrocytes coated with *T. pallidum* antigens - hemagglutination occurs if
     antibodies are present.

**Cold agglutinin test:** a nonspecific test. Example: auto-antibodies in patients
infected with *Mycoplasma pneumoniae* agglutinate human red blood cells at 4C but not at
37C. Can interfere with other diseases, causing false-positive results.

A cold agglutinins blood test detects and measures cold agglutinins - antibodies produced
in response to infection that clump red blood cells at low temperature. Cold agglutinin
disease can arise spontaneously (excessive cell proliferation) or from pathology:
lymphoma, leukemia, *Mycoplasma pneumoniae* infection, mononucleosis, HIV.

### Nucleic acid-based methods {#ch04-5}

Highly specific and sensitive; easy to perform. Different methods:

1. **DNA amplification methods** (mainly the 16S ribosomal gene):
   - PCR (Polymerase Chain Reaction).
   - Isothermal amplification (LAMP) - good as a point-of-care (POC) test.
2. **DNA sequence analysis:**
   - Sanger sequencing.
   - High-throughput sequencing (NGS).
3. **Nucleic acid probes, DNA hybridization, and reverse line hybridization** - useful
   for bacteria difficult to culture (*Chlamydia* and *Mycobacterium* species); used to
   detect *C. trachomatis* and *N. gonorrhoeae* in urine samples, and to identify *M.
   tuberculosis* in sputum samples.

---

## Ch. 3 — Bacterial Physiology and Growth Requirements {#ch03}

> **Source:** 2023-slides, `3_ Bacterial Growth 2021.pdf`, all 38pp. Outline week 3.
> **Unclear source text:** pages 4, 7, 9-10, 13, 17-18, 24, 30, 35 carry only diagrams
> (growth curve, temperature/pH/oxygen-effect charts, metabolism overview) with no
> extractable text layer, so no caption text could be transcribed from them.

### Growth cycle and generation time {#ch03-1}

Bacteria reproduce by binary fission, forming two identical cells; bacteria are said to
undergo exponential growth.

**Generation time (doubling time):** the interval between successive binary fissions of a
cell or population of cells. Varies from 20 minutes (*Escherichia coli*) up to 18 hours
(*Mycobacterium tuberculosis*). A short doubling time results in rapid production of very
large numbers of bacteria. Doubling time varies not only by species but also with the
amount of nutrients, temperature, pH, and other environmental factors.

Example generation times: *E. coli* 20 min; *Staphylococcus aureus* 30 min;
*Mycobacterium tuberculosis* 15 hours; *Treponema pallidum* 33 hours.

**Source inconsistency:** the deck states *M. tuberculosis*'s generation time as "up to
18 hours" in one place and "15 hours" in the worked example list a page later. Both
preserved as written for verification.

### The bacterial growth curve {#ch03-2}

Four phases:
1. **Lag phase** — vigorous metabolic activity occurs but cells do not divide.
2. **Log/exponential (logarithmic) phase** — rapid cell division occurs; high metabolic
   rate, the potential drug-acting phase.
3. **Stationary phase** — occurs when nutrient depletion or toxic products cause growth
   to slow.
4. **Death phase** — marked by a decline in the number of viable bacteria.

Cells grown in a special apparatus called a chemostat, into which fresh nutrients are
added and from which waste products are continuously removed, can remain in the log
phase and do not enter the stationary phase.

### Nutritional requirements {#ch03-3}

Most bacteria grow on prepared media including purified chemicals (sugars, amino acids,
salts); blood is added for nutritional purposes. Some bacteria (*Chlamydia*,
*Rickettsia*, *Ehrlichia*, *Anaplasma*) can only grow within living cells — they are
obligate intracellular organisms, obligated to grow within cells because they lack the
ability to produce sufficient ATP and must use ATP produced by the host cell.

### Aerobic and anaerobic growth {#ch03-4}

For most organisms, an adequate oxygen supply enhances metabolism and growth. Oxygen acts
as the hydrogen acceptor in the final steps of energy production, catalyzed by
flavoproteins and cytochromes. Oxygen use generates two toxic molecules: 1) hydrogen
peroxide (H2O2); 2) free radical superoxide (O2-). Bacteria require two enzymes to
detoxify these:
1. **Superoxide dismutase**, catalyzing: 2O2- + 2H+ -> H2O2 + O2
2. **Catalase**, catalyzing: 2H2O2 -> 2H2O + O2

The response to oxygen is an important criterion for classifying bacteria and determining
the proper atmosphere for growth:
1. **Obligate aerobes** — require oxygen to grow (*M. tuberculosis*).
2. **Facultative anaerobes** — (*E. coli*) utilize oxygen if present, generating energy by
   respiration, but can use the fermentation pathway to synthesize ATP without oxygen.
3. **Obligate anaerobes** — (*Clostridium tetani*) cannot grow in the presence of oxygen
   because they lack superoxide dismutase, catalase, or both. Tolerance varies — some
   survive but cannot grow, others are killed rapidly.

### Metabolism {#ch03-5}

Metabolism (Greek *metabole*, meaning change) is the totality of an organism's chemical
processes to maintain life — the sum of catabolism and anabolism, opposite chemical
processes: catabolism releases energy (exergonic), anabolism takes up energy
(endergonic; the deck spells this "energonic").

**Fermentation of sugars:** the breakdown of a monosaccharide sugar (glucose or maltose)
to pyruvic acid and then lactic acid — the process by which facultative bacteria generate
ATP in the absence of oxygen. If oxygen is present, pyruvate produced by fermentation
enters the Krebs cycle and is metabolized to two final products, CO2 and H2O. The Krebs
cycle generates much more ATP than the glycolytic cycle, so facultative bacteria grow
faster in the presence of oxygen. Facultative and anaerobic bacteria ferment; aerobes do
not — aerobes such as *Pseudomonas aeruginosa* produce metabolites that enter the Krebs
cycle by processes other than fermentation, such as amino acid deamination.

**Sugar fermentation as an identification criterion:**
- *Neisseria gonorrhoeae* and *Neisseria meningitidis* are distinguished by fermentation
  of glucose or maltose — *N. gonorrhoeae* utilizes only glucose, while *N. meningitidis*
  produces acid from both glucose and maltose.
- *E. coli* is differentiated from *Salmonella* and *Shigella* by lactose fermentation.
- Fermentation tests: production of pyruvate and lactate acidifies the medium, detected by
  the pH indicator phenol red — a fermented sugar turns the medium yellow; an
  unfermented sugar leaves phenol red unchanged (red).
- The Triple Sugar Iron (TSI) test applies sugar fermentation as a differential
  biochemical test.

**Iron metabolism:** ferric ion is required for bacterial growth as an essential
component of cytochromes and other enzymes. Iron is available in the human body in very
low amounts, sequestered in iron-binding proteins such as transferrin. Bacteria produce
iron-binding compounds called siderophores — e.g., enterobactin, produced by *E. coli* —
which are secreted, capture iron by chelating it (competing with the host's
iron-binding proteins), attach to specific receptors on the bacterial surface, and are
actively transported into the cell, where the iron becomes available for use.
Siderophore-dependent iron uptake relies on high-affinity surface receptor proteins that
bind iron-loaded siderophores.

**Effect of pressure on bacterial growth:** halophilic organisms require high salt
concentrations; osmophilic organisms require high osmotic pressure.

### Energy sources and biological systems {#ch03-6}

**Autotrophs (self-feeding)** synthesize their food from simple carbon sources:
- **Photoautotrophs** (e.g., cyanobacteria) synthesize food using light energy and carbon
  dioxide gas (photosynthesis).
- **Chemoautotrophs** use carbon dioxide plus chemical reactions to obtain energy from
  inorganic compounds (chemosynthesis).

**Heterotrophs (other-feeding):**
1. **Photoheterotrophs** — light plus an organic compound (fatty acid or alcohol) as
   carbon source.
2. **Chemoheterotrophs** — organic compounds for both energy and carbon (e.g., glucose).
   A parasite feeds on living organic matter.

There are four basic groups of organisms based on their carbon and energy sources
(autotroph/heterotroph x photo-/chemo-), per the deck's summary slide.

---

## Ch. 5 — Bacterial Genetics {#ch05}

> **Source:** 2023-slides, `2_ Bacterial Genetics.pdf`, all 38pp. Outline week 5.

### Prokaryote vs. eukaryote genetics {#ch05-1}

The genetic material of a typical bacterium, *Escherichia coli*, is a single circular DNA
molecule of approximately 5 x 10^6 base pairs, coding for about 2000 proteins. A human
contains about 3 x 10^9 base pairs and encodes about 100,000 proteins (the deck also
gives a parenthetical figure of "about 30,000").

**Source note:** the deck states human protein-coding genes as both "100,000" and, in a
parenthetical immediately after, "(about 30,000!!!)". Both numbers preserved as written.

Bacterial cells are haploid, with a single chromosome (human cells are diploid). In
haploid cells, any gene that has mutated — and is therefore not expressed — results in a
cell that has lost that trait.

| | Prokaryotes | Eukaryotes |
|---|---|---|
| Ploidy | Haploid | Often diploid |
| Chromosome | Single circular chromosome | Linear chromosomes (usually more than one) |
| Extra elements | Small circular DNA molecules called plasmids, conferring properties such as drug resistance | — |
| Replication | Only circular DNA molecules replicate | — |

Other genetic elements: plasmids, transposons, viruses, and others. Reproduction is
asexual; bacteria need other mechanisms for diversity, and have poor ability to control
their environment.

### Plasmids {#ch05-2}

Small, circular, double-stranded pieces of DNA that replicate independently of the
bacterial chromosome.
- **Conjugative plasmids:** the F factor (fertility factor) of *E. coli* is the most
  studied — it carries genes encoding the sex pilus for physical transfer of genetic
  material.
- **R factors:** confer multiple drug resistance (MDR plasmid).
- **Hfr:** a conjugative plasmid integrated into the chromosome, characterized by high
  frequency of recombination; it passes this trait to any receptive bacterium with which
  the host cell conjugates.

### Bacterial mutation {#ch05-3}

Alteration of the information in a bacterial chromosome through a permanent change in the
DNA. Two types: 1) spontaneous, 2) induced.

**Spontaneous mutation:** heritable changes to the DNA base sequence occurring from
natural phenomena — radiation penetrating the atmosphere, errors during DNA replication.
May occur once per 10^6 to 10^10 replications. The mutant may survive, multiply, and
emerge as dominant (example given: *Neisseria gonorrhoeae*).

**Induced mutation:** results from planned experiments subjecting bacteria to chemical or
physical agents. Causes:
- Ultraviolet light (UV) — induces adjacent thymine dimers.
- Nitrous acid — a chemical mutagen that converts DNA's adenine to hypoxanthine
  (affecting replication) / deaminates adenine and cytosine.
- Base analog — 5-bromouracil (the deck notes acyclovir, an antiviral, in this context).

**How mutagenic chemicals act:**
- Nitrous acid and alkylating agents alter an existing base so it preferentially forms a
  hydrogen bond with the wrong base.
- 5-bromouracil is a base analogue resembling normal bases — it can be inserted in place
  of thymine; having less hydrogen-bonding fidelity than thymine, it binds guanine more
  frequently, causing a transition from an A-T base pair to a G-C base pair. The antiviral
  drug iododeoxyuridine acts as a base analogue of thymidine.
- Benzpyrene (found in tobacco smoke) binds existing DNA bases and causes frameshift
  mutations.

**Mutation by X-rays and ultraviolet light:** X-rays have high energy and damage DNA
three ways: (a) breaking covalent bonds holding the ribose-phosphate chain together;
(b) producing free radicals that attack the bases; (c) altering electrons in the bases,
changing their hydrogen bonding. Ultraviolet radiation causes cross-linking of adjacent
pyrimidine bases to form dimers (thymine dimer; repaired by photolyase). Certain viruses,
such as the bacterial virus Mu (mutator bacteriophage), cause a high frequency of
mutations (frameshift mutations).

**Three types of mutations:**
1. **Base substitution** — one base inserted in place of another; produced by DNA
   polymerase errors or by a mutagen changing hydrogen bonding. Two subtypes:
   a) missense mutation (causes a different amino acid to be inserted); b) nonsense
   mutation (no protein is produced).
2. **Frameshift mutation** — one or more base pairs are added or deleted, resulting in an
   inactive protein.
3. **Transposons or insertion sequences** integrated into the DNA.

**Base-pair substitution:** transcription of the gene produces one incorrect base in the
mRNA codon sequence.
- Silent mutation — no change.
- Missense mutation — leads to insertion of the wrong amino acid.
- Nonsense mutation — generates a stop codon.

**Frameshift and transposons:** base-pair deletion or insertion — loss or addition of a
base in the gene (frameshift mutation). Transposons/insertion sequences integrate into
the DNA, causing profound changes in the genes into which they insert and in adjacent
genes.

**Point-mutation illustration (from the deck):**
```
THE FAT CAT ATE THE RAT   (normal)
THE FAT CAN ATE THE RAT   (substitution)
THE F  TC ATA TET HER AT  (deletion)
THE FAT ACA TAT ETH ERA T (insertion)
```

**Conditional lethal mutations:** used in vaccine development, e.g., using influenza
virus as a vector. Temperature-sensitive organisms can replicate at a relatively low,
permissive temperature (e.g., 32C) but not at a higher, restrictive temperature (e.g.,
37C) — from a mutation altering the conformation of essential proteins. Such a virus
cannot grow at 37C and so cannot infect the lungs, but can grow at 32C in the nose, where
it replicates and induces immunity.

### Transfer of DNA within bacterial cells {#ch05-4}

Two mechanisms: transposons, and programmed rearrangement.

**Transposons** transfer DNA from one site on the bacterial chromosome to another site or
to a plasmid. Transfer of a transposon to a plasmid, followed by transfer of that plasmid
to another bacterium by conjugation, contributes significantly to the spread of
antibiotic resistance.

**Programmed rearrangements:** transfer of DNA within a bacterium responsible for many
antigenic changes seen in *Neisseria gonorrhoeae* and *Borrelia recurrentis*. A programmed
rearrangement is the movement of a gene from a silent storage site (no expression) to an
active expression locus, where transcription and translation occur — purpose: to evade
the immune response. Mechanism: a copy of gene 2 is made and inserted into the expression
locus; when gene 2's DNA is inserted, gene 1's DNA is excised and degraded.

### Transfer of DNA between bacterial cells {#ch05-5}

Three mechanisms:
1. **Transformation** — bacteria take up DNA from their environment and incorporate it
   into their genome (the Griffith experiment).
2. **Conjugation** — direct transfer of DNA between bacteria, usually via plasmids.
3. **Transduction** — movement of DNA between bacteria by viruses.

This may affect: 1) antibiotic resistance genes are spread from one bacterium to another
primarily by conjugation; 2) several important exotoxins are encoded by bacteriophage
genes and transferred by transduction.

**1) Conjugation:** transfer of genetic material from donor to recipient cell, controlled
by an F (fertility) plasmid (F factor), which carries the genes required for conjugation.
One of the most important proteins is pilin, which forms the sex pilus (conjugation
tube). Mating begins when the pilus of the donor (male, F+) bacterium attaches to a
receptor on the surface of the recipient (female, F-) bacterium. After enzymatic
cleavage of the F factor DNA, one strand transfers across the conjugal bridge (sex pilus)
into the recipient; synthesis of the complementary strand completes the process, forming
a double-stranded F factor plasmid in both donor and recipient. In this instance, only
the F factor — not the bacterial chromosome — is transferred. The new plasmid in the
recipient is composed of one parental strand and one newly synthesized strand; at the end
of synthesis, both donor and recipient contain a complete plasmid copy.

**High-frequency recombination (Hfr):** an F plasmid integrated into the bacterial
chromosome mediates transfer of the donor's bacterial chromosome into the recipient.

**Resistance plasmids (R plasmids):** carry one or more genes for enzymes that degrade
antibiotics and modify membrane transport systems — e.g., R plasmids encode the
β-lactamases of *S. aureus*, *E. coli*, and *K. pneumoniae*. R plasmids transfer by
conjugation not only within the same species but also to other species.

**2) Transduction:** transfer of cell DNA by means of a bacteriophage. The virus can take
a piece of bacterial DNA, incorporate it into the virus particle, and transfer it to a
new recipient cell at the next infection. Within the recipient, phage DNA can integrate
into cell DNA, and the cell acquires a new trait — lysogenic conversion. This can turn a
nonpathogenic organism into a pathogenic one. Diphtheria toxin, botulinum toxin, cholera
toxin, and erythrogenic toxin (*Streptococcus pyogenes*) are encoded by bacteriophages
and transferred by transduction.

Transduction sequence: A) a bacteriophage infects a bacterium and phage DNA enters the
cell; B) phage DNA replicates, bacterial DNA fragments; C) progeny phages assemble and
are released (a few contain bacterial DNA); D) another bacterium is infected by a
phage-containing bacterial DNA; E) the transduced bacterial DNA integrates into host DNA,
and the host acquires a new trait.

**3) Transformation:** transfer of DNA from one cell to another. Occurs by: 1) in
nature, DNA from dying bacteria may be taken up by recipient cells — e.g., *Neisseria*
and *Haemophilus* synthesize surface receptors that bind and uptake environmental DNA;
2) in the laboratory — DNA extracted from one bacterial type is introduced into
genetically different bacteria; part of the DNA can also be transferred via plasmid.
Transfection refers to DNA injected into the cell or nucleus of a eukaryotic cell.

**Transformation experiment (1944):** DNA extracted from encapsulated smooth pneumococci
could transform nonencapsulated rough pneumococci into encapsulated smooth organisms —
demonstrating that the transforming principle was DNA.

**Comparison of conjugation, transduction, and transformation:**

| Transfer procedure | Process | Type of cells involved | Nature of DNA transferred |
|---|---|---|---|
| Conjugation | DNA transferred from one bacterium to another | Prokaryotic | Chromosomal or plasmid |
| Transduction | DNA transferred by a virus from one cell to another | Prokaryotic | Any gene, in generalized transduction |
| Transformation | Purified DNA taken up by a cell | Prokaryotic or eukaryotic | Any DNA |

### Recombination {#ch05-6}

Once DNA is transferred from donor to recipient, it can integrate into the host cell
chromosome by recombination. Two types:
- **Homologous recombination** — two DNA pieces with extensive homologous regions pair up
  and exchange pieces by breakage and reunion.
- **Nonhomologous recombination** — little, if any, homology is necessary.

Different genetic loci govern these two types, and different enzymes are involved
(endonucleases and ligases).

---

## Ch. 6 — Normal Flora of the Body {#ch06}

> **Source:** 2023-slides, `4_ Normal Flora.pdf`, all 32pp. Outline week 6.

### Definitions {#ch06-1}

Normal flora describes the bacteria and fungi that are permanent residents of certain
body sites, especially the skin, oropharynx, colon, and vagina. Viruses and parasites are
never considered members of the normal flora. Normal flora are commensal organisms —
they derive benefit from the host without damaging it. "Human microbiome" refers to the
normal flora of the human body — specifically, the genetic material (total bacterial
content) of all microbes living on and inside the body.

**Resident flora:** species that live on or in nearly everyone, almost all the time, in
specific sites — e.g., *Staph. epidermidis* (skin), *E. coli* (colon and small
intestine). In their natural sites, resident flora do not harm healthy tissue, and some
are beneficial. They may become pathogenic if introduced into abnormal sites — *E. coli*
is considered an opportunist in this sense.

**Transient flora:** species found periodically on or in the body, less well adapted than
resident flora (example: *Streptococcus pneumoniae*). Transients may become pathogenic
when host resistance is lowered — e.g., in an elderly person with influenza, *S.
pneumoniae* may invade the lower respiratory tract and cause serious or fatal pneumonia.

**Carrier** implies an individual harbors a potential pathogen and can be a source of
infection for others — not related to the presence of normal flora. Distinct from
**colonization**, which refers to acquisition of a new organism on mucosal surfaces
(versus normal flora, which are permanent residents).

### Roles of normal flora in health and disease {#ch06-2}

Three significant ways:
1. Their presence matters in immunocompromised individuals.
2. They constitute a protective host defense mechanism — nonpathogenic resident bacteria
   occupy attachment sites on skin and mucosa, interfering with colonization by
   pathogenic bacteria (colonization resistance).
3. Nutritional function — intestinal bacteria produce several B vitamins and vitamin K;
   poorly nourished people treated with oral antibiotics can develop vitamin
   deficiencies.

**The human microbiome:** the "microbiota" located in/on different body sites, many
identified by DNA analysis. The largest and most complex microbial population resides in
the colon. The intestinal microbiota plays a role in certain autoimmune diseases such as
inflammatory bowel disease, influences maturation and function of the immune response,
and contributes to colonization resistance.

**Advantages of normal flora:**
- Host nutrition.
- Prevents colonization — by competing for receptors/binding sites, competing for
  nutrients, producing antibiotics or bacteriocins, and producing toxic products.
- Stimulation of natural antibodies that cross-react with pathogenic organisms.

**Disadvantages of normal flora:**
- Become pathogenic when host resistance is lowered.
- May act as pathogens in tissue outside their normal habitat. Examples:
  - Intestinal flora may cause UTIs.
  - *Bacteroides fragilis* causes peritonitis associated with perforation of the
    intestinal wall following trauma, appendicitis, or diverticulitis.
  - *Streptococcus viridans* (*S. mutans*) can enter the bloodstream following tooth
    extraction or tonsillectomy, causing infective endocarditis.

### Effect of antibiotics on normal flora {#ch06-3}

Resident flora may be diminished by antibiotics used to treat bacterial infections — an
antibiotic does not distinguish between the pathogen and resident bacteria. Without the
usual competition, yeasts or pathogenic bacteria may overgrow and create new infections.

In the intestine specifically: clindamycin can suppress the predominant normal flora,
allowing a rare toxin-producing *Clostridium difficile* to overgrow and cause severe
colitis. Neomycin given prior to GI surgery to sterilize the gut decreases bacterial
levels, which return to normal after several days.

### Localization of normal flora by site {#ch06-4}

Sites: skin, eyes (conjunctiva), nose and throat (upper respiratory tract), mouth, large
intestine, urinary and reproductive systems.

**Skin:** predominant organism is *Staphylococcus epidermidis* — nonpathogenic on skin
but can cause disease when it reaches sites such as artificial heart valves and
prosthetic joints. Some organisms are found in hair follicles, acting as a reservoir to
replenish superficial flora after hand washing. Anaerobic organisms such as
*Propionibacterium* and *Peptococcus* sit in deeper follicles in the dermis —
*Propionibacterium acnes* is a common skin anaerobe implicated in acne pathogenesis. The
yeast *Candida albicans* is also part of normal skin flora.

**Respiratory tract:** colonizes nose, throat, and mouth (mainly streptococcal and
staphylococcal), but not the lower bronchi and alveoli. The throat contains a mixture of
viridans streptococci, *Neisseria* species, and *S. epidermidis*; these nonpathogens
inhibit growth of the pathogens *Streptococcus pyogenes*, *Neisseria meningitidis*, and
*S. aureus*, respectively.

Viridans group in the mouth (green colonies): *Streptococcus mutans*, a member of the
viridans group, is found in large numbers in dental plaque, the precursor of caries.
Viridans streptococci also cause subacute bacterial (infective) endocarditis — they can
enter the bloodstream during dental surgery and attach to damaged heart valves.

**Intestinal tract:** the small intestine usually contains small numbers of streptococci,
lactobacilli, and yeasts (particularly *C. albicans*); larger numbers occur in the
terminal ileum. The colon is the major bacterial location in the body — roughly 20% of
feces is bacteria, approximately 10^11 organisms/g. More than 90% of fecal flora are
anaerobes, the most important being *Bacteroides fragilis*. The most abundant facultative
bacteria are the coliforms (*E. coli*).

Intestinal normal flora plays a significant role in extra-intestinal disease: *E. coli*
is the leading cause of urinary tract infections; *B. fragilis* is an important cause of
peritonitis associated with perforation of the intestinal wall following trauma,
appendicitis, or diverticulitis. Other important pathogens that can cause UTI and
endocarditis: *Fusobacterium* and *Peptostreptococcus* (anaerobic); *Enterococcus
faecalis* (facultative) causes endocarditis; *Pseudomonas aeruginosa* causes hospital
infections (present in 10% of normal stools, and also in soil and water).

**Genitourinary tract:** *Lactobacillus* species are normal vaginal flora (in adults)
that produce acidic pH. Lactobacilli can prevent growth of potential pathogens — since
antibiotic treatment can lead to overgrowth by *C. albicans*. During passage through the
urethra, urine becomes contaminated with *S. epidermidis*, coliforms, diphtheroids, and
nonhemolytic streptococci. *Mycobacterium smegmatis* is mainly found in secretions around
the urethral area. *Staphylococcus saprophyticus* is found on skin surrounding the
genitourinary tract and can cause UTI in women.

**Diseases caused by normal flora of the intestinal tract:**
- *E. coli* -> UTI.
- *Bacteroides fragilis* -> peritonitis (perforation of intestinal wall following
  trauma, appendicitis, diverticulitis).
- *Enterococcus faecalis* -> UTI and endocarditis.
- *Pseudomonas aeruginosa* -> various infections in patients with low host defenses.

**Diseases caused by normal flora of the genitourinary tract:**
- Suppression of lactobacilli by antibiotics -> overgrowth of the yeast-like fungus
  *Candida albicans* -> "Candida vaginitis."
- Recurrent UTIs due to *E. coli* and *Enterobacter* (anus close to vagina).
- 15-20% of women of child-bearing age carry group B streptococci in the vagina ->
  sepsis and meningitis in the newborn.

### Probiotics {#ch06-5}

The use of normal GI-tract flora to treat diseases; stabilizes the composition of normal
flora. Dose range: 10^9-10^10 organisms.

**Classification criteria for a probiotic strain:** beneficial physiological effect;
strain of human origin; safe for human use; stable in acid and bile; adheres to
intestinal mucosa. Most common strains: *Lactobacillus acidophilus*, *Bifidobacterium
bifidum*, *Streptococcus thermophilus*.

**Use of probiotics in treatment of diseases:**
1. Treatment and prevention of diarrhea — rotavirus diarrhea in children; travelers'
   diarrhea and enteritis; post-antibiotic diarrhea from long-term antibiotic use.
2. Alleviation of lactose intolerance symptoms (lactic acid bacteria).
3. Food allergies, e.g., milk.
4. Treatment of GI inflammation associated with disruption of the mucosal
   barrier/permeability — Crohn's disease, food allergies, atopic eczema.
5. Reduction of recurrent respiratory infections — e.g., pneumonia in cystic fibrosis.

---

## Ch. 7 — Pathogenic Mechanisms {#ch07}

> **Source:** 2023-slides, `5_Topic 7, Bacterial Pathogenesis.pdf`, pp. 1-16 and 36-102.
> Outline week 7. This deck interleaves pathogenic-mechanism content with a transmission
> block; pp. 17-35 (transmission, portals of entry, vectors, zoonoses) are drawn out into
> Ch. 8. The split is ours, not the source's, and the page ranges are recorded here so it
> can be checked.

### Symbiosis {#ch07-1}

Symbiosis ("live together") describes two organisms living in association with one
another. Three types of relationship, based on the quality of the relationship for each
member:

**Mutualism** — both members benefit. Classic example: lactic acid bacteria living on the
vaginal epithelium — the woman provides a habitat with constant temperature and a
nutrient supply (glycogen) in exchange for lactic acid production; the bacteria protect
the vagina from colonization and disease by yeast and other potentially harmful microbes.

**Commensalism** — no apparent benefit or harm to either member. Example:
*Staphylococcus epidermidis*, a consistent human skin inhabitant, produces lactic acid
that protects the skin from colonization by harmful microbes. Other bacterial
metabolites have been suggested as an important cause of body odors and possibly
associated with certain skin cancers.

**Parasitism** — a parasite grows, feeds, and shelters on or in a different organism
while contributing nothing to the host's survival, and is capable of damaging the host. A
parasite may become pathogenic if the damage results in disease. Some parasitic bacteria
live as normal human flora while waiting for an opportunity to cause disease.

### Principles of pathogenesis {#ch07-2}

A **pathogen** is a microorganism that can cause disease. **Opportunistic** pathogens
rarely cause disease but cause serious infection in immunocompromised patients (normal
flora, and some parasites).

**Pathogenicity:** the ability to produce disease in a host organism.
**Virulence:** the degree of pathogenicity of the microbe — a quantitative measure,
measured by the number of organisms required to cause disease.

**Types of pathogens:**
- **Potential (opportunistic) pathogens** — normal bacterial flora such as
  *Staphylococcus aureus*, *Streptococcus pneumoniae*, *Haemophilus influenzae*; live in
  a commensal or parasitic relationship without producing disease, until an opportunity
  arises from some compromise or weakness in the host's anatomical barriers, tissue
  resistance, or immunity.
- **Obligate pathogens** — do not associate with their host except in the case of
  disease; exist in a form where they cannot be eliminated by the host.

The **50% lethal dose (LD50)** is the number of organisms needed to kill half the hosts;
the **50% infectious dose (ID50)** is the number needed to cause infection in half the
hosts. Organisms with a lower LD50 (or ID50) are more virulent, since fewer organisms are
needed to cause death or disease. The infectious dose required varies greatly among
pathogenic bacteria. Virulence factors affecting infection rate include: presence of pili
to adhere to mucous membranes, production of exotoxins or endotoxins, possession of a
capsule, and ability to survive nonspecific host defenses such as stomach acid.

Some bacterial pathogens are obligate intracellular parasites (e.g., *Chlamydia* and
*Rickettsia*) because they can grow only within host cells. Many bacteria are facultative
parasites, able to grow within cells, outside cells, or on bacteriologic media.

### Why people get infectious diseases {#ch07-3}

People get infectious diseases when microorganisms overpower host defenses, and the
organism or its products are present in sufficient amounts to induce symptoms (fever and
inflammation, interpreted as infectious disease). Two important factors favoring
infection: 1) number of organisms to which the host is exposed; 2) pathogen virulence.
The production of specific virulence factors also determines which disease the bacteria
cause — e.g., *E. coli* producing one exotoxin type causes watery (nonbloody) diarrhea,
while a different strain producing another exotoxin type causes bloody diarrhea.

### Determinants of virulence {#ch07-4}

Determinants of a pathogen's virulence are its genetic, biochemical, and structural
features — they enable the pathogen to produce disease in a host.

- **Single determinant of virulence:** toxin (*Clostridium tetani*, *Corynebacterium
  diphtheriae*).
- **Large/multiple determinants of virulence:** (*Staphylococcus aureus*, *Streptococcus
  pyogenes*, *Pseudomonas*) — produce different diseases affecting different tissues in
  their host.

A healthy immune response provides better protection against infections. **Asymptomatic
infections:** the host acquires an organism but no infectious disease occurs because host
defenses were successful — antibody against the organism can still be detected in the
patient's serum.

### Two major mechanisms of disease causation {#ch07-5}

1. **Toxin production** — two types:
   - **Exotoxins:** polypeptides released by the cell.
   - **Endotoxins:** lipopolysaccharides (LPS) that form an integral part of the Gram-
     negative cell wall.
2. **Invasion and inflammation**

Endotoxins occur only in Gram-negative rods and cocci, are not actively released from the
cell, and cause fever and shock. Both exotoxins and endotoxins can cause symptoms without
requiring the bacteria's continued presence in the host. Invasive bacteria grow to large
numbers and induce an inflammatory response — erythema, edema, warmth, and pain.

---

*(Chapter continues from page 36 of the source deck — pages 17-35, on transmission and
spread, are covered separately in Ch. 8.)*

### Biofilms and adherence-related structures {#ch07-6}

**Biofilms** consist of various polysaccharides and proteins, formed after bacterial
attachment. They protect bacteria from both antibiotics and host immune defenses
(antibodies, neutrophils). Biofilms are important in the persistence of *Pseudomonas* in
the lungs of cystic fibrosis patients and in dental plaque formation, the precursor of
dental caries.

**Quorum sensing:** as in *Pseudomonas*, bacteria grow nonaggressively until a certain
density is reached, at which point synthesis of new virulence factors (e.g., biofilms)
contributing to pathogenesis begins (the deck notes this alongside "contact inhibition").
**Contact-dependent growth inhibition (CDI) systems** are designed to achieve direct
physical contact of one bacterial cell with nearby cells via receptor-mediated toxin
delivery.

**Curli:** surface proteins on some strains (e.g., *E. coli*, *Salmonella*) that mediate
bacterial binding to endothelium and to extracellular proteins such as fibronectin. Curli
also interact with serum proteins such as factor XII (coagulation factor), and are
thought to play a role in producing the thrombi seen in disseminated intravascular
coagulation (DIC) associated with sepsis caused by these bacteria. **Thrombus:** a
clotting process that prevents bleeding. **Thrombosis:** when a clot prevents blood flow
in a healthy blood vessel.

### Invasion, inflammation, and intracellular survival {#ch07-7}

Several enzymes are involved in the bacterial invasive process:
1. **Collagenase and hyaluronidase** — degrade subcutaneous tissue; important in
   cellulitis caused by *Streptococcus pyogenes* (a skin infection appearing as a
   swollen, red area of skin).
2. **Coagulase** — produced by *Staphylococcus aureus* and *Yersinia pestis*, accelerates
   fibrin clot formation, which may protect bacteria from phagocytosis by walling off the
   infected area and coating organisms with a fibrin layer.
3. **Immunoglobulin protease** — degrades IgA, allowing the organism to adhere to mucous
   membranes; produced chiefly by *N. gonorrhoeae*, *Haemophilus influenzae*, and
   *Streptococcus pneumoniae* (*S. pyogenes* produces IgG protease instead).
4. **Leukocidins** — pore-forming toxins that can destroy both neutrophilic leukocytes
   and macrophages.

**Other virulence (invasive) factors** act by limiting host defense mechanisms
(phagocytosis):
1. **The capsule** — e.g., in *S. pneumoniae* and *Neisseria meningitidis*; the
   polysaccharide capsule prevents phagocytosis. Opsonization (anticapsular antibodies
   and complement proteins) allows more effective phagocytosis. Vaccines against *S.
   pneumoniae*, *H. influenzae*, and *N. meningitidis* contain capsular polysaccharides
   that induce protective anticapsular antibodies.
2. **Cell wall proteins of Gram-positive cocci** — e.g., M protein of group A
   streptococci (*S. pyogenes*) and protein A of *S. aureus*. M protein is
   antiphagocytic; protein A binds IgG and prevents complement activation. M protein is
   strongly antiphagocytic and a major virulence factor — it binds serum factor H,
   destroying C3-convertase and preventing opsonization by C3b.

**Two types of inflammation caused by bacteria:**
1. **Pyogenic (pus-producing) inflammation** — neutrophils predominate; most important
   pyogenic bacteria are certain Gram-positive and Gram-negative cocci.
2. **Granulomatous inflammation** — macrophages and helper T cells predominate; most
   important organism is *Mycobacterium tuberculosis*. Phagocytosis by macrophages kills
   most bacteria, but some survive and grow within macrophages in the granuloma.

**Chronic Granulomatous Disease (CGD):** a diverse group of hereditary immunodeficiency
diseases in which certain immune cells have difficulty forming reactive oxygen compounds
(most importantly the superoxide radical, due to defective phagocyte NADPH oxidase) used
to kill certain ingested pathogens — leading to granuloma formation in many organs.

**Pseudomembranes:** another inflammation example. Diphtheria and pseudomembranous
colitis are both characterized by inflammatory lesions called pseudomembranes — thick,
adherent, grayish or yellowish exudates on the mucosal surfaces of the throat (diphtheria)
or the colon (pseudomembranous colitis).

**Intracellular survival:** important for some pathogens to avoid the immune system and
cause disease. Intracellular pathogens commonly cause granulomatous lesions — examples:
*Mycobacterium*, *Legionella*, *Brucella*, *Listeria*, and *Histoplasma* (a fungus).
These organisms are not obligate intracellular (unlike *Chlamydia* and *Rickettsia*) —
they prefer an intracellular location, probably because they are protected there from
antibody and neutrophils.

**Bacterial mechanisms for intracellular survival:**
1. Inhibition of phagosome-lysosome fusion.
2. Inhibition of phagosome acidification, reducing lysosomal degradative enzyme
   activity.
3. Escape from the phagosome into the cytoplasm, where there are no degradative enzymes.

*Mycobacterium* and *Legionella* use the first and second mechanisms; *Listeria* species
use the third.

**Invasins** are bacterial surface proteins that help bacterial cells invade host cells,
interacting with cellular receptors of the integrin family of transmembrane adhesion
proteins. Actin microfilaments also help bacteria invade cells. Once inside the cell:
1) some bacteria reside within cell vacuoles (phagosomes); 2) others migrate into the
cytoplasm; 3) some move from the cytoplasm into adjacent cells through tunnels formed
from actin.

Infection of surrounding cells lets bacteria evade host defenses — e.g., *Listeria
monocytogenes* aggregates actin filaments on its surface and is propelled in a
"sling-shot" fashion (actin rockets) from one host cell to another.

**Yops (Yersinia outer-membrane proteins):** produced by several *Yersinia* species
(cause of plague); important virulence factors acting primarily after the organism
invades human cells (12 different proteins). Most important effects: inhibit
phagocytosis by neutrophils and macrophages, and inhibit cytokine production (e.g., TNF)
by macrophages. Example: Yop J of *Yersinia pestis* is a protease that cleaves signal
transduction proteins required for TNF synthesis induction.

**Pathogenicity islands:** genes coding many virulence genes on the bacterial
chromosome. Genes encoding adhesins, invasins, and exotoxins are adjacent to each other
on these islands. Nonpathogenic variants of these bacteria lack these islands, which
appear to have been transferred as a block via conjugation or transduction.
Pathogenicity islands are found in many Gram-negative rods (*E. coli*, *Salmonella*,
*Shigella*, *Pseudomonas*, *Vibrio cholerae*) and Gram-positive cocci (*S. pneumoniae*).

Example (nonpathogenic *E. coli* strain vs. one carrying pathogenicity islands): PAI-A
encodes an enterotoxin; PAI-B encodes pili that bind urinary tract epithelium; PAI-C
encodes enzymes synthesizing the K-1 capsular polysaccharide.

After bacteria colonize and multiply at the portal of entry, they may invade the
bloodstream and spread to other body parts. Receptors for the bacteria on cell surfaces
determine the affected organs — e.g., certain bacteria or viruses infect the brain
because receptors for them are located on brain neuron surfaces.

### Toxin production {#ch07-8}

The second mechanism by which bacteria cause disease.

**Comparison of exotoxins and endotoxins:**

| Property | Exotoxin | Endotoxin |
|---|---|---|
| Source | Certain species of Gram-positive and Gram-negative bacteria | Cell wall of Gram-negative bacteria |
| Secreted from cell | Yes | No |
| Chemistry | Polypeptide | Lipopolysaccharide |
| Location of genes | Plasmid or bacteriophage | Bacterial chromosome |
| Toxicity | High (fatal dose ~1 ug) | Low (fatal dose ~hundreds of ug) |
| Clinical effects | Various effects | Fever, shock |
| Mode of action | Various modes | Includes TNF and interleukin-1 |
| Antigenicity | Induces high-titer antibodies called antitoxins | Poorly antigenic |
| Vaccines | Toxoids used as vaccines | No toxoids formed, no vaccine available |
| Heat stability | Destroyed rapidly at 60C (except staphylococcal enterotoxin) | Stable at 100C for 1 hour |
| Typical diseases | Tetanus, botulism, diphtheria | Meningococcemia, sepsis by Gram-negative rods |

**Exotoxins** are very toxic substances — the fatal dose of tetanus toxin for a human is
estimated at less than 1 ug. Purified exotoxins can reproduce all aspects of the disease,
so bacterial cells are needed only to synthesize the exotoxins that cause pathogenesis.
Exotoxins are polypeptides able to induce synthesis of protective antibodies (as in
botulism and tetanus). **Toxoids** are formaldehyde-, acid-, or heat-treated toxins that
retain antigenicity but lose toxicity — used in vaccine production.

Many exotoxins have an **A-B subunit structure**: the A (active) subunit possesses the
toxic enzymatic activity; the B (binding) subunit binds the exotoxin to specific
receptors on the human cell membrane and determines the exotoxin's specific site of
action (e.g., botulinum toxin acts at the neuromuscular junction). Important A-B subunit
exotoxins: diphtheria toxin, tetanus toxin, botulinum toxin, cholera toxin, enterotoxin
of *E. coli*.

The exotoxin A subunit is often an enzyme catalyzing addition of ADP-ribose to a target
human protein (ADP-ribosylation), which may inactivate or hyperactivate the modified
protein:
- Diphtheria toxin and *Pseudomonas* exotoxin A ADP-ribosylate elongation factor-2
  (EF-2), inactivating it and inhibiting protein synthesis.
- Cholera toxin and *E. coli* toxin ADP-ribosylate the Gs (stimulatory) protein,
  activating it — this increases adenylate cyclase activity, raises cyclic AMP, and
  produces watery diarrhea.

**Mode of action of diphtheria toxin:** the toxin binds to the cell surface via its
binding subunit; the active subunit enters the cell and catalyzes ADP-ribose addition to
EF-2, inactivating it and inhibiting protein synthesis.

**Pertussis toxin** (*Bordetella pertussis*) acts differently — it ADP-ribosylates and
inactivates the Gi (inhibitory) protein. Inactivating this inhibitory regulator turns on
adenylate cyclase, increasing cyclic AMP, which plays a role in whooping cough symptoms.

**Secretion of exotoxins:** exotoxins are released via specialized structures (secretion
systems). The most important and virulent is the **type III secretion system**
("injectosome"), mediated by a needle-like projection (a "molecular syringe") and
transport pumps in the bacterial cell membrane. *Pseudomonas aeruginosa* strains with
this system are significantly more virulent than those without. Other medically important
Gram-negative rods using injectosomes include *Shigella*, *Salmonella*, *E. coli*, and
*Y. pestis*.

**Superantigen:** nonspecific activation of T cells, inducing production of different
cytokines. **Lecithinase:** causes myonecrosis and hemolysis.

**Gram-positive bacterial exotoxins** — several mechanisms, different clinical effects:
1. **Diphtheria toxin** — inhibits protein synthesis by inactivating EF-2.
2. **Tetanus toxin and botulinum toxin** — neurotoxins that prevent neurotransmitter
   release.
3. **Toxic shock syndrome toxin (TSST)**, produced by *S. aureus* — acts as a
   superantigen causing release of large amounts of cytokines from helper T cells and
   macrophages.

1) **Diphtheria toxin** (*Corynebacterium diphtheriae*): inhibits protein synthesis by
ADP-ribosylation of EF-2, leading to cell death and two prominent diphtheria symptoms:
pseudomembrane formation in the throat, and myocarditis.

**Mechanism of action of diphtheria toxin:** exotoxin binds cell membrane receptors ->
transported across the membrane -> active fragment A cleaves and separates -> fragment A
inactivates EF-2 by ADP-ribosylation. The enzymatic activity is specific for EF-2; no
other protein is ADP-ribosylated. The mechanism affects all eukaryotic cells, but none of
the prokaryotic cells.

2) **Tetanus toxin** (*Clostridium tetani*): a neurotoxin that prevents release of the
inhibitory neurotransmitter glycine, leading to muscle spasms/paralysis.

3) **Botulinum toxin** (*Clostridium botulinum*): a neurotoxin that blocks acetylcholine
release at the synapse, producing flaccid paralysis. Approximately 1 ug is lethal for
humans. One toxin subunit is a protease that degrades the protein(s) responsible for
acetylcholine release.

4) *Clostridium difficile* produces two exotoxins, both involved in pseudomembranous
colitis pathogenesis: **Exotoxin A (tcdA)** is an enterotoxin causing watery diarrhea;
**Exotoxin B (tcdB)** is a cytotoxin that damages colonic mucosa and causes
pseudomembranes to form (disrupting the cytoskeleton and tight junctions).

5) *Clostridium perfringens* (gas gangrene) produces multiple toxins; best characterized
is **alpha toxin**, a lecithinase that hydrolyzes lecithin in the cell membrane,
destroying the membrane and causing widespread cell death.

6) *Bacillus anthracis* (anthrax) produces three exotoxins: **edema factor** (an
adenylate cyclase, increases cAMP); **lethal factor** (a protease that cleaves
phosphokinase); **protective antigen** (forms pores in the human cell membrane).

7) **TSST** is a superantigen produced by certain *S. aureus* and *S. pyogenes* strains.
It binds directly to class II MHC proteins on antigen-presenting cells (macrophages)
without intracellular processing, activating cells and causing release of large amounts
of interleukin-1, interleukin-2, and TNF.

**Gram-negative bacterial exotoxins:** important examples — enterotoxins of *E. coli* and
*V. cholerae* (cholera toxin), both increasing cyclic AMP within the enterocyte,
resulting in watery diarrhea.

1. **Heat-labile enterotoxin** (*E. coli*): causes watery, nonbloody diarrhea by
   stimulating adenylate cyclase activity — the resulting cyclic AMP increase causes
   chloride ion excretion, inhibition of sodium ion absorption, and significant fluid and
   electrolyte loss into the gut lumen.
2. **Heat-stable toxin:** affects cyclic GMP rather than cyclic AMP — stimulates
   guanylate cyclase, increasing cyclic GMP, which inhibits sodium ion reabsorption and
   causes diarrhea. Genes for both the heat-labile and heat-stable toxins are carried on
   plasmids. Cellular mechanism: luminal toxin binds to and activates guanylyl cyclase C
   (a brush-border enzyme highly expressed in the small intestine and proximal colon);
   the resulting cGMP increase activates membrane-bound protein kinase G (PKG), which
   opens neighboring anion channels or inhibits neighboring Na/H and Cl/HCO3 exchangers.
3. **Shiga toxin** (also called verotoxin, because it can kill Vero cells, and
   Shiga-like toxin): produced by strains of *E. coli* (O157:H7). These
   enterohemorrhagic strains cause bloody diarrhea and are the cause of outbreaks
   associated with undercooked meat or raw vegetables. The toxin inactivates protein
   synthesis by removing adenine from a specific site on the 28S rRNA in the large
   subunit of the human ribosome. Encoded by a lysogenic bacteriophage. When in the
   bloodstream, can cause hemolytic-uremic syndrome (HUS) — Shiga toxin binds to
   receptors on the kidney and on small-blood-vessel endothelium, inhibits protein
   synthesis, causing cell death that leads to renal failure and microangiopathic
   hemolytic anemia (small blood vessel disease). The antibiotic ciprofloxacin (inhibits
   DNA gyrase) increases the amount of Shiga toxin produced by *E. coli* O157,
   predisposing to HUS.
4. **Pertussis toxin** (*Bordetella pertussis*): catalyzes transfer of ADP-ribose from
   NAD to an inhibitory G protein. Inactivating this inhibitory regulator (Gi) has two
   effects: a) stimulates adenylate cyclase, raising cyclic AMP in affected cells,
   causing edema and other respiratory-tract changes leading to whooping cough; b)
   inhibits the signal transduction pathway used by chemokine receptors, causing the
   marked lymphocytosis seen in pertussis patients (lymphocytes cannot enter lymphoid
   tissue and remain in blood).
5. Enterotoxins produced by *V. cholerae* and *Bacillus cereus* (a cause of diarrhea) act
   similarly to the heat-labile toxin of *E. coli* (increasing cAMP in cells).

**Mode of action of *E. coli* and *V. cholerae* enterotoxins:** the enterotoxin (e.g.,
cholera toxin) binds the enterocyte surface via its binding subunit; the active subunit
enters the enterocyte and catalyzes addition of ADP-ribose to the Gs regulatory protein,
activating adenylate cyclase to overproduce cyclic AMP. Cyclic-AMP-dependent protein
kinase activity increases, and water and electrolytes leave the enterocyte, causing
watery diarrhea.

**Endotoxins:** lipopolysaccharides produced by enzymes encoded by genes on the
bacterial chromosome; integral parts of the cell walls of both Gram-negative rods and
cocci. Low toxicity, producing generalized effects of fever and shock. Weakly antigenic;
not used for vaccine production.

**Mode of action of endotoxin** (affects mainly macrophages): the most important cause of
septic shock, characterized by fever, hypotension, and DIC, which can cause death.
Endotoxin causes these effects by:
1. Activating macrophages to produce IL-1, TNF, and nitric oxide — endotoxin binds
   LPS-binding protein in plasma, and the complex binds CD14 on macrophages, activating
   toll-like receptor-4 (TLR-4).
2. Activating complement to produce C3a and C5a (chemokines).
3. Activating tissue factor, an early component of the coagulation cascade.

Sequence (as depicted): endotoxin (lipopolysaccharide, e.g., of *Pseudomonas
aeruginosa*) -> IL-1, TNF -> fever, DIC, septic shock -> death.

**Two features of septic shock:**
1. Septic shock is characterized by presence of bacteria in the bloodstream, while in
   toxic shock it is the toxin that circulates in the blood (blood culture vs.
   immunological test).
2. Septic shock can cause a patient's death even after antibiotics have killed the
   bacteria in the blood — it is mediated by cytokines (TNF and IL-1).

**Biologic effects of endotoxin:**
1. **Fever** — from IL-1 (endogenous pyrogen) and IL-6 release by macrophages (acting on
   body temperature regulation).
2. **Hypotension/shock** — from induced vasodilation and increased capillary
   permeability.
3. **DIC** — from activation of the coagulation cascade, resulting in thrombosis.
4. **Activation of the alternative complement pathway** — resulting in inflammation and
   tissue damage.
5. **Activation of macrophages**, and activation of many B lymphocyte clones.

Endotoxin effects are indirect — endotoxins:
1. Induce production of cytokines such as IL-1 and TNF from macrophages. Purified
   recombinant TNF reproduces endotoxin's effects, and antibody against TNF blocks
   endotoxin's effects.
2. Induce production of macrophage migration inhibitory factor, playing a role in
   septic shock induction.

Endotoxins can cause fever if present in intravenous fluids. Important: endotoxins must
be sterilized by filtration, which physically removes the organism without releasing its
endotoxin.

**Beneficial and harmful effects of TNF:**

| Beneficial effects of small amounts of TNF | Harmful effects of large amounts of TNF |
|---|---|
| Inflammation (e.g., vasodilation), increased vascular permeability | Septic shock (e.g., hypotension and high fever) |
| Adhesion of neutrophils to endothelium | Disseminated intravascular coagulation |
| Enhanced microbicidal activity of neutrophils | Inflammatory symptoms of some autoimmune diseases |
| Activation and adhesion of platelets | |
| Increased expression of class I and II MHC proteins | |

Endotoxin-like pathophysiologic effects can occur in Gram-positive bacteremic infections
— *S. aureus* and *S. pyogenes* (Gram-positive) have endotoxin-like structures
(lipoteichoic acid) with pathophysiological effects that can cause TNF and IL-1 release
from macrophages.

### Immunopathogenesis {#ch07-9}

When the effect of the immune response itself causes disease symptoms (examples of
hypersensitivity type III):
- **Rheumatic fever:** antibodies form against the M protein of *S. pyogenes*, which
  cross-react with joint, heart, and brain tissue. These antibodies cause inflammation
  resulting in arthritis, carditis, and chorea (abnormal involuntary movement of hands
  and legs).
- **Acute glomerulonephritis:** caused by streptococcal infections.

### Bacterial infections associated with cancer {#ch07-10}

Observations: 1) *Helicobacter pylori* infection is associated with gastric carcinoma and
gastric mucosal-associated lymphoid tissue (MALT) lymphoma; 2) *Campylobacter jejuni*
infection is associated with MALT lymphoma of the small intestine (also known as
alpha-chain disease). It has been observed that antibiotics can cause these cancers to
regress if treated at an early stage.

### Different strains of the same bacteria can produce different diseases {#ch07-11}

*Staphylococcus aureus* causes inflammatory, pyogenic diseases (endocarditis,
osteomyelitis, septic arthritis) as well as nonpyogenic, exotoxin-mediated diseases
(toxic shock syndrome, scalded skin syndrome, food poisoning). Some *E. coli* strains are
harmless; some are Shiga toxin-producing (STEC) and cause food-borne disease.
*Propionibacterium acnes* is given as a further example. Why: individual bacteria
produce different virulence factors, encoded on plasmids, transposons, (lysogenic)
phages, or pathogenicity islands.

### Typical stages of an infectious disease {#ch07-12}

A typical acute infectious disease has four main stages: 1) the incubation period;
2) the prodrome period; 3) the specific-disease period; 4) the recovery
(convalescence) period. After recovery, the outcome may be: chronic carrier state,
latent infection, or subclinical (inapparent) infection.

### Koch's postulates {#ch07-13}

Used to determine whether an organism isolated from a patient actually caused the
disease:
1. The organism must be isolated from every patient with the disease.
2. The organism must be isolated free from all other organisms and grown in pure culture
   in vitro.
3. The pure organism must cause the disease in a healthy, susceptible animal.
4. The organism must be recovered from the inoculated animal.

Isolation of sufficient numbers of the specific pathogen can support the diagnosis. If no
organism was isolated, detection of a fourfold rise in antibody titer in a later serum
sample can support the diagnosis.

---

## Ch. 8 — Transmission and Spread of Microorganisms {#ch08}

> **Source:** 2023-slides, `5_Topic 7, Bacterial Pathogenesis.pdf`, pp. 17-35. Outline
> week 8. Drawn out of the same deck as Ch. 7 — see the note there on how the split was
> made.

### Communicability and disease patterns {#ch08-1}

Many, but not all, infections are communicable (spread from host to host). Example:
tuberculosis is communicable (spread person-to-person via airborne droplets from
coughing); botulism is not, because the exotoxin produced in contaminated food affects
only those eating that food. **Contagious spread:** describes a disease that is highly
communicable.

- **Epidemic infection:** occurs much more frequently than usual.
- **Pandemic:** has a worldwide distribution.
- **Endemic infection:** constantly present at a low level in a specific population.
- **Inapparent/subclinical:** not a clear infection; detectable only by a rise in
  antibody titer or by isolating the organism.
- **Latent infection state:** reactivation of organism growth and recurrence of symptoms
  may occur.
- **Chronic carrier state:** organisms continue to grow with or without producing
  symptoms in the host. Chronic carriers (e.g., "Typhoid Mary") are an important source of
  infection for others and hence a public health hazard.

### Stages of bacterial pathogenesis (overview) {#ch08-2}

A generalized sequence of infection stages:
1. Transmission from an external source into the portal of entry.
2. Evasion of primary host defenses such as skin or stomach acid.
3. Adherence to mucous membranes, usually by bacterial pili.
4. Colonization by growth of the bacteria at the site of adherence.
5. Disease symptoms caused by toxin or invasion, accompanied by inflammation.
6. Host responses, both nonspecific and specific (immunity).
7. Progression or resolution of the disease.

### 1. Transmission {#ch08-3}

Understanding the mode of transmission of bacteria and other infectious agents is
important for interrupting the chain of transmission and preventing infectious diseases.
Different modes of transmission:
- Human-to-human.
- Transmission from nonhuman sources: soil, water, and animals.
- Fomites (such as towels and other clothes).

Example: Shiga toxin-producing *E. coli* (STEC) can be found in ground meat, raw milk,
and fecal contamination of vegetables.

**Vertical transmission:** from mother to offspring, via: 1) across the placenta;
2) the birth canal during birth; 3) breast milk.
**Horizontal transmission:** person-to-person transmission.

Pathogens exit the infected patient via the respiratory and gastrointestinal tracts,
among other routes. Transmission to a new host usually occurs via airborne respiratory
droplets or fecal contamination of food and water. Organisms can also be transmitted by
sexual contact, urine, skin contact, blood transfusions, contaminated needles, or biting
insects. Screening blood donors for pathogens is important to reduce infection risk.

Major bacterial diseases transmitted by ticks (genus *Ixodes*): Lyme disease (*Borrelia*),
Rocky Mountain spotted fever (*Rickettsia*), ehrlichiosis, relapsing fever, and
tularemia. Lyme disease is caused by *Borrelia burgdorferi*, transmitted to humans
through the bite of infected black-legged ticks; typical symptoms include fever,
headache, fatigue, and a characteristic skin rash called erythema migrans.

**Important portals of entry:** respiratory tract, gastrointestinal tract, genital tract,
skin.

Some diseases are transmitted by insects (vectors). **Zoonotic disease:** transmission of
a pathogen between animals (which can be a reservoir host) and humans.

### 2. Adherence to cell surfaces {#ch08-4}

Achieved by specialized structures or substances called **adhesins** that enhance a
pathogen's ability to cause disease — such as pili, and capsules or glycocalyces.
Examples: pili of *Neisseria gonorrhoeae* and *E. coli* mediate attachment to urinary
tract epithelium; glycocalyx of *Staphylococcus epidermidis* and certain viridans
streptococci allows strong adherence to the endothelium of heart valves.

### Reference tables: portals, vertical transmission, food/waterborne and zoonotic pathogens {#ch08-5}

> **Patch note:** these five tables come from pages 19, 20, 24, 27, 29, 30, 33, and 35
> of the same deck, originally logged as image-only diagrams with no extractable
> caption text. Re-read via `prep.py`'s patch mode (Stage 0 vision, scoped to just
> these pages) — they turned out to be dense reference tables, not uncaptioned
> diagrams. Page 20's text layer duplicates the stages-of-pathogenesis list already
> in {#ch08-2}, so nothing new was added from it. Page 19 (a "Typhoid Mary" newspaper
> clipping) and page 35 (an unlabeled flagellum/pili micrograph) remain genuinely
> without extractable new facts — both are illustrations of points already stated in
> prose ({#ch08-1}'s Typhoid Mary example; this section's adhesin discussion).

**Portals of entry of common pathogens:**

| Portal of entry | Pathogen | Disease |
|---|---|---|
| Respiratory tract | *Streptococcus pneumoniae* | Pneumonia |
| | *Neisseria meningitidis* | Meningitis |
| | *Haemophilus influenzae* | Meningitis |
| | *Mycobacterium tuberculosis* | Tuberculosis |
| | Influenza virus | Influenza |
| | Rhinovirus | Common cold |
| | Epstein-Barr virus | Infectious mononucleosis |
| | *Coccidioides immitis* | Coccidioidomycosis |
| | *Histoplasma capsulatum* | Histoplasmosis |
| Gastrointestinal tract | *Shigella dysenteriae* | Dysentery |
| | *Salmonella typhi* | Typhoid fever |
| | *Vibrio cholerae* | Cholera |
| | Hepatitis A virus | Infectious hepatitis |
| | Poliovirus | Poliomyelitis |
| | *Trichinella spiralis* | Trichinosis |
| Skin | *Clostridium tetani* | Tetanus |
| | *Rickettsia rickettsii* | Rocky Mountain spotted fever |
| | Rabies virus | Rabies |
| | *Trichophyton rubrum* | Tinea pedis (athlete's foot) |
| | *Plasmodium vivax* | Malaria |
| Genital tract | *Neisseria gonorrhoeae* | Gonorrhea |
| | *Treponema pallidum* | Syphilis |
| | *Chlamydia trachomatis* | Urethritis |
| | Human papillomavirus | Genital warts |
| | *Candida albicans* | Vaginitis |

**Vertical transmission of important pathogens** — organized by the three routes
already defined in {#ch08-3} (transplacental, birth canal, breast milk):

| Route | Pathogen | Disease in fetus/neonate |
|---|---|---|
| Transplacental | *Treponema pallidum* | Congenital syphilis |
| | *Listeria monocytogenes* | Neonatal sepsis and meningitis |
| | Cytomegalovirus | Congenital abnormalities |
| | Parvovirus B19 | Hydrops fetalis |
| | *Toxoplasma gondii* | Toxoplasmosis |
| Within birth canal / at birth | *Streptococcus agalactiae* (group B strep) | Neonatal sepsis and meningitis |
| | *Escherichia coli* | Neonatal sepsis and meningitis |
| | *Chlamydia trachomatis* | Conjunctivitis or pneumonia |
| | *Neisseria gonorrhoeae* | Conjunctivitis |
| | Herpes simplex virus type 2 | Skin, CNS, or disseminated infection (sepsis) |
| | Hepatitis B virus | Hepatitis B |
| | Human immunodeficiency virus | Asymptomatic infection |
| | *Candida albicans* | Thrush |
| Breast milk | *Staphylococcus aureus* | Oral or skin infections |
| | Cytomegalovirus | Asymptomatic infection |
| | Human T-cell leukemia virus | Asymptomatic infection |

**Transmission of important waterborne diseases:**

| Portal of entry | Pathogen | Disease |
|---|---|---|
| GI tract — ingestion of drinking water | *Salmonella* species, *Shigella* species, *Campylobacter jejuni*, Norovirus, *Giardia lamblia*, *Cryptosporidium parvum* | Diarrhea |
| GI tract — ingestion of water while swimming | *Leptospira interrogans* | Leptospirosis |
| Respiratory tract — inhalation of water aerosol | *Legionella pneumophila* | Pneumonia (Legionnaires' disease) |
| Skin — penetration | *Pseudomonas aeruginosa* | Hot-tub folliculitis |
| | *Schistosoma mansoni* | Schistosomiasis |
| Nose — penetration through the cribriform plate into meninges/brain | *Naegleria fowleri* | Meningoencephalitis |

**Bacterial diseases transmitted by food** (selected — full table covers more
organisms than reproduced here):

| Category | Bacterium | Typical food | Reservoir | Disease |
|---|---|---|---|---|
| Diarrheal — Gram-positive cocci | *Staphylococcus aureus* | Custard-filled pastries, potato/egg/tuna salad | Humans | Food poisoning, especially vomiting |
| Diarrheal — Gram-positive rods | *Bacillus cereus* | Reheated rice | Soil | Diarrhea |
| | *Clostridium perfringens* | Cooked meat, stew, gravy | Soil, animals, humans | Diarrhea |
| | *Listeria monocytogenes* | Unpasteurized milk products | Soil, animals, plants | Diarrhea |
| Diarrheal — Gram-negative rods | *Escherichia coli* | Various foods and water | Humans | Diarrhea |
| | *E. coli* O157:H7 | Undercooked meat | Cattle | Hemorrhagic colitis |
| | *Salmonella enteritidis* | Poultry, meats, eggs | Domestic animals | Diarrhea |
| | *Salmonella typhi* | Various foods | Humans | Typhoid fever |
| | *Shigella* species | Various foods and water | Humans | Diarrhea (dysentery) |
| | *Vibrio cholerae* | Foods and water | Humans | Diarrhea |
| | *Campylobacter jejuni* | Various foods | Domestic animals | Diarrhea |
| Nondiarrheal — Gram-positive rods | *Clostridium botulinum* | Improperly canned vegetables, smoked fish | Soil | Botulism |
| Nondiarrheal — Gram-negative rods | *Brucella* species | Meat and milk | Domestic animals | Brucellosis |
| | *Francisella tularensis* | Meat | Rabbits | Tularemia |
| Nondiarrheal — Mycobacteria | *Mycobacterium bovis* | Milk | Cows | Intestinal tuberculosis |

**Zoonotic diseases caused by bacteria:**

| Group | Pathogen | Animal reservoir | Route | Disease |
|---|---|---|---|---|
| Mycobacteria | *Mycobacterium bovis* | Cows | Ingestion of unpasteurized milk | Intestinal tuberculosis |
| Spirochetes | *Borrelia burgdorferi* | Mice | Tick bite (*Ixodes*) | Lyme disease |
| | *Leptospira interrogans* | Rats and dogs | Urine | Leptospirosis |
| Chlamydiae | *Chlamydia psittaci* | Psittacine birds | Inhalation of aerosols | Psittacosis |
| Rickettsiae | *Rickettsia rickettsii* | Rats and dogs | Tick bite (*Dermacentor*) | Rocky Mountain spotted fever |
| | *Coxiella burnetii* | Sheep | Inhalation of aerosols of amniotic fluid | Q fever |
| | *Ehrlichia chaffeensis* | Dogs | Tick bite (*Dermacentor*) | Ehrlichiosis |

---

## Ch. 9 — Antibiotics {#ch09}

> **Source:** 2023-slides, `7_Topic 8, Antibiotics.pdf`, all 48pp. Outline week 10.

### General principles {#ch09-1}

Antibiotics are medications used to treat bacterial infections. Before beginning
antibiotic therapy, suspected infection sites should be cultured to identify the causative
organism and potential antibiotic susceptibilities.

**Antimicrobial drug stewardship:** reduce inappropriate antibiotic use; encourage
targeted treatment with narrow-spectrum drugs; limit adverse effects.

- **Empirical therapy:** suspected pathogens, not a definitive diagnosis.
- **Prophylactic therapy:** treatment with antibiotics to prevent post-infection.
- **Bactericidal:** kills bacteria.
- **Bacteriostatic:** inhibits growth of susceptible bacteria without immediate killing,
  which can still lead to bacterial death. Related concepts: MIC (minimum inhibitory
  concentration), MBC (minimum bactericidal concentration).

**Use of antibiotic combinations:** for serious infections, for synergistic inhibitory
effect, and to prevent the emergence of resistant mutants.

**Drug interaction types:** indifference, synergism, antagonism.

### Classification by mechanism {#ch09-2}

1. **Inhibition of cell wall synthesis** — penicillins, cephalosporins.
2. **Inhibition of protein synthesis:**
   - Drugs acting on the 30S subunit — aminoglycosides, tetracyclines.
   - Drugs acting on the 50S subunit — chloramphenicol, macrolides, clindamycin.
3. **Inhibition of nucleic acid synthesis:**
   - Inhibition of precursor synthesis — sulfonamides, trimethoprim.
   - Inhibition of DNA synthesis — quinolones, flucytosine.
   - Inhibition of mRNA synthesis — rifampin.

### Cell wall synthesis inhibitors {#ch09-3}

**Penicillins:** first introduced in the 1940s; bactericidal, inhibiting cell wall
synthesis; kill a wide variety of bacteria; also called "beta-lactams."

**Mechanism of action:** inhibit transpeptidases. Penicillins enter the bacteria via the
cell wall and bind to penicillin-binding protein; the result is bacterial cell death from
cell lysis. Penicillins do not kill other (human) cells in the body.

Penicillin-beta-lactamase inhibitor combination drugs — example: amoxicillin +
clavulanic acid.

**Therapeutic uses:** prevention and treatment of infections caused by susceptible
bacteria, particularly Gram-positive bacteria — *Streptococcus*, *Enterococcus*,
*Staphylococcus* species.

**Side effects:** allergic reactions occur in 5-10% of patients (urticaria, pruritus,
angioedema); 10% of allergic reactions are life-threatening. Common side effects: nausea,
vomiting, diarrhea, abdominal pain.

**Cephalosporins:** structurally and pharmacologically related to penicillins;
bactericidal; broad spectrum; divided into generations by antimicrobial activity.

- **First generation:** good Gram-positive coverage, poor Gram-negative coverage.
- **Second generation:** good Gram-positive coverage, better Gram-negative coverage than
  first generation.
- **Third generation:** most potent group against Gram-negative organisms, less active
  against Gram-positive.
- **Fourth generation:** broader spectrum of antibacterial activity than third
  generation, especially against Gram-positive bacteria.

**Other cell-wall-active antibiotics:** beta-lactam drugs — carbapenems (imipenem),
monobactam. Others: vancomycin (glycopeptide), cycloserine and bacitracin.

### Bacterial protein synthesis inhibitors {#ch09-4}

**Tetracyclines:** natural and semi-synthetic, obtained from cultures of *Streptomyces*;
bacteriostatic — inhibit bacterial growth by inhibiting protein synthesis, stopping many
essential bacterial functions.

**Therapeutic uses:** wide spectrum — Gram-negative, Gram-positive, protozoa,
*Mycoplasma*, *Rickettsia*, *Chlamydia*, syphilis, Lyme disease. Demeclocycline is also
used to treat pleural and pericardial effusions.

**Side effects:** strong affinity for calcium — discoloration of permanent teeth and
tooth enamel in fetuses and children; may retard fetal skeletal development if taken
during pregnancy. Alteration of intestinal flora may result in superinfection
(overgrowth of nonsusceptible organisms such as *Candida*), diarrhea, and
pseudomembranous colitis.

**Aminoglycosides:** natural and semi-synthetic, produced from *Streptomyces*; poor oral
absorption (no PO forms); very potent with serious toxicities; bactericidal. Examples:
gentamicin, tobramycin, amikacin, streptomycin.

**Therapeutic uses:** used to kill Gram-negative bacteria such as *Pseudomonas* spp.,
*E. coli*, *Proteus* spp., *Klebsiella* spp., *Serratia* spp.; used in combination with
other antibiotics for synergistic effect.

**Side effects:** serious toxicities — nephrotoxicity (renal failure), ototoxicity
(auditory impairment and vestibular/eighth cranial nerve damage). Drug levels must be
monitored to prevent toxicity.

**Macrolides:** affect the 50S subunit; different generations exist.

**Therapeutic uses:** strep infections caused by *Streptococcus pyogenes* (group A
beta-hemolytic streptococci); mild to moderate upper respiratory infections
(*Haemophilus influenzae*); spirochetal infections (syphilis and Lyme disease);
gonorrhea, *Chlamydia*, *Mycoplasma*, *Legionella*.

**Side effects:** GI effects primarily with erythromycin — nausea, vomiting, diarrhea,
hepatotoxicity, jaundice, anorexia. Newer agents (clarithromycin and azithromycin) have
fewer side effects, longer duration of action, better efficacy, and better tissue
penetration.

**Other protein-synthesis-affecting antibiotics:** clindamycin, linezolid,
chloramphenicol.

### Bacterial nucleic acid synthesis inhibitors {#ch09-5}

**Sulfonamides — folic acid synthesis inhibitors:** bacteriostatic; prevent synthesis of
folic acid required for purine and nucleic acid synthesis; do not affect human cells,
which can use preformed folic acid.

**Therapeutic uses:** combined with phenazopyridine (an analgesic-anesthetic affecting
the urinary tract mucosa) to treat UTIs and reduce UTI-associated pain. Combined with
trimethoprim to treat UTIs, *Pneumocystis carinii* pneumonia, ear infections,
bronchitis, and gonorrhea.

**Quinolones — DNA synthesis inhibitors:** bactericidal; effective against Gram-negative
organisms and some Gram-positive organisms; alter bacterial DNA, causing bacterial
death; do not affect human DNA. Examples: nalidixic acid (a quinolone but not a
fluoroquinolone), ciprofloxacin, levofloxacin, moxifloxacin.

**Therapeutic uses:** lower respiratory tract infections, bone and joint infections,
infectious diarrhea, urinary tract infections (except moxifloxacin), skin infections,
sexually transmitted diseases.

**Rifampin — RNA synthesis inhibitor:** inhibits mRNA synthesis. Used for treatment of
tuberculosis, prophylaxis in close contacts of patients with meningitis, and in
combination with other drugs for treatment of prosthetic-valve endocarditis.

---

## Ch. 10 — Sterilization and Disinfection {#ch10}

> **Source:** 2023-slides, `6_ Sterilization Nov 2020 b.pdf`, all 39pp. Outline week 11.
> **Unclear source text:** pages 4, 6, 7, 18, 19, 21, 22, 25, 26, 28, 31, 32, 36, and 39
> carry diagrams with no extractable caption text.

### Standard precautions and infection control {#ch10-1}

Sterilization and disinfection prevent transmission of microbes to patients. Standard
precautions for interaction with all patients: hand hygiene; respiratory hygiene and
cough etiquette; safe injection practices; proper disposal of needles and scalpels. Use
of personal protective equipment (PPE) — masks or face shields, gloves, gowns, protective
eyewear — when dealing with body fluids or exposed to aerosols. Avoid bacterial
transmission (contact, droplet, and airborne).

**Infection control precautions and practices:**

| Type of precaution | Type of patient / infection | Key practice |
|---|---|---|
| Standard | All patients | Hand hygiene; respiratory hygiene and cough etiquette; safe injection practices; proper disposal of needles and scalpels |
| Standard | Likely exposure to blood, secretions, or body fluids | PPE — mask, face shield, goggles, gloves, or gown (lab coat) |
| Contact | Stool incontinence/diarrhea (e.g., *C. difficile*, norovirus); generalized rash (e.g., varicella); draining wounds | Wear gloves and gown; disinfect room |
| Droplet | Respiratory viruses (e.g., influenza); *Bordetella pertussis* (whooping cough); early *Neisseria meningitidis* infection | Face mask or face shield for patient and provider; disinfect room |
| Airborne | Tuberculosis; measles; varicella when patient is coughing | Isolation room, negative pressure; face mask, N-95 respirator; disinfect room |

### Principles of sterilization and disinfection {#ch10-2}

**Sterilization:** killing or removal of all microorganisms, including bacterial spores.
Usually by autoclaving (steam at 121C under 15 lb/in2 pressure for 15 minutes).
Heat-sensitive instruments are usually sterilized by exposure to ethylene oxide gas
(low-temperature method). Solutions are sterilized by filtration.

In **disinfection**, some organisms and bacterial spores may survive. Disinfectants
include corrosive phenol-containing compounds (toxic), and ethanol and iodine (usable on
skin surfaces). **Antiseptics** are chemicals used to kill microorganisms on the surface
of skin and mucous membranes.

**Uses of common disinfectants and sterilization methods:**

| Clinical use | Disinfectant / method |
|---|---|
| Disinfect surgeon's hands prior to surgery | Chlorhexidine |
| Disinfect surgical site prior to surgery | Iodophor |
| Disinfect skin prior to venipuncture or immunization | 70% ethanol |
| Disinfect skin prior to blood culture or vascular catheter insertion | Tincture of iodine followed by 70% ethanol, or iodophor, or chlorhexidine |
| Cleanse wounds | Thimerosal, chlorhexidine, hydrogen peroxide |
| Cleanse burn wounds | Silver sulfadiazine |
| Cleanup of blood spill (hepatitis B or C patient) | Hypochlorite (bleach, Clorox) |
| Sterilize surgical instruments / heat-sensitive materials (endoscopes, respiratory therapy equipment) | Ethylene oxide or glutaraldehyde |
| Sterilize non-heat-sensitive materials (surgical gowns, drapes) | Autoclave |
| Sterilize intravenous solutions | Filtration |
| Disinfect air in operating room (when not in use) | Ultraviolet light |
| Disinfect floor of operating room | Benzalkonium chloride (Lysol) |
| Disinfect stethoscope | 70% ethanol |
| Preservative in vaccines | Thimerosal |

### Rate of killing of microorganisms {#ch10-3}

Death of microorganisms occurs at a rate dependent primarily on two variables: 1) the
concentration of the killing agent; 2) the length of time the agent is applied. The rate
of killing follows N ~ 1/CT, where N = number of survivors, C = concentration of the
agent, T = time of application.

### Chemical agents {#ch10-4}

Chemicals vary greatly in their ability to kill microorganisms. **Phenol coefficient:** a
quantitative measure of chemical efficiency in killing bacteria — the ratio of phenol
concentration to the agent's required concentration to cause the same amount of killing
under standard test conditions. Disinfectants more effective than phenol have a
coefficient greater than 1; less effective ones have a coefficient less than 1.

Chemicals induce bacterial killing by: 1) disruption of the lipid-containing cell
membrane; 2) modification of proteins; 3) modification of DNA.

**Disruption of cell membranes:**

**Alcohol:** used to clean the skin before immunization or venipuncture. Acts mainly by
disorganizing membrane lipid structure and denaturing proteins. Ethanol requires water
for maximal activity (70% has optimal activity) and is often used as an antiseptic.
Because it is less effective than iodine-containing compounds, the latter should be used
prior to blood culture collection and IV catheter placement. Ethanol will not kill
bacterial spores, so it is not used for sterilization.

100% isopropyl alcohol coagulates proteins instantly, creating a protein layer that
protects other proteins from further coagulation. 70% isopropyl alcohol penetrates the
cell wall more slowly and coagulates all cell wall and organism proteins, killing the
microorganism — extra water content slows evaporation, increasing surface contact time
and enhancing effectiveness. Cited example: *Staphylococcus aureus* was killed in less
than 10 seconds by a 50% isopropyl alcohol solution but was not killed in 2 hours by a
90% solution (Tainter et al., 1944), emphasizing the importance of water in killing
microorganisms.

**Detergents:** "surface-active" agents composed of a long-chain, lipid-soluble,
hydrophobic portion and a polar hydrophilic group (cationic, anionic, or nonionic); these
surfactants disrupt the membrane. Quaternary ammonium compounds (e.g., benzalkonium
chloride) are cationic detergents widely used for skin antisepsis. Benzalkonium chloride
is the active ingredient in Lysol (commercial claim: kills 99.9%), a commonly used
disinfectant for floors and other surfaces.

**Phenols:** phenol was the first disinfectant used in the operating room (Lister, 1860s)
but is rarely used now, being too caustic/corrosive (causes burns). Chlorhexidine is a
chlorinated phenol widely used as a hand disinfectant prior to surgery ("surgical scrub")
and in wound cleansing — remains effective for 6 hours, binding to the skin.
Hexachlorophene, a biphenol with six chlorine atoms, is used in germicidal soaps (can
cause neurotoxicity). Phenols damage membranes and also denature proteins.

**Modification of proteins:**

**Chlorine:** used as a disinfectant to purify water supply and treat swimming pools
(found in hypochlorite, ClO-, bleach/Clorox). A powerful oxidizing agent that kills by
cross-linking essential sulfhydryl groups in enzymes to form the inactive disulfide.

**Iodine:** the most effective skin antiseptic (used prior to blood culture and IV
catheter placement). Like chlorine, an oxidant that inactivates sulfhydryl-containing
enzymes; also binds specifically to tyrosine residues in proteins. Supplied in two forms:
1) Tincture of iodine (2% solution of iodine and potassium iodide in ethanol), used to
prepare skin prior to blood culture — should be removed with alcohol since it can
irritate skin. 2) Iodophors (such as povidone-iodine, a polymer used as an antiseptic) —
complexes of iodine with detergents, used to prepare skin prior to surgery because less
irritating than tincture of iodine.

**Heavy metals:** mercury and silver have the greatest antibacterial activity among heavy
metals and are the most widely used in medicine, acting by binding sulfhydryl groups and
blocking enzymatic activity. Thimerosal (Merthiolate) and merbromin (Mercurochrome),
which contain mercury, are used as skin antiseptics. Silver nitrate drops effectively
prevent gonococcal neonatal conjunctivitis (ophthalmia neonatorum) from *Neisseria
gonorrhoeae* or *Chlamydia*. Silver sulfadiazine is used to prevent burn wound infection.

**Hydrogen peroxide:** used as an antiseptic to clean wounds and disinfect contact
lenses; not effective against catalase-producing bacterial cells. An oxidizing agent that
attacks sulfhydryl groups, inhibiting enzymatic activity.

**Formaldehyde:** available as a 37% water solution (formalin); denatures proteins and
nucleic acids.

**Glutaraldehyde:** has two reactive aldehyde groups, is 10 times more effective than
formaldehyde and less toxic. Used in hospitals to sterilize respiratory therapy
equipment, endoscopes, and hemodialysis equipment.

**Ethylene oxide gas:** used extensively in hospitals to sterilize heat-sensitive
materials such as surgical instruments and plastics. Kills by alkylating both proteins
and nucleic acids. Classified as a mutagen and a carcinogen.

**Acids and alkalis:** strong acids and alkalis kill by denaturing proteins. Many
bacteria are susceptible; *Mycobacterium tuberculosis* resists 2% NaOH (used in
liquefying sputum). Weak acids (benzoic, propionic, citric) are frequently used as food
preservatives because they are bacteriostatic.

**Modification of nucleic acids:**

**Crystal violet (gentian violet):** used as a skin antiseptic; acts by binding the
positively charged dye molecule to the negatively charged phosphate groups of nucleic
acids.

**Malachite green** (a triphenylamine-based dye): an antifungal used in fish farming.

### Physical agents {#ch10-5}

Categories: heat, radiation, filtration.

**Heat:**
1. **Moist heat sterilization (autoclaving)** — kills even spores.
2. **Dry heat sterilization** — 180C for 2 hours; effective for glassware.
3. **Pasteurization** (milk industry) — heating milk to 62C for 30 minutes followed by
   rapid cooling; kills milk-borne pathogens (e.g., *Mycobacterium bovis*, *Salmonella*,
   *Streptococcus*, *Listeria*, *Brucella*), but does not sterilize the milk.

**Radiation:** ultraviolet (UV) light and X-rays.

**UV:** greatest antimicrobial activity occurs at 250-260 nm, the wavelength region of
maximum absorption by DNA's purine and pyrimidine bases. UV irradiation causes formation
of thymine dimers, inhibiting DNA replication. Cells have repair mechanisms (cleavage of
dimers in the presence of visible light, or excision of damaged bases without light).
Used in operating rooms; human exposure should be avoided.

**X-rays:** higher energy and penetrating power than UV; kill mainly by producing free
radicals (hydroxyl radicals) that break covalent bonds in DNA, killing the organism.
X-rays kill vegetative cells readily, but spores are remarkably resistant, probably due
to their lower water content. Used in medicine to sterilize heat-sensitive items such as
sutures, surgical gloves, and plastic items such as syringes.

**Filtration:** used to sterilize heat-sensitive solutions. Autoclaving will not remove
the heat-resistant endotoxin of dead Gram-negative bacteria, which causes fever, so
solutions must be filtered to become pyrogen-free prior to autoclaving. The most commonly
used filter is composed of nitrocellulose with a pore size of 0.22 um, which retains all
bacteria and spores.

---

## Ch. 11 — Viral Structure and Classification {#ch11}

> **Source:** 2023-slides, `8_Virology - Part One 1220.pdf`, pp. 1-26, plus `8_Virology -
> Part Two 1220.pdf`, pp. 1-5. Outline week 12.

### General properties of viruses {#ch11-1}

Viruses: are not cells; need cells for their replication; cannot synthesize their own
energy; are not seen in a light microscope (with exceptions); have DNA or RNA but not
both; have a protein coat; some have a lipoprotein membrane (envelope); are obligate
intracellular.

### Viral nucleic acids {#ch11-2}

Single- or double-stranded DNA, or single- or double-stranded RNA. The nucleic acid can
be linear or circular. DNA is always a single molecule; RNA can exist as a single
molecule or in several pieces (influenza virus and rotavirus have segmented RNA
genomes). Viruses are haploid, except the retrovirus family, which has two copies of its
RNA molecule.

### Viral capsid and symmetry {#ch11-3}

The nucleic acid is surrounded by a protein coat called a capsid, made of capsomer
subunits. **Nucleocapsid:** the structure composed of the nucleic acid genome and the
capsid proteins. Two forms of symmetry:
1. **Icosahedral** (20 faces) — capsomers arranged in 20 triangles forming a symmetric,
   approximately spherical figure (can be enveloped or naked).
2. **Helical** — capsomers arranged in a hollow coil, appearing rod-shaped (there are no
   naked helical viruses).

Cross-section types: A) nonenveloped virus with icosahedral nucleocapsid; B) enveloped
virus with helical nucleocapsid.

Advantage of building the virus particle from identical protein subunits: 1) reduces the
need for genetic information; 2) promotes self-assembly (no enzyme or energy required).

### Viral proteins {#ch11-4}

Capsid proteins protect the genome DNA/RNA from degradation. Viral surface proteins
mediate attachment to specific host cell receptors (important in species and organ
specificity). Outer viral proteins are important antigens, inducing neutralizing
antibody and activating cytotoxic T cells to kill virus-infected cells. Internal proteins
can serve as structural proteins (capsid); some act as enzymes (reverse transcriptase;
some viruses have a DNA or RNA polymerase attached to the genome).

**Serotype:** classification of viruses into subgroups based on surface antigens. Number
of serotypes depends on the number of different antigenic determinants — measles virus
has one serotype; polioviruses have three; rhinoviruses (common cold) have over 100.
Influenza virus, HIV, and hepatitis C virus have multiple serotypes due to quick changes
in antigenic determinants.

**Medical importance of multiple serotypes:**
1. A person is immune only to the specific serotype they were infected by or vaccinated
   against.
2. A vaccine must contain all serotypes (e.g., three for polioviruses) to be completely
   protective.
3. Difficulty producing an effective vaccine if viral antigenicity constantly changes
   (e.g., influenza vaccine needs new antigens every year).

Some viral proteins act as "superantigens" (similar to toxic shock syndrome toxin of *S.
aureus*) — examples: Epstein-Barr virus and cytomegalovirus (both herpesvirus family).
Main hypothesis: production of superantigens activates CD4-positive T cells, which is
required for replication of these viruses.

**Tegumental proteins:** located between the nucleocapsid and the envelope (called matrix
proteins in some viruses); regulatory proteins (transcription and translation factors).

**Viral envelope proteins:** the envelope is a lipoprotein membrane composed of
host-cell-derived lipid and virus-specific protein. May have glycoproteins (of viral
origin) that attach to host cell receptors during cell entry. The matrix protein mediates
the interaction between capsid proteins and the envelope. Most viruses derive their
envelope from the host cell membrane (budding) — exception: herpesviruses, which derive
their envelope from the cell's nuclear membrane. Viral surface proteins (capsid or
envelope glycoproteins) are the principal antigens evoking the host immune response.

Many enveloped viruses transmit person-to-person in respiratory aerosol droplets:
influenza virus, measles virus, rubella virus, respiratory syncytial virus — if they
don't infect directly they dry out and become inactivated. Rhinoviruses (transmitted by
respiratory droplets) are more resistant because they are naked nucleocapsid viruses
(also transmissible by hands). Enveloped viruses are unstable — more sensitive to heat,
drying, detergents, and lipid solvents such as alcohol and ether.

### Atypical virus-like agents {#ch11-5}

Four exceptions to typical viruses:
1. **Defective viruses:** mutated or deleted viral nucleic acid and proteins, needing a
   "helper" virus to provide a missing function for replication.
2. **Pseudovirions:** contain host cell DNA instead of viral DNA within the capsid — can
   infect cells but do not replicate.
3. **Viroids:** consist only of a single molecule of circular RNA without a protein coat
   or envelope; cause several plant diseases.
4. **Prions:** rod-shaped infectious particles composed only of protein (no nucleic
   acids). Example: "slow" disease viruses causing transmissible spongiform
   encephalopathies (Creutzfeldt-Jakob disease [CJD] in humans, scrapie in sheep). Prions
   are much more resistant than viruses to inactivation by UV, heat, formaldehyde, and
   nucleases. Prion protein (morphologically similar to amyloid, an aggregate of proteins
   in nerve cells) is the product of a normal cellular gene, so no immune or
   inflammatory response forms against it in infected brain tissue.

### Classification of medically important viruses {#ch11-6}

Can be based on: 1) the nucleic acid (RNA/DNA); 2) capsid structure and morphology;
3) presence or absence of a virus envelope. (The deck presents classification tables for
DNA viruses (Table 31-1) and RNA viruses (Table 31-2), and classification schemes for
each, as figures without extractable caption text.)

---

## Ch. 12 — Viral Replication {#ch12}

> **Source:** 2023-slides, `8_Virology - Part One 1220.pdf`, pp. 27-51. Outline week 13.
>
> **Update-layer finding:** `2024-slides/9_ Virology - Part Two.pdf` pp. 1-21 covers this
> same material (viral growth curve, attachment/penetration/uncoating, gene expression and
> genome replication, DNA/RNA virus strategies, translation, assembly and release). Per
> the chapter-list plan, this 2024 material was to be layered in as additional
> replication detail. On full read, page by page, it restates the 2023 content
> essentially verbatim, re-paginated one point per slide rather than several per slide —
> it adds no fact not already present in the 2023 source used here. Nothing from the
> 2024 file has been merged in, since there was nothing substantive to merge; this note
> corrects the plan's assumption that it would add distinct content.

### Viral growth curve {#ch12-1}

The time required for the growth cycle varies — minutes for some bacterial viruses, hours
for some human viruses. One infectious virus particle (virion) entering a cell at
infection results in more than 100 infectious virions 10 hours later. The **eclipse
period** is the time during which no infectious virus is detectable within infected
cells (4-5 hours). The **latent period** is the time from infection onset to the
appearance of extracellular virus (eclipse period plus rise period).

**Cytopathic effect (CPE):** the start of cell morphological alteration and cell
lysis/death (not seen in all viruses).

**Viral growth cycle in the cell:**
1. Attachment.
2. Viral genome is uncoated (capsid removed).
3. Early synthesis of mRNA and proteins (functional enzymes needed for replication).
4. Late synthesis of proteins (structural: capsid proteins).
5. Virion progeny are assembled.
6. New viruses exit the cell.

(Example given: adenovirus, a nonenveloped DNA virus.)

### Attachment, penetration, and uncoating {#ch12-2}

Specific surface receptors of the virion attach to specific receptors on the cell
surface; this attachment determines the host range (and organ specificity) of the virus.
Narrow-range vs. broad-range viruses: poliovirus can enter only human and other primate
cells, whereas rabies virus can enter all mammalian cells.

Enveloped viruses use their envelope to fuse with the cell's outer membrane — blocking
this fusion is the target of some antiviral drugs. Virus particles are pinocytosed,
followed by uncoating due to low pH within the pinocytosis vesicle, which later ruptures
to release the virus's inner core. Receptors for viruses on the cell surface are proteins
that have other functions in the cell's life. Examples: CD4 protein on T helper cells and
HIV; rabies virus and the acetylcholine receptor; Epstein-Barr virus and the complement
receptor; vaccinia virus and epidermal growth factor.

Viral receptors are key regulators of host range, tissue tropism, and viral
pathogenesis. Common viral receptors include sialic acid, cell adhesion molecules such as
immunoglobulin superfamily members and integrins, and phosphatidylserine receptors.

**Infectious nucleic acid:** purified viral DNA or RNA (without any protein) that can
carry out the entire viral growth cycle and produce complete virus particles. All viruses
are "infectious" in a person or cell culture, but not all purified genomes are
infectious. Important notes:
1. Proof that nucleic acids are the genetic material.
2. Infectious nucleic acid can bypass the host range specificity provided by viral
   protein-cell receptor interaction.
3. Only certain viruses yield infectious nucleic acid.

Viruses that do not require a polymerase in the virion can produce infectious DNA or
RNA. By contrast, viruses requiring a virion polymerase — poxviruses, negative-stranded
RNA viruses, double-stranded RNA viruses, and retroviruses — cannot yield infectious
nucleic acid.

### Gene expression and genome replication {#ch12-3}

The first step in viral gene expression is mRNA synthesis; viruses follow different
approaches depending on the nature of their nucleic acid. The deck presents "seven
classes of viral genome" per the David Baltimore model (as a figure, no extractable
caption text).

- **Parvoviruses** (DNA viruses) use host cell DNA polymerase to synthesize viral
  double-stranded DNA, and host cell RNA polymerase to synthesize viral mRNA.
- Viruses with a single-stranded, negative-polarity RNA genome (e.g., orthomyxoviruses
  such as influenza virus) use a virion RNA polymerase to synthesize viral mRNA.
- Some viruses with a single-stranded, positive-polarity RNA genome (e.g., retroviruses)
  use a virion DNA polymerase to synthesize a DNA copy of the RNA genome, but a host cell
  RNA polymerase to synthesize viral mRNA.
- Some viruses with a single-stranded, positive-polarity RNA genome (e.g.,
  picornaviruses) use the virion genome RNA itself as their mRNA.

DNA viruses, with one exception, replicate in the nucleus and use the host cell
DNA-dependent RNA polymerase to synthesize mRNA. All DNA viruses encode their own DNA
polymerase to replicate the genome — they do not use the host cell DNA polymerase.
Poxviruses (a DNA genome) are the exception, replicating in the cytoplasm and carrying
their own polymerase within the virus particle. Most RNA viruses undergo their entire
replicative cycle in the cytoplasm; the two principal exceptions are retroviruses and
influenza viruses, both having an important replicative step in the nucleus.

**RNA viruses fall into four groups with different mRNA synthesis strategies:**
1. As in poliovirus — single-stranded RNA of positive polarity, using the RNA genome
   directly as mRNA.
2. As in retroviruses — single-stranded RNA of positive polarity, transcribed into
   double-stranded DNA by the RNA-dependent DNA polymerase (reverse transcriptase)
   carried by the virus (relevant to reverse transcriptase-targeting antiviral drugs).
3. Single-stranded RNA of negative polarity — the virus carries its own RNA-dependent
   RNA polymerase.
4. Double-stranded RNA as genetic material — the virus carries its own polymerase.

**Important features of RNA viruses:**

| RNA genome | Polarity | Virion polymerase | Source of mRNA | Infective genome | Prototype human virus |
|---|---|---|---|---|---|
| Single strand, nonsegmented | + | No | Genome | Yes | Poliovirus |
| Single strand, nonsegmented | - | Yes | Transcription | No | Measles virus, rabies virus |
| Segmented | - | Yes | Transcription | No | Influenza virus |
| Double strand, segmented | +/- | Yes | Transcription | No | Rotavirus |
| Single strand, diploid | + | Yes | Transcription | No | HTLV, HIV |

Once viral mRNA is synthesized, it is translated by host cell ribosomes into viral
proteins. **Early proteins:** produced before genome replication — enzymes required for
replication to synthesize many copies of viral genetic material; most viruses encode
their own replicases. **Late proteins:** structural proteins of the progeny viruses. Some
viral mRNAs are translated into precursor polypeptides (single polypeptide) that must be
cleaved by proteases to produce functional structural proteins; other viral mRNAs
translate directly into structural proteins. Protease inhibitor drugs inhibit these
cleaving enzymes (as in hepatitis C virus and yellow fever virus). (The deck notes "Gag"
— group-specific antigen — in this context.)

The actual viral genome is synthesized based on the principle of complementarity — a
complementary base sequence is first synthesized and serves as a template for
replicating the viral genome.

### Assembly and release {#ch12-4}

Progeny particles are assembled by packaging viral nucleic acid within capsid proteins.
Virus particles are released from the cell by either of two processes:
1. Rupture of the cell membrane, releasing mature particles — usually with nonenveloped
   viruses.
2. Release by budding — enveloped viruses. Budding frequently does not damage the cell;
   in certain instances the cell survives while producing large numbers of budding virus
   particles.

**Budding:** most enveloped viruses derive their lipoprotein envelope from the cell
membrane. The matrix protein mediates the interaction between the viral nucleocapsid and
the viral envelope (exception: herpesviruses, which derive their envelope from the
cell's nuclear membrane).

### Are viruses alive? {#ch12-5}

Only one characteristic of life applies: reproduction. Viruses can only reproduce inside
a host cell. The process of reproduction is the lytic cycle.

### Bacteriophage reproductive cycles {#ch12-6}

Phages (bacterial viruses) have two reproductive cycles.

**Lytic cycle:**
1. The virus injects DNA into the host.
2. Phage DNA becomes part of host DNA.
3. The host cell reads virus DNA and makes virus proteins and more virus DNA.
4. Host ribosomes make new virus particles; the host bursts when full of virus; new
   viruses (phages) infect other cells.

**Lysogenic cycle:**
5. Virus (phage) DNA enters the host and becomes part of host DNA.
6. The host cell copies its own DNA and the virus DNA, reproducing normally but passing
   virus DNA to all its offspring. A cell carrying virus DNA that is not active is called
   a **prophage**.
7. The prophage can become active and enter the lytic cycle at any time.
8. The virus can hide and become inactive if the immune system detects it, hiding inside
   cells where the immune system cannot see it as easily.

Viral DNA integrated into the host cell chromosome (the prophage) produces no progeny
virus particles at that time. If the bacteria are exposed to certain activators (e.g.,
UV), the prophage DNA is excised and the phage enters the lytic cycle.

**Importance of the lysogenic cycle:** it can direct synthesis of exotoxins in bacteria —
diphtheria, botulinum, cholera, and erythrogenic toxins are encoded by the genes of the
integrated bacteriophage (prophage). **Lysogenic conversion** (mediated by transduction)
is the term for new properties a bacterium acquires from expression of integrated
prophage genes. Example: transduction of the diphtheria toxin gene by beta bacteriophage
results in lysogenic conversion of nonlysogenized, nonpathogenic *Corynebacterium
diphtheriae*.

**Lysogeny mechanism:** the linear lambda (λ) phage DNA is injected into the bacterium,
circularizes, and integrates into the bacterial DNA (now called a prophage). When induced
to enter the replicative cycle, aberrant excision of the phage DNA can occur — part of
the phage DNA and part of the bacterial DNA, including the adjacent *gal* gene, are
excised together. The *gal* gene can then be transduced to another bacterium.

---

## Ch. 13 — Viral Pathogenesis {#ch13}

> **Source:** 2023-slides, `8_Virology - Part Two 1220.pdf`, pp. 6-32. Outline week 14.

### Two levels of viral disease {#ch13-1}

Viruses can cause disease on two levels: 1) changes occurring within individual cells;
2) the process (tissue damage and immunopathogenesis) taking place in the infected
patient.

### At the cell level {#ch13-2}

Infected cells may contain **inclusion bodies** containing viral particles, with
different appearances: **Negri bodies** — eosinophilic cytoplasmic inclusions in
rabies-virus-infected brain neurons; **owl's eye inclusion** — seen in the nucleus of
cytomegalovirus-infected cells.

At the cell level, viruses can cause:
1. **Cell death** — due to selective inhibition of macromolecular synthesis (host, not
   viral); protein synthesis is inhibited first, followed by DNA/RNA inhibition.
2. **Fusion of cells to form multinucleated cells (cytopathic effect)** — from cell
   membrane changes caused by viral proteins (infection with herpesviruses and
   paramyxoviruses). Infected cells typically show cytopathic effect (CPE): cell lysis or
   giant cell formation, more visible in cell culture. CPE is the basis for the **plaque
   assay**, an important method for quantifying virus amount in a sample.
3. **Malignant transformation** — characterized by unrestrained growth, prolonged
   survival, and morphologic changes.
4. **No apparent morphologic or functional change** — infection can occur without
   morphologic or gross functional changes, highlighting the wide variation in
   virus-cell interactions.

**Viruses associated with cancer:** Epstein-Barr virus (EBV) — Burkitt's lymphoma;
hepatitis B virus (HBV) — liver cancer; hepatitis C virus (HCV) — liver cancer; human
herpesvirus 8 (HHV-8) — Kaposi's sarcoma; human papillomavirus (HPV) — cervical cancer,
head and neck cancers; human T-cell lymphotropic virus 1 (HTLV) — adult T-cell leukemia;
Merkel cell polyomavirus — skin cancer.

### The infected patient {#ch13-3}

Includes: 1) transmission of the virus and its entry into the host; 2) replication of the
virus and damage to cells; 3) spread of the virus to other cells and organs; 4) the
immune response, both as host defense and as immunopathogenesis; 5) persistence of the
virus in some instances.

**Transmission and portal of entry:** transmission occurs by many different routes and
portals of entry — person-to-person (respiratory secretions, saliva, blood, or semen);
fecal contamination of water or food; vertical and horizontal transmission;
animal-to-human transmission (directly by bite, or indirectly via insects).

### Localized or disseminated infections {#ch13-4}

Most viral infections are either localized to the portal of entry or spread
systemically through the body. Localized infection example: the common cold, caused by
rhinoviruses in the upper respiratory tract. Respiratory viruses have a short incubation
period because they replicate directly in the mucosa; systemic infections such as
poliomyelitis and measles have a longer incubation period because viremia and secondary
replication sites are required. (Example: systemic viral infection by poliovirus,
resulting in paralytic poliomyelitis, CNS = central nervous system.)

### Pathogenesis and immunopathogenesis {#ch13-5}

Signs and symptoms result from cell killing due to inhibition of macromolecular
synthesis. Death of virus-infected cells causes loss of function and disease symptoms.
Examples: poliovirus kills motor neurons, causing paralysis; Ebola virus causes
hemorrhages from damage to vascular endothelial cells.

Symptoms of some diseases are not caused by the virus damaging or killing the infected
cell — e.g., rotavirus induces diarrhea by stimulating enterocytes to produce cytokines
that stimulate enteric neurons, resulting in excess fluid and electrolyte secretion into
the bowel lumen.

Cell killing can also be indirect, via immunologic attack mediated by cytotoxic T cells
and antibodies (antibody-dependent cellular cytotoxicity, ADCC) — example: infected cell
killing by Tc cells in the pathogenesis of hepatitis caused by hepatitis A, B, and C
viruses. Pathogenesis can also relate to deposition of virus-antibody-complement
complexes in various tissues.

### Evasion of host defenses {#ch13-6}

**Immune evasion:** processes viruses use to evade the immune response. Adapted
strategies:
1. **Synthesis of receptors for immune mediators** — vaccinia virus encodes a protein
   that binds IL-1; fibroma virus encodes a protein that binds TNF; cytomegalovirus (CMV)
   encodes a chemokine receptor that binds several chemokines. These proteins block the
   ability of these mediators to interact with receptors on effector cells, reducing host
   defense mechanisms — called cytokine decoys.
2. **Reduction of class I MHC protein expression** — as in HIV and herpesviruses (herpes
   simplex virus and CMV) — reduces the ability of cytotoxic T cells to kill
   virus-infected cells.
3. **Multiple antigenic types/serotypes** — the immune response against one serotype is
   not protective against others. Rhinovirus has more than 100 serotypes; influenza
   virus, HIV, and hepatitis C virus also have multiple serotypes — a difficulty for
   vaccine development against these viruses.

### Persistent viral infections {#ch13-7}

Mechanisms that may play a role in viral persistence:
1. Integration of a DNA provirus into host cell DNA (retroviruses).
2. Immune tolerance — neutralizing antibodies are not formed.
3. Formation of virus-antibody complexes, which remain infectious.
4. Location within an immunologically sheltered/immune-privileged site (e.g., the
   brain).
5. Rapid antigenic variation.
6. Spread from cell to cell without an extracellular phase (direct cell-cell contact).
7. Immunosuppression, as in AIDS.

**Three types of persistent viral infections:**
1. **Chronic-carrier infections** — some patients continue producing significant amounts
   of virus for long periods; can be asymptomatic or result in chronic illness. Examples:
   chronic hepatitis B and hepatitis C virus carriers, and neonatal rubella virus and CMV
   infections.
2. **Latent infections** — as in the herpesvirus group: the patient recovers from the
   initial infection and virus production stops, but symptoms may subsequently recur,
   accompanied by virus production. In herpes simplex virus infections, the virus enters
   a latent state in the sensory ganglia cells.
3. **Slow virus infections** — "slow" refers to the prolonged period, usually measured in
   years, between initial infection and disease onset.

---

## Ch. 14 — Antiviral Agents {#ch14}

> **Source:** 2023-slides, `8_Virology - Part Two 1220.pdf`, pp. 33-51. Outline week 15.
>
> **Update-layer finding:** `Virology - Part Two modified for antiviral drugs 2021.pptx`
> was also checked against this content, since it was flagged in the chapter-list plan as
> a possible addition to this chapter. On full read, it is a condensed re-presentation of
> material already in this range (pathogenesis, immune evasion, persistent infections,
> and this same antiviral drug content) — it contains no antiviral fact beyond what is
> transcribed below. Nothing from it has been merged in for the same reason as Ch. 12's
> 2024 supplement: there was nothing distinct to add.

### General characteristics of antiviral drugs {#ch14-1}

The number of antiviral drugs is very small, due to difficulties obtaining selective
toxicity against viruses.

**Modes of action:** blocking early events in viral replication; blocking viral nucleic
acid synthesis; protease inhibitors (cleave precursor polypeptides); blocking release of
viruses from infected cells.

**Why antivirals are limited:**
1. Difficulty obtaining selective toxicity — since viral replication is tied to host
   cell metabolism, it is very difficult to develop an antiviral that attacks only the
   virus and not the host cell.
2. Antivirals are relatively ineffective because many cycles of viral replication occur
   during the incubation period.
3. Emergence of drug-resistant viral mutants.
4. Restricted spectrum.
5. No standardized in-vitro susceptibility tests.
6. Most inhibit replication rather than eradicate the virus — cure depends on the host
   immune system; immunocompromised patients may have recurrences.
7. Many antivirals need to be activated by viral and cellular enzymes before exerting
   their effect — the activity of these enzymes and substrate concentration influence
   efficacy.

**Potential sites of antiviral attack:** viral attachment, penetration, and uncoating;
reverse transcription (retroviruses); viral replication and integration; transcription
and translation; viral release.

**Classification:**
- Purine and pyrimidine analogues (herpes, CMV, HIV, respiratory syncytial virus).
- Non-nucleoside inhibitors of reverse transcriptase (HIV).
- Direct inhibitor of DNA polymerase and reverse transcriptase — foscarnet.
- Protease inhibitors (HIV).
- Interferon-alpha (hepatitis B and C, herpes).
- Others: amantadine, rimantadine (influenza).

### Inhibitors of cell penetration and uncoating {#ch14-2}

**Amantadine and rimantadine:** two related synthetic amines. Act at early stages of
infection of certain RNA viruses by preventing uncoating or inhibiting RNA transcription.
Active against influenza A but not B. Influenza A virus becomes resistant to both agents
during treatment; resistance requires only a single amino acid change in a transmembrane
protein.

Both agents are taken orally and have low toxicity. Reduce disease severity if given
within the first few hours of symptom onset. Prophylaxis: 70% effective if given daily
during influenza outbreaks. Mechanism: target the M2 (matrix) protein. Toxicity: CNS
complaints — minor nervousness and light-headedness.

### Inhibitors of viral attachment {#ch14-3}

Work through specific interaction with the virus and cell receptor. Blocking can be
achieved by neutralization with antibody (palivizumab). Other examples: enfuvirtide
(blocks entry); maraviroc (a CCR5 binding inhibitor, blocking HIV binding).

### Inhibitors of nucleic acid synthesis {#ch14-4}

Most antivirals are nucleoside analogs that interfere with viral DNA and RNA synthesis,
serving as chain terminators after incorporation into nucleic acids. Most specific agents
act on virus-specific nucleic acid polymerases or transcriptases.

**Nucleoside analogues — general mechanism of action:**
1. Taken up by cells.
2. Converted by viral and cellular enzymes to the triphosphate form.
3. The triphosphate form inhibits DNA polymerase, reverse transcriptase, or RNA
   polymerase — or it may be incorporated into growing DNA, leading to abnormal proteins
   or breakage.

**Acyclovir:** effective against HSV-1, HSV-2, varicella-zoster virus (VZV), and
Epstein-Barr virus (EBV), but not CMV. Causes termination of herpes DNA elongation.
Little toxicity for host cells. CMV is resistant to acyclovir because it does not encode
a thymidine kinase, or its thymidine kinase is unable to phosphorylate the drug.

**Ganciclovir:** an acyclovir analog with a similar mechanism, but active against all
herpesviruses including CMV — the drug of choice for CMV infections (retinitis,
pneumonia, colitis). Low oral bioavailability; given IV. Most common adverse effects:
bone marrow suppression (leukopenia in 40%, thrombocytopenia in 20%) and CNS effects
(headache, behavioral changes, psychosis, coma, convulsions).

**Anti-retroviral agents:**
- **Nucleoside reverse transcriptase inhibitors (chain terminators):** zidovudine/
  azidothymidine (ZDV or AZT), didanosine (ddI), zalcitabine (ddC), stavudine (D4T),
  lamivudine (3TC).
- **Non-nucleoside analogues** (inhibit HIV replication): nevirapine, delavirdine — do
  not require phosphorylation, and bind directly to reverse transcriptase.

**Protease inhibitors:** HIV protease inhibitors — ritonavir, nelfinavir. Produce
non-infectious viral particles/virions. Inhibit the HIV protease required to process HIV
gag precursors into mature gag (capsid, matrix, and nucleocapsid) proteins, thereby
inhibiting viral assembly and release.

### Inhibitors of viral release {#ch14-5}

**Oseltamivir (Tamiflu) and zanamivir:** selectively inhibit the neuraminidase of
influenza virus. Orally administered. Reduce influenza symptoms and shorten illness
duration. Active against both influenza A and B.

### Interferons {#ch14-6}

Antiviral, anticancer, and immunomodulating. Host proteins providing the first line of
defense against viral infections. Recombinant interferons are commonly used. Multiple
sites of action in the viral cycle, but mainly inhibit translation of viral proteins.

Interferon-alpha has shown a definite role in herpes zoster and CMV infections; proved
beneficial in treating chronic hepatitis B and hepatitis C liver infection; active
against HIV in vitro and synergistic with AZT. Some toxicity from effects on host cell
protein synthesis. Toxicity: flu-like syndrome, bone marrow suppression, CNS effects.

---

## Ch. 15 — Introduction to Mycology {#ch15}

> **Source:** 2023-slides, `9_Mycology 2.pdf`, all 25pp. Outline week 16.
> **Unclear source text:** pages 4-6 (yeast/Saccharomycetes), 7 (molds), 11
> (basidiospores), 14, and 24 carry images with no extractable caption text. Page 25 is a
> journal citation for a figure (FEMS Microbiol Rev. 2015;39(6):797-811), reproduced here
> for completeness since it appeared in the source deck.

### Fungal cell structure {#ch15-1}

Comparison between fungi and bacteria: fungi have sterols of the ergosterol type. Fungal
cell wall consists of chitin (long chains of N-acetylglucosamine); may also contain other
polysaccharides such as beta-glucan (also found in bacteria), a long polymer of
D-glucose and the site of action of the antifungal drug caspofungin. Fungal cell membrane
contains ergosterol (found in fungi and protozoa but not human cells) — the site of
action of Amphotericin B and azole drugs.

### Types of fungi {#ch15-2}

1. **Yeast:** single cells reproducing by asexual budding.
2. **Molds:** grow as long filaments (hyphae) forming a mat (mycelium). Some hyphae form
   transverse walls (septate hyphae); others do not (nonseptate hyphae). Nonseptate
   hyphae are multinucleated (coenocytic).

Some fungi are thermally dimorphic — they form different structures at different
temperatures: molds in the environment at ambient temperature, yeasts (or other
structures) in human tissue at body temperature. Most fungi are obligate aerobes; some
are facultative anaerobes; none are obligate anaerobes. All fungi require a preformed
organic source, obtained from decaying matter.

Example organisms: *Histoplasma* affects the lungs; *Blastomyces dermatitidis* affects
lungs and skin and can be systemic; *Coccidioides* causes lung disease.

### Fungal reproduction and spores {#ch15-3}

Some fungi reproduce sexually by forming sexual spores: zygospores, ascospores,
basidiospores. Fungi that do not form sexual spores are termed "imperfect" and classified
as fungi imperfecti (producing spores by mitosis).

Most medically important fungi propagate asexually by forming conidia (asexual spores):
1. **Arthrospores** — arise by fragmentation of hyphae ends; the mode of transmission of
   *Coccidioides immitis*.
2. **Chlamydospores** — rounded, thick-walled, and quite resistant (*Candida*).
3. **Blastospores** — formed by the budding process by which yeasts reproduce asexually
   (some yeasts, e.g., *C. albicans*, can form multiple buds).
4. **Sporangiospores** — formed within a sac (sporangium) on a stalk, by molds such as
   *Rhizopus* and *Mucor* (in soil).

### Immune response to fungi {#ch15-4}

Granulomas are the immune response against systemic fungal diseases
(coccidioidomycosis, histoplasmosis, blastomycosis) — the cell-mediated immune response
is involved in granuloma formation. Fungi do not have endotoxin in their cell walls and
do not produce bacterial-type exotoxins. Activation of the cell-mediated immune system
results in a delayed hypersensitivity skin test response to certain fungal antigens
injected intradermally — a positive skin test indicates exposure to the fungal antigen;
*Candida* antigens can be used to determine whether cell-mediated immunity is normal.

**Nonspecific actions against fungal infections:** healthy skin protects against certain
fungi (*Candida*, dermatophytes); fatty acids in the skin inhibit dermatophyte growth;
normal skin and mucous membrane flora suppress fungi; nasopharyngeal mucous membranes
protect the respiratory tract.

Circulating IgG and IgM are produced in response to fungal infection. The cell-mediated
immune response is protective; its suppression can lead to reactivation and
dissemination of asymptomatic fungal infections and to disease caused by opportunistic
fungi.

### Fungal toxins and allergies {#ch15-5}

**Mycotic infections:** indicate fungal infection in humans. Two other kinds of fungal
disease:
1. **Mycotoxicoses** — caused by ingested toxins. Examples: poisoning from eating
   Amanita mushrooms; ergotism, caused by the mold *Claviceps purpurea*, which infects
   grains; aflatoxins — another ingested toxin, produced by *Aspergillus flavus*, causing
   liver damage and tumors in animals and suspected of causing hepatic carcinoma in
   humans (aflatoxin B1 induces a mutation in the p53 tumor suppressor gene).
2. **Allergies to fungal spores** — characterized by an asthmatic reaction (rapid
   bronchoconstriction mediated by IgE) and eosinophilia; these clinical findings result
   from an immediate hypersensitivity response.

### Laboratory diagnosis {#ch15-6}

1. Direct microscopic examination — finding spores, hyphae, or yeasts after treatment
   with KOH.
2. Culture of the organism — Sabouraud's agar facilitates the appearance of slow-growing
   fungi by inhibiting bacterial growth in the specimen.
3. DNA-based tests.
4. Serologic tests — presence of antibodies (a significant rise in antibody titer) in
   patient serum or spinal fluid, used in diagnosing systemic mycoses. The complement
   fixation test is most frequently used in suspected coccidioidomycosis,
   histoplasmosis, and blastomycosis.

### Antifungal therapy {#ch15-7}

Bacterial antibiotics have no effect on fungal diseases. The most effective antifungal
drugs are amphotericin B and the various azoles:
- **Amphotericin B (Fungizone)** — disrupts fungal cell membranes at the site of
  ergosterol.
- **Azole drugs** — inhibit synthesis of ergosterol.
- **Caspofungin** (an echinocandin, brand name Cancidas) — inhibits synthesis of
  beta-glucan.

---

## Ch. 16 — Parasitology {#ch16}

> **Source:** 2023-slides, `10_Parasitology_summary.pdf`, all 61pp.
> **No outline week.** The course outline's weekly table (weeks 1-17) does not mention
> parasitology, though the course learning outcomes require it ("Define basic principles
> of parasitology as regards structure, classification") and this 61-page deck exists in
> the spine. Placed last because it is the final numbered file in the spine (`10_`,
> following `9_Mycology`) — this ordering is ours, not the outline's.
> **Unclear source text:** pages 6, 18, 22, 34, 35, 41-43, 49, 52, and 58 carry images
> (life cycle diagrams, micrographs, distribution maps) with no extractable caption text.
> The intestinal nematode and trematode/cestode species lists (pp. 53-55) are presented
> in the source as bare genus/species lists with no further description on those pages —
> transcribed as given, not expanded.

### General parasitology concepts {#ch16-1}

Parasites can be: single-celled (protozoa), or multicellular metazoa (helminths/worms).

**Protozoan life cycle stages** (intestinal protozoa): **trophozoite** — the active,
motile, feeding, reproducing form, surrounded by a flexible cell membrane; **cyst** — the
resting stage, nonmotile, nonmetabolizing, nonreproducing, surrounded by a thick wall.

**Helminth life cycle stages** (trematodes, cestodes, nematodes): adult; egg/ova; larva
(different names and forms depending on species). Components of the life cycle:
**definitive host** — where the sexual cycle occurs or the adult is present;
**intermediate host** — where the asexual cycle occurs or the larva is present;
**vector** — an insect or snail that may carry the infective stage; **reservoir host**
(the deck lists this term without further elaboration on this page).

**Diagnosis of parasites:** ova and parasite finding; immunological methods; high
eosinophilia associated with helminth infections; DNA detection.

### Intestinal and urogenital protozoa — overview {#ch16-2}

In the intestinal tract: 1) *Entamoeba histolytica*; 2) *Giardia lamblia*;
3) *Cryptosporidium hominis* (a sporozoan). In the urogenital tract: *Trichomonas
vaginalis* (a flagellate). Blood and tissue protozoa: *Trypanosoma* (flagellate);
*Leishmania* (flagellate); *Plasmodium* and *Toxoplasma* (sporozoans); *Pneumocystis*
(a fungus, but a lung pathogen covered alongside these).

### Intestinal protozoa {#ch16-3}

**Entamoeba histolytica** causes amebic dysentery and liver abscess. Cysts are ingested;
the cyst produces trophozoites that cause amebic dysentery in the colon; trophozoites can
spread to the liver, lung, and brain. The cyst has four nuclei; the mature trophozoite has
a single nucleus. No protective antibodies form; there is no animal reservoir.

Trophozoites invade the colonic epithelium, causing localized necrosis and a typical
"flask-shaped" ulcer. Trophozoites can reach the portal circulation. Can cause bloody
diarrhea. **Diagnosis:** microscopic finding of trophozoites in diarrheal stools or cysts
in formed stools.

**Giardia lamblia** causes giardiasis. Life cycle: trophozoite and cyst. The trophozoite
is pear-shaped with two nuclei, four pairs of flagella, and a suction disk. The cyst has
four nuclei; each cyst gives rise to two trophozoites during excystation in the
intestinal tract.

The trophozoite is confined to the gut wall and does not enter the bloodstream; it
causes malabsorption of protein and fat. Many infected individuals have asymptomatic
infections. Chlorination does not kill the cysts. Mammals as well as humans act as
reservoirs. Advanced symptoms: watery (nonbloody), foul-smelling diarrhea. **Diagnosis:**
microscopic examination; the string test (the deck notes it is "still used").

**Cryptosporidium hominis / C. parvum** causes cryptosporidiosis, with diarrhea as the
main symptom; important in immunocompromised patients. Infection is acquired by
fecal-oral transmission. Infective stage: oocysts, from human or animal sources. The
cysts are highly resistant to chlorination but are killed by pasteurization and can be
removed by filtration.

Life cycle: oocysts release sporozoites; trophozoites form (schizonts and merozoites);
later, zygotes and then oocysts form through the sexual stages. In immunocompromised
patients: watery, non-bloody diarrhea. Symptoms are self-limited in immunocompetent
patients. (Diagnostic note: acid-fast stain of cysts in stool shows cysts appearing red
on a blue background.)

### Urogenital protozoa {#ch16-4}

**Trichomonas vaginalis** causes trichomoniasis. A pear-shaped organism with a central
nucleus and four anterior flagella; exists only as a trophozoite (no cyst form). The
dark median rod visible in stained preparations is the axostyle, characteristic of
trichomonads (approximate size 26 um).

**Pathogenesis and epidemiology:** primary locations are the vagina and the prostate.
Found only in humans; there is no animal reservoir.

### Blood and tissue protozoa — malaria {#ch16-5}

**Plasmodium**, the causative agent of malaria. Four main species infecting humans:
- *Plasmodium vivax* — "vivax, simple, benign, tertian malaria" (43% of cases).
- *Plasmodium malariae* — "malariae, quartan malaria" (7% of cases).
- *Plasmodium falciparum* — "falciparum, malignant, tropical," the most pathogenic/fatal
  (50% of cases).
- *Plasmodium ovale* — "ovale, tertian malaria," rare and confined to tropical regions.

**Life cycle:** vector is the female *Anopheles* mosquito. Two phases: sexual cycle in
mosquitoes, asexual cycle in humans. In humans: 1) exoerythrocytic stage in the liver;
2) erythrocytic stages in red blood cells. In *P. vivax* and *P. ovale*, hypnozoites (a
latent liver-cell form) are produced. The synchronized release of merozoites causes the
periodic fever and chills characteristic of malaria (tertian and quartan patterns).

**Pathogenesis and epidemiology:** red blood cell destruction from merozoite release and
splenic action. Splenomegaly from splenic congestion with erythrocytes, plus hyperplasia
of lymphocytes and macrophages. *P. falciparum* is more severe than the others — it
infects more red cells and causes capillary occlusion with aggregates of parasitized red
cells, leading to life-threatening hemorrhage and necrosis, particularly in the brain
(cerebral malaria). Hemoglobinuria gives the patient's urine a dark color, the origin of
the term "blackwater fever."

Chloroquine-resistant strains now predominate in most malaria-endemic areas; *P.
falciparum* shows chloroquine resistance. **Natural resistance:** individuals with sickle
cell trait; people homozygous recessive for the Duffy blood group antigen. More than 200
million people worldwide have malaria, and more than 1 million die of it each year,
making it the most common lethal infectious disease.

**Clinical findings:** fever and chills, accompanied by headache and myalgias; fever can
reach 41C; shaking chills, nausea, vomiting, abdominal pain; fever followed by drenching
sweats; patients usually feel well between febrile episodes; splenomegaly and
hepatomegaly; anemia is prominent.

**Laboratory diagnosis:** microscopic examination of blood using both thick and thin
Giemsa-stained smears; ring-shaped trophozoites can be seen within infected red blood
cells. *Plasmodium* species typically produce hemozoin pigment in infected red blood
cells, whereas *Babesia* does not (*Plasmodium* metabolizes red-cell heme into
hemozoin). Also: PCR; ELISA.

**Prevention:** chemoprophylaxis for travelers to chloroquine-resistant *P. falciparum*
endemic areas — mefloquine or doxycycline; a fixed-dose combination of atovaquone and
proguanil (Malarone) can also be used. Also: mosquito netting, window screens, protective
clothing, and insect repellents.

### Toxoplasma gondii {#ch16-6}

Causes toxoplasmosis, including congenital toxoplasmosis. **Life cycle:** the definitive
host is the domestic cat; the intermediate host is most other mammalian animals (humans
are accidental hosts). Humans can be infected via: 1) ingestion of infective oocysts
(from soil or cat feces); 2) ingestion of cysts in undercooked meat; 3) congenital
(transplacental) transmission. (Micrograph note: tachyzoites, Giemsa stain, crescent
shaped with a centrally placed nucleus; a tachyzoite is also shown in cardiac muscle
tissue; ocular toxoplasmosis presents as retinochoroiditis.)

**Pathogenesis and epidemiology:** upon intestinal infection, the parasite spreads to
other organs, especially the brain, lungs, liver, and eyes. An effective immune response
(cellular and humoral) develops. Most initial infections are asymptomatic, with parasites
persisting as cysts in tissue. Immunosuppression allows activation of organisms in the
cysts. Congenital infection of the fetus occurs only when the mother is infected during
pregnancy — if infected before pregnancy, the organism is already in cyst form and no
trophozoites remain to cross the placenta. *T. gondii* infection occurs worldwide.

### Trypanosoma {#ch16-7}

("Sleeping sickness.") Three major species:
1. *Trypanosoma cruzi* — causative agent of Chagas' disease (American trypanosomiasis),
   mainly in South America; transmitted by the reduviid bug (kissing bug).
2. *Trypanosoma gambiense* and *Trypanosoma rhodesiense* — causative agents of Human
   African Trypanosomiasis (HAT), in Africa; transmitted by the tsetse fly.

Tsetse-transmitted trypanosomiasis: US$5 billion in annual losses to livestock production
in Africa; 25 million people at risk from sleeping sickness. (Micrograph notes:
*Trypanosoma brucei* species; *T. cruzi*; *T. cruzi* amastigotes in heart tissue.)

### Leishmaniasis {#ch16-8}

Species/forms noted: *L. tropica* (chronic dry-type lesion); *L. major* (papules
ulcerate rapidly — moist, wet sore); *L. aethiopica*. **Vector:** sand flies,
specifically *Phlebotomus* (species transmitting cutaneous leishmaniasis: *P. papatasi*
and *P. sergenti*). In mammals, the parasite lives in macrophages as the amastigote stage
(in tissue and blood); in the insect vector it is the promastigote (called
"leptomonas" in the deck).

Clinical forms shown: cutaneous leishmaniasis; mucocutaneous leishmaniasis (ulcers on
the oral or nasal mucosa); visceral leishmaniasis (abdominal swelling without definite
illness, anemia, dermal nodules or lesions resembling leprosy).

### Other parasites listed in the deck {#ch16-9}

The final pages of the deck present genus/species lists and disease-picture pages for
additional parasites, with limited accompanying text:

- ***Echinococcus granulosus*** (dog tapeworm) — causes echinococcosis (Cyclophyllidea).
- **Trematodes:** *Schistosoma* species, *Fasciola hepatica*, *Clonorchis sinensis*,
  *Fasciolopsis buski* (spelled "fuski" in the source).
- **Cestodes:** *Taenia saginata*, *Taenia solium*, *Hymenolepis nana*, *Hymenolepis
  diminuta* (both spelled "Hymenolopis" in the source), *Diphyllobothrium latum*
  (spelled "Diphylobuthrium" in the source), *Echinococcus granulosus*.
- **Intestinal nematodes:** *Ascaris lumbricoides*; *Trichuris trichiura* (labelled
  "(pigs)" in the source — **Source note:** *T. trichiura* is a human whipworm; the
  "(pigs)" annotation in the deck is preserved as written rather than corrected, since
  its intended meaning is not clear from context); hookworms — *Necator americanus*,
  *Ancylostoma duodenale*; *Strongyloides stercoralis*; *Enterobius vermicularis*;
  *Capillaria hepatica*.
- ***Onchocerca volvulus*** (river blindness) — vector: *Simulium* (black fly). Clinical
  findings pictured: Calabar swelling; sclerotizing keratitis.
