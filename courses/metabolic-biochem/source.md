# Metabolic Biochemistry — Source

Built from `slides/2024-slides/` (19 decks, 537 pages, two parallel lecture series —
Dr. Osama Essawi, 9 decks, and Dr. Suheir Ereqat, 10 decks — teaching the same
course). Both lecturers cover the same topic spine but neither's own chapter
numbering covers every topic the other teaches (Dr. Osama has no standalone
gluconeogenesis/regulation chapter; his material is folded into other chapters
instead). The chapter numbering below is therefore this file's own — assigned in
teaching order, not copied verbatim from either deck — and is fixed once written;
it does not change if a later merge finds more material for a chapter.

Each chapter merges both lecturers' slides on that topic. Where one lecturer says
something the other doesn't, it's included with no special marking — this is
normal for two independent lecture decks on the same subject. Where they actually
diverge on a fact (not just depth of coverage), both are kept side by side with a
**Source note**, per the project's hard rule that the source outranks nobody and
nothing is invented to resolve a disagreement.

Reading order: text layer first (PyMuPDF, free) for all 537 pages. A first pass
flagged pages under a 30-character text floor as vision candidates — but that
floor alone missed real content: several pages carry only a title plus a
full-page embedded diagram (e.g. "Glucose Transporters", "How does insulin
work?" in Ch. 2), where the text layer clears 30 characters on the title alone
while the entire substantive content sits in an image `page.get_text()` never
sees. The actual pass instead rendered every page where an embedded image
covers a substantial fraction of the page area, regardless of title-text
length — confirmed per page via `page.get_images()` / `get_image_rects()`,
not assumed from a character count alone. About 90 pages were read this way
(diagrams, tables, and structures the text layer alone would have missed or
under-described); the rest came from the text layer directly.

---

## Chapter list

1. [Bioenergetics and Introduction to Metabolism](#ch01)
2. [Glycolysis and Fermentation](#ch02)
3. [Pyruvate Dehydrogenase and the Citric Acid Cycle](#ch03)
4. [Oxidative Phosphorylation and the Electron Transport Chain](#ch04)
5. [Feeder Pathways and the Pentose Phosphate Pathway](#ch05)
6. [Glycogen Metabolism](#ch06)
7. [Gluconeogenesis and Regulation of Carbohydrate Metabolism](#ch07)
8. [Fatty Acid Catabolism (β-Oxidation)](#ch08)
9. [Triglyceride Synthesis](#ch09)
10. [Protein Metabolism](#ch10)

---

## Ch. 1 — Bioenergetics and Introduction to Metabolism {#ch01}

> **Source:** Dr. Osama Essawi, "Ch 1 - Bioenergetics and introduction to metabolic
> biochemistry" (37 slides); Dr. Suheir Ereqat, "1) Bioenergetics & introduction to
> metabolism" (28 slides).

### 1.1 Biochemistry and metabolism — definitions {#ch01-1}

Biochemistry is the study of the chemical reactions and energy-transfer processes
that occur in the body. It has a direct impact on medicine: it helps understand and
maintain health, understand disease and its effective treatment, and health/disease
studies have themselves opened new areas within biochemistry.

Biochemistry's four major molecule classes and disease examples given: nucleic
acids → genetic disease; proteins → sickle cell anemia; lipids → atherosclerosis;
carbohydrates → diabetes mellitus.

**Metabolism** is the sum of all chemical reactions in the cell — the set of
chemical reactions that happen in living organisms to maintain life. These
processes let organisms grow and reproduce, maintain their structures, and respond
to their environment. Related reactions form **metabolic pathways**, which can be
linear, branched, or cyclic.

Metabolism = **Catabolism** + **Anabolism**:
- **Catabolism** — the degradative, energy-**yielding** phase; breaks down
  more-complex molecules into simpler ones. Catabolic pathways are **convergent**.
- **Anabolism** — the energy-**requiring** phase; builds simpler molecules up into
  more-complex ones. Anabolic pathways are **divergent**.

Catabolic reactions provide the energy that drives anabolic reactions forward
(energy coupling).

### 1.2 Autotrophs and heterotrophs {#ch01-2}

Living organisms are built of complex, low-entropy structures; building such
structures is only possible when energy is spent in the process. The ultimate
source of that energy on Earth is sunlight.

Two large groups of organisms, by carbon source:
- **Autotrophs** — use atmospheric CO₂ to construct carbon-containing biomolecules;
  can be photosynthetic, using sunlight directly for energy.
- **Heterotrophs** — obtain carbon from complex organic molecules such as glucose;
  rely on organic nutrients.

Autotrophs and heterotrophs exist in an interdependent cycle, exchanging carbon,
oxygen, and water. Solar energy is the driving force behind the global cycling of
carbon, oxygen, and nitrogen.

### 1.3 Reactions in metabolic pathways {#ch01-3}

Energy-releasing reactions are coupled to energy-requiring reactions (**coupled
reactions**). Other reaction types seen repeatedly in pathways: reduction/oxidation
reactions, electron-transfer reactions, and **activation** — the formation of a
more reactive species.

### 1.4 Thermodynamics and bioenergetics {#ch01-4}

**Thermodynamics** is the study of energy. **Bioenergetics** describes the
transfer and utilization of energy in living systems.

**Laws of thermodynamics:**
- **First law (conservation of energy)** — for any physical or chemical change,
  the total energy in the universe stays constant; energy may change form or be
  transported, but is never created or destroyed.
- **Second law** — the universe always tends toward increasing disorder
  (**entropy**); in all natural processes the entropy of the universe increases.
  Dr. Suheir's slides add: cells themselves are **not** disordered, and so have
  low entropy — examples of entropy given are diffusion and ice.

**Thermodynamic quantities:**
- **Free energy (ΔG)** — the portion of a system's energy that can perform work
  (at constant T); the energy available to do work. Organisms live at the expense
  of free energy.
  - **Exergonic** reaction — net release of free energy to the surroundings
    (ΔG < 0).
  - **Endergonic** reaction — absorbs free energy from surroundings (ΔG > 0).
  - When a reaction reaches equilibrium, ΔG = 0.
- **Enthalpy (ΔH)** — the heat content of the reacting system; a measure of all
  (total) the energy in a system.
  - Exothermic reaction: releases heat (ΔH < 0). Endothermic: absorbs heat
    (ΔH > 0).
- **Entropy (ΔS)** — a measure of randomness/disorder in a system. Reactions with
  a gain in entropy involve more disordered products.

**Free energy equation:** ΔG = ΔH − TΔS, where ΔG = free energy, ΔH = enthalpy
(total energy), T = temperature in K, ΔS = entropy.

**Equilibrium constant and standard free energy:**
- **Equilibrium constant (Keq)** — defined by the concentrations of reactants and
  products at equilibrium in a general reaction.
- **Standard free-energy change (ΔG′°)** — the force driving a system toward
  equilibrium under standard conditions of temperature, pressure, and initial
  concentrations.
- Relationship: **ΔG′° = −RT ln Keq′**

### 1.5 Energetics of chemical reactions {#ch01-5}

- **Hydrolysis reactions** tend to be strongly favorable (spontaneous).
- **Isomerization reactions** have smaller free-energy changes; isomerization
  between enantiomers has ΔG′° = 0.
- **Complete oxidation of reduced compounds** is strongly favorable — this is how
  chemotrophs obtain most of their energy. In biochemistry the oxidation of
  reduced fuels with O₂ is stepwise and controlled. Being thermodynamically
  favorable is not the same as being kinetically rapid.

(Osama's slides cite "TABLE 13-4 Standard Free-Energy Changes of Some Chemical
Reactions" for further examples — the table itself is not reproduced on the
slide.)

### 1.6 Organic chemistry review and chemical reactivity {#ch01-6}

Most reactions in biochemistry are thermal, heterolytic processes. Nucleophiles
react with electrophiles. Heterolytic bond breakage often gives rise to
transferable groups such as protons. Oxidation of reduced fuels often occurs via
transfer of electrons and protons to a dedicated redox cofactor.

Most reactions in living cells fall into one of five general categories:
1. Reactions that make or break carbon–carbon bonds
2. Internal rearrangements, isomerizations, and eliminations
3. Free-radical reactions
4. Group transfers
5. Oxidation–reductions

**Homolytic vs. heterolytic cleavage** — covalent bonds can be broken either way.
Homolytic cleavage is very rare. Heterolytic cleavage is common, but its products
are highly unstable, and this instability dictates the chemistry that follows.

**Nucleophiles and electrophiles** — nucleophiles are electron donors;
electrophiles are electron acceptors.

**C–C bond formation/breakage** — a C–C bond is formed in both the aldol
condensation and the Claisen ester condensation. In the decarboxylation of a
β-keto acid, a C–C bond is broken.

**Addition–elimination reactions** — an elimination that does not affect overall
oxidation state is loss of water from an alcohol, introducing a C=C bond. Similar
eliminations occur in amines.

**Group transfer reactions** — transfer of acyl, glycosyl, and phosphoryl groups
from one nucleophile to another is common in living cells. Acyl group transfer
generally involves addition of a nucleophile to the carbonyl carbon of an acyl
group, forming a tetrahedral intermediate.

### 1.7 Phosphoryl transfer and ATP {#ch01-7}

Phosphoryl group transfers are significant throughout metabolic pathways.
Inorganic orthophosphate (Pi) and inorganic pyrophosphate (PPi) are common
leaving groups in nucleophilic substitution reactions. Nucleophilic substitutions
are facilitated by attaching a phosphoryl group to a poor leaving group, such as
hydroxyl (OH). In metabolic reactions, a phosphoryl group is often transferred
from ATP to form a phosphate ester.

**Why ATP hydrolysis is highly favorable under standard conditions:**
- Better charge separation in products
- More favorable resonance stabilization of products
- Energy is released from ATP through the loss of phosphate groups

Catabolically, hydrolysis of ATP produces ADP + Pi (inorganic phosphate) + energy.

**Actual ΔG of ATP hydrolysis differs from ΔG′°:** the actual free-energy change
of a process depends on the standard free energy *and* the actual concentrations
of reactants and products. Cellular concentrations of ATP, ADP, and Pi are not
identical to standard conditions and are lower than them. The true reactant and
product are **Mg-ATP** and **Mg-ADP** respectively — ΔG′° of ATP hydrolysis is
Mg²⁺-dependent.

**Why some phosphorylated compounds have large, negative ΔG′° of hydrolysis** —
their products are more stable than the reactants because of one or more of:
1. Electrostatic repulsion in the reactant bond is relieved by charge separation
   (e.g., ATP).
2. The products are stabilized by ionization/resonance (e.g., ATP, acyl
   phosphates, thioesters).
3. The products are stabilized by isomerization (tautomerization) (e.g.,
   phosphoenolpyruvate).

**Worked examples of high-ΔG′° hydrolysis:**
- **Phosphoenolpyruvate (PEP)** — undergoes hydrolysis in glycolysis, ΔG′° =
  −61.9 kJ/mol. Hydrolysis of PEP (coupled to ATP synthesis, catalyzed by
  pyruvate kinase) yields the enol form of pyruvate, which tautomerizes to the
  more stable keto form. Removal of Pi from PEP's ester linkage is spontaneous
  because the enol spontaneously converts to a ketone; the greater resonance
  stabilization of the released Pi also contributes to the negative ΔG′°.
  Sequence: PEP → enolpyruvate → pyruvate, with ADP → ATP.
- **1,3-Bisphosphoglycerate** — a glycolytic intermediate. Water addition across
  the anhydride bond gives 3-phosphoglyceric acid directly, favoring the forward
  reaction; further metabolism of 3-phosphoglyceric acid and formation of a
  resonance-stabilized ion also favor the forward direction.
- **Thioesters (e.g., acetyl-CoA)** — hydrolysis of thioesters is strongly
  favorable. Acetyl-CoA is an important donor of acyl groups: it feeds
  two-carbon units into metabolic pathways and supplies fatty acid synthesis.

**Why ATP specifically (and not, say, PEP) is the cell's main energy currency —
"intermediate energy release":**
- While compounds like PEP release more energy per hydrolysis, ATP's
  intermediate energy release suits cellular processes — releasing too much
  energy at once could be inefficient or harmful.
- **Regulation** — controlled ATP hydrolysis gives a managed, regulated energy
  release, letting energy release be tuned to specific cellular activities.
- **Economic considerations** — ATP synthesis and hydrolysis are efficiently
  coupled to metabolic pathways; the cost of ATP synthesis/usage is reasonable.
- **Buffering capacity** — ATP is present in high concentrations, giving a
  readily available energy reservoir.

More generally, ATP is a good energy source because it can participate in many
different kinds of cellular reactions, is usually directly involved in reactions,
and wastes little energy during phosphorylation of an intermediate.

### 1.8 Oxidation–reduction reactions {#ch01-8}

**Dehydrogenations** are common biological oxidations where a compound loses two
electrons and two hydrogen ions. In some biological oxidations, carbon atoms
become covalently bonded to oxygen. Oxidations must be accompanied by
reductions, where an electron acceptor takes up the electrons removed during
oxidation. Oxidation reactions generally release energy, and most living cells
obtain energy by oxidizing metabolic fuels like carbohydrates or fats.

Many biochemical redox reactions transfer two electrons at once; to keep charges
balanced, proton transfer often accompanies electron transfer. In many
dehydrogenases, the reaction proceeds by stepwise transfer of a proton (H⁺) and a
hydride (:H⁻) — illustrated on the slides by the reversible oxidation of a
secondary alcohol to a ketone.

**NAD and NADP are the common redox cofactors** cited for these reactions.

### 1.9 Enzymes {#ch01-9}

Maximizing cellular efficiency depends on using ATP as noted above, plus:
- **Enzymes** — biological catalysts that facilitate and accelerate biochemical
  reactions; they enhance reaction specificity and decrease randomness in
  cellular reactions.
- **Enzyme regulation** — governs the regulation and optimization of cellular
  reactions.

**How enzymes work:**
- **Substrate binding** — enzymes have a specific active site for substrate
  binding; the enzyme is substrate-specific. Substrate = any molecule to which an
  enzyme will bind. Although an enzyme can be a large protein, only a specific
  region (the active site) interacts with the substrate. Binding forms an
  enzyme–substrate complex that brings the substrate's reactive groups into
  proximity, facilitating the reaction. **Induced fit** occurs as a result of the
  enzyme–substrate complex — as enzyme and substrate bind, the enzyme's shape is
  modified to better fit the substrate.
- **Catalysis of the reaction** — enzymes stabilize the transition state,
  lowering activation energy, which accelerates the specific biochemical
  reaction.
- **Product formation and release** — catalyzed reactions form products; products
  are released and the enzyme is unchanged, so it is available for reuse in
  further catalytic cycles.
- Some enzymes use helper molecules: a **cofactor** is an inorganic molecule
  (a mineral); a **coenzyme** is an organic, non-protein molecule (a vitamin).

### 1.10 Regulation of metabolism {#ch01-10}

- **Allosteric regulation** — enzyme function can be stimulated or inhibited by
  the binding of molecules to an allosteric site (a site other than the active
  site).
- **Feedback inhibition** — the end product of a metabolic pathway can act as an
  allosteric inhibitor of an earlier enzyme in that same pathway, helping
  regulate and control metabolic flux.

---

## Ch. 2 — Glycolysis and Fermentation {#ch02}

> **Source:** Dr. Osama Essawi, "Ch2 - Glycolysis and fermentation" (29 slides);
> Dr. Suheir Ereqat, "2) Glycolysis" (35 slides).

### 2.1 Central importance of glucose {#ch02-1}

Glucose is an excellent fuel: it yields a good amount of energy on complete
oxidation (ΔG = −2840 kJ/mol), can be stored efficiently in polymeric form, and
many organisms/tissues can meet their energy needs on glucose alone. Glucose is
also a versatile biochemical precursor — many organisms can use it to generate
all the amino acids, membrane lipids, nucleotides for DNA/RNA, and metabolic
cofactors.

**Major pathways of glucose utilization:**
- **Synthesis of structural polysaccharides** — alternate carbohydrates used in
  the cell walls of bacteria, fungi, and plants.
- **Storage** — as starch or glycogen (polymeric form), for later energy needs.
- **Energy production** — via oxidation of glucose, for short-term energy needs.
- **Production of NADPH and pentoses** — NADPH for relieving oxidative stress and
  for fatty acid synthesis; pentose phosphates for DNA/RNA biosynthesis.

### 2.2 Glucose transporters and insulin (Dr. Suheir only) {#ch02-2}

Four glucose transporter isoforms, each tissue-restricted:

| Transporter | Tissue | Insulin dependence |
|---|---|---|
| GLUT1 | Blood (RBCs), blood–brain barrier, placenta | Insulin-independent |
| GLUT2 | Liver, pancreatic β cells, small intestine | Insulin-independent |
| GLUT3 | Brain, neurons | Insulin-independent |
| GLUT4 | Skeletal muscle, adipose tissue, cardiac muscle | Insulin-dependent |

> **Unclear source text:** the GLUT3 and GLUT4 rows' bullet text is cut off at
> the bottom edge of the slide capture (GLUT3's line reads "Insulin Independent,
> low K..." with the rest unreadable; GLUT4's reads "Insulin Depen..." cut at
> the same point). Both transporters' insulin-dependence label itself is legible
> and reproduced above; only the trailing qualifier text is lost.

**How insulin triggers GLUT4-mediated glucose uptake** (5-step diagram): (1)
insulin binds the insulin receptor at the cell surface; (2) the receptor
autophosphorylates; (3) the resulting signal triggers a GLUT4-containing
intracellular vesicle to move toward the plasma membrane; (4) the vesicle fuses
with the plasma membrane; (5) GLUT4 is now embedded in the membrane and
transports glucose into the cell.

### 2.3 Glycolysis — overview {#ch02-3}

**Glycolysis** is a nearly universal 10-step metabolic pathway that converts one
molecule of glucose into two molecules of the three-carbon compound pyruvate,
via a series of enzyme-catalyzed reactions. All carbohydrates that are to be
catabolized must enter the glycolytic pathway. Pyruvate can be further
aerobically oxidized, or used as a biosynthetic precursor. Some of the free
energy released is captured as ATP and NADH.

The glycolytic breakdown of glucose is the **sole source of metabolic energy**
in some mammalian tissues and cell types — named on Dr. Suheir's slides as
**erythrocytes, renal medulla, and brain**.

Glycolysis releases only a small fraction of the total available energy of the
glucose molecule; the two pyruvate molecules it produces still hold most of
glucose's chemical potential energy, extractable by the citric acid cycle and
oxidative phosphorylation.

**Three noteworthy types of chemical transformation** recur through glycolysis:
1. Degradation of the carbon skeleton of glucose to yield pyruvate.
2. Phosphorylation of ADP to ATP by compounds with high phosphoryl-group
   transfer potential, formed during glycolysis.
3. Transfer of a hydride ion (H⁻) to NAD⁺, forming NADH.

**Importance of phosphorylated intermediates** — each of the nine glycolytic
intermediates between glucose and pyruvate is phosphorylated. The phosphoryl
groups serve three functions:
1. They prevent the (charged) intermediates from leaving the cell.
2. The high-energy phosphate compounds formed in glycolysis (1,3-BPG, PEP)
   donate phosphoryl groups to ADP to form ATP — an essential component of
   metabolic energy conservation.
3. Binding energy from phosphate-group binding at enzyme active sites lowers
   activation energy and increases the specificity of the enzymatic reactions.

### 2.4 Two stages of glycolysis {#ch02-4}

- **A. Preparatory (energy-investment) phase** — reactions 1–5. Glucose is
  converted to two molecules of glyceraldehyde 3-phosphate; two ATP are
  consumed (spent to raise the free energy, ΔG, of the intermediates).
- **B. Payoff phase** — reactions 6–10. The two glyceraldehyde 3-phosphate
  molecules are converted to two pyruvate, with formation of 4 ATP and 2 NADH
  (a **net** of 2 ATP and 2 NADH per glucose, once the 2 ATP spent in the
  preparatory phase are subtracted). Two molecules of 1,3-bisphosphoglycerate
  are converted to two molecules of pyruvate over this phase.

Because one glucose yields **two** triose-phosphate molecules at the end of the
preparatory phase, the energy yields of every payoff-phase reaction are
effectively doubled per glucose.

### 2.5 The ten reactions of glycolysis {#ch02-5}

Each entry gives the enzyme, the transformation, its standard free-energy
change ΔG′° (from Dr. Suheir's slides — not given in Dr. Osama's), and notable
mechanistic detail from either lecturer.

**Preparatory phase:**

1. **Hexokinase** — glucose + ATP → glucose 6-phosphate + ADP (Mg²⁺-requiring).
   ΔG′° = −16.7 kJ/mol. Irreversible under intracellular conditions. First ATP
   utilization. Hexokinase is present in the cytosol of most tissues of nearly
   all organisms; humans have four isozymes (hexokinase I–IV). **Hexokinase IV
   = glucokinase**, found in hepatocytes, with different kinetic/regulatory
   properties from the other isoforms (below). In the hexokinase–glucose
   enzyme–substrate complex, the two lobes of the enzyme swing together to
   engulf the substrate (induced fit); this excludes water from the active
   site, which prevents wasteful ATP hydrolysis.
   - **Hexokinase vs. glucokinase, compared:**

     | | Hexokinase (I–III) | Glucokinase (hexokinase IV) |
     |---|---|---|
     | Location | Cytosol of most tissues | Liver, pancreatic β cells |
     | Specificity | Low | High |
     | Km for glucose | Low (~0.1 mM) — high affinity | High (~10 mM) |
     | Product inhibition | Inhibited by its own product, glucose 6-phosphate | Inhibited by fructose 6-phosphate (not glucose 6-P) |

     A kinetics graph (relative enzyme activity vs. glucose concentration)
     shows hexokinase I saturating (plateauing near 1.0) by ~5 mM glucose,
     while glucokinase (hexokinase IV) rises far more gradually and has not
     plateaued even by ~20+ mM — consistent with the Km values above.

2. **Phosphohexose isomerase** (phosphoglucose isomerase) — reversible
   isomerization of glucose 6-phosphate (an aldose) to fructose 6-phosphate (a
   ketose), Mg²⁺-assisted, via an enediol intermediate. ΔG′° = +1.7 kJ/mol.
   Reaction proceeds readily in either direction.

3. **Phosphofructokinase-1 (PFK-1)** — fructose 6-phosphate + ATP → fructose
   1,6-bisphosphate + ADP (Mg²⁺-requiring). ΔG′° = −14.2 kJ/mol. Essentially
   irreversible under cellular conditions; the first **"committed" step** of
   glycolysis. Second ATP utilization.

4. **Aldolase** (fructose-1,6-bisphosphate aldolase) — cleaves fructose
   1,6-bisphosphate (reverse aldol condensation) into glyceraldehyde
   3-phosphate (an aldose) and dihydroxyacetone phosphate (a ketose). ΔG′° =
   +23.8 kJ/mol. Reversible in the cell because reactant concentrations are
   low. Aldolase runs in the **reverse** direction during gluconeogenesis.

5. **Triose phosphate isomerase** — converts dihydroxyacetone phosphate to
   glyceraldehyde 3-phosphate. ΔG′° = +7.5 kJ/mol. Reversible; final step of
   the preparatory phase.

**Payoff phase** (all yields ×2 per glucose, from here on):

6. **Glyceraldehyde 3-phosphate dehydrogenase** — oxidizes glyceraldehyde
   3-phosphate (+ inorganic phosphate + NAD⁺) to 1,3-bisphosphoglycerate (+
   NADH + H⁺). ΔG′° = +6.3 kJ/mol. The **1st energy-conserving reaction** of
   glycolysis, eventually leading to ATP formation. Mechanistically, the
   aldehyde group of glyceraldehyde 3-phosphate is oxidized not to a free
   carboxyl group but to a mixed carboxylic–phosphoric acid anhydride (an
   **acyl phosphate**) — this anhydride type has a very high standard free
   energy of hydrolysis, conserved by forming the acyl phosphate group at C-1.

7. **Phosphoglycerate kinase** — transfers the high-energy phosphoryl group
   from the carboxyl group of 1,3-bisphosphoglycerate to ADP, forming ATP and
   3-phosphoglycerate. ΔG′° = −18.5 kJ/mol. This is **substrate-level
   phosphorylation** — ATP formation by phosphoryl-group transfer from a
   substrate (soluble enzymes and chemical intermediates), distinct from
   respiration-linked phosphorylation (membrane-bound enzymes, transmembrane
   proton gradients). Note: the enzyme is named for the *reverse* reaction (it
   catalyzes both directions) — it runs in the phosphoglycerate-kinase-named
   direction during gluconeogenesis.

8. **Phosphoglycerate mutase** — reversible shift of the phosphoryl group
   between C-2 and C-3 of glycerate (3-phosphoglycerate ⇌ 2-phosphoglycerate),
   Mg²⁺-requiring. ΔG′° = +4.4 kJ/mol. Mechanism: the enzyme is first
   phosphorylated on a His residue; the phosphoenzyme transfers its phosphoryl
   group to 3-phosphoglycerate, forming 2,3-bisphosphoglycerate (2,3-BPG) as an
   intermediate; the phosphoryl group at C-3 of 2,3-BPG is then transferred
   back to the same His residue, producing 2-phosphoglycerate and regenerating
   the phosphoenzyme.

9. **Enolase** — reversible removal of a water molecule from 2-phosphoglycerate
   to yield phosphoenolpyruvate (PEP), via a Mg²⁺-stabilized enolic
   intermediate. ΔG′° = +7.5 kJ/mol. The **2nd energy-conserving reaction** of
   glycolysis, eventually leading to ATP formation.

10. **Pyruvate kinase** — transfers the phosphoryl group from PEP to ADP,
    yielding pyruvate + ATP; requires K⁺ and either Mg²⁺ or Mn²⁺. ΔG′° = −31.4
    kJ/mol. Essentially irreversible under intracellular conditions and an
    important site of regulation. Net production: 2 ATP per glucose from this
    step. Substrate-level phosphorylation, same mechanism class as reaction 7.

### 2.6 Overall balance and fates of pyruvate {#ch02-6}

**Overall equation** (before cancellation):
Glucose + 2 ATP + 2 NAD⁺ + 4 ADP + 2 Pi → 2 pyruvate + 2 ADP + 2 NADH + 2 H⁺ +
4 ATP + 2 H₂O

**Net equation** (after subtracting the 2 ATP spent in the preparatory phase):
Glucose + 2 NAD⁺ + 2 ADP + 2 Pi → 2 pyruvate + 2 NADH + 2 H⁺ + 2 ATP + 2 H₂O

- Used: 1 glucose, 2 ATP, 2 NAD⁺.
- Produced: 2 pyruvate (various downstream fates), 4 ATP (gross; used for
  energy-requiring cellular processes), 2 NADH (must be reoxidized to NAD⁺ for
  glycolysis to continue). The 2 NADH provide the energy for ATP synthesis by
  respiration-linked (oxidative) phosphorylation, once reoxidized aerobically.

**Fates of pyruvate:**
- **Aerobic:** oxidative reactions of the citric acid cycle; oxidative
  phosphorylation.
- **Anaerobic:** reduction to lactate; reduction to ethanol.
- Pyruvate can also provide the carbon skeleton for alanine synthesis or for
  fatty acid synthesis.

### 2.7 Fermentation {#ch02-7}

**Fermentation** — pyruvate is reduced to other products, generating ATP
without consuming oxygen or NAD⁺ (i.e., it regenerates the NAD⁺ that glycolysis
itself consumes, so glycolysis can continue anaerobically). Used industrially in
producing foods and beverages such as yogurt and soy sauce.

- **Lactic acid fermentation** — pyruvate accepts electrons from NADH and is
  reduced to lactate (catalyzed by lactate dehydrogenase), regenerating NAD⁺.
  ΔG′° = −25.1 kJ/mol. Reversible.
  - Animals undergo lactic acid fermentation this way: organisms regenerate
    NAD⁺ by transferring electrons from NADH to pyruvate, forming lactate.
    During strenuous exercise, lactate builds up in muscle within under a
    minute; the resulting acidification limits continued strenuous work.
  - **Lactate recycling** — acidification from lactic acid ionization in
    muscle and blood limits the period of vigorous activity (e.g., sprinting).
    Lactate is carried in the blood to the liver, where it is converted back
    to glucose during recovery.
- **Ethanol (alcohol) fermentation** — pyruvate is further catabolized to
  ethanol, via two steps, each requiring its own cofactors:
  1. **Pyruvate decarboxylase** (cofactors Mg²⁺ and thiamine pyrophosphate,
     TPP) — pyruvate → acetaldehyde + CO₂. **Humans do not have pyruvate
     decarboxylase.** The CO₂ released here is what makes dough rise during
     bread baking.
  2. **Alcohol dehydrogenase** (cofactors Zn²⁺ and NAD⁺) — acetaldehyde + NADH
     + H⁺ → ethanol + NAD⁺.
  - Carried out by yeast and other microorganisms as a way to regenerate NAD⁺.

### 2.8 The Warburg effect (Dr. Suheir only) {#ch02-8}

**Warburg effect** — an altered cancer-cell metabolism: increased glucose
uptake and fermentation of glucose to lactate (**aerobic glycolysis**) even in
the presence of fully functioning mitochondria and oxygen. Cancer cells rewire
their metabolism to promote growth, survival, proliferation, and long-term
maintenance. Proposed explanations on the slide (given as a hypothesis, not
established fact — preserved as presented):
1. **Timewise** — glucose uptake is 10–100× greater than normal, generating
   ATP faster overall despite fermentation's lower ATP yield per glucose (a
   faster process).
2. **Increased glucose uptake** diverts flux into the pentose phosphate
   pathway, generating NADPH and ribose sugars needed for RNA/DNA synthesis
   during cell proliferation.
3. **Proton production** — one H⁺ is produced per lactate, increasing the
   acidity (lowering pH) of the tumor microenvironment, which increases tumor
   invasiveness.
4. Lactate's entry into other pathways produces metabolic intermediates that
   affect cell signaling in favor of tumor cell proliferation (decreasing
   apoptosis).

---

## Ch. 3 — Pyruvate Dehydrogenase and the Citric Acid Cycle {#ch03}

> **Source:** Dr. Osama Essawi, "Ch3 - The citric acid cycle and PDH" (33
> slides); Dr. Suheir Ereqat, "4) PDH and TCA cycle" (26 slides).

### 3.1 Cellular respiration — overview {#ch03-1}

**Cellular respiration** is the process by which the pyruvate produced by
glycolysis is further oxidized to H₂O and CO₂. Used by animals, plants, and
many microorganisms; provides far more energy (ATP) from glucose than
glycolysis alone, and also captures the energy stored in lipids and amino
acids (all three fuel classes — amino acids, fatty acids, glucose — converge on
acetyl-CoA production).

Occurs in three major stages:
1. **Acetyl-CoA production** — oxidation of fuels to acetyl-CoA; generates ATP,
   NADH, FADH₂. Glycolysis itself occurs in the cytoplasm.
2. **Acetyl-CoA oxidation** — oxidation of acetyl groups to CO₂ in the citric
   acid cycle (tricarboxylic acid/TCA cycle, Krebs cycle); generates NADH,
   FADH₂, and one GTP. Occurs in the mitochondrial matrix.
3. **Electron transfer and oxidative phosphorylation** — generates the vast
   majority of ATP from catabolism. Occurs at the mitochondrial inner
   membrane.

### 3.2 Pyruvate dehydrogenase (PDH) complex {#ch03-2}

**Oxidative decarboxylation of pyruvate** to acetyl-CoA is an irreversible
oxidation in which the carboxyl group is removed as CO₂; catalyzed by the
**pyruvate dehydrogenase complex**, in the mitochondria. Requires five
cofactors, four of which derive from vitamins.

**Three enzymes** (multiple copies each):
- **E1 — pyruvate dehydrogenase**
- **E2 — dihydrolipoyl transacetylase**
- **E3 — dihydrolipoyl dehydrogenase**

**Five coenzymes/prosthetic groups:**
- **Lipoate (lipoic acid)**
- **Thiamine pyrophosphate (TPP)** — from vitamin B1
- **FAD** — from vitamin B2
- **NAD** — from vitamin B3
- **Coenzyme A (CoA-SH)** — from vitamin B5 (pantothenic acid)

**Mechanism, 5 steps** (illustrated on a circular 5-enzyme-complex diagram):
1. Pyruvate reacts with TPP bound to E1, decarboxylating (losing CO₂) to form
   the hydroxyethyl-TPP derivative.
2. E1 transfers two electrons and the acetyl group from TPP to the oxidized
   lipoyllysyl group of E2, forming a thioester (acetyl group linked via S) —
   the reduced/acetylated lipoyl form.
3. **Transesterification**: the -SH of CoA replaces the -SH of E2's lipoyl
   arm, releasing **acetyl-CoA** (product 1) and leaving the fully reduced
   (dithiol) lipoyl group on E2.
4. E3 transfers two hydrogen atoms from the reduced lipoyl groups of E2 to its
   own FAD prosthetic group, regenerating the oxidized lipoyllysyl form of E2.
5. The resulting FADH₂ on E3 transfers a hydride to NAD⁺, forming **NADH**
   (product 2) and regenerating oxidized FAD — the complex is ready for
   another cycle.

### 3.3 Regulation of the PDH complex {#ch03-3}

Regulated by a combination of **covalent modification** and **allosteric**
mechanisms.

**Allosteric:**
- Inhibited by ATP, acetyl-CoA, and NADH (high energy state).
- Activated by AMP, CoA, and NAD⁺ (which accumulate when acetyl flow into the
  TCA cycle is insufficient).
- High ATP and NADH (sufficient energy production) inhibit PDH, slowing
  pyruvate decarboxylation; elevated ADP and Ca²⁺ activate it, promoting
  pyruvate → acetyl-CoA conversion when more energy is needed.
- **Product/feedback inhibition specifically**: NADH competes with NAD⁺ for
  binding at E3; acetyl-CoA competes with CoA-SH for binding at E2.

**Covalent modification** (phosphorylation cycle):
- **PDH kinase** phosphorylates and *inactivates* PDH (using ATP → ADP).
  Inactivation is promoted by high ratios of acetyl-CoA:CoA-SH, NADH:NAD⁺, and
  ATP:ADP.
- **PDH phosphatase** dephosphorylates and *reactivates* PDH (using H₂O → Pi),
  a reaction promoted/signalled by Ca²⁺ — activation is promoted by any sudden
  cellular demand, signalled by Ca²⁺.

**During starvation:** PDH kinase increases in most tissues (including
skeletal muscle) via increased gene transcription, while PDH phosphatase
decreases. The resulting PDH inhibition prevents muscle and other tissues from
catabolizing glucose and gluconeogenesis precursors — metabolism shifts toward
fat utilization, muscle protein breakdown increases (to supply gluconeogenesis
precursors), and the glucose that remains is spared for the brain.

### 3.4 PDH deficiency and thiamine deficiency (clinical) {#ch03-4}

**Pyruvate dehydrogenase deficiency** — a rare genetic mitochondrial disorder
from mutations in genes encoding PDH complex components, causing a
dysfunctional enzyme. Most commonly linked to the α subunit of E1 (X-linked),
though autosomal recessive variants also exist. Causes elevated serum lactate,
pyruvate, and alanine (**lactic acidosis**); associated with developmental and
neurological/neuromuscular defects, generally resulting in death (usually
during childhood, per Dr. Osama's slides).

**Treatment:**
- **Ketogenic diet** — high-fat, adequate-protein, low-carbohydrate; mimics
  starvation, forcing the body to burn fat rather than carbohydrate, which
  mitigates the metabolic challenges of PDH deficiency.
- **Dichloroacetic acid (DCA)** — investigated for the associated lactic
  acidosis. Stimulates PDH activity by *inhibiting PDH kinase*, shifting
  pyruvate metabolism from glycolysis toward mitochondrial oxidation and
  reducing lactate production.

**Thiamine (vitamin B1) deficiency → Beriberi** — thiamine is an essential
dietary requirement for most vertebrates, who neither synthesize nor store it
in significant amounts. TPP is a crucial PDH coenzyme in glucose metabolism.
Deficiency causes **Beriberi**, a fatal disease with neurological
disturbances, paralysis, limb atrophy, and cardiac failure. Dr. Suheir's
slides add the mechanistic link: the **brain exclusively uses aerobic glucose
catabolism** for energy and PDC is critical for that aerobic catabolism —
hence thiamine deficiency causes severe neurological symptoms specifically.
Beriberi is rare in developed countries (vitamin-enriched foods) but more
prevalent in people who abuse alcohol, since excess alcohol impairs thiamine
absorption/storage and leads to poor nutrition generally.

### 3.5 The citric acid cycle — overview and the 8 reactions {#ch03-5}

Per cycle turn: one acetyl group enters as acetyl-CoA, two molecules of CO₂
are released, one molecule of oxaloacetate is used to form citrate and one is
regenerated (no net removal of oxaloacetate — theoretically, one oxaloacetate
molecule could support oxidation of an infinite number of acetyl groups, and
in fact oxaloacetate is present in cells at very low concentration). Four of
the eight steps are oxidations, conserving energy as NADH and FADH₂, which
then donate electrons to the respiratory chain to drive ATP synthesis.

1. **Citrate synthase** — condenses acetyl-CoA with oxaloacetate to form
   citrate, via a transient citroyl-CoA intermediate. A large negative ΔG′° is
   needed because [oxaloacetate] is normally very low. **Induced fit**:
   the free enzyme (open conformation) has no acetyl-CoA binding site; binding
   of oxaloacetate causes a conformational change (closed conformation) that
   creates the acetyl-CoA binding site — this decreases the likelihood of
   premature hydrolysis of acetyl-CoA's thioester bond. (Dr. Suheir's slides
   describe this the same way: binding of OAA → conformational change →
   facilitates acetyl-CoA binding → further conformational change → product
   formation.)
2. **Aconitase** (aconitate hydratase) — reversible isomerization of citrate to
   isocitrate via the intermediate **cis-aconitate**. Water addition to
   cis-aconitate is stereospecific. Low [isocitrate] pulls the reaction
   forward. Bound to the inner mitochondrial membrane (per the labeled cycle
   diagram, "Bound to IMM" is actually annotated near succinate
   dehydrogenase — see reaction 6 below).
3. **Isocitrate dehydrogenase** — oxidative decarboxylation of isocitrate to
   α-ketoglutarate + CO₂. Mn²⁺ interacts with the carbonyl group of the
   transient oxalosuccinate intermediate, stabilizing the enol form. Specific
   isozymes exist for NADP⁺ (cytosolic and mitochondrial) or NAD⁺
   (mitochondrial only).
4. **α-Ketoglutarate dehydrogenase complex** — oxidative decarboxylation of
   α-ketoglutarate to succinyl-CoA + CO₂; energy of oxidation is conserved in
   succinyl-CoA's thioester bond.
5. **Succinyl-CoA synthetase** (succinate thiokinase) — breaks the thioester
   bond of succinyl-CoA to form succinate; the energy released drives
   synthesis of a phosphoanhydride bond in GTP or ATP (**substrate-level
   phosphorylation**).
6. **Succinate dehydrogenase** — a flavoprotein catalyzing the reversible
   oxidation of succinate to fumarate. An integral protein of the inner
   mitochondrial membrane (**bound to IMM**) in eukaryotes, containing three
   iron–sulfur clusters and a covalently bound FAD. **Competitively inhibited
   by malonate** — malonate's structure (a 3-carbon dicarboxylic acid) closely
   resembles succinate's (4-carbon dicarboxylic acid), which is why it
   competes at the active site.
7. **Fumarase** — reversible hydration of fumarate to L-malate; transition
   state is a carbanion. **Stereospecific**: does not act on maleate (the
   *cis* geometric isomer of fumarate) or on D-malate — only the *trans*
   (fumarate) and L- forms are substrates.
8. **Malate dehydrogenase** — oxidizes L-malate to oxaloacetate, coupled to
   NAD⁺ reduction. Low [oxaloacetate] pulls the reaction forward, regenerating
   oxaloacetate for the next turn's citrate synthesis.

**Narrative summary:** acetyl-CoA donates its acetyl group to oxaloacetate,
forming citrate (6 carbons). Citrate → isocitrate (6 carbons); dehydrogenation
with loss of CO₂ gives α-ketoglutarate (5 carbons). α-Ketoglutarate loses a
second CO₂, ultimately yielding succinate (4 carbons). Succinate is converted
in three enzymatic steps back to oxaloacetate (4 carbons), completing the
cycle.

**Net result of one turn:**
Acetyl-CoA + 3 NAD⁺ + FAD + GDP + Pi + 2 H₂O →
2 CO₂ + 3 NADH + FADH₂ + GTP + CoA + 3 H⁺

Net oxidation of two carbons to CO₂; energy conserved as 3 NADH + 1 FADH₂ + 1
GTP (convertible to ATP). Note (Dr. Suheir's slides): although the two carbons
that *enter* the cycle become part of oxaloacetate, they are not the same two
carbons released as CO₂ in that same turn — those two carbons are actually
released as CO₂ only in the *third* subsequent turn of the cycle, even though
the energy accounting above is for "one turn."

### 3.6 The TCA cycle in anabolism, and anaplerotic reactions {#ch03-6}

The citric acid cycle is **amphibolic** — it serves both catabolic and
anabolic processes in aerobic organisms:
- Oxaloacetate and α-ketoglutarate are precursors for aspartate and glutamate
  (via simple transamination).
- Succinyl-CoA is required for synthesizing the porphyrin ring of heme groups.
- Oxaloacetate can be converted to glucose via gluconeogenesis.

**Anaplerotic reactions** — when TCA intermediates are diverted into these
biosynthetic pathways (amino acids, fatty acids, glucose), they must be
replenished ("filled up") for the cycle and central metabolism to continue.

> **Table 16-2, Anaplerotic Reactions** (per Dr. Suheir's slides):
>
> | Reaction | Enzyme | Tissue(s)/organism(s) |
> |---|---|---|
> | Pyruvate + HCO₃⁻ + ATP ⇌ oxaloacetate + ADP + Pi | Pyruvate carboxylase | Liver, kidney, and nervous tissues |
> | PEP + CO₂ + GDP ⇌ oxaloacetate + GTP | PEP carboxykinase | Heart, skeletal muscle |
> | PEP + HCO₃⁻ ⇌ oxaloacetate + Pi | PEP carboxylase | Higher plants, yeast, bacteria (not mammalian) |
> | Pyruvate + HCO₃⁻ + NAD(P)H ⇌ malate + NAD(P)⁺ | Malic enzyme | Widely distributed in eukaryotes and prokaryotes |

Dr. Osama's slides single out the **pyruvate carboxylase** reaction (reversible
carboxylation of pyruvate to oxaloacetate) as the most important anaplerotic
reaction in mammalian **liver, kidney, and brown adipose tissue**; Dr. Suheir's
table (above) extends its tissue list to include nervous tissue as well.

### 3.7 Regulation of the TCA cycle {#ch03-7}

Regulation balances the supply of key intermediates against the demands of
energy production and biosynthesis. Occurs at strongly exergonic
(rate-controlling) steps; fluxes are also affected by substrate/product
concentrations.

| Regulatory enzyme | Activated by | Inhibited by |
|---|---|---|
| Citrate synthase | ADP | ↑NADH/NAD⁺, ATP, succinyl-CoA, long-chain fatty acids, citrate |
| Isocitrate dehydrogenase | ↓ATP/ADP, Ca²⁺ | ↑NADH/NAD⁺, ↑ATP/ADP |
| α-ketoglutarate dehydrogenase | Ca²⁺ | ↑NADH/NAD⁺, ↑ATP/ADP, GTP, succinyl-CoA |

**Summary of PDH → TCA metabolite-flow regulation** (Dr. Suheir's slides):
- The PDH complex is allosterically inhibited when [ATP]/[ADP], [NADH]/[NAD⁺],
  and [acetyl-CoA]/[CoA] ratios are high — an energy-sufficient state.
- TCA cycle flow can be limited by availability of citrate synthase's own
  substrates (oxaloacetate, acetyl-CoA), or by NAD⁺ availability (depleted as
  it's converted to NADH), which slows the three NAD-dependent oxidation
  steps.
- Feedback inhibition by succinyl-CoA, citrate, and ATP also slows the cycle
  by inhibiting early steps.
- In muscle tissue, Ca²⁺ signals contraction and also stimulates
  energy-yielding metabolism, replacing the ATP consumed by that contraction.

---

## Ch. 4 — Oxidative Phosphorylation and the Electron Transport Chain {#ch04}

> **Source:** Dr. Osama Essawi, "Ch 4 Oxidative phosphorylation" (27 slides);
> Dr. Suheir Ereqat, "5) electron transport chain" (32 slides).

### 4.1 Overview {#ch04-1}

Carbohydrates, lipids, and amino acids are the cell's main reduced fuels.
Electrons from these reduced fuels are transferred to the reduced cofactors
NADH or FADH₂. **Oxidative phosphorylation** occurs in mitochondria, where the
energy from NADH and FADH₂ is used to make ATP.

Biological oxidations are catalyzed by intracellular enzymes, with the purpose
of obtaining energy. **Electron transport**: electrons carried by NADH or
FADH₂ pass sequentially through a chain of proteins and coenzymes (the
electron transport chain) to O₂. **Oxidative phosphorylation** = coupling of
electron transport (oxidation) with ATP synthesis (phosphorylation). All of
this happens at the inner mitochondrial membrane (in eukaryotic cells).

Cellular respiration, viewed as a series of reactions, consists of oxidations
(loss of electrons) that are also dehydrogenations (loss of a hydrogen atom =
1 electron + 1 proton, H = H⁺ + e⁻). Electrons carry energy from one molecule
to another and are shuttled through electron carriers to a final acceptor — in
aerobic respiration, that final acceptor is O₂. NAD⁺ is one such electron
carrier: it accepts electrons + 1 proton to become NADH, reversibly.

### 4.2 Mitochondrial structure {#ch04-2}

- **Outer membrane** — relatively porous; allows passage of metabolites.
- **Inner membrane** — relatively impermeable, with a proton gradient across
  it; location of the electron transport chain complexes; its convolutions
  (**cristae**) increase surface area.
- **Intermembrane space (IMS)** — similar environment to the cytosol; higher
  proton concentration (lower pH). Called the **P-side** (positive side, where
  protons accumulate).
- **Matrix** — location of the citric acid cycle and parts of lipid/amino acid
  metabolism; lower proton concentration (higher pH). Called the **N-side**
  (negative side).

### 4.3 Electron carriers of the respiratory chain {#ch04-3}

Oxidative phosphorylation begins with electrons entering the respiratory
chain. Three types of electron transfer occur: direct electron transfer;
transfer as a hydrogen atom (H⁺ + e⁻); transfer as a hydride ion (:H⁻, which
carries two electrons).

**Five types of electron-carrying molecules** in the chain:
1. **Nicotinamide nucleotides (NAD⁺/NADP⁺)** — dehydrogenases funnel electrons
   from catabolic pathways into these universal acceptors, via the general
   reversible reaction: reduced substrate + NAD⁺ ⇌ oxidized substrate + NADH +
   H⁺. Two hydrogens are removed from the substrate: one transferred as a
   hydride to NAD(P)⁺, one released as H⁺ into the medium.
2. **Flavin nucleotides (FMN or FAD) / flavoproteins** — the oxidized flavin
   can accept either one electron (yielding the semiquinone form) or two
   electrons (yielding FADH₂ or FMNH₂).
3. **Ubiquinone (coenzyme Q, or Q)** — a lipid-soluble benzoquinone with a long
   isoprenoid side chain. Accepts one or two electrons; freely diffusible
   within the inner mitochondrial membrane; central to coupling electron flow
   to proton movement. Its 2-electron reduction proceeds via a 1-electron
   **semiquinone radical** intermediate: Q (fully oxidized) → •QH (semiquinone
   radical) → QH₂ (ubiquinol, fully reduced) — each of the two steps adds one
   H⁺ + one e⁻.
4. **Cytochromes** — proteins with strong visible-light absorption from their
   iron-containing heme prosthetic groups; one-electron carriers. Three
   mitochondrial classes — **a, b, c** — differing by ring substituents.
5. **Iron–sulfur proteins** — contain equal numbers of iron and sulfur atoms,
   coordinated by cysteine residues; one-electron carriers.

**Standard reduction potentials** (Table 19-2, Dr. Osama's slides), listing
E′° for the respiratory chain's own half-reactions in the order electrons flow
(most negative/reducing to most positive/oxidizing):

| Redox half-reaction | E′° (V) |
|---|---|
| 2H⁺ + 2e⁻ → H₂ | −0.414 |
| NAD⁺ + H⁺ + 2e⁻ → NADH | −0.320 |
| NADP⁺ + H⁺ + 2e⁻ → NADPH | −0.324 |
| NADH dehydrogenase (FMN) + 2H⁺ + 2e⁻ → NADH dehydrogenase (FMNH₂) | −0.30 |
| Ubiquinone + 2H⁺ + 2e⁻ → ubiquinol | 0.045 |
| Cytochrome b (Fe³⁺) + e⁻ → cytochrome b (Fe²⁺) | 0.077 |
| Cytochrome c₁ (Fe³⁺) + e⁻ → cytochrome c₁ (Fe²⁺) | 0.22 |
| Cytochrome c (Fe³⁺) + e⁻ → cytochrome c (Fe²⁺) | 0.254 |
| Cytochrome a (Fe³⁺) + e⁻ → cytochrome a (Fe²⁺) | 0.29 |
| Cytochrome a₃ (Fe³⁺) + e⁻ → cytochrome a₃ (Fe²⁺) | 0.35 |
| ½ O₂ + 2H⁺ + 2e⁻ → H₂O | 0.817 |

### 4.4 The four respiratory complexes {#ch04-4}

Four unique electron-carrier complexes, embedded in the inner mitochondrial
membrane, catalyze electron transfer through the chain; a lipid-soluble
coenzyme (Q) and a water-soluble protein (cytochrome c) shuttle electrons
between them. (Complex V is ATP synthase — §4.6.)

> **Table 19-3, Protein Components of the Mitochondrial Electron-Transfer
> Chain** (Dr. Suheir's slides):
>
> | Complex | Enzyme complex/protein | Mass (kDa) | Subunits (bacterial equivalent) | Prosthetic group(s) |
> |---|---|---|---|---|
> | I | NADH dehydrogenase | 850 | 43 (14) | FMN, Fe–S |
> | II | Succinate dehydrogenase | 140 | 4 | FAD, Fe–S |
> | III | Ubiquinone:cytochrome c oxidoreductase | 250 | 11 | Hemes, Fe–S |
> | — | Cytochrome c† | 13 | 1 | Heme |
> | IV | Cytochrome oxidase | 160 | 13 (3–4) | Hemes; Cu_A, Cu_B |
>
> †Cytochrome c is not part of an enzyme complex — it moves as a freely
> soluble protein between Complexes III and IV.

1. **Complex I** (NADH:ubiquinone oxidoreductase / NADH dehydrogenase; also
   called NADH-UQ oxidoreductase) — from NADH to ubiquinone. A large L-shaped
   enzyme with >40 polypeptide chains. Its FMN-containing flavoprotein accepts
   2 electrons from NADH; several Fe–S centers then pass electrons on to
   ubiquinone. Catalyzes the exergonic hydride transfer from NADH (plus a
   matrix proton) to Q: **NADH + H⁺ + Q → NAD⁺ + QH₂**, coupled to the
   endergonic pumping of **4 protons** from the matrix to the intermembrane
   space — Complex I is a proton pump driven by electron-transfer energy.

2. **Complex II** (succinate dehydrogenase; succinate-ubiquinone
   oxidoreductase) — from succinate to ubiquinone. Smaller/simpler than
   Complex I. This single enzyme has **dual roles**: converts succinate to
   fumarate in the citric acid cycle, *and* captures/donates electrons in the
   ETC. Electrons pass from FAD → Fe–S centers → Q. **No proton pumping.**

3. **Complex III** (cytochrome bc₁ complex; ubiquinone:cytochrome c
   oxidoreductase) — from ubiquinone to cytochrome c. Couples electron
   transfer from ubiquinol to cytochrome c with vectorial proton transport
   from matrix to intermembrane space. Uses two electrons from QH₂ to reduce
   two molecules of cytochrome c. Clearance of electrons from reduced
   quinones via the **Q-cycle** translocates **4 additional protons** to the
   intermembrane space. Contains cytochrome b, cytochrome c₁, and the Rieske
   iron–sulfur protein.

4. **Complex IV** (cytochrome oxidase; cytochrome c oxidase) — from
   cytochrome c to O₂, reducing O₂ to H₂O. Mammalian cytochrome oxidase is a
   13-subunit membrane protein containing two heme groups (a and a₃) and two
   Cu ions. Four electrons reduce one O₂ molecule to two H₂O; four protons are
   picked up from the matrix in this process, and **4 additional protons**
   are pumped from the matrix to the intermembrane space. Overall reaction: 2
   H⁺ + 2 e⁻ + ½ O₂ → H₂O. Cytochrome oxidase is the enzyme that interacts
   directly with oxygen — any chemical interfering with electron/proton
   exchange between cytochrome oxidase and oxygen halts the entire ETC and
   stops respiration (see cyanide, §4.7).

**Overall proton accounting:** for each pair of electrons transferred to O₂
via NADH, **10 protons are pumped out** (4 + 4 + 2, from Complexes I, III, and
IV respectively). Since Complex II does not pump protons, electrons entering
via FADH₂/succinate (bypassing Complex I) are pumped out at only **6 protons**
per pair (via Complexes III and IV only).

### 4.5 Chemiosmotic model {#ch04-5}

Electron transport sets up a **proton-motive force (PMF)** — the ETC acts as
an H⁺ pump, pulling protons into the intermembrane space; some electron
energy is lost with each transfer step, and that energy is used to pump
protons across the membrane from matrix to intermembrane space. This
electrochemical proton gradient's energy is the **chemiosmotic potential**
(= PMF). De-energized electrons combine with H⁺ and O₂ to form water in the
matrix (catalyzed by cytochrome oxidase). The energy of the proton-motive
force drives ATP synthesis.

### 4.6 ATP synthase {#ch04-6}

The higher negative charge in the matrix attracts protons back from the
intermembrane space into the matrix; most protons return to the matrix
*through ATP synthase*. **ATP synthase** is a membrane-bound **F-type ATPase**
with two functional units: **F₀** (contains the proton channel/shaft/stator)
and **F₁** (site of ATP synthesis, on its β subunit) — described by the
**binding-change model**.

- The number of protons pumped out per electron pair is **10 for NADH** and
  **6 for succinate/FADH₂**.
- The number of protons needed to drive synthesis of one ATP molecule is **4**.
- Net: **NADH → ~2.5 ATP**; **FADH₂ → ~1.5 ATP**.
- Theoretical energy yields: earlier estimates of 36 ATP/glucose have been
  revised downward — the currently accepted figure is **30–32 ATP per
  glucose** (Dr. Suheir's slides explicitly flag this as "new calculation").

### 4.7 Inhibitors and uncouplers of oxidative phosphorylation {#ch04-7}

Electron transport and ATP synthesis are tightly coupled (each direction):
inhibitors of electron transfer block ATP synthesis, and inhibitors of ATP
synthesis likewise block electron transfer.

> **Table 19-4, Agents That Interfere with Oxidative Phosphorylation** (both
> lecturers' slides carry this table; Dr. Osama's version labels the same
> brown-adipose-tissue proton-pore protein "Uncoupling protein 1" where Dr.
> Suheir's labels it "Thermogenin" — both names for the same protein,
> preserved as each deck states it):
>
> | Type of interference | Compound(s) | Target/mode of action |
> |---|---|---|
> | Inhibition of electron transfer | Cyanide, carbon monoxide | Inhibit cytochrome oxidase |
> | | Antimycin A | Blocks electron transfer from cytochrome b to cytochrome c₁ |
> | | Myxothiazol, Rotenone, Amytal, Piericidin A | Prevent electron transfer from Fe–S center to ubiquinone |
> | Inhibition of ATP synthase | Aurovertin | Inhibits F₁ |
> | | Oligomycin, Venturicidin | Inhibit F₀ (and CF₀) |
> | | DCCD | Blocks proton flow through F₀ (and CF₀) |
> | Uncoupling of phosphorylation from electron transfer | FCCP, DNP (2,4-dinitrophenol) | Hydrophobic proton carriers |
> | | Valinomycin | K⁺ ionophore |
> | | Thermogenin / Uncoupling protein 1 | In brown adipose tissue, forms proton-conducting pores in the inner mitochondrial membrane |
> | Inhibition of ATP-ADP exchange | Atractyloside | Inhibits adenine nucleotide translocase |

**Cyanide**, specifically: blocks electron transfer between cytochrome oxidase
(Complex IV) and O₂, inhibiting both respiration and ATP synthesis — this is
the mechanistic basis for cyanide poisoning.

**DNP (2,4-dinitrophenol)**, structurally, is a phenol that can reversibly
lose/gain a proton (phenol ⇌ phenolate + H⁺); after entering the mitochondrial
matrix in its protonated form, it releases a proton, dissipating the proton
gradient — the general mechanism by which the "hydrophobic proton carrier"
class of uncouplers works.

### 4.8 Transport across the inner mitochondrial membrane {#ch04-8}

- **Adenine nucleotide translocase** — an antiporter that moves ADP into the
  matrix and ATP out.
- **Phosphate translocase** — promotes symport of one H₂PO₄⁻ and one H⁺ into
  the matrix.
- **ATP synthasome** — the complex of ATP synthase together with both of the
  above translocases.

### 4.9 Shuttle systems for cytosolic NADH {#ch04-9}

The NADH dehydrogenase of the inner mitochondrial membrane accepts electrons
only from NADH *in the matrix* — but the inner membrane is not permeable to
NADH itself. Problem: cytosolic NADH (e.g., from glycolysis) cannot cross
directly, so how is it reoxidized via the respiratory chain? Solution:
dedicated **shuttle systems** carry reducing equivalents from cytosolic NADH
into the mitochondrion by an indirect route.

- **Malate–aspartate shuttle** — the most active NADH shuttle; operates in
  **liver, kidney, and heart** mitochondria. Cytosolic NADH oxidized via this
  shuttle contributes its electrons to **Complex I**, yielding **~2.5 ATP**
  per NADH (same yield as matrix NADH, since it still enters at Complex I).
  Diagram elements named on the slides: aspartate aminotransferase (AST) acts
  on both sides of the shuttle, interconverting keto acid/amino acid pairs
  as part of the cycle.
- **Glycerol 3-phosphate shuttle** — the alternative shuttle, used in
  **skeletal muscle and brain**. NADH equivalents are moved in by a reaction
  catalyzed by cytosolic glycerol 3-phosphate dehydrogenase together with a
  second isozyme bound to the outer face of the inner membrane; unlike the
  malate–aspartate shuttle, this one does **not** involve a membrane
  transport system. Because it hands electrons to **Complex III** (bypassing
  Complex I), it yields only **~1.5 ATP** per cytosolic NADH.

### 4.10 ATP yield from complete glucose oxidation {#ch04-10}

Complete oxidation of one glucose molecule to CO₂ yields **30 or 32 ATP**
(the exact number depends on which shuttle ferries cytosolic NADH — see
§4.9). By contrast, anaerobic glycolysis (lactate fermentation) yields only
**2 ATP per glucose**. Oxidative phosphorylation therefore produces the large
majority of ATP made in aerobic cells.

> **Table 19-5, ATP Yield from Complete Oxidation of Glucose** (Dr. Suheir's
> slides):
>
> | Process | Direct product | Final ATP |
> |---|---|---|
> | Glycolysis | 2 NADH (cytosolic) | 3 or 5* |
> | | 2 ATP | 2 |
> | Pyruvate oxidation (2 per glucose) | 2 NADH (mitochondrial matrix) | 5 |
> | Acetyl-CoA oxidation in citric acid cycle (2 per glucose) | 6 NADH (mitochondrial matrix) | 15 |
> | | 2 FADH₂ | 3 |
> | | 2 ATP or 2 GTP | 2 |
> | **Total yield per glucose** | | **30 or 32** |
>
> *The cytosolic-NADH number depends on which shuttle system transfers the
> reducing equivalents into the mitochondrion (glycerol-3-phosphate shuttle →
> 3; malate–aspartate shuttle → 5, consistent with §4.9's per-NADH figures).

### 4.11 Regulation of ATP-producing pathways {#ch04-11}

The rate of mitochondrial respiration (O₂ consumption) is tightly regulated,
generally limited by the availability of **ADP, Pi, and O₂**. All four
ATP-producing pathways — glycolysis, pyruvate oxidation, the citric acid
cycle, and oxidative phosphorylation — are coordinately accelerated whenever
ATP use increases and ADP, AMP, and Pi accumulate as a result. A summary
diagram on the slides traces this activation/inhibition pattern down the
whole sequence:

- **Glycolysis** control points: hexokinase (activated by Pi; inhibited by its
  own product, glucose 6-phosphate); phosphofructokinase-1 (activated by AMP;
  inhibited by ATP and citrate); pyruvate kinase (activated by ADP; inhibited
  by ATP and NADH).
- **PDH complex**: activated by AMP, ADP, NAD⁺; inhibited by ATP, NADH.
- **Citrate synthase**: activated by ADP; inhibited by ATP, NADH.
- **Isocitrate dehydrogenase**: activated by ADP; inhibited by ATP.
- **α-Ketoglutarate dehydrogenase**: activated by AMP, ADP, NAD⁺; inhibited by
  ATP, NADH — driving succinyl-CoA → oxaloacetate onward to the respiratory
  chain, which itself is activated by ADP + Pi (its direct substrates) and
  proceeds NADH/NAD⁺ ⇌ ½ O₂/H₂O, ADP + Pi → ATP.

---

## Ch. 5 — Feeder Pathways and the Pentose Phosphate Pathway {#ch05}

> **Source:** Dr. Osama Essawi, "ch5 - Feeder Pathway and PPP" (labelled
> "14.2 Feeder pathways for glycolysis & 14.6 Pentose phosphate pathway", 27
> slides); Dr. Suheir Ereqat, "6) pentose-p-shunt / feeder pathway" (35
> slides).

### 5.1 Feeder pathways for glycolysis — overview {#ch05-1}

Many carbohydrates besides glucose meet their catabolic fate in glycolysis,
after being transformed into one of the glycolytic intermediates. The most
significant: the storage polysaccharides **glycogen and starch** (endogenous
or dietary); the disaccharides **maltose, lactose, and sucrose**; and the
monosaccharides **fructose, mannose, and galactose**.

**Disaccharidase reactions** (hydrolysis, each with its own enzyme):
- Dextrin + n H2O --(dextrinase)--> n D-glucose
- Maltose + H2O --(maltase)--> 2 D-glucose
- Lactose + H2O --(lactase)--> D-galactose + D-glucose
- Sucrose + H2O --(sucrase)--> D-fructose + D-glucose
- Trehalose + H2O --(trehalase)--> 2 D-glucose

**Dietary polysaccharides**: **alpha-amylase** (salivary and small-intestinal)
hydrolyzes the internal alpha(1→4) glycosidic linkages of starch and glycogen,
producing di- and trisaccharides. Pancreatic alpha-amylase yields mainly maltose,
maltotriose, and **limit dextrins** (branched fragments of amylopectin
containing alpha(1→6) branch points, removed separately by limit dextrinases).

**Glycogen/starch phosphorolysis** — glycogen (starch) phosphorylase removes a
glucose unit from the *nonreducing end* using inorganic phosphate (Pi), **not
water** — producing **glucose 1-phosphate** directly (plus a glycogen chain
shortened by one unit), rather than free glucose. Because this route skips the
hexokinase step (and its ATP cost) that hydrolysis-then-phosphorylation would
require, glycogen breakdown by phosphorolysis is more energy-efficient than
would be breakdown by hydrolysis followed by phosphorylation. (See also
Chapter 6, where this same phosphorylase reaction is covered as the entry step
of glycogenolysis.)

### 5.2 Individual sugar entry pathways {#ch05-2}

**Lactose and lactose intolerance** — **lactase** converts lactose to glucose
+ galactose; present in infants, often absent in adults. **Lactase
persistence** = the phenotype of continued lactase production into adulthood.
**Lactose intolerance** = inability to digest lactose from the disappearance
of lactase in adulthood — causes abdominal cramps and diarrhea. Mechanistically:
undigested lactose passes into the large intestine, where bacteria convert it
to toxic products causing the cramps/diarrhea; undigested lactose and its
metabolites also raise intestinal osmolarity, favoring water retention in the
gut.

**Galactose metabolism and galactosemia** — in the liver: (1) **galactokinase**
phosphorylates galactose at C-1 (using ATP) to galactose 1-phosphate; (2) a
**transferase** converts galactose 1-phosphate to **UDP-galactose**, formed
when galactose 1-phosphate displaces glucose 1-phosphate from UDP-glucose; (3)
**UDP-glucose 4-epimerase** epimerizes UDP-galactose at C-4 to UDP-glucose —
mechanistically, oxidation of C-4 by NAD+ followed by reduction of C-4 by
NADH, inverting that carbon's configuration. The regenerated UDP-glucose is
recycled through another round of the transferase reaction; net effect is
conversion of galactose 1-phosphate to glucose 1-phosphate, with **no net
production or consumption** of UDP-galactose or UDP-glucose overall.

Three genetic galactosemias, one per enzyme defect:
- **Galactokinase deficiency (GALK gene)** — high blood/urine galactose;
  causes cataracts in infants.
- **Transferase deficiency (GALT gene)** — more serious: poor growth, speech
  abnormality, mental deficiency, and potentially fatal liver damage.
- **Epimerase deficiency (GALE gene)** — similar symptoms to transferase
  deficiency, but careful dietary control reduces their severity.

**Fructose and mannose entry:**
- **Muscle/kidney route**: hexokinase phosphorylates fructose (in the small
  intestine) — a major pathway of fructose entry into glycolysis in muscle and
  kidney.
- **Liver route**: **fructokinase** phosphorylates fructose at C-1 (not C-6).
  The resulting fructose 1-phosphate is cleaved by **fructose 1-phosphate
  aldolase (aldolase B)** into glyceraldehyde and dihydroxyacetone phosphate;
  glyceraldehyde is then phosphorylated (by ATP + **triose kinase**) to
  glyceraldehyde 3-phosphate. Both fructose-1-phosphate cleavage products thus
  enter glycolysis as glyceraldehyde 3-phosphate.
- **Mannose**: released during digestion of various dietary polysaccharides
  and glycoproteins; phosphorylated at C-6 by hexokinase to mannose
  6-phosphate, then converted by phosphohexose isomerase (phosphomannose
  isomerase) to fructose 6-phosphate, entering glycolysis directly.

**Hereditary Fructose Intolerance (HFI)** — autosomal recessive, caused by
**aldolase B** gene mutations (mapped to chromosome 9, locus 9q22.3; a
non-invasive DNA test is increasingly used for diagnosis). Affected
individuals develop a strong aversion to sweets/fruit; eating fructose causes
severe abdominal pain, vomiting, and hypoglycemia; infants may show growth
delays. Mechanistically: aldolase B deficiency lets **fructose 1-phosphate
accumulate** in liver and kidney cells, causing **phosphate depletion** and
gradual long-term organ damage; the phosphate depletion also worsens
hypoglycemia by impairing glycogen breakdown. Standard therapy: a
fructose-free diet.

### 5.3 The pentose phosphate pathway (PPP) — overview {#ch05-3}

Also called the **phosphogluconate pathway** or **hexose monophosphate
pathway**. Oxidizes glucose 6-phosphate to produce pentose phosphates and
NADPH — "a shunt" off of glycolysis. One fate of G6P (alongside glycolysis) is
this pathway; the relative concentrations of NADP+ and NADPH determine which
fate G6P takes (§5.6).

General scheme: **oxidative phase** (G6P → 6-phosphogluconate → ribulose
5-phosphate + CO2, generating 2 NADPH) feeds into either biosynthetic use of
ribose 5-phosphate, or — via the **nonoxidative phase** (using transketolase
and transaldolase) — recycling back to G6P to continue NADPH production.

Rapidly dividing cells use the ribose 5-phosphate product to make RNA, DNA,
and coenzymes.

### 5.4 Oxidative phase {#ch05-4}

1. **Glucose-6-phosphate dehydrogenase (G6PD)** oxidizes G6P to a delta-lactone,
   reducing NADP+ to NADPH.
2. **Lactonase** hydrolyzes the lactone (to 6-phosphogluconate).
3. **6-phosphogluconate dehydrogenase** further oxidizes and decarboxylates
   6-phosphogluconate, producing **ribulose 5-phosphate (Ru5P)** (+ CO2 + a
   second NADPH).
4. **Phosphopentose isomerase** (Mg2+-requiring, per the diagram) converts
   ribulose 5-phosphate to **ribose 5-phosphate**.

**Overall equation** (in tissues where the pathway stops here): Glucose
6-phosphate + 2 NADP+ + H2O → Ribose 5-phosphate + CO2 + 2 NADPH + 2 H+.

Net result: **NADPH** (a reductant for biosynthetic reactions) and **ribose
5-phosphate** (a nucleotide-synthesis precursor).

### 5.5 Nonoxidative phase {#ch05-5}

Used in tissues that need **more NADPH than ribose 5-phosphate** (e.g., liver
and adipose tissue) — the nonoxidative phase recycles pentose phosphates back
to glucose 6-phosphate, so oxidative-phase NADPH production can continue
(converting G6P, over repeated turns, to 6 CO2 overall).

1. **Ribulose 5-phosphate epimerase** epimerizes ribulose 5-phosphate to
   **xylulose 5-phosphate**.
2. **First transketolase reaction** — transketolase transfers a 2-carbon
   fragment from a ketose donor to an aldose acceptor: specifically, C-1 and
   C-2 of xylulose 5-phosphate are transferred to ribose 5-phosphate, forming
   the 7-carbon **sedoheptulose 7-phosphate** (and leaving a 3-carbon
   fragment, glyceraldehyde 3-phosphate, from the xylulose).
3. **Transaldolase reaction** — transaldolase condenses a 3-carbon fragment
   from sedoheptulose 7-phosphate with glyceraldehyde 3-phosphate, forming
   **fructose 6-phosphate** and the 4-carbon **erythrose 4-phosphate**.
4. **Second transketolase reaction** — forms fructose 6-phosphate and
   glyceraldehyde 3-phosphate from erythrose 4-phosphate and xylulose
   5-phosphate.

Net: six pentose phosphates (5-carbon) are converted, via these carbon-skeleton
rearrangements, into five hexose phosphates (6-carbon; as glucose
6-phosphate), completing the recycle. **Transketolase and transaldolase are
specific to this pathway**; the other enzymes involved (isomerase, epimerase)
also serve in glycolysis or gluconeogenesis. The fate of the resulting triose
phosphates is determined by the cell's relative needs for pentose phosphates,
NADPH, and ATP.

### 5.6 Regulation of the PPP {#ch05-6}

**Glucose-6-phosphate dehydrogenase (G6PD)** is the **rate-limiting,
rate-controlling** enzyme of the pathway — allosterically **stimulated by
NADP+**. The NADPH:NADP+ ratio is normally about **100:1 in liver cytosol**,
making the cytosol a highly reducing environment. When an NADPH-utilizing
pathway (e.g., a biosynthetic pathway) consumes NADPH and forms NADP+, the
rising NADP+ stimulates G6PD — i.e., PPP flux is feedback-driven by how fast
NADPH is being *used*, not simply by how much has accumulated. Conversely,
when NADPH is forming faster than it is consumed (by biosynthesis and
glutathione reduction), the resulting drop in NADP+ availability slows the
pathway, and G6P is instead used for glycolysis.

### 5.7 NADPH and glutathione — physiological roles {#ch05-7}

The **Pentose Phosphate Pathway is the major source of NADPH** used for:
- **Biosynthesis** of fatty acids (liver, adipose tissue, lactating mammary
  gland), cholesterol (liver, adrenal cortex, skin, gonads), and
  catecholamines (nervous system, adrenal medulla).
- **Preserving eye-lens transparency** — keeping crystallin (the eye lens
  protein) in its active, reduced state.
- **Preserving erythrocyte membrane integrity.**

**Glutathione (GSH)** — a tripeptide, existing in reduced (GSH) and oxidized
(GSSG, glutathione disulfide) forms, working with NADPH and other redox-active
compounds to regulate cellular redox status (NADPH reduces GSSG back to 2 GSH
via **glutathione reductase**). Protective functions of GSH:
- Serves as a reductant.
- Conjugates to drugs, making them water-soluble.
- Involved in amino acid transport across cell membranes.
- Acts as a cofactor in some enzymatic reactions, including rearrangement of
  protein disulfide bonds.

**Reactive oxygen species (ROS)** — highly reactive molecules generated as
natural byproducts of cellular metabolism, sourced (per Dr. Suheir's slides)
from the **peroxisome, mitochondria, cytochrome P450, and NOX (NADPH
oxidase)**. Include free radicals such as superoxide (O2 dot-minus) and hydroxyl
radical (OH dot), and non-radical molecules such as hydrogen peroxide (H2O2). In
actively respiring mitochondria, **1-4% of the O2 used forms oxygen radicals**
— more than enough to be lethal unless rapidly removed.

**Antioxidant defenses** — a complex system of antioxidant enzymes and
molecules regulates ROS levels:
- Enzymes: superoxide dismutase, glutathione peroxidase, glutathione
  reductase, catalase.
- Small molecules: ascorbic acid (vitamin C), tocopherol (vitamin E),
  carotenoids.

Reduced glutathione also keeps protein sulfhydryl groups in their reduced
state, preventing some of the deleterious effects of oxidative stress.

**NADPH/glutathione in red blood cells** — oxidation of G6P to ribulose
5-phosphate + CO2 is very active in mammalian RBCs; the NADPH produced keeps
intracellular glutathione reduced. Reduced glutathione helps prevent oxidation
of hemoglobin's iron from Fe(II) to Fe(III); Fe(III)-containing hemoglobin
cannot effectively bind O2.

### 5.8 Clinical correlations {#ch05-8}

**Glucose-6-phosphate dehydrogenase (G6PD) deficiency** — **favism**, a
condition triggered by fava bean ingestion, causes erythrocyte lysis
(hemolysis begins 24-48 hours after ingestion, per Dr. Suheir's slides),
releasing free hemoglobin into the blood; symptoms include jaundice and, in
severe cases, kidney failure. Similar symptoms can follow ingestion of
**primaquine** (an antimalarial), sulfa antibiotics, or exposure to certain
herbicides. G6PD deficiency has a genetic basis and affects about **400
million people worldwide**; most affected individuals are asymptomatic —
clinical manifestations require the combination of G6PD deficiency *and*
certain environmental triggers.

**Wernicke-Korsakoff syndrome** — caused by severe **thiamine (vitamin B1)**
deficiency; thiamine is a precursor of the cofactor TPP. Insufficient B1
intake typically causes abnormal eye movements, gait problems, and other
neurological defects. More common among people with alcoholism, since chronic
heavy alcohol consumption interferes with intestinal thiamine absorption. A
**genetic mutation in the transketolase gene** (producing an enzyme with
lowered affinity for thiamine) heightens sensitivity to thiamine deficiency,
worsening symptoms — slowing the whole PPP, and exacerbating the memory loss,
mental confusion, and partial paralysis characteristic of the syndrome.

---

## Ch. 6 — Glycogen Metabolism {#ch06}

> **Source:** Dr. Osama Essawi, "Ch 6 - Glycogen Metabolism" (25 slides); Dr.
> Suheir Ereqat, "7) GLYCOGEN" (37 slides).

### 6.1 Glycogen — structure and why the cell stores glucose this way {#ch06-1}

**Glycogen** is a branched polymer of alpha(1→4)-linked glucose, with
alpha(1→6) branch-point linkages every 12-14 glucose units — each chain
segment has 12-14 glucose residues (per the "General Structure of a Glycogen
Particle" diagram). It is the polymeric storage form of glucose in animals,
found primarily in **liver** (up to ~10% of liver weight) and **skeletal
muscle** (~1-2% of muscle weight).

- **Muscle glycogen** provides a quick energy source for either aerobic or
  anaerobic metabolism, delivering glucose for muscle contraction within
  seconds; it can be exhausted in **less than an hour** of vigorous activity.
- **Liver glycogen** is a reservoir of glucose for *other* tissues when
  dietary glucose is unavailable (between meals or during a fast) — this
  matters especially for brain neurons, which cannot use fatty acids as fuel.
  Liver glycogen can be depleted in **12-24 hours**.

**Why store glucose as glycogen rather than as free glucose or G6P?**
- Free glucose is water-soluble: it could be excreted via the kidneys, and at
  storage-level concentrations would disturb osmotic pressure (be
  hypertonic), risking cell lysis. (A hepatocyte storing its glycogen's worth
  of glucose monomerically would reach roughly 0.4 M — high enough to raise
  osmolarity and cause cell rupture.)
- G6P would instead simply be degraded via glycolysis rather than stored.
- **Glycogen**, as a polymer, is insoluble and does not disturb osmotic
  pressure, while its many nonreducing ends remain accessible for rapid
  mobilization by glycogen metabolism.

### 6.2 Glycogen particle structure and glycogenin {#ch06-2}

A glycogen particle is a tiered, highly branched globular granule built
around a core protein, **glycogenin**: primer chain (attached to glycogenin)
→ second tier → third tier → fourth tier → outer (unbranched) tier. The
entire granule may contain roughly **30,000 glucose units**.

**Glycogenin primes new glycogen chains**, in two steps:
1. **Autocatalytic** formation of a glycosidic bond between the glucose of
   UDP-glucose and **Tyr194** of glycogenin, catalyzed by the
   glucosyltransferase activity of glycogenin itself.
2. Sequential addition of **seven more glucose residues** (each from
   UDP-glucose), via glycogenin's chain-extending activity, forming an
   8-glucose primer. **Glycogen synthase** then takes over, extending the
   chain further, followed by the branching enzyme.

Glycogenin remains buried within the particle, covalently attached to the
single reducing end of the whole glycogen molecule.

### 6.3 Glycogenolysis (breakdown) {#ch06-3}

Glycogen enters the glycolytic pathway through three enzymes:

1. **Glycogen phosphorylase** — catalyzes phosphorolytic cleavage at
   nonreducing ends: glucose_n + Pi -> glucose 1-phosphate + glucose_(n-1).
   Requires inorganic phosphate (Pi) and a **pyridoxal phosphate (PLP)**
   coenzyme (the same cofactor used in transamination reactions). Acts
   repetitively, chopping off one glucose 1-phosphate at a time, until it
   reaches a point **four residues away** from an alpha(1→6) branch point,
   then stops.
2. **Debranching enzyme** (formally oligo-(alpha1→6)-to-(alpha1→4)-
   glucantransferase) — bifunctional, catalyzing two successive reactions:
   - *Transferase activity*: shifts a block of **three glucose residues**
     from the branch to a nearby nonreducing end, reattaching them there in
     alpha(1→4) linkage.
   - *(alpha1→6)-glucosidase activity*: releases the single remaining glucose
     residue at the branch point (still in alpha1→6 linkage) as **free
     glucose** — note specifically that this step releases a free glucose,
     **not** glucose 1-phosphate. Glycogen phosphorylase then resumes work on
     the now-unbranched chain.
3. **Phosphoglucomutase** — catalyzes the reversible isomerization of glucose
   1-phosphate to glucose 6-phosphate (the reaction proceeds through the
   enzyme first phosphorylated on a Ser residue).

**Fates of the resulting glucose 6-phosphate:**
- **In muscle** (and adipose tissue): G6P enters glycolysis directly as an
  energy source for contraction. Muscle and adipose tissue **lack glucose
  6-phosphatase**, so they cannot convert this G6P to free glucose — these
  tissues therefore do **not** contribute glucose to the blood.
- **In liver**: **glucose-6-phosphatase** converts G6P to free glucose, which
  is released into the blood. Mechanistically, this requires the G6P to enter
  the endoplasmic reticulum via a transporter, be dephosphorylated by
  glucose-6-phosphatase on the ER's inside wall, and then the resulting free
  glucose leaves the cell via another transporter.

### 6.4 Glycogenesis (synthesis) {#ch06-4}

1. Glucose is phosphorylated by **hexokinase** to glucose 6-phosphate.
2. G6P is isomerized by **phosphoglucomutase** to glucose 1-phosphate.
3. **UDP-glucose pyrophosphorylase**: glucose 1-phosphate + UTP -> UDP-glucose
   + PPi. UDP-glucose is the immediate substrate for glycogen synthase.
   - **Sugar nucleotides** generally (of which UDP-glucose is an example) are
     compounds in which a sugar's anomeric carbon is activated by attachment
     to a nucleotide via a phosphate ester linkage — they are the substrates
     for polymerizing monosaccharides into disaccharides, glycogen, starch,
     cellulose, and more complex extracellular polysaccharides.
4. **Glycogen synthase** elongates the glycogen chain: it transfers the
   glucose residue of UDP-glucose to the nonreducing end of a glycogen
   branch, forming a new alpha(1→4) linkage and releasing UDP. The chain
   being extended must already be longer than 4 residues (i.e., synthase acts
   on an existing primer/branch, consistent with glycogenin's role in
   priming new chains).
5. **Glycogen-branching enzyme** forms the alpha(1→6) branch-point bonds —
   glycogen synthase itself *cannot* make these. The branching enzyme
   transfers a terminal fragment of **6 or 7 glucose residues** from the
   nonreducing end of a branch that is at least **11 residues** long, to the
   C-6 hydroxyl of a glucose residue at a more interior position (at least
   **4 units away** from the existing branch point) of the same or another
   chain — creating a new branch, which glycogen synthase can then extend
   further.

**Biological effect of branching**: makes the glycogen molecule more soluble
and increases the number of nonreducing ends — which increases the number of
sites accessible to both glycogen phosphorylase and glycogen synthase, since
both enzymes act only at nonreducing ends.

### 6.5 Coordinated regulation of breakdown and synthesis {#ch06-5}

Like glycolysis and gluconeogenesis, regulation of the glycogen
breakdown/synthesis cycle occurs at irreversible points in the pathway (the
cyclical relationship glucose <-> G6P <-> G1P <-> UDP-glucose <-> glycogen,
via hexokinase/glucose-6-phosphatase, phosphoglucomutase, UDP-glucose
pyrophosphorylase/glycogen synthase, and glycogen phosphorylase respectively).

**Skeletal muscle glycogen phosphorylase** exists in two interconvertible
forms:
- **Phosphorylase a** — catalytically active (phosphorylated form).
- **Phosphorylase b** — much less active (dephosphorylated form).

**Allosteric regulation** (independent of hormones) — by ATP, AMP, and
glucose 6-phosphate: depletion of ATP is an excellent reason to tap the
glycogen store to regenerate it (activating breakdown), while glucose
6-phosphate is plentiful exactly when glucose itself is abundant, so it
should promote synthesis rather than breakdown.

**Hormonal control** — epinephrine (from vigorous muscle activity, acting in
both liver and muscle) and glucagon (acting in the liver) trigger a cAMP
cascade that phosphorylates and interconverts these enzymes:
1. Elevated [cAMP] activates **cAMP-dependent protein kinase (protein kinase
   A, PKA)**.
2. PKA phosphorylates and activates **phosphorylase b kinase**.
3. Phosphorylase b kinase phosphorylates **glycogen phosphorylase b**,
   converting it to the active **phosphorylase a**, stimulating glycogen
   breakdown.
4. PKA *also* directly phosphorylates **glycogen synthase**, which
   *inactivates* it (glycogen synthase a, the active form, has three Ser
   residues near its C-terminus; phosphorylation of these — by **glycogen
   synthase kinase 3, GSK3** — converts it to the inactive b form). Glycogen
   synthase and phosphorylase therefore respond in **opposite** ways to
   phosphorylation: synthase is inactivated, phosphorylase is activated.

**Insulin** promotes the active glycogen-synthesizing state: it inhibits
GSK3 and activates **phosphoprotein phosphatase 1 (PP1)**, which removes
phosphoryl groups from all three of the enzymes phosphorylated in response to
glucagon/epinephrine — phosphorylase kinase, glycogen phosphorylase, and
glycogen synthase — thereby simultaneously stimulating glycogen synthesis and
inhibiting breakdown. Epinephrine (or glucagon in the liver) has the opposite
overall effect.

**Comparison of glycogen phosphorylase regulation, liver vs. skeletal
muscle:**

| Glycogen phosphorylase | Liver | Skeletal muscle |
|---|---|---|
| Activated by | Epinephrine, glucagon | Epinephrine, AMP, Ca2+ |
| Inhibited by | Insulin, glucose | Insulin, ATP |

**Liver-specific integration** — either glucagon or epinephrine maximizes
hepatic glucose output to the blood. A fuller liver signaling diagram (Dr.
Osama's slides) traces two directions:
- **High blood glucose** -> insulin -> (via insulin-sensitive protein kinase,
  PKB, and increased [glucose]_inside via GLUT2) -> PP1 up / GSK-3 down ->
  phosphorylase kinase down, glycogen phosphorylase down, glycogen synthase
  up -> glycogen breakdown down, glycogen synthesis up, glycolysis up
  (glycolysis also promoted by new synthesis of hexokinase II, PFK-1,
  pyruvate kinase).
- **Low blood glucose** -> glucagon -> cAMP up -> PKA up -> phosphorylase
  kinase up, glycogen phosphorylase up; PKA also raises FBPase-2 / lowers
  PFK-2 activity, lowering [fructose 2,6-bisphosphate] (F26BP), which lowers
  PFK-1 and pyruvate kinase L activity -> glycogen breakdown up, glycogen
  synthesis down, glycolysis down. (F26BP's role as the PFK-1/FBPase-1
  switch is covered fully in Chapter 7's gluconeogenesis-regulation section.)

**Skeletal muscle**, by contrast: uses its own stored glycogen only for its
own needs, undergoes very large swings in ATP demand, and **lacks the
enzymatic machinery for gluconeogenesis** entirely — so unlike liver, it
never contributes glucose back to the blood regardless of hormonal state.

### 6.6 Glycogen storage diseases {#ch06-6}

**Glycogen storage diseases (GSDs)** are genetic enzyme deficiencies
associated with excessive glycogen accumulation within cells; some of the
implicated enzymes belong to these same interconnected
breakdown/synthesis pathways. Genetic defects in either **glucose
6-phosphatase** or the **glucose 6-phosphate transporter T1** specifically
cause **type Ia** GSD.

> **Table 1, Glycogen Storage Diseases of Humans** (Dr. Osama's slides):
>
> | Type (name) | Enzyme affected | Primary organ/cells affected | Symptoms |
> |---|---|---|---|
> | Type 0 | Glycogen synthase | Liver | Low blood glucose, high ketone bodies, early death |
> | Type Ia (von Gierke) | Glucose 6-phosphatase | Liver | Enlarged liver, kidney failure |
> | Type Ib | Microsomal glucose 6-phosphate translocase | Liver | As in type Ia; also high susceptibility to bacterial infections |
> | Type Ic | Microsomal Pi transporter | Liver | As in type Ia |
> | Type II (Pompe) | Lysosomal glucosidase | Skeletal and cardiac muscle | Infantile form: death by age 2; juvenile form: muscle defects (myopathy); adult form: as in muscular dystrophy |
> | Type IIIa (Cori or Forbes) | Debranching enzyme | Liver, skeletal, and cardiac muscle | Enlarged liver in infants; myopathy |
> | Type IIIb | Liver debranching enzyme (muscle enzyme normal) | Liver | Enlarged liver in infants |
> | Type IV (Andersen) | Branching enzyme | Liver, skeletal muscle | Enlarged liver and spleen, myoglobin in urine |
> | Type V (McArdle) | Muscle phosphorylase | Skeletal muscle | Exercise-induced cramps and pain; myoglobin in urine |
> | Type VI (Hers) | Liver phosphorylase | Liver | Enlarged liver |
> | Type VII (Tarui) | Muscle PFK-1 | Muscle, erythrocytes | As in type V; also hemolytic anemia |
> | Type VIb, VIII, or IX | Phosphorylase kinase | Liver, leukocytes, muscle | Enlarged liver |
> | Type XI (Fanconi-Bickel) | Glucose transporter (GLUT2) | Liver | Failure to thrive, enlarged liver, rickets, kidney dysfunction |

> **Second table, same diseases** (Dr. Suheir's slides — kept alongside the
> table above per this source's policy of preserving both lecturers'
> material rather than merging tables that phrase clinical details
> differently):
>
> | Type | Deficient enzyme | Organ | Clinical features |
> |---|---|---|---|
> | I: von Gierke's | Glucose-6-phosphatase (also gluconeogenic) | Liver | Severe hypoglycemia, hepatomegaly, kidney failure |
> | II: Pompe's | Lysosomal alpha-1,4-glucosidase (acid maltase) | Skeletal muscles, heart | Cardiomegaly, muscle weakness, death by age 2 from heart failure and respiratory weakness |
> | III: Cori's | Debranching enzyme | Liver, muscles | Mild hypoglycemia, liver enlargement, myopathy |
> | IV: Anderson's | Branching enzyme | Liver, muscles | Cirrhosis, death by age 2 |
> | V: McArdle's | Muscle glycogen phosphorylase | Muscles | Muscle cramp and weakness on exercise, myoglobin in urine |
> | VI: Hers' | Hepatic glycogen phosphorylase | Liver | Mild hypoglycemia, hepatomegaly, cirrhosis |
> | VII: Tarui's | PFK-1 (muscle) | RBC; muscles | Inability to exercise, hemolytic anemia, myoglobin in urine |

---

## Ch. 7 — Gluconeogenesis and Regulation of Carbohydrate Metabolism {#ch07}

> **Source:** Dr. Suheir Ereqat, "3) Regulation and GLUCONEOGENESIS" (37
> slides). Dr. Osama Essawi's 2024 deck set has no standalone chapter on this
> topic — this chapter is built from Dr. Suheir's material only. (Dr. Osama's
> Ch3 slides briefly name pyruvate carboxylase as the main anaplerotic
> reaction feeding oxaloacetate — see Chapter 3, §3.6 — but do not cover
> gluconeogenesis as its own pathway.)

### 7.1 Regulation of glycolysis {#ch07-1}

Glucose flux through glycolysis is regulated to keep ATP levels nearly
constant. This is achieved by: a complex interplay of ATP consumption, NAD+
regeneration, and allosteric regulation of the pathway's three essentially
irreversible enzymes — **hexokinase, PFK-1, and pyruvate kinase**; hormonal
regulation (glucagon, epinephrine, insulin); and changes in gene expression
for several glycolytic enzymes.

**1. Hexokinase and glucokinase:**
- **Hexokinase** performs glycolysis step 1 in most tissues (muscle, brain).
  Low Km (high affinity) for glucose, so it can initiate glycolysis even when
  blood glucose is relatively low — but has a relatively low Vmax. It is
  inhibited by its own reaction product, glucose 6-phosphate — an important
  regulatory step that prevents wasting cellular ATP making G6P when glucose
  is not actually limiting.
- **Glucokinase** (hexokinase IV; liver and pancreatic beta cells) needs a
  much higher glucose concentration for maximal activity — most active when
  portal-vein glucose is very high, i.e. right after a carbohydrate-rich
  meal. High Vmax lets the liver effectively clear excess glucose and
  minimize post-meal hyperglycemia. Inhibited by **fructose 6-phosphate**
  (not by its own product, G6P).
  - **Regulation by nuclear sequestration**: a regulatory protein inhibits
    glucokinase by forming a complex with it in the presence of high
    fructose 6-phosphate; this same protein is a nuclear-binding protein
    that draws glucokinase *into the nucleus* when liver F6P is high, and
    releases it back to the cytosol when glucose concentration is high.

**2. Phosphofructokinase-1 (PFK-1):** the single most important allosteric
regulator of *both* glycolysis and gluconeogenesis is **fructose
2,6-bisphosphate (F2,6BP)** — notably, F2,6BP is not itself an intermediate
of either pathway (full mechanism in §7.4-7.5). ATP is also a direct
allosteric inhibitor of PFK-1.
- Regulation of F2,6BP level tracks the **insulin/glucagon ratio**
  (fed/starved state): glucagon is high in starvation (low blood glucose),
  favoring hepatic gluconeogenesis; insulin favors glycolysis instead.
  F2,6BP's stimulation of PFK-1 by rising F6P is an example of **feed-forward
  stimulation** and makes F2,6BP a potent activator of glycolysis when
  present.

**3. Pyruvate kinase:** regulated by both allosteric effectors and covalent
modification (phosphorylation), like PFK-1.
- **Allosteric**: activated by fructose 1,6-bisphosphate in the liver
  (another feed-forward stimulation example); ATP and alanine are allosteric
  inhibitors.
- **Covalent/hormonal**: only the **liver isozyme (L form)** — not the muscle
  isozyme (M form) — is regulated by phosphorylation. High glucagon (low
  blood glucose) triggers cAMP-dependent protein kinase (PKA) to phosphorylate
  and *inactivate* the L isozyme, slowing hepatic glucose consumption and
  sparing glucose for export to the brain and other organs.
- Hormonal regulation of glycolysis this way coordinates activity across
  tissues/organs — the same hormones also regulate gluconeogenesis and
  glycogen metabolism (Chapter 6).

**Pyruvate kinase deficiency** — an autosomal recessive disorder; the
resulting enzyme lack slows glycolysis. In red blood cells specifically, this
rapidly causes ATP deficiency and hemolysis, producing **hemolytic anemia**
and increased plasma bilirubin. Mechanistically: a mismatch between RBC
energy requirements and ATP-generating capacity causes irreversible membrane
injury (cellular distortion, rigidity, dehydration), leading to premature
erythrocyte destruction by the spleen and liver.

### 7.2 Gluconeogenesis — overview and the three bypass reactions {#ch07-2}

**Gluconeogenesis** occurs mainly in **liver, kidney, and small intestine**.
It synthesizes glucose from pyruvate, reusing many glycolytic enzymes — but
three glycolytic reactions have such large negative delta-G that they are
essentially irreversible: those catalyzed by **hexokinase/glucokinase,
PFK-1, and pyruvate kinase**. Each must be *bypassed* by a distinct
gluconeogenic reaction (two of the three bypasses are simple hydrolyses).

**First bypass — of pyruvate kinase (two enzymes):**
1. **Pyruvate carboxylase**: pyruvate + HCO3- + ATP -> oxaloacetate + ADP +
   Pi. Requires **biotin** as a cofactor.
   - *Mechanism* (Lehninger Fig. 16-16, biotin's role): biotin is attached to
     the enzyme via an amide bond to a Lys residue's epsilon-amino group
     (forming biotinyl-enzyme). Biotin-mediated carboxylations occur in two
     phases, generally at separate active sites: **phase 1** — bicarbonate
     is activated by ATP to carboxyphosphate, which breaks down to CO2 (with
     release of Pi); CO2 then reacts with biotin (+H+) to form
     carboxybiotin. **Phase 2** — biotin transports the CO2 from the first
     active site to the second (on an adjacent monomer of the tetrameric
     enzyme); there, pyruvate is first converted to its enolate form
     (pyruvate enolate) as biotin is decarboxylated; the pyruvate enolate
     then reacts with the released CO2 to form oxaloacetate, which is
     released.
2. **PEP carboxykinase**: oxaloacetate + GTP -> PEP + GDP + CO2.

**Second bypass — of PFK-1:**
- **Fructose-1,6-bisphosphatase (FBPase-1)**: fructose 1,6-bisphosphate + H2O
  -> fructose 6-phosphate + Pi (a straightforward hydrolysis, the reverse
  direction from PFK-1's ATP-consuming phosphorylation).

**Third bypass — of hexokinase/glucokinase:**
- **Glucose-6-phosphatase**: glucose 6-phosphate + H2O -> glucose + Pi (again
  a simple hydrolysis).

> **Table 14-3, Sequential Reactions in Gluconeogenesis Starting from
> Pyruvate** (Dr. Suheir's slides; the three bypass reactions above are
> shown x2 in the table because two 3-carbon precursors are needed per
> glucose molecule; all other listed reactions are the shared reversible
> steps of glycolysis run in reverse):
>
> | Reaction | Count |
> |---|---|
> | Pyruvate + HCO3- + ATP -> oxaloacetate + ADP + Pi | x2 |
> | Oxaloacetate + GTP <=> PEP + CO2 + GDP | x2 |
> | PEP + H2O <=> 2-phosphoglycerate | x2 |
> | 2-phosphoglycerate <=> 3-phosphoglycerate | x2 |
> | 3-phosphoglycerate + ATP <=> 1,3-bisphosphoglycerate + ADP | x2 |
> | 1,3-bisphosphoglycerate + NADH + H+ <=> glyceraldehyde 3-phosphate + NAD+ + Pi | x2 |
> | Glyceraldehyde 3-phosphate <=> dihydroxyacetone phosphate | |
> | Glyceraldehyde 3-phosphate + dihydroxyacetone phosphate <=> fructose 1,6-bisphosphate | |
> | Fructose 1,6-bisphosphate -> fructose 6-phosphate + Pi | |
> | Fructose 6-phosphate <=> glucose 6-phosphate | |
> | Glucose 6-phosphate + H2O -> glucose + Pi | |
>
> **Sum**: 2 Pyruvate + 4 ATP + 2 GTP + 2 NADH + 2 H+ + 4 H2O -> glucose + 4
> ADP + 2 GDP + 6 Pi + 2 NAD+.
>
> Note (as given on the slide): reactions needed to replace the cytosolic
> NADH consumed at the glyceraldehyde-3-phosphate dehydrogenase step (i.e.,
> converting lactate to pyruvate in the cytosol, or transporting reducing
> equivalents from mitochondria to cytosol as malate) are *not* included in
> this summary equation. Biochemical equations here are not necessarily
> balanced for H and charge.

### 7.3 Sources of carbon for gluconeogenesis {#ch07-3}

During fasting or carbohydrate starvation, the pyruvate and oxaloacetate fed
into gluconeogenesis come mainly from **amino acid catabolism**: some amino
acids are catabolized directly to pyruvate or oxaloacetate; muscle proteins
may break down to supply amino acids, which are transported to the liver,
deaminated, and converted into gluconeogenic inputs. **Glycerol**, from
hydrolysis of triacylglycerols in fat cells, is also a significant
gluconeogenic input.

> **Table 14-4, Glucogenic Amino Acids, Grouped by Site of Entry** (Dr.
> Suheir's slides):
>
> | Entry point | Amino acids |
> |---|---|
> | Pyruvate | Alanine, cysteine, glycine, serine, threonine, tryptophan* |
> | alpha-Ketoglutarate | Arginine, glutamate, glutamine, histidine, proline |
> | Succinyl-CoA | Isoleucine*, methionine, threonine, valine |
> | Fumarate | Phenylalanine*, tyrosine* |
> | Oxaloacetate | Asparagine, aspartate |
>
> *Also ketogenic (i.e., these three are both glucogenic and ketogenic — see
> Chapter 10). Note on the table: all these amino acids are glucose/liver
> glycogen precursors because they can be converted to pyruvate or citric
> acid cycle intermediates. Of the 20 common amino acids, **only leucine and
> lysine** are unable to furnish carbon for net glucose synthesis (i.e.,
> they are purely ketogenic).

**Malate shuttle in gluconeogenesis** — transporting malate from the
mitochondrion to the cytosol, and reconverting it there to oxaloacetate
(catalyzed by malate dehydrogenase, MDH, on both sides), effectively moves
reducing equivalents (as NADH) into the cytosol, where they are otherwise
scarce. This route (pyruvate -> ... -> malate -> OAA -> PEP) therefore also
balances the NADH produced vs. consumed in the cytosol during
gluconeogenesis. (Note: when lactate itself is the gluconeogenic input, its
conversion to pyruvate in hepatocyte cytosol directly yields cytosolic NADH,
so this malate-shuttle export of reducing equivalents becomes unnecessary in
that specific case.)

### 7.4 The Cori cycle and the alanine cycle {#ch07-4}

Gluconeogenesis participates in **two cycles** that help maintain blood
glucose level: the **Cori cycle** and the **alanine cycle**. Glucose formed
by gluconeogenesis circulates in blood to peripheral tissues.

**Cori cycle** — lactate (produced by anaerobic glycolysis in muscle or RBCs)
travels via blood to the liver, where it is converted back to glucose;
that glucose returns via blood to muscle. Necessary to recycle lactate in
large mammals on a recovery basis after anaerobic exercise. Quantitatively
(per the slide's own diagram): muscle glycolysis converts glucose to 2
lactate at a cost of **2 ATP**; liver gluconeogenesis converts that 2 lactate
back to glucose at a cost of **6 ATP** — the cycle is a net energy *cost* to
the liver on behalf of the muscle, not a net gain anywhere.

**Alanine cycle** — named alongside the Cori cycle as the second such
cycle (glucose-carbon-recycling systems); covered together with the Cori
cycle as "2 cycles to maintain blood glucose level" on the slides, though
without its own separate diagram in this deck (compare Chapter 10's coverage
of alanine's role in carrying amino groups from muscle to liver via the
glucose-alanine cycle).

### 7.5 Regulation of gluconeogenesis {#ch07-5}

**Reciprocal regulation with glycolysis** — glycolysis and gluconeogenesis
are reciprocally regulated so both pathways are never fully active at the
same time (which would otherwise just waste ATP/GTP in a futile cycle).

**PFK-1 vs. FBPase-1**, by ATP/ADP/AMP/citrate (mirrors the ATP-producing
pathway logic of Chapter 4, §4.11):
- **PFK-1** (glycolysis): inhibited by ATP and citrate; activated by ADP and
  AMP.
- **FBPase-1** (gluconeogenesis): inhibited by AMP (opposite effect from its
  effect on PFK-1).
- Framed as an ATP/ADP,AMP-ratio-driven switch between the two enzymes acting
  on the shared fructose-6-phosphate/fructose-1,6-bisphosphate pool.

**Fructose 2,6-bisphosphate (F2,6BP)** — the master allosteric regulator of
both pathways at this step:
- **High [F2,6BP]** -> stimulates PFK-1, inhibits FBPase-1 -> stimulates
  glycolysis, inhibits gluconeogenesis.
- **Low [F2,6BP]** -> inhibits PFK-1 (removing its stimulatory effect),
  activates FBPase-1 -> inhibits glycolysis, stimulates gluconeogenesis.

F2,6BP's own level is set by a single **bifunctional enzyme**, **PFK-2/
FBPase-2** (one polypeptide with two opposing catalytic activities,
interconverted by phosphorylation):
- **Dephosphorylated form**: PFK-2 domain active, FBPase-2 domain inactive ->
  F2,6BP is synthesized (accumulates) -> stimulates glycolysis, inhibits
  gluconeogenesis. Favored by **insulin**, via activation of a
  phosphoprotein phosphatase that dephosphorylates the bifunctional enzyme.
- **Phosphorylated form**: PFK-2 domain inactive, FBPase-2 domain active ->
  F2,6BP is degraded (falls) -> inhibits glycolysis, stimulates
  gluconeogenesis. Favored by **glucagon**, via cAMP -> cAMP-dependent
  protein kinase (PKA), which phosphorylates the bifunctional enzyme.
- Phosphorylation of this bifunctional enzyme is thus regulated by blood
  glucose level, mediated by the glucagon/insulin balance. High glucagon
  (low blood sugar) converts F2,6BP back to F6P (removing PFK-1
  stimulation), slowing glycolysis; glucagon also promotes transcription of
  the **PEP carboxykinase** gene, reinforcing gluconeogenesis at the gene
  level.
- Conversion of F6P to F2,6BP is itself stimulated by high F6P levels — a
  second example of **feed-forward stimulation**, which (as a general
  principle) ensures pathway intermediates don't accumulate uselessly.
  F2,6BP therefore regulates gluconeogenesis as much as it regulates
  glycolysis.

**Acetyl-CoA and pyruvate's two alternative fates:**
- When fatty acids are readily available as fuel, their breakdown in liver
  mitochondria yields acetyl-CoA — a signal that further oxidation of
  glucose for fuel is unnecessary.
- **Acetyl-CoA is a positive allosteric modulator of pyruvate carboxylase**
  (stimulating gluconeogenesis) and simultaneously a **negative modulator of
  the pyruvate dehydrogenase complex** (inhibiting further glucose
  oxidation) — i.e., the same molecule pushes pyruvate toward
  gluconeogenesis and away from the TCA cycle at once. Pyruvate carboxylase
  is stimulated by acetyl-CoA specifically to increase gluconeogenesis rate
  when the cell has adequate fatty-acid supplies for its energy needs.

**A cross-kingdom limitation** (noted explicitly on the slides): **animals
cannot convert acetyl-CoA derived from fatty acids into net glucose** — only
plants and microorganisms can (via the glyoxylate cycle, not covered in this
deck). This is why fatty acid breakdown can *signal* and *support*
gluconeogenesis (via acetyl-CoA's allosteric effects above and by supplying
ATP) but can never itself be a net carbon *source* for new glucose in
animals.

---

## Ch. 8 — Fatty Acid Catabolism (beta-Oxidation) {#ch08}

> **Source:** Dr. Osama Essawi, "Ch 7: Fatty Acid Catabolism" (22 slides);
> Dr. Suheir Ereqat, "8) Fatty Acid oxidation" (23 slides).

### 8.1 Fatty acid oxidation as an energy source {#ch08-1}

Fatty acid oxidation is a central energy-yielding pathway for many organisms
and tissues — the greatest fraction of fuel for most vertebrate organs,
particularly **muscle (including heart) and liver**: providing as much as
**80% of energetic needs in mammalian heart and liver**, and about **40% of
daily energy requirement** overall. Electrons removed from fatty acids during
oxidation pass through the respiratory chain, driving ATP synthesis; the
acetyl-CoA produced can be completely oxidized to CO2 in the citric acid
cycle. Many hibernating animals (e.g., bears) rely almost exclusively on fat
for energy.

**Sources of fatty acid fuel** (four): fats consumed in the diet; fats stored
in cells as lipid droplets (adipocytes); fats synthesized in one organ for
export to another (liver, from carbohydrate); fats obtained by autophagy.

**Advantages of fat over polysaccharide as an energy store:**
- Fatty acids carry more energy per carbon, being more reduced.
- Fatty acids are nonpolar, so they carry/complex with less water.
- Fats suit long-term (months) energy storage — dense storage, slow
  delivery.

### 8.2 Digestion, transport, and mobilization of fat {#ch08-2}

Dietary fats are absorbed in the small intestine. **Chylomicrons** —
spherical lipoprotein particles (apolipoprotein + lipids) that package and
transport dietary lipid; lipoprotein particles range in density from
chylomicrons and VLDL up to (V)HDL.

**Hormonal mobilization of stored triacylglycerols**: epinephrine and
glucagon stimulate adenylyl cyclase, raising intracellular cAMP; cAMP-
dependent protein kinase (PKA) then opens the lipid droplet to cytosolic
lipases, which act on tri-, di-, and monoacylglycerols, releasing fatty acids
and glycerol for transport to tissues such as skeletal muscle, heart, and
renal cortex for oxidation.

**Glycerol's fate** — only about **5% of triacylglycerol's biologically
available energy** resides in the glycerol moiety (the rest is in the three
long-chain fatty acids).
- **Well-fed state** — glycerol kinase phosphorylates glycerol (using ATP) to
  glycerol 3-phosphate, which (via glyceraldehyde 3-phosphate) enters
  **glycolysis**.
- **Fasting state** — glycerol is instead converted into glucose via
  **gluconeogenesis** (entering near fructose 1,6-bisphosphate, via
  aldolase).

### 8.3 Activation and mitochondrial transport of fatty acids {#ch08-3}

**Activation** — transport of long-chain fatty acids (14+ carbons) across the
mitochondrial membrane requires activation to a **fatty acyl-CoA** first.
**Fatty acyl-CoA synthetase** isozymes, in the outer mitochondrial membrane
(also called thiokinase), activate the fatty acid by forming a fatty
acyl-CoA thioester — a thioester linkage between the fatty acid's carboxyl
group and CoA's thiol group, itself a high-energy compound.

**Carnitine shuttle** — long-chain (14+ carbon) fatty acyl-CoA must be
attached to **carnitine** to cross the inner mitochondrial membrane. The
**acyl-carnitine/carnitine cotransporter** allows passive transport of the
fatty acyl-carnitine ester: as one fatty acyl-carnitine moves into the
matrix, one free carnitine moves back out into the intermembrane space. This
carnitine-mediated entry is the **rate-limiting step** for mitochondrial
fatty acid oxidation, and a key regulatory point (§8.7).

### 8.4 beta-Oxidation — three stages, four-step cycle {#ch08-4}

Fatty acid catabolism, overall, has three stages (paralleling glucose
oxidation, Chapter 3):
1. **beta-Oxidation** — oxidative removal of successive 2-carbon units from
   the fatty acid, as acetyl-CoA.
2. **Citric acid cycle** — oxidation of the acetyl-CoA groups to CO2, in the
   mitochondrial matrix; generates NADH, FADH2, and one GTP per turn.
3. **Electron transport chain / oxidative phosphorylation** — generates ATP
   from the NADH and FADH2.

**The four-reaction beta-oxidation cycle** (repeated once per 2-carbon unit
removed):
1. **Acyl-CoA dehydrogenase** — a flavoprotein with tightly bound FAD;
   dehydrogenates the fatty acyl-CoA to a **trans-Delta2-enoyl-CoA**
   (introducing a trans double bond between C2-C3).
2. **Enoyl-CoA hydratase** — hydrates the double bond of
   trans-Delta2-enoyl-CoA, yielding **L-beta-hydroxyacyl-CoA**.
3. **beta-Hydroxyacyl-CoA dehydrogenase** — oxidizes L-beta-hydroxyacyl-CoA to
   **beta-ketoacyl-CoA** (NAD+-linked).
4. **Thiolase** (acyl-CoA acetyltransferase) — thiolytic cleavage of
   beta-ketoacyl-CoA by free CoA, yielding **acetyl-CoA** and a fatty
   acyl-CoA shortened by two carbons — ready to re-enter step 1.

**Stoichiometry for palmitoyl-CoA (16 carbons, 7 rounds of the cycle):**
Palmitoyl-CoA + 7 CoA + 7 FAD + 7 NAD+ + 7 H2O -> 8 acetyl-CoA + 7 FADH2 + 7
NADH + 7 H+.

> **Table 17-1, Yield of ATP during Oxidation of One Molecule of
> Palmitoyl-CoA to CO2 and H2O** (Dr. Osama's slides):
>
> | Enzyme catalyzing the oxidation step | NADH or FADH2 formed | ATP ultimately formed |
> |---|---|---|
> | *beta-Oxidation* | | |
> | Acyl-CoA dehydrogenase | 7 FADH2 | 10.5 |
> | beta-Hydroxyacyl-CoA dehydrogenase | 7 NADH | 17.5 |
> | *Citric acid cycle* | | |
> | Isocitrate dehydrogenase | 8 NADH | 20 |
> | alpha-Ketoglutarate dehydrogenase | 8 NADH | 20 |
> | Succinyl-CoA synthetase | (GTP, direct) | 8 |
> | Succinate dehydrogenase | 8 FADH2 | 12 |
> | Malate dehydrogenase | 8 NADH | 20 |
> | **Total** | | **108** |
>
> (This total of 108 is before subtracting the 2 ATP-equivalents spent
> activating the free fatty acid to palmitoyl-CoA at the outset — the
> commonly cited net yield for palmitate is 106 ATP.)

### 8.5 Oxidation of odd-chain and unsaturated fatty acids {#ch08-5}

**Odd-numbered fatty acids** — beta-oxidation of an odd-chain fatty acid
yields acetyl-CoA units plus one final 3-carbon **propionyl-CoA** (propionate
itself, CH3-CH2-COO-, is also formed by cattle and other ruminants during
carbohydrate fermentation). Propionyl-CoA is processed to enter the TCA
cycle:
1. **Propionyl-CoA carboxylase** carboxylates propionyl-CoA to
   **D-methylmalonyl-CoA**.
2. **Methylmalonyl-CoA epimerase** epimerizes D-methylmalonyl-CoA to its
   **L**-stereoisomer.
3. **Methylmalonyl-CoA mutase** rearranges L-methylmalonyl-CoA
   intramolecularly to **succinyl-CoA**, which enters the citric acid cycle.

**Unsaturated fatty acids** — an extra **isomerase** step is needed to handle
the naturally-occurring **cis** double bond, since **enoyl-CoA hydratase**
(step 2 of the standard cycle) acts only on **trans** double bonds. Two
mechanisms depending on the double bond's original position:
- **One cis double bond** (e.g., **oleic acid**, 18:1 cis-Delta9): standard
  beta-oxidation proceeds normally for 3 cycles (yielding 3 acetyl-CoA),
  reaching a 12-carbon **cis-Delta3-dodecenoyl-CoA** intermediate — this
  cannot serve as a substrate for enoyl-CoA hydratase. **Delta3,Delta2-enoyl-
  CoA isomerase** ("the auxiliary enzyme") converts this cis-Delta3 double
  bond to a **trans-Delta2** double bond, restoring a normal hydratase
  substrate; beta-oxidation then resumes for 5 more cycles, yielding 6 more
  acetyl-CoA (9 acetyl-CoA total from the 18-carbon chain).
- Polyunsaturated fatty acids additionally require a **2,4-dienoyl-CoA
  reductase** step (mentioned in the sources only as a named auxiliary
  enzyme, not worked through in detail on these slides).

### 8.6 Regulation of beta-oxidation {#ch08-6}

Fatty acid oxidation is tightly regulated to occur only when the organism
actually needs the energy. In the liver, cytosolic fatty acyl-CoA has two
competing fates: mitochondrial **beta-oxidation**, or cytosolic conversion
into **triacylglycerols and phospholipids**. Which fate predominates depends
on the rate of long-chain fatty acyl-CoA transfer into mitochondria — i.e.,
on the carnitine shuttle (§8.3), the rate-limiting and key regulatory step.
Once fatty acyl groups have entered the mitochondrion, they are committed to
oxidation.

**Malonyl-CoA / CAT-1 switch** — malonyl-CoA, the first intermediate of
cytosolic fatty acid *synthesis*, **inhibits carnitine acyltransferase I
(CAT-1 / CPT-1)**, blocking fatty acid entry into mitochondria — preventing a
futile simultaneous cycle of fat synthesis and fat breakdown. The full
signaling logic (Dr. Suheir's diagram):
- **High blood glucose** -> insulin -> a phosphatase dephosphorylates and
  *activates* **acetyl-CoA carboxylase (ACC)** -> active ACC converts
  acetyl-CoA (from glycolysis/PDH) to malonyl-CoA (feeding fatty acid
  synthesis) -> malonyl-CoA inhibits CAT-1 -> beta-oxidation is blocked.
- **Low blood glucose** -> glucagon -> PKA phosphorylates and *inactivates*
  ACC -> malonyl-CoA falls -> CAT-1 is no longer inhibited -> fatty
  acyl-carnitine forms and enters the mitochondrion -> beta-oxidation
  proceeds, generating FADH2, NADH, and acetyl-CoA.

**Direct metabolite feedback** on two beta-oxidation enzymes, signaling
energy sufficiency:
- High **[NADH]/[NAD+]** ratio inhibits **acyl-CoA dehydrogenase**.
- High **[acetyl-CoA]** inhibits **thiolase**.

### 8.7 Ketone bodies {#ch08-7}

**Ketone bodies** — acetone, acetoacetate, and D-beta-hydroxybutyrate —
are formed from acetyl-CoA in the **liver**. Acetone is simply exhaled;
acetoacetate and D-beta-hydroxybutyrate are transported (being quite soluble
in blood and urine) to other tissues, where they are converted back to
acetyl-CoA for oxidation in the citric acid cycle. During starvation, the
liver processes fatty acids into ketone bodies specifically because, unlike
fatty acids themselves, ketone bodies **can cross the blood-brain barrier**
and fuel the brain.

**Formation (ketogenesis), from acetyl-CoA:**
1. **Thiolase** condenses two acetyl-CoA into **acetoacetyl-CoA** — this is
   the reversal of beta-oxidation's last step.
2. **HMG-CoA synthase** condenses acetoacetyl-CoA with a third acetyl-CoA to
   form **beta-hydroxy-beta-methylglutaryl-CoA (HMG-CoA)**.
3. **HMG-CoA lyase** cleaves HMG-CoA into free **acetoacetate** and
   acetyl-CoA.
4. To be released into the blood, CoA must first be removed from these
   species — acetone, acetoacetate, and beta-hydroxybutyrate can then travel
   freely through the blood; acetone specifically is removed as a gas and
   exhaled, while acetoacetate and beta-hydroxybutyrate are trafficked
   onward (to the brain and other tissues) for energy production.

**Use as fuel (extrahepatic), from D-beta-hydroxybutyrate:**
1. **D-beta-hydroxybutyrate dehydrogenase** oxidizes D-beta-hydroxybutyrate
   back to acetoacetate, in extrahepatic tissue.
2. **beta-Ketoacyl-CoA transferase** (also called **thiophorase**) activates
   the acetoacetate (transferring CoA from succinyl-CoA), forming
   acetoacetyl-CoA — which thiolase then cleaves to 2 acetyl-CoA, entering
   the citric acid cycle.
- **The liver itself lacks beta-ketoacyl-CoA transferase** — so ketone bodies
  are used as fuel in *all* tissues except the liver: the liver is a
  *producer* of ketone bodies for other tissues, never a *consumer* of them.
  Ketone bodies exported from the liver serve as an energy source for heart,
  skeletal muscle, kidney, and brain (per the export diagram) — note the
  liver diverts its own oxaloacetate into gluconeogenesis during this same
  state, which is part of why liver acetyl-CoA is routed to ketogenesis
  rather than the TCA cycle in the first place (§8.8).

### 8.8 Ketone body overproduction: starvation, diabetes, and ketoacidosis {#ch08-8}

**During starvation**: gluconeogenesis depletes citric acid cycle
intermediates (drawing them off, e.g. oxaloacetate, as gluconeogenic
substrate), diverting acetyl-CoA — from oxidation of mobilized stored fat —
away from the TCA cycle and toward ketone body production instead.

**In untreated diabetes**: insufficient insulin means extrahepatic tissues
cannot efficiently take up blood glucose, either for fuel or for conversion
to fat. Fatty acids then enter mitochondria and are degraded to acetyl-CoA —
but this acetyl-CoA cannot pass through the citric acid cycle, because cycle
intermediates have themselves been drawn off as gluconeogenic substrates (the
same underlying mechanism as starvation). The resulting acetyl-CoA
accumulation accelerates ketone body formation beyond extrahepatic tissues'
capacity to oxidize them.

**Consequences**: increased blood levels of acetoacetate and
D-beta-hydroxybutyrate lower blood pH, causing **acidosis**; extreme acidosis
can lead to coma and, in some cases, death. Ketone bodies reaching
extraordinary levels in blood/urine (as in untreated diabetes) is called
**ketosis**; ketosis combined with acidosis is **ketoacidosis**.

---

## Ch. 9 — Triglyceride Synthesis {#ch09}

> **Source:** Dr. Osama Essawi, "Chapter 8: TG synthesis" (labelled "21.2
> Biosynthesis of Triacylglycerols", 13 slides); Dr. Suheir Ereqat, "9) TG
> synthesis and TAG cycle" (12 slides).

### 9.1 Triacylglycerol structure and why the body stores fat this way {#ch09-1}

A **triacylglycerol (TAG/TG)** is glycerol esterified at all three carbons to
fatty acids — a *mixed* TAG carries three different fatty acids, e.g. the
named example **1-stearoyl, 2-linoleoyl, 3-palmitoyl glycerol**.

Synthesized or ingested fatty acids are either stored for energy or used in
membranes, depending on the organism's needs. Animals and plants both store
fat for fuel (plants: in seeds and nuts). A typical 70-kg human carries
roughly **15 kg of fat** — enough energy to last about **12 weeks** — compare
this with only about **12 hours'** worth of glycogen stored in liver and
muscle combined (Chapter 6). Animals, plants, and bacteria alike also make
phospholipids for cell membranes.

### 9.2 Biosynthesis pathway {#ch09-2}

**Glycerol 3-phosphate formation** — two sources:
- **Major route**: siphoned from **dihydroxyacetone phosphate (DHAP)**,
  itself a glycolytic intermediate, via the cytosolic NAD-linked enzyme
  **glycerol 3-phosphate dehydrogenase**.
- **Minor route** (liver and kidney only): directly from glycerol, via
  **glycerol kinase**.

**Stage 1 — phosphatidic acid**: **phosphatidic acid** (glycerol 3-phosphate
+ 2 fatty acids, attached by acyl transferases, releasing CoA each time) is
the shared precursor to *both* TAGs and phospholipids. The **acyl-CoA
synthetases** that activate the fatty acids here are the same enzymes that
prepare fatty acids for beta-oxidation (Chapter 8) — i.e., fatty-acyl-CoA
activation is a shared entry point feeding either catabolic (oxidation) or
anabolic (TAG/phospholipid synthesis) fates.

**Stage 2 — from phosphatidic acid to TAG:**
1. **Phosphatidic acid phosphatase** (lipin) removes the 3-phosphate,
   yielding **1,2-diacylglycerol**.
2. The third (C-3) carbon is then acylated with a third fatty acid, yielding
   the final **triacylglycerol**.

### 9.3 Regulation by insulin {#ch09-3}

**Insulin stimulates triacylglycerol synthesis.** Lack of insulin instead
causes: increased lipolysis; increased fatty acid oxidation (sometimes as far
as ketone body formation, if citric acid cycle intermediates — specifically
oxaloacetate, needed to react with acetyl-CoA — are depleted, as in Chapter
8's ketogenesis discussion). People with severe, untreated diabetes mellitus
consequently fail to synthesize fatty acids at all — and (per Dr. Suheir's
slides) also fail to use glucose properly; with increased fat oxidation and
ketone body formation as a result, these individuals lose weight.

### 9.4 The triacylglycerol cycle {#ch09-4}

About **75% of all fatty acids released by TAG breakdown (lipolysis) are
re-esterified back into TAG**, rather than being used directly for fuel —
this happens even during starvation. Some of this fatty acid recycling
happens locally in adipose tissue before release into the bloodstream.

**The TAG cycle**, as a systemic loop (per Dr. Suheir's 4-step description):
1. Triacylglycerol molecules in adipose tissue are broken down by lipolysis;
   some of the released free fatty acids (FFAs) pass into the bloodstream,
   while the rest are used to resynthesize TG locally.
2. Of the FFAs released into the blood, some are used for energy (e.g., in
   muscle), while others are taken up by the **liver** and used there for TG
   synthesis.
3. The TG formed in the liver is transported in the blood back to adipose
   tissue.
4. At adipose tissue, extracellular **lipoprotein lipase** releases the
   fatty acid from this TG again; it is taken up by adipocytes and
   re-esterified into TG once more, closing the cycle.

### 9.5 Glyceroneogenesis {#ch09-5}

**Question posed on the slides**: in adipose tissue, what is the source of
the glycerol 3-phosphate required for this TAG cycling, given that
**gluconeogenesis occurs in liver but not in adipose tissue**?

**Answer — glyceroneogenesis**: a shortened version of gluconeogenesis that
occurs in **both** liver and adipose tissue. It converts pyruvate to DHAP
(via the same early gluconeogenic enzymes, stopping short of glucose itself),
and DHAP is then converted to glycerol 3-phosphate for use in TAG synthesis.
This explains why adipose cells express **pyruvate carboxylase** and **PEP
carboxykinase (PEPCK)** — the same two enzymes that open gluconeogenesis
proper (Chapter 7) — even though fat cells never actually make glucose. The
rate of glyceroneogenesis controls the rate of TAG synthesis.

**Roles of glyceroneogenesis:**
- Helps control the rate of fatty acid release into the blood.
- Controls the rate at which free fatty acids reach mitochondria for use in
  thermogenesis.
- Supports glycerol 3-phosphate synthesis in fasting humans (when dietary
  glycerol/glucose is unavailable).

**Regulation by cortisol** — a stress hormone, has *reciprocal* effects on
glyceroneogenesis in the two tissues:
- In **liver**: cortisol *stimulates* PEP carboxykinase expression ->
  stimulates TAG production and export.
- In **adipose tissue**: cortisol *suppresses* PEP carboxykinase expression
  -> reduces fatty acid incorporation into TAG (favoring FA release instead).
- **Net effect**: increases the availability of both FA and TAG in the blood
  as an energy source. Framed generally: a *lower* rate of glyceroneogenesis
  in adipose tissue favors fatty acid *release* over recycling, while a
  *higher* rate in the liver favors TAG *synthesis and export* — the same
  pathway is regulated in opposite directions in the two tissues to the same
  net physiological end.

### 9.6 Clinical correlation: type 2 diabetes and thiazolidinediones {#ch09-6}

In **type 2 diabetes**, elevated blood free fatty acid levels interfere with
glucose utilization in muscle and promote/predispose to **insulin
resistance**.

**Thiazolidinediones (glitazones)** — a drug class used to treat type 2
diabetes. They work by increasing the expression of **PEP carboxykinase
specifically in adipose tissue**, which stimulates glyceroneogenesis there,
driving more FA incorporation into TAG (rather than release) — this lowers
circulating blood [FA], which in turn increases insulin sensitivity and
improves glucose utilization by muscle. (Contrast with cortisol above, which
suppresses adipose PEPCK — glitazones act in the opposite direction on the
same enzyme, in the same tissue, specifically to correct the diabetic FA/
insulin-resistance state.)

---

## Ch. 10 — Protein Metabolism {#ch10}

> **Source:** Dr. Osama Essawi, "Chapter 9: Protein Metabolism" (labelled
> "Amino Acid Oxidation and the Production of Urea", 20 slides); Dr. Suheir
> Ereqat, "10) Metabolism of Protein" (39 slides).

### 10.1 When amino acids are catabolized {#ch10-1}

Animals oxidatively degrade amino acids under three circumstances:
1. **Normal protein turnover** — some amino acids released by breakdown of
   cellular proteins are not needed for new protein synthesis and are
   catabolized instead.
2. **Protein-rich diet** — ingested amino acids exceed the body's needs for
   protein synthesis; the surplus is catabolized, since amino acids
   **cannot be stored** the way glucose (glycogen) or fat (TAG) can.
3. **Prolonged starvation or uncontrolled diabetes mellitus** — when
   carbohydrates are unavailable or not properly utilized, cellular proteins
   are used as fuel instead.

Overall, amino acid catabolism contributes only **10-15% of the body's
energy production** under ordinary circumstances.

### 10.2 Protein digestion {#ch10-2}

**In the stomach**: entry of dietary protein stimulates gastric mucosa to
secrete **gastrin**, which stimulates HCl secretion by parietal cells and
**pepsinogen** secretion by chief cells. The acidic gastric juice (pH
1.0-2.5) is both antiseptic (kills most bacteria/foreign cells) and a
protein-denaturing agent (unfolds globular proteins, exposing internal
peptide bonds to enzymatic hydrolysis). **Pepsinogen** (an inactive
zymogen) is converted to active **pepsin** by autocatalytic cleavage;
pepsin then hydrolyzes ingested protein into smaller peptides.

**In the small intestine**: as acidic stomach contents enter, the low pH
triggers secretion of **secretin** into the blood, which stimulates the
pancreas to secrete **bicarbonate**, neutralizing gastric HCl and raising pH
to about 7. Arrival of amino acids in the duodenum then triggers release of
**cholecystokinin**, which stimulates secretion and activation of several
pancreatic enzymes with pH 7-8 optima. **Trypsin and chymotrypsin** further
hydrolyze the peptides pepsin produced in the stomach.

**Zymogen protection of the pancreas** — the proteolytic enzymes are
secreted as inactive zymogens (trypsinogen — activated by
**enteropeptidase**; chymotrypsinogen; procarboxypeptidase A/B), alongside
pancreatic trypsin inhibitor and other anti-proteinases, to protect
pancreatic tissue from self-digestion.

**Acute pancreatitis** — caused by obstruction of the normal pathway by
which pancreatic secretions enter the intestine. The proteolytic zymogens
are converted to their active forms *prematurely*, inside the pancreatic
cells themselves, and attack the pancreas — causing excruciating pain and
potentially fatal organ damage.

### 10.3 Removing the amino group — transamination {#ch10-3}

Amino acids from dietary protein are the source of most amino groups; most
amino acids are metabolized in the liver.

**Transamination** — the first step in catabolism of most L-amino acids
(once they reach the liver): removal of the alpha-amino group by
**aminotransferases (transaminases)**. The alpha-amino group is transferred
to **alpha-ketoglutarate**, forming the corresponding alpha-keto acid of the
original amino acid, and **L-glutamate**. These reversible reactions
effectively collect amino groups from many different amino acids in the
single common form of L-glutamate, which then acts as an amino-group donor
for either biosynthesis or nitrogen-excretion pathways. Named examples
(amino acid / alpha-keto acid pair): glutamate/alpha-ketoglutarate,
alanine/pyruvate, aspartate/oxaloacetate.

**Pyridoxal phosphate (PLP)**, the coenzyme form of vitamin B6, is the
prosthetic group for **all** aminotransferases:
- **Pyridoxal phosphate** — the aldehyde form; accepts an amino group.
- **Pyridoxamine phosphate** — the aminated form; donates its amino group to
  an alpha-keto acid.

**Mechanism** — aminotransferases catalyze bimolecular **Ping-Pong**
reactions: the first substrate reacts and its product must leave the active
site before the second substrate can bind.
1. The incoming amino acid binds, donates its amino group to PLP, and
   leaves as an alpha-keto acid (PLP is now pyridoxamine phosphate).
2. The incoming alpha-keto acid binds, accepts the amino group from
   pyridoxamine phosphate, and departs as an amino acid (regenerating PLP).

### 10.4 Collecting and transporting amino groups {#ch10-4}

Glutamate and glutamine act as the body's general collection points for
amino groups — in most tissues, both are present at higher concentration
than other amino acids.

**Glutamate dehydrogenase (transdeamination)** — in hepatocytes, glutamate
(transported from cytosol into mitochondria) undergoes **oxidative
deamination**, catalyzed by **glutamate dehydrogenase**, releasing NH4+ and
regenerating alpha-ketoglutarate. This mitochondrial-matrix enzyme is unusual
in being able to use *either* NAD+ or NADP+ as the reducing-equivalent
acceptor. The alpha-ketoglutarate produced can re-enter the citric acid
cycle or be used for glucose synthesis. The combined action of an
aminotransferase followed by glutamate dehydrogenase is called
**transdeamination**; glutamate dehydrogenase itself sits at an important
intersection of carbon and nitrogen metabolism.

**Glutamine synthetase (ammonia transport)** — ammonia is toxic to animal
tissues, so **glutamine** serves as the nontoxic transport form of ammonia
between tissues/cells (and is the primary transport form of nitrogen
overall). **Glutamine synthetase** combines free ammonia with glutamate to
form glutamine (ATP-requiring). Glutamine also serves as an amino-group
source for various biosynthetic reactions. Excess glutamine travels via
blood to intestine, liver, and kidney, where **glutaminase** converts it
back to glutamate + ammonium ion ("offloads N as NH4+, recycles glutamate").
The ammonium ion produced in intestine and kidney is transported (in the
blood) to the liver for urea synthesis.

**The glucose-alanine cycle (alanine as an alternate nitrogen carrier)** —
vigorously working muscle operates nearly anaerobically, relying on
glycolysis; glycolysis yields pyruvate, which (if not disposed of) would
otherwise build up as lactic acid. Instead: in muscle, amino groups
collected by transamination as glutamate can transfer their alpha-amino
group to pyruvate (via **alanine aminotransferase**) to form **alanine**,
using pyruvate — a readily available glycolytic product — instead of
alpha-ketoglutarate as the carbon-skeleton acceptor. Alanine thus carries
*both* ammonia and the pyruvate carbon skeleton from muscle to the liver in
one nontoxic molecule. In the liver: the ammonia is excreted (via the urea
cycle), and the pyruvate carbon skeleton is used to make glucose
(gluconeogenesis), which is returned to the muscle — completing the cycle.
In the liver's mitochondria, glutamate can alternatively undergo glutamate
dehydrogenase deamination (releasing NH4+ directly) or transaminate with
oxaloacetate to form **aspartate** — a second nitrogen donor, this one
feeding directly into the urea cycle (§10.6).

### 10.5 Toxicity of ammonia {#ch10-5}

Ammonia, produced during amino acid catabolism, is highly toxic, particularly
to the **brain**. Removing ammonia from the cytosol requires two reactions:
1. **Reductive amination**: alpha-ketoglutarate + NH4+ + NADH -> glutamate +
   NAD+ (glutamate dehydrogenase, run in the ammonia-consuming direction).
2. **Glutamine synthetase**: glutamate + ATP + NH4+ -> glutamine + ADP + Pi.

Both enzymes are present at high levels in the brain (per Dr. Suheir's
slides, the glutamine synthetase reaction is almost certainly the more
important of the two for brain ammonia removal). The mechanism of toxicity:
in reaction 1, high NH4+ depletes cellular **NADH and alpha-ketoglutarate**
that are otherwise needed for ATP production; reaction 2 depletes **ATP**
itself, needed to maintain brain function. **Astrocytes** specifically
express glutamine synthetase to help remove ammonia — but excess ammonia
still impairs astrocyte function, altering their capacity to maintain
potassium homeostasis, leading to abnormal neuronal activity and potential
brain edema. Depletion of glutamate itself (consumed making glutamine) can
also deplete **glutamate and GABA (gamma-aminobutyrate)**, both important
neurotransmitters — so the brain's sensitivity to ammonia may reflect
neurotransmitter depletion as well as osmotic/potassium disturbance.

### 10.6 The urea cycle {#ch10-6}

**Excretory forms of nitrogen** vary by organism:
- **Ammonotelic** (excrete NH4+ directly) — most aquatic vertebrates, e.g.
  bony fishes and amphibian larvae.
- **Ureotelic** (excrete urea) — many terrestrial vertebrates, and also
  sharks.
- **Uricotelic** (excrete uric acid) — birds, reptiles.

The urea cycle's enzymes are split between the **mitochondrial matrix** and
the **cytosol**. **Carbamoyl phosphate** and **aspartate** are the two
nitrogen-bearing components formed (or supplied) that feed into the cycle.

**Four steps of the urea cycle:**
1. **Formation of citrulline** from ornithine + carbamoyl phosphate (entry
   of the *first* amino group); citrulline then passes into the cytosol.
   (Carbamoyl phosphate itself is made in the mitochondrial matrix by
   **carbamoyl phosphate synthetase I, CPS I**: HCO3- + NH4+ + 2 ATP ->
   carbamoyl phosphate + 2 ADP + Pi.)
2. **Formation of argininosuccinate**, via a citrullyl-AMP intermediate
   (entry of the *second* amino group, from **aspartate**).
3. **Formation of arginine** from argininosuccinate; this step releases
   **fumarate**, which enters the citric acid cycle.
4. **Formation of urea**, which also regenerates **ornithine** (closing the
   cycle) — this final step uses arginase.

### 10.7 Linking the urea cycle and the citric acid cycle {#ch10-7}

The fumarate released in step 3 (by argininosuccinase/argininosuccinate
lyase) is itself a citric acid cycle intermediate — linking the two cycles
in what is nicknamed the **"Krebs bicycle."** The connecting pathway is
called the **aspartate-argininosuccinate shunt**, which effectively links
the fates of amino groups (nitrogen) and carbon skeletons together.
Cytosolic fumarate can be converted to cytosolic malate, used locally or
transported into mitochondria to re-enter the TCA cycle; aspartate (the
urea cycle's second nitrogen donor) is regenerated from oxaloacetate via
transamination with glutamate (aspartate aminotransferase). The
**malate-aspartate shuttle** (Chapter 4, §4.9) helps move reducing
equivalents (NADH) into the mitochondrion as part of this same
interconnected system.

**Reducing the energetic cost of urea synthesis** — synthesizing one urea
molecule requires **4 high-energy phosphate groups**: 2 ATP to make
carbamoyl phosphate, and 1 ATP to make argininosuccinate (this last ATP
undergoes pyrophosphate cleavage to AMP + PPi, and the PPi is then
hydrolyzed to 2 Pi — so this single "ATP" actually costs the equivalent of
2 high-energy bonds). Overall equation:

2 NH4+ + HCO3- + 3 ATP + H2O -> urea + 2 ADP + 4 Pi + AMP + 2 H+.

The cycle's energetic cost is reduced by its interconnection with the TCA
cycle: fumarate generated by the urea cycle is converted to malate and
transported into mitochondria, where the **malate dehydrogenase** reaction
(regenerating oxaloacetate) produces NADH — each such NADH can generate up
to **2.5 ATP** during mitochondrial respiration, substantially offsetting
the urea cycle's own direct ATP cost.

### 10.8 Significance and regulation of the urea cycle {#ch10-8}

**Significance:**
- **Detoxification of ammonia** — toxic ammonia is converted to nontoxic
  urea.
- **Arginine biosynthesis** — kidney and intestine contribute most of the
  body's arginine, but lack the **arginase** enzyme; arginase is present
  **only in the liver**, so only the liver can complete the final urea cycle
  step and release free arginine as urea + ornithine.
- **Urea is the only new compound created by the cycle** — every other
  intermediate/reactant is recycled.
- The cycle's reactions consume **3-4 ATP equivalents** overall (consistent
  with the 4-high-energy-phosphate accounting above).

**Regulation, at two levels:**
- **Gross/long-term regulation** — at the level of enzyme synthesis: all
  four urea cycle enzymes *and* CPS I (five enzymes total) are synthesized
  at higher rates in starving animals and animals on very-high-protein
  diets, compared to well-fed animals eating primarily carbohydrate and fat.
- **Fine/short-term regulation** — allosteric activation of **CPS I** by
  **N-acetylglutamate**. N-acetylglutamate is itself synthesized from
  acetyl-CoA + glutamate by **N-acetylglutamate synthase**, an enzyme that
  is itself activated by **arginine** — so rising arginine (an intermediate
  further along the very same cycle) reinforces CPS I activity at the
  cycle's entry point.
- **Deficiency of any urea cycle enzyme (or CPS I) causes hyperammonemia** —
  toxic ammonia accumulation, since the cycle can no longer clear it (per
  Dr. Suheir's slides, noting these reactions are irreversible and a
  deficiency state = hyperammonemia).

### 10.9 Fates of amino acid carbon skeletons {#ch10-9}

The 20 amino acids' catabolic pathways converge onto just **six major
products**: **pyruvate, acetyl-CoA, alpha-ketoglutarate, succinyl-CoA,
fumarate, and oxaloacetate** — all of which enter the citric acid cycle,
from where they can be diverted to gluconeogenesis, to ketogenesis, or
completely oxidized to CO2 and H2O.

- **Glucogenic amino acids** — convert to glucose (via one of the TCA-cycle/
  pyruvate entry points; full list already given as Table 14-4 in Chapter 7,
  §7.3).
- **Ketogenic amino acids** — convert to ketone bodies (entering via
  acetyl-CoA or acetoacetyl-CoA).
- **Leucine and lysine** are the only two amino acids that are **exclusively
  ketogenic** (see also Chapter 7, §7.3's note on the same two amino acids
  being unable to furnish carbon for *net* glucose synthesis).
- Several amino acids are **both** glucogenic and ketogenic (isoleucine,
  phenylalanine, threonine, tryptophan, tyrosine — visible on the combined
  entry-point diagram as appearing in both an oxaloacetate/TCA-intermediate
  glucogenic box and the acetoacetyl-CoA ketogenic box).

---
