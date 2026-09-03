---
course: public-health
tab: finals
questions: 107
tiers: claimed 89 | open 18
forms: mcq 107
needs-eye: 0
disputed: 2
next-id: PH-F-108
---

<!-- batch 01 -- raw/finals/2023/نموذج 5.pdf, all 50 pages (Q1-Q50), 100% vision
  (no text layer, per prep.py's manifest.json for this batch). First extraction for
  this tab -- PH-F- IDs start at 001. RUN-PLAN row 16.

  This is one model (نموذج 5, "model 5") of the public-health course's 2023-2024
  final exam, the longest single model captured of a reshuffled-models sitting. Per
  the exception in job-a-extract.md ("reshuffled models of one exam"), every entry
  here carries `models: [5]` so later sessions (RUN-PLAN rows 17-18, نموذج 1/3/4) can
  merge into these IDs by stem match rather than re-minting new ones. نموذج 2 of this
  exam was never captured by any student and will never exist -- not a gap in this
  session's coverage. Nothing in this batch was matched or merged against anything
  outside these 50 pages; that cross-model merge is explicitly rows 17-18's job, not
  this one's.

  Straightforward capture, single continuous Moodle attempt, Q1 through Q50 with no
  numbering gaps and no question split across a page boundary that required
  stitching. Q1-Q30 are entirely "Not yet answered" (tier open). Starting at Q31 the
  same attempt shows "Answer saved" with one filled radio each straight through Q50,
  with a single exception: **Q39 reverts to "Not yet answered"** mid-stream (its
  radio column is empty, badge unambiguous) -- read as a real state, not a capture
  artifact, since every neighboring question above and below it clearly shows the
  opposite state on the same photographed page. No official tier anywhere in this
  batch -- no "The correct answer is:" line or printed key on any page, consistent
  with this course's other tabs (quizzes, midterm, practice all independently noted
  zero official tier). Net: 31 open (Q1-30, Q39), 19 claimed (Q31-38, Q40-50).

  All 50 questions are plain stem+options `mcq`, `type: single` -- no checkboxes, no
  "correct answers are" (plural) language, no matching/EMQ blocks, no qa/fact-shaped
  items. None depend on a photo, chart, or diagram -- every question is pure text, so
  no crops were needed in `flagged/`.

  One source anomaly worth flagging rather than silently normalizing: **Q5's four
  options are textually identical** ("The infant mortality rate was reported in 2021
  as ...... live births." / a-d all read "9.6/1000"). Re-read directly off the page
  at full resolution to rule out a downscale/vision misread -- confirmed genuine,
  all four options really do print the same text in the source. Transcribed exactly
  as printed, nothing invented or corrected; the question was never answered anyway
  (tier open), so this doesn't create an answer conflict, just a structurally odd
  item for Job C to note if it ever gets there via a claim from a later model.

  Anti-loss checks: number continuity 1-50 confirmed unbroken across all 8
  read-batches (p1-8, p9-16, p17-24, p25-32, p33-40, p41-48, p49-50). Count
  reconciliation: each batch's visible question count matched the number
  transcribed (8, 8, 8, 8, 8, 8, 8, 2 = 50). Structural floor: all 50 are `mcq`
  with >=4 options, none malformed. Language check: all stems/options are English;
  the only Arabic in the source is the "نموذج 5" filename/course-folder label
  itself, never inside a stem or option. Computed header counts: questions/tiers/
  forms/needs-eye/disputed all derived by counting the body below, matching this
  file's own totals. **Not yet run through Job C or D.** -->

<!-- batch 02 -- raw/finals/2023/نموذج 1.pdf (25 pages) + نموذج 4.pdf (23 pages),
  both 100% vision (no text layer). RUN-PLAN row 17. Merges both models into the
  50 existing PH-F- entries by stem match (per job-a-extract.md's "reshuffled
  models of one exam" exception) and mints new IDs PH-F-051 through PH-F-107 for
  questions that never appeared in نموذج 5. نموذج 1 and نموذج 4 were also
  cross-matched against each other, not just against the existing 50.

  نموذج 1: a clean, full-width Moodle capture, straightforward single continuous
  attempt, Q1 through Q50 read in strict page order with no gaps and no question
  split across a page boundary. Every one of its 50 questions shows "Answer saved"
  with a filled radio -- unlike نموذج 5, this attempt has no "Not yet answered"
  questions at all. 14 of its 50 questions matched existing PH-F-001-050 entries
  by stem (all 14 agreed with نموذج 5's existing claim where one existed, or
  supplied the first claim where the entry was still tier `open`); the other 36
  were genuinely new stems and were minted PH-F-051 through PH-F-086, in the
  order encountered (Q1, Q3, Q4, Q5, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17,
  Q18, Q19, Q21, Q23, Q24, Q27, Q28, Q29, Q30, Q32, Q33, Q35, Q36, Q37, Q38, Q41,
  Q43, Q44, Q45, Q46, Q47, Q49, Q50).

  نموذج 4: a Moodle export whose page order does **not** follow question-number
  order -- e.g. Question 1 is printed on page 3, after Q3-Q6 on pages 1-2, and
  Q19/Q20 appear on page 8 while Q15-Q18 don't show up until pages 9-10. All 23
  pages were read in full regardless of this scrambling, and the 43 question
  numbers that did surface (Q1, Q3-Q43) were then sorted by number for the
  continuity check. **Q2 never appeared on any of the 23 pages** -- confirmed by
  reading every page of this model and finding no second question anywhere; this
  reads as a genuine capture gap in the student's export (a page that was never
  screenshotted/printed), not a reading failure on this session's part, since the
  rest of the sequence (1, 3-43) is unbroken and every other page was legible.
  Recorded here rather than silently absorbed. Pages p018 and p021 were flagged
  `below_floor: true` in prep.py's manifest -- both were read at extra care and
  found fully legible (Q37/Q38 and Q39/Q40 respectively; the below-floor pages
  render with red/orange countdown-timer styling near the end of the attempt, not
  a resolution problem), so neither needed `needs-eye` or a flagged/ crop.
  Of نموذج 4's 42 present questions: 9 matched existing PH-F-001-050 entries
  directly (2 of those, Q7->023 and Q13->046, were triple-matches also hit by
  نموذج 1), 12 matched newly-minted نموذج-1 stems (extending those entries'
  `models:` instead of re-minting), and 21 were new to both models and were
  minted PH-F-087 through PH-F-107 in the order encountered (Q3, Q4, Q5, Q6, Q8,
  Q9, Q15, Q16, Q18, Q25, Q26, Q27, Q28, Q30, Q31, Q32, Q34, Q35, Q39, Q40, Q43).

  No question in either model depends on a photo, chart, or diagram -- all 92
  read questions (50 + 42, ignoring نموذج 4's missing Q2) are pure text `mcq`,
  `type: single`. No crops were saved to flagged/.

  Two genuine disputes surfaced, both between نموذج 1 and نموذج 4 on questions
  neither model shares with نموذج 5 (so neither is a fifth-vote situation --
  it's a straight 1-vs-1 disagreement, no official tier available to break it):
  **PH-F-053** ("The number of deaths per one thousand people per year means:")
  -- model 1 selects "Death rate", model 4 selects "Infant mortality rate".
  **PH-F-066** ("...normally co-ordinated by?", re: actions to reduce ill-health
  exposure) -- model 1 selects "Government", model 4 selects "National Health
  Service". Both recorded as `disputed: true` with per-model `claims:`.

  A cluster of near-duplicate-but-distinct stems is worth flagging for future
  sessions even though none of them merge under the stem-match rule (different
  wording is a different question, not the same one reshuffled): the
  equity/inequity/disparity definition family now spans PH-F-020, PH-F-059
  (ex-نموذج-1 Q13), PH-F-090 (ex-نموذج-4 Q6), and PH-F-093 (ex-نموذج-4 Q15) --
  each asks about a different one of these closely related terms. The
  prevention-tier family spans PH-F-001 (secondary), PH-F-002 and PH-F-056
  (primordial), and PH-F-091 (tertiary, ex-نموذج-4 Q8) -- all distinct stems,
  same conceptual ladder. The Palestine-demographic-statistic family (life
  expectancy PH-F-039, crude birth rate PH-F-080, crude death rate PH-F-085,
  West Bank population PH-F-105) likewise share a pattern (a specific 2021/2022
  national statistic with four numeric distractors) without sharing a stem.
  Relative-risk-vs-odds-ratio "<1 suggests" is another such pair: PH-F-050 (odds
  ratio) and PH-F-095 (relative risk, ex-نموذج-4 Q18) ask the parallel question
  about two different metrics and were kept as separate entries.

  Anti-loss checks: number continuity confirmed unbroken 1-50 for نموذج 1 across
  all 4 read-batches (p1-7, p8-14, p15-21, p22-25); نموذج 4's continuity is
  1, 3-43 as documented above (the Q2 gap is a source anomaly, not a drop -- all
  23 pages were read and accounted for). Count reconciliation: each batch's
  visible question count matched the number transcribed for both models.
  Structural floor: all entries are `mcq` with >=4 options (one has 5), none
  malformed. Language check: all stems/options are English; the only Arabic
  anywhere is the نموذج filename label itself. Computed header counts:
  questions/tiers/forms/needs-eye/disputed all recomputed from the full body
  below (50 original + 57 new = 107), matching this file's own totals.
  **Not yet run through Job C or D.** -->

### PH-F-001
tier: open
form: mcq
type: single
models: [5]
What is the primary focus of secondary prevention in healthcare?
a) Preventing the occurrence of disease
b) Rehabilitating individuals after illness
c) Promoting healthy behaviors
d) Minimizing the impact of a disease in its early stages

