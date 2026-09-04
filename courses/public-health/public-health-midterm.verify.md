---
course: public-health
tab: midterm
scope: raw/midterm/2023/ (نموذج ١+٢+٣, PH-M-001–084) + raw/midterm/2022/ (PH-M-085–128) + raw/midterm/2015/Mid Exam P.H. 2015.pdf (PH-M-129–177) — all 177 questions
questions: 177
verified: 135 | conflict: 6 | external: 18 | not-in-source: 16 | needs-eye: 2
---

Zero official tier anywhere in this course (per CLAUDE.md course header) — every
question decided independently from `source.md` first, claim compared second, per
job-c-verify.md's own rule. The three 2023 نماذج (PH-M-001–084) and the 2022 paper
exam (PH-M-085–128) are covered by `source.md`'s 16 chapters throughout. The 2015
sitting (PH-M-129–177) draws claims from `public-health-practice.extract.md`'s PYQ
bank (PH-P-034–082, a verbatim reproduction of this same 2015 exam with a student's
answers marked in bold) rather than from this file's own tier field, which is `open`
throughout that range — stem-matched programmatically (48 of 49 matched with a
stem-similarity ≥0.85; PH-M-151 has no PYQ counterpart) and option letters remapped
by matching option text, since PYQ's option order frequently differs from PH-M's.
A large share of the 2015 sitting (roughly a third) sits outside this course's
16-chapter `source.md` entirely — family dynamics, DSM/mental-disorder
classification, community-participation typology, and similar topics never covered
by the 2023-24 lecture decks this source was built from — and is marked
`not-in-source` rather than forced against a chapter that doesn't address it.

**6 real conflicts found** — see the report for the full list; most involve either
a definition genuinely swapped between two adjacent concepts in the source itself
(spiritual vs. emotional health, environmental vs. life-style vs. multi-causal
disease theory, medical model vs. public-health model) or a claim that
contradicts a source-stated fact outright (Palestine's own workforce table showing
nurses outnumber physicians).

### PH-M-001
status: external
answer: d
claimed: a (first pass), b (second pass)
basis: external — not covered in source.md
evidence: Neither claimed answer (Correlation, Statistical significance) is the
  standard criterion for establishing causation in a single scientific study —
  correlation is explicitly the thing causation must be distinguished from, and
  statistical significance only rules out chance, not confounding. The textbook
  answer is randomization/experimental control, which is what allows a study to
  support a causal claim rather than a merely associative one (Ch. 6's
  observational-vs-experimental framing is the closest source material, but this
  exact framing — "primary criterion for causation" — isn't stated there in these
  terms).
note: Both of Job A's disputed claims (a, b) are wrong by this same external
  reasoning, not just one.

### PH-M-002
status: verified
answer: d
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-3}
evidence: "Physical health — anatomical integrity and physiological functioning of
  the body; the ability to perform routine tasks without physical restriction."

### PH-M-003
status: verified
answer: d
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-2}
evidence: "Necessary cause: a disease cannot develop in the absence of this
  cause" — required for occurrence but (unlike a sufficient cause) not
  necessarily enough on its own.

### PH-M-004
status: external
answer: c
basis: external — not covered in source.md
evidence: Standard nutrition/public-health fact (food insecurity drives reliance on
  cheap, high-calorie, nutrient-poor food, raising chronic-disease risk) — Ch. 3's
  food-insecurity passage covers supply-chain shocks, not this downstream health
  mechanism.

### PH-M-005
status: verified
answer: c
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Epidemiologic transition stage 3, "Degenerative and human-created
  diseases — ...rise of cardiovascular disease, heart attacks, various cancers."

### PH-M-006
status: verified
answer: b
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-9}
evidence: "Program Trial: evaluates a type of service provided to a population...
  an analytical investigation requiring a control population... Example: an
  intervention program to promote healthy eating and physical activity" — matches
  a community-based intervention tested against control regions.

