# Metabolic Biochemistry Lab — Source

Separate from [source.md](source.md) (the lecture spine) so a lab citation can never be
confused with a lecture one — anchors here use `{#labNN}`, never `{#chNN}`.

Base document: `slides/lab/metabolicmanual.pdf`, *Biochemistry Laboratory Manual*, 2022-2023,
Al-Quds University Faculty of Medicine, Department of Biochemistry & Molecular Biology,
prepared by Dr. Kifaya Azmi, Dr. Rula Abdul-Ghani, and Dr. Suheir Ereqat — the official
lab document. It has zero extractable text layer (a scan; its `.docx` twin has zero text
too, confirmed via python-docx before committing to a full vision read), so all 112 pages
were rendered and read directly (vision), not OCR'd — there is no OCR tool on this
machine. The manual's own 11-session numbering and titles are used as this file's chapter
structure.

Supplementary decks, layered in where they add real detail beyond the manual (noted per
chapter): `slides/lab/Slides/2024 slides/Lab #1/` through `Lab #5/` (PDFs and PPTX, the
2024 cohort's own session slides) and `Manual cases.pptx` (the session-11 case-discussion
deck). Spot-checking multiple sessions found the manual and the 2024 slides share large
verbatim passages — the slides were evidently built from the manual's own text — so the
slides were read first (free, text-layer/pptx-text) and the manual's vision pages were
then used to confirm each session and add whatever the slides omitted, abbreviated, or
illustrated only as a diagram (worked reaction schemes, a fuller safety-poster rule set,
exact reference-value tables, buffer-preparation recipes). Not read: `Lab Reports/` (a
blank report template, no content); `Slides/Previous Slides/` (prior-year decks —
gap-filler only, same category as the main course's own `previous-slides/`); `Summaries/`
(student transcriptions of the lectures, including two Arabic-language files — reference
material for Job C, not primary Job B input, same category as the main course's
`_reference/`). The manual's own back matter — reagent-kit manufacturer pamphlets
(pp. ~74–111: Acid Phosphatase, Bilirubin D+T, and others; boilerplate procedure codes,
storage conditions, catalog numbers) and the DNA-extraction kit's own reagent-volume chart
(p. 112) — was skimmed for reference-value tables worth keeping but not transcribed in
full; those pamphlets are manufacturer inserts, not instructor content, and their
procedural boilerplate isn't the kind of thing a question bank draws on.

**Session 11's own content is three full published case reports**, reproduced in the
manual as unpaginated inserts between Session 10 and the kit-pamphlet appendix: Song et
al. (Wilson's disease via LFT pattern, case report), a PIEZO1/HbA1c case report
(*Frontiers in Endocrinology*, 2020), and a hypertriglyceridemia case report (*Journal of
Tropical Biomedicine*, 2011). `Manual cases.pptx` is the instructor's own lecture
walk-through of these three papers, built around the same clinical-reasoning questions
the manual's own case discussions raise — read as the primary source for Lab 11, with a
handful of specific lab values pulled from the full papers where the slide deck only
summarized them.

**Source note:** two specific numeric discrepancies were found between the manual/slides
and the embedded published papers, and are flagged rather than silently resolved, per the
project's fidelity rule: (1) the DNA-extraction kit is named "MasterPure™ ... Version I"
in the 2024 slides' Lab #4 but "Version II" on the manual's own kit-contents page (p. 53) —
both are given as stated; (2) the LDL/VLDL calculation is given as VLDL = TG/5 (Session 7,
manual p. 51, the standard Friedewald constant for mg/dL) but the Case III paper itself
computes LDL = TC − (TG/3) − HDL (p. 85) — both formulas are reproduced as their own
sources state them, not reconciled.

---

## Lab sessions

1. [Safety Rules and Basic Measurements](#lab01)
2. [Spectrophotometry and Beer's Law](#lab02)
3. [Measurement of Plasma Enzymes — Alkaline and Acid Phosphatase](#lab03)
4. [Liver Function Tests](#lab04)
5. [Glucose and Total Protein](#lab05)
6. [Kidney Function Tests](#lab06)
7. [Lipoproteins and Lipids](#lab07)
8. [DNA Extraction](#lab08)
9. [Polymerase Chain Reaction (PCR)](#lab09)
10. [Agarose Gel Electrophoresis](#lab10)
11. [Selected Clinical Cases](#lab11)

---

## Lab 1 — Safety Rules and Basic Measurements {#lab01}

> **Source:** manual pp. 3–17 (Introduction, Lab objectives, Sessions 1-A/B/C);
> `Slides/2024 slides/Lab #1/Lab Safety Rules and Guidelines DR.pptx` (40 slides).

### Introduction and lab objectives

This lab course introduces undergraduate students to biochemistry-lab techniques and
biological-sample handling for clinically relevant biochemical parameters, using ten
experiments covering basic calculations, spectrophotometric principles, enzyme kinetics,
liver function tests, carbohydrate metabolism, kidney function tests, lipid profile, and
molecular methods — with clinical significance and interpretation of results emphasized
throughout. Lab reports (short essay questions interpreting results in clinical context)
are a graded component (20% of the course mark). Six stated objectives: introduce basic
clinical biochemistry; use simple protocols/available materials to understand biochemical
substances; teach independent lab work; stimulate a research mindset; train patience,
accuracy, and teamwork toward good data; and train discussing results with colleagues to
reach the right conclusion.

### General laboratory safety rules

Two major concerns when working in a biochemistry laboratory: **safety** and
**efficiency**. All students must read and understand the general laboratory safety
rules before the first session.

**A. Personal protective equipment (PPE)** — equipment used to prevent/minimize exposure
to hazards. The four most important: **lab coats, footwear, gloves, eyewear**.
- Never wear lab coats, gloves, or other PPE outside laboratory areas.
- **Footwear**: shoes must have a nonslip sole firmly attached to the foot; sandals,
  sneakers, and open-toed shoes do not adequately protect against falling heavy objects.
- **Gloves**: required to protect hands from chemical, physical, or biological hazards
  entering through the skin; should be polyvinyl or another non-latex material (an
  acceptable alternative for people with latex allergies).
- **Eyewear**: safety goggles are the best protection against chemical splashes, mists,
  vapors, and dusts, and must be worn whenever projectile objects are in use. Contact
  lenses do not offer eye protection and are strongly discouraged in the lab — if worn,
  eye-cup safety goggles should be used over them. Ultraviolet-absorbing protective
  glasses should be worn when working with UV light.

**B. Chemical safety** (17-item numbered list; items 1–13 also appear, in briefer form,
on the 2024 slides):
1. Mouth pipetting is never allowed — use only a rubber bulb or automated micropipette.
2. Hair must be tied back.
3. Do not wear jewelry or loose/baggy clothing.
4. Never touch, taste, or smell a chemical unless instructed to.
5. Don't mix chemicals unless instructed to.
6. Keep lids on chemical containers when not in use.
7. Never place pencils, pens, or other materials in your mouth.
8. Don't eat or drink in the laboratory; never use glassware as food/water containers.
9. Use fume hoods when toxic or irritating vapors are involved.
10. Do not engage in laboratory practical jokes or horseplay.
11. Keep nonessential books and clothing away from your work area.
12. Report all accidents, including minor ones, to your instructor immediately.
13. Do not perform unauthorized experiments, and never work alone in the laboratory.
14. Before obtaining any chemical, carefully read the label on the reagent bottle.
15. Protect your hands: wash them after every lab session, and handle glassware, sharp
    tools, and heated containers carefully.

**General laboratory safety rules poster** (manual p. 9; a separate summary infographic,
not fully duplicated in the numbered list above): follow instructions and get questions
answered before starting; be attentive (never leave a lit Bunsen burner unattended or
leave an experiment in progress; do not place inflammable substances nearby); keep a
clean workplace (use provided detergents before/after use); treat everything as a
hazardous source — label bottles before beginning, report accidental exposure to
hazardous materials immediately; be responsible in the lab (never randomly mix chemicals
or deviate from protocol — this could cause fire, explosion, or toxic fumes); clean up
after completing the lab and wash your hands; never taste or sniff chemicals or
biological cultures (the safest way to know a container's contents is its label); do not
eat, drink, smoke, apply cosmetics, or chew gum in the lab; **do not use a mobile phone
inside the lab**; dress appropriately (goggles, a clean tidy lab coat with buttons
fastened, gloves); leave experiment materials and specimens at the lab — in some cases
lab notebooks must stay in the lab too; before entry, leave unnecessary materials
(bags, heavy jackets/coats, removable hats and books, excluding the lab manual) on the
coat hooks and the special bench near the entrance; know the location of emergency
numbers and exits, and be aware of key safety signs.

### Basic biochemistry laboratory equipment

A biochemistry lab includes work benches with equipment (spectrophotometers,
microscope, balances, electrophoresis equipment...) plus tools to manipulate samples.

**1. Centrifuge** — separates fluids/gases/liquids into sub-fractions by density,
viscosity, shape, and size, using centripetal force to drive denser material toward the
tube bottom faster than gravity alone would. **Centrifugation** is the general process of
using centrifugal force to sediment heterogeneous mixtures — denser components migrate
away from the rotation axis, less-dense components toward it. Three basic parts: **rotor,
drive shaft, motor** (the motor turns the rotor via the drive shaft; a larger rotor has a
slower maximum speed).
- **Microfuge (microcentrifuge)** — smallest type; spins 1–2 mL tubes up to
  12,000–13,000 rpm; very small, light rotors.
- **Large super-speed centrifuge** — ~20,000 rpm, various tube sizes by rotor; suited to
  producing viruses, vaccines, gamma globulin, and prothrombin.
- **Refrigerated centrifuge** — maintains a steady temperature (−20 to −40 °C) at
  maximum speed; suited to DNA, RNA, PCR, and antibody work.
- **Ultracentrifuge** — up to 1,000,000 g; exploits tiny density differences between
  molecules like proteins and nucleic acids. Two types: **preparative** (separates
  particles by density, isolates macromolecules/lipoproteins from plasma, deproteinizes
  physiological fluids for amino-acid studies; different rotors spin many samples at
  different angles/speeds) and **analytical** (a light-based optical detection system
  gives real-time monitoring of the sedimentation process as it happens; smaller sample
  volumes, precise analysis rather than bulk processing).

**2. Analytical balance** — highly sensitive, readability 0.1–0.01 mg; has a draft
shield/weighing chamber to keep air currents from disturbing tiny samples. Works on the
"magnetic force restoration" principle — an electromagnetic balance that measures the
downward force on the pan (via an electromagnet) rather than mass directly.

**3. Spectrophotometer** — measures light absorption/transmission across wavelengths;
different molecules absorb specific wavelengths, giving information on concentration,
purity, and chemical composition (full detail in Lab 2).

**4. pH meter** — measures a fluid's acidity/alkalinity via the electrical potential
difference between a pH electrode and a reference electrode, displayed as a pH value.
Working principle: the meter measures voltage between two electrodes and converts it to
pH. The glass (or combination) electrode and reference electrode are immersed in the test
solution; H⁺ ions in the solution exchange with other positive ions on the glass bulb; an
amplifier detects the resulting potential difference between the electrodes and converts
it to a pH unit.

**5. Pipette** — measures and transfers precise liquid volumes via a narrow tube with a
volume indicator and tapered tip, dispensing by vacuum or mechanical action.
- **Automatic micropipette** — accurate/precise for small volumes (glass pipettes are not
  reliable below 1 mL); each pipette is set within its own specified volume range.
  Choose the pipette whose capacity is closest to, but greater than, the desired volume.
- **Three plunger positions**: Position 1 = pipette at rest; Position 2 (first stop) =
  reached by pressing the plunger down to first resistance; Position 3 (second stop) =
  reached by pressing further from position 2 (used to fully expel the last of the
  sample).
- **Stepwise operation**: (1) select the proper pipette and set the volume by rotating
  the adjustment knob to the desired digital reading; (2) pre-wet the tip at least 3
  times; (3) work at temperature equilibrium; (4) examine the tip before and after
  dispensing; (5) attach the correct tip; (6) press the plunger to the first stop; (7)
  immerse to the proper depth; (8) draw up the sample; (9) dispense the sample and
  withdraw the tip; (10) withdraw the pipette and release the plunger; (11) discard the
  tip.
- **Guidelines for optimal reproducibility**: consistent speed/smoothness pressing and
  releasing the plunger; consistent pressure at the first stop; consistent, sufficient
  immersion depth; near-vertical pipette positioning; avoid all air bubbles.

### Phlebotomy

**Phlebotomy** (Greek *phleb-* "vein" + *-tomia* "cutting") — inserting a needle into a
vein to draw blood for testing. **17-step standard procedure**:
1. Confirm the patient's identity matches the paperwork.
2. Check the ordered tests and samples (prevents administrative errors).
3. Bring supplies to the patient (syringe, needles, cotton, 70% alcohol, tubes,
   tourniquet); remove equipment from packaging.
4. Wash hands and put on gloves.
5. Choose the draw arm and tie the tourniquet (prolonged tourniquet time can injure the
   patient).
6. Find a suitable palpable vein. Top three sites: **median cubital vein** (most common),
   **cephalic vein** (a safe secondary option, along the upper arm to the thumb), and
   **basilic vein** (last resort — not as close to the skin surface, greater risk of
   damage to the median nerve and brachial artery).
7. Disinfect the puncture site with an alcohol wipe.
8. Wipe the area with sterile cotton gauze.
9. Anchor the vein with your thumb ~2 cm below the puncture site; insert the needle at
   15°.
10. If blood appears in the syringe hub, slowly and gently pull back on the plunger.
11. Untie the tourniquet.
12. Remove the needle and firmly place cotton gauze on the puncture site.
13. Unload the blood into the tube; invert 5–10 times to mix.
14. Label all tubes with the patient's name, date of birth, and other essential
    identifiers.
15. Once bleeding stops, apply a bandage over the wound.
16. Dispose of all trash and medical waste properly.
17. Check in with the patient for lightheadedness/illness; offer water or a light snack
    and let them rest if needed.

---

## Lab 2 — Spectrophotometry and Beer's Law {#lab02}

> **Source:** manual pp. 18–24; `Slides/2024 slides/Lab #1/Spectrophotometer and Beer's
> law done WITH EXPERIMENTSs.pptx` (30 slides).

**Spectrophotometer** — measures the light absorbed or transmitted by a substance across
wavelengths, giving information about composition and concentration. **Spectrophotometry**
is the corresponding technique; one of the principal methods of biochemical analysis, used
in DNA/RNA/protein isolation, enzyme kinetics, and general biochemical analysis.

**Main components:**
- **Light source** — a stable source spanning a broad wavelength range.
- **Monochromator** — selects specific wavelengths to pass to the sample.
- **Sample compartment** — holds the cuvette; the sample interacts with the light here.
- **Detector** — measures the intensity of light passing through the sample.
- **Signal processor** — converts the detector's electrical signal to a measurable output.
- **Display and controls** — sets parameters (wavelength, mode) and shows results.
- **Data output** — exports measurement data to computers/printers.

**Classification by wavelength:**
1. **Visible spectrophotometer** — 400–700 nm; accuracy varies; plastic or glass cuvettes.
2. **UV spectrophotometer** — 180–400 nm; used for fluids and solids; only quartz
   cuvettes (glass/plastic absorb UV).
3. **IR spectrophotometer** — 700–15,000 nm.

**Seven types by application/technology** (manual only, not in the slides): **visible
light** (routine work, tungsten lamp); **UV/Visible** (a visible unit converted with a
second lamp, up to 1100 nm, with scanning, integral printer, multi-cell settings);
**near-infrared** (non-invasive, minimal sample prep; useful for fat, protein, fiber,
starch content in highly absorbing solids); **nuclear magnetic resonance (NMR)
spectroscopy** (determines organic-compound structure and reaction dynamics — a
structural, not concentration, tool); **atomic absorption spectrophotometer** (a flame
evaporates and dissociates the sample into ions, changing light intensity at the
detector; high-precision, used in toxicology/environmental/QC labs); **mercury
spectrophotometer/analyzer** (instantly measures trace mercury in water); **fluorometer**
(measures fluorescence released after exposure to a single wavelength).

**Cuvettes** — three types in routine use: **blank** (solvent/reference only, no
analyte — a baseline correcting for background noise/light-source fluctuation),
**sample/test** (contains the analyte), and **standard** (a solution of known
concentration/optical properties, used to calibrate and verify instrument performance).
**Care of cuvettes**: clean and dry before use; handle only at the top (avoid fingerprint/
dirt contamination of optical surfaces); wipe gently with soft tissue before inserting;
ensure no air bubbles adhere to the inner surface after filling; store in wooden or
plastic-coated racks; wash with soap, rinse with tap water, then rinse 3× with distilled
water before use.

**Measurement principle** — the compound is placed in a cuvette in the spectrophotometer;
light of a chosen wavelength passes through, and the transmitted (Transmittance) or
absorbed (Absorbance) amount is measured. Because other compounds (or the solvent) may
absorb the same wavelengths as the analyte, the sample's absorbance is compared to a
**reference blank** — everything in the sample solution *except* the substance being
measured. Light intensity before the sample is I₀ (photons/second); the blank, containing
no analyte, does not absorb light and defines the reference.

Since the reference blank has no analyte, its transmittance is defined as **100% T**.
- **Transmittance**: T = I / I₀; **%T** = (I / I₀) × 100.
- Since some light is absorbed by the test compound, its %T is lower than the blank's
  (100% by definition).
- **Absorbance (A)**, also called Optical Density (OD) — the preferred measure for most
  biological applications — relates to transmittance logarithmically: **A = −log T**.
- Using It (intensity after the cuvette) and I₀ (intensity before): **T = It / I₀**.
  Biologists measure absorption rather than transmission because of this relationship;
  the Beer-Lambert law can then compute a solution's concentration if its extinction
  coefficient is known.

**Beer–Lambert's law:**
- **Beer's law** — absorbance is directly proportional to the concentration of the
  absorbing material.
- **Lambert's law** — absorbance is directly proportional to the path length of the
  sample cell (cuvette).
- **Beer–Lambert's law** (combined) — A = εCL, where **A** = absorbance, **C** =
  concentration, **L** = cuvette path length (ε = the extinction/molar absorptivity
  coefficient, implicit in the relationship).

**Applications of spectrophotometry**: qualitative analysis (identifying compound classes
in biological or pure samples); quantitative analysis (determining unknown concentration
via absorption spectrometry — e.g., nucleic acid content of a protein sample); **enzyme
assay is the primary use of spectrophotometry**; identifying molecular weight of samples
such as amine picrates, ketones, aldehydes, and sugars.

**Experiment — Part A** (Objective: determine A_max of four dyes — malachite green,
safranine, iodine, crystal violet): read each colored solution's absorbance starting at
the low end of the assigned range (380–730 nm), repeating every 50 nm across the range;
re-zero the spectrophotometer against the blank at every wavelength change.

**Experiment — Part B** (Objective: see the effect of concentration on absorbance): make
serial dilutions of a colored solution, measure absorbance for each, and plot absorbance
vs. concentration (cuvette path length 1.00 cm) to see the linear Beer's-law relationship
directly.

---

## Lab 3 — Measurement of Plasma Enzymes: Alkaline and Acid Phosphatase {#lab03}

> **Source:** manual pp. 25–29; `Slides/2024 slides/Lab #2/lab 2.pdf` pp. 6–30
> ("BIOCHEMISTRY LAB SESSION 3").

**Enzymes** are proteins acting as biological catalysts, accelerating reactions by
lowering activation energy; the molecules they act on are substrates, the products are
what they're converted to. Virtually every intracellular reaction needs enzyme
catalysis, since most reactions don't proceed at a detectable rate under physiological
pH/temperature/ionic conditions; metabolic pathways depend on enzymes for each step.

**Plasma enzymes are of two types**: those normally present with a functional plasma
role, and those released from tissues with no functional plasma role but diagnostic
value. Normally, intracellular-enzyme content in plasma is low or absent; when cells are
damaged, that content appears in blood. A disease process altering cell-membrane
permeability or increasing cell death releases intracellular enzymes — analyzing blood
for these cellular components gives clinicians a convenient way to evaluate damage to
specific tissues.

### Alkaline phosphatase (ALP, EC 3.1.3.1)

A non-specific phosphomonoester hydrolase catalyzing hydrolysis of a wide variety of
organic monophosphates. Possible functions beyond phosphoester hydrolysis: phosphate
transferase activity, protein phosphatase activity, phosphate transport modulation, and
involvement in cell proliferation. In general, phosphatases transfer a phosphate group
from one compound to a second, forming an alcohol plus a second phosphate compound; when
water is the phosphate acceptor, inorganic orthophosphate results.

**Principle**: serum ALP hydrolyzes p-nitrophenyl phosphate to p-nitrophenol (yellow) +
phosphate; the rate of p-nitrophenol liberation is proportional to ALP activity and is
measured photometrically. Optimal activity at pH ~10.4; ALP requires **magnesium and
zinc ions** for stability and maximal activity.

**Tissue distribution**: small intestine, liver, bone, kidney, placenta.

**Causes of increased plasma ALP:**
- *Physiological*: pregnancy (last trimester), childhood.
- *Pathological* (often 5× the upper normal limit): two disease groups — those affecting
  liver function, and those involving osteoblastic bone activity. In hepatic disease, a
  rise in ALP activity generally indicates **biliary obstruction**.
- Also raised in: primary hyperparathyroidism; secondary hyperparathyroidism from
  chronic renal disease; rickets and osteitis deformans juvenilia from vitamin D
  deficiency, malabsorption, or renal tubular dystrophies; Von Recklinghausen's disease
  with bone involvement; malignant bone infiltrations.

**Causes of decreased plasma ALP**: hyperthyroidism; the rare condition idiopathic
hypophosphatasia (associated with rickets and excess urinary phosphatidylethanolamine);
vitamin C deficiency; cretinism.

**Specimens for enzyme testing generally**: serum or heparinized plasma, free of
hemolysis, separated from the clot. Complexing anticoagulants (citrate, oxalate, EDTA)
must be avoided. Fresh samples should be assayed within 4 hours of collection (kept at
room temperature) or refrigerated if necessary — **freezing causes loss of activity**.

**Reading a reagent pamphlet**: every kit includes a leaflet/pamphlet stating what it is,
its uses, and how to read/use it — always consult it.

### Acid phosphatase (ACP, EC 3.1.3.2)

A hydrolase-class enzyme acting in acidic medium, cleaving phosphate groups from other
molecules during digestion. Found in lysosomes, becoming active after fusing with
endosomes (which acidifies the local pH, creating ACP's optimal environment). Found
throughout the body — primarily in the **prostate gland**, and in smaller amounts in
bone, spleen, liver, kidney, blood, stomach, muscle, erythrocytes, and platelets. **Not a
screening test for prostate cancer** on its own, though the highest ACP levels occur in
metastasized prostate cancer; largely superseded by **prostate-specific antigen (PSA)**.

**Principle (modified Hillmann method)**: ACP hydrolyzes α-naphthylphosphate to
α-naphthol, which reacts immediately with Fast Red TR to form a dye measured at 405 nm;
the rate of absorbance increase is proportional to ACP activity. **Tartrate** is used as
a prostatic-fraction-specific inhibitor: adding L-tartrate inhibits prostatic ACP
specifically while all other serum ACP still reacts, so the assay is run both with and
without L-tartrate — the activity difference equals the serum's prostatic ACP activity.

**Elevated prostatic ACP** is also found in: bone diseases (e.g., Paget's disease); blood
diseases (sickle cell disease, multiple myeloma) or lysosomal disorders (Gaucher's
disease); it also serves as a cytogenetic marker distinguishing the two lineages of Acute
Lymphoblastic Leukemia — **B-ALL is ACP-negative, T-ALL is ACP-positive**. Decreased
serum ACP has no clinical significance. As always, clinical diagnosis should never rest
on a single test result; it must integrate clinical and other laboratory data.

**Samples/reagents**: serum or plasma, clear and unhemolyzed, separated from the clot
promptly. ACP is very labile — stabilize by adding 40 µL acetic acid (R.4) per mL of
sample; stable 7 days at 2–8 °C. Two reagent methods provided: for TOTAL ACP, and for
PROSTATIC ACP.

**Reference values (37 °C)**: Total ACP — men up to 5.4 U/L, women up to 4.2 U/L.
Prostatic ACP — up to 1.7 U/L.

**Calculations**: Total ACP activity (U/L) = 743 × ΔAbs/min (sample, without tartrate).
Non-prostatic ACP activity (U/L) = 743 × ΔAbs/min (sample, with tartrate). Prostatic ACP
= Total ACP (without tartrate) − Non-prostatic ACP (with tartrate).

---

## Lab 4 — Liver Function Tests {#lab04}

> **Source:** manual pp. 30–37; `Slides/2024 slides/Lab #2/lab 2.pdf` pp. 31–60
> ("BIOCHEMISTRY LAB SESSION 4").

**Liver function tests (LFTs)** — a "liver panel" of blood tests measuring various
liver-made enzymes, proteins, and substances on a single sample, often including AST,
ALT, ALP, GGT (gamma-glutamyltransferase), serum albumin, protein, and bilirubin.
Classified as: (a) tests of hepatic *excretion* (direct/indirect bilirubin); (b)
evaluation of hepatic *synthesis* (albumin, prothrombin time, platelet count, glucose);
(c) evaluation of *enzyme activity* (AST, ALT, ALP, GGT). LFTs are most often used to:
diagnose liver disease presence and type; assess disease extent/progression (e.g., how
badly damaged/scarred by disease such as cirrhosis); and monitor medication side effects.
Note: liver-disease diagnosis rests on a complete history, physical exam, LFTs, and
further invasive/noninvasive testing together.

### Transaminases: AST and ALT

**Transaminases (aminotransferases)** catalyze a transamination reaction between an
amino acid and an α-keto acid: the NH₂ group of one molecule exchanges with the =O group
of the other — the amino acid becomes a keto acid, and the keto acid becomes an amino
acid (general scheme, manual p. 30: two amino acid/keto acid pairs, R¹ and R², exchange
amino/keto groups via transaminase, reversibly). Most often used to: help diagnose liver
disease (e.g., hepatitis); monitor treatment; assess damage/scarring severity (e.g.,
cirrhosis); monitor medication side effects.

**AST (aspartate aminotransferase)**, also called serum glutamate-oxaloacetate
transaminase (SGOT), participates in gluconeogenesis and is present in liver, muscle,
heart, kidney, brain, pancreas, and erythrocytes — **but not in bone**. Two isoforms:
cytoplasmic (AST1, released during *moderate* cell damage) and mitochondrial (AST2,
blood activity rises during *severe* cell damage). AST relies on **PLP (vitamin B6)** as
a cofactor to transfer the amino group from aspartate or glutamate to the corresponding
keto acid.

**ALT (alanine aminotransferase)**, formerly SGPT, is found mainly in the **liver**;
high ALT signals liver damage from hepatitis, infection, cirrhosis, liver cancer, or
other liver disease. Because AST is expressed in other tissues too, **AST is a less
specific liver-injury marker than ALT**. Both assays: the rate of *decrease* in
absorbance at 340 nm is proportional to enzyme activity.

**Clinical interpretation**:
- History should always cover drug history, alcohol use, viral exposure; combine with
  physical exam and lab pattern (are levels in the thousands? what's the AST/ALT ratio?).
- **Levels in the thousands** suggest: hepatotoxic drugs (e.g., acetaminophen);
  autoimmune hepatitis; ischemic injury (Budd-Chiari or congestion); acute viral
  hepatitis.
- **AST/ALT ratio < 1** (AST < ALT): uncomplicated viral hepatitis; minor fatty liver
  disease; extrahepatic cholestasis.
- **AST/ALT ratio > 1**: alcoholic hepatitis (typically ratio > 2; AST usually ≤ 500 U/L
  in alcoholic hepatitis); fulminant/necrotic hepatitis; decompensated cirrhosis (ratio
  rises as fibrosis advances); hepatocellular carcinoma or liver metastases; muscle
  damage; myocardial infarction.

### Bilirubin (total and direct)

**Bilirubin** is a red-orange compound from the normal catabolic breakdown of heme in
vertebrates — very hydrophobic, transported to the liver bound to albumin, then through
the gallbladder and digestive tract before excretion, conjugated with glucuronic acid and
secreted in bile. This clears waste from destruction of aged/abnormal red blood cells: in
the first step, heme is stripped from hemoglobin, then undergoes region-dependent
porphyrin catabolism. Structurally, bilirubin is an open-chain tetrapyrrole formed by
oxidative cleavage of heme's porphyrin ring, giving biliverdin; biliverdin is reduced to
bilirubin, which is excreted after glucuronic-acid conjugation.

**Conjugation**: in the liver, **glucuronyltransferase** conjugates bilirubin with
glucuronic acid, first to bilirubin glucuronide, then to bilirubin diglucuronide, making
it water-soluble — this conjugated form is the main species in the "direct" bilirubin
fraction, mostly excreted via bile into the small intestine. Unconjugated bilirubin is
"indirect" bilirubin. **Total serum bilirubin = direct + indirect.** High bilirubin can
result from infections, inherited disease, liver disease, bile-duct blockage, sickle
cell disease, or certain medications.

**Three-phase pathophysiology of jaundice** (manual detail beyond the slides):
- **Prehepatic (production)**: bilirubin is the end product of heme released from
  senescent/defective RBCs; in reticuloendothelial cells of the spleen, liver, and bone
  marrow, heme undergoes: Heme → Biliverdin → Bilirubin (insoluble, tight hydrogen
  bonding).
- **Hepatic**: (1) *hepatocellular uptake* — unconjugated (non-soluble) bilirubin,
  transported bound to albumin, has the albumin–bilirubin bond broken and is taken alone
  into hepatocytes via carrier-mediated transport, then bound to cytosolic proteins to
  limit efflux back to plasma; (2) *conjugation* — in the endoplasmic reticulum,
  unconjugated bilirubin is conjugated to glucuronic acid (soluble in bile) by
  **UDP-glucuronosyl transferase**.
- **Posthepatic**: (1) *bile secretion* — conjugated bilirubin is released into bile
  canaliculi → bile ducts → gallbladder → ampulla of Vater → colon; (2) *intestinal
  metabolism and renal transport* — intestinal mucosa cannot reabsorb conjugated
  bilirubin (too hydrophilic, too large); colonic bacteria deconjugate and metabolize it
  to **urobilinogens**, 80% of which is excreted in feces as **stercobilin**, and the
  remaining 10–20% undergoes enterohepatic circulation; some urobilins are excreted via
  the kidneys, giving urine its yellow pigment.
- **Diagnostic logic**: prehepatic dysfunction → elevated **unconjugated** bilirubin;
  posthepatic insult → elevated **conjugated** bilirubin; hepatic-phase impairment can
  elevate **both**.

Bilirubin circulates as **indirect (unconjugated)** and **direct (conjugated)** forms.
Total and direct bilirubin are measured directly; indirect is derived (total − direct).
Blood/serum tubes for bilirubin assay must be protected from light (bilirubin degrades
under illumination). Adult samples: venous needle draw. Newborns: heel-stick (a small
sharp blade cuts the infant's heel to collect a few drops).

**Principle**: total bilirubin is determined by reaction with diazotized sulphanilic
acid in the presence of caffeine, forming an azopigment; the same reaction without
caffeine measures direct bilirubin alone. The derivative's color is pH-dependent — pink
in acid/neutral medium, blue under alkaline conditions.
- **Direct (conjugated) bilirubin** + diazotized sulfanilic acid (p-diazobenzenesulfonic
  acid) → blue azobilirubin, at alkaline pH.
- **Indirect (unconjugated) bilirubin** is diazotized only in the presence of an
  "accelerating agent" (a caffeine-benzoate-acetate mixture). So the blue azobilirubin
  produced *with* the accelerating agent comes from both direct and indirect fractions,
  reflecting **total** bilirubin: Total bilirubin + caffeine-benzoate-acetate mixture +
  diazotized sulfanilic acid → azobilirubin.

**Reference values** (BILIRUBIN D+T liquicolor kit, modified Jendrassik/Gróf method,
manual back matter): Total bilirubin — at birth up to 5 mg/dL (85.5 µmol/L); 5 days up to
12 mg/dL (205 µmol/L); 1 month up to 1.5 mg/dL (25.6 µmol/L); adults up to 1.1 mg/dL
(18.8 µmol/L). Direct bilirubin — adults up to 0.25 mg/dL (4.3 µmol/L).

**Clinical notes**: if the liver is failing, bilirubin rises. **Hyperbilirubinemia** =
raised blood bilirubin; **jaundice** = yellowish discoloration of sclera/skin — not all
hyperbilirubinemia is jaundice, and not all jaundice is hyperbilirubinemia.
**Cholestasis** = impaired production, secretion, or outflow of bile. Jaundice is
classified as prehepatic, hepatic, or posthepatic (mechanism above). Liver injuries can
present as a **hepatocellular pattern** or a **cholestatic pattern**.

---

## Lab 5 — Glucose and Total Protein {#lab05}

> **Source:** manual pp. 38–42; `Slides/2024 slides/Lab #3/LAB 3.pdf` pp. 1–20
> ("Biochemistry lab session 5").

### Plasma proteins

The largest solute fraction of blood is **total protein**, collectively **albumin** and
**globulin**. **Albumin** (made in the liver) keeps fluid from leaking out of blood
vessels and helps move hormones, medicines, vitamins, and other substances throughout the
body. **Globulins** help fight infection and move nutrients — some are liver-made, others
made by the immune system.

**Functions of serum proteins**: (1) part of the body's amino-acid pool; (2) can be
deaminated to ketoacids for caloric energy; (3) can be transformed into carbohydrates and
lipids; (4) act as transport agents for metabolites, metal ions, carbohydrates, lipids;
(5) enzymes, antibodies, and certain hormones are themselves proteins; (6) maintain blood
osmotic pressure and pH; (7) liver-produced fibrinogen and prothrombin are central to
coagulation.

**When to order a total protein test**: unexplained weight loss; fatigue; edema; symptoms
of kidney or liver disease.

**Increased protein concentration**: dehydration (vomiting/diarrhea — affects all
fractions equally); multiple myeloma and related diseases (one fraction, usually gamma,
greatly increased). **Decreased protein concentration**: malnutrition; nephrotic
syndrome; kidney damage; extensive bleeding; liver damage; inadequate intake; deficient
GI absorption.

**Albumin/globulin (A/G) ratio**: normally slightly above 1. A **low** ratio (low
albumin or high globulin) suggests autoimmune disease, multiple myeloma, cirrhosis, or
kidney disease. A **high** ratio can indicate genetic deficiencies or leukemia.

### Biuret test (protein determination)

A chemical test for peptide bonds: a peptide structure with at least two peptide links
produces a violet color when treated with alkaline copper sulfate (the biuret reaction).
In alkaline solution, blue Cu²⁺ ions complex with the peptide bond (unshared electron
pairs on nitrogen/oxygen), forming a coordination complex between Cu²⁺ and the carbonyl
oxygen (>C=O) and amide nitrogen (=NH) of the peptide bond — once formed, the solution
turns from blue to purple; deeper purple = more peptide–copper complexes. The reaction
occurs with any compound bearing at least two H₂N–C, H₂N–CH₂–, H₂N–CS–, or similar groups
linked directly or via a carbon/nitrogen atom. One copper ion links to roughly 6 nearby
peptide linkages by coordinate bonds; color intensity is proportional both to the number
of peptide bonds per reacting protein molecule and to the number of protein molecules
present. **Biuret reagent** = NaOH or KOH (alkaline medium) + hydrated copper(II) sulfate
+ potassium sodium tartrate (chelates/stabilizes the cupric ions, keeping them soluble in
alkaline solution). Reaction diagram (manual p. 40): a peptide chain reacts with Cu²⁺
(blue) to form a deep-purple peptide–copper complex.

**Principle for total protein measurement**: in alkaline solution, proteins form a
highly stable, spectrophotometrically measurable colored complex with copper ions,
proportional to protein concentration.

### Blood glucose determination

**Biomedical significance**: blood/plasma glucose level. Glucose is a major energy source
for most cells, including the brain; carbohydrates are rapidly converted to glucose.
Blood glucose is regulated antagonistically by **insulin and glucagon**, secreted by the
pancreatic islet cells (pancreatic endocrine hormones). Levels shift with body
composition, age, physical activity, and sex.

**Principle — glucose oxidase method**: glucose oxidase is highly specific for glucose
(does not react with other blood saccharides), so it's used for blood glucose estimation.
It catalyzes oxidation of β-D-glucose to D-glucono-1,5-lactone, forming hydrogen peroxide;
the lactone slowly hydrolyzes to D-gluconic acid. The H₂O₂ produced is broken down by a
**peroxidase** enzyme to oxygen and water; the oxygen reacts with an oxygen acceptor
(e.g., o-toluidine), itself converted to a colored compound measurable colorimetrically.

**Clinical notes**: **hyperglycemia** is associated with diabetes and with hyperactivity
of the thyroid, pituitary, or adrenal gland. Diabetes involves abnormal blood-sugar
metabolism and defective insulin production, making blood glucose a key diabetes
parameter. **Hypoglycemia** is seen with insulin overdose, an insulin-secreting tumor,
Addison's disease, and other conditions interfering with glucose absorption.

**Plasma glucose parameters**:
- **Fasting blood sugar (FBS)** — glucose after >8 hours' fasting.
- **Random sample** — collected any time, no prior preparation.
- **Oral glucose tolerance test (OGTT)** — fasting glucose plus glucose 2 hours after a
  75 g glucose load.
- **Hemoglobin A1c (HbA1c)** — glycated hemoglobin, reflecting average blood glucose over
  the prior 8–12 weeks.

**Diabetes mellitus (DM) clinical note**: **Type 1** — no insulin; **Type 2** — insulin
resistance. Presentation: polyphagia, polydipsia, polyuria, weight loss. Treatment: Type
1 — give insulin; Type 2 — drugs to lower glucose, or insulin.

**Diagnostic criteria for DM**: random blood glucose ≥ 200 mg/dL in a patient with
hyperglycemia symptoms (polydipsia, polyuria, polyphagia, unexplained weight loss), OR
≥ 2 abnormal test results for hyperglycemia.

---

## Lab 6 — Kidney Function Tests {#lab06}

> **Source:** manual pp. 43–45; `Slides/2024 slides/Lab #3/LAB 3.pdf` pp. 21–37
> ("Biochemistry lab session 6").

**Kidney functions**: production of urine; excretion of metabolic waste and end-products
(urea, drugs); regulation of extracellular fluid volume/osmolality; acid-base balance;
electrolyte concentration maintenance; regulation of blood pressure/volume;
participation in gluconeogenesis (via glutamine/glutamate) and ketogenesis; hormone
synthesis (**erythropoietin, calciferol, prostaglandins, dopamine, renin**). Overall
process: filtration (glomerular filtration rate, GFR) → reabsorption → excretion.

**Kidney function test panel**:
I. **Creatinine** (predicts filtration — GFR).
II. **BUN** (can be reabsorbed — helps classify renal disease).
III. **Uric acid** (predicts excretion).
IV. Others — serum electrolytes (Na⁺/FeNa, K⁺, Ca²⁺, phosphate), vitamin D, parathyroid
hormone (PTH).

### I. Creatinine

The end product of creatine decomposition; daily urinary creatinine excretion is
individually constant, depending on muscle mass. Creatinine **cannot be reabsorbed** from
the primary urine, so excreted-creatinine measurement estimates renal filtration
capacity. Creatinine derives from creatine (a muscle component convertible to ATP);
creatinine production tracks muscle mass and stays fairly stable; excreted by the
kidneys. With progressive renal insufficiency, urea, creatinine, and uric acid are all
retained in blood.

**Principle — Jaffe reaction** (the most popular creatinine method): creatinine reacts
with picric acid under alkaline conditions, forming a yellow-orange complex. The Jaffe
reaction is **not specific** — proteins and other body-fluid substances interfere, and
their color is measured alongside creatinine's. Upon acidification, the creatinine-
derived color is destroyed while the nonspecific-substance color remains; the difference
in yellow-orange intensity (measured near 520 nm) before and after acidification is
proportional to creatinine concentration.

### II. Blood urea nitrogen (BUN)

**Urea** is the most abundant nitrogenous end product of protein catabolism, generated
in the liver and excreted by the kidney. It filters freely through the glomerulus into
the ultrafiltrate and diffuses passively back into blood as it passes down the renal
tubules; under normal flow, about 40% of filtered urea is reabsorbed — reduced flow rate
increases the fraction passively reabsorbed. **Blood urea** (total urea amount) is
distinct from **blood urea nitrogen** (the nitrogen content of that urea).

**Principle (colorimetric, slides)**: urease specifically hydrolyzes urea to ammonia and
CO₂; the ammonia ions react with a salicylate/hypochlorite/nitroprusside mixture to form
a blue-green dye (indophenol), whose intensity is proportional to urea concentration. A
BUN test requires no special fasting — normal eating/drinking beforehand ensures results
reflect usual levels.

**Principle (UV kinetic method, manual — a different assay principle for the same
analyte, both preserved)**: urease hydrolyzes urea to ammonia and CO₂ (Urea + H₂O
--urease--> 2 NH₃ + CO₂); the ammonia is then used by **glutamate dehydrogenase (GDH)**,
with NAD or NADP as cofactor, to reductively aminate α-ketoglutarate (α-KG) while
oxidizing NADH (NH₃ + α-KG + NADH(+H⁺) --GDH--> L-glutamate + NAD⁺). The UV absorbance at
340 nm **decreases** as NADH converts to NAD⁺, proportional to BUN concentration.

**Clinical note — kidney disease classification and BUN causes**: serum urea nitrogen
rises with impaired renal function. Elevated blood urea can result from: (1) **prerenal**
causes — dehydration, hypotension, renal artery stenosis, GI bleeding, shock, severe
burns, congestive heart failure or recent MI; (2) urinary tract obstruction (stones or
tumor); (3) certain medications (some antibiotics); (4) a high-protein diet (recall the
urea cycle's amino-acid-catabolism origin).

**BUN/Cr ratio**: > 20 → prerenal; < 15 → intrarenal; postrenal is diagnosed by imaging
(ultrasound).

### III. Uric acid

A product of purine nucleotide breakdown. High blood concentration (**hyperuricemia**)
can lead to **gout**. Causes: over-production of uric acid, or inadequate renal
clearance — further investigation distinguishes the two. Genetic inborn errors of purine
metabolism, metastatic cancer, multiple myeloma, leukemia, and cancer chemotherapy can
increase production; chronic renal disease, acidosis, toxemia of pregnancy, and
alcoholism can decrease excretion.

**Principle (uricase method)**: uricase catalyzes oxidation of urate to allantoin, H₂O₂,
and CO₂ (Uric acid + 2 H₂O + O₂ --uricase--> Allantoin + H₂O₂ + CO₂). The peroxide then
reacts, via peroxidase, with a chromogenic system to form a quinoneimine dye whose red
intensity is proportional to uric acid concentration, read photometrically (manual
equation: 2 H₂O₂ + DCHBS + PAP --peroxidase--> quinoneimine + HCl + 4 H₂O). Lipemic
samples generate turbidity that can falsely elevate results.

---

## Lab 7 — Lipoproteins and Lipids {#lab07}

> **Source:** manual pp. 46–51; `Slides/2024 slides/Lab #4/Lab 4.pdf` pp. 1–23
> ("Lab session 7").

**Biomedical significance**: cholesterol, triglycerides, and high-density lipoproteins
are key constituents of the body's lipid fraction. **Cholesterol** is an unsaturated
alcohol of the steroid family, essential for normal function of all animal cells and a
fundamental cell-membrane component. A **lipoprotein** is a biochemical assembly of
protein and bound lipid, letting fats move through the aqueous environment inside and
outside cells. Plasma lipoproteins separate (by hydrated density, electrophoretic
mobility, size, and cholesterol/triglyceride/protein content) into five major classes:
**chylomicrons, VLDL, IDL, LDL, HDL**. Their role: transporting triacylglycerols and
cholesterol in blood between tissues, chiefly liver and adipose tissue. The **liver** is
the central lipid-handling platform — hepatocytes store glycerol and fats, synthesize
triacylglycerols de novo, and produce bile from cholesterol.

Blood plasma lipoprotein determination reveals disorders of lipid metabolism (both hyper-
and hypolipidemias). "Good" and "bad" cholesterol colloquially (if imprecisely) refer to
**HDL** and **LDL** respectively: LDL carries cholesterol to where it's needed, but excess
LDL cholesterol tends to cling to arterial walls, depositing and forming plaques that lead
to **atherosclerosis**; high HDL appears protective, since it drives reverse cholesterol
transport back to the liver.

**Triglycerides (TG)** — lipid molecules of three fatty acid chains on a glycerol
backbone; a major energy-storage form (in adipose tissue) and a circulating bloodstream
lipid, also supplying fatty acids for membrane synthesis. Serum TG measurement matters in
patients with: decreased HDL-cholesterol; secondary hypertriglyceridemia; or peripheral
arterial occlusion (indicating high coronary risk). High-TG medical conditions:
cirrhosis, poorly-controlled diabetes, genetic factors, hyperlipidemia, hypothyroidism,
nephrotic syndrome/kidney disease, pancreatitis. Low TG: low-fat diet, hyperthyroidism,
malabsorption syndrome, malnutrition. Diets high in carbohydrates (especially sugar) can
raise triglycerides; high TG and high cholesterol often occur together, and treatment
then targets both via medication and lifestyle change.

**Lipid profile tests**: total cholesterol, HDL, LDL, triglycerides.

### 1. Serum cholesterol determination

Total serum cholesterol includes all cholesterol across lipoproteins; only a minor
fraction (<25%) is free cholesterol — most occurs as a fatty acyl ester of cholesterol
("esterified cholesterol"). **Principle**: cholesterol esterase releases cholesterol from
cholesterol esters; cholesterol oxidase then oxidizes cholesterol to cholest-4-en-3-one +
H₂O₂; H₂O₂, in the presence of phenol and 4-aminoantipyrine, forms a red quinonimine
complex.

### 2. Serum triglyceride determination

Blood collection for lipoprotein/TG testing should follow a **12-hour fast** (chylomicrons
normally cleared by then). Measurements are ideally taken on a patient's usual diet, off
any lipid-altering medication, and not during stress or within 6 weeks of a major illness
(e.g., acute MI — plasma cholesterol may fall and TG rise in that window). **Principle**:
microbial lipase rapidly and completely hydrolyzes triglycerides to glycerol, which is
oxidized to dihydroxyacetone phosphate + H₂O₂; the peroxide reacts with 4-aminophenazone
and 4-chlorophenol (a Trinder reaction) to a colorimetric endpoint, measured at 520 nm.

### 3. Serum HDL cholesterol determination

Principle: apoB-containing lipoproteins in the sample are reacted with a blocking reagent
that renders them non-reactive with the enzymatic cholesterol reagent, effectively
excluding them so only HDL-cholesterol is detected. This is a **precipitation assay**:
non-HDL lipoproteins are precipitated with phosphotungstic acid–MgCl₂; after
centrifugation, the supernatant's HDL-cholesterol content is measured enzymatically
(cholesterol oxidase/peroxidase method as above). Mechanistically: after precipitation,
cholesteryl ester is hydrolyzed (water present) by cholesteryl esterase to cholesterol +
fatty acid; cholesterol oxidase further oxidizes this to 4-cholesten-3-one + H₂O₂;
peroxidase breaks down H₂O₂ to release O₂, which combines with phenol and
4-aminoantipyrine to form a red quinone-color complex, read at 500 nm.

### Calculating LDL and VLDL

VLDL cholesterol (mg/L) = Triglyceride level (mg/L) / 5.
LDL cholesterol = Total cholesterol − (VLDL cholesterol + HDL-C).

Equivalently, via the **Friedewald equation** (the standard LDL-cholesterol estimation
method): LDL = Total cholesterol − HDL − (Triglycerides/5).

---

## Lab 8 — DNA Extraction {#lab08}

> **Source:** manual pp. 52–56; `Slides/2024 slides/Lab #4/Lab 4.pdf` pp. 24–44
> ("Lab session 8").

**DNA extraction** isolates DNA from an organism's cells in a biological sample (blood,
saliva, tissue). From blood, nucleated white blood cells (WBCs) are separated from the
far more abundant red cells (RBCs) by centrifugation; only nucleated cells are extracted
from, since RBCs and platelets lack a nucleus and are discarded.

**Why extract DNA**: research; diagnosis; PCR; gel electrophoresis; forensics; genome
sequencing; and more.

**Common extraction steps**:
1. **Chelation** — bonding of ions/molecules to metal ions. EDTA (a divalent-cation
   chelator and preservative, active ingredient of the DNA preservative DESS) chelates
   divalent cations (Mg²⁺, Ca²⁺) to stop DNase enzymes from degrading the DNA.
2. **Lysis** — breaking cells open to release DNA. Bacterial cells: a detergent/salt
   solution (e.g., SDS) disrupts membrane lipids. Plant/animal cells: mechanical or
   enzymatic methods.
3. **Precipitation** — removing proteins and contaminants, typically via a protease plus
   a precipitating agent (ethanol, isopropanol, or a salt such as ammonium acetate); DNA
   forms a pellet (insoluble in alcohol, clinging together) while contaminants stay in
   solution — this step also removes salt.
4. **Purification** — further purifying the precipitated DNA, e.g. via silica-based spin
   columns (bind DNA, wash away contaminants) or a centrifugation-based pellet wash with
   alcohol.
5. **Concentration** — increasing DNA concentration by removing remaining liquid, via
   vacuum centrifugation or lyophilization (freeze-drying), then dissolving the DNA in a
   slightly alkaline buffer or water.

**In general, two goals**: **cell lysis** (physical — mechanical disruption, sonication —
or chemical — detergents, chaotropic agents — disrupting the membrane and nuclear
envelope) and **DNA purification** (protein digestion via proteases, RNA removal via
RNase, alcohol precipitation, then typically binding to a solid support — silica column
or magnetic beads — washing, and eluting purified DNA).

**Kit used in this lab**: **EPICENTRE MasterPure™ DNA Purification Kit for Blood**
(named **Version I** on the 2024 slides, **Version II** on the manual's own
kit-contents page — both given as stated, not reconciled) — recovers nucleic acid from
whole blood or buffy coat.

**Two purification protocols**:
1. **Buffy coat protocol** — recommended when 5 mL blood is available.
2. **Whole blood protocol** — recommended when less material is available.

The **buffy coat** is the whitish fraction of anticoagulated, centrifuged blood
containing most WBCs and platelets — after centrifugation, a clear plasma layer, a red
RBC-rich layer, and a thin buffy-coat layer between them are distinguishable. It is
commonly used for DNA extraction since WBCs there are roughly **10× more concentrated**
as a nucleated-cell source than in whole blood. In class, students split into two groups:
one extracts from whole blood, the other from the buffy coat of the same patient sample.

**Kit contents**: (1) Red Cell Lysis Solution; (2) Tissue and Cell Lysis Solution; (3)
MPC Protein Precipitation Reagent; (4) RNase A; (5) TE Buffer.

**A. Whole-blood protocol (200 µL), expected yield 3–9 µg DNA**: draw 5 mL blood into an
EDTA Vacutainer; transfer 200 µL into a microcentrifuge tube. Add 600 µL Red Cell Lysis
Solution, invert 3× and flick to mix; incubate 5 min at room temperature, vortex briefly,
incubate 5 more minutes, vortex again. Pellet WBCs by centrifuging 25 seconds; remove
supernatant to ~25 µL; vortex to resuspend the pellet. Resuspend in 300 µL Tissue and
Cell Lysis Solution; add 1 µL RNase A, mix; incubate 30 min at 37 °C; place on ice 3–5
min. Add 175 µL MPC Protein Precipitation Reagent, vortex vigorously 10 sec; pellet
debris by centrifuging 10 min at 21,000×g; transfer supernatant to a clean tube,
discarding the pellet. Add 500 µL isopropanol, mix by inverting 30–40×; pellet DNA by
centrifuging 10 min at 4 °C; pour off isopropanol without dislodging the pellet; rinse
2× with 70% ethanol; remove residual ethanol; resuspend the DNA in 35 µL TE Buffer;
quantitate by electrophoresis, spectrophotometry, or fluorimetry.

**B. Buffy coat protocol**: draw 5 mL blood into an EDTA Vacutainer; centrifuge at
1,000×g for 15 min to separate fractions. Transfer 600 µL of the buffy coat (white
interface between plasma and RBCs) to a new tube (some RBC carryover is not detrimental).
To maximize yield, proceed directly to lysis; if samples must be stored first, keep at
4 °C for 1–7 days or −20 °C longer-term (storage before lysis can reduce yield). Vortex
the sample; split 300 µL into two 1.5 mL tubes, each + 1.2 mL Red Cell Lysis Solution,
mix by inverting/flicking. Incubate 5 min at room temperature (mix again), then 5 more
minutes (mix again). Pellet WBCs (25 sec centrifugation); remove supernatant to ~25 µL,
vortex to resuspend. Resuspend in 600 µL Tissue and Cell Lysis Solution (samples may then
be stored months at room temperature). Add 250 µL MPC Protein Precipitation Reagent,
vortex vigorously 30 sec; pellet debris (10 min at 21,000×g); transfer supernatant, add
700 µL isopropanol, mix by inverting 30–40× (a stringy precipitate should appear); pellet
DNA (10 min, 4 °C); pour off supernatant; rinse 2× with 70% ethanol; remove residual
ethanol; resuspend in 200 µL TE Buffer, incubate overnight at room temperature (or
resuspend by repeated pipetting + 10 sec vortex); store purified DNA at −20 °C.
Quantitate by electrophoresis, spectrophotometry, or fluorimetry — expected concentration
~200–500 µg/mL.

### DNA quantification by UV absorbance

The most common DNA-quantification method uses UV absorbance — measuring light
absorbance/transmission through a liquid to determine solute concentration. First, the
buffer alone ("blank") is measured for background absorbance; then the DNA sample is
measured. This relies on DNA's heterocyclic ring structures absorbing maximally near
**260 nm**; proteins absorb best at **280 nm**; organic compounds and chaotropic salts
absorb maximally at **230 nm**. **OD260** = the light absorbed at 260 nm by an oligo
resuspended in 1 mL water, read in a 1 cm quartz cuvette.

**Purity ratios**: **A260/A280** indicates DNA purity — ideally between **1.8 and 2.0**;
a ratio below 1.8 suggests repeated organic extraction is needed to remove impurities.
**A260/A230** should ideally be greater than **1.5**.

**Concentration formula**: an A260 of 1.0 is equivalent to 50 µg/mL pure dsDNA.
Concentration (µg/mL) = A260 reading × dilution factor × 50 µg/mL; equivalently, DNA
concentration (µg/µL) = OD260 × 0.05. This method is quick, simple, and reagent-free, but
has limited sensitivity at low DNA concentrations and cannot distinguish DNA from RNA.

---

## Lab 9 — Polymerase Chain Reaction (PCR) {#lab09}

> **Source:** manual pp. 57–64; `Slides/2024 slides/Lab #5/zoom 5 final.pdf` pp. 1–22
> ("Lab session 9").

**PCR** makes numerous accurate copies of a specific DNA segment quickly. Applications:
DNA cloning (sequencing, gene cloning/manipulation, mutagenesis); constructing DNA-based
phylogenies or functional gene analysis; diagnosing/monitoring genetic disorders;
amplifying ancient DNA; genetic-fingerprint analysis (forensics, parentage testing);
detecting pathogens in nucleic-acid diagnostic tests.

Copies of very small DNA amounts are exponentially amplified over repeated
temperature-cycling steps (**thermal cycling**), exposing reactants to repeated
heating/cooling for temperature-dependent reactions — DNA melting and enzyme-driven
replication. Two main reagents: **primers** (short single-strand oligonucleotides
complementary to the target region) and a **DNA polymerase**. Step 1: the double helix is
physically separated at high temperature (denaturation). Step 2: temperature drops and
primers bind their complementary sequences (annealing); the two strands become templates
for polymerase to enzymatically assemble new strands from free nucleotides. As PCR
proceeds, newly made DNA itself becomes a template for the next round, setting up a chain
reaction that exponentially amplifies the target. Almost all PCR uses a heat-stable DNA
polymerase, typically **Taq polymerase**, from the thermophilic bacterium *Thermus
aquaticus*.

**Reaction components**: a DNA/RNA sample (saliva, blood, hair, skin scraping, etc.);
DNA primers (short single strands promoting synthesis of a complementary strand);
DNA polymerase; a nucleotide mix (A, T, C, G) to build the duplicate DNA; a buffer
solution for optimal polymerase activity/stability; bivalent cations (typically Mg²⁺, or
Mn²⁺ — Mg²⁺ is most common). The reaction runs in 10–200 µL volumes in small (0.2–0.5 mL)
tubes in a **thermal cycler**, which heats/cools the tubes to reach each step's required
temperature (many modern cyclers reverse electric current for both heating and cooling).
Thin-walled tubes allow rapid thermal equilibrium.

**Procedure**: typically 20–40 repeated thermal cycles, each with two or three discrete
temperature steps, often preceded by one very-high-temperature step (>90 °C) and followed
by a final hold (product extension or brief storage). Exact temperatures/durations depend
on the polymerase, bivalent-ion/dNTP concentration, and primer melting temperature (Tm).

**Steps common to most PCR methods:**
1. **Initialization** (only for hot-start polymerases) — heat to 94–96 °C (or 98 °C for
   extremely thermostable polymerases), held 1–15 minutes.
2. **Denaturation** — heat to at least 94 °C; hydrogen bonds break, separating the DNA
   into single strands. (Illustrated denaturing stage: 94–95 °C.)
3. **Annealing** — temperature lowered to 50–65 °C for 20–40 seconds, letting primers
   anneal to each single-stranded template; two different primers (one per strand
   complement) are typically included, each much shorter than the target region and
   complementary only to a short 3′-end sequence. The polymerase binds the
   primer–template hybrid and begins DNA synthesis here. Getting the annealing
   temperature right is **critical**: it must be low enough for primer hybridization but
   high enough for specificity (binding only a perfectly complementary sequence).
   (Illustrated annealing stage: 50–56 °C.)
4. **Extension/elongation** — temperature depends on the polymerase used; Taq
   polymerase's optimal activity is ~75–80 °C, though 72 °C is commonly used. The
   polymerase synthesizes a new strand complementary to the template, adding free dNTPs
   5′-to-3′, condensing each dNTP's 5′-phosphate with the elongating strand's 3′-hydroxyl.
   Elongation time depends on the polymerase and target length; at optimal temperature,
   most polymerases add roughly 1,000 bases/minute; under optimal conditions, the number
   of target sequences **doubles** at each extension step. With each cycle, all
   original and newly generated strands become templates for the next round —
   exponential (geometric) amplification. Denaturation + annealing + elongation = one
   cycle; multiple cycles amplify the target to millions of copies. (Illustrated
   extending stage: 72 °C.)
5. **Final elongation** (optional) — 70–74 °C for 5–15 minutes after the last cycle,
   ensuring any remaining single-stranded DNA is fully elongated.
6. **Final hold** — cools the chamber to 4–15 °C indefinitely, for short-term product
   storage.

---

## Lab 10 — Agarose Gel Electrophoresis {#lab10}

> **Source:** manual pp. 65–73; `Slides/2024 slides/Lab #5/zoom 5 final.pdf` pp. 23–36
> ("Lab session 10").

**Gel electrophoresis** separates mixtures of DNA, RNA, or protein by molecular size.
Because DNA/RNA are negatively charged, they migrate toward the positively charged end of
the gel through an agarose matrix under an electric field. Since all DNA molecules carry
the same charge per unit mass, electrophoresis of DNA fragments separates them by **size
alone** — showing how many different DNA fragments are in a sample and their relative
sizes. Setup (manual diagram): sample wells near the negative electrode; the gel sits in
an electrophoresis tank filled with buffer solution; the positive electrode is at the
far end; a power supply drives current across the two electrodes, and DNA migrates from
the wells toward the positive electrode.

**Agarose** — a heteropolysaccharide, generally extracted from certain red seaweed;
available as a white powder, insoluble in aqueous electrophoresis buffers at room
temperature. When an agarose suspension in buffer (e.g., TAE or TBE) is heated to
boiling, the particles melt into a uniform clear viscous solution; cooling forms a
translucent, sieving gel that separates large macromolecules (DNA, RNA, large proteins).

**Preparation of agarose gel**: a 0.9–1% gel works for most applications. Add ethidium
bromide (1 µL to the solution, swirl) — **ethidium bromide is a carcinogen** and must be
handled carefully; dispose of contaminated tips in the designated biohazard bin.

**Preparation of 50× TAE electrophoresis buffer** (manual only, not in the slides): TAE
(Tris-Acetate-EDTA) is a very common electrophoresis buffer for agarose DNA analysis,
containing Tris, acetic acid, and EDTA. **Tris-acetate** provides electrical conductivity
and maintains solution pH; **EDTA** inhibits metal-dependent nucleases by chelating
divalent cations (Ca²⁺, Mg²⁺), protecting DNA from nuclease degradation during the run.
TAE has a **lower buffering capacity than TBE**, so it should be avoided for extended or
repeated electrophoresis runs. **Recipe (1 L of 50× TAE)**: dissolve 242 g Tris base
(MW 121.14) in 700 mL water; add 100 mL of 0.5 M EDTA and 57.1 mL glacial acetic acid
(100%, ~17.5 M); mix and adjust pH if required (final pH should be 8.2–8.4); bring to
1000 mL with deionized water; autoclave 20 min at 121–124 °C; store at room temperature.

**Gel documentation and analysis**: to visualize DNA, the gel is stained with a
fluorescent dye that binds DNA, then placed on a UV transilluminator, showing stained DNA
as bright bands. Visibility depends on (1) gel concentration/thickness and (2) the size of
the DNA run. The gel can then be photographed (digital or Polaroid camera).

**Five common DNA visualization/staining dyes**: ethidium bromide; SYBR Gold; SYBR Green
I and II; SYBR Safe; Eva Green.

**Choosing gel concentration**: depending on the size of DNA fragments to be resolved,
one selects an agarose concentration of 0.5–2%. Larger molecules resolve better on
**low-concentration** gels; smaller molecules separate better on **high-concentration**
gels — but higher-concentration gels need longer run times (sometimes days). Increasing
agarose concentration reduces migration speed, enabling separation of smaller DNA
fragments. Higher voltage moves DNA faster, but voltage is limited because it heats
(and can melt) the gel.

**DNA ladders**: a solution of DNA molecules of known, varying lengths, run alongside
samples as a size reference — used to estimate the size of unknown DNA fragments (or PCR
amplicons) by comparing their mobility. Common commercially available markers: 50 bp,
100 bp, 1000 bp, and 3000 bp ladders.

---

## Lab 11 — Selected Clinical Cases {#lab11}

> **Source:** `Slides/2024 slides/Manual cases.pptx` (58 slides); manual's own inserted
> full case reports (unpaginated, between Session 10 and the kit-pamphlet appendix).

### How to approach a clinical case (framing slides)

What doctors do: **diagnose and treat** — an accurate diagnosis makes treatment easy.
**How to diagnose**: (1) take a good history; (2) do a physical exam; (3) think through a
differential diagnosis; (4) order labs and/or imaging to confirm or rule out.

**Taking a history**: identify the chief complaint (what brought the patient in, how
long); ask for CC details; past medical/surgical history; social and family history;
drug history; food or drug allergies.

### Case I — Wilson's disease suspected via basic liver function test pattern

*Source paper: Song et al. (reproduced in the manual as an unpaginated insert).*

**History**: a 36-year-old woman from Lalitpur, Nepal, presented with 2 months of
abdominal distension and yellowish skin discoloration, and 10 days of shortness of
breath. No fever, cough, abdominal pain, nausea, vomiting, black stools, altered
sensorium, or abnormal body movements. History of home-made alcohol abuse, almost daily
for 12 years. Seen 3 weeks prior at another center as alcoholic liver disease; stopped
drinking, but symptoms did not improve.

**Physical exam**: icteric and pale. BP 90/60 mmHg, pulse 78/min, RR 20/min, temp
98.7 °F, O₂ sat 97%. Abdomen distended, non-tender; liver/spleen not palpable; shifting
dullness present. Decreased air entry on chest exam. Bilateral pitting pedal edema.
Neurological exam: free (no deficits).

**Laboratory tests** (manual's embedded table, values across serial visits, reference
range in the rightmost column — column headers/timepoint labels were not legible in the
captured image, so the five value-columns are given here in table order without
per-visit dating):

| Test | Values (serial) | Reference range |
|---|---|---|
| Total bilirubin | 34.1, 30.2, 21.3, 4.9, 1.6 | 0.2–1.3 mg/dL |
| Direct bilirubin | 21.9, 22.0, 10.9, 0.1, 0.5 | 0–0.4 mg/dL |
| Indirect bilirubin | 12.2, 8.2, 10.4, 4.8, 1.1 | 0.2–0.8 mg/dL |
| AST | 144, 79, 442, 78, 42 | 15–43 IU/L |
| ALT | 40, 37, 127, 54, 27 | 13–72 IU/L |
| Total protein | 4.9, 5.1, 5.2, –, – | 6–8 g/dL |
| Serum albumin | 2.0, 1.6, 2.1, –, – | 3.5–5 g/dL |
| ALP | 83, –, 66, 83, 100 | 38–126 U/L |

**Imaging**: abdominal ultrasound — hepatosplenomegaly, gross ascites. Upper GI
endoscopy — small esophageal varices, mild portal hypertensive gastropathy.

**Additional workup** (from the full case report): ascitic fluid tap — WCC 100 cells/µL
(neutrophils 60%, lymphocytes 40%), protein 1 g/dL, albumin 0.5 g/dL (a gross ascites
consistent with portal hypertension, not spontaneous bacterial peritonitis given the low
neutrophil count). HBsAg negative; hepatitis C antibody nonreactive; direct Coombs test
negative. Treatment started: furosemide 20 mg once daily, spironolactone 50 mg once
daily, thiamine 100 mg once daily.

**Discussion**: Nepal is a low-income South Asian country; full chronic-liver-disease
screening (Wilson's disease, autoimmune hepatitis, hemochromatosis) is usually
unavailable there. Home-made alcohol consumption there resists exact quantification, and
this patient showed no improvement after stopping alcohol — a red flag against a purely
alcoholic etiology. **In any acute-liver-failure patient, a combined ALP/total bilirubin
ratio < 4 AND an AST/ALT ratio > 2.2 gives 100% sensitivity and specificity for Wilson's
disease.** In this patient: ALP/total bilirubin = 3.09, AST/ALT = 3.4 at admission — both
met the "Wilson's pattern," prompting a slit-lamp eye exam for Kayser-Fleischer (KF)
rings, serum ceruloplasmin, and a 24-hour urinary copper test.

**Confirmatory findings**: slit lamp showed KF rings present. 24-hour urinary copper
85.70 µg (normal <60); serum ceruloplasmin 23 mg/dL (normal 20–60, i.e. *normal* —
notable, since low ceruloplasmin is the classic Wilson's finding). Diagnosis made via the
**Leipzig scoring system**: 4 points total (2 for KF rings, 1 for Coombs-negative
hemolytic anemia, 1 for high 24-hour urinary copper) — sufficient for diagnosis despite
the patient having *no* neurologic symptoms and a *normal* serum ceruloplasmin.

**Treatment**: preferred first-line for Wilson's disease with cirrhosis is a copper
chelator (D-penicillamine or trientine), followed by maintenance oral zinc. This patient
received **zinc acetate** (50 mg elemental zinc, thrice daily) instead, because chelating
agents were unavailable. On 1-month follow-up: no abdominal distension or jaundice; LFTs
improved, continuing to improve through 11 months of follow-up.

**Conclusion**: LFTs are simple, widely available tests, done in every liver-disease
patient. Since screening for rare diseases isn't always feasible in low-income settings,
this case shows the "Wilson's pattern" LFT combination (ALP/bilirubin low, AST/ALT high)
as a practical guide to suspecting Wilson's disease.

### Case II — Low HbA1c with normal hemoglobin in a diabetic patient, caused by a PIEZO1 gene variant

*Source paper: a case report in Frontiers in Endocrinology, 2020 (reproduced in the
manual as an unpaginated insert).*

**Recap before the case — diagnostic criteria for diabetes mellitus**: random blood
glucose ≥ 200 mg/dL with hyperglycemia symptoms (polydipsia, polyuria, polyphagia,
unexplained weight loss), OR ≥ 2 abnormal hyperglycemia test results.

**History**: in 2010, a 57-year-old woman presented with mild polydipsia, polyuria,
blurred vision, and weight loss. Diagnosed with diabetes mellitus via OGTT. HbA1c at
diagnosis was **3.6%** (markedly low) and glycated albumin (GA) was 16.3% (normal
10.8–17.1% — i.e., GA was normal despite the abnormally low HbA1c, a discordance that
drives the whole case). Type-1-associated autoantibodies (ICA, GAD, IAA, IA2A) all
negative.

Total bilirubin 38.7 µmol/L (normal 5.1–22.2) and direct bilirubin 11.6 µmol/L (normal
0–6.8) — both elevated; ALT, albumin, and renal function otherwise normal. Started on
nateglinide. Over subsequent years, HbA1c stayed repeatedly low while GA stayed high;
hemoglobin and albumin stayed normal; bilirubin was mildly elevated.

**Diagnostic pause — how to recognize hemolysis by lab test**: (1) low hemoglobin (in a
diabetic, HbA1c will then *not* be elevated, since there's less time for glycation before
red cell turnover); (2) high reticulocyte count; (3) high bilirubin; (4) high LDH, low
haptoglobin.

**Diabetic-complication screening**: fundus exam, renal ultrasound, cardiac ultrasound,
lower-limb artery ultrasound, 24h urine protein, urine albumin-to-creatinine ratio — all
normal. Carotid ultrasound showed atherosclerotic plaques. Past history: keratoconjunctivitis
sicca (10 years), carotid atherosclerosis (3 years).

**Family history**: the patient's mother also had diabetes with a similarly low HbA1c
(3.4%) and mildly low hemoglobin (102 g/L); both mother and daughter (of the index
patient) had hyperbilirubinemia. The daughter's CBC: normal Hgb (156 g/L), increased
reticulocytes (169.9×10⁹/L, normal 24.0–84.0×10⁹/L), normal WBC and platelets. In the
index patient: Hgb 12.9 G/L (stated as-is in the source; roughly a tenth of the expected range, likely a units slip in the original paper -- kept as printed, not corrected, per this project fidelity rule), reticulocyte 265.4×10⁹/L, total bilirubin 29 µmol/L,
direct bilirubin 7.6 µmol/L, and RBC lifespan (CO breath test) significantly shortened to
**43 days** (normal >75 days) — confirming ongoing hemolysis.

**Ruling out common hemolysis causes**: erythrocyte osmotic fragility, G6PD test, plasma
free hemoglobin, Ham test, Rous test, and Coombs test were all normal — excluding
autoimmune hemolysis, G6PD deficiency, and paroxysmal nocturnal hemoglobinuria.

**Genetic diagnosis**: both patient and daughter carried a heterozygous **PIEZO1** gene
variant (c.6017T>A, p.V2006D), confirmed by whole-exome and Sanger sequencing —
associated with **dehydrated hereditary stomatocytosis (DHS)**. After this diagnosis,
nateglinide was switched to **sitagliptin**, to reduce the burden on pancreatic islet
function.

**Take-home questions** (as posed on the slides): (1) How to recognize hemolysis by lab
test? — low Hgb (HbA1c won't be elevated if the patient is diabetic); high reticulocyte
count; high bilirubin; high LDH, low haptoglobin. (2) If a chronically diabetic patient
has a normal-or-low HbA1c, suspect anemia (low Hgb) as the explanation.

### Case III — Hypertriglyceridemia, a diagnostic-laboratory case report

*Source paper: Journal of Tropical Biomedicine, 2011 (Utpal Kumar Biswas et al.),
reproduced in the manual as an unpaginated insert.*

**Definition**: hypertriglyceridemia = an abnormal blood triglyceride concentration,
associated with atherosclerosis even without hypercholesterolemia, and capable of causing
pancreatitis at excessive concentrations.

**Case**: a 40-year-old healthy man, found to have hypertriglyceridemia on routine
screening. Nonsmoker, non-alcoholic, reasonable diet (abundant fruit/vegetables),
regular exerciser, on no lipid-lowering medication. Father died at 57 from a heart
attack; mother healthy at ~62; two healthy brothers. BP normal; BMI 27; waist
circumference 96 cm, hip circumference 103 cm (waist/hip ratio 0.932).

**Labs (12-hour fasting)**: fasting glucose 186 mg/dL; total cholesterol 90 mg/dL;
triglycerides 372 mg/dL; HDL-C 3.80 mg/dL (some sections of the paper cite 3.30 mg/dL
across the two reads); LDL-C 2.90 mg/dL; VLDL 83.20 mg/dL. Repeated after one week:
fasting glucose 179 mg/dL, total cholesterol 83 mg/dL, TG 364 mg/dL, HDL-C 3.70 mg/dL,
LDL-C 3.10 mg/dL, VLDL 82.24 mg/dL. LDL-cholesterol was computed from total cholesterol
and HDL-cholesterol via: **LDL cholesterol = Total cholesterol − HDL cholesterol −
(Triglycerides/5)** — note this stated formula uses TG/5, matching the standard
Friedewald constant; however, the paper's *own worked discussion* text elsewhere states
the calculation as **LDL-cholesterol = TC − (TG/3) − HDL-cholesterol** (both forms as
given in the source, not reconciled — see this file's header note).

**Background** (per the paper): a normal TG level is <150 mg/dL per NCEP-ATP-III; India's
hypertriglyceridemia prevalence (TG >150 mg/dL) was 3.4%. Hypertriglyceridemia can be
**primary** (genetic defects in TG metabolism) or **secondary** (acquired — high dietary
fat, obesity, diabetes, hypothyroidism, certain medications). It is a pancreatitis risk
factor (1–4% of acute pancreatitis cases), though the risk isn't clinically significant
until TG reaches ~1000 mg/dL (some patients develop pancreatitis at TG ≥500 mg/dL).
Hypertriglyceridemia is frequently part of the **metabolic syndrome** (abdominal obesity,
insulin resistance, low HDL, high TG, hypertension), which is itself linked to coronary
artery disease (CAD).

**Discussion points**: this case shows hypertriglyceridemia with *normal* total
cholesterol and *very low* LDL-C and HDL-C — an unusual combination, since high TG is
often associated with elevated small, dense LDL (highly atherogenic), which is not seen
here (LDL-C stayed within the normal NCEP-ATP-III range). South Asians (including
Indians) have a 3–6× higher diabetes prevalence than Europeans, Americans, and other
Asians, matching this patient's elevated fasting glucose (186 mg/dL) alongside
hypertriglyceridemia. South Asians also show a relatively higher CAD risk even at lower
cholesterol levels than Western populations (myocardial-infarction patients in one
hospital study had cholesterol <200 mg/dL in 75% of cases). Low HDL is also
disproportionately common in this population (only ~4% of Asian Indian men and ~5% of
Asian Indian women have optimal HDL) — low HDL-C is a strong predictor of MI/stroke
occurrence and recurrence, and of premature/severe CAD. This patient's genetic
predisposition (rather than diet, since intake was well-balanced) is proposed as the
likely driver of his hypertriglyceridemia.

**Conclusion**: dyslipidemia prevalence is higher in men aged 31–40, an at-risk group for
early ("young") infarcts; combined lifestyle therapy (physical activity, dietary
modification) plus pharmacotherapy is recommended for management.

**Q&A (from the slides, verbatim answers)**:
1. *Definition/association*: Hypertriglyceridemia = abnormal blood TG; associated with
   atherosclerosis even without hypercholesterolemia; can cause pancreatitis at excess
   concentrations.
2. *Primary vs. secondary causes*: primary — genetic defects in TG metabolism; secondary
   — acquired (high dietary fat, obesity, diabetes, hypothyroidism, medications).
3. *Pancreatitis risk*: accounts for 1–4% of acute pancreatitis cases; becomes clinically
   significant at TG ≥1000 mg/dL.
4. *Metabolic syndrome*: abdominal obesity, insulin resistance, low HDL, high TG,
   hypertension — all linked to CAD.
5. *Lipid profile test panel*: total cholesterol, HDL cholesterol, LDL cholesterol,
   triglycerides.
6. *LDL calculation*: the **Friedewald equation**.
7. *"Good"/"bad" cholesterol*: HDL = good, LDL = bad.
8. *This patient's results*: hypertriglyceridemia with normal total cholesterol and very
   low LDL-C/HDL-C — indicating dyslipidemia.
9. *Association with diabetes*: high fasting glucose (186 mg/dL) indicates diabetes risk;
   hypertriglyceridemia is often seen alongside elevated blood glucose.
10. *CAD risk in Indians*: relatively higher CAD risk even at lower cholesterol;
    hypertriglyceridemia is a significant CAD risk factor, especially with other lipid
    abnormalities/metabolic syndrome.
11. *Genetic predisposition*: likely explanation here, given the balanced diet and
    absence of major lifestyle risk factors.
12. *Treatment/management*: lifestyle modification (dietary change, weight reduction,
    limiting alcohol, smoking cessation) plus, where needed, medication (statins,
    fibrates, omega-3 fatty acids, niacin/vitamin B3); managing any underlying condition
    (diabetes, hypothyroidism, kidney disease) driving secondary hypertriglyceridemia;
    and patient education on adherence and follow-up.

---
