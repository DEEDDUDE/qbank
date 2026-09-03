---
course: public-health
tab: finals
questions: 229
tiers: claimed 217 | open 12
forms: mcq 197 | qa 32
needs-eye: 0
disputed: 8
next-id: PH-F-230
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

<!-- batch 03 -- raw/finals/2023/نموذج 3.pdf (26 pages), 100% vision (no text layer) +
  raw/finals/2020-2021/1/Public Health final 2020-2021.pdf (20 pages), 100% vision (no
  text layer). RUN-PLAN row 18. Bundles two unrelated exam sittings into one session
  purely to hit a page budget -- kept completely separate, no cross-matching between
  them.

  Part 1 (نموذج 3): a fourth reshuffled model of the SAME 2023-2024 sitting already
  in this file as models 1, 4, 5 (نموذج 2 was never captured and doesn't exist). Its
  26 captured pages are NOT in reading order -- the p001-p026 filenames run in reverse
  relative to the exam's own Q1-Q50 order (p001 shows Q49-50, p026 shows Q1-2), a
  capture-order quirk of this particular screenshot sequence. All 26 pages were read
  regardless of filename order and every question re-sorted by its own printed
  question number for the continuity check; Q1-Q50 confirmed unbroken with no gaps
  (p019 and p020 turned out to be two near-identical captures of the same Q13-15
  region -- no new information, not a duplicate drop). Matched every question by stem
  text (never by number, since models are shuffled) against the existing PH-F-001-107
  pool first: 32 of model 3's 50 questions matched existing entries by stem --
  extending their `models:` list with `3`, and upgrading six previously-`open`
  entries (PH-F-006, 007, 009, 010, 011, 029) to `claimed` since model 3 supplied
  their first-ever claim. The other 18 were genuinely new stems, minted PH-F-108
  through PH-F-125 in the order encountered (Q2, Q6, Q8, Q10, Q13, Q14, Q17, Q18,
  Q20, Q23, Q26, Q27, Q28, Q31, Q37, Q39, Q40, Q46).

  Two new disputes surfaced where model 3's claim disagreed with an existing model's
  claim on content (not just letter -- distractor order is reshuffled per model, so
  matches and disputes were judged by comparing what the selected option *says*, not
  its letter): **PH-F-100** (health-promotion approach addressing socioeconomic/
  environmental determinants) -- model 4 selected "Behaviour change approach", model 3
  selected "Community development approach". **PH-F-104** (Health Policy Indicators,
  EXCEPT) -- model 4 selected "The proportion of GDP spent on health services", model
  3 selected "None is correct". Both recorded `disputed: true` with per-model
  `claims:`, bringing the file's running dispute total to 4. Every other overlapping
  question agreed on content across models despite letter reshuffling (e.g. PH-F-094's
  "25%" is option b in model 3 but option a in model 4 -- same claim, not a dispute).

  Model 3's own Moodle attempt shows "Answer saved" with a filled radio on all 50
  questions -- no "Not yet answered" state anywhere, unlike نموذج 5's earlier mixed
  state. No question in model 3 depends on a photo, chart, or diagram -- all 50 are
  pure text `mcq`, `type: single`; no crops saved to flagged/.

  Part 2 (2020-2021 sitting): a separate exam from a separate academic year, kept
  entirely out of the PH-F-001-107/108-125 stem-matching pool per the task brief --
  no cross-matching attempted or found. Its own new ID range: PH-F-126 through
  PH-F-165, Q1-Q40 in printed order, one straightforward continuous Moodle attempt,
  "Answer saved" with a filled radio on every question, no gaps. Tagged
  `source: 2020-2021 sitting` on every entry (mirrors microbiology finals' `source:
  Exam I` precedent) since this sitting has no reshuffled-model identity of its own.
  A second, Messenger-photo capture of this same 2020-2021 sitting already sits
  un-processed in `.prep/finals/2020-2021/` (the `2_received_*.jpg` files) --
  explicitly out of scope for this session (RUN-PLAN row 19's job) and never opened;
  every entry here was transcribed verbatim off the printed Moodle text specifically
  so that a future stem-match against that second capture will work cleanly.

  Three source anomalies in Part 2, transcribed exactly as printed rather than
  corrected or invented around: **PH-F-158** has two identical options ("Observational
  case-control" printed for both c and d) -- confirmed at full resolution, genuine
  duplicate in the source. **PH-F-160**'s stem states the risk ratio as "0.07" but its
  selected answer (a) describes "0.7 times the risk" -- a decimal-place mismatch
  between stem and answer text, preserved as printed. **PH-F-162**'s stem has its
  exposed-group sample size ("... following ___ smokers ...") covered by an on-screen
  UI overlay (a floating close/"x" icon) baked into the screenshot itself -- not a
  downscale artifact, so no crop of the original could recover it; recorded as
  `[obscured]` rather than guessed, and doesn't affect the answer since the
  interpretation question depends only on the stated risk ratio of 17, not the sample
  size. Four questions in Part 2 (PH-F-136, 141, 146, 157) share one otitis-media
  vignette but each individually asks about "streptococcal sore throat" in its own
  final sentence -- a disease-name mismatch against the vignette printed on every one
  of the four repeats, not a one-off typo; transcribed verbatim on all four rather
  than corrected. No question in Part 2 depends on a photo, chart, or diagram beyond
  the plain-text vignettes above; no crops saved to flagged/.

  Anti-loss checks: number continuity confirmed unbroken 1-50 for model 3 (re-sorted
  by printed question number, independent of the reversed capture-order filenames)
  and 1-40 for the 2020-2021 sitting, checked separately per source per the task
  brief. Count reconciliation: each batch's visible question count matched the number
  transcribed in both parts (50 for model 3 across 26 pages; 40 for 2020-2021 across
  20 pages, 2 questions/page with no overflow). Structural floor: all 90 new/updated
  entries are `mcq` with >=2 options (most 4, several True/False with 2, the four
  vignette vitals-metric questions with 5), none malformed. Language check: all
  stems/options are English; the only non-English text anywhere is the نموذج 3
  filename/course-folder label itself, never inside a stem or option. Computed header
  counts: questions/tiers/forms/needs-eye/disputed all recomputed from the full body
  below (107 existing + 18 new from model 3 + 40 new from 2020-2021 = 165), matching
  this file's own totals. **Not yet run through Job C or D.** -->

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
models: [1, 3, 5]
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
tier: claimed
form: mcq
type: single
claimed: a
models: [3, 5]
What is the term for an epidemic that has spread across a large geographic area and affects multiple countries or continents?
a) Pandemic
b) Outbreak
c) Epidemic
d) Endemic

### PH-F-007
tier: claimed
form: mcq
type: single
claimed: c
models: [3, 5]
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
tier: claimed
form: mcq
type: single
claimed: c
models: [3, 5]
Health literacy is best defined as the capacity of a person to:
a) Read health-related literature
b) Access the internet
c) Recognize and know how to find information about a health problem
d) Follow medical instructions for specific healthcare problems

### PH-F-010
tier: claimed
form: mcq
type: single
claimed: d
models: [3, 5]
What is the role of secondary prevention in the natural history of a disease?
a) Secondary prevention focuses on preventing the occurrence of diseases.
b) Secondary prevention is unrelated to the natural history of diseases.
c) Secondary prevention primarily deals with rehabilitation after illness.
d) Secondary prevention aims to identify diseases in their early stages.

### PH-F-011
tier: claimed
form: mcq
type: single
claimed: b
models: [3, 5]
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
models: [1, 3, 5]
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
models: [3, 4, 5]
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
models: [1, 3, 5]
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
models: [3, 4, 5]
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
tier: claimed
form: mcq
type: single
claimed: c
models: [3, 5]
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
models: [3, 4, 5]
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
models: [1, 3, 5]
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
models: [3, 5]
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
models: [1, 3, 4, 5]
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
models: [1, 3]
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
models: [1, 3]
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
models: [1, 3]
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
models: [1, 3]
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
models: [1, 3, 4]
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
models: [1, 3]
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
models: [1, 3]
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
models: [1, 3]
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
models: [3, 4]
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
models: [3, 4]
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
models: [3, 4]
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
models: [3, 4]
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
disputed: true
claims:
  - source: model 4
    answer: c (Behaviour change approach)
  - source: model 3
    answer: b (Community development approach)
models: [3, 4]
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
models: [3, 4]
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
disputed: true
claims:
  - source: model 4
    answer: c (The proportion of GDP spent on health services)
  - source: model 3
    answer: d (None is correct)
models: [3, 4]
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
models: [3, 4]
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
models: [3, 4]
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

### PH-F-108
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
What does the relative risk (RR) measure in epidemiology?
a) The ratio of the risk of an outcome in the exposed group to the risk in the unexposed group
b) The odds of developing a disease
c) The proportion of cases with exposure
d) The prevalence of a disease in a population

### PH-F-109
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
In which field of epidemiology would you expect to see ecological studies?
a) Descriptive epidemiology
b) Intervention studies
c) Analytical epidemiology
d) Statistical analysis

### PH-F-110
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
Between the public health and the medical model, the medical model health is concerned with all of the following except for one
a) Prevention of the disease
b) Diagnosis of the disease
c) Treatment of the disease
d) Intervention in disease management

### PH-F-111
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
What is the fundamental question that analytical epidemiology aims to answer?
a) "How do exposures relate to disease occurrence?"
b) "Who is affected by the disease?"
c) "What is the basic pattern of the disease?"
d) "What is the disease's geographic distribution?"

### PH-F-112
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
Differentiation between a point-source epidemic and a progressive (propagated) epidemic is made by:
a) Considering the characteristics of the infectious agent
b) Plotting the distribution of cases by time onset
c) Determining the level of immunity in the community
d) Determining the number of persons infected and calculating the attack rate

### PH-F-113
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
What is the primary characteristic of a case-control study?
a) Selection based on outcome status
b) Random assignment of participants
c) Prospective data collection
d) Observation of exposure and outcome simultaneously

### PH-F-114
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
Completeness of primary health care requires that:
a) Adequate attention to all aspects of a medical problem, including prevention, early detection, diagnosis, treatment, follow-up measures, and rehabilitation.
b) The care is provided for all types of health problems.
c) All are correct
d) The management of a patient's care over time is coordinated among providers.

### PH-F-115
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
What is the primary goal of analytical studies in research?
a) To explore and describe natural phenomena
b) To test hypotheses and identify associations or relationships
c) To gather information from a large sample about attitudes
d) To manipulate variables and observe their effects

### PH-F-116
tier: claimed
form: mcq
type: single
claimed: d
models: [3]
In a retrospective descriptive study, when is the data collected?
a) Before the occurrence of the phenomenon
b) Simultaneously with the occurrence of the phenomenon
c) At multiple points in time
d) After the occurrence of the phenomenon

### PH-F-117
tier: claimed
form: mcq
type: single
claimed: c
models: [3]
Which of the following is an essential criterion for a condition to be suitable for screening?
a) No treatment available
b) No early symptoms.
c) High prevalence
d) Low prevalence

### PH-F-118
tier: claimed
form: mcq
type: single
claimed: c
models: [3]
How has the globalization of pharmaceuticals affected access to healthcare in developing countries?
a) No impact on medication accessibility
b) Improved access to affordable medications
c) Increased healthcare disparities
d) Reduced availability of medications worldwide

### PH-F-119
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
What is the purpose of routine screenings in secondary prevention?
a) To detect diseases in their early stages
b) To prevent the occurrence of diseases
c) To rehabilitate individuals after illness
d) To diagnose diseases at an advanced stage

### PH-F-120
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
The ______ is a specialized agency of the United Nations responsible for international public health. This international health organization compiles statistics of diseases and investigates health problems.
a) Occupational Safety and Health Administration
b) World Health Organization
c) Food and Drug Administration
d) Center for Disease Control

### PH-F-121
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
In epidemiological studies, when is it generally true that the odds ratio (OR) approximately equals the risk ratio (RR)?
a) Only in experimental studies
b) When the outcome is rare (low prevalence)
c) When the outcome is common (high prevalence)
d) Regardless of the prevalence of the outcome

### PH-F-122
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
Which of the following is not an Obstacle to the utilization of healthcare services?
a) Rationality
b) Affordability
c) Acceptability
d) Accessibility

### PH-F-123
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
Fall in standardized death rates from infectious diseases in the USA during the 60's occurred because of the
a) Shift in environmental risk factors
b) Development of antibiotics
c) Discovery of vaccination of Poliomyelitis
d) Strict hygiene rules

### PH-F-124
tier: claimed
form: mcq
type: single
claimed: b
models: [3]
note: Radio marked on option b, "Tea drinkers have a higher risk of developing diabetes" -- transcribed exactly as selected on the page, despite the printed RR of 0.86 conventionally indicating a protective effect. Not corrected; Job A transcribes, it does not judge.
In a cohort study, the risk ratio of developing diabetes was 0.86 when comparing consumers of tea (the exposed) to those who did not drink tea (the unexposed). Which one of the statements is correct?
a) Tea drinkers have a lower risk of developing diabetes.
b) Tea drinkers have a higher risk of developing diabetes.
c) The risk ratio is close to the value one, so there is no difference in disease risk between the two groups
d) Based on the information given we cannot tell if the observed difference in disease risk is the result of developing diabetes

### PH-F-125
tier: claimed
form: mcq
type: single
claimed: a
models: [3]
What is a key characteristic of multipurpose screening tests in healthcare?
a) They simultaneously assess multiple health conditions
b) They are primarily used for diagnostic purposes.
c) They focus on a single specific condition
d) They are designed for research purposes only

### PH-F-126
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Identify what this situation reflects: Over 20 million people worldwide died from influenza in 1918—1919
a) Epidemic disease
b) Pandemic disease.

### PH-F-127
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
A person working as a health educator use an approach that views health as related to
a) Pathological processes
b) Behavioral change
c) Health screening
d) Minimize complication

### PH-F-128
tier: claimed
form: mcq
type: single
claimed: c
source: 2020-2021 sitting
which of the following studies apply to this: Persons diagnosed with new-onset Lyme disease were asked how often they walk through woods, use insect repellant, wear short sleeves and pants, etc. Twice as many patients without Lyme disease from the same physician's practice were asked the same questions, and the responses in the two groups were compared
a) Observational cross-sectional
b) Observational cohort
c) Observational case-control
d) Experimental

### PH-F-129
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
In which one of the following circumstances will the prevalence of a disease in the population increase, all else being constant?
a) If the incidence rate of the disease falls
b) If the population in which the disease is measured increases.
c) If recovery of the disease is faster
d) If survival time with the disease increases.

### PH-F-130
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
The _______ rate is the average number of children per women in reproductive age.
a) growth
b) family
c) birth
d) fertility

### PH-F-131
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Health Equality is the opportunity for everyone to attain his or her full health potential.
a) True
b) False

### PH-F-132
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
The individual's culture does not impact his/her views towards health issues.
a) True
b) False

### PH-F-133
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Health promotion became a core policy for the World Health Organization with the Alma-Ata Declaration in 1978 and the 'Health-for-All by the Year Program.
a) False
b) True

### PH-F-134
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
A person's health and wellbeing is dependent on a good start, good future, good care and support. These influences, social, economic, physical and environmental factors are known as
a) Health care
b) Determinants of Health
c) Health promotion
d) Public Health

### PH-F-135
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
which of the following studies apply to this: Representative sample of residents were telephoned and asked how much they exercise each week and whether they currently have (have ever been diagnosed with) heart disease.
a) Observational cohort
b) Observational cross-sectional
c) Observational case-control
d) Experimental

### PH-F-136
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
note: Vignette (shared with PH-F-141/146/155) describes an otoscopic exam for otitis media (OM), but this question's own stem asks about "streptococcal sore throat" -- a disease-name mismatch against the vignette it's attached to. Transcribed exactly as printed, not corrected.
You are working in a pediatric clinic with an experienced pediatrician. You do otoscopic examination of the tympanic membrane (TM) to 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct. The negative predictive value for streptococcal sore throat was
a) 10/35
b) 20/35
c) 15/35
d) 20/50
e) 10/15

### PH-F-137
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Which is not a type of Epidemiology study?
a) Scientific
b) Descriptive
c) Experimental
d) Observational

### PH-F-138
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Isolation of a child with measles belongs to secondary prevention.
a) False
b) True

### PH-F-139
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Identify what this situation reflects: Cases of infectious disease occurred within 3 weeks among residents of a particular neighborhood (usually 0 or 1 per year)
a) Epidemic disease
b) Pandemic disease.

### PH-F-140
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
The decentralization of administrative and decision making functions is considered a way to involve the community in public health development.
a) True
b) False

### PH-F-141
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
note: Vignette (shared with PH-F-136/146/155) describes an otoscopic exam for otitis media (OM), but this question's own stem asks about "streptococcal sore throat" -- a disease-name mismatch against the vignette it's attached to. Transcribed exactly as printed, not corrected.
You are working in a pediatric clinic with an experienced pediatrician. You do otoscopic examination of the tympanic membrane (TM) to 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct. The predictive value of the doctors' clinical judgment for streptococcal sore throat was
a) 10/25
b) 10/50
c) 5/15
d) 10/15
e) 15/25

### PH-F-142
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Pathogenicity refers to the ability of an organism to cause disease
a) False
b) True

### PH-F-143
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Primary Health care philosophy includes the following EXCEPT
a) Treating health as commodity
b) Equity and Justice
c) Inter relationship of Health and Development
d) Individual and community self-reliance

### PH-F-144
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Health literacy is best defined as the capacity of a person to:
a) Recognize and know how to find information about a health problem
b) Follow medical instruction for specific health care problem
c) Read health-related literature
d) Access the internet

### PH-F-145
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: Prevention of disease progression and additional disease complication after overt clinical disease occurrence
  - source: Messenger capture
    answer: Prevention of clinical illness through the early and asymptomatic detection and remediation of certain disease conditions
source: 2020-2021 sitting
note: Second (Messenger) capture of this same sitting selected the option describing early/asymptomatic detection -- which is actually a description of secondary prevention, not tertiary -- while the PDF capture selected the option describing post-clinical progression/complications (correct for tertiary). Matched by content, not letter, since option order differs between captures. RUN-PLAN row 19.
Which of the following processes characterizes the level of disease prevention known as tertiary prevention?
a) Prevention of illness through appropriate individual and group behaviour modification designed to minimize infection risk
b) Prevention of disease before its biological onset
c) Prevention of clinical illness through the early and asymptomatic detection and remediation of certain disease conditions
d) Prevention of disease progression and additional disease complication after overt clinical disease occurrence

### PH-F-146
tier: claimed
form: mcq
type: single
claimed: c
source: 2020-2021 sitting
note: Vignette (shared with PH-F-136/141/155) describes an otoscopic exam for otitis media (OM), but this question's own stem asks about "streptococcal sore throat" -- a disease-name mismatch against the vignette it's attached to. Transcribed exactly as printed, not corrected.
You are working in a pediatric clinic with an experienced pediatrician. You do otoscopic examination of the tympanic membrane (TM) to 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct. The sensitivity of the doctors' clinical judgment was
a) 10/35
b) 10/50
c) 10/25
d) 5/15
e) 15/25

### PH-F-147
tier: claimed
form: mcq
type: single
claimed: c
source: 2020-2021 sitting
Getting a young person to quit smoking is an example of
a) Secondary prevention.
b) Health promotion
c) Primary prevention
d) Tertiary prevention

### PH-F-148
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Which of the following statements about exposures is true?
a) Dietary intake is not an 'exposure' because individuals make a choice about what they eat.
b) 'Exposure' refers to contact with some factor that may be harmful or beneficial to health.
c) An exposed individual has a greater risk of disease.
d) High body mass index is a risk factor for a range of health conditions, therefore, it cannot be treated as a single exposure.

### PH-F-149
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
In a case-control study, the Odds Ratio (OR) is the Ratio of the odds of exposure among the cases to the odds in favor of exposure among the controls
a) False
b) True

### PH-F-150
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Population per hospital bed in Palestine is:
a) 1.23 bed per 10,000 population
b) 12.3 bed per 10,000 population
c) 2 beds per 10,000 population
d) 1 bed per 10,000 population

### PH-F-151
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
The _________ is an international health organization that compiles statistics of diseases and investigates health problems.
a) Food and Drug Administration
b) Occupational Safety and Health Administration
c) Center for Disease Control
d) World Health Organization

### PH-F-152
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
A process by which people gain control and mastery over their own lives is called:
a) Sustainability
b) Intersectoral
c) Equity
d) Empowerment

### PH-F-153
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
_________ is used to describe a small, localized epidemic, often contained to a village or a small town
a) An outbreak
b) A pandemic
c) A sporadic disease
d) An epidemic

### PH-F-154
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Primary health care is usually practiced in:
a) Community health services and NGOs
b) Health education units only
c) Specialized health services and NGOs
d) Community and acute care clinics

### PH-F-155
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Public health services are given adequate attention in the financing of health care in Palestine.
a) True
b) False

### PH-F-156
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Social Justice refers
a) Social inclusion
b) An ethical concept based on human rights and fairness
c) An ethical concept based on autonomy
d) Ensuring the punishment fits the crime

### PH-F-157
tier: claimed
form: mcq
type: single
claimed: c
source: 2020-2021 sitting
note: Vignette (shared with PH-F-136/141/146) describes an otoscopic exam for otitis media (OM), but this question's own stem asks about "streptococcal sore throat" -- a disease-name mismatch against the vignette it's attached to. Transcribed exactly as printed, not corrected.
You are working in a pediatric clinic with an experienced pediatrician. You do otoscopic examination of the tympanic membrane (TM) to 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct. The specificity of the doctors' clinical judgment was
a) 20/35
b) 5/25
c) 20/25
d) 10/25
e) 20/50

### PH-F-158
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
note: Options c and d print identically ("Observational case-control") -- confirmed at full resolution, not a read error. Transcribed verbatim.
which of the following studies apply to this: Occurrence of cancer was identified between April 1991 and July 2002 for 50,000 troops who served in the first Gulf War (ended April 1991) and 50,000 troops who served elsewhere during the same period.
a) Observational cohort
b) Experimental
c) Observational case-control
d) Observational case-control

### PH-F-159
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
By basing programs and services in communities, organizations, and schools where most people spend most of their time, you can increase the likelihood of long-term success to the road of health and wellness.
a) False
b) True

### PH-F-160
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: Those who take vitamins C & E daily have 0.7 times the risk of heart attack compared to those who do not take vitamins
  - source: Messenger capture
    answer: The incidence of coronary artery disease in those who take vitamins C& E daily is 0.70 (or 70%)
source: 2020-2021 sitting
note: Stem prints the risk ratio as "0.07" but the PDF capture's selected answer describes "0.7 times the risk" -- transcribed exactly as printed, not corrected. Second (Messenger) capture of this same sitting selected a different option entirely ("incidence...0.70 (70%)"), a genuine within-sitting disagreement, not just a reshuffled letter. RUN-PLAN row 19.
A study is done to examine whether is an association between the daily use of vitamins C & E and risk of coronary artery disease (heart attack) over a 10 years period. When subjects who took both vitamins were compared to those who took not vitamins at all, the risk ratio was found to be 0.07. which of the following is a correct interpretation of this finding?
a) Those who take vitamins C & E daily have 0.7 times the risk of heart attack compared to those who do not take vitamins
b) The risk difference in this study is 0.70 per 100 vitamin users over ten years.
c) The risk difference in this study is 70 per 100 vitamin users over ten years
d) The incidence of coronary artery disease in those who take vitamins C& E daily is 0.70 (or 70%)

### PH-F-161
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: One exposure to this factor is always enough to develop the disease
  - source: Messenger capture (Q21, "Answer saved" state matching the rest of this capture)
    answer: One exposure to this factor is always enough to develop the disease
  - source: Messenger capture (page labeled "Question 78", "Marked out of 1.0", "Select one:" -- visual style anomalous vs. the rest of this capture, possibly a different attempt/quiz that got mixed into this photo set)
    answer: The exposure to this factor should precede the development of the disease.
source: 2020-2021 sitting
note: Same messenger capture set contains two photos of this question. One (numbered Question 21, styled like the rest of the set) reconfirms the existing PDF-capture claim. The other (numbered Question 78, styled differently -- "Marked out of 1.0" instead of "Marked out of 1", an explicit "Select one:" label, hand-drawn tick mark) disagrees and may not actually be from the same exam attempt as the rest of this photo set. Recorded as a dispute rather than silently preferring one; flagged for a future session to judge. RUN-PLAN row 19.
The following criteria are necessary to establish causal relationship between two variables except:
a) The exposure to this factor should precede the development of the disease.
b) The factor is present in all subjects with the disease
c) Elimination of the factor reduces risk of the disease.
d) One exposure to this factor is always enough to develop the disease

### PH-F-162
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: Smokers had 17 times the risk of lung cancer compared to non-smokers.
  - source: Messenger capture
    answer: Smokers had 17 times more risk of lung cancer than non-smokers.
source: 2020-2021 sitting
note: The PDF capture's on-screen UI overlay obscuring the exposed-group sample size ("... following ___ smokers ...") is NOT present in the second (Messenger) capture, which shows the number plainly -- "400 smokers" -- so the stem below is now complete instead of "[obscured]". On the answer itself, the two captures selected two similarly-worded but distinct options ("17 times the risk...compared to" vs. "17 times more risk...than"), a genuine disagreement, not a reshuffled letter -- both options exist in each capture's own list and only one of the two was selected each time. RUN-PLAN row 19.
A cohort study examined the association between smoking and lung cancer after following 400 smokers and 600 non-smoker for 15 years. At the conclusion of the study the investigators found a risk ratio=17. Which of the following would be the best interpretation of the risk ratio?
a) Smokers had 17% more lung cancers compared to non-smokers.
b) There were 17 more cases of lung cancer in the smokers.
c) Smokers had 17 times more risk of lung cancer than non-smokers.
d) 17% of the lung cancers in smokers were due to smoking.
e) Smokers had 17 times the risk of lung cancer compared to non-smokers.

### PH-F-163
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Which of the following is the best definition of public health?
a) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science
b) None of these
c) All of these
d) The process of mobilizing local, state/provincial, national and international resources to assure the conditions in which all people can be healthy
e) Ensuring the health of the individual by maintaining and improving the health of the community

### PH-F-164
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
What is the best way to prevent the spread of infection?
a) Avoid contact with ill patients
b) Wash your hands
c) Use alcohol wipes to clean surfaces
d) Use personal protective equipment

### PH-F-165
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
which of the following studies apply to this: Subjects were children enrolled in a health maintenance organization. At 2 months, each child was randomly given one of two types of a new vaccine against rotavirus infection. Parents were called by a nurse two weeks later and asked whether the children had experienced any of a list of side-effects.
a) Observational cohort
b) Experimental
c) Observational case-control
d) Observational cross-sectional

<!-- batch 04 -- .prep/finals/2020-2021/2/ (22 Messenger-photo pages, all vision, all below prep.py's 1000px floor per manifest.json but confirmed legible on direct read). RUN-PLAN row 19, Part 1. A second, independent capture of the SAME 2020-2021 sitting already in this file as PH-F-126-165 (that pool was captured via PDF, `raw/finals/2020-2021/1/`). Matched every fully-legible question against PH-F-126-165 by stem text only -- never against PH-F-001-125, which belong to a different sitting/year and were kept out of scope per this row's own brief (mirrors batch03's precedent of not cross-matching sittings).

  This capture is inherently fragmentary: 22 phone photos of a scrolling browser window, several page boundaries mid-question, several photos duplicating the same scroll position (no new information -- not a duplicate drop, same handling as batch03's p019/p020). Because of this, standard number continuity does not apply cleanly -- question numbers 13, 19, 33, 35, 37 were never captured at all, and several other questions were seen only as a stem with no visible answer state or vice versa (excluded below rather than guessed). This is a property of a partial re-capture, not a loss from this session's reading.

  21 questions matched PH-F-126-165 by stem with the same claimed content (letter position frequently differs between the two captures -- Moodle re-randomizes option order per attempt -- so matches were judged by what the selected option *says*, never by its letter): PH-F-126, 127, 128, 129, 130, 131, 132, 135, 136, 139, 141, 144, 146, 149, 150, 155, 157, 158, 159, 163, 164, 165 (22 listed -- one of these, PH-F-161, also surfaced a second, disagreeing sighting, see below). No changes were needed to these entries beyond this confirmation; none carry a `models:`-style cross-reference since this isn't the reshuffled-models exception, just a second capture of one sitting.

  4 questions matched but disagreed with the existing PDF-capture claim on content, not just letter -- each now marked `disputed: true` with per-capture `claims:`, updated in place above: **PH-F-145** (tertiary prevention -- Messenger capture selected the option describing early/asymptomatic detection, which actually describes secondary prevention). **PH-F-160** (vitamin C&E/CAD risk-ratio interpretation -- Messenger capture selected a wholly different option than the PDF capture, not just a relettered version of the same one). **PH-F-161** (causal-relationship-except -- see note below, an internal anomaly). **PH-F-162** (smoking/lung-cancer risk ratio=17 interpretation -- the two captures picked two similarly-worded but distinct options; the Messenger capture also incidentally recovered this question's previously `[obscured]` sample size, now legible as "400 smokers", folded into the stem with a note rather than left obscured).

  PH-F-161 is a special case worth flagging on its own: this capture contains TWO photos of the same question. One, numbered "Question 21" and styled identically to the rest of this photo set ("Answer saved", "Marked out of 1", no "Select one:" label), reconfirms the existing PDF-capture claim exactly. The other, numbered "Question 78" -- a number impossible for this 40-question sitting -- is styled differently ("Marked out of 1.0", an explicit "Select one:" line, a hand-drawn pen tick instead of a filled Moodle radio) and selects a different answer. This page may not actually belong to the same exam attempt as the rest of the folder; it was processed per this row's brief regardless (every image in the folder was read), and both sightings are recorded as competing claims in PH-F-161 rather than one being silently discarded.

  14 questions never appeared anywhere in PH-F-126-165 and were minted as new IDs, continuing the running counter (PH-F-166 through PH-F-179), tagged `source: 2020-2021 sitting` like the rest of this sitting's pool. One of the fourteen ("Primary health care is:") was itself seen on two separate photos within this same Messenger capture, agreeing both times -- counted once.

  No question in this batch depends on a photo, chart, or diagram -- all legible entries are plain-text `mcq`, `type: single`; no crops saved to `flagged/`. Every legible question in this capture already carries an "Answer saved" state with a filled radio, so every entry (new or matched) is tier `claimed`, consistent with the rest of PH-F-126-165 -- no official tier anywhere in this sitting.

  Anti-loss checks: number continuity does not cleanly apply to this fragmentary re-capture (see above) -- documented rather than silently skipped or forced. Count reconciliation: 22 photos yielded 39 distinct fully-legible question-sightings (some questions spanned 2 photos at a page boundary and were combined into one reading, consistent with job-a-extract.md's stitching rule) -- 21 clean matches + 4 disputed matches + 14 new = 39, accounted for. A handful of additional partial sightings (stems or option lists cut off at a photo boundary with no continuation elsewhere in this capture) were deliberately excluded rather than transcribed incomplete or guessed. Structural floor: all 14 new entries are `mcq` with >=2 options, none malformed. Language check: all stems/options are English; the only non-English text anywhere is Moodle interface chrome, discarded. Computed header counts: recomputed from the full body below at the end of this session's edits. **Not yet run through Job C or D.** -->

### PH-F-166
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
Health Promotion Action means EXCEPT
a) Reorient health services to focus on people empowerment
b) Strengthen community-wide health action
c) Building public healthy policy
d) Develop highly specialized medical services
e) Create supportive social environment

### PH-F-167
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Screening is a good way to prevent the occurrence of non-communicable diseases such as cancer.
a) False
b) True

### PH-F-168
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
Which of the following is an example of a non-communicable condition with multiple social determinants and causes?
a) Violence including suicide and homicide
b) Alcohol related deaths and disease
c) Obesity
d) All are correct
e) Teen/unplanned parenthood

### PH-F-169
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Which of the following can be an observational study:
a) Community trial
b) Cross-Sectional
c) Randomized controlled trial
d) Field trial

### PH-F-170
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Which of the following is considered to be a public health achievement during the twentieth century?
a) Vaccination
b) Maternal and infant care
c) All are correct
d) Antibiotics

### PH-F-171
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Becoming health literate requires understanding technical medical terms.
a) False
b) True

### PH-F-172
tier: claimed
form: mcq
type: single
claimed: c
source: 2020-2021 sitting
Which of the following is true of the determinants of health?
a) If a pathogenic organism can be shown to cause a disease then no other determinants are present
b) One determinant is operating to bring about each disease
c) They reflect multiple, interconnected underlying forces that influence health and the subsequent development of disease
d) Each determinant can usually be traced to specific diseases

### PH-F-173
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
note: Seen on two separate photos in this capture (once numbered Question 27), agreeing both times.
Primary health care is:
a) The first point of contact for people with the health care services.
b) Care provided in the acute setting
c) Care provided in hospices
d) Care provided by GPs only

### PH-F-174
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Epidemiological measures of effect assess the _______ between an exposure and an outcome.
a) Strength of the association
b) Strength of the causal mechanisms
c) Strength of the reversibility
d) Strength of a confounding factor

### PH-F-175
tier: claimed
form: mcq
type: single
claimed: d
source: 2020-2021 sitting
Which is the direct mechanism of transmission of communicable diseases:
a) Air borne
b) Vehicle borne
c) Vector borne
d) Sexual intercourse

### PH-F-176
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Health care services include:
a) All are correct
b) All of the above
c) Acute and Chronic
d) Restorative and palliative
e) Preventive

### PH-F-177
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
If a disease is endemic that means it is at the normal, expected level within the population.
a) False
b) True

### PH-F-178
tier: claimed
form: mcq
type: single
claimed: a
source: 2020-2021 sitting
Screening is considered sensitive if:
a) If high percentage of identified cases are true positives
b) If majority of identified cases are true negatives
c) All detected cases are true positives
d) If None of the identified cases is false positive

### PH-F-179
tier: claimed
form: mcq
type: single
claimed: b
source: 2020-2021 sitting
Availability means that the cost should be within the means and resources of the individual and the country.
a) True
b) False

<!-- batch 05 -- .prep/finals/2015-moodle-final/*.jpg (11 unique pages after Stage 0 dedup dropped 2 exact-duplicate PNGs; all vision, all below the 1000px floor per manifest.json but confirmed legible on direct read). RUN-PLAN row 19, Part 2. Genuine 2015 Moodle "Final exam" attempt screenshots -- confirmed directly: browser chrome (Firefox), breadcrumb reading "Home > Fall 2015/2016 > GENERAL MEDICINE... 2151-6106211-sec7 > General > Final exam", Al-Quds University Moodle header visible on 3 of the 11 photos, "Answer saved"/"Marked out of 1" states throughout. Own new pool, own new ID range (PH-F-180 through PH-F-197) -- not merged with PH-F-001-179, a distinct exam year with its own content. Every entry tagged `source: 2015 Moodle final (partial)`.

  This is inherently partial coverage, confirmed by the exam's own question-navigation grid (visible on 3 of the 11 photos): the grid runs to at least 80 ("79 80" then "Finish attempt...", "Time left 0:17:51"), so the exam has >=80 questions total, not the ~66 previously guessed -- these 11 photos cover only a fragment of that, and the rest was simply never screenshotted by whoever captured this, not a failure to find it. Do not assume/interpolate the missing questions.

  Of the 11 photos, several show duplicate scroll positions: two separate photos (different filenames/hashes, not caught by Stage 0's exact-file dedup) show the identical rendered page for Q26-Q29, and three separate photos show the identical rendered page for Q1-Q3 -- no new information beyond confirming the same reading each time, not a duplicate drop (same handling as batch03's p019/p020 precedent).

  18 questions were fully legible end to end (stem + complete option list + a visible selection) and were transcribed: Q1, Q2, Q3, Q4, Q5, Q6, Q10, Q11, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q26, Q27, Q28 -- minted PH-F-180 through PH-F-197 in question-number order. One of these, Q6, has the identical stem to Q2 ("Both equal utilization of health care and equal access to health care lead to equity.") and both independently selected True -- recorded as two separate entries (PH-F-181 and PH-F-185) since Moodle showed them as two separate numbered questions in the same attempt, not a page-boundary artifact; noted on PH-F-185.

  6 further questions were sighted but NOT transcribed because a photo-boundary cut them off before the answer state or full option list ever appeared on any of the 11 pages, and nothing elsewhere in this batch completes them: Q7 ("Body mass index is defined as...") -- stem visible, options/selection never captured. Q8 -- never appeared at all. Q9 -- only its answer tail ("a. False / b. True [selected]") is visible with no stem ever captured. Q12 ("The decentralization of administrative and decision making functions...") -- stem visible, options never captured. Q20 ("Prevention refers to the goals of medicine...") -- stem visible, options never captured. Q29 ("Environmental hazards might be") -- stem visible, options never captured. None of these six are guessed or interpolated; they simply don't exist in this extract.

  All 18 transcribed questions are plain-text `mcq` -- 12 are `type: single` True/False, 6 are `type: single` multi-option mcq (one with 6 options, Q4). None depend on a photo, chart, or diagram; no crops saved to `flagged/`. Every question shows "Answer saved" with a filled radio and no printed key anywhere -- tier `claimed` throughout, consistent with every other tab in this course.

  Anti-loss checks: number continuity does not apply -- this is a deliberately partial re-capture of a >=80-question exam, not a claim of a complete 1-N sequence (documented above rather than silently skipped). Count reconciliation: 11 photos, 18 fully legible + 6 explicitly-excluded partial sightings = 24 question-instances accounted for (some questions spanning 2-3 duplicate/boundary photos, combined into one reading each). Structural floor: all 18 are `mcq` with >=2 options, none malformed. Language check: all stems/options are English; the only non-English text is the Al-Quds University Arabic branding visible in the page chrome on 3 photos, never inside a stem or option. Computed header counts: recomputed from the full body below at the end of this session's edits. **Not yet run through Job C or D.** -->

### PH-F-180
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
Which of the following is considered to be a public health achievement during the twentieth century?
a) All of them
b) Maternal and infant care
c) Antibiotics
d) Vaccination

### PH-F-181
tier: claimed
form: mcq
type: single
claimed: b
source: 2015 Moodle final (partial)
Both equal utilization of health care and equal access to health care lead to equity.
a) False
b) True

### PH-F-182
tier: claimed
form: mcq
type: single
claimed: b
source: 2015 Moodle final (partial)
Health promotion fall into two clusters that are mutually exclusive.
a) True
b) False

### PH-F-183
tier: claimed
form: mcq
type: single
claimed: c
source: 2015 Moodle final (partial)
Methods of Primary Prevention:
a) None of them
b) Keeping yourself clean—wash hands with antibacterial soaps & shower
c) All of them
d) Exercise and good nutrition
e) Get enough rest
f) Isolation or avoidance—staying away from infected individuals

### PH-F-184
tier: claimed
form: mcq
type: single
claimed: d
source: 2015 Moodle final (partial)
The Declaration outlined the central concerns of the global community and articulated a set of interconnected and mutually reinforcing goals for sustainable development
a) Health determinants
b) Health development
c) Alma-Ata Declaration
d) Millennium Development Goals

### PH-F-185
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
note: Identical stem to PH-F-181 (Q2 in this same attempt); both independently selected True. Kept as two separate entries since Moodle presented them as two distinct numbered questions (Q2 and Q6) in the one attempt, not a capture artifact.
Both equal utilization of health care and equal access to health care lead to equity.
a) True
b) False

### PH-F-186
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
Chronic PEM effects are growth retardation, lowered resistance to infection, and increased mortality rates in young children.
a) True
b) False

### PH-F-187
tier: claimed
form: mcq
type: single
claimed: e
source: 2015 Moodle final (partial)
The main determinants of health are
a) Individual capacity & coping skills
b) Health services
c) Social & economic environment
d) Personal health practices
e) All of them
f) Physical environment

### PH-F-188
tier: claimed
form: mcq
type: single
claimed: b
source: 2015 Moodle final (partial)
Health improves only when scientific knowledge on disease causation adopted by the public.
a) False
b) True

### PH-F-189
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
Obesity affects children and adolescents, as well as the adult population.
a) True
b) False

### PH-F-190
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
The Inborn immune system is the following except
a) White blood cells & Lymphocytes
b) Macrophages, Natural Killer Cells & Neutrophils kill infectious agents
c) Skin—outer protective barrier
d) The body's first line of defense against disease.

### PH-F-191
tier: claimed
form: mcq
type: single
claimed: b
source: 2015 Moodle final (partial)
Socratis's approach to disease and research were the first steps on the way to the prevention and control of disease.
a) True
b) False

### PH-F-192
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
Alcoholism and other certain drug addictions may lead to malnutrition...
a) True
b) False

### PH-F-193
tier: claimed
form: mcq
type: single
claimed: c
source: 2015 Moodle final (partial)
Eric visits his doctor on a regular basis because he is a hypochondria. What level of prevention is it?
a) None of them
b) Tertiary prevention
c) Secondary prevention
d) Primary prevention

### PH-F-194
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
PEM stand for Positron emission mammography
a) False
b) True

### PH-F-195
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
Infant mortality rate is made up of two components, the neonatal mortality & postneonatal mortality.
a) True
b) False

### PH-F-196
tier: claimed
form: mcq
type: single
claimed: a
source: 2015 Moodle final (partial)
An individual must be an active and willing participant in health behavior change if that is to be maintained.
a) True
b) False

### PH-F-197
tier: claimed
form: mcq
type: single
claimed: b
source: 2015 Moodle final (partial)
Primary prevention aims to reduce the onset of ill health.
a) False
b) True

<!-- batch 06 -- raw/finals/2015-moodle-final/examPub.doc, a separate, unrelated document (own new pool, own new ID range PH-F-198 through PH-F-229). RUN-PLAN row 19, Part 3. An old binary OLE `.doc`, read via `antiword` (the Read tool cannot open it directly; antiword produced ~218 clean lines of text). Content: a fully-answered essay/short-answer exam template -- header "Al-Quds University, Faculty of Medicine, Khuloud Khayyat Dajani, M.D, M.Sc, CM.D, Ph.D., Date: May 15, 2013" with blank, never-filled-in `Name:____`/`Number:____` fields -- 6 numbered Questions, several with lettered or numbered sub-parts, each followed by a complete written answer, ending "GOOD LUCK (2 hrs)".

  **Tier is genuinely ambiguous and was deliberately set to `claimed`, not `official`, per job-a-extract.md's own rule ("when the tier is ambiguous, drop to the lower one").** The professor's name is in the header, but since Name/Number were never filled in, there's no way to tell whether this is the professor's own answer key, or a student's (or later compiler's) completed answer sheet using the professor's blank template. Job C should weigh this tier deliberately rather than pass it through as free/trusted -- it reads as polished and textbook-accurate, but its provenance is not certain.

  Every numbered Question (1-6) with its lettered/numbered sub-parts was split into one `form: qa` entry per sub-part, following this repo's existing precedent for matching/EMQ-style blocks (see `public-health-practice.extract.md`). No options were invented anywhere -- `qa` with no options is this entry type's correct shape, not a malformed one. Every entry tagged `source: Dajani essay exam (2013, definitions doc)`, distinct from Part 2's `source: 2015 Moodle final (partial)` even though both live in the same raw folder -- they are unrelated documents that merely happen to share a directory.

  The document has some Arabic annotations interspersed (e.g. after PH-F-202, PH-F-206, PH-F-207) that antiword renders as garbled `?` characters, since it does not handle non-Latin encoding. These are noted explicitly on the affected entries as "Arabic annotation present, not recoverable via antiword" rather than silently dropped or fabricated as a translation.

  The document has 9 embedded images (4 JPEG + 5 PNG, extracted via binary signature scan since antiword only leaves `[pic]` placeholders), each a formula or table supporting one specific written answer. All 9 were inspected directly; 8 are load-bearing (the written answer alone does not convey the formula/table, which exists only in the image) and were copied to `flagged/`: `PH-F-211-prevalence-formula.png`, `PH-F-212-incidence-formula.png`, `PH-F-213-case-fatality-formula.png`, `PH-F-214-infant-mortality-formula.png`, `PH-F-215-maternal-mortality-formula.png` (Q2's rate-formula sub-items), `PH-F-220-levels-of-prevention-table.jpg` (Q3), `PH-F-221-epi-study-types-table.jpg` (Q4), `PH-F-222-causation-criteria-table.jpg` (Q5). The 9th image (a "Table 7.2, Modes of transmission of an infectious agent" JPEG) sits after the exam's "GOOD LUCK (2 hrs)" sign-off, alongside an untranslated Arabic line and a trailing English paragraph on endemic/epidemic terminology -- judged, per this row's own instruction to use judgment on where the exam content ends, to be trailing supplementary notes rather than a formal numbered exam question. It was NOT minted as a PH-F entry and NOT copied to `flagged/` (nothing to be load-bearing for), but is recorded here rather than silently discarded -- a future session can revisit this call if warranted.

  Question 2's own text has a stray non-English fragment ("7asab jadwal 2*2", i.e. Arabic transliterated into Latin letters, roughly "according to the 2x2 table") inline in its Odd Ratio sub-answer -- preserved verbatim as printed, not translated or removed, since it is Latin-script and not the antiword-garbled Arabic seen elsewhere. Also preserved verbatim: the document's own spelling "Odd Ratio" (not "Odds Ratio") and a formula in Question 6 that appears to duplicate itself (Prevalence Rate and Attack Rate are both given as "(a+c)/(a+b+c+d)" despite being different measures) -- not corrected, flagged on the Attack Rate entry.

  Anti-loss checks: number continuity is not applicable (this is a lettered/numbered outline, not a numbered question sequence) -- documented rather than silently skipped, per job-a-extract.md's own carve-out for unnumbered material. Count reconciliation: 6 source Questions with 32 total sub-parts (Q1: 1 + 1 + 10 = 12; Q2: 10; Q3: 1; Q4: 1; Q5: 1; Q6: 1 + 6 = 7) match the 32 entries below (PH-F-198 through PH-F-229). Structural floor: all 32 are `form: qa` with no options -- their correct shape, not malformed. Language check: English throughout except the noted, explicitly-flagged Arabic/transliterated fragments. Computed header counts: recomputed from the full body below at the end of this session's edits. **Not yet run through Job C or D.** -->

### PH-F-198
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: Health: The state of complete physical, mental & social well-being & not merely the absence of disease or infirmity. Positive Health: Holds that health is the maximization of the biological and clinical indicator of organ function and the maximization of physical, mental and role functioning in every day life.
What is your understanding of health / positive health?

### PH-F-199
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: 1-Hygiene: Personal Health Exercise & Body Built. 2-Sanitation: Health Emergency, Sewage System, Water Supply, Solid Waste Disposal. 3-Preventive Medicine: A-Preventive Medicine (Immunization, Supplementation), B-Prevention of complication of diseases (Secondary Prevention), C-Prevent further complication of Rabies (tertiary prevention). Environmental Health: Monitor & protection of air pollution, Healthy Houses, Master Plan (Villages & towns), Safe water supply, Sewage Disposal, Solid Waste disposal, Protection of water source from pollution, Rodent Control, Control of Hazards waste. 4-Healthy Group: Ante-Natal and post Natal care, Child Care, Infants, Pre school, Adult age (including occupational Health), Elderly Care.
What are the goals of good health?

### PH-F-200
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: is a science that aims to prevent diseases, increase life expectancy, provide good health & good socioeconomic status. That is through concern on Environmental Health, Prevention of communicable and non communicable diseases, Provide Personal Hygiene education, early diagnosis of disease and Socio-economic Development.
Write the definition of the following: Public Health

### PH-F-201
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: is the total societal effort, undertaken in the private and public sectors focused on pursuing health.
Write the definition of the following: Health Care

### PH-F-202
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: An Arabic annotation follows this item in the source ("??????? ? ?? ???? ?? ?????? 5 ?? ???? ?????" per antiword, followed by "health Management") -- antiword garbles non-Latin script; not recoverable, not fabricated as a translation.
answer: within the larger domain of health care, health services are specific activities undertaken to maintain or improve health or to prevent decrements of health. These services can be preventive, acute, chronic, restorative or palliative.
Write the definition of the following: Health Care Service/s

### PH-F-203
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: HSOs are entities that provide the organizational structure within which the delivery of health services is made directly to consumers, whether the purpose of the services is preventive, acute, chronic, restorative or palliative.
Write the definition of the following: Health Care Services Organization

### PH-F-204
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: the study of the distribution and determinants of health-related states or events in specified populations, and the applications of this study to control of health problems.
Write the definition of the following: Epidemiology

### PH-F-205
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: 1- the continuum of health services outlined previously has been provided traditionally by autonomous or independent HSOs, often in an uncoordinated and disjointed manner. 2- anthropologists refer to various practices for healing the sick, according to diverse religious, philosophical, magical, and empirical doctrines.
Write the definition of the following: Health System

### PH-F-206
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: An Arabic annotation follows this item in the source ("???? ??? ??????? ?? ????? ????? ?? ????? ??????? ???? ?????? ??? ????? ????? ." per antiword) -- antiword garbles non-Latin script; not recoverable, not fabricated as a translation.
answer: is the occurrence in a community or region of number of cases of a disease that is unusually large or unexpected for the given place and time. Time period, Geographical region and the particular community group in which the cases occur must be clearly specified.
Write the definition of the following: Epidemic Disease

### PH-F-207
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: An Arabic annotation follows this item in the source ("*???? ?? ????? ????? ??? ???? ?? ????? ???? ?????" per antiword) mixed with the English fragment "normal number of cases" -- antiword garbles non-Latin script; not recoverable, not fabricated as a translation.
answer: is one that usually present in a given geographical area or population group at relatively high prevalence and incidence rate in comparison with the other area or population, e.g: Malaria.
Write the definition of the following: Endemic Disease

### PH-F-208
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: An Arabic annotation follows this item in the source ("?????? ????? ??? ???? ????? ." per antiword) -- antiword garbles non-Latin script; not recoverable, not fabricated as a translation.
answer: is an epidemic of infectious disease that has spread through human populations across a large region; for instance multiple continents, or even worldwide.
Write the definition of the following: Pandemic Disease

### PH-F-209
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: is an event, condition, characteristic or a combination of these factors which plays an important role in producing the disease. Logically, a cause must precede a disease. A cause is termed sufficient when it inevitably produces or initiates a disease and is termed necessary if a disease cannot develop in its absence.
Write the definition of the following: Causal Association

### PH-F-210
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: a measure of the frequency with which an event occurs in a defined population in specified period of time. R = (No. of events / No. of total pop) x 10^n.
Explain the following and show how to measure each: Rate

### PH-F-211
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-211-prevalence-formula.png
answer: is the number of cases in a defined population at a specified point in time. Formula shown in the referenced image: P = (Number of people with the disease or condition at a specified time / Number of people in the population at risk at the specified time) x 10^n.
Explain the following and show how to measure each: Prevalence

### PH-F-212
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-212-incidence-formula.png
answer: the number of new cases arising in a given period in a specified population. Formula shown in the referenced image: I = (Number of people who get a disease in a specified period / Sum of the length of time during which each person in the population is at risk) x 10^n.
Explain the following and show how to measure each: Incidence

### PH-F-213
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-213-case-fatality-formula.png
answer: is a measure of the severity of a disease and is defined as the proportion of cases of a specified disease or condition which are fatal within a specified time. Formula shown in the referenced image: Case-fatality (%) = (Number of deaths from a disease in a specified period / Number of diagnosed cases of the disease in the same period) x 100.
Explain the following and show how to measure each: Case-Fatality

### PH-F-214
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-214-infant-mortality-formula.png
answer: is commonly used as an indicator of the level of health in a community. It measures the death rate in children during the first year of life. Formula shown in the referenced image: Infant mortality rate = (Number of deaths in a year of children less than 1 year of age / Number of live births in the same year) x 1000.
Explain the following and show how to measure each: Infant Mortality Rate

### PH-F-215
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-215-maternal-mortality-formula.png
answer: Formula shown in the referenced image: Maternal mortality rate = (Maternal pregnancy-related deaths in one year / Total births in same year) x 10^n.
Explain the following and show how to measure each: Maternal Mortality Rate

### PH-F-216
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: incidence of disease, measured by counting the number of people who become ill.
Explain the following and show how to measure each: Morbidity

### PH-F-217
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: any restriction or lack (resulting from impairment) of ability to perform an activity in the manner or within the range considered normal for a human being.
Explain the following and show how to measure each: Disability

### PH-F-218
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: Source spells this "Odd Ratio", not "Odds Ratio" -- preserved as printed. Contains an inline transliterated-Arabic fragment ("7asab jadwal 2*2", i.e. "according to the 2x2 table") -- preserved verbatim, not translated or removed.
answer: the rate of the odds of the exposure among cases to the odds in favour of exposure among control. OR = (a*d)/(b*c) (7asab jadwal 2*2).
Explain the following and show how to measure each: Odd Ratio

### PH-F-219
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: the ratio of the risk of occurrence of a disease among people exposed to that in unexposed.
Explain the following and show how to measure each: Relative Risk

### PH-F-220
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-220-levels-of-prevention-table.jpg
answer: Shown in the referenced image (Table 6.1, Levels of prevention): Primordial -- phase: underlying conditions leading to causation; target: total population and selected groups. Primary -- phase: specific causal factors; target: total population, selected groups and healthy individuals. Secondary -- phase: early stage of disease; target: patients. Tertiary -- phase: late stage of disease (treatment, rehabilitation); target: patients.
Levels of prevention can be identified corresponding to different phases of the development of disease. All levels of prevention are important and complementary. Explain the levels of prevention and relate each to phase of disease, and identify the target population.

### PH-F-221
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-221-epi-study-types-table.jpg
answer: Shown in the referenced image (Table 3.1, Types of epidemiological study): Observational studies -- Descriptive studies; Analytical studies: Ecological (alt. name Correlational, unit: Populations), Cross-sectional (alt. name Prevalence, unit: Individuals), Case-control (alt. name Case-reference, unit: Individuals), Cohort (alt. name Follow-up, unit: Individuals). Experimental studies (alt. name Intervention studies): Randomized controlled trials (alt. name Clinical trials, unit: Patients), Field trials (unit: Healthy people), Community trials (alt. name Community intervention studies, unit: Communities).
Concerning the different types of Epidemiological studies, please fill the following table.

### PH-F-222
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
img: flagged/PH-F-222-causation-criteria-table.jpg
answer: Shown in the referenced image: Temporal relation (does the cause precede the effect? -- essential), Plausibility (is the association consistent with other knowledge -- mechanism of action, evidence from experimental animals), Consistency (have similar results been shown in other studies?), Strength (what is the strength of the association between the cause and the effect? -- relative risk), Dose-response relationship (is increased exposure to the possible cause associated with increased effect?), Reversibility (does removal of a possible cause lead to reduction of disease risk?), Study design (is the evidence based on a strong study design?), Judging the evidence (how many lines of evidence lead to the conclusion?).
List the basic concept to establish causation about a case of a disease (Causal Association).

### PH-F-223
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: a = true positive, b = false positive, c = false negative, d = true negative.
The screening test is valid if it correctly categorizes people with and without disease. From the following (2x2) table: | | Disease present | Disease absent | | Screening test positive | a | b | | Screening test negative | c | d |. From the (2x2) table, explain what a, b, c, and d represent.

### PH-F-224
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: a / (a+c)
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Sensitivity

### PH-F-225
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: d / (b+d)
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Specificity

### PH-F-226
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: a / (a+b)
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Positive Predictive value

### PH-F-227
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: d / (c+d)
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Negative Predictive Value

### PH-F-228
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
answer: (a+c) / (a+b+c+d) -- (x) [printed exactly as this, with a trailing "- (x)" of unclear referent; preserved verbatim, not corrected]
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Prevalence Rate

### PH-F-229
tier: claimed
form: qa
source: Dajani essay exam (2013, definitions doc)
note: This formula is printed identically to Prevalence Rate's (PH-F-228) above, despite Attack Rate being a different measure -- preserved verbatim, not corrected; likely a source error.
answer: (a+c) / (a+b+c+d)
From the screening-test 2x2 table (a = true positive, b = false positive, c = false negative, d = true negative), measure the following: Attack Rate, if (X) reflects the people who died
