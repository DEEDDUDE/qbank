---
course: public-health
tab: midterm
questions: 84
tiers: claimed 46 | open 38
forms: mcq 84
needs-eye: 5
disputed: 3
next-id: PH-M-085
---

First extraction for this tab — `PH-M-` IDs start at 001. Scope: `raw/midterm/2023/`,
all three reshuffled models of the 2023 sitting. نموذج ١ (45 questions,
PH-M-001–045) and نموذج ٣ (32 questions captured, 18 new after merging by stem —
PH-M-046–063) were extracted in an earlier session; this session added نموذج ٢ (34
vision pages, all 45 questions covered though captured out of question-number order),
merging 24 of its questions into existing entries and adding 21 new ones
(PH-M-064–084).

Reshuffled models of one 2023 sitting, merged by stem text per the exception in
job-a-extract.md (same technique as microbiology finals نموذج 1/5). نموذج ١ is a
live attempt (every question "Answer saved") shot off a laptop screen at an angle —
several stems are cut off at the right edge by the photo frame itself, confirmed by
re-rendering the source PDF pages at 3x resolution: the missing text is outside the
photographed area, not a downscale/blur artifact, so it cannot be recovered from this
same file. Where نموذج ٣ or نموذج ٢ captured the same stem in full it is used to
complete the text (noted per-entry); where none did, the entry is `needs-eye: true`
with a crop saved to `flagged/` — 5 remain unresolved after all three models (down
from 12 after نموذج ١+٣ alone). نموذج ٣ is a straighter, fully legible capture of the
same sitting, entirely "Not yet answered" (tier open) except one question with a
filled radio under a stale banner (`needs-eye`-adjacent discrepancy, recorded as a
claim per the pharmacology row 19 radio-state precedent).

**نموذج ٢'s answers are structurally unrecoverable — not a capture failure, a
deliberate redaction.** Every question's radio-button column is covered by a
hand-drawn white whiteout stroke in the source PDF itself, confirmed by re-rendering
several pages at 3x resolution and zooming tight on the radio column: the stroke has
soft rounded ends and irregular width, consistent with a digital highlighter tool,
not a rendering artifact or a downscale/crop issue. This holds for every "Answer
saved" question in the file — none of نموذج ٢'s answers are transcribable, so all 45
of its questions are tier `open` here regardless of whether Moodle recorded an
answer. نموذج ٢ still contributed real value: fuller-context stem recovery for
several needs-eye entries, and confirmation for the "(UseD.." (PH-M-006) and "...then."
(PH-M-020) oddities as genuine source text rather than capture cutoffs, since all
three independent captures end identically. Its own countdown timer/section headers
also show it's a separate photographed attempt from نموذج ١ and نموذج ٣, not a
reshuffled duplicate of either.

**نموذج ١'s own PDF holds two passes through part of the exam.** Its last two pages
(26–27) revisit Q1–Q13 a second time with the identical option order but two
different selections than the first pass (Q1, Q12) — recorded `disputed: true` with
both captures as claims, same precedent as public-health quizzes row 8's
same-attempt two-photos-two-different-answers case. No way to tell which pass is
final.

**One further dispute is cross-model**, not same-model: PH-M-007 (Epidemic/Outbreak
terminology) is claimed `a` by نموذج ١ and `d` by نموذج ٣ — but نموذج ٣'s claim is
itself the discrepant filled-radio-under-stale-badge case, so this is a dispute
between two independently uncertain claims rather than two confident ones.

### PH-M-001
tier: claimed
form: mcq
type: single
disputed: true
models: [1]
claims:
  - source: first pass (page 1)
    answer: a
  - source: second pass (page 26, later in the file)
    answer: b
img: flagged/PH-M-001-012-second-pass-review.jpg
note: Same attempt captured twice in this PDF — see the tab-level note above.
What is the primary criterion for establishing causation in a scientific study?
a) Correlation
b) Statistical significance
c) Replication
d) Randomization

### PH-M-002
tier: claimed
form: mcq
type: single
claimed: d
needs-eye: true
models: [1]
img: flagged/PH-M-002-dimension-health-cutoff.jpg
note: Right-edge cutoff present identically in both this attempt's passes (page 1
  and page 26) — genuinely missing from the source photos, not a resolution issue.
  Answer choice is legible regardless.
