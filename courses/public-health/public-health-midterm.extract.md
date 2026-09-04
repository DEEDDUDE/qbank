---
course: public-health
tab: midterm
questions: 177
tiers: claimed 46 | open 131
forms: mcq 176 | unknown 1
needs-eye: 6
disputed: 3
next-id: PH-M-178
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

**Two more sittings added (PH-M-085–177): `raw/midterm/2022/` (a scanned paper
exam, 8 photos, PH-M-085–128) and `raw/midterm/2015/Mid Exam P.H. 2015.pdf` (a
free-text-layer Moodle export, 15 pages, PH-M-129–177).** Neither carries any
answer mark, so every question here is tier `open`. Both are genuinely different
exams from the three 2023 نماذج above — not reshuffled models of that sitting —
so nothing here extends a نموذج's own `models:` list; a `models:` tag of `2022`
or `2015` marks which of *these two* sittings a question was seen in instead.

**2022 (paper exam) specifics.** Printed exam, "(1 point)"/"(2 point)" marks
visible per question, page numbers 1–8 seen — only 8 of what was likely a longer
paper were photographed, so this is a partial capture; don't infer the missing
pages' content. Bold text on some option letters is inconsistent with any
answer pattern and reads as ordinary typesetting/OCR-adjacent styling, not a
mark — per this row's own pre-flight note, not read as a claim. One genuine gap
within the captured range: **PH-M-113 (Q29)** — the photo ends right after the
stem, the next photo starts fresh at Q30, and the question's own options were
simply never photographed. Recorded with `form: unknown`, `needs-eye: true`,
stem only, rather than inventing four options.

**2015 (Moodle export PDF) specifics.** Clean text layer, `Question N` /
`Select one:` anchors, no marks anywhere — confirmed against the header note's
own expectation. **This sitting's answers may still be recoverable at Job C**:
row 5 of this course's practice tab found that `public-health-practice.extract.md`
(PYQ bank, p11 section, PH-P-*) is a verbatim reproduction of this same 2015
midterm with a student's answers marked (bold, not capitalization — see that
file's own row-6 correction). Same Q1 stem ("main insurance program scheme in
Palestine") confirms it's the identical exam. Job C should cross-check each of
PH-M-129–177 against that PYQ-bank section before defaulting to `not-in-source`
or a from-scratch `source.md` lookup — per hard rule 5, that cross-reference
belongs to Job C, not this extraction. One annotation of note: **PH-M-151
(Q24)** carries a handwritten-style Arabic margin note, "في جوابين صح" ("there
are two correct answers"), despite the question printing "Select one:" —
excluded from the stem (interface-adjacent text) but preserved in the entry's
own `note:` field since it's informative, not chrome; it names no specific
options, so the question stays tier `open` rather than guessed at.

**One cross-sitting merge found**: **PH-M-087** (2022's Q3, "major determinants
of health") and 2015's own Q9 share the same four option texts, just reordered
— merged into one entry carrying `models: [2015, 2022]` rather than kept as two
separate near-identical entries. No other exact cross-sitting matches were
found between 2015 and 2022 despite substantial thematic overlap (both cover
WHO's health definition, Alma-Ata content, disease-causation theories,
determinants of health) — the specific option sets differ enough on every other
shared theme that they're kept as separate entries per the batch-matching
convention (match on stem *and* options, not topic alone). Neither 2015 nor
2022 was cross-checked against the three 2023 نماذج (PH-M-001–084) beyond a
quick thematic skim that found no exact stem/option matches — a fuller
cross-check across all five sittings is Job C's job at verification time, not
this row's.

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

### PH-M-085
tier: open
form: mcq
type: single
models: [2022]
WHO 1986 definition of health is:
a) Ensuring the health of the individual by maintaining and improving the health of the community.
b) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science.
c) A complete state of physical, mental and social wellbeing and not merely the absence of disease.
d) Health is the extent to which an individual or group is able, on the one hand to realize aspirations and satisfy needs; and, on the other hand, to change or cope with the environment. It is to be seen as a resource for everyday life and not merely the objective of living.

### PH-M-086
tier: open
form: mcq
type: single
models: [2022]
All of the following are considered functions of Public health, except:
a) Mobilizes communities for health
b) Provides conditions conducive to health
c) Promotes healthy lifestyles
d) Heart transplant operation in specialized heart medical center

