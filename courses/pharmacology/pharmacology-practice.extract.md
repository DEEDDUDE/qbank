---
course: pharmacology
tab: practice
questions: 481
tiers: official 95 | claimed 281 | open 105
forms: mcq 449 | qa 32
needs-eye: 0
disputed: 0
next-id: PHARM-P-482
---

<!-- batch 01 (probe) — raw/practice/Pharmacology PYQ and Bank Questions.pdf, pages
  1-46 of 134. RUN-PLAN row 2: this batch runs first because it's free (real text
  layer, no vision) and proves the OCR-text extraction path before 368 vision pages
  get spent on the other three tabs. Pages 47-134 (the "TEST BANK", the dental
  students 2022/2023 set, "Pharma020", and the final numbered set) are separate
  RUN-PLAN rows (10-12), not covered here.

  Three source sections, each its own numbering:
    p1-26   Fawzi Shihadeh & Malik Suliman's compiled set. No answers anywhere on
            these pages -> tier open throughout. Internally THREE separately-
            numbered lists back to back (1-39/1-40/1-26), each restarting from 1 --
            this is the source's own structure, not a Job A error. PHARM-P-001
            through PHARM-P-099.
    p28-31  Rama Harb & Sana Alsokhon's "Midterm collected Questions of
            pharmacology 021" -- numbered 1) through 24), each followed by an
            "Ans:" line -> tier claimed. Two gaps are real, not dropped: #4 never
            appears, and #11 is a bare "11)" with nothing after it -- the source
            itself left it blank. PHARM-P-100 through PHARM-P-121 (22 real
            entries; the empty #11 has no corresponding ID since there was nothing
            to transcribe). PHARM-P-104 references a figure (image saved to
            flagged/) -- the stem literally says "look carefully at this figure."
            PHARM-P-122 is a 23rd question from this same page range that exists
            ONLY as an embedded image (page 29) -- invisible to a text-layer read,
            found by checking every page in this range for embedded images and
            inspecting each one. Same claimed tier as its neighbors.
    p31-45  Rama Harb & Sana Alsokhon's "Final collected Questions of pharmacology
            021" -- unnumbered, one question per paragraph, each closed by an
            "ans:"/"ANSWER:"/"AMSWER:" line (all three spellings appear in the
            source; preserved as printed) -> tier claimed. PHARM-P-123 through
            PHARM-P-174.

  Every embedded image on pages 1-46 was checked (get_images() per page, not just
  pages a stem explicitly names) -- five found total. Two are load-bearing and
  saved to flagged/ with the question they answer (PHARM-P-033's "Ultron" dose-
  response curve, PHARM-P-104's route-of-administration curve, plus the embedded
  PHARM-P-122 question itself). One (PHARM-P-022, a first-order-kinetics plot) is
  a plausible but unconfirmed tie, kept anyway. Two were discarded, not kept in
  flagged/: page 27's cover-sheet photo/logo art (decorative, no question content)
  and an unlabeled half-life decay graph on page 29 with no textual tie to any
  question on that page.

  The source's own compiler left a closing note after page 26 (Arabic, trailing
  what is now PHARM-P-099's last option in the raw text): "external sources -- the
  answers are at the end of each source, answered by academic staff. Note: the
  files contain additional material, so be careful." Recorded here since it is a
  remark about the whole compiled document, not about PHARM-P-099 specifically.

  The p1-26 text layer is OCR output, not native typing (page.get_text() on a
  PDF with visible scan artifacts) -- errors like "Faise" for False, "Phase!" for
  Phase I, "(Va)" for Vd, and "aftel" for after are preserved exactly as extracted,
  per CLAUDE.md's don't-correct-drug-names note on this file. The p27-45 pages read
  the same way but with fewer artifacts. -->

### PHARM-P-001
tier: open
form: mcq
type: single
Pharmacokinetics is:
a) The study of how drugs reach their target in the body and how the levels of a drug in the blood are affected by various factors
b) The study of how drugs can be designed using molecular modelling based on a drug's pharmacophore.
c) The study of how a drug interacts with its target binding site at the molecular level
d) The study of which functional groups are important in binding a drug to its target binding site and the identification of a pharmacophore.

### PHARM-P-002
tier: open
form: mcq
type: single
Which of the following is the most correct sentence concerning
intravenous administration of drugs?
a) Gives predictable blood levels
b) None undergoes first pass metabolism
c) All of it undergoes first pass metabolism
d) A and B
e) A, B, and C

### PHARM-P-003
tier: open
form: mcq
type: single
Some drugs have a low oral bioavailability due to extensive
metabolism in the GI tract or liver. Which dosage form can be used
to best avoid this complication?
a) Controlled release tablet
b) Enteric coated tablet
c) Soft capsule
d) Sublingual

### PHARM-P-004
tier: open
form: mcq
type: single
Concerning the enteral route of administration, the correct
sentence is:
a) The bioavailability here is excellent as compared to parenteral route
b) Has faster onset of action as compared to parenteral route
c) Could be used by either conscious or unconscious patients
d) None of the above

### PHARM-P-005
tier: open
form: mcq
type: single
Which of the following preparations will give sustained drug
delivery with prolonged duration of action?
a) Sugar coated tablet
b) Aqueous prepared IM injection
c) Transdermal patches
d) Sublingual tablet

### PHARM-P-006
tier: open
form: mcq
type: single
For a drug with a narrow therapeutic index, the plasma
concentration required for therapeutic effects is near the
concentration that produces toxic effects, and such a drug require
routine plasma monitoring.
a) True
b) Faise

### PHARM-P-007
tier: open
form: mcq
type: single
All of the following statements are true about intranasal route of
administration EXCEPT:
a) It is only used for administration of drugs used in respiratory conditions.
b) It has a rapid onset of action.
c) It possesses good compliance among patients
d) Few systemic side effects

### PHARM-P-008
tier: open
form: mcq
type: single
Variation in cytochrome P450 enzyme profile between individuals
can explain individual variation in drug susceptibility.
a) True
b) False

### PHARM-P-009
tier: open
form: mcq
type: single
If the plasma concentration of a drug declines with "first-order
kinetics," this means that:
a) There is only one metabolizing enzyme for drug disposition
b) The half-life is the same regardless of the plasma concentration
c) The drug is largely metabolized in the liver after oral administration and has low bioavailability
d) All of them

### PHARM-P-010
tier: open
form: mcq
type: single
In relation to the therapeutic window of a drug, which of the
following sentences is true:
a) Drugs with wide therapeutic range are not potent enough compared with narrow therapeutic range.
b) A drug must exceed the maximum effective dose in order to be therapeutically active.
c) Drugs with plasma concentration below the minimum effective concentration show no therapeutic effect.
d) It is a range of concentration that determines both the safety and efficacy of drugs.

### PHARM-P-011
tier: open
form: mcq
type: single
Which of the following statements is the closest description of
Phase! metabolism?
a) Reactions which add an endogenous polar molecule to a functional group already present on a drug or one of its metabolites.
b) Reactions which occur in the blood supply.
c) Reactions which add a polar functional group to a drug
d) Reactions which occur in the gut wall.

### PHARM-P-012
tier: open
form: mcq
type: single
The term of pharmacokinetics includes all of the following
EXCEPT?
a) Clinical response to a drug ie; toxicity & efficacy
b) Drug concentration at site of action
c) Dose of drug administered

### PHARM-P-013
tier: open
form: mcq
type: single
The volume of distribution (Va) for a drug highly bound to
plasma protein as compared to others would be?
a) High
b) Low
c) Unchanged
d) Cannot be determined, it's an apparent parameter

### PHARM-P-014
tier: open
form: mcq
type: single
Factors associated with drug absorption that can result in
incomplete absorption
a) Drug metabolism by gastrointestinal flora
b) Drug instability in gastric acid
c) Presence of food in the GI tract
d) A and B
e) A B, and C

### PHARM-P-015
tier: open
form: mcq
type: single
Patient's age may affect a drug elimination
a) True
b) False

### PHARM-P-016
tier: open
form: mcq
type: single
Warfarin is metabolized by CYP450, and rifampicin is CYP450
inducer. Administration of warfarin and rifampicin together will
a) Rifampicin will decrease therapeutic effectiveness of warfarin
b) Rifampicin will increase the side effect of warfarin
c) Rifampicin of no effect on therapeutic effect of warfarin
d) Both A and B

### PHARM-P-017
tier: open
form: mcq
type: single
Dose adjustment is needed in the following situation EXCEPT
a) Elderly and newborn patients
b) Patients with renal and hepatic problems.
c) Patients with lung diseases
d) Patient with heart failure

### PHARM-P-018
tier: open
form: mcq
type: single
A type of absorption is called () Appears to depend on an
oscillating carrier protein, depends on concentration gradient, no
energy required. For a few drugs movement occurs faster than
predicted.
a) Active transport
b) Passive transport
c) Facilitated diffusion.
d) Simple diffusion

### PHARM-P-019
tier: open
form: mcq
type: single
In case of severe renal dysfunction, the duration of action of
most drugs:
a) Increases
b) Decreases
c) Will not change

### PHARM-P-020
tier: open
form: mcq
type: single
The onset of effect for a drug given orally is the time for the
drug to:
a) Reach the peak plasma concentration.
b) Reach the minimum effective concentration.
c) Reach the concentration of steady state.
d) Begin to be within the therapeutic concentration.
e) To be absorbed from the small intestine

### PHARM-P-021
tier: open
form: mcq
type: single
The therapeutic range is the range of plasma drug
concentrations that clearly defines optimal drug therapy and where
adverse effects cannot occur.
a) True
b) False

### PHARM-P-022
tier: open
form: mcq
type: single
img: flagged/PHARM-P-022-first-order-kinetics-figure.png
note: Page 6 carries an unreferenced semi-log concentration-vs-time plot (straight
  line on log-linear axes). No option explicitly says "see figure," but option c)
  ("the time vs. plasma drug concentration profile is as follow") trails off as if
  pointing at one, and this is the only figure on the page — plausible tie, not
  certain, kept as evidence either way.
Which of the following statements best describes first-order
kinetics?
a) The same fraction of drug is eliminated during a given time interval
b) The same amount of drug is eliminated during a given time interval
c) The time vs. plasma drug concentration profile is as follow
d) Both A and C

### PHARM-P-023
tier: open
form: mcq
type: single
In case of liver disorders accompanied by a decline in
microsomal enzyme activity the therapeutic effect of this treatment
will be:
a) Decreased
b) Increased
c) Remained unchanged

### PHARM-P-024
tier: open
form: mcq
type: single
Half-life (t %) doesn't depend on:
a) Rate of metabolism
b) Concentration of a drug in plasma
c) Rate of drug elimination
d) Time of drug absorption

### PHARM-P-025
tier: open
form: mcq
type: single
Oral bioavailability of the drug could be affected by which of the
following:
a) Gastric acidity and gastric enzymes
b) Drug formulation
c) Metabolism by liver enzymes prior to reaching the systemic circulation
d) Expression of intestinal P-glycoprotein
e) All the above

### PHARM-P-026
tier: open
form: mcq
type: single
Alkalinization of urine hastens (facilitates) the excretion of
weakly basic drugs:
a) True
b) False
c) False, it hastens acidic drug excretion

### PHARM-P-027
tier: open
form: mcq
type: single
A small Vd has an important influence on the half-life of a drug,
this means that a drug with small Vd has short half-life.
a) True
b) False
c) Maybe true, but not important at all

### PHARM-P-028
tier: open
form: mcq
type: single
Treatment of pediatric patients sometimes requires considering
age- appropriate dosage forms. For example, when treating a 4 year
old boy with an inner ear infection, the antibiotic dosage
formulation most acceptable to them would be alan:
a) Capsule
b) Oblong large tablet
c) Oral suspension
d) Normal tablet

### PHARM-P-029
tier: open
form: mcq
type: single
Which of the following phase II metabolic reactions make phase
I metabolites readily excretable in urine?
a) Oxidation
b) Reduction
c) Alcohol dehydrogenation
d) Glutathione conjugation
e) None of them

### PHARM-P-030
tier: open
form: mcq
type: single
Which of the following drugs/or substances may inhibit the
hepatic microsomal P450 responsible for the metabolism of
substrate drugs
a) Grapefruit juice
b) Ethanol
c) Rifampin
d) Smoking

### PHARM-P-031
tier: open
form: mcq
type: single
The term bioavailability of a preparation of a drug is a measure
of:
a) The relative toxicity of the preparation to laboratory animals
b) The stability of the preparation
c) The availability of the drug from natural sources
d) We simply say: BIOAVAILABLE! Means available to patients
e) None of the above

### PHARM-P-032
tier: open
form: mcq
type: single
If 3 g of a drug are added and distributed throughout a tank and
the resulting concentration is 0.15 g/L, calculate the volume of the
tank.
a) 10 L
b) 20 L
c) 30 L
d) 200 L

### PHARM-P-033
tier: open
form: mcq
type: single
img: flagged/PHARM-P-033-ultron-dose-response-figure.png
note: The stem's "three dose response relationships" are the figure on page 9 —
  % patients vs. plasma concentration curves for hiccups suppressed (desired
  effect), facial flushing, and vomiting (the toxic effect the stem names). The
  therapeutic index calculation this question asks for depends on reading EC50/TD50
  off this curve, so it is load-bearing.
"Ultron" is a new drug for the treatment of hiccups. When
administered over a wide concentration range, three dose response
relationships were defined in tested subjects. Using vomiting as an
unwanted (toxic) effect, what would be the estimated therapeutic
index for "Ultron"?
a) 0.01
b) 0.1
c) 10
d) 100

### PHARM-P-034
tier: open
form: mcq
type: single
Metabolic transformation and conjugation usually results in an
increase of a substance biological activity
a) True
b) False

### PHARM-P-035
tier: open
form: mcq
type: single
Generally, the rate of drug absorption is most rapid when the
drug is formulated as a
a) Hard gelatin capsule
b) Solution, e.g syrup
c) Controlled.release product
d) compressed tablet

### PHARM-P-036
tier: open
form: mcq
type: single
Ampicillin is eliminated by first-order kinetics. Which of the
following statements best describes the process by which the
plasma concentration of this drug declines
a) The drug is distributed to only 1 compartment outside the vascular system
b) The drug is largely metabolized in the liver after oral administration and has low bioavailability
c) The rate of elimination is proportional to the rate of administration at all times
d) The halflife is the same regardless of the plasma concentration

### PHARM-P-037
tier: open
form: mcq
type: single
What is implied by {{passive transport}}
a) Transport without energy consumption
b) Engulf of drug by a cell membrane with a new vesicle formation
c) Transport of drugs through a membtane by means of diffusion
d) Transport against conæntration gradient

### PHARM-P-038
tier: open
form: mcq
type: single
Drug metabolism is mainly done in the kidneys and is responsible
for drug elminnation
a) True
b) False

### PHARM-P-039
tier: open
form: mcq
type: single
Concerning renal clearance, which of the following is correct
a) Influenced by renal disease
b) None of them
c) Both of them
d) Altered by blood flow

### PHARM-P-040
tier: open
form: mcq
type: single
If the plasma concentration Of a drug declines with "first-order
kinetics," this means that
a) The half-life is thesame regardless of the plasma concentration
b) There Is Only one metabolic for drug disposition
c) The drug is largely metabolized in the liver aftel oral administration and has low bioavailability
d) All of them

### PHARM-P-041
tier: open
form: mcq
type: single
you want to enhance urine elimination of a basic drug, you need
to make the urine
a) More alkaline
b) More acidic
c) Urine pH of no effect

### PHARM-P-042
tier: open
form: mcq
type: single
The oral bioavailability of most of drugs is less than 100%
because
a) Both
b) Incomplete absorption
c) Neither
d) First pass effect

### PHARM-P-043
tier: open
form: mcq
type: single
Which statement best describes bioavailability
a) All
b) Measurement of the rate and amount of the unchanged drug reaches the systemic circulation
c) Amount of the drug destroyed in the liver before entering systemic circulation
d) Measurement of the relative toxicity of the preparation
e) Movement of drug into body tissues over time

### PHARM-P-044
tier: open
form: mcq
type: single
Fill the blanks-----------: In case of liver cirrhosis, half-life is---------
for paracetamol and should be used in
a) Decreased, higher doses
b) Increased, lower doses
c) Decreased, lower doses
d) Increased, higher doses

### PHARM-P-045
tier: open
form: mcq
type: single
The correct sentence/ s concerning prodrug is/are
a) An active drug that is transformed in the body to an inactive metabolite
b) Means inactive drug that is transformed in the body to an active metabolite
c) None of them
d) Medications that are transformed in the bods into toxic metabolites
e) Mostly, medications are prodrugs

### PHARM-P-046
tier: open
form: mcq
type: single
Smoking is enzyme inhibitor; this can increase the half-life of
theophylline in those who are smokers
a) True
b) False

### PHARM-P-047
tier: open
form: mcq
type: single
Which of the following is not a pharmacokinetics process
a) Drug metabolites are removed in the urine
b) The drug causes dilation of coronary vessels
c) Movement of drug from the gut into circulation
d) Alteration of the drug by liver enzymes
e) The drug is readily deposited in fat tissue

### PHARM-P-048
tier: open
form: mcq
type: single
Regarding renal excretion, the following are with importance to
be considered
a) Glomerular filtration rate
b) Extent of plasma protein binding of drugs
c) Active renal tubular reabsorption
d) All of them
e) Re-absorption in distal tubules

### PHARM-P-049
tier: open
form: mcq
type: single
Regarding biotransformation
a) CYP2D6 accounts for the majority of P450 activity
b) Phase one reactions always precede phase two reactions
c) water conjugation is a phase one reaction
d) None of them

### PHARM-P-050
tier: open
form: mcq
type: single
AII the following statements are correct concerning intravenous
drug administration EXCEPT
a) It is painful and stressful for the patient
b) Drugs undergo first-pass metabolism
c) A trained staff is required
d) Risk of bacterial contamination at the site of injection

### PHARM-P-051
tier: open
form: mcq
type: single
A 12-month-old infant is hospitalized for nausea, vomiting,
fevers. He is placed on a rectal treatment to treat the nausea and
vomiting. Which of the following statements is true about this route
of administration
a) Rectal irritation following administration is uncommon
b) Rectal administration ot medications is well accepted
c) Maximal biotransformation of the drug by the liver
d) Useful if patient is unconscious or vomiting
e) Allows destruction of the medication by gastric enzymes

### PHARM-P-052
tier: open
form: mcq
type: single
The IV administration of drugs are
a) Rapidly excreted by renal
b) Undergoes the first-pass metabolism
c) Rapidly absorbed
d) bioavailable 100%

### PHARM-P-053
tier: open
form: mcq
type: single
The same dose of Four different drugs was administered IV to
the same lab animal on four different occasions. The following
pharmacokinetic data were obtained: Drug Plasma concentration):
for drug A 25 ng/mL Drug B: 12 ng/mL Drug C: 44 ng/mL
Drug D:90ng/ml. which of the following drugs will have the lowest
Vd the following drugs will have the lowest Vd
a) Drug C
b) Drug B
c) Drug A
d) DrugD

### PHARM-P-054
tier: open
form: mcq
type: single
33 year old female patient is brought to emergency department
due to drug overdose and acute toxicity. Which routes of
administration is desirable for antidote administration
a) I.V
b) S.L
c) Orally
d) S.C

### PHARM-P-055
tier: open
form: mcq
type: single
Clopidogrel (pro-dug) is metabolized by CYP450 is taken with
rifampicin which is a CYP450 inducer. This will lead to
a) No effect on therapeutic effect of Clopidogrel
b) Increase therapeutic response of Clopidogrel
c) Decrease therapeutic response of Clopidogrel
d) Decrease the plasma concentration of Clopidogrel active metabolite

### PHARM-P-056
tier: open
form: mcq
type: single
Which statement about the distribution of drugs to specific
tissues is most correct
a) Distribution to an organ is independent of blood flow
b) Distribution has no effect on the half-life ot the drug
c) Distribution depends on the unbound drug concentration gradient between blood and the tissue
d) Dist ution is independent of the solubility of the drug in that tissue
e) Distribution is increased for drugs that are strongly bound to plasma vroteins

### PHARM-P-057
tier: open
form: mcq
type: single
Therapeutic index (Tl) is
a) ratio used to evaluate the elimination of a drug
b) ratio used to evaluate the safely and usefulness of a drug for indication
c) ratio used to evaluate the bioavailability of a drug
d) ratio used to evaluate the effectiveness of a erug