Which dimension of health involves the ability to engage in activities of daily
living with vigor and alertness, without undue f[text cut off by photo frame]
energy to enjoy leisure activities?
a) Occupational health
b) Intellectual health
c) Emotional health
d) Physical health

### PH-M-003
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
What is a necessary cause in epidemiology?
a) A factor that is always sufficient to cause a disease
b) A factor that increases the risk of a diseasE.
c) A factor that is always present in healthy individuals.
d) A factor that is required for the occurrence of a disease but may not be
   sufficient alone

### PH-M-004
tier: claimed
form: mcq
type: single
claimed: c
needs-eye: true
models: [1]
img: flagged/PH-M-004-food-insecurity-cutoff.jpg
What is the relationship between food insecurity and chronic diseases like
diabetes and heart dis[text cut off by photo frame]?
a) It has no effect on chronic diseases.
b) It reduces the risk of chronic diseases.
c) It can increase the risk of chronic diseases due to poor nutrition.
d) It only affects acute diseases, not chronic conditions.

### PH-M-005
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 3]
note: Stem completed via model 3's clean capture — model 1's own photo cuts off
  after "towards lifestyl...".
During which stage of epidemiological transition do countries typically experience
a shift towards lifestyle-related diseases like heart disease and cancer?
a) Stage 1
b) Stage 2
c) Stage 3
d) Stage 4

### PH-M-006
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 3]
note: Stem ends exactly "...(UseD.." in both models' independent captures — this is
  how the question is authored in the source (likely a professor's editing slip),
  not a photo cutoff. Preserved verbatim per hard rule 2. Option order taken from
  model 3's clean capture.
A study was conducted to examine the effectiveness of a community-based multimodal
intervention program for relative marriage prevention in regions where the relative
marriage rate was relatively high compared to control regions (UseD..
a) Program review
b) Program Trial
c) Cross sectional
d) Clinical trial

### PH-M-007
tier: claimed
form: mcq
type: single
disputed: true
models: [1, 3]
claims:
  - source: model 1
    answer: a
  - source: model 3
    answer: d
note: Model 3's claim comes from a filled radio under a stale "Not yet answered"
  badge (see tab-level note) — recorded as a claim per the radio-state-over-badge
  precedent, but it is itself a lower-confidence capture than an ordinary "Answer
  saved" claim.
What term is used to describe a sudden increase in the number of disease cases
above the expected level in a specific population or area?
a) Epidemic
b) Outbreak
c) Endemic
d) Pandemic

### PH-M-008
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
Which of the following is NOT considered one of the determinants of community
health?
a) Individual genetics
b) Socioeconomic status
c) Healthcare Access
d) Environmental factors

### PH-M-009
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2]
note: Stem was cut off twice in نموذج ١'s own capture; fully recovered via نموذج ٢
  (models: [1, 2] above). The old crops evidencing the cutoff stay in flagged/ per
  CLAUDE.md (never deleted) but are no longer referenced from this entry.
British investigators conducted a study to compare measles-mumps-rubella (MMR)
vaccine history among 1,294 children with pervasive development disorder (e.g.,
autism and development disorder) and 4,469 children without such disorders. (They
found no association.) This is an example of which type(s) of study?
a) Clinical trial
b) Cohort
c) Cross-sectional
d) Case-control

### PH-M-010
tier: claimed
form: mcq
type: single
claimed: a
models: [1]
Which term is used to describe the consistent and usual presence of a disease
within a specific geographic area?
a) Endemic
b) Outbreak
c) Epidemic
d) Pandemic

### PH-M-011
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 3]
Which of the following best describes health disparities?
a) Variations in health outcomes that are always based on individual choices
b) Differences in health outcomes that are purely due to genetics
c) Systematic and unfair differences in health outcomes between different groups
d) Temporary differences in health that have no long-term impact

### PH-M-012
tier: claimed
form: mcq
type: single
disputed: true
models: [1]
claims:
  - source: first pass (page 7)
    answer: c
  - source: second pass (page 27, later in the file)
    answer: b
img: flagged/PH-M-001-012-second-pass-review-cont.jpg
note: Same same-attempt double-capture phenomenon as PH-M-001.
How can globalization influence the availability and affordability of healthcare
services in low-income countries?
a) It has no impact on healthcare accessibility.
b) It often leads to reduced healthcare access and affordability.
c) It exclusively improves healthcare services in low-income countries.
d) It doesn't affect healthcare services in low-income countries.