### PH-M-087
tier: open
form: mcq
type: single
models: [2015, 2022]
note: Same four options as public-health midterm 2015 Q9 (PH-M-129 range), reordered
  -- merged as one entry, models: [2015, 2022]. This option wording (2022's
  ordering) kept as canonical; 2015 lettered them a) HB/Env/Lifestyle/HC b)
  Comm/Env/Sociodem/culture c) HB/culture/Behav/HC d) HB/Sociodem/Behav/Physical
  -- same four texts, different order/lettering.
Which of the following are the major determinants of health?
a) Human biology, Socio-demographic, Behavioural, Physical
b) Human biology, Environment, Lifestyle behavior, Health care organization
c) Community organization, Environment, Socio-demographic, culture
d) Human biology, culture, Behavioural, Health care organization

### PH-M-088
tier: open
form: mcq
type: single
models: [2022]
Twentieth century models of disease causation theories include:
a) Miasma theory.
b) Supernatural theory.
c) The Multi Causal Theory
d) All of the above are right.

### PH-M-089
tier: open
form: mcq
type: single
models: [2022]
The name of the person, who introduced in 1862 that germs caused many diseases, and in 1888 established the first public health lab is ____.
a) Willian Harvey
b) John Snow
c) Edward Jenner
d) Louis Pasteur

### PH-M-090
tier: open
form: mcq
type: single
models: [2022]
The following are determinant of inequities except:
a) Health damaging behaviors.
b) Exposure to unhealthy, stressful living and working conditions.
c) Inadequate access to essential health and other public services.
d) Differences in the incidence and prevalence of health conditions and health status between groups

### PH-M-091
tier: open
form: mcq
type: single
models: [2022]
____ affects the health of a community and it includes the geography (e.g. High land versus low land), the environment (e.g. Manmade or natural catastrophes) and the industrial development (e.g. pollution occupational hazards)
a) Socio - cultural determinants
b) physical determinants
c) behavioral determinants
d) biological determinants

### PH-M-092
tier: open
form: mcq
type: single
models: [2022]
Maternal mortality ratio is defined as:
a) The ratio of the number of maternal deaths during a given time period per 100,000 live births during the same time-period
b) The ratio of maternal deaths during a given period per 1000 deliveries during the same period of time
c) The ratio of maternal deaths due to all causes during a given period per 1000 deliveries during the same period of time
d) The ratio of maternal deaths due to hypertension during a given period per 1000 deliveries during the same period of time

### PH-M-093
tier: open
form: mcq
type: single
models: [2022]
Infant mortality rate is the number of deaths of infants under one year old is measured per:
a) 100 000 live births
b) 10000 live births
c) 1000 live birth
d) 100 live births

### PH-M-094
tier: open
form: mcq
type: single
models: [2022]
Epidemiological transition refers to
a) The change of mortality from infectious diseases to degenerative diseases
b) A change in levels of diabetes in overweight adults
c) The changing prevalence of vitamin D deficiency
d) The change in birth defects due to genetic abnormalities

### PH-M-095
tier: open
form: mcq
type: single
models: [2022]
The health and wellbeing of the community is dependent on a good start, good future, good care and support. These include social, economic, physical and environmental factors which are known as:
a) A person's health
b) Health promotion
c) Public Health
d) Determinants of health

### PH-M-096
tier: open
form: mcq
type: single
models: [2022]
____ is the difference in health care which is not only unnecessary and avoidable but unfair and unjust
a) Health equity
b) Health inequity
c) Health disparities
d) Health equality

### PH-M-097
tier: open
form: mcq
type: single
models: [2022]
Miasma theory is an obsolete medical theory that held that diseases-such as cholera, chlamydia, or the Black Death-were caused by:
a) a noxious form of "bad air", by the odor of decaying of organic materials
b) by a vicious viral infection
c) by genetic factors
d) by all of the above

### PH-M-098
tier: open
form: mcq
type: single
models: [2022]
Hippocrates is credited with the following except:
a) Diseases were caused naturally, not because of superstition
b) Disease was the punishment of God.
c) Considered the father of medicine.
d) Having the disciples of Pythagoras of allying philosophy and medicine