### PH-F-002
tier: open
form: mcq
type: single
models: [5]
What is a key strategy in primordial prevention?
a) Early diagnosis and treatment
b) Individual Health education and promotion
c) Addressing social determinants of health
d) Vaccination campaigns

### PH-F-003
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 5]
What does positive predictive value (PPV) represent in the context of a medical test?
a) The likelihood of obtaining a true positive result
b) The probability that a positive test result is truly positive
c) The precision in diagnosing rare conditions
d) The ability to minimize false positives.

### PH-F-004
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 5]
We examined the relationship between television viewing and initiation of smoking and found a strong relationship between both variables. What does this mean
a) Dose-response relationship
b) Consistency
c) Strength of association
d) Plausibility

### PH-F-005
tier: open
form: mcq
type: single
models: [5]
note: All four options print identically in the source ("9.6/1000") -- confirmed at full resolution, not a read error. Transcribed verbatim.
The infant mortality rate was reported in 2021 as ...... live births.
a) 9.6/1000
b) 9.6/1000
c) 9.6/1000
d) 9.6/1000

### PH-F-006
tier: open
form: mcq
type: single
models: [5]
What is the term for an epidemic that has spread across a large geographic area and affects multiple countries or continents?
a) Pandemic
b) Outbreak
c) Epidemic
d) Endemic