### PHARM-P-058
tier: open
form: mcq
type: single
Principal organ/s for biotransformation of drugs is/are
a) Kidney
b) Kidney and liver
c) Lung
d) Liver
e) Skin

### PHARM-P-059
tier: open
form: mcq
type: single
Advantages of the rectal route of drug administration are
a) Suitable for children
b) A way to avoid first-pass metabolism. even partially
c) All of them
d) Suitable for unconscious patients
e) Suitable for children and unconscious patients

### PHARM-P-060
tier: open
form: mcq
type: single
Binding of a drug to plasma proteins will tend to?
a) Decrease half-life.
b) Decrease its rate of glomerular filtration.
c) Increase its rate of biotransformation.
d) None

### PHARM-P-061
tier: open
form: mcq
type: single
Compared to the average adult dose, the recommended dose of
a drug for elderly a patients will likely be?
a) Less than average due to increased biotransformation.
b) Less than average due to decreased renal function or excretion
c) More than average due to decreased plasma protein binding capacity.
d) More than average due to increased renal excretion.

### PHARM-P-062
tier: open
form: mcq
type: single
Which one of the following statements is applicable to
absorption of drugs from the gastrointestinal tract?
a) Absorption of weak acids occurs only from the stomach and not from the small intestine.
b) Some drugs are metabolized extensively by the liver and do not reach the general circulation (first-pass effect)
c) Ingesting drugs with food always enhances drug absorption.
d) None

### PHARM-P-063
tier: open
form: mcq
type: single
A patient is treated chronically with a drug (A) metabolized by
CYP 3A4. Recently he administer another drug (B) which is an
enzymatic inducer of the CYP2D6. Which of the following is likely to
occur?
a) Longer half life of drug (A)
b) Longer half life of drug (B)
c) Enhanced pharmacological effect of drug A
d) No significant drug interaction
e) Reduced pharmacological effect of drug B

### PHARM-P-064
tier: open
form: mcq
type: single
In general, biotransformation usually results in a product, which
is more?
a) Likely to produce side effects.
b) Likely to distribute intracellularly.
c) Lipid soluble than the original drug.
d) Likely to be reabsorbed by kidney tubules.
e) Water soluble than the original drug

### PHARM-P-065
tier: open
form: mcq
type: single
Enzyme inhibitors such as Cimetidine and Erythromycin are
likely to produce?
a) Increase rate of breakdown of some drugs
b) Increase free level of some drugs
c) Inhibition of certain enzymes. which break down some drugs.
d) Improvement of bioavailability of some drugs

### PHARM-P-066
tier: open
form: mcq
type: single
What does "affinity" mean?
a) A measure of how tightly a drug binds to plasma proteins
b) measure of how tightly a drug binds to a receptor
c) measure of inhibiting potency ofa drug
d) A measure of bioavailability ofa drug

### PHARM-P-067
tier: open
form: mcq
type: single
Target proteins, which a drug molecule could bind, is/are ?
a) Only receptors
b) Only ion channels
c) Only carriers
d) All

### PHARM-P-068
tier: open
form: mcq
type: single
An agonist is a substance that ?
a) Interacts with the receptor without producing any effect
b) Interacts with the receptor and initiates changes in cell function, producing various effects
c) Increases concentration of another substance to produce effect
d) Interacts with plasma proteins and doesn't produce any effect

### PHARM-P-069
tier: open
form: mcq
type: single
A competitive antagonist is a substance that ?
a) Interacts with receptors and produces submaximal effect
b) Binds to the same receptor site and progressively inhibits the agonist response
c) Binds to the nonspecific sites of tissue
d) None of them

### PHARM-P-070
tier: open
form: mcq
type: single
Tick the second messenger of G-protein-coupled (metabotropic)
receptor ?
a) Adenylyl cyclase
b) Sodium ions
c) Phospholipase C
d) cAmp

### PHARM-P-071
tier: open
form: mcq
type: single
What is the type Of drug-to-drug interaction, which is
connected, with processes of
absorption, biotransformation, distribution and excretion?
a) Pharmacodynamic interaction
b) Physical and chemical interaction
c) Pharmaceutical interaction
d) Pharmacokinetic interaction

### PHARM-P-072
tier: open
form: mcq
type: single
The term "chemical antagonism" means that?
a) Two drugs combine with one another to form an inactive compound
b) Two drugs combine with one another to form a more active compound
c) Two drugs combine with one another to form a more water soluble compound
d) Two drugs combine with one another to form a more fat soluble compound

### PHARM-P-073
tier: open
form: mcq
type: single
Idiosyncratic reaction of a drug is?
a) A type of hypersensitivity reaction
b) A type of drug antagonism
c) Unpredictable, inherent, qualitatively abnormal reaction to a drug
d) Quantitatively exaggerated response

### PHARM-P-074
tier: open
form: mcq
type: single
Therapeutic index (TI) is?
a) ratio used to evaluate the safety and usefulness ofa drug for indication
b) ratio used to evaluate the effectiveness of a drug
c) A ratio used to evaluate the bioavailability ofa drug
d) A ratio used to evaluate the elimination ofa drug

### PHARM-P-075
tier: open
form: mcq
type: single
A hydrophilic medicinal agent has the following property?
a) ability to penetrate through the cell membrane lipids
b) Penetrate through membranes by means of endocytosis
c) Easy permeation through the blood-brain barrier
d) High reabsorption in renal tubules

### PHARM-P-076
tier: open
form: mcq
type: single
What is implied by «active transport»?
a) Transport of drugs through a membrane by means of diffusion
b) Transport without energy consumption
c) Engulf of drug by a cell membrane with a new vesicle formation
d) Transport ae22t concentration gradient

### PHARM-P-077
tier: open
form: mcq
type: single
What does the term "bioavailability" mean?
a) Plasma protein binding degree of substance
b) Permeability through the brain-blood barrier
c) Fraction of an uncharged drug reaching the systemic circulation following any route administration
d) Amount ofa substance in urine relative to the initial dose

### PHARM-P-078
tier: open
form: mcq
type: single
Pick out the appropriate route of administration when passage or
drugs through liver is partially decreased?
a) Oral
b) Transdermal
c) Rectal
d) Intraduodenal

### PHARM-P-079
tier: open
form: mcq
type: single
What is characteristic of the intramuscular route of drug
administration?
a) Only water solutions can be injected
b) Oily solutions can be injected —depot injections
c) Opportunity of hypertonic solution injections
d) The action develops slower, than at oral administration

### PHARM-P-080
tier: open
form: mcq
type: single
Drug distribution: Most of drugs are distributed homogeneously?
a) True
b) False

### PHARM-P-081
tier: open
form: mcq
type: single
The term "biotransformation" includes the following?
a) Accumulation of substances in a fat tissue
b) Binding of substances with plasma proteins
c) Accumulation of substances in a tissue
d) process of physicochemical and biochemical alteration of a drug in the body

### PHARM-P-082
tier: open
form: mcq
type: single
note: The source itself has no option d) — the printed choices skip from c) to e).
  Not a Job A drop; nothing invented to fill the gap.
Which of the following characteristics is most likely to be
associated with a high apparent volume of distribution?
a) High hepatic extraction ratio-e
b) Extensive binding to plasma protein
c) Distribution into total body water
e) Extensive binding to tissue constituents

### PHARM-P-083
tier: open
form: mcq
type: single
A characteristic of drugs eliminated by zero order kinetic
processes is that the half-life is not constant?
a) True
b) False

### PHARM-P-084
tier: open
form: mcq
type: single
The rate of drug transport across a cell membrane by lipid
diffusion depends on all of the following EXCEPT?
a) Drug size (diffusion constant)
b) Surface area of absorption
c) Lipid partition coefficient
d) Density of transporters
e) Concentration gradient

### PHARM-P-085
tier: open
form: mcq
type: single
The volume of distribution of gentamicin, a highly polar water-
soluble drug, is 14L
per 70 kg. This reflects the distribution of gentamicin into?
a) Plasma
b) Plasma, and interstitial fluid (extracellular)
c) Interstitial fluid
d) Total body water
e) Adipose tissue

### PHARM-P-086
tier: open
form: mcq
type: single
For continuous intravenous infusion as method of
administration the time needed to achieve the concentration of
steady state depends on the rate of drug administration?
a) True
b) False

### PHARM-P-087
tier: open
form: mcq
type: single
The half-life of a drug eliminated by first order elimination
kinetics will be LONGER in individuals who have a/an?
a) Increased volume of distribution or increased clearance
b) Increased volume of distribution or decreased clearance
c) Decreased volume of distribution or increased clearance
d) Decreased volume of distribution or decreased clearance

### PHARM-P-088
tier: open
form: mcq
type: single
For drugs that have first order kinetics, after 4 half-lives about
drug will be eliminated?
a) 50%
b) 75%
c) 93%
d) 100%

### PHARM-P-089
tier: open
form: mcq
type: single
The half-life of the drug is important to determine all of the
following EXCEPT?
a) Clearance V
b) Dosing interval
c) Time to reach css
d) Therapeutic dose

### PHARM-P-090
tier: open
form: mcq
type: single
The concentration of steady state (css) will increase when?
a) Increase the rate of infusion
b) Decrease the rate of metabolism
c) Decrease excretion
d) All
e) None

### PHARM-P-091
tier: open
form: mcq
type: single
To calculate half-life we use which the following formula?
a) 0.693 x Css/Cl
b) 0.693 x Vd/
c) 0.693 x Cl/Vd
d) Tv-z= 0.693 x dose / Cl

### PHARM-P-092
tier: open
form: mcq
type: single
The drug concentration between MEC and MTC is?
a) Therapeutic window
b) Therapeutic index
c) Area under the curve
d) Duration of action

### PHARM-P-093
tier: open
form: mcq
type: single
The correct sentence concerning parenteral administration is?
a) It is too slow for emergency
b) Cannot be used with unconscious patient
c) May produces a more rapid side effects than oral administration
d) Have lower bioavailability comparing to other route of administration

### PHARM-P-094
tier: open
form: mcq
type: single
note: Option b) carries a trailing Arabic annotation, "غير مؤكد" ("not certain") —
  not Moodle interface chrome (this is a document, not a Moodle capture), so it
  reads as the compiler's own doubt about that option and is kept rather than
  discarded.
Systemic clearance will increase when?
a) Volume of distribution increased
b) Rate of metabolism increase غير مؤكد
c) GFR decrease
d) All

### PHARM-P-095
tier: open
form: mcq
type: single
Controlled-release tablets are formulated to release the drug in
intestine to decrease the effect of gastric pH on it?
a) True
b) False

### PHARM-P-096
tier: open
form: mcq
type: single
Which of the following may induce the hepatic microsomal P450
responsible for the metabolism of some drugs?
a) Smoking
b) Ethanol
c) High protein diet
d) All

### PHARM-P-097
tier: open
form: mcq
type: single
Drug X produces maximal contraction of cardiac muscle in a
manner similar to epinephrine. Drug X is considered to be a/an?
a) Partial agonist
b) Irreversible antagonist
c) Agonist
d) Inverse agonist

### PHARM-P-098
tier: open
form: mcq
type: single
All of the following concerning the blood-brain barrier (BBB)
and the passage of drugs from the systemic circulation to
cerebrospinal fluid (CSF) is true EXCEPT?
a) Ionized drugs are likely to cross into the CSF than unionized drugs
b) The higher the lipid solubility ofa drug, the more likely it will cross into the CSF
c) Inflammation of the meninges improves the likelihood that drugs will cross the BBB as
d) P glycoprotein serves to pump back the drugs into the systemic circulation from endothelial cell linings of the BBB

### PHARM-P-099
tier: open
form: mcq
type: single
Drug concentration at the receptor site is influenced by all of
the following except?
a) Drug dose
b) Drug Metabolism
c) Allosteric interaction with the microsomal enzymes
d) Elimination Rate

### PHARM-P-100
tier: claimed
form: mcq
type: single
claimed: b
The science concern about the diagnosis, prevention and treatment of
human?
a) Toxicology
b) Medical pharmacology
c) pharmacodynamics
d) Pharmacy
e) Pharmacokinetics

### PHARM-P-101
tier: claimed
form: qa
claimed: Prolonged use of receptor agonist
All of the following are true regarding receptor up-regulation,
EXCEPT?

### PHARM-P-102
tier: claimed
form: qa
claimed: NaHCO2
Which of the following make the urine alkane ?

### PHARM-P-103
tier: claimed
form: qa
claimed: Affinity and no intrinsic activity
Antagonist has:

### PHARM-P-104
tier: claimed
form: mcq
type: single
claimed: a
img: flagged/PHARM-P-104-route-of-administration-figure.png
note: The figure is a plasma-concentration-vs-time curve (rise to peak, then decay)
  labeled with MTC, MEC, peak time, and AUC — the stem explicitly says "look
  carefully at this figure," so the image is load-bearing for the answer.
Look carefully at this figure What is the route of administration used?
a) oral
b) Rectal
c) Intravenous bolus injection
d) Intravenous infusion
e) Inhalation

### PHARM-P-105
tier: claimed
form: qa
claimed: ED50
What is the median effective dose , or the 50% of the individuals give
the quantal effective response?

### PHARM-P-106
tier: claimed
form: qa
claimed: IV bolus
the route of inflammation?

### PHARM-P-107
tier: claimed
form: qa
claimed: 130 L
Dose 650 ,Plasma conc=5 ,Vd=??

### PHARM-P-108
tier: claimed
form: qa
claimed: 7 hr
T1/2 if VD=200 and CL=20

### PHARM-P-109
tier: claimed
form: qa
claimed: Lipid diffusion
the most important mechanism for drugs to enter the body ?

### PHARM-P-110
tier: claimed
form: qa
claimed: orally
the safest and affordable way for taking drugs is?

### PHARM-P-111
tier: claimed
form: qa
claimed: it is the volume of blood or plasma that is completely cleared of drug per unit time
drug clearance :

### PHARM-P-112
tier: claimed
form: qa
claimed: sodium bicarbonate
to excrete weak acids faster in urine ,we give the patient :

### PHARM-P-113
tier: claimed
form: qa
claimed: CYP3A4
which of the following is responsible for the metabolism of more
than 50% of prescription drugs metabolized in the liver ?

### PHARM-P-114
tier: claimed
form: qa
claimed: drugs absorbed from GIT must pass through the gut wall and portal vein to the liver before reaching the systemic circulation
First pass effect is:

### PHARM-P-115
tier: claimed
form: qa
claimed: it is the fraction of the uncharged active drug reaching the systemic circulation ,following drug administration ,irrespective of the route .
Bioavailability :

### PHARM-P-116
tier: claimed
form: qa
claimed: is the science that deals with the use of drugs for diagnosis, prevention and treatment of human disease .
the medical pharmacology is:

### PHARM-P-117
tier: claimed
form: qa
claimed: the drug concentration is high in tissue proteins .
the high VD means :

### PHARM-P-118
tier: claimed
form: qa
claimed: it needs single dose
the wrong about steady state is:

### PHARM-P-119
tier: claimed
form: qa
claimed: the drugs always safe.
the wrong sentence is :

### PHARM-P-120
tier: claimed
form: qa
claimed: Tolerance
the patient was taking a drug for along period of time, as a result the
responsiveness to the drug by his body decreased what we mean by
that?

### PHARM-P-121
tier: claimed
form: qa
claimed: produce high initial concentration of the drug that might be toxic
the disadvantage of giving the drug IV is ?

### PHARM-P-122
tier: claimed
form: mcq
type: single
claimed: b
img: flagged/PHARM-P-122-embedded-therapeutic-window-question.png
note: Embedded as an image on page 29 (real PDF page), not present in the page's
  text layer at all — invisible to a text-only read. Transcribed from the image
  directly. The image shows a Moodle-style capture with option b) already
  highlighted/selected, which is the claim recorded here, same as any other
  hand-marked or pre-selected claimed answer.
Given the information shown in the figure below, which of the following statements is correct?
a) Drug A has the most appropriate pharmacodynamic properties of the three drugs shown as it reaches maximal efficacy within the therapeutic window.
b) Drug B has the most appropriate pharmacodynamic properties of the three drugs shown as a range of its plasma concentrations are within the therapeutic window.
c) Drug C has the most appropriate pharmacodynamic properties of the three drugs shown as non-toxic effects are achieved within the therapeutic window.
d) All three drugs have appropriate pharmacodynamic properties as they all achieve maximal physiological effects and have concentrations within the therapeutic window.

### PHARM-P-123
tier: claimed
form: mcq
type: single
claimed: a
Clonidine reflex hypertension which @-blocker we use to produce
hypotension?
a) prazosin
b) Phen…
c) Phen…..

### PHARM-P-124
tier: claimed
form: mcq
type: single
claimed: b
Used to provide short term relief of heart failure symptom:
a) fenoldopam
b) dopamine
c) isoproterenol
d) ritodrine
e) ephedrine

### PHARM-P-125
tier: claimed
form: mcq
type: single
claimed: b
All of the following activate adenylyl cyclase and increase con. cAMP
except
a) d1
b) d2
c) b1
d) b2
e) b3

### PHARM-P-126
tier: claimed
form: qa
claimed: Nafcillin
Used to treat toxic shock syndrome?

### PHARM-P-127
tier: claimed
form: mcq
type: single
claimed: b
Not affected by muscrinic receptors?
a) Atrioventricular node
b) uterus
c) Sphenicter of iris muscle

### PHARM-P-128
tier: claimed
form: mcq
type: single
claimed: c
Atropine overdose cause each of the following excet?
a) Delirium
b) Tachycardia
c) Sedation

### PHARM-P-129
tier: claimed
form: mcq
type: single
claimed: a
Pilocarpine produce hypertension after initial hypotension via which
RECEPTOR?
a) M1
b) M2
c) M3

### PHARM-P-130
tier: claimed
form: mcq
type: single
claimed: d
Among the following which is not a true sentence:
a) The cell walls of bacteria are essential for their normal growth
b) Peptidoglycan provides rigid mechanical stability tor bacterial cell wall
c) In gram-positive bacteria the cell wall is 50 to 100 molecules thick
d) The cell wall is 50 to 100 molecules thick in gram-negative bacteria
e) All the above

### PHARM-P-131
tier: claimed
form: mcq
type: single
claimed: e
Among the following which is the least resistant to B-lactamases:
a) Nafcillin
b) Oxacillin
c) Cloxacillin
d) Dicloxacillin
e) Penicillin

### PHARM-P-132
tier: claimed
form: mcq
type: single
claimed: d
Sulphonamides are almost obsolete nowadays because of all the
following except:
a) Bacterial resistance
b) Their Toxicity
c) Their Bacteriostatic properties
d) Their bactericidal effects
e) They are associated with Blood dyscrasia

### PHARM-P-133
tier: claimed
form: mcq
type: single
claimed: c
Regarding Static effects of chemotherapeutic drug which is false:
a) Occurs when the toxic effects of a chemotherapeutic drug are reversible
b) Depends on the pharmacological properties of the drug
c) Occurs when the toxic effects of a chemotherapeutic drug are irreversible
d) Depends on the immune system function
e) All the above

### PHARM-P-134
tier: claimed
form: mcq
type: single
claimed: d
All the following B-lactamase inhibitor combinations are parenteral
formulations except
a) ampicillin-sulboctam
b) ticorcillin-clavulanic ocid
c) piperacillin-tazobactam
d) amoxicillin-clauvlanic acid
e) All of the above

### PHARM-P-135
tier: claimed
form: mcq
type: single
claimed: b
Defining therapeutic success of pneumonia involves All of the
following except
a) Purulent sputum production
b) Frequency of dosing
c) Normalization of the white blood cell count
d) Reversal of tachypnea and hypoxia
e) Resolution of fever

### PHARM-P-136
tier: claimed
form: mcq
type: single
claimed: c
Regarding Sulfonamides, which is true
a) They are considered as structural agonists of para-aminobenzoic acid(PABA)
b) They are considered as structural analogs and competitive antagonists of Folic acid
c) They are considered as structural analogs and competitive antagonists of para-aminobenzoic acid (PABA)
d) They are considered as structural antagonists of penicillin
e) None of the above