### PH-M-099
tier: open
form: mcq
type: single
models: [2022]
The primary purpose of social determinants of health is to ensure:
a) The importance of providing medical treatment for chronic diseases
b) The importance of reducing inequity within population
c) The multi-sectoral approach in promoting health and preventing illness in the population.
d) The involvement of people in designing and implementing health interventions

### PH-M-100
tier: open
form: mcq
type: single
models: [2022]
Health illness continuum, it is
a) The line between optimal health and death, people are moving on this line according to their social conditions
b) People are not easy to move on the continuum if they are rich,
c) All of the above
d) None of the above

### PH-M-101
tier: open
form: mcq
type: single
models: [2022]
Major public health achievements in the 20th century except:
a) Seat belts
b) Tobacco as a health risk
c) Discovery of CT scans
d) Vaccines

### PH-M-102
tier: open
form: mcq
type: single
models: [2022]
Screening is considered sensitive if:
a) All detected cases are true positives
b) If high percentage of identified cases are true positives
c) If majority of identified cases are true negatives
d) If None of the identified cases is false positive

### PH-M-103
tier: open
form: mcq
type: single
models: [2022]
____ furthered the study of disease etiology (germs/bacteria) and introduced the 1st scientific approach to immunization and pasteurization
a) Willian Harvey
b) John Snow
c) Edward Jenner
d) Louis Pasteur

### PH-M-104
tier: open
form: mcq
type: single
models: [2022]
Economic and social relationships, employment, housing and education that contribute to or detract from the health of individuals and communities are known as the ____
a) Social determinants of health
b) Community factors in health
c) Environmental factors of health
d) Perceived benefits of health

### PH-M-105
tier: open
form: mcq
type: single
models: [2022]
The epidemiologic analytical triad of disease causation refers to: (Choose one best answer)
a) Agent, host, environment
b) Time, place, person
c) Source, mode of transmission, susceptible host
d) John Snow, Robert Koch, Kenneth Rothman

### PH-M-106
tier: open
form: mcq
type: single
models: [2022]
The criteria for instituting a screening program includes the following, except:
a) Rare disease with understood Natural history and long period between first signs and overt disease
b) Diagnostic test: Sensitive and specific, Simple and cheap, Safe and acceptable, reliable
c) Diagnosis: Facilities are adequate
d) Treatment: Effective, acceptable, and safe treatment available.

### PH-M-107
tier: open
form: mcq
type: single
models: [2022]
____: differences in the incidence and prevalence of health conditions and health status between groups
a) Health equity
b) Health inequity
c) Health disparities
d) Health equality

### PH-M-108
tier: open
form: mcq
type: single
models: [2022]
A study in which cancer patients are randomly assigned to receive either a newly formulated chemotherapy or the currently available chemotherapy, and are followed to monitor for side effect and effectiveness of each drug, is an example of which type of study?
a) Interventional.
b) Observational.
c) Cohort.
d) Ecological.

### PH-M-109
tier: open
form: mcq
type: single
models: [2022]
Comparison of study designs: ____ Best for rare diseases:
a) Case Control Studies.
b) Prospective Cohort Studies.
c) Descriptive Studies.
d) Cross Sectional Studies.

### PH-M-110
tier: open
form: mcq
type: single
models: [2022]
A prevalence rate is:
a) The total number of cases of a disease existing in a population divided by the total population.
b) The number of new cases of a disease divided by the number of persons at risk for the disease.
c) The number of new cases of a disease divided by the number of all cases of a disease.
d) None of the above.

### PH-M-111
tier: open
form: mcq
type: single
models: [2022]
A study that measures the incidence of a disease
a) Case report
b) Cross sectional
c) Case control
d) Cohort

### PH-M-112
tier: open
form: mcq
type: single
models: [2022]
All are correct about Environmental theory except
a) Significant number of chronic disease caused by toxins.
b) It emphasizes the interrelatedness of many variables in disease causality, principally those under control of the individual.
c) Disease prevention, instead of requiring medical treatments or personal hygiene, demands change in the industrial production.
d) Concentrates on toxic substances in the air water and soil.

### PH-M-113
tier: open
form: unknown
needs-eye: true
models: [2022]
note: Options never captured -- the source photo ends right after this question's
  stem, and the next photo starts fresh at Q30. A genuine page-break gap in this
  8-photo partial capture of the paper exam, not a legibility issue -- see the
  tab-level note.