### PH-F-007
tier: open
form: mcq
type: single
models: [5]
A health system is defined by
a) A health system is the combined activities of all resources, actors, and institutions related to the financing, regulation, and provision of all activities whose primary intent is to improve or maintain health
b) A health system is the combined strategies of all resources, actors, and institutions related to the financing, regulation, and provision of all activities whose primary intent is to improve or maintain health
c) A health system is the combined entity of all resources, actors, and institutions related to the financing, regulation, and provision of all activities whose primary intent is to improve or maintain health
d) All of the answers are true

### PH-F-008
tier: open
form: mcq
type: single
models: [5]
What is the disadvantage of case-control studies?
a) Provides direct evidence of causation
b) Allows for the calculation of incidence rates
c) Suitable for studying rare exposures
d) Vulnerable to cases and control selection bias

### PH-F-009
tier: open
form: mcq
type: single
models: [5]
Health literacy is best defined as the capacity of a person to:
a) Read health-related literature
b) Access the internet
c) Recognize and know how to find information about a health problem
d) Follow medical instructions for specific healthcare problems

### PH-F-010
tier: open
form: mcq
type: single
models: [5]
What is the role of secondary prevention in the natural history of a disease?
a) Secondary prevention focuses on preventing the occurrence of diseases.
b) Secondary prevention is unrelated to the natural history of diseases.
c) Secondary prevention primarily deals with rehabilitation after illness.
d) Secondary prevention aims to identify diseases in their early stages.

### PH-F-011
tier: open
form: mcq
type: single
models: [5]
One of the following is not a health determinant
a) The impact of the natural environment
b) Health insurance regulations in the country
c) Behavioral factors.
d) Genetic determinants.

### PH-F-012
tier: open
form: mcq
type: single
models: [5]
Which descriptive study design is most suitable for investigating the prevalence of a specific condition in a population at a particular point in time?
a) Longitudinal study
b) Cross-sectional study
c) Case-control study
d) Experimental study

### PH-F-013
tier: claimed
form: mcq
type: single
claimed: d
models: [4, 5]
The Germ Theory is one of the
a) 18th-century theories
b) 19th-century theories
c) 21st-century theories
d) 20th-century theories

### PH-F-014
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 5]
Which term is used to describe the principle that the cause should consistently precede the effect?
a) Temporal relationship
b) Consistency
c) Specificity
d) Coincidence

### PH-F-015
tier: claimed
form: mcq
type: single
claimed: d
models: [4, 5]
In a case-control study, the odds ratio is used to:
a) Estimate the prevalence of the disease
b) Assess the incidence rate of the outcome
c) Measure the strength of the association between exposure and outcome
d) Calculate the absolute risk reduction

### PH-F-016
tier: open
form: mcq
type: single
models: [5]
What aspect of a screening test does reliability primarily assess?
a) The ability to minimize false negatives.
b) The ability to identify individuals at high risk
c) The precision in diagnosing advanced stages of a disease
d) The consistency and stability of test results over time

### PH-F-017
tier: open
form: mcq
type: single
models: [5]
What factor is primarily responsible for the shift from high mortality rates due to infectious diseases to low mortality rates from chronic diseases in the epidemiological transition?
a) Advances in medical technology and healthcare
b) Decreased urbanization
c) Increased population density
d) Climate change