### PHARM-P-137
tier: claimed
form: mcq
type: single
claimed: d
Regarding antibiotics which is true
a) Patients should not be instructed to continue antibiotics for the full duration indicated if they feel better to avoid resistance
b) If the patient's recovery is delayed from what is reasonably expected the diagnosis should not be reconsidered
c) Influenza pneumonia and viral upper respiratory infections for example are usually controlled by antibiotics
d) Many patients receive lengthy courses of antibiotics that probably should not have been started
e) All of the above

### PHARM-P-138
tier: claimed
form: mcq
type: single
claimed: c
Regarding chemotherapy whice it is true
a) The less closely related the undesirable cells are the normal human cell,the more difficult the task of finding a magic bullet
b) The more closely related the undesirable cells are the normal human cell,the less difficult the task of finding a magic bullet
c) The more closely related the undesirable cells are the normal human cell,the more difficult the task of finding a magic bullet
d) Effective chemotherapeutic drug are not affective by the common legacy human share with all living organism
e) None of the above

### PHARM-P-139
tier: claimed
form: mcq
type: single
claimed: a
the synergism that occurs between aminoglycoside and B-lactam
antibiotic drug is partially due to which of the following
a) B-lactam antibiotics will reverse the negative effects of both low pH and low oxygen tension on the ability of amionglycosides to penetrate bacteria.
b) B-lactam antibiotics will decrease pH and insduse aminoglycosides to penetrate bacteria.
c) B-lactam antibiotics will decrease oxygen and induce aminoglycosides to penetrate bacteria.
d) B-lactam antibiotics will decrease pH and inhibit aminoglycosides to penetrate bacteria.
e) All the above.

### PHARM-P-140
tier: claimed
form: mcq
type: single
claimed: d
regarding Beta lactam Antibiotics which is false
a) All contain a beta lactam ring
b) Work to inhibit cell wall synthesis
c) The beta lactam ring is the active functional group where antibiotic activity resides
d) Work to inhibit protein biosynthesis
e) All the above

### PHARM-P-141
tier: claimed
form: mcq
type: single
claimed: b
Regarding the clinical uses of nitrofurantoin which is false
a) The singular indication for nitrofurantoin is the treatment and long-term prophylaxis of lower UTIS caused by susceptible bacteria
b) it is used as a bacterial suppressant
c) It is often used prophylactically post intercourse in women with chronic UTIS
d) The bacteriostatic or bactericidal activity of nitrofurantoin is concentration dependent
e) None of the above

### PHARM-P-142
tier: claimed
form: mcq
type: single
claimed: d
Regarding the quinolone antibiotics which of the following is true
a) The quinolone antibiotics target bacterial RNA gyrase and Topoisomeras
b) The quinolone antibiotics target bacterial DNA gyrase and Topoisomeras which is responsible for the continuous introduction of positive supercoils into RNA
c) The quinolone antibiotics target bacterial viral gyrase
d) The quinolone antibiotics target bacterial DNA gyrase and Topoisomeras which is responsible for the continuous introduction of negative supercoils into DNA
e) None of the above

### PHARM-P-143
tier: claimed
form: mcq
type: single
claimed: a
Regarding Erythromycins which is true
a) It has Same spectrum of penicillin, so substitutes in penicillin allergic patients.
b) It has very limited distribution in the body
c) It Cannot be given orally
d) Very toxic cannot be given to children
e) All the above
note: Option e) reads "All the above Clear my choice" in the source — "Clear my
  choice" is a leaked Moodle terminator string (job-a-extract.md lists it as a
  close anchor), not part of the option content, so it is dropped here.

### PHARM-P-144
tier: claimed
form: mcq
type: single
claimed: e
Resistance to Chloramphenicol is due to
a) Changes in the ribosome binding site
b) Decreased affinity for the drug
c) Decreased permeability
d) Plasmids that code for enzymes that degrade it
e) All of the above

### PHARM-P-145
tier: claimed
form: mcq
type: single
claimed: d
Cefepime is…
a) First generation
b) Second generation
c) Third generation
d) Fourth generation
e) Fifth generation

### PHARM-P-146
tier: claimed
form: mcq
type: single
claimed: d
Which of the following does not belong to quinolones
a) Nalidixic acid
b) Norfloxacin
c) Ciprofloxacin
d) Arsenic
e) Gatifloxacin

### PHARM-P-147
tier: claimed
form: mcq
type: single
claimed: b
Among the following which is true sentence
a) The cell walls of bacteria are not essential for their normal growth
b) Peptidoglycan provides rigid mechanical stability tor bacterial cell wall
c) In gram-negative bacteria the cell wall is 50 to 100 molecules thick
d) The cell wall is only 1 or 2 molecules thick in gram-positive bacteria
e) All the above

### PHARM-P-148
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is a 3rd generation cephalosporin that has the
best activity against P. aeruginosa infections
a) Cefixime
b) Cephamandole
c) Cefalexin
d) Cefoperazone
e) Cefepime

### PHARM-P-149
tier: claimed
form: mcq
type: single
claimed: c
The following drug is effective in treatment of meninigitis caused by
Haemophyllus influenzae if administered orally
a) Penicillin G
b) Gentamicin
c) Chloramphenicol
d) Ticarcillin
e) Cefepime

### PHARM-P-150
tier: claimed
form: mcq
type: single
claimed: d
Each of the following statements concerning the mechanism of
action of antimicrobial drugs is correct EXCEPT
a) ß-Lactams interfere with peptidoglycan cross-linking by binding to transpeptidases called PBPS
b) Sulfonamides affect folic acid synthesis in bacteria, a pathway that does not occur in human cells
c) Quinolones, such as ciprofloxacin, act by inhibiting the DNA gyrase of bacteria
d) Macrolides are bactericidal drugs that disrupt cell membranes by a detergent-like action
e) Aminoglycosides are bactericidal drugs that inhibit protein synthesis

### PHARM-P-151
tier: claimed
form: mcq
type: single
claimed: b
The following antibiotics-chemotherapeutic agents are primarily
bactericidal
a) Sulfonamides
b) Aminoglycosides
c) Tetracyclines
d) Chloramphenicol
e) Clarithromycin

### PHARM-P-152
tier: claimed
form: mcq
type: single
claimed: d
Regarding Chloramphenicol which is false
a) Chloramphenicol is rapidly and completely absorbed from the gastrointestinal tract
b) 60% of the drug is bound to serum albumin
c) The potentially fatal nature of chloramphenicol induced bone marrow suppression restricts its use
d) Chloramphenicol is recognized as first choice treatment of choice for any bacterial infection
e) All the above

### PHARM-P-153
tier: claimed
form: mcq
type: multi
claimed: b, d
Regarding the mechanism of action of chloramphenicol, the drug
a) Is bactericid
b) Binds to the 50S ribosomal subunit
c) Causes misreading of the code on the mRNA template
d) Inhibits transpeptidases
e) Stabilizes polysomes

### PHARM-P-154
tier: claimed
form: mcq
type: single
claimed: d
Which of the following antimycobacterial drug inhibits the synthesis
of mycolic acids in bacterial cell wall
a) Daptomycin
b) Vancomycin
c) Basitracin
d) Izoniazid
e) Etambutol

### PHARM-P-155
tier: claimed
form: mcq
type: single
claimed: d
Which of the following antibiotic has an effect on bacterial DNA.
a) Amikacin
b) Bacitracin
c) Teicoplanin
d) Ciprofloxacin
e) Meropenem

### PHARM-P-156
tier: claimed
form: mcq
type: single
claimed: e
Which of the following doesn't belong to Aminoglycosides
a) Gentamicin
b) Tobramycin
c) Streptomycin
d) Neomycin
e) Clarithromycin

### PHARM-P-157
tier: claimed
form: mcq
type: single
claimed: d
Which of the following antibiotics has (have) good activity against
Helicobacter pylori
a) Clarithromycin
b) Tetracycline
c) Azithromycin
d) A and C
e) All of the above

### PHARM-P-158
tier: claimed
form: mcq
type: single
claimed: c
Among the following antibiotics or chemotherapeutic agents, choose
the one which best crosses the blood brain barrier
a) Penicillin
b) Cephalosporins
c) Chloramphenicol
d) Sulfa drugs
e) Macrolides

### PHARM-P-159
tier: claimed
form: mcq
type: single
claimed: d
All of the following are true regarding aminoglycosides; EXCEPT
a) They inhibit bacterial protein synthesis
b) They are bactericidal
c) They do not penetrate the BBB easily
d) Dose adjustment is not necessary in patients with renal impairment
e) They are ineffective orally in the management of meningitis

### PHARM-P-160
tier: claimed
form: mcq
type: single
claimed: a
Which of the following antibiotics you should use for a patient who is
allergic only to penicillin and has been diagnosed to have
enterococci infection
a) Vancomycin
b) Amoxicillin
c) Ceftriaxone
d) Cefepime
e) Cefotaxime

### PHARM-P-161
tier: claimed
form: mcq
type: single
claimed: e
Pseudomembraneous colitis has been reported following the use of
a) Penicillin G
b) Penicillin V
c) Flucloxacillin
d) Cephalexin
e) Clindamycin

### PHARM-P-162
tier: claimed
form: mcq
type: single
claimed: e
Red man syndrome is an adverse effect for which of the following
agents
a) Amoxicillin
b) Imipenem
c) Cefazolin
d) Ceftriaxone
e) Vancomycin

### PHARM-P-163
tier: claimed
form: mcq
type: single
claimed: c
Aplastic anemia is reported complication of
a) Tigecycline
b) Nalidixic acid
c) Chloramphenicol
d) Sulfanilamide
e) Azithromycin

### PHARM-P-164
tier: claimed
form: mcq
type: single
claimed: d
Which is true about pseudomembranous colitis
a) Can be Treated by Vancomycin
b) It never treated by clindamycin
c) It is overgrowth of clostridium difficile
d) All of the above

### PHARM-P-165
tier: claimed
form: mcq
type: single
claimed: d
Parents of a 1-month-old baby are told their child has developed
"gray baby syndrome." Which of the following antibiotics did the
baby likelyreceive
a) Tobramycin
b) Linezolid
c) Ervthromycin
d) Chloramphenicol

### PHARM-P-166
tier: claimed
form: mcq
type: single
claimed: a
Which of the following antibiotics exhibits a long post antibiotic
effect that permits once-daily dosing
a) Gentamicin
b) Penicillin G
c) Vancomycin
d) Aztreonam
e) None of the Above

### PHARM-P-167
tier: claimed
form: qa
claimed: Chloramphenicol
Which of the following causes gray baby syndrome

### PHARM-P-168
tier: claimed
form: qa
claimed: They are not the drugs of first choice for any infection
The wrong statement regarding cephalosporins

### PHARM-P-169
tier: claimed
form: qa
claimed: misused by doctors in the treatment of simple sore throat or URTI
Which of the following is true regarding Lincomycin and Clindamycin

### PHARM-P-170
tier: claimed
form: qa
claimed: Bacteria can resist aminoglycosides by producing lactamase enzyme that breaks the lactam ring
Which of the following is not correct regarding the mechanism of
action of aminoglycosides

### PHARM-P-171
tier: claimed
form: qa
claimed: Clavulanic acid inhibits beta lactamase
Regarding Penicillins, which is true

### PHARM-P-172
tier: claimed
form: qa
claimed: Highly metabolized
Which of the following is false regarding aminoglycosides

### PHARM-P-173
tier: claimed
form: qa
claimed: They cannot be given with other drugs due to the postantibiotic effect of aminoglycosides
note: Source spells this answer's terminator "AMSWER:" (typo for ANSWER), preserved
  as evidence the answer line is genuinely there, not a Job A transcription slip.
Which of the following is not correct regarding the post-antibiotic
effect of aminoglycosides

### PHARM-P-174
tier: claimed
form: qa
claimed: Liberation of formaldehyde
Methenamine effect is due to

<!-- batch 02 — raw/practice/Pharmacology PYQ and Bank Questions.pdf, pages 47-66
  of 134. RUN-PLAN row 10. Two source sections, each its own numbering and its own
  printed answer key -- RUN-PLAN row 10's own "No answers in either" note turned
  out wrong for both halves, the same kind of survey-estimate miss as rows 2 and 5.

    p47-59  "Pharmacology TEST BANK," credited to Ola Nwafleh & Hamza Ja'areh on
            a title-page image at p67 (outside this page range, kept for
            reference only, not transcribed as a question). Numbered 1.-45., no
            inline answers, but a printed answer-key table spans p57-59 covering
            every question -> tier official throughout. Q12 is a two-part
            question (most efficacious / most potent, read off one four-drug
            dose-response graph) whose key entry is "(A) C (B) A" rather than a
            single letter -- split into two `qa` entries (PHARM-P-186,
            PHARM-P-187) sharing one flagged image rather than forcing a
            fabricated mcq option list onto it. PHARM-P-175 through PHARM-P-220
            (46 entries for 45 source questions, the +1 from the Q12 split).
    p60-66  "Pharmacology for dental students (2022/2023)," Dr. Abdulraheem Jabr.
            Numbered 1)-50), no inline answers, but a printed key at the bottom of
            p66 covering every question except #24 (genuinely blank in the
            source's own key, not dropped here) -> tier official for 49, open for
            the one gap. Several pages in this section carry stray single-word
            text fragments ("t", "_i", "It", "REFER", "INNNENNINET" etc.) in an
            Apple system-UI font distinct from the body text -- interface chrome
            bleeding into the text layer, not exam content, and not transcribed
            (same treatment CLAUDE.md gives Moodle's own Arabic chrome).
            PHARM-P-221 through PHARM-P-270.

  Four embedded graphs on p48-50 are load-bearing (therapeutic-index and
  potency/efficacy questions built entirely around a figure) and saved to
  flagged/: PHARM-P-177 (Ultron hiccups/flushing dose-response), PHARM-P-179 (D2
  receptor activity curves A-E), PHARM-P-180 (isoproterenol + Drug X),
  PHARM-P-181 (norepinephrine + Drug X), PHARM-P-186/187 (four-drug
  dose-response, one shared image). Every page 47-66 was checked for embedded
  images (get_images() per page, not just pages a stem names); the only other
  images found were decorative (a logo on p47, a title-page photo on p67 outside
  this range) and were not saved. -->

### PHARM-P-175
tier: official
form: mcq
type: single
answer: e
A 66-year-old man is admitted to the hospital with confusion, nausea, and blurred 
vision. He is currently on digoxin for the treatment of heart failure. On physical exam, 
his heart rate is 120 bpm. Further evaluation reveals a digoxin level of 5.3 ng/mL 
(normal range: 0.5-2 ng/mL). The doctor believes his symptoms are due to digoxin 
toxicity. Which parameter is used to indicate the ability of digoxin to produce the 
desired effect relative to a toxic effect?
a) Bioavailability
b) Efficacy
c) Intrinsic activity
d) Potency
e) Therapeutic index

### PHARM-P-176
tier: official
form: mcq
type: single
answer: c
A 24-year-old female is prescribed erythromycin for gastroparesis. It is prescribed four 
times daily due to its short half-life. What is the rationale for such a frequent dosing?
a) Achieve the steady-state plasma concentration of the drug
b) Aid more complete distribution of the drug
c) Avoid the toxicity of the drug because of its low therapeutic index
d) Ensure that the drug concentration remains constant over time
e) Inhibit the first-pass metabolism of the drug

### PHARM-P-177
tier: official
form: mcq
type: single
answer: c
img: flagged/PHARM-P-177-ultron-hiccup-flushing-graph.png
Your lab group has been evaluating the effects of "Ultron" a new drug for the treatment 
of intractable hiccups. When administered over a wide concentration range, three dose 
response relationships were defined in test subjects. Using facial flushing as an 
unwanted side effect, what would be the estimated therapeutic index for Ultron?
a) 0.1
b) 100
c) 10
d) Can’t determine

### PHARM-P-178
tier: official
form: mcq
type: single
answer: b
Digoxin is a drug that has been used to treat systolic heart failure for over 200 years. It 
has a therapeutic index value of 2. How many daily doses of digoxin will the average 
patient have to take at one time to have a 50:50 chance of developing toxic side effects?
a) One
b) Two
c) I don’t know

### PHARM-P-179
tier: official
form: mcq
type: single
answer: b
img: flagged/PHARM-P-179-d2-receptor-activity-curves.png
Drugs with low efficacy bind to receptors but do not fully activate them. Such "partial 
agonists" can act as either as a weak agonist (in the absence of a full agonist), or as a 
competitive antagonist (if a full agonist is present). Which curve best reflects the effect 
produced by this type of agonist when it is administered alone?
a) A
b) B
c) C
d) D
e) E

### PHARM-P-180
tier: official
form: mcq
type: single
answer: a
img: flagged/PHARM-P-180-isoproterenol-drugx-graph.jpg
This graph illustrates the dose-response relationship for the effect of the beta agonist 
isoproterenol on an isolated perfused heart, both alone and in the presence of different 
fixed concentrations of Drug X. Based upon the data shown, Drug X is most likely a(n):
a) beta agonist
b) competitive antagonist
c) irreversible antagonist
d) noncompetitive antagonist

### PHARM-P-181
tier: official
form: mcq
type: single
answer: b
img: flagged/PHARM-P-181-norepinephrine-drugx-graph.jpg
This graph shows the concentration-dependent effects of norepinephrine on arterial 
blood pressure, both alone, and in the presence of a fixed concentration of Drug X. 
Which type of antagonist is Drug X?
a) Silent
b) Non – competitive
c) Competitive
d) Chemical

### PHARM-P-182
tier: official
form: mcq
type: single
answer: d
Angina is caused by:
a) Blocking beta1 receptors with a constant binding of noradrenaline
b) Activating beta2 receptors
c) Beta1 receptors are not active anymore
d) Extreme binding of noradrenaline due to up regulation

### PHARM-P-183
tier: official
form: mcq
type: single
answer: a
What is correct concerning TI:
a) A safer drug has a higher theraputic index
b) TI might be equal to 1
c) The more the unwanted adverse effect, the ration decreases
d) You are in danger if you take 1.8 ng/ml of Digoxin which has the margin of safety 
(0.8-2)

### PHARM-P-184
tier: official
form: mcq
type: single
answer: d
What is the correct statement concerning noncompetitive antagonism:
a) The potency of the drug does not change
b) the number of receptors able to bind the agonist is affected
c) by increasing the conc. of the agonist, we cannot overcome the problem
d) non of the above is wrong

### PHARM-P-185
tier: official
form: mcq
type: single
answer: e
A patient comes to the ER having his quadriceps muscle constantly contracted, you 
should give him:
a) Norepinephrine to stimulate the sympathetic nervous system
b) An antagonist for Norepinephrine
c) Acetylcholinesterase
d) Agonist for acetylcholine
e) b and d are correct

### PHARM-P-186
tier: official
form: qa
answer: Drug C
img: flagged/PHARM-P-186-four-drug-dose-response-graph.jpg
Dose response data was collected during the preclinical testing of four drugs for the 
treatment of acute heart failure. Which drug studied was the most efficacious? (See the dose-response graph of four drugs, A-D, tested for acute heart failure.)

### PHARM-P-187
tier: official
form: qa
answer: Drug A
img: flagged/PHARM-P-186-four-drug-dose-response-graph.jpg
Dose response data was collected during the preclinical testing of four drugs for the 
treatment of acute heart failure. Of the four drugs shown, which is the most 
potent? (Same graph as PHARM-P-186.)

### PHARM-P-188
tier: official
form: mcq
type: single
answer: b
As a clinical consultant for the Breathright drug research firm, you are given the task of 
using an in vitro assay to screen ten thousand drug analogs to find the most potent 
beta-2 receptor agonist. When analysing your data, the biomarker that you should 
screen for is:
a) E max
b) Emax
c) EC50
d) Half life
e) Toxicity

### PHARM-P-189
tier: official
form: mcq
type: single
answer: c
Mutations in receptor tyrosine kinases would most likely be associated with :
a) Neurologic diseases
b) Endocrine diseases
c) Cancers
d) Metabolic abnormalities

### PHARM-P-190
tier: official
form: mcq
type: single
answer: b
A newly developed medication for pulmonary hypertension targets blood vessels in the 
lungs, but does not affect blood vessels in the liver. Which of the following is most likely 
true of this medication?
a) It is a ligand that is specific for lung and liver blood-vessel receptors. but which is 
metabolized rapidly in the liver
b) It is a ligand that is specific for blood-vessel receptors in the lung but not in the liver
c) It is a receptor that is upregulated when oxygen tension in the lungs is low
d) It is a receptor that is only expressed on blood vessels in the lungs