Which of the following is a case-control study?

### PH-M-114
tier: open
form: mcq
type: single
models: [2022]
A study was conducted to investigate the effect of HIV infection on mortality among people in Kenya with TB. Individuals with TB were recruited from hospitals and their HIV status determined. They were then followed-up over ten years to compare mortality rates in the HIV positive group and HIV negative group.
a) Case-control study
b) Cohort study
c) Randomized controlled trial
d) Ecological study

### PH-M-115
tier: open
form: mcq
type: single
models: [2022]
In the Netherlands there is an increase in the prevalence of cardiovascular diseases. This is a consequence of
a) deterioration of the food pattern
b) increase in hypertension
c) improved treatment
d) increase in obesity

### PH-M-116
tier: open
form: mcq
type: single
models: [2022]
In an epidemiological context, what is the population at risk?
a) The proportion of a population that engage in risky behaviours.
b) The group of people that may experience the outcome we want to study.
c) A group of people participating in a study that may be harmful to them.
d) The population group with the highest relative risk of disease.

### PH-M-117
tier: open
form: mcq
type: single
models: [2022]
____ discovered that scurvy could be controlled by lime juice
a) Willian Harvey
b) John Snow
c) Edward Jenner
d) Dr. James Lind

### PH-M-118
tier: open
form: mcq
type: single
models: [2022]
Which definition best describe the process of globalization?
a) Capitalist companies are spreading across the planet
b) We all now live in a single society
c) Individuals, groups and nations are becoming more interdependent
d) Human beings now live on every continent of the planet

### PH-M-119
tier: open
form: mcq
type: single
models: [2022]
Prevention of progression or recurrence in patients with prostate cancer is an example of
a) Primordial prevention.
b) Primary prevention.
c) Secondary prevention
d) Tertiary prevention

### PH-M-120
tier: open
form: mcq
type: single
models: [2022]
An example of secondary prevention would be
a) Wearing a seat belt
b) Adequate treatment of. Diabetes once detected
c) Education about healthy eating exercising regularly
d) Getting a flu vaccination

### PH-M-121
tier: open
form: mcq
type: single
models: [2022]
Improving sanitation, establishing healthy communities, and promoting a healthy lifestyle in childhood are examples on:
a) Primordial prevention.
b) Primary prevention.
c) Secondary prevention
d) Tertiary prevention

### PH-M-122
tier: open
form: mcq
type: single
models: [2022]
Screening programs for breast cancer are aimed at:
a) Identifying true positives
b) Identify true negatives only
c) Specificity
d) Negative predictive value

### PH-M-123
tier: open
form: mcq
type: single
models: [2022]
The probability of a person's having the disease when the test is positive
a) Sensitivity
b) Specificity
c) Positive predictive value
d) Negative predictive value

### PH-M-124
tier: open
form: mcq
type: single
models: [2022]
An epidemiologist in Tanzania wants to study the efficacy of iron supplementation for the prevention of HIV infection. He wants to make sure that only subjects who are (still) free of HIV infection are enrolled in his trial. Therefore, he screens a large group of people using a diagnostic test. Based on the outcome of the test, he decides who could participate in his iron supplementation trial. For this purpose, it is very important that the diagnostic test has a high...
a) Sensitivity
b) Positive predictive value
c) Specificity
d) Negative predictive value

### PH-M-125
tier: open
form: mcq
type: single
models: [2022]
You are working in a pediatric clinic with an experienced pediatrician. You examine 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct.

Calculate the sensitivity of your examination.
a) 10/25
b) 10/15
c) 15/35
d) 15/50

### PH-M-126
tier: open
form: mcq
type: single
models: [2022]
You are working in a pediatric clinic with an experienced pediatrician. You examine 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct.

Calculate the specificity of your examination.
a) 10/15
b) 15/35
c) 15/50
d) 20/25

### PH-M-127
tier: open
form: mcq
type: single
models: [2022]
You are working in a pediatric clinic with an experienced pediatrician. You examine 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct.

Calculate the chance that your diagnosis of Otitis Media is correct.
a) 10/25
b) 10/15
c) 15/35
d) 15/50