### PH-F-018
tier: claimed
form: mcq
type: single
claimed: c
models: [4, 5]
Primary health care strategy towards Changes in the Health care system includes:
a) Use and control of resources, Redistribution of existing resources, and Reorientation of Health manpower to PHC
b) Total coverage with essential health care, Integrated system, and Involvement of communities
c) All are correct
d) Legislative changes, and Design, planning, and management of health system

### PH-F-019
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 5]
Primary health care (PHC) became a core policy for the World Health Organization with:
a) In 1948 the WHO resolution, including the social health dimension
b) The Alma-Ata Declaration in 1978 and the 'Health-for-All by the Year 2000' Program.
c) None of the choices
d) In 1986 by Ottawa Charter for Health Promotion
e) At the Adelaide Healthy Public Policy and Supportive Environments meeting

### PH-F-020
tier: open
form: mcq
type: single
models: [5]
Avoidable differences in the incidence and prevalence of health conditions and health status between groups is the definition of
a) Health Inequities
b) None of the answers is true
c) Health Inequality
d) Health Disparities

### PH-F-021
tier: open
form: mcq
type: single
models: [5]
During which stage of the demographic transition model does a country typically experience rapid population growth?
a) Stage 2
b) Stage 3
c) Stage 1
d) Stage 4

### PH-F-022
tier: open
form: mcq
type: single
models: [5]
One of the following, is not one of the Modern Public Health Ten Great Achievements in Public Health, 1900-1999
a) Motor-vehicle safety.
b) Safer workplaces.
c) Vaccination.
d) Development of Modern MRI for disease diagnosis

### PH-F-023
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4, 5]
Health indicators:
a) are used to measure the health status of the community.
b) All are incorrect
c) they are indirect parameters or variables that assess the state of the health of the community.
d) All are correct
e) They are defined as parameters that can measure changes in the level of health.

### PH-F-024
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 5]
This approach to health promotion is synonymous with health education as it aims to increase individuals' knowledge about the causes of health and illness.
a) none of these
b) biomedical approach
c) community development approach
d) behaviour change approach

### PH-F-025
tier: open
form: mcq
type: single
models: [5]
Any diseases for which an official report is required either nationally or internationally is called:
a) Contagious disease.
b) Communicable disease.
c) Surveillance of disease.
d) Notifiable disease.
e) Infectious disease.

### PH-F-026
tier: claimed
form: mcq
type: single
claimed: a
models: [4, 5]
What role does food insecurity play in the prevalence of chronic diseases?
a) Increases the risk of chronic diseases
b) Has no impact on chronic disease prevalence
c) Decreases the risk of chronic diseases
d) Promotes overall health and well-being

### PH-F-027
tier: claimed
form: mcq
type: single
claimed: b
models: [4, 5]
Which of the following is considered to be a public health achievement during the twentieth century?
a) Antibiotics
b) All are correct
c) Vaccination
d) Maternal and infant care

### PH-F-028
tier: open
form: mcq
type: single
models: [5]
Health Promotion Action means EXCEPT:
a) Building Healthy Public Policy
b) Strengthen community action
c) Develop highly specialized medical services
d) Reorient health services
e) Create supportive environments

### PH-F-029
tier: open
form: mcq
type: single
models: [5]
A prevalence rate is:
a) The total number of cases of a disease existing in a population divided by the total population.
b) The number of new cases of a disease is divided by the number of all cases of a disease.
c) None of the above.
d) The number of new cases of a disease is divided by the number of persons at risk for the disease.

### PH-F-030
tier: claimed
form: mcq
type: single
claimed: c
models: [4, 5]
In a study to evaluate the association between tobacco smoking and lung cancer, it was found that PAR equals 30%. What does the value "30%" PAR represent in this context?
a) The prevalence of smoking in the population
b) The total number of lung cancer cases in the population
c) The proportion of lung cancer cases that can be attributed to smoking
d) The odds of developing lung cancer in smokers

### PH-F-031
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
Primary health care is:
a) Care is provided in hospices.
b) The first point of contact for people with the health care services.
c) Care is provided in the acute setting.
d) Care is provided by GPs only.

### PH-F-032
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 5]
The following ARE indirect mechanisms of transmission of communicable diseases, EXCEPT:
a) Vector-borne
b) Vehicle borne
c) Air-borne
d) Skin touch

### PH-F-033
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
Which group of determinants is often characterized by broader, societal factors that influence health outcomes at a population level?
a) Genetic determinants
b) Distal determinants
c) Environmental determinants
d) Proximal determinants

### PH-F-034
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 5]
The denominator of the Maternal mortality rate is:
a) Total term deliveries
b) Total pregnant females
c) Midyear population
d) Live births