### PH-M-013
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 3]
A positive association based on risk difference is referred to as Risk difference
of
a) Less than 0
b) More than 1
c) More than 0
d) Less than 1

### PH-M-014
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2]
If the relative risk of lung cancer among heavy smokers (20+ cigarettes per day) is
25 times higher than that of non-smokers, what can be concluded?
a) There is no significant relationship between heavy smoking and lung cancer.
b) The relative risk is unrelated to the number of cigarettes smoked.
c) Heavy smokers are at a lower risk of lung cancer.
d) Heavy smokers are at a much higher risk of lung cancer.

### PH-M-015
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 3]
A study in which children are randomly assigned to receive either a newly
formulated vaccine or the currently available vaccine, and are followed to monitor
for side effects and effectiveness of each vaccine, is an example of which type of
study?
a) Cohort
b) Cross-sectional
c) Clinical trial
d) Case-control

### PH-M-016
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 3]
A cohort study differs from a case-control study in that:
a) Subjects are asked about their exposure status in a cohort study but not in a
   case-control study
b) Cohort studies require many years to conduct, but case-control studies do not
c) Subjects are enrolled or categorized on the basis of their exposure status in a
   cohort study but not in a case-control study
d) Cohort studies are conducted to investigate chronic diseases, case-control
   studies are used for infectious diseases

### PH-M-017
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2]
What is the fundamental question that analytical epidemiology aims to answer?
a) "What is the basic pattern of the disease?"
b) "How do exposures relate to disease occurrence?"
c) "What is the disease's geographic distribution?"
d) "Who is affected by the disease?"

### PH-M-018
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2, 3]
What does the term 'longitudinal design' mean?
a) A study completed far away from where the researcher lives
b) A study with two contrasting cases
c) A study which is very long to read
d) A study completed over a distinct period of time

### PH-M-019
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 3]
note: Model 1's own capture was too blurred to read the confidence-interval
  figures; recovered via model 3's clean capture of the same stem/options. The
  claimed option (OR 0.3) was identifiable by position and leading digit in the
  blurred photo even before the cross-model confirmation.
Which of the following represents a significant negative association between
Obesity and physical activity?
a) OR 7.2 (5.1 – 6.2)
b) OR 0.7 (0.2 – 0.8)
c) OR 0.3 (0.1 – 1.4)
d) OR 1.3 (1.1 – 2.3)

### PH-M-020
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2]
note: Option d's text ends exactly "...because then." in the source capture —
  preserved verbatim per hard rule 2, though it reads as an incomplete sentence.
RR is close to OR in all of the following except for one
a) The Disease prevalence is high
b) Cases are representative of all cases in the population w.r.t. exposure history
c) Controls representative of all non-cases in the population w.r.t. exposure
   history
d) Outcome is rare because then.

### PH-M-021
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
Life expectancy at birth is a commonly used indicator to assess:
a) Access to technology
b) Income inequality
c) Health inequalities and disparities
d) Educational attainment

### PH-M-022
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
In what way can food insecurity contribute to obesity in some populations?
a) It only affects underweight individuals, not those with obesity.
b) It can result in the consumption of low-cost, high-calorie, and nutrient-poor
   foods.
c) It often leads to reduced food intake and weight loss.
d) It has no connection to obesity.

### PH-M-023
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2]
Socioeconomic status and education level of an individual are examples of:
a) Distal determinants
b) Environmental determinants
c) Proximal determinants
d) Genetic determinants

### PH-M-024
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 3]
In the context of health equity, what does the "social determinants of health"
refer to?
a) Genetics and family history that determine one's health
b) The availability of advanced medical technologies
c) The impact of healthcare professionals on individual health outcomes
d) Factors such as income, education, and social support that influence health

### PH-M-025
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
What does the guideline of "Temporal Sequence" in causation imply?
a) The effect must always precede the cause.
b) The cause must precede the effect in a plausible temporal order.
c) The cause and effect must occur simultaneously.
d) The temporal sequence has no bearing on causation.

### PH-M-026
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2]
note: Stem fully recovered via نموذج ٢ (models: [1, 2] above); the old cutoff-
  evidence crops stay in flagged/ per CLAUDE.md but are no longer referenced here.
The Iowa Women's Health Study, in which researchers enrolled 41,837 women in 1986
and collected exposure and lifestyle information to assess the relationship
between these factors and subsequent occurrence of cancer, is an example of which
type(s) of study?
a) Clinical trial
b) Case-control
c) Cohort
d) Cross-sectional