### PH-M-128
tier: open
form: mcq
type: single
models: [2022]
You are working in a pediatric clinic with an experienced pediatrician. You examine 50 children whose parents are concerned about the possibility of ear infection. You believe that 15 children have red and bulging tympanic membranes consistent with otitis media (OM). The pediatrician examines these same children and makes a diagnosis of otitis media in 25 children. The pediatrician agrees that 10 of your 15 diagnoses of children with otitis media are correct.

Calculate the chance that your diagnosis of normal eardrum is correct.
a) 10/15
b) 15/35
c) 15/50
d) 20/35

### PH-M-129
tier: open
form: mcq
type: single
models: [2015]
The main insurance program scheme in Palestine is:
a) Most population without health insurance
b) Private Health Insurance
c) UNRWA health insurance
d) Government health insurance

### PH-M-130
tier: open
form: mcq
type: single
models: [2015]
Prevention refers to the goals of medicine that are to promote, to preserve, and to restore health when
it is impaired, and to minimize suffering and distress.
a) True
b) False

### PH-M-131
tier: open
form: mcq
type: single
models: [2015]
Reasons to Study Global Health:
a) To learn about low-cost but highly effective interventions
b) Nature of many global health concerns
c) All of them
d) Need for different actors to work together
e) Link between health and development

### PH-M-132
tier: open
form: mcq
type: single
models: [2015]
Which of the following is not a characteristic of healthy system?
a) The system should have feedback from the subsystems and the community at large
b) The system should have completely open boundaries
c) The system has ability to differentiate and grow through self-regulation and change.
d) The system has a hierarchy of systems such as parents, grandparents, and children

### PH-M-133
tier: open
form: mcq
type: single
models: [2015]
ARI in Almata conference stands for
a) None of them
b) Autism Research Institute
c) Acute respiratory infection
d) Air resource institute

### PH-M-134
tier: open
form: mcq
type: single
models: [2015]
The Millennium Development Goals (MDGs) is
a) Eradication of extreme poverty and hunger
b) All of them
c) Combating HIV/AIDS, malaria and other diseases.
d) Improvement in maternal health
e) Reduction of child mortality

### PH-M-135
tier: open
form: mcq
type: single
models: [2015]
Poverty is associated with:
a) Malnutrition
b) Lower life expectancy
c) Lower life expectancy and Higher infant mortality only
d) All of the THEM
e) Higher infant mortality

### PH-M-136
tier: open
form: mcq
type: single
models: [2015]
Mrs. Samia is 32 years old who is now divorced and has four children. This is an n example of:
a) Blended family
b) Nuclear family
c) Alternative family
d) Single parent family

### PH-M-137
tier: open
form: mcq
type: single
models: [2015]
Supernatural theory: Disease is caused by the odor of decaying of organic materials.
a) False
b) True

### PH-M-138
tier: open
form: mcq
type: single
models: [2015]
Development is:
a) Encompasses the total well-being of individual, a community or a nation
b) Must be measured by the rate of economic growth.
c) Concerned with the total person, his economic, social, political, physiological, and psychic and
d) All of the them
e) None of them

### PH-M-139
tier: open
form: mcq
type: single
models: [2015]
Physicians are the largest group employed in public health
a) False
b) True

### PH-M-140
tier: open
form: mcq
type: single
models: [2015]
Marginal participation of people in the health programs may be limited and temporary.
a) True
b) False

### PH-M-141
tier: open
form: mcq
type: single
models: [2015]
Culture includes knowledge, belief, art, morale, law, customs, habits and other capabilities acquired by
man as a member of society.
a) True
b) False

### PH-M-142
tier: open
form: mcq
type: single
models: [2015]
Hippocrates is considered the father of eastern medicine.
a) False
b) True

### PH-M-143
tier: open
form: mcq
type: single
models: [2015]
Which of the following is the best definition of public health?
a) None of them
b) Ensuring the health of the individual by maintaining and improving the health of the community
c) A complete state of physical, mental and social wellbeing and not merely the absence of disease.
d) The science and art of preventing disease, prolonging life, and promoting health through the
e) All of these are great definitions

### PH-M-144
tier: open
form: mcq
type: single
models: [2015]
Culture is one of the determinants of health among the environmental factors.
a) True
b) False