### PHARM-P-191
tier: official
form: mcq
type: single
answer: c
In which type of cell are ligand-gated ion channels most commonly found?
a) Cells that are terminally differentiated
b) Cells that produce large proteins
c) Cells that need to respond quickly to external stimuli
d) Cells that respond to mechanic forces

### PHARM-P-192
tier: official
form: mcq
type: single
answer: d
Which of the following is NOT true regarding ligand-gated ion channels?
a) React quickly to a stimulus or ligand
b) Can have intracellular binding sites
c) Can exhibit allosteric binding
d) Open or close in response to deformations in the cell membrane

### PHARM-P-193
tier: official
form: mcq
type: single
answer: d
Once phosphorylated, the intracellular segment of a receptor tyrosine kinase
a) Activates adenylate cyclase
b) Causes dissociation of the ligand from an allosteric binding site
c) Terminates intracellular signaling cascades
d) Allows docking of intracellular proteins involved in signal transduction

### PHARM-P-194
tier: official
form: mcq
type: single
answer: a
Isoproterenol produces maximal contraction of cardiac muscle in a manner similar to 
epinephrine . Which of the following best describe isoproterenol ?
a) Fuller agonist
b) Partial agonist
c) Irreversible antagonist
d) Inverse agonist

### PHARM-P-195
tier: official
form: mcq
type: single
answer: b
If 10 mg of naproxen produces the same analgesic response as 100 mg of ibuprofen , 
which of the following statements is correct ?
a) Naproxen is more efficacious than is ibuprofen
b) Naproxen is more potent than ibuprofen
c) Naproxen is full agonist , and ibuprofen is a partial agonist .
d) Naproxen is a competitive antagonist .
e) Naproxen is a better drug to take for pain relief than is ibuprofen .

### PHARM-P-196
tier: official
form: mcq
type: single
answer: e
If a 10 mg morphine produces a greater analgesic response than can achieved by 
ibuprofen at any dose , which of the following statements is correct ?
a) Morphine is less efficacious than is ibuprofen .
b) Morphine is less potent than is ibuprofen .
c) Morphine is a full agonist , and ibuprofen is a partial agonist .
d) Ibuprofen is ab competitive antagonist .
e) Morphine is a better drug to take for pain relief than is ibuprofen .

### PHARM-P-197
tier: official
form: mcq
type: single
answer: a
In the presence of naloxone , a higher concentration of morphine is required to elicit full 
pain relief . Naloxone by it self has no effect . Which of the following is correct regarding 
these medications ?
a) Naloxone is a competitive antagonist .
b) Morphine is a full agonist , and naloxone is a partial agonist .
c) Morphine is less efficacious than is naloxone .
d) Morphine is less potent than is naloxone .
e) Naloxone is a noncompetitive antagonist .

### PHARM-P-198
tier: official
form: mcq
type: single
answer: b
In the presence of pentazocine , a higher concentration of morphine is required to elicit 
pain relief . Pentazocine by it self has a smaller analgesic effect than does morphine , 
even at the highest dose , Which of the following is correct regarding these medications 
?
a) Pentazocine is a competitive antagonist .
b) Morphine is a full agonist , and pentazocine is a partial agonist .
c) Morphine is less efficacious than is pentazocine .
d) Morphine is less potent than is pentazocine .
e) Pentazocine is a noncompetitive antagonist .

### PHARM-P-199
tier: official
form: mcq
type: single
answer: e
In the presence of picrotoxin , diazepam is less efficacious at causing sedation , 
regardless of the dose . Picrotoxin by it self has no sedative effect even at the highest 
dose . Which of the following is correct ?
a) Picrotoxin is a competitive antagonist .
b) Diazepam is a full agonist , and picrotoxin is a partial agonist.
c) Diazepam is less efficacious than is picrotoxin.
d) Diazepam is less potent than is picrotoxin .
e) Picrotoxin is a noncompetitive antagonist .

### PHARM-P-200
tier: official
form: mcq
type: single
answer: e
Which of the following would up regulate postsynaptic beta 1 adrenergic receptors? 
Daily use of amphetamine that causes norepinephrine to be released .
a) A disease that causes an increase in the activity of norepinephrine neurons .
b) Daily use of isoproterenol , a beta 1 receptor agonist .
c) Daily use of formoterol , a beta 2 receptor agonist.
d) E-Daily use of propranolol , a beta 1 receptor antagonist .

### PHARM-P-201
tier: official
form: mcq
type: single
answer: b
Which one of the following is a fundamental difference between competitive and 
noncompetitive antagonist ?
a) Competitive and non competitive work on different receptors .
b) Competitive antagonist reduces agonist potency (increase EC50)  and non 
competitive antagonist reduces agonist efficacy (decrease E max ) .
c) There is no difference between them , they are exactly the same .
d) Non competitive antagonist causes an upward shift of the E max while competitive 
antagonist does the opposite .

### PHARM-P-202
tier: official
form: mcq
type: single
answer: c
Which of the following regarding E max is correct ?
a) E max assumes that as long as you increase the concentration of the drug , there will 
be a higher effect of the drug .
b) E max is used to compare the potency of different drugs .
c) E max assumes that all receptors are occupied by the drug and no increase in 
response is observed if a higher concentration of drug is obtained .
d) All of the previous points are incorrect .

### PHARM-P-203
tier: official
form: mcq
type: single
answer: a
Candesartan and irbesartan are angiotensin receptor blockers that are used to treat 
hypertension . The therapeutic dose range for candesartan is 4 to 32 mg , as compared 
to 75 to 300 mg for irbesartan . which of the following regarding this statement is 
correct ?
a) Candesartan is more potent than is irbesartan .
b) Candesartan and irbesartan have different efficacy .
c) Candesartan is a non competitive antagonist for irbesartan .
d) Irbesartan is a competitive antagonist for candesartan .

### PHARM-P-204
tier: official
form: mcq
type: single
answer: b
A characteristic that distinguishes true receptors from other drug binding sites 
present in blood and other biological tissues is the characteristic of:  

 (A)binding affinity.
b) reversible binding
c) signal transduction 
D) stereoselective interaction.

### PHARM-P-205
tier: official
form: mcq
type: single
answer: c
A drug which does not produce any action by itself but decreases the slope of the 
log dose-response curve and suppresses the maximal response to another drug is a…  
 
(a) Physiological antagonist  
(b) Competitive antagonist.  
(c) Noncompetitive antagonist.  
(d) Partial agonist.

### PHARM-P-206
tier: official
form: mcq
type: single
answer: b
'Drug efficacy' refers to..  
(a) The range of diseases in which the drug is beneficial..  
(b) The maximal intensity of response that can be produced by the drug..  
(c) The therapeutic dose range of the drug..  
(d) The therapeutic index of the drug.

### PHARM-P-207
tier: official
form: mcq
type: single
answer: c
Competitive antagonists.  
(a) Dissociate from receptors faster than their respective agonists  
(b) Alter the shape of the log dose response curve of an agonist  
(c) According to the rate theory have low dissociation rate constants 
 (d) Initiate the opposite cellular response to receptor occupancy to that obtained by 
the agonist 
 (e) All the above .

### PHARM-P-208
tier: official
form: mcq
type: single
answer: d
A non-competitive antagonist : 
 
(a) Alters the mechanism of action of an agonist 
 (b) Alters the potency of an agonist  
(c) Shifts the dose-response curve of an agonist to the right  
(d) Decreases the maximum response to an agonist  
(e) None of the above.

### PHARM-P-209
tier: official
form: mcq
type: single
answer: d
The types of antagonism are:  

 
a) Summarized.  
 b) Potentiated.  
c) Additive.  
d) Competitive.

### PHARM-P-210
tier: official
form: mcq
type: single
answer: a
The term "chemical antagonism" means that:  
a) two drugs combine with one another to form an inactive compound.  
b) two drugs combine with one another to form a more active compound.  
c) two drugs combine with one another to form a more water soluble compound.  
d) two drugs combine with one another to form a more fat soluble compound.

### PHARM-P-211
tier: official
form: mcq
type: single
answer: b
An agonist is substance that: 
 a) Interacts with the receptor without producing any effect  
b) Interacts with the receptor and initiates changes in cell function, producing various 
effects 
 c) Increases concentration of another substance to produce effect  
d) Interacts with plasma proteins and doesn't produce any effect

### PHARM-P-212
tier: official
form: mcq
type: single
answer: d
If an agonist can produce maximal effects and has high efficacy it's called:  
a) Partial agonist  
b) Antagonist 
 c) Agonist-antagonist  
d) Full agonist

### PHARM-P-213
tier: official
form: mcq
type: single
answer: a
If an agonist can produce submaximal effects and has moderate efficacy it's called: 
a) Partial agonist 
 b) Antagonist 
 c) Agonist-antagonist 
 d) Full agonist

### PHARM-P-214
tier: official
form: mcq
type: single
answer: d
antagonist is a substance that:  
a) Binds to the receptors and initiates changes in cell function, producing maximal 
effect 
 b) Binds to the receptors and initiates changes in cell function, producing submaximal 
effect  

c) Interacts with plasma proteins and doesn't produce any effect  
d) Binds to the receptors without directly altering their functions

### PHARM-P-215
tier: official
form: mcq
type: single
answer: b
A competitive antagonist is a substance that: 
 a) Interacts receptors and produces submaximal effect 
B)  Binds to the same receptor site and progressively inhibits the agonist response  
c) Binds to the nonspecific sites of tissue  
d) Binds to one receptor subtype as an agonist and to another as an antagonist

### PHARM-P-216
tier: official
form: mcq
type: single
answer: c
Irreversible interaction of an antagonist with a receptor is due to: 
 a) lonic bonds  
b) Hydrogen bonds  
c) Covalent bonds 
 d) All of the above

### PHARM-P-217
tier: official
form: mcq
type: single
answer: b
Mechanisms of transmembrane signaling are the following EXCEPT: 
 a) Transmembrane receptors that bind and stimulate a protein tyrosine kinase  
b) Gene replacement by the introduction of a therapeutic gene to correct a genetic 
effect 
 c) Ligand-gated ion channels that can be induced to open or close by binding a ligand.  
d) Transmembrane receptor protein that stimulates a GTP-binding signal transducer 
protein (G-protein) which in turn generates an intracellular second messenger .

### PHARM-P-218
tier: official
form: mcq
type: single
answer: d
Tick the second messenger of G-protein-coupled (metabotropic) receptor:  
a) Adenylyl cyclase  
b) Sodium ions 
 c) Phospholipase C. 
 d) CAMP .

### PHARM-P-219
tier: official
form: mcq
type: single
answer: c
Tick the substance which changes the activity of an effector element but doesn't 
belong to second messengers:  
a) CAMP 
 b) CGMP  
c) G-protein 

 d) Calcium ions

### PHARM-P-220
tier: official
form: mcq
type: single
answer: d
note: Source's own Q45 stem is literally prefixed "18." before the question text
  (a leftover artifact, not a typo in the question itself) — preserved as written.
18. All of the following statements about efficacy and potency are true EXCEPT:  
a) Efficacy is usually a more important clinical consideration than potency 
 b) Efficacy is the maximum effect of a drug 
 c) Potency is a comparative measure, refers to the different doses of two drugs that 
are needed to produce the same effect  
d) The ED50 is a measure of drug's efficacy

### PHARM-P-221
tier: official
form: mcq
type: single
answer: a
In the following, what describes absorption?
a) The tightness that drug bind to receptor
b) Irreversible transport from site of administration to the bloodstream
c) Drug leaving the blood to peripheral tissue
d) Proportional to drug concentration in plasma (First order kinetics implied)

### PHARM-P-222
tier: official
form: mcq
type: single
answer: c
In the following, what describes distribution?
a) The tightness that drug bind to receptor
b) Irreversible transport from site of administration to the bloodstream
c) Drug leaving the blood to peripheral tissue
d) Proportional to drug concentration in plasma (First order kinetics implied)

### PHARM-P-223
tier: official
form: mcq
type: single
answer: a
In the following, what describes affinity?
a) The tightness that drug bind to receptor
b) Irreversible transport from site of administration to the bloodstream
c) Drug leaving the blood to peripheral tissue
d) Proportional to drug concentration in plasma (First order kinetics implied)

### PHARM-P-224
tier: official
form: mcq
type: single
answer: d
Which one of the following is true for a drug whose elimination from plasma shows first order kinetics?
a) Half-life is proportional to the drug concentration in plasma
b) The amount eliminated per unit of time is constant
c) A plot of drug concentration versus time is a straight line
d) The rate of elimination is proportional to the plasma concentration

### PHARM-P-225
tier: official
form: mcq
type: single
answer: b
The addition of glucuronic acid to a drug?
a) Lowers its water solubility
b) Usually leads to inactivation of drug
c) Is an example of phase I reactions
d) Involves cytochrome P450

### PHARM-P-226
tier: official
form: mcq
type: single
answer: b
A patient is treated with drug A, which has high affinity for albumin and is administered in amount that don't 
exceed the binding capacity of albumin, A second drug B also has high affinity for albumin but is administered in 
amounts that are 100 times the binding capacity of albumin. what happens after administering drug B?
a) Increase tissue concentration of drug A
b) Increase serum concentration of unbound drug A
c) Decrease tissue concentration of drug A
d) Decrease half-life of drug A

### PHARM-P-227
tier: official
form: mcq
type: single
answer: c
Drugs showing zero-order kinetics of elimination?
a) Are more common than those showing first order kinetics
b) Decrease in concentration exponentially with time
c) Amount of drug eliminated is independent of dose
d) Show constant fraction of the drug eliminated per unit time 
 
 
 
 

### PHARM-P-228
tier: official
form: mcq
type: single
answer: b
A drug with half-life of 12 hours is administered Intravenously. how long will it take for the drug to reach 90% of 
its final steady state?
a) 90 hours
b) 40 hours
c) 30 hours
d) 24 hours

### PHARM-P-229
tier: official
form: mcq
type: single
answer: d
The route of drug administration is determined by?
a) Water solubility of the drug
b) Ionization of the drug
c) Desirability of rapid onset of action of the drug
d) All of the above

### PHARM-P-230
tier: official
form: mcq
type: single
answer: d
All of the following about passive absorption is true EXCEPT?
a) The driving force is concentration gradient
b) Doesn't involve a carrier
c) The process shows a low structural specificity
d) The process is saturable

### PHARM-P-231
tier: official
form: mcq
type: single
answer: d
The following factor(s) influencing drug absorption?
a) Blood flow to the absorption area
b) Total surface area available
c) Contact time at the absorption surface
d) All of the above

### PHARM-P-232
tier: official
form: mcq
type: single
answer: d
Factor(s) that influence bioavailability of drugs?
a) First-pass hepatic metabolism
b) Solubility of the drug
c) Chemical instability in GIT
d) All of the above

### PHARM-P-233
tier: official
form: mcq
type: single
answer: d
The following factor(s) determine drug distribution?
a) Blood flow
b) Capillary permeability
c) Binding of drug to plasma proteins
d) All of the above

### PHARM-P-234
tier: official
form: mcq
type: single
answer: b
All of the following is true about drug metabolism EXCEPT?
a) pro-drug must be metabolized to their active forms
b) First-order kinetics metabolism means constant amount of drug is metabolized per unit time
c) In zero-order kinetics metabolism. the enzyme is saturable
d) None of the above

### PHARM-P-235
tier: official
form: mcq
type: single
answer: a
All of the following is true about drug metabolism EXCEPT?
a) Water soluble drugs must first be metabolized in the liver
b) Phase I reaction function to convert lipophilic molecules into lipophobic
c) Phase II reaction include conjugation with endogenous substances 
 

### PHARM-P-236
tier: official
form: mcq
type: single
answer: b
Pharmacokinetics is?
a) The study of biological and therapeutic effect of drugs
b) The study of absorption, distribution, metabolism and excretion of drugs
c) The study of mechanisms of drug action
d) The study of methods of new drug development

### PHARM-P-237
tier: official
form: mcq
type: single
answer: d
What kind of substances can't penetrate membranes by passive diffusion?
a) Lipid soluble
b) Non-ionized
c) Hydrophobic
d) Hydrophilic

### PHARM-P-238
tier: official
form: mcq
type: single
answer: d
What's implied by (active transport)?
a) Transport of drugs through a membrane by means of diffusion
b) Transport without energy consumption
c) Engulf of drug by a cell membrane with a new vesicle formation
d) Transport against concentration gradient

### PHARM-P-239
tier: official
form: mcq
type: single
answer: c
Pick out the appropriate alimentary route of administration when passage of drug through liver is minimized?
a) Oral
b) Transdermal
c) Rectal
d) Intraduodenal

### PHARM-P-240
tier: official
form: mcq
type: single
answer: b
Which route of drug administration is most likely to lead to the first pass effect?
a) Sublingual
b) Oral
c) Intravenous
d) Intramuscular

### PHARM-P-241
tier: official
form: mcq
type: single
answer: a
What is characteristic of the sublingual route?
a) fast absorption
b) Drug exposed to gastric secretion
c) Drug exposed to more prominent liver metabolism
d) Drug can be administrated in a variety of doses

### PHARM-P-242
tier: official
form: mcq
type: single
answer: c
Parenteral administration?
a) Cannot be used with unconsciousness patients
b) Generally, results in a less accurate dosages than oral administration
c) Usually produces a more rapid response than oral administration
d) Is too slow for emergency use

### PHARM-P-243
tier: official
form: mcq
type: single
answer: c
Correct statements listing characteristics of a particular route of drug administration include all of the following 
EXCEPT?
a) Intravenous administration provides a rapid response
b) Intramuscular administration requires a sterile technique
c) Inhalation provides slow access to the general circulation
d) Subcutaneous administration may cause local irritation 

### PHARM-P-244
tier: open
form: mcq
Pick out the right statement?
a) Microsomal oxidation always results in inactivation of a compound
b) Microsomal oxidation results in a decrease of compound toxicity
c) Microsomal oxidation results in an increase of ionization and water solubility of a drug
d) Microsomal oxidation results in increase of lipid solubility of a drug thus its excretion from the organism is 
facilitated

### PHARM-P-245
tier: official
form: mcq
type: single
answer: b
Metabolic transformation (Phase I) is?
a) Acetylation and methylation of substances
b) Transformation of substances due to oxidation, reduction or hydrolysis
c) Glucuronide formation
d) Binding to plasma protein

### PHARM-P-246
tier: official
form: mcq
type: single
answer: c
Which of the following is not a conjugation of a drug?
a) Glucuronidation
b) Sulfate formation
c) Hydrolysis
d) Methylation

### PHARM-P-247
tier: official
form: mcq
type: single
answer: b
Metabolic (Phase I and Phase II) reactions usually result in increase of substance biological activity?
a) True
b) False

### PHARM-P-248
tier: official
form: mcq
type: single
answer: b
Half-life of drug doesn't depend on?
a) Biotransformation
b) Time of drug absorption
c) Concentration of a drug in plasma
d) Rate of drug elimination

### PHARM-P-249
tier: official
form: mcq
type: single
answer: c
All of the following statements related to the binding of drugs by plasma proteins are correct EXCEPT?
a) Bound drug is unable to diffuse into tissue until it becomes unbound
b) Displacement of the bound drug by another drug can increase the effects of a given dosage of the first drug
c) Bound drug is the pharmacologically active part of the drug
d) None of the above

### PHARM-P-250
tier: official
form: mcq
type: single
answer: b
Binding of a drug to plasma proteins will tend to?
a) Decrease half-life
b) Decrease rate of glomerular filtration
c) Increase its rate of biotransformation
d) Increase its concentration in plasma

### PHARM-P-251
tier: official
form: mcq
type: single
answer: b
Pharmacodynamics involves?
a) Info about main mechanisms of drug absorption
b) Info about unwanted effects
c) Info about biological barriers
d) Info about excretion of a drug from the organism 
 
 

### PHARM-P-252
tier: official
form: mcq
type: single
answer: d
Proteins which a drug molecule bind are?
a) Receptors
b) Ion channels
c) Carriers
d) All of the above

### PHARM-P-253
tier: official
form: mcq
type: single
answer: d
If an agonist can produce maximal effect and has high efficacy it's called?
a) Partial agonist
b) Antagonist
c) Agonist-Antagonist
d) Full Agonist