### PH-F-035
tier: claimed
form: mcq
type: single
claimed: a
models: [5]
Which of the following statements about exposures is true?
a) 'Exposure' refers to contact with some factor that may be harmful or beneficial to health.
b) High body mass index is a risk factor for a range of health conditions, therefore, it cannot be treated as a single exposure.
c) Dietary intake is not an 'exposure' because individuals make a choice about what they eat.
d) An exposed individual has a greater risk of disease.

### PH-F-036
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
Which of the following are the major determinants of the health of individuals
a) Community organization, Environment, Socio-demographic, culture
b) Human biology, Socio-demographic, Behavioural, Physical
c) Human biology, Environment, Lifestyle behavior, Health care organization
d) Human biology, culture, Behavioral, Health care organization

### PH-F-037
tier: claimed
form: mcq
type: single
claimed: d
models: [5]
Which factor emphasizes the strength of association in causation assessment?
a) Consistency
b) Specificity
c) Coherence
d) Magnitude of effect

### PH-F-038
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 5]
Collective behavior which explains that the crowd can cause a hypnotic impact on individuals represents the:
a) The Contagion theory
b) Miasma theory
c) The germ theory
d) The supernatural theory

### PH-F-039
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 5]
note: In model 5 this sits amid an otherwise "Answer saved" run (Q31-38, Q40-50) but its own badge clearly read "Not yet answered" with an empty radio column -- read as a real state, not a capture artifact. Model 1 answers it (claimed a), which is why tier is now claimed.
Life expectancy in Palestine is reported in 2021 as
a) 74.2
b) 78.1
c) 66.3
d) 80.5

### PH-F-040
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
When epidemiologists judge the evidence to establish possible causes of a health outcome, they consider EXCEPT
a) The estimated strength of the association between an exposure and the outcome.
b) Evidence shows that an increase in the exposure level will reverse the risk of the outcome.
c) Evidence shows that reductions in the exposure level will reverse the risk of the outcome.
d) Evidence that the exposure of interest has appeared before the outcome.

### PH-F-041
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 5]
Which of the following can't be considered as unacceptable?
a) Smoking
b) Living in a stressful living condition
c) Sedentary lifestyle
d) Having a family history of diabetes

### PH-F-042
tier: claimed
form: mcq
type: single
claimed: a
models: [5]
What distinguishes opportunistic screening in healthcare?
a) It occurs during routine medical visits for unrelated reasons
b) It follows a systematic and scheduled approach
c) It targets individuals with known risk factors
d) It is exclusively performed in specialized clinics.

### PH-F-043
tier: claimed
form: mcq
type: single
claimed: a
models: [5]
Which of the following study designs is considered at the top of the hierarchy in terms of providing strong evidence for causation?
a) Randomized controlled trial
b) Cohort study
c) Cross-sectional study
d) Case-control study

### PH-F-044
tier: claimed
form: mcq
type: single
claimed: a
models: [5]
One of the following is not from the three strategies to influence the determinants of behavior
a) Coercive
b) Automatic protective strategies
c) Education
d) Research-based strategies

### PH-F-045
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
Communicable diseases control strategies include:
a) Prevent recurrence
b) All are correct
c) Identify the cause (diagnosis), and Treatment of cases
d) Analysis and reporting

### PH-F-046
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4, 5]
How does food insecurity influence healthcare utilization?
a) Has no impact on healthcare utilization
b) Enhances preventive care practices
c) Decreases the need for healthcare services
d) Increases the reliance on healthcare services

### PH-F-047
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 5]
What does the odds ratio (OR) measure in epidemiology?
a) The ratio of the odds of an outcome in the exposed group to the odds in the unexposed group
b) The risk of developing a disease
c) The prevalence of a disease in a population
d) The proportion of cases with the exposure

### PH-F-048
tier: claimed
form: mcq
type: single
claimed: a
models: [5]
What does Population Attributable Risk (PAR) represent in epidemiology?
a) The proportion of cases that can be attributed to a specific exposure in a population
b) The total number of cases in a population
c) The prevalence of a disease in a specific demographic group
d) The odds of developing a disease in the exposed group

### PH-F-049
tier: claimed
form: mcq
type: single
claimed: d
models: [4, 5]
What is the primary goal of descriptive epidemiology?
a) To develop new treatments for diseases.
b) To identify the causes of diseases.
c) To conduct randomized controlled trials.
d) To summarize and characterize health-related events in populations.

### PH-F-050
tier: claimed
form: mcq
type: single
claimed: b
models: [5]
In the context of odds ratio, what does a value less than 1 suggest?
a) An increased odds of the outcome in the exposed group
b) A protective effect of the exposure
c) The study is biased
d) No association between the exposure and outcome

### PH-F-051
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4]
What is the main characteristic of selective or targeted screening in public health?
a) It aims to identify individuals with specific risk factors
b) It is primarily used for diagnostic purposes.
c) It focuses only on symptomatic individuals
d) It involves screening the entire population