### PH-M-027
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
How does food insecurity impact children's development and health?
a) It only affects children's physical health, not their cognitive development.
b) It can result in stunted growth, learning difficulties, and poor health
   outcomes.
c) It has no effect on children's development and health.
d) It leads to better growth and cognitive development.

### PH-M-028
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
What are health disparities?
a) Variations in healthcare services within a single hospital
b) Inequalities in health outcomes among different population groups
c) Differences in health outcomes between individuals of different ages
d) Changes in health status due to natural aging processes

### PH-M-029
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 3]
"Inevitable health differences" typically refer to disparities in health outcomes
that are primarily caused by:
a) Individual lifestyle choices
b) Genetic factors
c) Unavoidable factors and out of human control
d) Temporary fluctuations in health

### PH-M-030
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2]
Epidemiology plays a significant role in identifying and understanding:
a) To describe the natural history of the disease.
b) Risk factors associated with diseases and health conditions
c) All of the answer are correct
d) The community diagnosis of certain diseases and their control

### PH-M-031
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
Epidemiologists measure the impact of diseases on populations using which key
rubric?
a) Person
b) Place
c) Magnitude
d) Cause
e) Time

### PH-M-032
tier: claimed
form: mcq
type: single
claimed: d
models: [1]
Which type of study design is best suited for investigating causal relationships?
a) Case-control study
b) Descriptive study
c) Cross-sectional study
d) Cohort study

### PH-M-033
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 3]
One of the following is not one of the SDGs
a) Put an End to the Death of Children Under the Age of 5
b) Reduce the Rate of Premature Mortality
c) End Epidemics
d) Ending Maternal Mortality Ratio

### PH-M-034
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2]
Which stage of the epidemiological transition is characterized by high mortality
rates from infectious diseases and a lack of effective medical interventions?
a) Stage 2
b) Stage 1
c) Stage 3
d) Stage 4

### PH-M-035
tier: claimed
form: mcq
type: single
claimed: a
needs-eye: true
models: [1]
img: flagged/PH-M-035-MI-obesity-cutoff.jpg
For a study comparing the risk of obesity between myocardial infarction (MI) and
none MI patient[text cut off by photo frame]
a) Odds ratio
b) PAR
c) Relative risk
d) Risk difference

### PH-M-036
tier: claimed
form: mcq
type: single
claimed: a
needs-eye: true
models: [1]
img: flagged/PH-M-035-MI-obesity-cutoff.jpg
note: Same source page as PH-M-035; crop shown covers both.
What does the concept of "dose-response relationship" in epidemiology suggest?
(U[text cut off by photo frame]
a) As exposure to the factor increases, the risk of the outcome also increases.
b) The relationship between exposure and outcome is unpredictable.
c) The more exposure to the factor, the lower the risk of the outcome.
d) Exposure to the factor has no impact on the risk of the outcome.

### PH-M-037
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2]
In the context of epidemiological transition, what is a characteristic of Stage 2?
a) High mortality rates from infectious diseases
b) High birth rates and low mortality rates
c) A decline in infectious diseases and a rise in chronic diseases
d) A predominance of chronic diseases

### PH-M-038
tier: claimed
form: mcq
type: single
claimed: b
models: [1]
If a necessary cause is removed from a population, what would be the expected
impact on the associated disease?
a) The disease will become more prevalent.
b) The disease will disappear from the population.
c) The disease will continue to occur at the same ratE.
d) The disease will become less severe but still occur

### PH-M-039
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2]
A study comparing two treatment methods for a specific disease reveals an odds
ratio of 1.2 for one treatment method compared to the other. What does this odds
ratio value imply?
a) The first treatment method is more effective in reducing the odds of the
   disease.
b) The odds ratio value is not indicative of the treatment method's effectiveness.
c) Both treatment methods are equally effective in reducing the odds of the
   disease.
d) The second treatment method is more effective in reducing the odds of the
   disease.

### PH-M-040
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2]
note: Stem fully recovered via نموذج ٢ (models: [1, 2] above); the old cutoff-
  evidence crop stays in flagged/ per CLAUDE.md but is no longer referenced here.
________________ aims to identify the proportion of the population which has the
disease being studied with the aim of collecting information about the health
status of the population.
a) community trail
b) cohort study
c) case-control study
d) cross-sectional study

### PH-M-041
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3]
note: Options a and b recovered in full via model 3 — model 1's own capture cut
  both off mid-sentence at the right edge.