### PH-M-145
tier: open
form: mcq
type: single
models: [2015]
Spiritual health is the ability of expressing emotions in the appropriate way, for example to fear, to be
happy, and to be angry.
a) True
b) False

### PH-M-146
tier: open
form: mcq
type: single
models: [2015]
Some problematic behaviors are given the status of disease in DSM:
a) Drug abuse
b) Alcohol abuse and dependence
c) Conduct disorders in children
d) All of the them

### PH-M-147
tier: open
form: mcq
type: single
models: [2015]
Mental disorders represent a “clinically significant behavioral or psychological syndrome or pattern that
occurs in an individual and that is associated with present distress (e.g., a painful symptom) or disability.
a) True
b) False

### PH-M-148
tier: open
form: mcq
type: single
models: [2015]
Lifespan is shortest in which of the following regions?
a) United States
b) Northern Europe
c) South America
d) East Asia
e) Sub-Saharan Africa

### PH-M-149
tier: open
form: mcq
type: single
models: [2015]
A family of preschool children encounters all the following tasks, except:
a) adjusting to the role of mother and father
b) maintain safety of children as they move around in the environment
c) separation of children from parents and starting school
d) maintain marital relationship as parents focus more on children and give less time to their

### PH-M-150
tier: open
form: mcq
type: single
models: [2015]
Health plays a major role in:
a) Reducing poverty.
b) Disease development.
c) None of them
d) All of the them
e) Promoting economic development.
f) Promoting economic development and Reducing poverty

### PH-M-151
tier: open
form: mcq
type: single
models: [2015]
note: Source carries a handwritten-style Arabic annotation next to this stem reading
  "في جوابين صح" ("there are two correct answers") -- excluded from the stem per
  the interface-text convention, but recorded here since it is informative
  content, not UI chrome. It does not specify which two options, and the
  question itself still prints "Select one", so this is left tier open rather
  than guessed at.
Nineteen-century models of disease causation Theories includes:
a) None of them
b) The environmental theory
c) Miasma theory
d) All of them
e) Supernatural theory.

### PH-M-152
tier: open
form: mcq
type: single
models: [2015]
Decentralization is:
a) Brings decision closer to the communities served and the field level providers of services &
b) Sharing and transferring power and decision away from the center to the periphery & . Brings
c) Keeping all of the important decision making powers within head office
d) Leads to greater efficiency in service provision
e) Brings decision closer to the communities served and the field level providers of service
f) Sharing and transferring power and decision away from the center to the periphery.

### PH-M-153
tier: open
form: mcq
type: single
models: [2015]
Contagion theory is not accepted because too many instances where people become ill regardless of
their isolation from human contact.
a) True
b) false

### PH-M-154
tier: open
form: mcq
type: single
models: [2015]
The effects of Globalization on health are diverse; these can be:
a) Positive.
b) Mixed.
c) All of them
d) Negative.

### PH-M-155
tier: open
form: mcq
type: single
models: [2015]
Public health does which of the following:
a) Provides conditions conducive to health
b) All of the them
c) Mobilizes communities
d) Promotes healthy lifestyles
e) Mobilizes communities & Promotes healthy lifestyles

### PH-M-156
tier: open
form: mcq
type: single
models: [2015]
The Study of distribution and determinants of disease and injuries in human population is
a) Research
b) Epidemiology
c) Demography
d) Ecology

### PH-M-157
tier: open
form: mcq
type: single
models: [2015]
Primary Health care philosophy includes except
a) Equity and Justice
b) Individual and community self reliance
c) Reorientation of Health manpower
d) Inter relationship of Health and Development

### PH-M-158
tier: open
form: mcq
type: single
models: [2015]
Universal package promotes broader support among population and health providers than schemes
targeting poor alone—such support helps to sustain financing over time.
a) True
b) False

### PH-M-159
tier: open
form: mcq
type: single
models: [2015]
Infant mortality rate is measured by :
a) per 100 000 live births
b) per 1000 live births
c) None of them
d) per 10000 live births

### PH-M-160
tier: open
form: mcq
type: single
models: [2015]
Health care PROVISION in Palestine consist of:
a) The public sector: the MOH and the security forces medical services & United Nation Relief and
b) United Nation Relief and Working Agency (UNRWA) & NGOs & private for-profit
c) United Nation Relief and Working Agency (UNRWA)
d) NGOs & private for-profit
e) The public sector: the MOH and the security forces medical services
f) All of them