### PH-F-052
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
Which of the following is a characteristic of cross-sectional research?
a) Snapshot of a population at a single point in time
b) Manipulation of variables to observe their effects
c) Data collected at multiple time points
d) Focus on changes and developments over time

### PH-F-053
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: model 1
    answer: d
  - source: model 4
    answer: c
models: [1, 4]
The number of deaths per one thousand people per year means:
a) Birth rate
b) Child mortality rate
c) Infant mortality rate
d) Death rate

### PH-F-054
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 4]
What is a potential negative health consequence of increased global marketing and consumption of processed foods?
a) Decreased obesity rates
b) Enhanced overall well-being
c) Increased risk of non-communicable diseases
d) Improved nutritional status

### PH-F-055
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
note: Options b and d print identically ("Medical factors that influence the health outcomes") -- confirmed at full resolution, not a read error. Transcribed verbatim.
Social determinants of health (SDH) are the
a) non-medical factors that influence health outcomes.
b) Medical factors that influence the health outcomes
c) All of the answers are true
d) Medical factors that influence the health outcomes

### PH-F-056
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 4]
What is the primary goal of primordial prevention?
a) To prevent the progression of diseases
b) To rehabilitate individuals with existing health conditions
c) To address the root causes of risk factors in populations
d) To promote early detection and treatment

### PH-F-057
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
What is the best way to prevent the spread of infection?
a) Use personal protective equipment
b) Wash your hands
c) Use alcohol wipes to clean surfaces
d) Avoid contact with ill patients

### PH-F-058
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
Which organization is crucial in the monitoring and advising of global health issues?
a) United Nations
b) World Health Organization
c) Central of disease control
d) North Atlantic Treaty Organization

### PH-F-059
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
Systematic and unjust distribution of social, economic, and environmental conditions needed for health as a definition of
a) Health Disparities
b) None of the answers is true
c) Health Inequality
d) Health Inequities

### PH-F-060
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
Additional elements incorporated into PHC, after Alma-Ata are, EXCEPT:
a) Oral Health
b) Occupational health
c) Mental Health
d) COVID 19

### PH-F-061
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
What is the primary purpose of screening in public health?
a) To replace diagnostic tests
b) To provide treatment for diagnosed conditions.
c) To identify individuals with no risk factors
d) To detect early signs of diseases before symptoms appear

### PH-F-062
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4]
Which of the following is a description of 'descriptive epidemiology'?
a) Examining the incidence of disease in relation to person, place, and time
b) Intervention to change exposure to the factor being studied
c) Identifying the associations between disease and causes
d) Actions to reduce exposure to factors which impact on health

### PH-F-063
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
the Sustainable Development Goals for Health include the following EXCEPT:
a) Better Access to Reproductive and Sexual Healthcare
b) Health coverage, Reduce the Risk of Contamination
c) Promoting healthy lifestyles
d) Tobacco Control, Research and Development

### PH-F-064
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
All the following are true about the prevention and control of Non- communicable Diseases (NCDs) EXCEPT:
a) Establish and strengthen national policies and plans
b) Implement programs that are focused on hospitals
c) Assess and monitor the burden of NCDs and their determinants
d) Establish a high-quality surveillance and monitoring system

### PH-F-065
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
Socioeconomic status and education level of an individual are examples of:
a) Proximal determinants
b) Distal determinants
c) Environmental determinants
d) Genetic determinants

### PH-F-066
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: model 1
    answer: d
  - source: model 4
    answer: a
models: [1, 4]
'Actions to reduce exposure to factors which can impact on the development of ill-health' in terms of public health and epidemiology are normally co-ordinated by?
a) National Health Service
b) Health protection
c) General practitioners
d) Government

### PH-F-067
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 4]
Which of the following is an example of a primary prevention strategy?
a) Providing physical therapy after surgery
b) Administering antibiotics to treat an infection
c) Vaccinating against infectious diseases
d) Prescribing pain medication for chronic pain

### PH-F-068
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
This approach to health promotion is based on the assumption that humans are rational decision-makers, this approach relies heavily upon the provision of information about the risks and benefits of certain behaviours.
a) behaviour change approach
b) biomedical approach
c) none of these
d) community development approach

### PH-F-069
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
In an observational study, what is the primary goal of the researcher?
a) To establish cause-and-effect relationships.
b) To control for confounding variables
c) To manipulate variables and observe their effects
d) To describe and understand natural phenomena

### PH-F-070
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
Which of the following is a limitation of prevalence studies?
a) Requires a long duration of follow-up
b) Cannot establish cause-and-effect relationships
c) Minimizes recall bias
d) Provides information on the temporal sequence of events

