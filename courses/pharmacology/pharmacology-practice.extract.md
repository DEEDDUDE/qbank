---
course: pharmacology
tab: practice
questions: 174
tiers: open 99 | claimed 75
forms: mcq 145 | qa 29
needs-eye: 0
disputed: 0
next-id: PHARM-P-175
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