### PHARM-P-254
tier: official
form: mcq
type: single
answer: c
Irreversible interaction of an antagonist with a receptor is due to?
a) Ionic bonds
b) Hydrogen bonds
c) Covalent bonds
d) All of the above

### PHARM-P-255
tier: official
form: mcq
type: single
answer: b
In the previous question, the antagonist represents?
a) Competitive antagonism
b) Noncompetitive antagonism

### PHARM-P-256
tier: official
form: mcq
type: single
answer: d
Tick the substances whose mechanisms are based on interaction with ion channels?
a) Sodium channel blockers
b) Calcium channel blockers
c) Potassium channel activators
d) All of the above

### PHARM-P-257
tier: official
form: mcq
type: single
answer: c
What term is used to describe a more gradual decrease in responsiveness to a drug, taking weeks or months or 
years to develop?
a) Refractoriness
b) Cumulative effect
c) Tolerance
d) Tachyphylaxis

### PHARM-P-258
tier: official
form: mcq
type: single
answer: c
If two drugs with the same effect, taken together, produce an effect equal in magnitude to the sum of their 
effects given individually. It's called?
a) Antagonism
b) Synergism
c) additive drug effect
d) None of the above

### PHARM-P-259
tier: official
form: mcq
type: single
answer: a
Chemical antagonism means?
a) Two drugs combine with one another to form an inactive compound
b) Two drugs combine with one another to form a more active compound
c) Two drugs acting competitively on the same receptor
d) Two drugs acting on different receptors with opposite effects at the same time  
 

### PHARM-P-260
tier: official
form: mcq
type: single
answer: a
If 87.5% of a drug is eliminated via first order kinetics in 15 hours. Half-life of this drug is expected to be?
a) 5 hours
b) 10 hours
c) 15 hours
d) 30 hours

### PHARM-P-261
tier: official
form: mcq
type: single
answer: d
A pharmacological response might be reduced by all of the following EXCEPT?
a) Low solubility of drug
b) Abnormal target receptors
c) Lack of absorption at site of administration
d) Interference with drug elimination

### PHARM-P-262
tier: official
form: mcq
type: single
answer: b
The oral route of drug administration tends to be associated with all of the following EXCEPT?
a) Relative safety
b) Rapid response
c) Convenience
d) Incomplete absorption

### PHARM-P-263
tier: official
form: mcq
type: single
answer: a
Therapeutic index of a drug reflects its?
a) Relative safety
b) Duration of action
c) Onset effects
d) Potency

### PHARM-P-264
tier: official
form: mcq
type: single
answer: c
Which of the following is CORRECT?
a) Value of t (1/2) depends on rate of absorption
b) Increase in Kd of drug with plasma protein is associated with increase in T (1/2)
c) T (1/2) value is required for dose estimation
d) Drugs associated with short T (1/2) are characterized by low systemic clearance.

### PHARM-P-265
tier: official
form: mcq
type: single
answer: d
Which of the following statements about drug receptor interactions is TRUE?
a) An agonist interacts with its target receptors and produces a biological effect
b) A reversible antagonist shifts the dose response curve to the right without affecting the maximal response
c) Partial agonist are drugs that have affinity for receptors with moderate efficacy
d) All of the above

### PHARM-P-266
tier: official
form: mcq
type: single
answer: d
Variation in pharmacological responses to drugs among individuals can be attributed to?
a) Drug-Drug interactions
b) Sex
c) Age
d) All of the above

### PHARM-P-267
tier: official
form: mcq
type: single
answer: c
Which of the following statements is CORRECT?
a) If 10 mg of drug A produces the same response as 100 mg of drug B, then drug A is more efficacious than 
drug B
b) Skipping a dose is not important in calculating the time to reach steady state
c) Generally, Reduction in the oxidative metabolism through cytochrome P450 system result in a reduction in 
the drugs clearance 

### PHARM-P-268
tier: official
form: mcq
type: single
answer: b
When two drugs with the same effect give together and produce an effect that is greater in magnitude than the 
sum of their effects when the drugs are given individually, we call this?
a) Competitive drug effect
b) Synergic drug effect
c) Additive drug effect
d) Potentiation drug effect

### PHARM-P-269
tier: official
form: mcq
type: single
answer: c
Hydrophilic drug with a law molecular weight is most likely to distribute to which of the following 
compartments?
a) Extracellular
b) Plasma
c) Total body water
d) A + B

### PHARM-P-270
tier: official
form: mcq
type: single
answer: a
Which of the following statements is CORRECT?
a) In competitive antagonism a higher concentration of agonist is necessary to achieve the therapeutic effect 
of the agonist
b) With competitive antagonism, the dose effect curve is shifted to the left
c) Competitive antagonism is produced by antagonists that have the ability to activate receptors
d) Emax does not depend on the number of drug-receptor complexes formed

<!-- batch 03 — raw/practice/Pharmacology PYQ and Bank Questions.pdf, pages 67-115
  of 134, the "Pharma020" section credited (p115) to Mohanad Al-ahmad. RUN-PLAN
  row 11. Two separately-numbered lists back to back, both restarting at 1 -- the
  source's own structure, not a Job A error:

    p68-75   "Intro & Pharmacodynamics," numbered 1)-28), each followed inline by
             an "ans :"/"Ans:" line -> tier claimed. Five real gaps: #23-27 carry
             no answer line at all in the source (open tier for those five only).
             PHARM-P-271 through PHARM-P-298.
    p76-115  "Pharmacokinetics," numbered Q1)-Q110), each followed inline by an
             "Answer: X" line -> tier claimed throughout (a student-authored
             compiled set with answers, same treatment as the Rama/Sana batch in
             batch 01 -- not an instructor key, so not official). Two source
             oddities, both preserved rather than cleaned up:
               Q1  is a "match the following" question (four processes a-d
                   matched against four numbered definitions) with key
                   "1D, 2A, 3B, 4C" -- rendered as one `qa` entry (PHARM-P-299)
                   with the matching spelled out, not forced into invented mcq
                   options.
               Q11 (PHARM-P-309) has a malformed option (e): the source runs
                   "e) Answer: A" together with no text of its own between the
                   bullet and the answer line. Option (e) is transcribed blank
                   rather than inventing filler text.
             A "RANDOM" subheading appears before Q92 but numbering does not
             restart there -- treated as a section label, not a new list.
             PHARM-P-299 through PHARM-P-408.

  Four embedded graphs (Q105, Q107, Q108, Q110, all in the Pharmacokinetics list)
  are load-bearing clinical-vignette questions built around a figure and saved to
  flagged/: PHARM-P-403 (glucuronidation-rate saturation curve), PHARM-P-405
  (peak/trough plasma levels, two dosing intervals), PHARM-P-406 (neonate vs.
  adult plasma concentration), PHARM-P-408 (two oral NSAID formulations' plasma
  curves). Every page 67-115 was checked for embedded images; a run of ~20
  13x13px images on p74-75 are decorative bullet-point icons, not saved. -->

### PHARM-P-271
tier: claimed
form: mcq
type: single
claimed: a
The data presented in the figure below show that:
a) Drugs A and B have equal efficacy
b) Drug B and C have equal efficacy
c) Drug B is a partial agonist
d) Drugs A and C have the same affinity and efficacy
e) Drugs A and B have equal potency

### PHARM-P-272
tier: claimed
form: mcq
type: single
claimed: d
Concerning competitive antagonism, which of the following sentence is  
correct?
a) Competitive antagonism is produced by antagonists that have the ability to activate receptors
b) With competitive antagonism, maximal drug effect cannot be obtained, even at high agonist 
concentrations
c) Competitive antagonism is based on reversible drug/antagonist binding at receptor sites
d) With competitive antagonism, the dose-effects curve is shifted to the left.
e) All of the above.

### PHARM-P-273
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is NOT an example of drug misuse
a) Not following the instructions when taking a prescription medication
b) Taking a friend's prescription medication to treat headache
c) Taking an over-the-counter medication more often than is recommended
d) Regular use of increasing amounts of cocaine to get high
e) None of the above

### PHARM-P-274
tier: claimed
form: mcq
type: single
claimed: b
The development of tolerance to a drug is accompanied by an increase in which of the following 
parameters of that drug?
a) Maximal efficacy
b) Therapeutic index
c) Effective dose
d) Potency
e) All of the above

### PHARM-P-275
tier: claimed
form: mcq
type: single
claimed: d
Which of the following statements is correct?
a) Always you should write the drug chemical name in your prescription
b) For a drug with high plasma protein binding capacity, lower plasma protein level  
in children means that the free drug will be less
c) Metabolism is always more or in adults than children
d) Stopping a drug can be a cause of an adverse effect.
e) The risk benefit: ration for any drug is constant for the human life stages.

### PHARM-P-276
tier: claimed
form: mcq
type: single
claimed: c
If the effect of combination of two drugs is equal to the sum of their individual effects, the two 
drugs are exhibiting? .
a) Antagonism
b) Potentiation
c) Synergism
d) Additive

### PHARM-P-277
tier: claimed
form: mcq
type: single
claimed: e
Which term describes the use of a drug for a purpose which it was not intended?
a) Misuse
b) habitual
c) Addiction
d) Tolerance
e) Abuse

### PHARM-P-278
tier: claimed
form: mcq
type: single
claimed: c
High plasma protein binding
a) Increases the volume of distribution of the drug
b) Facilitates glomerular filtration of the drug
c) Generally makes the drug long acting
d) Minimizes drug interactions
e) Makes the drugs more potent

### PHARM-P-279
tier: claimed
form: mcq
type: single
claimed: a
Which of the following statements is correct?
a) Receptor in our bodies are in a dynamic state
b) In a patient, a response to a low dose to a drug is likely followed by an  
indefinitely increasing response as the dose is increased
c) Always you should write the drug trade name in your prescription
d) Regardless the tissue site of the receptor, activation of a receptor in the body  
always produces the same effect.
e) None of the above

### PHARM-P-280
tier: claimed
form: mcq
type: single
claimed: c
The therapeutic index of a drug is a measure of its
a) Dose variability
b) Additive
c) Safety
d) Potency
e) Efficacy

### PHARM-P-281
tier: claimed
form: mcq
type: single
claimed: b
Which of the following statements is correct?
a) hypersensitivity reactions is classified as augmented (dose dependent) drug  
reaction.
b) Variation in response to a drug among different individuals is most likely to  
occur with a drug showing narrow therapeutic index.
c) If the TD50 is much higher than the ED50 then the drug is described as a narrow  
therapeutic drug
d) Potency is indicated by the height of the log dose response
e) It is safe to consume as much as you want from the OTC drugs.

### PHARM-P-282
tier: claimed
form: mcq
type: single
claimed: d
Amer was poisoned with a drug that antagonize receptor A irreversibly, which of the following is 
an appropriate pharmacological intervention?
a) To give drug that increase the metabolism of Drug A
b) To give receptor A non-competitive antagonist
c) To give receptor A non-competitive agonist
d) To give another drug that is an agonist to a different receptor, such receptor has the same 
physiological function as receptor A
e) To give another drug that is an agonist to a different receptor, such receptor has opposite 
physiological function to receptor A

### PHARM-P-283
tier: claimed
form: mcq
type: single
claimed: a
Isoproterenol produces maximal contraction of cardiac muscle in a manner similar to 
epinephrineWhich of the following best describes isoproterenol?
a) Full agonist.
b) Partial agonist.
c) Competitive antagonist.
d) Irreversible antagonist.
e) Inverse agonist.

### PHARM-P-284
tier: claimed
form: mcq
type: single
claimed: b
2 If 10 mg of naproxen produces the same analgesic response as 100 mg of ibuprofen, which of the 
following statements is correct?
a) Naproxen is more efficacious than is ibuprofen.
b) Naproxen is more potent than ibuprofen.
c) Naproxen is a full agonist, and ibuprofen is a partial  
agonist.
d) Naproxen is a competitive antagonist.
e) Naproxen is a better drug to take for pain relief than  
is ibuprofen.

### PHARM-P-285
tier: claimed
form: mcq
type: single
claimed: e
If 10 mg of morphine produces a greater analgesic response than can be achieved by ibuprofen at 
any dose, which of the following statements is correct?
a) Morphine is less efficacious than is ibuprofen.
b) Morphine is less potent than is ibuprofen.
c) Morphine is a full agonist, and ibuprofen is a partial  
agonist.
d) Ibuprofen is a competitive antagonist.
e) Morphine is a better drug to take for pain relief than  
is ibuprofen

### PHARM-P-286
tier: claimed
form: mcq
type: single
claimed: a
In the presence of naloxone, a higher concentration of morphine is required to elicit full pain 
relief. Naloxone by itself has no effect. Which of the following is correct regarding these medications?
a) Naloxone is a competitive antagonist.
b) Morphine is a full agonist, and naloxone is a partial  
agonist.
c) Morphine is less efficacious than is naloxone.
d) Morphine is less potent than is naloxone.
e) Naloxone is a noncompetitive antagonist

### PHARM-P-287
tier: claimed
form: mcq
type: single
claimed: b
In the presence of pentazocine, a higher concentration of morphine is required to elicit full pain 
relief. Pentazocine by itself has a smaller analgesic effect than does morphine, even at the highest 
dose. Which of the following is correct regarding these medications?
a) Pentazocine is a competitive antagonist.
b) Morphine is a full agonist, and pentazocine is a  
partial agonist.
c) Morphine is less efficacious than is pentazocine.
d) Morphine is less potent than is pentazocine.
e) Pentazocine is a noncompetitive antagonist.

### PHARM-P-288
tier: claimed
form: mcq
type: single
claimed: e
In the presence of picrotoxin, diazepam is less efficacious at causing sedation, regardless of the 
dose. Picrotoxin by itself has no sedative effect even at the highest dose. Which of the following is 
correct?
a) Picrotoxin is a competitive antagonist.
b) Diazepam is a full agonist, and picrotoxin is a partial  
agonist.
c) Diazepam is less efficacious than is picrotoxin.
d) Diazepam is less potent than is picrotoxin.
e) Picrotoxin is a noncompetitive antagonist

### PHARM-P-289
tier: claimed
form: mcq
type: single
claimed: e
Which of the following would up-regulate postsynaptic β1 adrenergic receptors?
a) Daily use of amphetamine that causes norepinephrine to be released.
b) A disease that causes an increase in the activity of norepinephrine neurons.
c) Daily use of isoproterenol, a β1 receptor agonist.
d) Daily use of formoterol, a β2  receptor agonist.
e) Daily use of propranolol, a β1 receptor antagonist.

### PHARM-P-290
tier: claimed
form: mcq
type: single
claimed: c
Which of the following parameters is used to indicate the ability of a drug to produce the desired 
therapeutic effect relative to a toxic effect?
a) Potency
b) Intrinsic activity
c) TI
d) Efficacy
e) Bioavailability

### PHARM-P-291
tier: claimed
form: mcq
type: single
claimed: d
Concerning drug receptor interactions, the constant Kd refers to:
a) maximal physiological effect
b) maximal binding
c) the drug concentration required to occupy 50% of receptors
d) drug concentration that results in half-maximal physiological response
e) all of the above

### PHARM-P-292
tier: claimed
form: mcq
type: single
claimed: b
EC50 mainly reflexs a drug's:
a) maximal effect
b) potency
c) lethality
d) ease of elimination
e) safety

### PHARM-P-293
tier: open
form: mcq
Drug effects are thought to be proportional to the number of occupied receptors
a) true
b) false

### PHARM-P-294
tier: open
form: mcq
True statement(s) concerning competitive inhibition:
a) competitive in addition is based on reversible drug/antagonist binding at receptor sites
b) with competitive inhibition, the dose-effects curve the shifted to the left
c) with competitive inhibition, maximal drug effect cannot be obtained, even at high agonist 
concentrations
d) all the above

### PHARM-P-295
tier: open
form: mcq
An example of a receptor which is a structural protein.
a) Na/K ATPase
b) acetylcholinesterase
c) tubulin
d) DNA
e) phospholipase C

### PHARM-P-296
tier: open
form: mcq
An example of an agent that exerts much of its effects through intracellular receptors that in 
complex form binds to DNA response elements:
a) acetylcholine
b) dopamine
c) corticosteroids
d) diltiazem
e) atropine

### PHARM-P-297
tier: open
form: mcq
Factors that may cause variation in drug responsiveness:
a) changes in the number or function of receptors
b) tachyphylaxis
c) idiosyncratic drug responses
d) hypersensitivity reactions
e) all of the above

### PHARM-P-298
tier: claimed
form: mcq
type: single
claimed: e
Major roles of receptors:
a) determine rate of drug elimination
b) determine drug action selectivity
c) provide a means of blocking drug action as well as mediating drug action
d) act as drug storage sites
e) b+c

### PHARM-P-299
tier: claimed
form: qa
claimed: 1-Excretion, 2-Absorption, 3-Distribution, 4-Biotransformation
note: Source is a matching question (four lettered process names a-d matched
  against four numbered definitions 1-4) with answer key "1D, 2A, 3B, 4C" --
  i.e. definition 1 matches d) Excretion, 2 matches a) Absorption, 3 matches
  b) Distribution, 4 matches c) Biotransformation. Rendered as a qa question
  rather than invented mcq options.
Match the following: a. Absorption / b. Distribution / c. Biotransformation /
d. Excretion -- against: 1. Irreversible transfer of drugs from internal to
external environment / 2. Irreversible transport from site of administration
to the blood circulation / 3. The drug leaving the blood to peripheral tissue /
4. The process of preventing renal reabsorption by drug's alteration

### PHARM-P-300
tier: claimed
form: mcq
type: single
claimed: b
What does “pharmacokinetics” include?
a) Complications of drug therapy
b) Drug biotransformation in the organism
c) Influence of drugs on metabolism processes
d) Influence of drugs on genes

### PHARM-P-301
tier: claimed
form: mcq
type: single
claimed: c
All of the following about passive absorption is true EXCEPT:
a) The driving force is concentration gradient
b) Does not involve a carrier
c) The process is saturable
d) The process shows a low structural specificity
e) The process is suitable for lipid soluble drugs

### PHARM-P-302
tier: claimed
form: mcq
type: single
claimed: b
All of the following are general mechanisms of drug permeation Except
a) Aqueous diffusion
b) Aqueous hydrolysis
c) Lipid diffusion
d) Pinocytosis or endocytosis
e) Special carrier transport

### PHARM-P-303
tier: claimed
form: mcq
type: single
claimed: a
A hydrophilic medicinal agent has the following property:
a) Low ability to penetrate through the cell membrane lipids
b) Penetrate through membranes by means of endocytosis
c) Easy permeation through the blood-brain barrier
d) High reabsorption in renal tubules

### PHARM-P-304
tier: claimed
form: mcq
type: single
claimed: a
Biological barriers include all except:
a) Renal tubules
b) Cell membranes
c) Capillary walls
d) Placenta

### PHARM-P-305
tier: claimed
form: mcq
type: single
claimed: d
The following factor(s) influencing drug absorption:
a) Blood flow to the absorption site
b) Total surface area available for absorption
c) Contact time at the absorption surface
d) All of the above
e) None of the above

### PHARM-P-306
tier: claimed
form: mcq
type: single
claimed: c
First pass effect is:
a) The amount of the drug destroyed by stomach acidity after oral 
administration of drugs for the first time.
b) The amount of the drug passed with stool after oral administration.
c) Amount of drug lost due to hepatic metabolism during drug absorption for 
the first time after oral administration
d) Amount of drug that is eliminated by the liver by hepatic artery.
e) The amount of drug that bypass the Cirrhosed liver after oral 
administration through portosystemic anastomosis.

### PHARM-P-307
tier: claimed
form: mcq
type: single
claimed: c
What does the term “bioavailability” mean?
a) Plasma protein binding degree of substance
b) Permeability through the brain-blood barrier
c) Fraction of an uncharged drug reaching the systemic circulation following 
any route administration
d) Amount of a substance in urine relative to the initial doze

### PHARM-P-308
tier: claimed
form: mcq
type: single
claimed: e
Factor(s) that influence bioavailability of drugs:
a) First-pass hepatic metabolism
b) Solubility of the drug
c) Chemical instability in GIT
d) Nature of the drug formulation re
e) All of the above

### PHARM-P-309
tier: claimed
form: mcq
type: single
claimed: a
note: Source's option (e) has no text of its own -- "e) Answer: A" runs directly
  together in the source, so (e) is transcribed blank rather than invented.