### PH-F-071
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4]
How is the odds ratio calculated?
a) (Odds in exposed group) / (Odds in unexposed group)
b) (Number of cases in exposed group) / (Total number in exposed group)
c) (Risk in exposed group) / (Risk in unexposed group)
d) (Number of cases in unexposed group) / (Total number in unexposed group)

### PH-F-072
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
Web of disease causation is another name given to the
a) The Environmental Theory
b) The Life Style Theory
c) The Multi Causal Theory
d) The Germ Theory

### PH-F-073
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
In which stage of the demographic transition model do birth rates remain high while death rates decline significantly?
a) Stage 3
b) Stage 2
c) Stage 1
d) Stage 4

### PH-F-074
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4]
The following are all characteristics of the prevalence of a disease except one, which one?
a) It can be used to help determine the healthcare needs of a community
b) It includes all of the existing cases of disease in a community
c) It depends on the incidence of the disease
d) It is always measured over time
e) It depends on the duration of the disease process

### PH-F-075
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
CDC is an abbreviation of one of the following:
a) Centers for Disease Control and Prevention
b) Class of Disease Control
c) Center for Disease Correction
d) Consortium of Disease Control

### PH-F-076
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4]
What does the term "consistency" in causation assessment focus on?
a) Consistency in research methodology
b) Geographic concentration of cases
c) Singular outcome caused by multiple factors
d) Diverse outcomes resulting from a single cause

### PH-F-077
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4]
One of the following is not a social determinant of health
a) Family history of chronic diseases
b) Income and social protection
c) Working life conditions
d) Education

### PH-F-078
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
What is the primary aim of disease control in public health?
a) Reducing the incidence, pathological impact, and financial burden of the disease
b) Minimizing the impact of a disease in its early stages
c) Early detection of diseases
d) Achieving and maintaining optimal management of symptoms and disease progression

### PH-F-079
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
Among the leading causes of death, between 1990 to 2000, ischemic heart diseases
a) Stayed the 1st leading causes
b) Was not on the list from the beginning
c) Decreased to the 2nd cause
d) Decreased to the 3rd cause

### PH-F-080
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
The crude birth Rate in Palestine as reported in 2021 was
a) 28.1/1000 population
b) 33.2/1000 population
c) 21.4/1000 population
d) 23.4/1000 population.

### PH-F-081
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
What is the major advantage of a case-control study design?
a) Allows for the calculation of relative risk
b) Provides information on the temporal sequence of events
c) Suitable for rare diseases or outcomes
d) Minimizes recall bias

### PH-F-082
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
Appropriateness as one of the Basic Requirements for Sound PHC means:
a) The service has to be properly selected and carried out by trained personnel in the proper way.
b) Sufficient volume of care to meet the needs and demands of a community
c) The cost should be within the means and resources of the individual and the country.
d) care can be obtained whenever people need it.

### PH-F-083
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
What is a potential consequence of food insecurity on mental health?
a) Enhanced emotional well-being
b) Increased stress and mental health disorders
c) Improved cognitive function
d) Reduced risk of anxiety and depression

### PH-F-084
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
A process by which people gain control and mastery over their own lives.
a) Sustainability
b) Equity
c) Intersectoral
d) Empowerment

### PH-F-085
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4]
The Crude Death rate in Palestine as reported in 2021 was
a) 2.3 per 1,000 population.
b) 5.3 per 1,000 population.
c) 5.6 per 1,000 population.
d) 3.5 per 1,000 population.

### PH-F-086
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
Why is the concept of relative risk important in epidemiology?
a) It is only relevant in experimental studies
b) It quantifies the strength of association between exposure and outcome
c) It helps calculate odds ratios
d) It measures the prevalence of diseases

### PH-F-087
tier: claimed
form: mcq
type: single
claimed: b
models: [4]
The declaration of health as a human right was declared at
a) Kazakhstan 1982
b) Alam Ata 1978
c) United natation 2015
d) WHO 1986

### PH-F-088
tier: claimed
form: mcq
type: single
claimed: a
models: [4]
The Old definition of Health: From a professional point of view
a) Health was defined as a measure of the state of the physical bodily organs, and the ability of the body as a whole to function
b) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science.
c) A complete state of physical, mental and social wellbeing and not merely the absence of disease
d) Ensuring the health of the individual by maintaining and improving the health of the community.

### PH-F-089
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
What is the primary objective of a program trial?
a) To investigate the incidence of new cases in a population
b) To establish the prevalence of a health condition
c) To assess the effectiveness of a specific intervention or program
d) To measure the duration of a disease in affected individuals

### PH-F-090
tier: claimed
form: mcq
type: single
claimed: b
models: [4]
Defined as the absence of unfair and avoidable or remediable differences in health among population groups defined socially, economically, demographically, or geographically. This defines
a) all the answers are true
b) health equity
c) health inequity
d) health disparity