### PH-M-007
status: verified
answer: a
claimed: a (model 1), d (model 3)
basis: Ch. 5 — Epidemiology and Public Health {#ch05-4}
evidence: "Epidemic: an unusually high occurrence of a disease or illness in a
  population or area" — matches the stem's "specific population or area" directly.
  "Outbreak" specifically requires a small, localized setting (a village or small
  town), not stated in the stem.
note: Model 3's competing claim (Outbreak) is itself the weaker, filled-radio-
  under-stale-badge capture — this is a case where the stronger claim also happens
  to be source-correct.

### PH-M-008
status: verified
answer: a
basis: Ch. 4 — Determinants of Health and Disease {#ch04-7}
evidence: The community-health determinant framework names four factors — Physical,
  Socio-cultural, Community organization, Behavioral — with no genetics category;
  genetics belongs to the separate individual-level "Human biology" determinant
  (§4.3), not this community-level list.

### PH-M-009
status: verified
answer: d
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-6}
evidence: Case-control design: "identify CASES (with disease) and CONTROLS
  (without disease); look backward in time to classify each as E+ or E-" — exactly
  the MMR-vaccine-history-by-disorder-status comparison described.

### PH-M-010
status: verified
answer: a
basis: Ch. 5 — Epidemiology and Public Health {#ch05-4}
evidence: "Endemic: a disease present or usually prevalent in a population at all
  times, in a particular geographical area."

### PH-M-011
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: "Health Disparities: Avoidable differences in the incidence and
  prevalence of health conditions and health status between groups." The other
  three options (individual choice, purely genetic, no long-term impact) all
  contradict this framing.
note: Source's own comparison table reserves "unfair and unjust" specifically for
  "Health Inequities," so option c's wording blurs the two related terms — but it
  is still the best of the four given options by a wide margin.

### PH-M-012
status: verified
answer: b
claimed: c (first pass), b (second pass)
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: Globalization's negative/mixed effects list includes "patent rights
  limiting poor countries' access to technologies" — directly supports reduced,
  not exclusively improved, healthcare access/affordability in low-income
  countries.
note: The second-pass claim (b) is the one the source backs; the first pass (c)
  is wrong.

### PH-M-013
status: verified
answer: c
basis: Ch. 7 — Measures of Association {#ch07-2}
evidence: "RD > 0 = positive association."

### PH-M-014
status: verified
answer: d
basis: Ch. 7 — Measures of Association {#ch07-3}
evidence: "RR > 1 = positive association" — worked example uses an RR of ~20 for
  heavy smoking and lung cancer as "very high, indicating the relationship is not
  likely a chance finding"; RR=25 here reads the same way.

### PH-M-015
status: verified
answer: c
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-4}
evidence: "Design of a Clinical Trial: SAMPLE → randomization to groups...
  Intervention Group and Control Group... measure outcome" — random assignment
  between two vaccines is the defining feature of a clinical trial.

### PH-M-016
status: conflict
answer: c
claimed: b
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-6}/{#ch06-7}
evidence: The structural distinction the source actually draws is how subjects are
  grouped: a cohort study starts "from POPULATION... split into Exposed and
  Unexposed groups," while a case-control study starts by identifying "CASES...and
  CONTROLS" and only classifies exposure status afterward, looking backward. This
  is a definitional difference true regardless of disease timeline. The claimed
  answer (b, "cohort studies require many years") is only conditionally true —
  source frames it as "the main limitation... ESPECIALLY for chronic diseases,"
  not a universal distinguishing feature — and case-control's stated advantage is
  likewise conditional ("efficient IF there's a long delay").
note: The circulating claim isn't unreasonable, but option c states the more
  fundamental, always-true structural difference that source's own design
  descriptions are built around.

### PH-M-017
status: verified
answer: b
basis: Ch. 5 — Epidemiology and Public Health {#ch05-7}
evidence: "Analytical Epidemiology: hypothesis-testing... Answers How? and Why?"

### PH-M-018
status: external
answer: d
basis: external — not covered in source.md
evidence: Source never uses the term "longitudinal design," though its repeated
  "followed forward in time" framing for cohort designs (Ch. 6) is consistent with
  the standard meaning.

### PH-M-019
status: conflict
answer: b
claimed: c
basis: Ch. 7 — Measures of Association {#ch07-4}
evidence: "OR < 1 = negative association." A *significant* negative association
  additionally requires the confidence interval to exclude 1 — standard
  interpretation of the CI convention this source itself uses elsewhere (e.g. "OR
  3.8, 95% CI: 1.6–8.7" as its own example of a reportable OR). Of the four
  options, only b (OR 0.7, CI 0.2–0.8) is both negative (OR<1) and significant (CI
  entirely below 1); the claimed option c (OR 0.3, CI 0.1–1.4) has OR<1 but its CI
  spans 1, so it is not statistically significant.

### PH-M-020
status: verified
answer: a
basis: Ch. 7 — Measures of Association {#ch07-4}
evidence: "OR ≈ RR when: the outcome is rare... cases representative of all cases
  [re. exposure history]... controls representative of all non-cases [re. exposure
  history]." Options b, c and d are three of these exact conditions (d, though
  garbled, echoes "the outcome is rare"); option a ("disease prevalence is high")
  is the opposite of the real condition, making it the one that doesn't belong.

### PH-M-021
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: "Inequality in life expectancy — a key population health measure — is
  therefore one of the foremost measures of health inequality."

### PH-M-022
status: external
answer: b
basis: external — not covered in source.md
evidence: Standard nutrition/food-insecurity mechanism (reliance on cheap,
  high-calorie food); not stated in Ch. 3's food-insecurity passage.

### PH-M-023
status: verified
answer: a
basis: Ch. 5 — Epidemiology and Public Health {#ch05-8}
evidence: "Distal determinants of morbidity and mortality: socio-economic factors
  (personal/household wealth, community development, women's education and
  employment)."

### PH-M-024
status: verified
answer: d
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: The commonly listed SDOH set includes "education, employment,
  income/poverty" alongside "access to resources," matching income/education/
  social support directly.

### PH-M-025
status: verified
answer: b
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Temporal relation | Does the cause precede the effect? (essential)."

### PH-M-026
status: verified
answer: c
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-7}
evidence: Cohort design: "identify relevant group(s) of people and collect
  information about their exposure history; follow these people over time and
  measure incidence of outcome(s)" — matches the enrollment/exposure-tracking/
  cancer-incidence description exactly.

### PH-M-027
status: external
answer: b
basis: external — not covered in source.md
evidence: Standard child-nutrition/development knowledge, not stated in Ch. 3.

### PH-M-028
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: "Health Disparities: ...differences in the incidence and prevalence of
  health conditions and health status between groups" — matches "inequalities...
  among different population groups."

### PH-M-029
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: "The crucial test of whether a resulting health difference is 'unfair'
  turns largely on whether people chose the situation... or whether it was mainly
  out of their direct control" — differences out of anyone's control are the
  "inevitable"/acceptable ones in this framework.

### PH-M-030
status: verified
answer: c
basis: Ch. 5 — Epidemiology and Public Health {#ch05-2}
evidence: The five uses of epidemiology include describing natural history,
  identifying risk factors, and community diagnosis — options a, b and d are all
  genuine listed uses, making "all of the answer are correct" the right choice.

### PH-M-031
status: verified
answer: c
basis: Ch. 5 — Epidemiology and Public Health {#ch05-9}
evidence: The 5 Rubrics' first entry, "Quantity — 'How many?': how many people in
  the population are affected as cases... or becoming cases" — this is the rubric
  for measuring a disease's magnitude of impact on a population.

### PH-M-032
status: verified
answer: d
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-1}
evidence: The hierarchy of evidence ranks Cohort Studies above Case Control
  Studies for demonstrating cause and effect (Randomized Controlled Trial ranks
  higher still, but isn't offered as an option here).

### PH-M-033
status: verified
answer: d
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-2}
evidence: SDG 3's actual targets read "(1) reduce maternal mortality ratio" and
  "(2) end preventable deaths of children under 5" and "(3) end epidemics" — the
  maternal-mortality target is phrased as *reducing*, not *ending*, the ratio,
  unlike the other three options' "end"-framed wording.
note: This is a fine phrasing distinction rather than a clean-cut fact; all four
  options are technically SDG3 sub-targets, not standalone SDGs.

### PH-M-034
status: verified
answer: b
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Demographic-transition Stage 1: "high birth and death rates... high
  rates of communicable disease" — matching high infectious-disease mortality with
  no effective interventions.

### PH-M-035
status: verified
answer: a
basis: Ch. 7 — Measures of Association {#ch07-4}
evidence: Comparing an exposure (obesity) between a disease-positive (MI) and
  disease-negative group is the classic case-control-style comparison, for which
  odds ratio is the standard measure.

### PH-M-036
status: verified
answer: a
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Dose-response relationship: occurs when changes in the level of a
  possible cause are associated with changes in the prevalence/incidence of the
  effect."

### PH-M-037
status: verified
answer: b
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Demographic-transition Stage 2: "high birth rates (>30) but declining
  death rates."

### PH-M-038
status: verified
answer: b
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-2}
evidence: "Necessary cause: a disease cannot develop in the absence of this
  cause" — removing it means the disease cannot occur.

### PH-M-039
status: external
answer: b
basis: external — not covered in source.md
evidence: An odds ratio reported alone, without a confidence interval, doesn't by
  itself establish whether the observed difference is real or due to chance —
  standard statistical-literacy point; source states the OR>1/=1/<1 rules (Ch. 7)
  but doesn't explicitly discuss a bare point estimate's limits this way.

### PH-M-040
status: verified
answer: d
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-8}
evidence: "Cross-sectional (prevalence) study: ...based on prevalence data...
  efficient for describing target-population characteristics" — matches
  identifying the proportion of the population with the disease.

### PH-M-041
status: conflict
answer: a
claimed: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: The WHO/CDC definition of social determinants of health is "the
  circumstances in which people are born, grow up, live, work, and age" — this is
  option a's wording almost verbatim ("born, live, learn, work, play, worship, and
  age"). Option b (the claimed answer) explicitly includes "genetics," but genetics
  is one of the classic 5 determinant *categories* source lists separately from
  socioeconomic/social determinants — genetics is not itself a social determinant.

### PH-M-042
status: verified
answer: b
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-3}
evidence: "Social health — the ability to make and maintain acceptable
  interactions with other people... creating and maintaining friendship and
  intimacy."

### PH-M-043
status: external
answer: a
claimed: b
basis: external — not covered in source.md
evidence: "Assess the strength and direction of a linear relationship between two
  variables" is the standard definition of the Pearson correlation coefficient —
  an odds ratio (the claimed answer) measures association between an exposure and
  a categorical outcome, not a linear relationship between two continuous
  variables. Source's Ch. 7 covers OR/RR/RD but never defines Pearson correlation,
  so this stays outside the source rather than a same-chapter conflict.

### PH-M-044
status: verified
answer: c
basis: Ch. 7 — Measures of Association {#ch07-4}
evidence: "4 times more likely" is a direct restatement of an odds ratio of 4 —
  no 2×2 table needed when the ratio is handed to you directly in these terms.

### PH-M-045
status: verified
answer: a
basis: Ch. 5 — Epidemiology and Public Health {#ch05-9}
evidence: The 5 Rubrics' second entry, "Location — 'Where?': where in the
  population are affected cases more likely to be found" — matches geographical
  distribution and clustering directly.

### PH-M-046
status: external
answer: a
basis: external — not covered in source.md
evidence: The stem's own wording ("compare the DIFFERENCE") names the intended
  measure directly, but comparing a continuous outcome (vital capacity) between
  two groups via risk difference is a stretch of the RD/RR/OR framework, which
  Ch. 7 builds entirely around binary disease outcomes — a design flaw in the
  question itself, not something source resolves cleanly either way.

### PH-M-047
status: verified
answer: c
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-2}
evidence: Rothman & Greenland's definition of "cause" (an event/condition that
  preceded the disease and without which it wouldn't have occurred) combined with
  "sufficient cause... inevitably produces" describes something both necessary and
  sufficient — "causal factor" is the closest of the four options to this general
  sense of cause.

### PH-M-048
status: verified
answer: d
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: The shift into Stage 2 (the Epidemiologic Transition) is "driven by:
  agricultural technology, improved food supply, better medical understanding of
  disease causes/spread, public sanitation technology" — broadly, advances in
  medical technology and public health infrastructure.

### PH-M-049
status: verified
answer: b
claimed: b
basis: Ch. 5 — Epidemiology and Public Health {#ch05-1}
evidence: Box 1.2's "Health-related states and events" entry covers diseases,
  causes of death, and related events broadly — consistent with "an incident that
  impacts the health and well-being of individuals or populations."

### PH-M-050
status: verified
answer: a
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Demographic-transition "Stage 1, 'Pre-Industrial': high birth and
  death rates (both ~40)."

### PH-M-051
status: verified
answer: d
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: Income/poverty is explicitly listed among the socioeconomic-adjacent
  SDOH set.

### PH-M-052
status: verified
answer: a
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Temporal relation | Does the cause precede the effect?" — the
  time-sequence requirement.

### PH-M-053
status: verified
answer: b
basis: Ch. 5 — Epidemiology and Public Health {#ch05-1}
evidence: Box 1.2, "Study | includes surveillance, observation, hypothesis
  testing, analytic research" — collecting/analyzing disease-occurrence data.

### PH-M-054
status: verified
answer: b
basis: Ch. 5 — Epidemiology and Public Health {#ch05-9}
evidence: The 5 Rubrics' third entry, "Causes — 'Why?': what accounts for some
  people becoming affected and not others?" — matches "risk factors and
  determinants."

### PH-M-055
status: verified
answer: a
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Demographic-transition Stage 2: "rate of natural increase rises sharply
  (population explosion), growing throughout the stage."

### PH-M-056
status: verified
answer: b
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: Negative globalization effects include "diseases of dietary excess
  driven by marketing → widespread urban obesity."

### PH-M-057
status: verified
answer: c
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-6}
evidence: The Public Health Model vs. Medical Model table assigns "Disease
  Prevention" to the public-health column and "Diagnosis"/"Treatment" to the
  medical-model column — prevention is explicitly not a medical-model activity.

### PH-M-058
status: not-in-source
basis: —
evidence: This specific "why health as a right matters" rationale list doesn't
  appear in any of the 16 chapters.

### PH-M-059
status: verified
answer: b
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Plausibility: is the association consistent with other knowledge?
  (mechanism of action...)" — biological plausibility is exactly this criterion.

### PH-M-060
status: verified
answer: c
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: Demographic-transition Stage 2: "high birth rates (>30) but declining
  death rates (to ~20)."

### PH-M-061
status: verified
answer: b
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: The 9-item Bradford Hill Criteria list includes "(4) Temporality" by
  name; none of the other three options (cross-sectional design, face validity,
  convenience) is a Hill criterion.

### PH-M-062
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-4}
evidence: Environment category "(a) life support (food, water, air, etc.)" —
  safe drinking water access is a classic environmental determinant.

### PH-M-063
status: verified
answer: d
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-6}
evidence: The breast-cancer causal-pie example lists the BRCA1 gene as one
  component cause among several (early menarche, late first birth, HRT) —
  genetics contributing as one component of a sufficient cause, not as a
  sufficient cause on its own.

### PH-M-064
status: verified
answer: a
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-4}
evidence: "Before an association is assessed for causality, other explanations —
  chance, bias, confounding — must first be excluded" — confounding is explicitly
  named as a source of bias in causal assessment.

### PH-M-065
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: The Health Disparities examples list "Race/ethnicity" first among
  affected groups.

### PH-M-066
status: verified
answer: d
basis: Ch. 7 — Measures of Association {#ch07-3}
evidence: "RR < 1 = negative association" — an RR of 0.8 for the first routine
  relative to the second indicates the first is associated with lower risk of the
  health issue, i.e. more effective at reducing it.

### PH-M-067
status: verified
answer: a
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Consistency" appears in both the Table 5.1 and 9-item Bradford Hill
  lists; sample size, face validity, and convenience are not Hill criteria.

### PH-M-068
status: verified
answer: c
basis: Ch. 5 — Epidemiology and Public Health {#ch05-7}
evidence: "Descriptive Epidemiology: examines the distribution of a
  disease/behavior/state of health... observing the features of its distribution
  by person, place and time" — the basic patterns and features of a health event.

### PH-M-069
status: verified
answer: d
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: Temporality/temporal relation is a genuine causation guideline in both
  source lists; the other three options describe methodological flaws, not
  guidelines.

### PH-M-070
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: WHO (2008): "absence of unfair and avoidable... differences in health
  among population groups" and "no one should be disadvantaged from achieving
  [full health potential]" — reducing disparities and ensuring fair opportunity.

### PH-M-071
status: verified
answer: d
basis: Ch. 7 — Measures of Association {#ch07-3}
evidence: "RR > 1 = positive association" — a direct restatement of a 1.2-fold
  increased risk.

### PH-M-072
status: verified
answer: d
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: Negative globalization effects list "worldwide travel and spread of
  infectious disease."

### PH-M-073
status: verified
answer: a
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Consistency: demonstrated when several studies give the same results...
  observed repeatedly by different persons, in different places, circumstances and
  times" — matches "replicated in different populations and settings" closely.

### PH-M-074
status: verified
answer: b
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: Positive globalization effects include cross-border benefits like
  improved information/resource flow; international medical expertise access
  during a health crisis fits this framing (loosely — not a verbatim source
  example).

### PH-M-075
status: verified
answer: c
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-5}
evidence: "Dose-response relationship: occurs when changes in the level of a
  possible cause are associated with changes in the prevalence/incidence of the
  effect" — restated as the relationship between exposure and disease risk.

### PH-M-076
status: verified
answer: b
basis: Ch. 5 — Epidemiology and Public Health {#ch05-3}
evidence: "Prevalence = the proportion of individuals in a population who have a
  disease at a particular time (also called point prevalence)."

### PH-M-077
status: verified
answer: a
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-3}
evidence: "Mental and intellectual health — the ability to learn and think
  clearly and coherently."

### PH-M-078
status: external
answer: c
basis: external — not covered in source.md
evidence: None of the four options (access to healthcare, genetics, SES, air
  quality) is source's own actual answer for chronic-disease risk (behavioral/
  lifestyle determinants, per Table 2.9.1) — socioeconomic status is the closest
  fit among the given options via its behavioral-determinant pathway, but this is
  a judgment call given the flawed option set.

### PH-M-079
status: verified
answer: b
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: "New shocks (climate change, conflict, pests..., infectious disease)
  hurt food production and disrupt supply chains" — land degradation fits this
  same shock-to-food-security pattern.

### PH-M-080
status: verified
answer: a
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: Health inequality (WHO): "the differences in health status... between
  different population groups" — disparities among groups are the definitional
  outcome of health inequality.

### PH-M-081
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: Matches the general SDOH framing directly (circumstances/conditions
  that contribute to or detract from health).

### PH-M-082
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-5}
evidence: Table 2.9.1's behavioural determinants column includes diet
  ("high-fat diet," "low-fibre diet") explicitly; age, pollution, and social norms
  are not behavioral determinants in this framework.

### PH-M-083
status: verified
answer: a
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-2}
evidence: "Alma-Ata Declaration (Alma-Ata, Kazakhstan, September 1978): stated
  health is a basic human right."

### PH-M-084
status: verified
answer: d
basis: Ch. 8 — Causal Thinking in Epidemiology {#ch08-6}
evidence: "Necessary cause: a component cause that is a member of *every*
  sufficient cause" (present in every causal pie) vs. an ordinary "component
  cause: any one of the set of conditions necessary for completion of a
  sufficient cause" (contributes to risk without being present in every pathway).

### PH-M-085
status: verified
answer: d
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-1}
evidence: WHO (1986): "health is the extent to which an individual or group is
  able... to realize aspirations and safety needs, and... to change or cope with
  the environment. It is to be seen as a resource for everyday life" — matches
  option d closely; option c is actually the WHO 1948 definition, a distractor.

### PH-M-086
status: verified
answer: d
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-6}
evidence: The Public Health Model vs. Medical Model table assigns individual
  clinical treatment (like a heart transplant) to the Medical Model column, not
  Public Health's population-level prevention/promotion focus.

### PH-M-087
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-2}
evidence: The Force Field paradigm names exactly these four: "(A) Human biology,
  (B) Environment, (C) Lifestyle behaviour, (D) Health care organization."

### PH-M-088
status: verified
answer: c
basis: Ch. 2 — History and Mission of Public Health {#ch02-7}/{#ch02-8}
evidence: Multi-Causal Theory (option c) is a genuine 20th-century model
  (§2.8) — options a (Miasma) and b (Supernatural) are 19th-century models
  (§2.7), so "all of the above" (d) is wrong.

### PH-M-089
status: verified
answer: d
basis: Ch. 2 — History and Mission of Public Health {#ch02-5}
evidence: "Louis Pasteur... In 1862 he showed germs caused many diseases; in
  1888 he established the first public health laboratory."

### PH-M-090
status: verified
answer: d
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: The seven determinants of health differentials list health-damaging
  behavior, exposure to unhealthy/stressful conditions, and inadequate access to
  services as genuine determinants — but "differences in incidence/prevalence...
  between groups" (option d) is the *definition* of the resulting disparity, not
  a determinant that produces it.

### PH-M-091
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-7}
evidence: "Physical determinants: geography (highland vs. lowland), environment
  (man-made or natural catastrophes), industrial development (pollution,
  occupational hazards)" — matches the stem verbatim.

### PH-M-092
status: verified
answer: a
basis: Ch. 14 — Measuring the Health of a Population {#ch14-4}
evidence: "MMR = Number of Maternal Deaths / Number of live births × 100,000."

### PH-M-093
status: verified
answer: c
basis: Ch. 14 — Measuring the Health of a Population {#ch14-4}
evidence: Infant mortality is standardly expressed "per 1,000... live births" in
  this source's own worked figures (e.g. Palestine's IMR table).

### PH-M-094
status: verified
answer: a
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-4}
evidence: The Epidemiologic Transition tracks the shift from infectious-disease
  to degenerative/chronic-disease mortality as its central subject.

### PH-M-095
status: verified
answer: d
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: Matches the general determinants-of-health framing (social, economic,
  physical, environmental factors shaping community well-being).

### PH-M-096
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: "Health Inequities: Systematic and unjust distribution of social,
  economic, and environmental conditions needed for health" — the unfair/unjust
  framing belongs to inequity specifically, distinguishing it from disparity.

### PH-M-097
status: verified
answer: a
basis: Ch. 2 — History and Mission of Public Health {#ch02-7}
evidence: "Miasma theory — 'bad air'; disease caused by the odor of decaying
  organic material."

### PH-M-098
status: verified
answer: b
basis: Ch. 2 — History and Mission of Public Health {#ch02-2}
evidence: Ancient Greece "rejected supernatural theory of disease" — "disease
  was the punishment of God" is exactly the supernatural theory Hippocrates'
  naturalistic approach rejected, not something credited to him.

### PH-M-099
status: verified
answer: b
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: The equity-in-health framework (§4.8) frames SDOH's central concern as
  reducing inequity — "no one should be disadvantaged... if avoidable" — more
  than the multi-sectoral or medical-treatment framings in the other options.

### PH-M-100
status: verified
answer: a
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-3}
evidence: "The health continuum: health is dynamic, viewed as a continuum
  running Death → Sickness → Health → Optimum Health."

### PH-M-101
status: verified
answer: c
basis: Ch. 2 — History and Mission of Public Health {#ch02-6}
evidence: The Ten Great Achievements in Public Health 1900–1999 list (seat-belt-
  adjacent motor-vehicle safety, tobacco recognition, and vaccines are all on it)
  does not include CT scan discovery.

### PH-M-102
status: verified
answer: b
basis: Ch. 10 — Screening {#ch10-6}
evidence: "A test with high sensitivity will identify a high percentage of the
  cases with the outcome" — sensitivity is about catching a high share of true
  cases, not a perfect share.

### PH-M-103
status: verified
answer: d
basis: Ch. 2 — History and Mission of Public Health {#ch02-5}
evidence: Same Louis Pasteur passage as PH-M-089 — "first scientific approach to
  immunization and pasteurization."

### PH-M-104
status: verified
answer: a
basis: Ch. 4 — Determinants of Health and Disease {#ch04-1}
evidence: Same SDOH definitional match as PH-M-081/095.

### PH-M-105
status: verified
answer: a
basis: Ch. 5 — Epidemiology and Public Health {#ch05-9}
evidence: "The Analytical Epidemiological Triad — Host, Agent, Environment."

### PH-M-106
status: verified
answer: a
basis: Ch. 10 — Screening {#ch10-5}
evidence: Criteria for the disease being screened requires "a high burden and of
  high public-health concern" — a rare disease with a long asymptomatic period is
  the opposite of what makes screening worthwhile; source's own criteria call for
  a common, high-prevalence condition.

### PH-M-107
status: verified
answer: c
basis: Ch. 4 — Determinants of Health and Disease {#ch04-8}
evidence: Same Health Disparities definition as PH-M-011/028.

### PH-M-108
status: verified
answer: b
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-7}
evidence: Recruiting by exposure status (HIV) and following forward for an
  outcome (mortality) over ten years is a textbook cohort design.

### PH-M-109
status: verified
answer: a
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-6}
evidence: "Strengths: well suited to study the etiology of rare outcomes."

### PH-M-110
status: verified
answer: a
basis: Ch. 14 — Measuring the Health of a Population {#ch14-5}
evidence: "Prevalence rate = Number of people with the disease at a specific
  time / Number of people in the population at-risk at that time."

### PH-M-111
status: verified
answer: d
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-7}
evidence: "Cohort... provides a direct measure of risk of outcome among exposed
  and unexposed persons" — the design that directly measures incidence.

### PH-M-112
status: verified
answer: b
basis: Ch. 2 — History and Mission of Public Health {#ch02-8}
evidence: "Emphasizes the interrelatedness of many variables... principally
  those under the individual's control" is the Life Style Theory's definition,
  not the Environmental Theory's (which is about toxins and industrial
  production) — a conflation between the two 20th-century models.

### PH-M-113
status: needs-eye
answer: —
basis: —
evidence: No options were ever captured for this question (the source photo cuts
  off right after the stem) — genuinely unanswerable without the missing content,
  carried forward from Job A's own needs-eye flag rather than resolved here.

### PH-M-114
status: verified
answer: b
basis: Ch. 6 — Designs of Epidemiologic Studies {#ch06-7}
evidence: Same cohort-design match as PH-M-108 (a duplicate-style scenario
  question in this batch).

### PH-M-115
status: verified
answer: c
basis: Ch. 14 — Measuring the Health of a Population {#ch14-5}
evidence: "Factors that increase observed prevalence: ...prolongation of life
  without cure" — improved treatment raises observed prevalence via longer
  survival with the disease, the classic explanation for this exact question
  type.

### PH-M-116
status: verified
answer: b
basis: Ch. 14 — Measuring the Health of a Population {#ch14-5}
evidence: Incidence's denominator is "persons AT RISK of developing the disease"
  — the group that could experience the outcome under study.

### PH-M-117
status: verified
answer: d
basis: Ch. 2 — History and Mission of Public Health {#ch02-4}
evidence: "Dr. James Lind discovered scurvy could be controlled by lime juice."

### PH-M-118
status: verified
answer: c
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: "The world is more economically interconnected" — globalization framed
  throughout as increasing interdependence among nations/individuals.

### PH-M-119
status: verified
answer: d
basis: Ch. 9 — Levels of Prevention {#ch09-5}
evidence: Managing an already-diagnosed cancer's progression/recurrence is
  tertiary prevention's domain (disability limitation and rehabilitation, applied
  once disease is present).

### PH-M-120
status: verified
answer: b
basis: Ch. 9 — Levels of Prevention {#ch09-4}
evidence: "Secondary prevention: ...early diagnosis... and adequate treatment" —
  treating already-detected diabetes matches directly.

### PH-M-121
status: verified
answer: a
basis: Ch. 9 — Levels of Prevention {#ch09-2}
evidence: "Primordial prevention begins in childhood... parents, teachers and
  peer groups are important in shaping children's health education" — population-
  wide sanitation/community/childhood-lifestyle measures match primordial, not
  primary, prevention.

### PH-M-122
status: verified
answer: a
basis: Ch. 10 — Screening {#ch10-3}
evidence: "Purpose of Screening: reducing disease burden; classifying people by
  likelihood of having a particular disease" — case detection (true positives) is
  screening's central aim.

### PH-M-123
status: verified
answer: c
basis: Ch. 10 — Screening {#ch10-6}
evidence: "Positive Predictive Value (PPV) = TP / (TP+FP) — proportion of true
  positives among all those with a positive screening test" — the probability of
  actually having the disease given a positive test.

### PH-M-124
status: verified
answer: a
basis: Ch. 10 — Screening {#ch10-6}
evidence: Ensuring only truly HIV-negative subjects are enrolled requires
  correctly catching nearly all true positives so none slip through as false
  negatives — this requires high sensitivity (TP/(TP+FN)).

### PH-M-125
status: verified
answer: a
basis: Ch. 10 — Screening {#ch10-6}
evidence: Reconstructing the 2×2 table from the stem (TP=10, FP=5, FN=15, TN=20):
  Sensitivity = TP/(TP+FN) = 10/25.

### PH-M-126
status: verified
answer: d
basis: Ch. 10 — Screening {#ch10-6}
evidence: Same table as PH-M-125: Specificity = TN/(TN+FP) = 20/25.

### PH-M-127
status: verified
answer: b
basis: Ch. 10 — Screening {#ch10-6}
evidence: Same table: PPV (chance your own positive diagnosis is correct) =
  TP/(TP+FP) = 10/15.

### PH-M-128
status: verified
answer: d
basis: Ch. 10 — Screening {#ch10-6}
evidence: Same table: NPV (chance your own negative diagnosis — "normal
  eardrum" — is correct) = TN/(TN+FN) = 20/35.

### PH-M-129
status: verified
answer: d
claimed: d (PYQ bank, PH-P-034)
basis: Ch. 16 — Health Care System in Palestine {#ch16-10}
evidence: Palestine's insurance system centers on public (government) health
  insurance covering employees, families and children under 3; source's own
  provider framework (§16.8) puts the MoH as the main provider.

### PH-M-130
status: verified
answer: a
claimed: a (PYQ bank, PH-P-035)
basis: Ch. 9 — Levels of Prevention {#ch09-1}
evidence: Prevention's definition matches this framing (actions to promote,
  preserve, restore health, and minimize suffering).

### PH-M-131
status: not-in-source
claimed: c (PYQ bank, PH-P-036)
basis: —
evidence: "Global Health" as a distinct topic/rationale list isn't covered by
  this course's 16 chapters.

### PH-M-132
status: external
answer: b
claimed: b (PYQ bank, PH-P-037)
basis: external — not covered in source.md
evidence: General systems theory: a functional system needs regulated, not
  "completely open," boundaries to self-regulate and differentiate — not covered
  in this source, but standard systems-theory reasoning consistent with the claim.

### PH-M-133
status: verified
answer: c
claimed: c (PYQ bank, PH-P-038)
basis: Ch. 12 — Primary Health Care {#ch12-3}
evidence: "Additional elements incorporated after Alma-Ata: ...acute respiratory
  infection (ARI)."

### PH-M-134
status: verified
answer: b
claimed: b (PYQ bank, PH-P-039)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-2}
evidence: All four named items (poverty/hunger eradication, combating HIV/
  malaria, maternal health, child mortality) are genuine MDGs.

### PH-M-135
status: external
answer: d
claimed: d (PYQ bank, PH-P-040)
basis: external — not covered in source.md
evidence: Standard poverty/health association (malnutrition, lower life
  expectancy, higher infant mortality) — not explicitly enumerated in Ch. 3.

### PH-M-136
status: external
answer: d
basis: external — not covered in source.md
evidence: Standard family-typology terminology (single-parent family); no claim
  recorded on either side (PYQ's own copy is also unanswered).

### PH-M-137
status: verified
answer: a
claimed: a (PYQ bank, PH-P-043)
basis: Ch. 2 — History and Mission of Public Health {#ch02-7}
evidence: This description ("odor of decaying organic material") is the Miasma
  theory's definition, not Supernatural theory's ("disease is a punishment for
  transgression of God's laws") — the statement as attributed to Supernatural
  theory is False, matching the claim.

### PH-M-138
status: not-in-source
claimed: d (PYQ bank, PH-P-044)
basis: —
evidence: "Development" as a distinct concept/definition isn't covered by this
  course's 16 chapters.

### PH-M-139
status: conflict
answer: a
claimed: b
basis: Ch. 16 — Health Care System in Palestine {#ch16-9}
evidence: Palestine's own Distribution of Medical Human Resources table shows
  Nurses (14,593) outnumbering Physicians (11,313) — physicians are not the
  largest employed group in public health, at least by this source's own
  workforce data.

### PH-M-140
status: not-in-source
claimed: a (PYQ bank, PH-P-046)
basis: —
evidence: Community-participation dynamics in health programs aren't covered by
  the 16 chapters.

### PH-M-141
status: external
answer: a
claimed: a (PYQ bank, PH-P-047)
basis: external — not covered in source.md
evidence: Standard (Tylor-style) anthropological definition of culture — not in
  this source.

### PH-M-142
status: verified
answer: a
claimed: a (PYQ bank, PH-P-048)
basis: Ch. 2 — History and Mission of Public Health {#ch02-2}
evidence: "Hippocrates (b. 460 BC) — 'Father of Western medicine'" — not eastern.

### PH-M-143
status: verified
answer: d
claimed: d (PYQ bank, PH-P-049)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-5}
evidence: Winslow (1920): "The science and art of preventing disease, prolonging
  life, and promoting health through the organized efforts..." matches option d
  word for word.

### PH-M-144
status: external
answer: a
claimed: a (PYQ bank, PH-P-050)
basis: external — not covered in source.md
evidence: Loosely consistent with the "psycho-social" environment category
  (§4.4), but not stated explicitly this way in source.

### PH-M-145
status: verified
answer: b
claimed: b (PYQ bank, PH-P-051)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-3}
evidence: "Emotional health — the ability to express emotions appropriately
  (fear, happiness, anger)" — this is emotional health's own definition, not
  spiritual health's, so the statement as attributed to spiritual health is False.

### PH-M-146
status: not-in-source
claimed: d (PYQ bank, PH-P-052)
basis: —
evidence: DSM disease classification isn't covered by this source.

### PH-M-147
status: not-in-source
claimed: a (PYQ bank, PH-P-053)
basis: —
evidence: Clinical mental-disorder definitions aren't covered by this source.

### PH-M-148
status: external
answer: e
claimed: e (PYQ bank, PH-P-054)
basis: external — not covered in source.md
evidence: Sub-Saharan Africa having the shortest life expectancy is standard
  global-health knowledge, broadly consistent with this source's own Ch. 15
  infectious-disease-burden data (Africa carries by far the largest share), but
  not stated as a life-expectancy ranking directly.

### PH-M-149
status: not-in-source
claimed: a (PYQ bank, PH-P-055)
basis: —
evidence: Family-development-task stages aren't covered by this source.

### PH-M-150
status: external
answer: d
claimed: d (PYQ bank, PH-P-056)
basis: external — not covered in source.md
evidence: Health's role in economic development and poverty reduction is
  touched by Ch. 3 ("a healthy population is also a driver of growth"), but "all
  of them" (including "disease development" as a positive role) isn't a clean
  source match.

### PH-M-151
status: needs-eye
answer: —
basis: Ch. 2 — History and Mission of Public Health {#ch02-7}
evidence: Two of the five options are genuinely correct 19th-century models —
  Miasma theory (c) and Supernatural theory (e) — while "the Environmental
  theory" (b) is actually a *20th*-century model per §2.8, ruling out "all of
  them" (d) as well. The question's own handwritten margin note ("there are two
  correct answers") is independently confirmed by this source check — the
  question is structurally ambiguous, not just visually.
note: No single letter answer is defensible; carried forward as needs-eye rather
  than forced to one option. No PYQ counterpart exists for cross-reference.

### PH-M-152
status: not-in-source
claimed: b (PYQ bank, PH-P-057)
basis: —
evidence: Decentralization as a governance concept isn't defined in this
  source's 16 chapters (Ch. 12's PHC principles mention "decentralization" as a
  requirement by name but don't define the term itself).

### PH-M-153
status: verified
answer: a
claimed: a (PYQ bank, PH-P-058)
basis: Ch. 2 — History and Mission of Public Health {#ch02-7}
evidence: "Rejected because too many people became ill regardless of isolation
  from human contact" — matches the stem's exact reasoning.

### PH-M-154
status: verified
answer: c
claimed: c (PYQ bank, PH-P-059)
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: "Effects of globalization can be positive, negative, or mixed."

### PH-M-155
status: verified
answer: b
claimed: b (PYQ bank, PH-P-060)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-6}
evidence: The 11 core activities of public health include mobilizing community
  action, promoting healthy behaviors, and providing conditions conducive to
  health — all of the listed options are genuine core activities.

### PH-M-156
status: verified
answer: b
claimed: b (PYQ bank, PH-P-061)
basis: Ch. 5 — Epidemiology and Public Health {#ch05-3}
evidence: Epidemiology's own key-terms framing centers on exactly "distribution"
  and "determinants" of disease in populations.

### PH-M-157
status: not-in-source
claimed: c (PYQ bank, PH-P-062)
basis: —
evidence: Genuinely ambiguous against source: "reorientation of health
  manpower" appears in the PHC *Strategy* section (§12.5) even though not in the
  explicit 8-item Principles list (§12.3), while "inter-relationship of health
  and development" doesn't appear anywhere in the PHC chapter — not confidently
  resolvable to one option from source content.

### PH-M-158
status: conflict
answer: a
claimed: b
basis: Ch. 16 — Health Care System in Palestine {#ch16-3}
evidence: Universal Health Coverage's pooling logic — "the wealthy & healthy
  subsidize the poor & sick" — is precisely the standard health-financing
  argument that broad-based (universal) programs sustain wider political and
  financial support than schemes narrowly targeting the poor, unlike the claimed
  False.

### PH-M-159
status: verified
answer: b
claimed: b (PYQ bank, PH-P-064)
basis: Ch. 14 — Measuring the Health of a Population {#ch14-4}
evidence: Infant mortality is standardly expressed per 1,000 live births.

### PH-M-160
status: verified
answer: f
claimed: f (PYQ bank, PH-P-065)
basis: Ch. 16 — Health Care System in Palestine {#ch16-8}
evidence: All named providers (MoH/security forces, UNRWA, NGOs, private sector)
  are the genuine five providers of health care in Palestine.

### PH-M-161
status: verified
answer: d
claimed: d (PYQ bank, PH-P-066)
basis: Ch. 4 — Determinants of Health and Disease {#ch04-7}
evidence: "Socio-cultural determinants: beliefs, traditions, social customs;
  economy, politics, religion in the community" — matches the stem verbatim.

### PH-M-162
status: external
answer: a
claimed: a (PYQ bank, PH-P-067)
basis: external — not covered in source.md
evidence: Loosely consistent with Ch. 12's "intersectoral coordination" PHC
  principle, but not defined this precisely in source.

### PH-M-163
status: external
answer: b
claimed: b (PYQ bank, PH-P-068)
basis: external — not covered in source.md
evidence: John Snow "founded modern epidemiology" (Ch. 2 §2.5) is the closest
  "founding father" framing among the options, though the "George Washington of
  Public Health" nickname itself isn't in this source.

### PH-M-164
status: verified
answer: d
claimed: d (PYQ bank, PH-P-069)
basis: Ch. 12 — Primary Health Care {#ch12-3}
evidence: The PHC essential-services list includes health education, food
  supply/nutrition, MCH/family planning, immunization, and communicable-disease
  control — matching all the listed combined options.

### PH-M-165
status: verified
answer: b
claimed: b (PYQ bank, PH-P-070)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-2}
evidence: Closest available match among the four options, though the
  "interconnected and mutually reinforcing goals for sustainable development"
  phrasing more precisely describes the SDGs (source's own SDG framing) than the
  MDGs — SDGs simply isn't offered as a choice here.
note: A genuine terminology tension in the source question itself, not fully
  resolvable to a clean match — kept as the best available option.

### PH-M-166
status: not-in-source
claimed: a (PYQ bank, PH-P-071)
basis: —
evidence: Mental-illness stigma/social-exclusion effects on mental-health course
  aren't covered by this source.

### PH-M-167
status: verified
answer: b
claimed: b (PYQ bank, PH-P-072)
basis: Ch. 2 — History and Mission of Public Health {#ch02-4}
evidence: Industrialization/urbanization intensified public-health strain
  (crowding, poor hygiene) that the later Great Sanitary Awakening had to
  address — it didn't itself solve public-health problems.

### PH-M-168
status: verified
answer: a
claimed: a (PYQ bank, PH-P-073)
basis: Ch. 3 — Expanding the Concept of Public Health {#ch03-3}
evidence: This "total person... psychic and environmental requirements" framing
  describes general "Development," not narrowly "Economic Growth," which source
  frames specifically around GDP/poverty reduction — the statement as attributed
  to Economic Growth is False, matching the claim.

### PH-M-169
status: verified
answer: d
claimed: d (PYQ bank, PH-P-074)
basis: Ch. 12 — Primary Health Care {#ch12-3}
evidence: "Additional elements incorporated after Alma-Ata: oral health, mental
  health, use of traditional medicine, occupational health, HIV/AIDS, ARI" —
  "Social health" is not on this list (mental health is, but not social health
  specifically).

### PH-M-170
status: conflict
answer: b
claimed: a
basis: Ch. 2 — History and Mission of Public Health {#ch02-8}
evidence: "Prevention through change in industrial production rather than
  medical treatment/personal hygiene" is the Environmental Theory's definition
  (§2.8), not the Multi-Causal Theory's (which is about a "web" of multiple
  contributing factors, with no such industrial-production framing) — the
  statement as attributed to Multi-Causal Theory is False.

### PH-M-171
status: not-in-source
claimed: e (PYQ bank, PH-P-076)
basis: —
evidence: Barriers to community involvement in health programs aren't covered
  by this source.

### PH-M-172
status: not-in-source
claimed: a (PYQ bank, PH-P-077)
basis: —
evidence: Family as the primary context for health promotion isn't covered by
  this source.

### PH-M-173
status: not-in-source
claimed: a (PYQ bank, PH-P-078)
basis: —
evidence: Community-participation typology (structural/horizontal/substantial)
  isn't covered by this source.

### PH-M-174
status: not-in-source
claimed: b (PYQ bank, PH-P-079)
basis: —
evidence: Family psychological-needs/dysfunction content isn't covered by this
  source.

### PH-M-175
status: not-in-source
claimed: d (PYQ bank, PH-P-080)
basis: —
evidence: Consequences of dysfunctional families/poor parenting aren't covered
  by this source.

### PH-M-176
status: not-in-source
claimed: b (PYQ bank, PH-P-081)
basis: —
evidence: "Appropriate technology" criteria (efficient/equitable/sustainable/
  affordable) aren't defined by this source — Ch. 11's OOPP content is adjacent
  (project planning) but doesn't cover this specific framework.

### PH-M-177
status: verified
answer: a
claimed: a (PYQ bank, PH-P-082)
basis: Ch. 1 — Introduction to Health and Public Health {#ch01-5}
evidence: Institute of Medicine's mission framing, quoted verbatim: "Fulfilling
  society's interest in assuring conditions in which people can be healthy."
note: Source attributes this quote to public health's mission generally (IOM),
  not specifically to "Health Promotion" — accepted given how closely this
  course frames health promotion as central to modern public health (Ch. 13
  opens by subtitling Health Promotion "The new public health").