Which of the following is the most accurate definition of social determinants of
health?
a) The conditions in the environments where people are born, live, learn, work,
   play, worship, and age affect a wide range of health, functioning, and
   quality-of-life outcomes and risks.
b) The factors that influence the health of an individual or population, include
   genetics, behavior, and the environment.
c) The policies and practices that influence the distribution of health within a
   population.
d) The social and economic conditions that shape the distribution of health within
   a population.

### PH-M-042
tier: claimed
form: mcq
type: single
claimed: b
needs-eye: true
models: [1]
img: flagged/PH-M-042-dimension-health-cutoff.jpg
Which dimension of health involves the ability to form and maintain satisfying and
supportive relationships wit[text cut off by photo frame]?
a) Spiritual health
b) Social health
c) Intellectual health
d) Emotional health

### PH-M-043
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3]
note: Stem completed via model 3 — model 1's own capture cut off after "between".
What statistical measure is commonly used to assess the strength and direction of
a linear relationship between two variables?
a) Pearson correlation coefficient
b) Odds ratio
c) P-value
d) Confidence interval

### PH-M-044
tier: claimed
form: mcq
type: single
claimed: c
models: [1]
In the study, individuals with the genetic mutation are 4 times more likely to
develop the medical condition compared to those without the mutation. What is the
odds ratio?
a) 16
b) 0.25
c) 4
d) 1

### PH-M-045
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2]
Epidemiologists studying the geographical distribution of disease to identify
clusters or patterns are primarily using which rubric?
a) Place
b) Cause
c) Time
d) Magnitude
e) Person

### PH-M-046
tier: open
form: mcq
type: single
models: [2, 3]
For the follow-up of 1000 smokers and 1000 none smokers for 5 years, to compare the
difference in lung vital capacity, we would use
a) Risk difference
b) PAR
c) Relative risk
d) Odds ratio

### PH-M-047
tier: open
form: mcq
type: single
models: [3]
What is the term for an event or factor that precedes the outcome of interest and
is both necessary and sufficient to cause the outcome?
a) Confounding factor
b) Risk factor
c) Causal factor
d) Independent variable

### PH-M-048
tier: open
form: mcq
type: single
models: [2, 3]
What factor is primarily responsible for the shift from high mortality rates due to
infectious diseases to low mortality rates from chronic diseases in the
epidemiological transition?
a) Increased population density
b) Climate change
c) Decreased urbanization
d) Advances in medical technology and healthcare

### PH-M-049
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3]
note: Radio filled at option b despite the page's "Not yet answered" badge —
  recorded as a claim per the radio-state-over-badge precedent (see tab-level
  note).
Which of the following best describes a health-related event?
a) A cultural festival
b) An incident that impacts the health and well-being of individuals or
   populations
c) A sports competition
d) A social gathering

### PH-M-050
tier: open
form: mcq
type: single
models: [3]
Which stage of the demographic transition model is characterized by high birth and
death rates?
a) Stage 1
b) Stage 2
c) Stage 4
d) Stage 3

### PH-M-051
tier: open
form: mcq
type: single
models: [3]
Which of the following is considered a key socioeconomic determinant of health?
a) Diet and nutrition
b) Genetics
c) Air quality
d) Income

### PH-M-052
tier: open
form: mcq
type: single
models: [3]
Which of the following is a key element in establishing a temporal relationship
between cause and effect?
a) Time sequence
b) Consistency
c) Sample size
d) Confounding variables

### PH-M-053
tier: open
form: mcq
type: single
models: [3]
Which of the following is a key aspect of epidemiology?
a) Developing new surgical techniques
b) Collecting and analyzing data on disease occurrence
c) Providing direct patient care
d) Managing healthcare facilities

### PH-M-054
tier: open
form: mcq
type: single
models: [3]
What does the "cause" rubric in epidemiology primarily aim to determine? (UseD.
a) The temporal patterns of health events
b) The risk factors and determinants of health-related events
c) The characteristics of individuals affected by a disease
d) The quantification of health issues
e) The geographical distribution of health events

### PH-M-055
tier: open
form: mcq
type: single
models: [3]
During which stage of the demographic transition model does a country typically
experience rapid population growth?
a) Stage 2
b) Stage 1
c) Stage 4
d) Stage 3