What is the proportion of nonionized form of week base (pka = 9.4)when put
in a media ( pH = 7.4 )
a) 99%
b) 1%
c) 0.1%
d) 50%
e) (blank in source)

### PHARM-P-310
tier: claimed
form: mcq
type: single
claimed: a
Which of the following acids has the highest degree of ionization in an 
aqueous solution?
a) Aspirin pKa = 3.5
b) Indomethacin pKa = 4.5
c) Warfarin pKa = 5.1
d) Ibuprofen pKa = 5.2
e) Phenobarbital pKa = 7.4

### PHARM-P-311
tier: claimed
form: mcq
type: single
claimed: a
The excretion of a weakly acidic drug generally is more rapid in alkaline 
urine than in acidic urine. This process occurs because
a) A weak acid in alkaline media will exist primarily in its ionized form, which 
cannot be reabsorbed easily
b) A weak acid in alkaline media will exist in its lipophilic form, which cannot be 
reabsorbed easily.
c) All drugs are excreted more rapidly in an alkaline urine.

### PHARM-P-312
tier: claimed
form: mcq
type: single
claimed: d
Passive diffusion doesn’t depend on,
a) Permeability
b) Thickness
c) Concentration difference
d) Number of transporters

### PHARM-P-313
tier: claimed
form: mcq
type: single
claimed: d
The following factor(s) determine drug distribution:
a) Blood flow
b) Capillary permeability
c) Drug structure
d) All of the above

### PHARM-P-314
tier: claimed
form: mcq
type: single
claimed: d
The volume of distribution (Vd) relates:
a) Single to a daily dose of an administrated drug
b) An administrated dose to a body weight
c) An uncharged drug reaching the systemic circulation
d) The amount of a drug in the body to the concentration of a drug in plasma

### PHARM-P-315
tier: claimed
form: mcq
type: single
claimed: b
Most of the drugs are distributed homogeneously
a) True
b) False

### PHARM-P-316
tier: claimed
form: mcq
type: single
claimed: b
The volume of distribution for a drug that is completely retained in the 
vascular compartment would be.
a) High
b) Low
c) Unchanged
d) Cannot be determined

### PHARM-P-317
tier: claimed
form: mcq
type: single
claimed: a
A patient is treated with a Drug A, which has a high affinity for Albumin and 
is administered in amount that don’t exceed the binding capacity of Albumin. A 
second drug B also has a high affinity for albumin but is administered in amounts 
that are 100 time the binding capacity of albumin. What happens after 
administration of Drug B?
a) High tissue Conc. for Drug A
b) Low tissue Conc. For Drug A
c) Low vd of Drug A
d) Low half life of Drug A
e) Addition of more Drug A significantly alters the serum conc. of unbound 
Drug B

### PHARM-P-318
tier: claimed
form: mcq
type: single
claimed: b
All of the following factors may increase the volume of distribution EXCEPT:
a) Extremely lipid soluble drugs
b) Blood tissue barriers
c) Drug-drug interactions
d) None of the above

### PHARM-P-319
tier: claimed
form: mcq
type: single
claimed: e
All of the following statements related to the binding of drugs by plasma 
proteins are correct EXCEPT?
a) Bound drug is unable to diffuse into tissue until it becomes unbound.
b) A drug that is bound by plasma proteins will have a smaller apparent volume 
of distribution than if it were not bound.
c) Displacement of the bound drug by another drug can increase the effects of a 
given dosage of the first drug.
d) Acidic drugs are bound mostly to plasma albumin.
e) Bound drug is the pharmacologically active part of the drug

### PHARM-P-320
tier: claimed
form: mcq
type: single
claimed: d
All of the following about free drugs (unbound drags) in plasma are correct 
EXCEPT:
a) Only free drugs can distribute to peripheral tissues
b) Only free drugs can pass through glomerular filtration
c) Only free drugs become available for hepatic metabolism
d) Highly bound drugs (98% bound) have clinically significant drug-drug 
interactions with other drugs through displacement from binding sites on 
plasma protein
e) Basic drugs bind with acidic binding sites on plasma globulins while acidic 
drugs bind with basic binding sites on plasma albumin

### PHARM-P-321
tier: claimed
form: mcq
type: single
claimed: b
A patient with an edema would have an increased volume of distribution if
a) The patient was taking a hydrophobic drug
b) The patient was taking a hydrophilic drug
c) An edema always causes an increase in Vd
d) An edema always causes an decrease in Vd

### PHARM-P-322
tier: claimed
form: mcq
type: single
claimed: c
What would be the expected distribution of Digoxin in the case of odema?
a) Higher than expected
b) Lower Vd than expected
c) None of above

### PHARM-P-323
tier: claimed
form: mcq
type: single
claimed: a
What is the reason of complicated penetration of some drugs through brain-
blood barrier?
a) Incredibly high lipid solubility of a drug
b) Meningitis
c) Absence of pores in the brain capillary endothelium
d) High endocytosis degree in a brain capillary

### PHARM-P-324
tier: claimed
form: mcq
type: single
claimed: e
All of the following conditions tend to increase the patients response to 
drugs EXCEPT:
a) Congestive cardiac failure.
b) Hepatic cirrhosis.
c) Hyperthyroidism.
d) Hypothyroidism
e) Hyperalbuminemia

### PHARM-P-325
tier: claimed
form: mcq
type: single
claimed: a
The P-glycoprotein is a multidrug transmembrane transporter protein that 
transports medications across cell membranes. Functions of this protein include
a) Pumping drugs into the urine for excretion
b) Transport of drugs into liver hepatocytes
c) Transport of drugs into fetal circulation for fetal treatment
d) Transport of drugs from the intestinal lumen to the circulation
e) Transport of drugs from the bloodstream into brain cells

### PHARM-P-326
tier: claimed
form: mcq
type: single
claimed: b
Researcher is studying the bioavailability of commonly used antimuscarinics 
to treat irritable bowel syndrome. Medication A is administered in a 100 mg daily 
dose orally and 60 mg of the drug is absorbed from the gastrointestinal tract 
unchanged. Thus, the bioavailability of Medication A is
a) 40%
b) 60%
c) 70%
d) 80%
e) 90%

### PHARM-P-327
tier: claimed
form: mcq
type: single
claimed: d
A 27-year-old female with vulvovaginal candidiasis is given a one-time 100 
mg dose of oral fluconazole. She has no other pertinent medical problems and 

takes no prescription medications. Administration of the medication results in a 
peak plasma concentration of 20 mg/L. What is the apparent volume of drug 
distribution?
a) 0.5 L
b) 1 L
c) 3 L
d) 5 L
e) 50 L

### PHARM-P-328
tier: claimed
form: mcq
type: single
claimed: c
Pick out the right statement:
a) High molecular weight drugs get excreted in Urine
b) Lipid-soluble drugs with low molecular weight get excreted in biles
c) Antibiotics may undergoes active secretion

### PHARM-P-329
tier: claimed
form: mcq
type: single
claimed: d
Elimination is expressed as follows:
a) Rate of renal tubular reabsorption
b) Clearance speed of some volume of blood from substance
c) Time required to decrease the amount of drug in plasma by one-half
d) Clearance of an organism from a xenobiotic

### PHARM-P-330
tier: claimed
form: mcq
type: single
claimed: a
The most rapid eliminated drugs are those with glomerular filtration rate 
and active secretion but aren’t passively reabsorbed:
a) True
b) False

### PHARM-P-331
tier: claimed
form: mcq
type: single
claimed: d
Elimination rate constant (Kelim} is defined by the following parameter:
a) Rate of absorption
b) Maximal concentration of a substance in plasma
c) Highest single dose
d) Half life (t1/2)

### PHARM-P-332
tier: claimed
form: mcq
type: single
claimed: a
Half life (t1/2) is the time required to:
a) Change the amount of a drug in plasma by half during elimination
b) Metabolize a half of an introduced drug into the active
c) Absorb a half of an introduced drug
d) Bind a half of an introduced drug to plasma proteins

### PHARM-P-333
tier: claimed
form: mcq
type: single
claimed: b
Half life (t1/2) doesn’t depend on:
a) Biotransformation
b) Time of drug absorption
c) Concentration of a drug in plasma
d) Rate of drug elimination

### PHARM-P-334
tier: claimed
form: mcq
type: single
claimed: b
Binding of a drug to plasma proteins will tend to:
a) Decrease half-life.
b) Decrease its rate of glomerular filtration.
c) Increase its rate of biotransformation.
d) Increase its concentration in the plasma
e) Increase its pharmacological activity

### PHARM-P-335
tier: claimed
form: mcq
type: single
claimed: b
If a drug is eliminated by first order kinetics
a) A constant amount of the drug will be eliminated per unit time
b) Its clearance value will remain constant
c) Its elimination half-life will increase with dose
d) It will be completely eliminated from the body in 2 x half-life period

### PHARM-P-336
tier: claimed
form: mcq
type: single
claimed: b
Disappearance of most drugs from the plasma follows first order kinetics, 
which means that:
a) The rate of disappearance is independent of the amount of drug left at any 
time
b) The rate of disappearance is proportional to the amount of drug left at any 
time
c) The disposition mechanisms are saturated
d) The drug is rapidly metabolized
e) The rate of disappearance is proportional to clearance rate

### PHARM-P-337
tier: claimed
form: mcq
type: single
claimed: d
Drugs showing zero-order kinetics of elimination
a) Are more common than showing first-order kinetics
b) Shows exponential decrease with time
c) Have a t1/2 independent of dose
d) Show a plot of drug concentration versus time that is linear
e) Shows a constant fraction of the drug eliminated per unit time

### PHARM-P-338
tier: claimed
form: mcq
type: single
claimed: d
If a drug is not metabolized, is bound 50% to plasma protein, and has a renal 
clearance of 400 mL/min in man, the mode of excretion must be:
a) Glomerular filtration
b) Filtration and reabsorption
c) Tubular secretion
d) Filtration and secretion
e) Excretion by extrarenal route

### PHARM-P-339
tier: claimed
form: mcq
type: single
claimed: d
The loading dose (DL) of a drug is usually based on the
a) Total body clearance of the drug
b) Percentage of drug bound to plasma proteins
c) Fraction of drug excreted unchanged in the urine
d) Apparent volume of distribution and desired drug concentration in plasma
e) Area under the plasma drug concentration versus time curve (AUC)

### PHARM-P-340
tier: claimed
form: mcq
type: single
claimed: a
Which of the following results in a doubling of steady-state conc. of the drug
a) Doubling the rate of infusion
b) Maintaining the rate of infusion but doubling the loading dose
c) Doubling the rate of infusion and doubling the concentration of the infused 
drug.
d) Tripling the rate of infusion

### PHARM-P-341
tier: claimed
form: mcq
type: single
claimed: a
A student studying pharmacology is a member of a team that is conducting 
research related to the elimination of multiple anticoagulant medications. His 
duty as a member of the team is to collect serum M samples of the subjects every 
4 hours and send them for analysis of serum drug levels. He is also supposed to 
collect, document and analyze the data. For one of the subjects, he notices that 

the subject is eliminating 0.5 mg of the drug every 4 hours. Which of the following 
anticoagulants did this patient most likely consume?
a) Aspirin
b) Enoxaparin
c) Dabigatran
d) Fondaparinux
e) Apixaban

### PHARM-P-342
tier: claimed
form: mcq
type: single
claimed: c
A drug with a half life of 8 hours is administered by continuous intravenous 
infusion. How long will it take to reach 90% of its final steady-state level?
a) 12 hours
b) 18 hours
c) 25 hours
d) 30 hours
e) 40 hours

### PHARM-P-343
tier: claimed
form: mcq
type: single
claimed: c
A patient receives a single dose of antibiotics following a prostate needle 
biopsy. He takes 500 mg of ciprofloxacin immediately after completion of the 
procedure. The half-life of the medication is 8 h. At approximately how many half-
lives will it take for 90% of the drug to be excreted from the body?
a) 1.0
b) 2.0
c) 3.0
d) 3.3
e) 5

### PHARM-P-344
tier: claimed
form: mcq
type: single
claimed: d
Pharmacokinetic characteristics of propranolol include Vd = 300 L/70 kg, CL 
= 700 mL/min, and oral bioavailability f = 0.25. What is the dose needed to 
achieve a plasma level equivalent to a steady-state level of 20 ?g/L?
a) 4 mg
b) 8 mg
c) 12 mg
d) 24 mg
e) 48 mg

### PHARM-P-345
tier: claimed
form: mcq
type: single
claimed: a
A doctor write in a prescription ( Take 1 Capsule (3mg) every 6 hours ) and 
you know the t1/2 of the drug = 3 hours, then, what’s the maximal amount of the 
drug that would accumulate in Plasma?:
a) 4mg
b) 3mg
c) 7mg
d) 6mg

### PHARM-P-346
tier: claimed
form: mcq
type: single
claimed: c
Normally, acetaminophen has a Vd = 70L and C1 = 350 mL/min. If 
acetaminophen was administered to a patient with 50% renal function, what 
parameter would differ from normal?
a) Loading dose would be higher
b) Maintenance dose would be lower
c) t ½ would be higher
d) Vd would be 35L
e) Cl would be 700 mL/min

### PHARM-P-347
tier: claimed
form: mcq
type: single
claimed: d
A drug with elimination rate of 5mg/h had a 5mg/L serum level. If the urine 
concentration of the drug is 30mg/L and urine flow rate is 10mg/L what is the 
renal clearance?
a) 10L/h
b) 20 L/h
c) 40 L/h
d) 60 L/h

### PHARM-P-348
tier: claimed
form: mcq
type: single
claimed: a
A solution Verapamil is administered to the portal vein of the isolated 
perfused liver of a rat at a concentration of 8.9 mg/L. After 5 minutes, the 
concentration that is measured at the hepatic vein is 2.99 mg/L and the hepatic 
blood flow is 1050 mL/min. What is the hepatic extraction rate (ERH) of verapamil 
in this model/Hepatic clearance respectively
a) 0.5286/687.2 mL/min
b) 0.7563/656.5 mL/min
c) 1.3345/732.7 mL/min
d) 0.2123/504.4 mL/min

### PHARM-P-349
tier: claimed
form: mcq
type: single
claimed: a
A 28-year-old man with seborrheic dermatitis is prescribed a topical 
corticosteroid crème by his dermatologist in hopes of alleviating the chronic rash 
and erythema on the cheeks. Which of the following steps is most critical to 
achieve a therapeutic drug concentration in plasma?
a) Absorption
b) Distribution
c) Elimination
d) Glycosylation
e) Metabolism

### PHARM-P-350
tier: claimed
form: mcq
type: single
claimed: e
The route of drug administration is determined by
a) Water solubility of the drug
b) Lipid solubility of the drug
c) Ionization of the drug
d) Desirability of rapid onset of action of the drug
e) All of the above

### PHARM-P-351
tier: claimed
form: mcq
type: single
claimed: c
What is characteristic of the oral route?
a) Fast onset of effect
b) Absorption depends on GI tract secretion and motor function
c) A drug reaches the blood passing the liver
d) The sterilization of medicinal forms is obligatory

### PHARM-P-352
tier: claimed
form: mcq
type: single
claimed: c
Bioavailability differences among oral formulations of a drug are most likely 
to occur if the drug
a) Is freely water soluble
b) Is completely absorbed
c) Is incompletely absorbed
d) Undergoes little first-pass metabolism

### PHARM-P-353
tier: claimed
form: mcq
type: single
claimed: b
All of the following about oral drug absorption is true EXCEPT:
a) The most variable route of administration
b) The most complicated of administration
c) Duodenum is the major site of entry to the systemic circulation
d) Most drugs absorbed from the gastrointestinal tract enter directly the 
systemic circulation
e) First-pass metabolism by the liver limits the efficacy of many drugs.

### PHARM-P-354
tier: claimed
form: mcq
type: single
claimed: a
Pick the feature of the sublingual route:
a) Pretty fast absorption
b) A drug is exposed to gastric secretion
c) A drug is exposed more prominent liver metabolism
d) A drug can be administrated in a variety of doses

### PHARM-P-355
tier: claimed
form: mcq
type: single
claimed: c
Correct statements listing characteristics of a particular route of drug 
administration include all of the following EXCEPT:
a) Intravenous administration provides a rapid response
b) Intramuscular administration requires a sterile technique
c) Inhalation provides slow access to the general circulation
d) Subcutaneous administration may cause local irritation

### PHARM-P-356
tier: claimed
form: mcq
type: single
claimed: c
Parenteral administration:
a) Cannot be used with unconsciousness patients
b) Generally results in a less accurate dosage than oral administration
c) Usually produces a more rapid response than oral administration
d) Is too slow for emergency use

### PHARM-P-357
tier: claimed
form: mcq
type: single
claimed: b
What is characteristic of the intramuscular route of drug administration?
a) Only water solutions can be injected
b) Oily solutions can be injected
c) Opportunity of hypertonic solution injections
d) The action develops slower, than at oral administration

### PHARM-P-358
tier: claimed
form: mcq
type: single
claimed: b
Intravenous injections are more suitable for oily solutions:
a) True
b) False

### PHARM-P-359
tier: claimed
form: mcq
type: single
claimed: c
Which of the following routes have the highest bioavailability?
a) Oral
b) Rectal
c) SC
d) More than one answer

### PHARM-P-360
tier: claimed
form: mcq
type: single
claimed: c
Pick out the appropriate alimentary route of administration when passage 
of drugs through liver is minimized:
a) Oral
b) Transdermal
c) Rectal
d) Intraduodenal

### PHARM-P-361
tier: claimed
form: mcq
type: single
claimed: e
Which of the following is disadvantage of IM administration?
a) Larger volumes can be used
b) Can affect lab test
c) Painful
d) A and C
e) B and C

### PHARM-P-362
tier: claimed
form: mcq
type: single
claimed: a
A 79-year-old man with end-stage Alzheimer’s disease and dysphagia is 
taking multiple medications. Physical examination reveals xerostomia and a 
limited gag reflex. Which of the following routes of medication administration 
would provide the lowest serum drug concentration?
a) Enteral
b) Intramuscular
c) Intrathecal
d) Intravenous
e) Transdermal

### PHARM-P-363
tier: claimed
form: mcq
type: single
claimed: b
A 15-year-old boy who has diabetes and is insulin dependent is brought to 
the emergency department after collapsing at a baseball game. His blood sugar is 
463 mg/dL by finger stick. Which of the following routes of administration would 
be most efficacious for medications to bring the blood sugar down?
a) Intramuscular
b) Intravenous
c) Sublingual
d) Subcutaneous

### PHARM-P-364
tier: claimed
form: mcq
type: single
claimed: a
In an anaesthetized dog, repeated intravenous injection of ephedrine shows 
the phenomenon of
a) Anaphylaxis
b) Tachyphylaxis
c) Idiosyncrasy
d) Drug resistance

### PHARM-P-365
tier: claimed
form: mcq
type: single
claimed: c
Which of the following therapeutic systems provides continuous, 
unattended, controlled drug input for a long period without gastrointestinal or 
hepatic drug inactivation prior to systemic circulation ?
a) Parenteral
b) Oral
c) Transdermal
d) All the above
e) None of the above

### PHARM-P-366
tier: claimed
form: mcq
type: single
claimed: b
Volatile drug may be best administered by:
a) Oral route
b) Inhalation
c) Sublingual route
d) Intrathecal route
e) Rectal route

### PHARM-P-367
tier: claimed
form: mcq
type: single
claimed: a
The main route of administration of a drug to produce a local effect is
a) Topical
b) Oral
c) Parenteral

### PHARM-P-368
tier: claimed
form: mcq
type: single
claimed: c
When a drug has a low therapeutic index, that drug should be
a) Used mostly orally
b) Used mostly intravenously
c) Considered a potentially toxic substance
d) Given only in submilligram doses

### PHARM-P-369
tier: claimed
form: mcq
type: single
claimed: d
Biotransformation of the drugs is to render them:
a) Less ionized
b) More pharmacologically active
c) More lipid soluble
d) Less lipid soluble

### PHARM-P-370
tier: claimed
form: mcq
type: single
claimed: a
Biotransformation of medicinal substance results in:
a) Faster urinary excretion
b) Slower urinary excretion
c) Easier distribution in organism
d) Higher binding to membranes