### PH-F-091
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
What is the primary goal of tertiary prevention in healthcare?
a) Identifying diseases in their early stages
b) Preventing the occurrence of diseases
c) Minimizing the impact of a disease in its early stages
d) Rehabilitating individuals after illness

### PH-F-092
tier: claimed
form: mcq
type: single
claimed: b
models: [4]
The influenza pandemic occurs after every 7 - 10 years. This kind of disease distribution in time is known as:
a) Secular trend
b) Cyclical trend
c) Seasonal trend E. Endemicity
d) Short time fluctuation,

### PH-F-093
tier: claimed
form: mcq
type: single
claimed: b
models: [4]
The word inequity refers to
a) None of the answers is true
b) differences that are unnecessary and avoidable but, in addition, are also considered unfair and unjust.
c) It refers to differences that are necessary and unavoidable but, in addition, are also considered fair and just.
d) It refers to similarities that are unnecessary and avoidable but, in addition, are also considered unfair and unjust.

### PH-F-094
tier: claimed
form: mcq
type: single
claimed: a
models: [4]
WHO Europe office,1984 set a target to reach, as part of enhancing health equities by ------% by the year 2000
a) 25%
b) 30%
c) 20%
d) 10%

### PH-F-095
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
In the context of relative risk, what does a value less than 1 suggest?
a) An increased risk of the outcome in the exposed group
b) No association between the exposure and outcome
c) The study is biased
d) A protective effect of the exposure

### PH-F-096
tier: claimed
form: mcq
type: single
claimed: a
models: [4]
Disease control measures are generally directed at all the following, EXCEPT:
a) Eliminating the host
b) Reducing host susceptibility
c) Eliminating the vector
d) Interrupting mode of transmission

### PH-F-097
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
A public health campaign is being organized to address a rising rate of obesity in a community. The organizers want to empower community members to take charge of their health. What is an empowering approach to engage the community?
a) Developing strategies based solely on expert opinions
b) Conducting informational sessions without seeking community input
c) Collaborating with community members to identify priorities and solutions
d) Implementing top-down directives without community involvement

### PH-F-098
tier: claimed
form: mcq
type: single
claimed: b
models: [4]
All of the following are sources for financing the health system except for one
a) Donations or community health insurance.
b) Extra budgets from other ministries
c) Social Health Insurance.
d) General Taxation.

### PH-F-099
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
What is a key characteristic of a cohort study in analytical research?
a) It compares two or more groups at a specific point in time.
b) It is a retrospective study design.
c) It involves the observation of two or more groups over time.
d) It focuses on the odds of exposure for an outcome.

### PH-F-100
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
This approach to health promotion aims to improve and promote health by addressing socioeconomic and environmental determinants of health within the community.
a) None of these
b) Community development approach
c) Behaviour change approach
d) Biomedical approach

### PH-F-101
tier: claimed
form: mcq
type: single
claimed: a
models: [4]
Epidemiological measures of effect assess the _______ between an exposure and an outcome.
a) Strength of the association.
b) Strength of the causal mechanisms.
c) Strength of a confounding factor
d) Strength of the reversibility.

### PH-F-102
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
Which one is the most cost-beneficial technology in improving community health in developing nations?
a) Oral rehydration solutions
b) Hospitals in all communities with at least 1,000 population
c) Safe water supply
d) One doctor for 500 population E. Control of industrial pollution

### PH-F-103
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
The health status of a defined group of people including the actions and conditions of both private and public sectors to promote, protect and preserve their health IS
a) Individual Health
b) Environmental Health
c) Community Health
d) Clinical Medicine

### PH-F-104
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
Regarding Health Policy Indicators, the most important indicator of political commitment is the allocation of adequate resources with the following relevant indicators, EXCEPT:
a) The proportion of total health resources devoted to primary health care
b) Proportion of GDP spent on health-related activities like water supply and sanitation & housing and nutrition
c) The proportion of GDP spent on health services
d) None is correct

### PH-F-105
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
According to the statistics from Palestine in 2022, the Palestinians in the West Bank were
a) 2,92 million
b) 4.12 million
c) 2.43 million
d) 3.14 million

### PH-F-106
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
In the context of a medical test, what does specificity measure?
a) The ability to minimize false negatives
b) The ability to correctly identify individuals with the disease
c) The precision in diagnosing rare conditions
d) The ability to correctly identify individuals without the disease

### PH-F-107
tier: claimed
form: mcq
type: single
claimed: c
models: [4]
We examined the relationship between television viewing and initiation of smoking and found a strong dose-response relationship with increasing hours. "The association was substantial, with youth who watched >5 hours per day being 5.99 times as likely to initiate smoking than youth who watched 0 to 2 hours per day." This is an example of?
a) Strength of association
b) Plausibility
c) Dose-response relationship
d) Temporal relation