### PH-M-056
tier: open
form: mcq
type: single
models: [3]
What is a potential negative health effect of globalization related to lifestyle
changes?
a) Reduced exposure to environmental pollutants
b) Sedentary lifestyles and increased prevalence of obesity
c) Increased consumption of traditional diets
d) Improved access to healthcare services

### PH-M-057
tier: open
form: mcq
type: single
models: [2, 3]
Between the public health and the medical model, the medical model health is
concerned with all of the following except for one
a) Treatment of the disease
b) Diagnosis of the disease
c) Prevention of the disease
d) Intervention in disease management

### PH-M-058
tier: open
form: mcq
type: single
models: [3]
Why health and rights to health are important for improving health of people
Except:
a) Provides a positive, alternate framework for the pure medical model
b) Liberate people from the foreign control;
c) It allows people to have informed health decisions
d) Decrease the severity of disparities in health care among people
e) Provides a unifying message based on the universality of rights

### PH-M-059
tier: open
form: mcq
type: single
models: [3]
The "Biological Plausibility" criterion for causation emphasizes the importance of:
a) Using convenience sampling.
b) Demonstrating a biologically credible mechanism.
c) Conducting randomized controlled trials.
d) Establishing a statistical relationship.

### PH-M-060
tier: open
form: mcq
type: single
models: [3]
In which stage of the demographic transition model do birth rates remain high
while death rates decline significantly?
a) Stage 3
b) Stage 1
c) Stage 2
d) Stage 4

### PH-M-061
tier: open
form: mcq
type: single
models: [2, 3]
Which of the following is a criterion for causation based on the Hill's
viewpoints?
a) Cross-sectional design
b) Temporality
c) Face validity
d) Convenience

### PH-M-062
tier: open
form: mcq
type: single
models: [3]
Which of the following is an example of an environmental determinant of community
health?
a) Family history of diseases
b) Diet and nutrition
c) Access to safe drinking water
d) Educational attainment

### PH-M-063
tier: open
form: mcq
type: single
models: [3]
Which of the following statements best characterizes the role of genetics in the
context of a sufficient cause?
a) Genetic factors are only necessary causes.
b) Genetic factors are always sufficient to cause a diseasE.
c) Genetic factors are unrelated to the concept of a sufficient cause.
d) Genetic factors contribute as component causes in complex diseases.

### PH-M-064
tier: open
form: mcq
type: single
models: [2]
In epidemiology, which of the following is a potential source of bias that can
affect the assessment of causation?
a) Confounding
b) Hypothesis testing
c) Randomization
d) Sample size

### PH-M-065
tier: open
form: mcq
type: single
models: [2]
Which population group is often disproportionately affected by health disparities
in many countries?
a) Older adults
b) Racial and ethnic minorities
c) Children
d) Middle-aged adults

### PH-M-066
tier: open
form: mcq
type: single
models: [2]
A study comparing two different exercise routines finds a relative risk of 0.8 for
one group compared to the other. What does this relative risk value imply?
a) Both exercise routines are equally effective in reducing the risk of health
   issues.
b) The relative risk value is not indicative of the effectiveness of exercise
   routines.
c) The second exercise routine is more effective in reducing the risk of health
   issues.
d) The first exercise routine is more effective in reducing the risk of health
   issues.

### PH-M-067
tier: open
form: mcq
type: single
models: [2]
note: Thematically close to PH-M-061 (Hill's criteria) but a distinct stem and
  option set — kept separate per the stem-match rule.
Which of the following is a criterion for causation proposed by Sir Austin
Bradford Hill?
a) Consistency
b) Sample size
c) Face validity
d) Convenience

### PH-M-068
tier: open
form: mcq
type: single
models: [2]
What does descriptive epidemiology help researchers understand about a health
event?
a) The effectiveness of medical treatments.
b) The specific genetic factors involved.
c) The basic patterns and features of the event.
d) The mechanisms of disease transmission.

### PH-M-069
tier: open
form: mcq
type: single
models: [2]
Which of the following criteria is a key guideline for establishing causation in
epidemiological research?
a) Correlation without consistency
b) Convenience sampling
c) Low statistical power
d) Temporality

### PH-M-070
tier: open
form: mcq
type: single
models: [2]
What is the key goal of health equity?
a) Providing equal access to healthcare for everyone
b) Promoting the highest possible quality of healthcare for all
c) Reducing health disparities and achieving fair opportunities for good health
d) Ensuring that everyone has the same health outcomes