### PHARM-P-371
tier: claimed
form: mcq
type: single
claimed: d
All of the following statements are true EXCEPT:
a) Biotransformation of drugs in the body usually yields products that diffuse 
across renal tubular membranes less readily than the parent compounds.
b) Biotransformation reactions often yield products that are inactive 
pharmacologically.
c) Biotransformation reactions can yield products that are pharmacologically 
more active than the parent compound
d) Biotransformation reactions can yield products that are more lipophilic 
than the parent compound.
e) In some cases, biotransformation reactions enhance the toxicity of 
chemicals introduced into the body.

### PHARM-P-372
tier: claimed
form: mcq
type: single
claimed: a
All of the about reaction of drug metabolism is correct EXCEPT:
a) Water soluble drugs must first be metabolized in the liver
b) Phase 1 reaction function to convert lipophilic molecules into lipophobic 
molecules
c) Phase 1 reactions involved in drug metabolism catalyzed by the p450 
system
d) Phase II include conjugation with endogenous substances

### PHARM-P-373
tier: claimed
form: mcq
type: single
claimed: e
Which of the following is entirely microsomal?:
a) Acetylation and methylation of substances
b) Transformation of substances  due to oxidation, reduction or hydrolysis…
c) Glucuronide formation
d) The use of Ziegler’s enzyme

### PHARM-P-374
tier: claimed
form: mcq
type: single
claimed: b
All of the following about drug metabolism is true EXCEPT:
a) Pro-drugs must be metabolized to their active forms
b) First-order kinetics metabolism means that a constant amount of drug is 
metabolized per unit of time
c) Zero-order kinetics metabolism the enzyme is saturable
d) Ethanol follows zero order kinetics
e) None of the above

### PHARM-P-375
tier: claimed
form: mcq
type: single
claimed: c
Pick out the right statement:
a) Microsomal oxidation always results in inactivation of a compound
b) Microsomal oxidation results in a decrease of compound toxicity
c) Microsomal oxidation results in an increase of ionization and water 
solubility of a drug
d) Microsomal oxidation results in an increase of lipid solubility of a drug thus 
its excretion from the organism is facilitated

### PHARM-P-376
tier: claimed
form: mcq
type: single
claimed: a
Conjunction is:
a) Process of drug reduction by special enzymes
b) Process of drug oxidation by special oxidases
c) Coupling of a drug with an endogenous substrate
d) Solubilization in lipids

### PHARM-P-377
tier: claimed
form: mcq
type: single
claimed: b
Metabolic transformation and conjugation usually results in an increase of a 
substance biological activity:
a) True
b) False

### PHARM-P-378
tier: claimed
form: mcq
type: single
claimed: b
The addition of glucuronic Acid to drug
a) Lowers its water solubility.
b) Usually leads to inactivation of the drug
c) Is an example of Phase 1 reaction.
d) Occurs at the same rate in adults and newborns.
e) Involves cytochrome P450

### PHARM-P-379
tier: claimed
form: mcq
type: single
claimed: b
In case of liver disorders accompanied by a decline in microsomal enzyme 
activity, the duration of action of some drugs is:
a) Decreased
b) Enlarged
c) Remained unchanged
d) Changed insignificantly

### PHARM-P-380
tier: claimed
form: mcq
type: single
claimed: e
An elder man was brought up to the emergency room for suspicion of Liver 
cirrhosis. His wife mentioned him having severe headache throughout the day, 
making swallow up to 10 analgesic analgesic pills which she forgot the name of. 
What was the drug?
a) NAISD
b) Isoniazid
c) Acetaminophen
d) Halothane
e) None of the above

### PHARM-P-381
tier: claimed
form: mcq
type: single
claimed: c
One of the following drugs undergoes metabolism just to be more effective 
and is the less-active form of morphine,
a) Levodopa
b) Enalapril
c) Codeine
d) Minoxidil

### PHARM-P-382
tier: claimed
form: mcq
type: single
claimed: b
One of the following drugs can be used to reduce blood pressure in patients 
with Chronic Renal Insufficiency:
a) Aspirin
b) Enalapril
c) Digoxin
d) Atenolol

### PHARM-P-383
tier: claimed
form: mcq
type: single
claimed: b
CYT3A4 heavily contributes to what part of Liver metabolism?
a) Conjugation
b) Oxidation
c) Reduction
d) Hydrolysis

### PHARM-P-384
tier: claimed
form: mcq
type: single
claimed: a
All of the following is true EXCEPT:
a) UGT is the predominant Phase 2 enzyme for lifetime
b) Glutathione conjugates are excreted in bile or are converted to 
mercapturic acid
c) For the sake of drugs’ inactivation, Methyltransferase may be used.
d) N-acetylated cysteine conjugates appear in urine by Active transport.

### PHARM-P-385
tier: claimed
form: mcq
type: single
claimed: e
Which drug after undergoing Acyl glucuronidation Become insanely 
reactive?
a) Ibuprofen
b) Paracetamol
c) NASIDs
d) A+B
e) A+C

### PHARM-P-386
tier: claimed
form: mcq
type: single
claimed: b
Paracetamol undergoes both Acetylation and Glucuronidation but without 
GSH the alternative CYT-450 dependent pathway causes hepatoxicity.
a) True
b) False

### PHARM-P-387
tier: claimed
form: mcq
type: single
claimed: a
Which of the following drugs may inhibit the hepatic microsomal P450 and 
contains Imidazole group
a) Cimetidine
b) Ethanol
c) Phenobarbital
d) Procainamide
e) Rifampin

### PHARM-P-388
tier: claimed
form: mcq
type: single
claimed: e
Antiepileptic drug, leads to tolerance to drug ,after 2-3 weeks it will not 
activate its metabolism and it is needed to increase the dose and ultimately 
inhibits the hepatic microsomal enzymes.
a) Ethanol
b) St. John’s wort
c) Ritonavir
d) Byproduct of tobacco
e) Carbamazepine

### PHARM-P-389
tier: claimed
form: mcq
type: single
claimed: c
Which one of the statements regarding microsomal enzymes is not correct
a) They lack specificity
b) Capable of metabolizing substances of different structure
c) Only catalyze reaction of compounds which are lipid insoluble
d) All the above

### PHARM-P-390
tier: claimed
form: mcq
type: single
claimed: c
An 82-year-old man is admitted to the hospital after a new diagnosis of 
multiple myeloma. Treatment is initiated with bortezomib, lenalidomide, and 
dexamethasone. Intravenous morphine is administered at regular intervals for 
control of bone pain. Two days later his creatinine increases from 1.0 to 2.3 
mg/dL. He is noted to be lethargic with respirations of 8/min (normal >12). 
Naloxone is administered and he becomes more alert with increased respirations. 
Which of the following may explain his response to morphine?
a) Decreased bioavailability
b) Increased volume of distribution
c) Accumulation of morphine metabolites
d) Inhibition of liver P450 enzymes
e) Downregulation of opioid receptors

### PHARM-P-391
tier: claimed
form: mcq
type: single
claimed: c
A 5-year-old boy is brought to the emergency room by his mother. One hour 
ago, he ingested an unknown quantity of one of her prescription medications. 
Serum testing shows the boy’s drug level is 5 mg/dL. The drug is known to have a 
half life of 1 hour, a volume of distribution of 150 ml, a bioavailability of 50%, and 
follow first-order elimination kinetics. Which of the following doses did the boy 
ingest?
a) 15mg
b) 20mg
c) 30mg
d) 40mg
e) 60mg

### PHARM-P-392
tier: claimed
form: mcq
type: single
claimed: d
A 45-year-old man is started on an intravenous neuroleptic drug for 
treatment of seizures. His weight is 75 kg. The drug has a volume of distribution 
of 0.5 L/kg. If the desired serum concentration is 20 mg/L, what is the appropriate 
loading dose?
a) 37.5mg
b) 100mg
c) 375mg
d) 750mg
e) 1500mg

### PHARM-P-393
tier: claimed
form: mcq
type: single
claimed: c
A 45-year-old man is started on an intravenous neuroleptic drug for 
treatment of seizures in the hospital. He achieves a steady state plasma drug 

concentration of 20 mg/L. After no seizure activity for 48 hours, plans are made 
to discharge him on an oral form of his seizure drug. The drug’s clearance rate is 
0.25 L/hr and bioavailability is 50%. Which of the following is an appropriate oral 
dosing regimen?
a) 10mg once per day
b) 20mg twice per day
c) 120mg twice per day
d) 1000me twice per day
e) 2000mg once per day

### PHARM-P-394
tier: claimed
form: mcq
type: single
claimed: b
You are currently employed as a clinical researcher working on clinical trials 
of a new drug to be used for the treatment of Parkinson’s disease. Currently, you 
have already determined the safe clinical dose of the drug in a healthy patient. 
You are in the phase of drug development where the drug is studied in patients 
with the target disease to determine its efficacy. Which of the following phases 
is this new drug currently in?
a) Phase 1
b) Phase 2
c) Phase 3
d) Phase 4

### PHARM-P-395
tier: claimed
form: mcq
type: single
claimed: e
A 49-year-old man with diabetes mellitus takes subcutaneous insulin for his 
insulin-dependent diabetes mellitus. He takes 4 U of regular insulin every 12 h to 
maintain his blood sugar in the range of 80 to 140 mg/dL. This route of 

administration allows for absorption of insulin by which of the following 
processes?
a) active transport
b) Facilitated transport
c) Osmosis
d) Passive transport
e) Simple diffusion

### PHARM-P-396
tier: claimed
form: mcq
type: single
claimed: a
An 80-year-old male nursing home resident is hospitalized on a morphine 
drip to control pain for his terminal metastatic pancreatic cancer. Morphine 
undergoes phase I and phase II metabolism in the liver as well as being 
metabolized by other enzymes. Some of these metabolic reactions decrease with 
age. Which of the following metabolic reactions is likely still intact in this patient?
a) 
a) Glucuronidation
b) Hydrolysis
c) Oxidation
d) Reduction
e) Unmasking of a functional group

### PHARM-P-397
tier: claimed
form: mcq
type: single
claimed: a
A 44-year-old black male is brought to the emergency department with 6 h 
of worsening lethargy and confusion. Past medical history is significant for easy 
bruising, 3 months of bone pain, and frequent pneumococcal infections. Labs 
were ordered, revealing serum calcium of 17 mg/dL (normal: 9.0 to 10.5 mg/dL). 
To rapidly lower his serum calcium, you administer calcitonin. However, 
calcitonin alone is insufficient because it is known to rapidly and suddenly lose its 
effectiveness within 2 to 3 days of repeated dosing. For this reason, a 
bisphosphonate, which take 2 to 3 days to become effective, is added 
simultaneously. What is the term for the rapid decrease in response to calcitonin?
a) Anaphylaxis
b) Prophylaxis
c) Tachyphylaxis
d) Tolerance

### PHARM-P-398
tier: claimed
form: mcq
type: single
claimed: d
Regarding the use of a daily baby aspirin, oral fiber supplements, and a 
daily “water” pill in an 89-year-old man with hypertension and coronary artery 
disease, which of the following statements is true regarding pharmacology in the 
elderly patient?
a) Coexisting disease states are unlikely to produce additive impairment
b) Elderly patients are less sensitive to drug effects
c) Elderly patients are less sensitive to drug side effects
d) Elimination of drugs becomes impaired with age
e) Responses to compensate for drug accumulation are satisfactory

### PHARM-P-399
tier: claimed
form: mcq
type: single
claimed: b
When comparing the administration of local anesthesia in a 4-year-old 
healthy boy to an 80-year-old man with a history of hypertension, cirrhosis, and 
diabetes, which of the following statements is likely to be true?
a) Liver failure is less likely a problem in the older patient
b) Maximal dose of anesthetic must be calculated
c) Older patients require higher doses of anesthetic
d) Older patients will have a better response to anesthetic
e) Younger patients will have a better response to anesthetic

### PHARM-P-400
tier: claimed
form: mcq
type: single
claimed: a
Drug A and Drug B are of equal magnitude. If Drug A and Drug B are 
combined together, this would be an example of which of the following?
a) Additive effects
b) Neutralization
c) Potentiation
d) Synergism

### PHARM-P-401
tier: claimed
form: mcq
type: single
claimed: e
A new vasopressor in development, Drug X, is a partial agonist at a1-
adrenergic receptors. Epinephrine is a full agonist at these same receptors. Which 
of the following statements is true regarding the potency of Drug X compared to 
epinephrine?
a) Drug X and epinephrine are equally potent because they act on the same 
receptors
b) Drug X is more potent because it is a partial agonist
c) Epinephrine is more potent because it is a full agonist
d) Epinephrine is more potent because it is an endogenous neurotransmitter
e) Relative potency cannot be determined from the information given

### PHARM-P-402
tier: claimed
form: mcq
type: single
claimed: e
Healthy adult volunteers are enrolled in a phase 1 clinical trial investigating 
the properties of a newly developed oral antimicrobial agent. The drug is 
administered in different amounts to the volunteers over the course of several 
weeks to determine the best dosage that minimizes toxicity while maintaining 
trough levels above the minimum inhibitory concentration. While reviewing the 
data, the researchers note that the drug's half-life seems to vary amongst the 
study participants. An increase in which of the following pharmacologic 
parameters is most likely responsible for the longer half-life seen in certain 
individuals?
a) Drug glucuronidation
b) Glomerular filtration rate
c) Oral bioavailability
d) Peak serum drug levels
e) Volume of distribution

### PHARM-P-403
tier: claimed
form: mcq
type: single
claimed: d
img: flagged/PHARM-P-403-glucuronidation-saturation-graph.jpg
note: Source stem includes a hand-annotated remark: "PROPORTION not the actual dose's concentration."
A large, multinational drug corporation conducts a phase 1 clinical trail to 
evaluate the safety profile and pharmacokinetics properties of a new drug 
designed to treat refractory epilepsy. Initial studies showed that the drug 
undergoes extensive metabolism by the 
liver into glucuronidation byproducts that 
are primarily excreted by the kidneys. The 
curve 
bellow 
demonstrates 
the 
glucuronidation rate of the drug over a 
wide range of doses.
a) A constant proportion of the drug is 
metabolized past point 3
b) Bioavailability of the drug is highest 
at point 1
c) Biotransformation of the drug ceases near point 2
d) Metabolism begins to switch to zero-order kinetics near point 2
e) The rate of drug metabolism is not dependent on dose before point 1

### PHARM-P-404
tier: claimed
form: mcq
type: single
claimed: d
A new aminoglycoside antibiotic is developed that is believed to be 
particularly effective against Pseudomonas. The volume of distribution of the 
drug is measured in a group of volunteers and is determined to be 4.5 L. This new 
drug is most likely to have which if the following properties:
a) It has low molecular weight
b) It is lipophilic
c) It doesn’t bind to albumin
d) It is highly charged
e) It has high bioavailability

### PHARM-P-405
tier: claimed
form: mcq
type: single
claimed: d
img: flagged/PHARM-P-405-vancomycin-dosing-interval-peak-trough-graph.jpg
Researchers are developing a new glycopeptide antibiotic similar to 
vancomycin. Susceptibility testing reveals that the new drug is bactericidal 
against gram-positive organisms at serum concentrations above 15 mcg/mL. Two 
different dosage regimens are developed to achieve a target serum trough 
concentration of 15-20 mcg/mL: one administered as 1 gram every 6 hours and 
the other as 2 grams every 12 hours. The two regimens are tested in healthy 
volunteers during an early-phase clinical trial, and the following pharmacokinetic 
profiles are obtained. 
 
 
 
 
 
 
Compared to the 12-hour dosing regimen, the 6-hour regimen is most likely to 
exhibit which of the following features?
a) Decreased renal clearance
b) Higher average plasma drug levels
c) Improved patient compliance
d) Lower drug toxicity
e) Narrower therapeutic window

### PHARM-P-406
tier: claimed
form: mcq
type: single
claimed: d
img: flagged/PHARM-P-406-neonate-adult-plasma-concentration-graph.jpg
note: Source includes a remark after the answer explaining why (A) and (C) are wrong: water-soluble drugs in infants have higher Vd and thus lower plasma concentration, contrary to what higher plasma-protein levels would suggest.
Researchers develop a novel glycopeptide antibiotic similar to 
vancomycin(Hydrophilic drug) that is bactericidal against many Gram-positive 
bacteria. From animal studies, they determine that the effective drug dosage is 5 
mg/kg/day  administered intravenously in divided doses. In a clinical trial, the 
antibiotic is administered to adult and neonatal patients with gram-positive 
infections. The drug is found to be effective in adults but not in neonates. During 
further analysis, plasma concentrations of the drug are measured in both groups, 
with the results shown in the image below: 
Compared to adults, which of 
the 
following 
neonatal 
factors is the most likely 
cause of the difference in 
drug effectiveness?
a) Decreased 
CTY450 
activity
b) Decreased renal blood 
flow
c) Elevated 
Plasma 
protein levels
d) High body water content

### PHARM-P-407
tier: claimed
form: mcq
type: single
claimed: b
A 34-year-old kidney transplant patient treated with cyclosporine comes to 
the office due to nausea and anorexia. The patient underwent transplantation 6 
months ago and had been doing well until recently. On examination, his blood 
pressure is 160/96 mm Hg. There is no tenderness at the site of the transplanted 
kidney. Serum creatinine is 3.4 mg/dL, and the serum cyclosporine level is 
markedly increased. A month ago, he had normal blood pressure and normal 
levels of cyclosporine and serum creatinine. Further questioning reveals that the 
patient has been drinking increased amounts of grapefruit juice lately as part of 
an attempt to improve his overall health. Which of the following mechanisms is 
most likely responsible for this patient's current condition?
a) Alteration of gastric acidity
b) Inhibition of cytochrome P450 enzymes in the gut wall
c) Modification of transmembrane drug transport
d) Pharmacodynamic potentiation
e) Reduction of plasma protein binding

### PHARM-P-408
tier: claimed
form: mcq
type: single
claimed: a
img: flagged/PHARM-P-408-two-nsaid-formulations-plasma-graph.jpg
note: Source includes a worked elimination remark after the answer explaining why B, C, D, and E are wrong.
A pharmaceutical company in the final stages of designing a new 
nonsteroidal anti-inflammatory agent develops 2 different oral formulations of 
the 
drug. 
Two 
groups 
of 
volunteers 
are 
each 
administered 
a 
different 
formulation, and average plasma 
drug levels are monitored over 
the next 12 hours. The results are 
shown below:
a) Delayed 
intestinal 
absorption
b) Enhanced 
CYP 
enzyme 
induction
c) Increased biliary excretion
d) Increased enterohepatic cycling
e) Reduced first-pass metabolism

<!-- batch 04 — raw/practice/Pharmacology PYQ and Bank Questions.pdf, pages
  116-134 of 134, credited (p134) to Mohanad Al-ahmad -- the same author as
  batch 03's p76-115 "Pharmacokinetics" list, a separate compiled set. RUN-PLAN
  row 12. Numbered 1)-74), each followed inline by an "ANS:" line -> tier claimed
  throughout (student-compiled, not an instructor key). One real gap: #6 never
  appears anywhere in the source (numbering jumps 5 -> 7) -- confirmed against
  the raw page text, not a Job A drop, so there is no PHARM-P entry for it.
  PHARM-P-409 through PHARM-P-481 (73 entries for the 73 questions that exist).

  Q8 (PHARM-P-415) is answered entirely from a photo ("This picture represent
  which Route?" -- a wheal from an intradermal test injection) and is saved to
  flagged/. Every page 116-134 was checked for embedded images; the only other
  ones found (a black divider bar and a decorative stock photo of pills on p115,
  just before this range starts) are not load-bearing to any question and were
  not saved. -->

### PHARM-P-409
tier: claimed
form: mcq
type: single
claimed: c
Correct statements listing characteristics of a particular route of 
drug administration include all of the following EXCEPT:
a) Intravenous administration provides a rapid response
b) Intramuscular administration requires a sterile technique
c) Inhalation provides slow access to the general circulation
d) Subcutaneous administration may cause local irritation

### PHARM-P-410
tier: claimed
form: mcq
type: single
claimed: a
Biological barriers include all except:
a) Renal tubules
b) Cell membranes
c) Capillary walls
d) Placenta

### PHARM-P-411
tier: claimed
form: mcq
type: single
claimed: b
A small amount of the volume of distribution is common for 
lipophilic substances easy penetrating through barriers and widely 
distributing in plasma, interstitial and cell fluids:
a) True
b) False