### PH-M-161
tier: open
form: mcq
type: single
models: [2015]
It affects the health of a community include the beliefs, traditions, and social customs in the community.
It also involves the economy, politics and religion in the community.
a) physical determinants
b) biological determinants
c) behavioral determinants
d) Socio – cultural determinants

### PH-M-162
tier: open
form: mcq
type: single
models: [2015]
Intersectoral Collaboration: Means a joint concern and responsibility of sectors responsible for
development in identifying problems, programs and undertaking tasks that have important bearing on
human well-being.
a) True
b) False

### PH-M-163
tier: open
form: mcq
type: single
models: [2015]
The George Washington of Public Health is…
a) Willian Harvey
b) John Snow
c) Edward Jenner
d) Louis Pateur

### PH-M-164
tier: open
form: mcq
type: single
models: [2015]
PHC components are:
a) Health Education & Provision of essential drugs
b) Immunization, MCH & FP and Communicable disease control & food supply and proper nutrition
c) Immunization, MCH & FP
d) All of them
e) Communicable disease control & food supply and proper nutrition

### PH-M-165
tier: open
form: mcq
type: single
models: [2015]
The declaration outlined the central concern of the global community and articulated a set of
interconnected and mutually reinforcing goals for sustainable development
a) Health Determinants
b) Millennium developmental goals
c) Health Development
d) Almata declaration

### PH-M-166
tier: open
form: mcq
type: single
models: [2015]
Relationship between social attitudes toward mental illness and the course of mental disorders—effects
of stigma, discrimination, and social exclusion are example of social and environmental factors
impacting mental health.
a) True
b) False

### PH-M-167
tier: open
form: mcq
type: single
models: [2015]
Industrialization and urbanization in the 19th Century helped to solve public health problems.
a) True
b) False

### PH-M-168
tier: open
form: mcq
type: single
models: [2015]
Economic Growth is concerned with the total person, his economic, social, political, physiological, and
psychic and environmental requirements.
a) False
b) True

### PH-M-169
tier: open
form: mcq
type: single
models: [2015]
Elements incorporated after Alma-Ata are except
a) Use of traditional medicine
b) Mental Health
c) Occupational health
d) Social health
e) Oral Health

### PH-M-170
tier: open
form: mcq
type: single
models: [2015]
The Multi Causal Theory concentrates on disease prevention, instead of requiring medical treatments or
personal hygiene, demands change in the industrial production.
a) True
b) False

### PH-M-171
tier: open
form: mcq
type: single
models: [2015]
Factors that hinder great involvement of the community in health includes:
a) The professional staff generally takes decisions in health services and there is no tradition of
b) Lack of flexibility in health service and general unwillingness to change.
c) Rigid professional behavior of health service provides, which need to be strengthened to allow
d) Wrong assumption by health staff that community does not know what is good for them and that
e) All of the them

### PH-M-172
tier: open
form: mcq
type: single
models: [2015]
The family is the primary social context in which health promotion and disease prevention take place.
a) True
b) False

### PH-M-173
tier: open
form: mcq
type: single
models: [2015]
Types of community participation/involvement are structural, horizontal and substantial.
a) False
b) True

### PH-M-174
tier: open
form: mcq
type: single
models: [2015]
When the psychological needs of family members are not met, symptoms of family dysfunction result.
a) False
b) True

### PH-M-175
tier: open
form: mcq
type: single
models: [2015]
Dysfunctional families and poor parenting can lead to:
a) Alcoholism and substance-abuse in the family
b) Overindulgence
c) Gambling problems
d) All of the them
e) Domestic violence
f) Child abuse – neglect, physical abuse, verbal abuse, sexual abuse

### PH-M-176
tier: open
form: mcq
type: single
models: [2015]
What are the criteria for the technology to be appropriate?
a) Efficient
b) All of them
c) Equitable
d) Locally sustainable & Equitable only
e) Locally sustainable
f) Affordable

### PH-M-177
tier: open
form: mcq
type: single
models: [2015]
The mission of Health Promotion is “fulfilling society’s interest in assuring conditions in which people
can be healthy.
a) True
b) False