### PH-M-071
tier: open
form: mcq
type: single
models: [2]
A study on the association between pesticide exposure and a specific health
condition shows a relative risk of 1.2. What does this relative risk value
indicate?
a) Pesticide exposure reduces the risk of the health condition.
b) The relative risk cannot be determined from this value.
c) There is no risk associated with pesticide exposure.
d) There is a 1.2-fold increased risk of the health condition with pesticide
   exposure.

### PH-M-072
tier: open
form: mcq
type: single
models: [2]
How does globalization impact the spread of infectious diseases?
a) It always leads to the containment of diseases.
b) It has no effect on disease transmission.
c) It reduces the incidence of infectious diseases.
d) It can accelerate the spread of infectious diseases.

### PH-M-073
tier: open
form: mcq
type: single
models: [2]
Which of the following criteria involves demonstrating that the cause and effect
relationship can be replicated in different populations and settings?
a) Consistency
b) Coincidence
c) Specificity
d) Biological plausibility

### PH-M-074
tier: open
form: mcq
type: single
models: [2]
Which of the following is an example of how globalization can improve health
outcomes?
a) Cultural preservation leading to isolation from outside influences
b) Access to international medical expertise and resources during health crises
c) Restricting the import of pharmaceuticals from other countries
d) Promoting traditional medicine practices exclusively

### PH-M-075
tier: open
form: mcq
type: single
models: [2]
note: A differently-worded "dose-response relationship" question from PH-M-036 —
  different stem, completely different option set, kept separate.
In epidemiology, what does the term "dose-response relationship" refer to?
a) The significance level in hypothesis testing
b) The effect of the independent variable on the dependent variable
c) The relationship between exposure and disease risk
d) The impact of confounding variables on study outcomes

### PH-M-076
tier: open
form: mcq
type: single
models: [2]
What does point prevalence measure in epidemiology?
a) The probability of developing a disease.
b) The proportion of the population with a disease at a specific point in time.
c) New cases of a disease during an outbreak.
d) The rate of death in a population.

### PH-M-077
tier: open
form: mcq
type: single
models: [2]
The dimension of health that encompasses the pursuit of knowledge and the ability
to think critically is known as:
a) Intellectual health
b) Spiritual health
c) Emotional health
d) Social health

### PH-M-078
tier: open
form: mcq
type: single
models: [2]
Which of the following health determinants is most strongly associated with an
individual's risk of chronic diseases such as heart disease, diabetes, and
obesity?
a) Access to healthcare
b) Genetics
c) Socioeconomic status
d) Air quality

### PH-M-079
tier: open
form: mcq
type: single
models: [2]
How can the degradation of agricultural land impact food security and nutrition?
a) It has no effect on food security and nutrition.
b) It can result in reduced food production and malnutrition.
c) It leads to increased agricultural productivity and better nutrition.
d) It only affects the quality of non-agricultural land.

### PH-M-080
tier: open
form: mcq
type: single
models: [2]
A common outcome of health inequality is:
a) Disparities in health outcomes among different population groups
b) Improved overall community health
c) Reduction in healthcare costs
d) Decreased life expectancy for everyone.

### PH-M-081
tier: open
form: mcq
type: single
models: [2]
note: A distinct stem from PH-M-024/041's social-determinants-of-health questions
  — this one is a definitional fill-in-the-blank naming exercise, kept separate.
Economic, social, cultural, and physical conditions that contribute to or detract
from the health of individuals and communities are known as the
a) Environmental factors of health
b) Social determinants of health
c) Community factors in health
d) Perceived benefits of health

### PH-M-082
tier: open
form: mcq
type: single
models: [2]
Which of the following factors is a behavioral determinant of health?
a) Social norms
b) Age
c) Diet
d) Pollution

### PH-M-083
tier: open
form: mcq
type: single
models: [2]
note: Option c preserves the source's own typo ("natation" for "nations") per
  hard rule 2.
The declaration of health as a human right was declared at
a) Alam Ata 1978
b) Kazakhstan 1982
c) United natation 2015
d) WHO 1986

### PH-M-084
tier: open
form: mcq
type: single
models: [2]
What distinguishes a necessary cause from a component cause in the context of a
sufficient cause?
a) A necessary cause is always sufficient, while a component cause is not.
b) A necessary cause is one of multiple factors, while a component cause is
   singular.
c) A necessary cause is a risk factor, while a component cause is an effect
   modifier.
d) A necessary cause is always present, while a component cause increases the
   risk.