### PHARM-P-412
tier: claimed
form: mcq
type: single
claimed: a
Half-life (t ½) is the time required to:
a) Change the amount of a drug in plasma by half during elimination
b) Metabolize a half of an introduced drug into the active metabolite
c) Absorb a half of an introduced drug
d) Bind a half of an introduced drug to plasma proteins

### PHARM-P-413
tier: claimed
form: mcq
type: single
claimed: c
If we give 2 people the same drug, all of the following will be the 
same except
a) mechanism of clearance
b) mechanism of metabolism
c) Half-life

### PHARM-P-414
tier: claimed
form: mcq
type: single
claimed: a
The similarity between the IV route and the rectal route is :
a) both can NOT be given to unconscious patient
b) both can be given to unconscious patient
c) both are parenteral routes
d) NON of the above

### PHARM-P-415
tier: claimed
form: mcq
type: single
claimed: a
img: flagged/PHARM-P-415-intradermal-injection-wheal-photo.jpg
This picture represent which Route?
a) Intradermal to check allergy to penicillin
b) Intravenous to check allergy to penicillin
c) Intramuscular to check allergy to penicillin

### PHARM-P-416
tier: claimed
form: mcq
type: single
claimed: a
If a patient took a drug and after 12 hours when the 
concentration was measured it was 800 mg so what was the initial 
amount of the drug ( half life = 4 hours ) ?
a) 6400
b) 3200
c) 1600
d) 800

### PHARM-P-417
tier: claimed
form: mcq
type: single
claimed: b
which of those deals with pharmacokinetics :-
a) signal transduction
b) moving across biological membrane
c) NON of the above

### PHARM-P-418
tier: claimed
form: mcq
type: single
claimed: a
if 93% of the drug eliminates in 24H what is t 1⁄2 :
a) 6 hours
b) 12 hours
c) 3 hours
d) 4 hours

### PHARM-P-419
tier: claimed
form: mcq
type: single
claimed: a
An unconscious patient arrived to the emergency room suffers 
from hypoglycemia (low glucose levels in the blood), and you want 
to administer glucose. Other than Intravenous administration, what 
route of administration is BEST to be used to save his life?
a) Intramuscular.
b) Oral.
c) Inhalational.
d) intradermal.
e) Sublingual.

### PHARM-P-420
tier: claimed
form: mcq
type: single
claimed: e
Drug X is a weak base (pKa 9.0). What percentage will be in the 
unionized form at an intestinal pH of 7.0?
a) 99
b) 50
c) 10
d) 90
e) 1

### PHARM-P-421
tier: claimed
form: mcq
type: single
claimed: c
Which of the following condition may Increase bioavailability 
(after oral drug administration)?
a) A patient who also takes a drug that enhances liver enzymes
b) The administered drug is a peptide drug with 17 amino acid units.
c) A patient with a condition that increases blood flow to intestines.
d) A patient had a previous surgery to remove half of the stomach.
e) A patient with inflammatory bowel disease in small intestine

### PHARM-P-422
tier: claimed
form: mcq
type: single
claimed: d
administration of ammonium chloride , as a weak acid increases 
urinary clearance of a drug . it is reasonable to assume that this 
drug is :
a) strong acid
b) strong base
c) neutral compound
d) weak Base

### PHARM-P-423
tier: claimed
form: mcq
type: single
claimed: b
what is the mechanism that is responsible for absorption in the 
GIT :
a) active transport
b) passive diffusion
c) BOTH A+B
d) NON of the above

### PHARM-P-424
tier: claimed
form: mcq
type: single
claimed: c
the oral rout of drug administration tend to be associated with 
all of the following except :
a) poor compliance
b) relative safety
c) rapid response
d) convenience

### PHARM-P-425
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is the loading dose of a IV drug having a 
volume of distribution of 150L , if the desired plasma concentration 
is 15mg/L ?
a) 75mg
b) 150mg
c) 2.25 mg
d) 5 g

### PHARM-P-426
tier: claimed
form: mcq
type: single
claimed: c
first hepatic metabolism may occur when drug is given :
a) intramuscular
b) sublingual
c) rectal
d) subcutaneous
e) none of the above

### PHARM-P-427
tier: claimed
form: mcq
type: single
claimed: e
The variation in pharmacological responses to drugs among 
individuals can be attributed to :
a) drug – drug interaction
b) sex
c) diet
d) age
e) all of the above

### PHARM-P-428
tier: claimed
form: mcq
type: single
claimed: d
Aspirin is a weak organic acid with pKa of 3.5 , what percentage 
of a given dose will be unionized at stomach pH of 2.5 :
a) 1%
b) 10%
c) 50%
d) 90%
e) 99%

### PHARM-P-429
tier: claimed
form: mcq
type: single
claimed: a
which of the following is related to rectal administration :
a) rectal absorption if often erratic and incomplete
b) rectal absorption if often erratic and complete
c) NON of the above

### PHARM-P-430
tier: claimed
form: mcq
type: single
claimed: a
Which of the following is true about drug absorption from GIT:
a) passive diffusion is the principle mechanism of drug absorption
b) the stomach is the major site of drug absorption
c) gastric emptying doesn’t affect the rate of drug absorption
d) intestinal motility has no effect on the rate or extent of drug 
absorption
e) all of the above

### PHARM-P-431
tier: claimed
form: mcq
type: single
claimed: b
which of the following is correct about bound protein :
a) binding is mainly done by globulins
b) the bound drug is pharmacologically ineffective
c) A + B
d) NON of the above are correct

### PHARM-P-432
tier: claimed
form: mcq
type: single
claimed: c
which of the following is true about first order kinetics :
a) most of drugs follow it
b) effected by concentration of the drug
c) ALL of the above
d) NON of the above

### PHARM-P-433
tier: claimed
form: mcq
type: single
claimed: a
Maintenance dose can be affected by volume of distribution. 
Loading dose can be affected by clearance
a) True
b) False

### PHARM-P-434
tier: claimed
form: mcq
type: single
claimed: e
1ST pass metabolism refers to
a) drug-receptor binding
b) drug-plasma protein binding
c) hepatic drug metabolism when given IV
d) hepatic drug metabolism & elimination for albumin-bound drugs
e) hepatic drug metabolism during transport from the gut to the blood

### PHARM-P-435
tier: claimed
form: mcq
type: single
claimed: e
Pharmacokinetics deal with
a) drug interaction with its intracellular receptor
b) dose-response quantitation
c) drug mechanism of action
d) toxicological response of drugs
e) none of the above

### PHARM-P-436
tier: claimed
form: mcq
type: single
claimed: e
Drug distribution is affected by :
a) blood flow to the tissues
b) drug structure & lipid solubility
c) capillary structure & permeability
d) drug binding to plasma protein
e) all of the above

### PHARM-P-437
tier: claimed
form: mcq
type: single
claimed: e
All of the following affect drug’s bioavailability except
a) 1st pass metabolism
b) drug’s hydrophobicity
c) drug’s chemical instability
d) drug’s chemical formulation
e) time needed to reach Css ( concentration at steady state )

### PHARM-P-438
tier: claimed
form: mcq
type: single
claimed: e
The duration of drug action correlates with all of the following 
except :
a) the rate of drug metabolism
b) the rate of drug excretion
c) the bioavailability of the drug
d) the administered dose of the drug
e) the molecular weight of the drug

### PHARM-P-439
tier: claimed
form: mcq
type: single
claimed: b
Which of the following is true regarding drug absorption from 
GIT
a) the ileum is the major site for drug absorption
b) passive diffusion is the primary mechanism of absorption
c) giving drug with food doesn’t alter drug absorption
d) ANS has no effect on drug absorption
e) patient general health does not affect drug absorption

### PHARM-P-440
tier: claimed
form: mcq
type: single
claimed: b
75 mg of drug T is given orally , 15mg damaged by stomach 
environment , 15mg is lost during 1st pass metabolism , drug T 
bioavailability is
a) 40%
b) 60%
c) 75%
d) 100%
e) can’t be calculated

### PHARM-P-441
tier: claimed
form: mcq
type: single
claimed: d
Drug A has a half-life of 2hours , the time needed to reach 90% 
of steady state concentration CSS
a) 2 hours
b) 4 hours
c) 6 hours
d) 6.6 hours
e) 8.6 hours

### PHARM-P-442
tier: claimed
form: mcq
type: single
claimed: b
If a decrease in urine pH enhance the urinary excretion of a 
drug , it’s reasonable to assume that this drug is
a) weak acid
b) weak base
c) strong acid
d) strong base
e) neutral

### PHARM-P-443
tier: claimed
form: mcq
type: single
claimed: d
The half-life of a drug is influenced by
a) volume of distribution
b) clearance
c) toxic dose
d) a & b
e) none of the above

### PHARM-P-444
tier: claimed
form: mcq
type: single
claimed: a
First pass hepatic effect refers to:
a) Liver metabolism of drugs delivered via the portal vein.
b) Activation of drugs by hepatic enzymes.
c) Storage of drugs in the liver.
d) Biliary excretion of drugs.
e) E-Liver metabolism of drugs delivered via the hepatic artery.

### PHARM-P-445
tier: claimed
form: mcq
type: single
claimed: d
First-order elimination process:
a) Is characterized by drug dose-dependent half-life of elimination 
(T1/2e).
b) Applies to a limited number of drugs in clinical practice.
c) Is not applicable to the rate of drug metabolism 
(biotransformation).
d) Proceeds at rates dependent on drug concentration.
e) Is characterized by all listed features.

### PHARM-P-446
tier: claimed
form: mcq
type: single
claimed: c
Biotransformation (metabolism) of drugs usually results in 
products that are likely to:
a) Have wide tissue distribution.
b) Produce severe side effects.
c) Be inactive pharmacologically.
d) Interact with target receptors similar to the parent drug.
e) Be more effective than parent drug.

### PHARM-P-447
tier: claimed
form: mcq
type: single
claimed: e
When drugs are administered orally:
a) Active transport is the main mechanism of drug absorption.
b) The stomach is the major site of absorption.
c) Gastric emptying does not effects the rate of drug absorption.
d) The pharmacological response tend to be rapid.
e) Incomplete absorption is likely consequence.

### PHARM-P-448
tier: claimed
form: mcq
type: single
claimed: c
Drug administered rectally are:
a) Not subjected to first pass hepatic effect.
b) Characterized by predictable pattern of absorption.
c) In general no favored by the patients.
d) Likely to be complicated with severe vomiting.
e) Characterized by all of the listed facts.

### PHARM-P-449
tier: claimed
form: mcq
type: single
claimed: b
Which of the following statements is true about drug binding to 
plasma proteins:
a) Binding is an irreversible process.
b) Bound drug is pharmacologically inactive.
c) Drug-protein complex is effectively excreted in urine.
d) Drugs are mainly bound to plasma globulin.
e) None of the listed statements.

### PHARM-P-450
tier: claimed
form: mcq
type: single
claimed: a
Which of the following is the most frequent mechanism of drug 
transport across biological membranes?
a) Passive diffusion.
b) Active transport.
c) Filtration.
d) Carrier-mediated process.
e) All of the listed mechanism have comparable frequency.

### PHARM-P-451
tier: claimed
form: mcq
type: single
claimed: a
Which of the following process is considered a pharmacokinetic 
process in pharmacology?
a) Drug transport across biological membranes.
b) Drug-receptor interaction.
c) Dose-response relationships.
d) Mechanism of drug action.
e) Toxicological response of drugs.

### PHARM-P-452
tier: claimed
form: mcq
type: single
claimed: e
The elimination half-life (T1/2e) of the drug:
a) is likely to reflect the duration of drug action.
b) is correlated with the elimination rate constant (Ke) of drug.
c) is useful for the estimation of dose interval (T).
d) cannot be estimated for drugs eliminated via zero-order kinetics.
e) Is associated by all of the listed facts.

### PHARM-P-453
tier: claimed
form: mcq
type: single
claimed: b
For drug with half-life elimination (T1/2e) of 250 minutes 
administered by I.V. infusion the therapeutic plasma steady state 
concentration (Css) “95% of the theoretical value” is expected to be 
achieved at:
a) 67 minutes.
b) 20 hours .
c) 12 hours.
d) 2days.
e) One week.

### PHARM-P-454
tier: claimed
form: mcq
type: single
claimed: b
If 88% of a drug dose is eliminated, via first-order kinetics, in 
120 hours then the half-life of elimination (T1/2e) is expected to be:
a) 15 hours.
b) 40 hours.
c) 60 hours.
d) 120 hours.
e) Greater than 120 hours.

### PHARM-P-455
tier: claimed
form: mcq
type: single
claimed: a
A pharmacological response might be delayed, reduced, or 
blocked by all of the following, EXCEPT:
a) Drug that goes rapid distribution.
b) a drug that does not get its site of action.
c) Abnormal target receptor.
d) Lack of absorption at site of administration.
e) The drug that is not soluble in water.

### PHARM-P-456
tier: claimed
form: mcq
type: single
claimed: e
Drugs that are highly bound (greater than 90%) to plasma 
protein are likely to:
a) Be associated with large volume of distribution (Vd).
b) Have very short half-life off elimination(T1/2e).
c) Be associated with wide therapeutic index (TI).
d) Have short duration of action.
e) Be characterized by low renal clearance values.

### PHARM-P-457
tier: claimed
form: mcq
type: single
claimed: e
Intravenous route of drug administration is associated with:
a) Absence of an absorption process.
b) High risk of systemic toxicity.
c) Rapid response.
d) Potential risks of topical and systemic infections.
e) All of the listed features.

### PHARM-P-458
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is the expected loading dose (Dl) of a 
drug having volume of distribution (Vd) value of 150 liter, if desired 
plasma concentration is 5 microgram/ml?
a) 225 mg
b) 450 mg
c) 750 mg
d) 1.5 mg
e) 5.0 mg

### PHARM-P-459
tier: claimed
form: mcq
type: single
claimed: c
Estimation of the maintenance (Dm) of drug depends on all of 
the following EXCEPT:
a) The dose interval (T).
b) The desired plasma steady state concentration (Css).
c) The absorption rate constant (Ka).
d) The drug Bioavailability (F).
e) Systemic clearance (CL).

### PHARM-P-460
tier: claimed
form: mcq
type: single
claimed: e
First order kinetics and zero-order kinetics are similar in:
a) Both of them are dose-dependent
b) Both of them are not susceptible to phase I and II metabolism
c) all of the listed statements are correct
d) Both of them have fixed half-lives.
e) Both of them are metabolized in the liver

### PHARM-P-461
tier: claimed
form: mcq
type: single
claimed: c
The principle organ for drug excretion is
a) intestine
b) lungs
c) kidneys
d) liver
e) CNS

### PHARM-P-462
tier: claimed
form: mcq
type: single
claimed: e
Which of the following conditions will INCREASE the volume of 
distribution of medications?
a) All of the listed conditions.
b) Conditions of dehydration.
c) Hydrophilic medications,
d) lonized medications.
e) Decrease liver functions.

### PHARM-P-463
tier: claimed
form: mcq
type: single
claimed: d
A drug was administered orally and intravenously in two 
different patients. The drug in both patients will be similar in:
a) Bioavailability.
b) Peak concentration.
c) Onset of action.
d) Half-life.
e) Potency

### PHARM-P-464
tier: claimed
form: mcq
type: single
claimed: b
A patient had given 400 mg of drug Z. After 70 hours, the 
amount left of the drug in the body was calculated to 12.5 mg. What 
is the half-life of drug Z?
a) 5.6 hours.
b) b.14 hours.
c) 32 hours.
d) Can not be calculated
e) 12.5 hours.

### PHARM-P-465
tier: claimed
form: mcq
type: single
claimed: d
What is the advantage of loading dose?
a) It will delay therapeutic effect of the drug.
b) It will increase the potency of the drug.
c) It will increase the half-life of the drug.
d) It will shorten the onset of action of the drug.
e) It will increase efficacy of the drug.

### PHARM-P-466
tier: claimed
form: mcq
type: single
claimed: c
The first half-life of a first-order kinetics drug is:
a) Shorter than the second half-life for the same drug after the same 
dose.
b) Shorter than the second half-life for the same drug after a higher 
dose.
c) Similar to the second half-life. for the same drug after a higher 
dose.
d) Longer than the first half-life for the same drug after a higher dose.
e) Longer than the second half-life for the same drug after the same 
dose.

### PHARM-P-467
tier: claimed
form: mcq
type: single
claimed: e
A drug with high clearance rate indicates:
a) It has high therapeutic index.
b) It has low efficacy.
c) It has long half-life.
d) It has high efficacy.
e) It should be administered more frequently.

### PHARM-P-468
tier: claimed
form: mcq
type: single
claimed: a
The duration of drug action depends on all of the following, 
EXCEPT:
a) Drug potency.
b) Drug bioavailability
c) Renal clearance of the drug.
d) Drug dose.
e) Rate of drug metabolism.

### PHARM-P-469
tier: claimed
form: mcq
type: single
claimed: a
Which of the following conditions will increase drug absorption 
from the intestines?
a) Increased blood flow to the intestines.
b) Decrease the dose of the administered drug.
c) Patients who already suffer from diarrhea.
d) All of the listed may increase the absorption.
e) Partial surgical removal of the small intestine.

### PHARM-P-470
tier: claimed
form: mcq
type: single
claimed: d
Parenteral routes of drug administration includes
a) IM & IV only
b) IM , IV & IA only
c) SC
d) SC , IM , IV & IA
e) SC , IM & IV

### PHARM-P-471
tier: claimed
form: mcq
type: single
claimed: b
What is the estimated blood concentration for ciprofloxacin if 
500mg of it was given by oral route , bioavailability is 40% and 
volume of distribution is 20 L
a) 25mg/L
b) 10mg/L
c) 100mg/L
d) 250mg/L
e) 100g/L

### PHARM-P-472
tier: claimed
form: mcq
type: single
claimed: a
If 87.5% of a drug is eliminated via 1st order kinetics in 15 
hours , then the t1/2 is
a) 5 hours
b) 10 hours
c) 15 hours
d) 30 hours
e) greater than 30 years

### PHARM-P-473
tier: claimed
form: mcq
type: single
claimed: a
In the previous question , the expected time for Css is
a) 1 day
b) 2 day
c) 3 days
d) 5 days
e) one week

### PHARM-P-474
tier: claimed
form: mcq
type: single
claimed: c
The oral route of drug administration tend to be associated with 
all of the following except
a) poor compliance
b) relative safety
c) rapid response
d) convenience

### PHARM-P-475
tier: claimed
form: mcq
type: single
claimed: b
Pharmacokinetics is:
a) The study of biological and therapeutic effects of drugs
b) The study of absorption, distribution, metabolism and excretion of 
drugs
c) The study of mechanisms of drug action
d) The study of methods of new drug development

### PHARM-P-476
tier: claimed
form: mcq
type: single
claimed: b
What does “pharmacokinetics” include
a) Complications of drug therapy
b) Drug biotransformation in the organism
c) Influence of drugs on metabolism processes
d) Influence of drugs on genes

### PHARM-P-477
tier: claimed
form: mcq
type: single
claimed: d
What does “pharmacokinetics” include?
a) Pharmacological effects of drugs
b) Unwanted effects of drugs
c) Chemical structure of a medicinal agent
d) Distribution of drugs in the organism

### PHARM-P-478
tier: claimed
form: mcq
type: single
claimed: d
The intensity (magnitude) and direction of drug action correlate 
in a predictable by way the:
a) Lipid/water partition coefficient (LWPC) of the drug.
b) Potency of the drug.
c) Molecular weight of the drug.
d) Administered dose of the drug.
e) Efficacy of the drug.

### PHARM-P-479
tier: claimed
form: mcq
type: single
claimed: b
What is characteristic of the intramuscular route of drug 
administration?
a) Only water solutions can be injected
b) Oily solutions can be injected
c) Opportunity of hypertonic solution injections
d) The action develops slower, than at oral administration

### PHARM-P-480
tier: claimed
form: mcq
type: single
claimed: b
Intravenous injections are more suitable for oily solutions:
a) True
b) False

### PHARM-P-481
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is a common similarity between 
sublingual route of administration, and oral route of 
administration?
a) Speediness in response.
b) Quickness in absorption.
c) All of the listed are commonality between them.
d) Cheapness.
e) Susceptibility to first-pass effect.
