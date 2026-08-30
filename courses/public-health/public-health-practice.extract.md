---
course: public-health
tab: practice
questions: 132
tiers: claimed 131 | open 1
forms: mcq 132
needs-eye: 0
disputed: 0
next-id: PH-P-133
---

<!-- batch 01 -- raw/practice/Public Health PYQ& bank question 2023@Fawzi,Ali,Malik.pdf,
  pages 1-32 of 64. RUN-PLAN row 5: this batch runs first because it's free (real
  text layer throughout, confirmed by prep.py -- 0 vision pages). Pages 33-64 (the
  epidemiological study-design/2x2-table sections) are a separate row (6), not
  covered here.

  IMPORTANT correction made after this batch's first pass: the document's real
  answer-mark is BOLD TEXT (Calibri-Bold vs. plain Calibri on the option lines),
  not a capitalized option letter. Capitalization looked plausible at a glance --
  it agrees with bold on most of the first 25 questions -- but it is unreliable
  and frequently disagrees with, or is entirely silent about, the actual bold
  mark: some questions have a capitalized letter that is NOT bold (decorative or
  a typo) while the true bold answer sits on a different, lowercase option; a
  large stretch of questions (the fifth section below) has no capitalized letter
  at all yet every one of them carries a real bold answer. A first draft of this
  file, built from capitalization alone, mis-answered roughly 50 questions and
  flagged two false disputes. It was corrected in place by re-deriving every
  answer from each PDF page's actual font/bold span data (PyMuPDF's `get_text
  ("dict")`, checking `Bold` in the span's font name) before this file was
  committed. Anyone extending this extract (row 6 onward) must check bold, not
  capitalization -- and must further check that bold actually discriminates
  within a question, since a later stretch of this same source (rows 6+) turns
  out to bold every option uniformly on some pages, which carries no information
  at all and must be read as unmarked.

  Page 1 is a title page, credited "Ali Shaban, Fawzi Shihadeh, Malik Suliman." Its
  three embedded images (a stock photo captioned "Public Health", two decorative
  flourishes) were checked and are purely decorative -- no question on pages 1-32
  depends on an image. Page 1 also carries a handful of stray isolated characters
  ("RE", "a?", "card", "4>") that don't attach to any sentence -- an artifact of
  the page's own layout/OCR layer bleeding through, not a dropped fragment of any
  question. Page 2 opens with an Arabic disclaimer from the compilers ("Note: our
  answers, God willing... any mistake is from us, any correctness is from God") --
  standard humility framing, not content, discarded per the Arabic-is-interface
  rule.

  The source is five back-to-back sections, each restarting its own numbering at 1
  (not just at the three points named in the course's own RUN-PLAN header note --
  a sixth restart turned up mid-file):
    p2-8    unlabeled first section (25 Q, "WHO 1986 definition of health..." to
            "process of globalization"). PH-P-001 through PH-P-025.
    p8-10   "Research Methodology -Midterm exam2023" (7 Q, restarts at 1), preceded
            by the compiler's own un-transcribed study note ("Time + big number of
            participants = cohort", etc. -- kept out of the question stream, it
            isn't a question). PH-P-026 through PH-P-030 (5 new; its Q1 and Q6
            duplicate stems from the first section, see below).
    p10     unlabeled third section (3 Q, restarts at 1, "basic assumption of
            health Promotion" / corona-Beit-Hanina / proximal determinant). PH-P-031
            through PH-P-033.
    p11-21  "main insurance program scheme in Palestine..." (49 Q, restarts at 1).
            Per the course's own RUN-PLAN header note, this is a verbatim
            reproduction of the 2015 midterm (same Q1) -- its answers here are the
            only key that midterm will ever have; cross-reference this batch when
            row 12 extracts raw/midterm/2015/Mid Exam P.H. 2015.pdf. PH-P-034
            through PH-P-082. Only one question in this whole section (PH-P-041,
            "Mrs. Samia... divorced... four children") carries no bold option at
            all -- genuinely open, not a read miss.
    p21-32  unlabeled fifth section (50 Q, restarts at 1, "Public health does
            which of the following" to "leading infectious cause of death").
            PH-P-083 through PH-P-132. This is the section whose questions carry
            almost no capitalized letters yet turn out fully bold-marked once
            checked properly -- every one of its 50 questions is tier claimed.
            Two genuine numbering gaps are in the source itself, not a read
            failure: Q3 never appears (page boundary p21/p22), and Q9 never
            appears (page boundary p22/p23, where the source also prints two
            consecutive "8."s -- both transcribed, PH-P-089/090).

  Net result: 131 of 132 questions in this batch are claimed tier; PH-P-041 is
  the sole open one. Zero disputes survive the bold re-check -- both of the
  original draft's "disputed" calls (a merged duplicate and a True/False item)
  turned out to be one side reading a bold mark correctly and the other reading
  a decorative capital letter that was never actually the answer.

  Duplicates merged within this batch (same stem, one entry, per the batch-merge
  rule): the "cancer patients randomly assigned...chemotherapy" question (first
  section Q17 = Research Methodology Q1, verbatim aside from "effect"/"effects"
  and "each"/"cach" typos) merged into PH-P-017, both sides agreeing on answer a.
  The "study that measures the incidence of a disease" question (first section
  Q20 vs Research Methodology Q6) merged into PH-P-020 -- both copies' bold marks
  agree on d (Cohort), even though their capitalized letters disagreed (b vs. c
  and d both capitalized).

  Several near-miss pairs share a topic or near-identical stem but differ enough
  in wording or option set that they were kept as separate entries rather than
  merged, per the pharmacology-practice precedent (row 11) for this exact
  situation -- each is cross-noted on both entries: PH-P-003/PH-P-042 (major
  determinants of health -- same four option-contents, reshuffled letters, both
  independently pick the same underlying option), PH-P-008/PH-P-118
  (epidemiological transition, differently worded but the same real-world answer),
  PH-P-040/PH-P-094 (poverty is associated with, different option sets, both land
  on their own "all of the above"-style option), PH-P-060/PH-P-083 ("Public
  health does which of the following", reshuffled options, both land on their own
  "all of them"-style option).

  PH-P-023 (first section Q23) has an Arabic annotation living inside the bold
  (correct) option c's own text in the source ("هكذا تم احتسابها في السنة
  السابقة" -- "this is how it was counted in the previous year") -- a compiler's
  aside confirming the same answer held in an earlier year too. Recorded as a
  note on the entry rather than folded into the option text, since it isn't part
  of the option itself. PH-P-027 (Research Methodology Q3) is missing its "a."
  label in the source for the first option -- transcribed positionally as (a),
  nothing invented. PH-P-031 has only 3 options (a-c) in the source, no d -- its
  correct shape, not a structural failure. PH-P-120 preserves the source's own
  typo "ymptoms" for "Symptoms" verbatim. -->

### PH-P-001
tier: claimed
form: mcq
type: single
claimed: d
WHO 1986 definition of health is?
a) Ensuring the health of the individual by maintaining and improving the health of the community.
b) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science.
c) A complete state of physical, mental, and social wellbeing and not merely the absence of disease.
d) Health is the extent to which an individual or group is able, on the one hand, to realize aspirations and safety needs; and, on the other hand, to change or cope with the environment. It is to be seen as a resource for everyday life and not merely the objective of living.

### PH-P-002
tier: claimed
form: mcq
type: single
claimed: d
All of the following are considered functions of public health, Except?
a) Mobilizes communities for health.
b) Provides conditions conducive to health.
c) Promotes healthy lifestyles.
d) Heart transplant operation in specialized heart medical center

### PH-P-003
tier: claimed
form: mcq
type: single
claimed: b
note: near-miss of PH-P-042 -- same four option-contents reshuffled; both entries independently pick the "Human biology, Environment, Lifestyle behavior, Health care organization" option despite the different letter.
Which of the following are the major determinants of health?
a) Human biology, Socio-demographic, Behavioural, Physical.
b) Human biology, Environment, Lifestyle behavior, Health care organization.
c) Community organization, Environment, Socio-demographic, culture.
d) Human biology, culture, Behavioural, Health care organization.

### PH-P-004
tier: claimed
form: mcq
type: single
claimed: d
The following are determinant of inequities Except?
a) Health damaging behaviors.
b) Exposure to unhealthy, stressful living and working conditions.
c) Inadequate access to essential health and other public services.
d) Differences in the incidence and prevalence of health conditions and health status between groups.

### PH-P-005
tier: claimed
form: mcq
type: single
claimed: b
_____ affects the health of a community and it includes the geography (e.g., High land versus low land), the environment (e.g., Manmade or natural catastrophes) and the industrial development (e.g., pollution occupational hazards)?
a) Socio - cultural determinants
b) physical determinants.
c) behavioral determinants
d) biological determinants.

### PH-P-006
tier: claimed
form: mcq
type: single
claimed: a
Maternal mortality ratio is defined as?
a) The ratio of the number of maternal deaths during a given time period per 100,000 live births during the same time-period.
b) The ratio of maternal deaths during a given period per 1000 deliveries during the same period of time.
c) The ratio of maternal deaths due to all causes during a given period per 1000 deliveries during the same period of time.
d) The ratio of maternal deaths due to hypertension during a given period per 1000 deliveries during the same period of time.

### PH-P-007
tier: claimed
form: mcq
type: single
claimed: c
Infant mortality rate is the number of deaths of infants under one year old measured per?
a) 100 000 live births.
b) 10000 live births.
c) 1000 live birth.
d) 100 live births.

### PH-P-008
tier: claimed
form: mcq
type: single
claimed: a
note: near-miss of PH-P-118 -- same topic, differently worded question and options.
Epidemiological transition refers to?
a) The change of mortality from infectious diseases to degenerative diseases.
b) A change in levels of diabetes in overweight adults.
c) The changing prevalence of vitamin D deficiency.
d) The change in birth defects due to genetic abnormalities.

### PH-P-009
tier: claimed
form: mcq
type: single
claimed: d
The health and wellbeing of the community is dependent on a good start, good future, good care and support. These include social, economic, physical and environmental factors which are known as?
a) A person's health.
b) Health promotion.
c) Public Health.
d) Determinants of health.

### PH-P-010
tier: claimed
form: mcq
type: single
claimed: b
_____ is the difference in health care which is not only unnecessary and avoidable but unfair and unjust?
a) Health equity.
b) Health inequity.
c) Health disparities.
d) Health equality.

### PH-P-011
tier: claimed
form: mcq
type: single
claimed: b
The primary purpose of social determinants of health is to ensure?
a) The importance of providing medical treatment for chronic diseases.
b) The importance of reducing inequity within population.
c) The multi-sectoral approach in promoting health and preventing illness in the population.
d) The involvement of people in designing and implementing health interventions.

### PH-P-012
tier: claimed
form: mcq
type: single
claimed: a
Health illness continuum, it is?
a) The line between optimal health and death, people are moving on this line according to their social conditions.
b) People are not easy to move on the continuum if they are rich,
c) All of the above
d) None of the above

### PH-P-013
tier: claimed
form: mcq
type: single
claimed: c
Major public health achievements in the 20th century Except?
a) Seat belts.
b) Tobacco as a health risk.
c) Discovery of CT scans.
d) Vaccines.

### PH-P-014
tier: claimed
form: mcq
type: single
claimed: a
Economic and social relationships, employment, housing, and education that contribute to or detract from the health of individuals and communities are known as the---------?
a) Social determinants of health
b) Community factors in health.
c) Environmental factors of health.
d) Perceived benefits of health.

### PH-P-015
tier: claimed
form: mcq
type: single
claimed: a
The epidemiologic analytical triad of disease causation refers to: (Choose one best answer)?
a) Agent, host, environment.
b) Time, place, person.
c) Source, mode of transmission, susceptible host.
d) John Snow, Robert Koch, Kenneth Rothman.

### PH-P-016
tier: claimed
form: mcq
type: single
claimed: c
________: differences in the incidence and prevalence of health conditions and health status between groups?
a) Health equity.
b) Health inequity.
c) Health disparities.
d) Health equality.

### PH-P-017
tier: claimed
form: mcq
type: single
claimed: a
note: merged with the Research Methodology section's Q1 -- identical stem/options aside from "effect"/"effects" and "each"/"cach" typos, same claimed answer.
A study in which cancer patients are randomly assigned to receive either a newly formulated chemotherapy or the currently available chemotherapy, and are followed to monitor for side effect and effectiveness of each drug, is an example of which type of study?
a) Interventional.
b) Observational.
c) Cohort.
d) Ecological.

### PH-P-018
tier: claimed
form: mcq
type: single
claimed: a
Comparison of study designs: .... Best for rare diseases?
a) Case Control Studies.
b) Prospective Cohort Studies.
c) Descriptive Studies.
d) Cross Sectional Studies.

### PH-P-019
tier: claimed
form: mcq
type: single
claimed: a
A prevalence rate is?
a) The total number of cases of a disease existing in a population divided by the total population.
b) The number of new cases of a disease divided by the number of persons at risk for the disease.
c) The number of new cases of a disease divided by the number of all cases of a disease.
d) None of the above.

### PH-P-020
tier: claimed
form: mcq
type: single
claimed: d
note: merged from two occurrences of the same stem (first section Q20, Research Methodology section Q6) -- both copies agree on d (Cohort) once the source's real answer-mark (bold text) is checked rather than its capitalized letters, which are unreliable in this document and disagree with each other and with the bold mark on both copies.
A study that measures the incidence of a disease?
a) Case report
b) Cross sectional.
c) Case control
d) Cohort.

### PH-P-021
tier: claimed
form: mcq
type: single
claimed: b
Which of the following is a case-control study?
a) Analysis of previous research in different places and under different circumstances to permit establishment of a hypothesis based on cumulative knowledge of all known factors identified in the disease under study.
b) Obtaining histories and other information from a group of people with a particular disease or condition and from a group without the disease to determine the relative frequency of a past exposure under study.
c) Defining a group of disease free people by their exposure status and then following up over time to see which ones develop a disease or condition.
d) Study of average exposure for a group and a population measure of outcome.

### PH-P-022
tier: claimed
form: mcq
type: single
claimed: b
A study was conducted to investigate the effect of HIV infection on mortality among people in Kenya with TB. Individuals with TB were recruited from hospitals and their HIV status determined. They were then followed-up over ten years to compare mortality rates in the HIV positive group and HIV negative group?
a) Case-control study.
b) Cohort study.
c) Randomized controlled trial.
d) Ecological study.

### PH-P-023
tier: claimed
form: mcq
type: single
claimed: c
note: the source's real answer-mark (bold text, not the unreliable capitalized "D") lands on option c, which also carries an Arabic annotation, "هكذا تم احتسابها في السنة السابقة" ("this is how it was counted in the previous year") -- a compiler's aside confirming this same answer held in an earlier year too.
In the Netherlands there is an increase in the prevalence of cardiovascular diseases. This is a consequence of?
a) deterioration of the food pattern.
b) increase in hypertension.
c) improved treatment.
d) increase in obesity.

### PH-P-024
tier: claimed
form: mcq
type: single
claimed: b
In an epidemiological context, what is the population at risk?
a) The proportion of a population that engage in risky behaviours.
b) The group of people that may experience the outcome we want to study.
c) A group of people participating in a study that may be harmful to them.
d) The population group with the highest relative risk of disease.

### PH-P-025
tier: claimed
form: mcq
type: single
claimed: c
Which definition best describe the process of globalization?
a) Capitalist companies are spreading across the planet.
b) We all now live in a single society.
c) Individuals, groups and nations are becoming more interdependent.
d) Human beings now live on every continent of the planet.

### PH-P-026
tier: claimed
form: mcq
type: single
claimed: b
Type of design where both exposure and disease are determined at the same time for each subject?
a) Case study.
b) Cross sectional study.
c) Case control study.
d) Cohort study.

### PH-P-027
tier: claimed
form: mcq
type: single
claimed: d
note: the source prints the first option without an "a." label; transcribed positionally as (a), nothing invented.
What does the term 'longitudinal design' mean?
a) A study completed far away from where the researcher lives.
b) A study which is very long to read.
c) A study with two contrasting cases.
d) A study completed over a distinct period of time.

### PH-P-028
tier: claimed
form: mcq
type: single
claimed: b
Occurrence of lung cancer was identified between May 1970 and July 2010 for 200,000 Japanese men who were regular smokers and 500,000 Japanese men who never smoked during the same period. This is an example of?
a) Cross-sectional Study.
b) Prospective Cohort Study.
c) Case report Study.
d) Experimental Study.

### PH-P-029
tier: claimed
form: mcq
type: single
claimed: a
A cross sectional study is carried out to examine whether Navy personnel of a higher rank have more positive coping skills than those of a lower rank. Which of the following statements is true regarding this study?
a) The independent variable is rank, and the dependent variable is coping skills.
b) The independent variable is coping, and the dependent variable is low rank.
c) The independent variable is coping, and the dependent variable is high rank.
d) Neither variable is dependent as the researcher cannot manipulate them.

### PH-P-030
tier: claimed
form: mcq
type: single
claimed: c
If the experimental design is lacking the element of randomization, then the study may be called?
a) Randomized control trial.
b) Descriptive.
c) Quasi-experimental study.
d) Experimental with external control.

### PH-P-031
tier: claimed
form: mcq
type: single
claimed: c
note: only 3 options are present in the source (a-c), no d -- its correct shape, not a structural failure.
The following are basic assumption of health Promotion?
a) Health status can be changed.
b) It is difficult to understand the causes of a disease and various risk factors.
c) Once health problems are identified preventive strategies can be developed.

### PH-P-032
tier: claimed
form: mcq
type: single
claimed: a
Which of the following studies apply to this: Occurrence of corona was identified between April 2020 and July 2020 for 5000 residents of Beit Hanina were infected and 5000 residents who infected elsewhere during the same period.?
a) Observational cohort
b) Experimental.
c) Observational case-control.
d) Observational cross sectional.

### PH-P-033
tier: claimed
form: mcq
type: single
claimed: c
A determinant that is clearly related to a change in health status is defined as a?
a) Distal determinant.
b) social determinant.
c) Proximal determinant.
d) Ecological determinant.

### PH-P-034
tier: claimed
form: mcq
type: single
claimed: d
note: this section is a verbatim reproduction of the 2015 midterm (per the course's own RUN-PLAN header note) -- cross-reference when raw/midterm/2015/Mid Exam P.H. 2015.pdf is extracted.
The main insurance program scheme in Palestine is?
a) Most population without health insurance
b) Private Health Insurance
c) UNRWA health insurance
d) Government health insurance

### PH-P-035
tier: claimed
form: mcq
type: single
claimed: a
Prevention refers to the goals of medicine that are to promote, to preserve, and to restore health when it is impaired, and to minimize suffering and distress?
a) True.
b) False

### PH-P-036
tier: claimed
form: mcq
type: single
claimed: c
Reasons to Study Global Health?
a) To learn about low-cost but highly effective interventions.
b) Nature of many global health concerns.
c) All of them.
d) Need for different actors to work together.
e) Link between health and development.

### PH-P-037
tier: claimed
form: mcq
type: single
claimed: b
Which of the following is not a characteristic of healthy system?
a) The system should have feedback from the subsystems and the community at large.
b) The system should have completely open boundaries.
c) The system has ability to differentiate and grow through self-regulation and change.
d) The system has a hierarchy of systems such as parents, grandparents, and children.

### PH-P-038
tier: claimed
form: mcq
type: single
claimed: c
ARI in Almata conference stands for Select one?
a) None of them
b) Autism Research Institute
c) Acute respiratory infection
d) Air resource institute

### PH-P-039
tier: claimed
form: mcq
type: single
claimed: b
The Millennium Development Goals (MDGs) is?
a) Eradication of extreme poverty and hunger.
b) All of them.
c) Combating HIV/AIDS, malaria and other diseases.
d) Improvement in maternal health.
e) Reduction of child mortality.

### PH-P-040
tier: claimed
form: mcq
type: single
claimed: d
note: near-miss of PH-P-094 -- same topic, different option set.
Poverty is associated with?
a) Malnutrition
b) Lower life expectancy
c) Lower life expectancy and Higher infant mortality only
d) All of the THEM.
e) Higher infant mortality

### PH-P-041
tier: open
form: mcq
type: single
Mrs. Samia is 32 years old who is now divorced and has four children. This is an example of?
a) Blended family.
b) nuclear family.
c) Alternative family.
d) Single parent family.

### PH-P-042
tier: claimed
form: mcq
type: single
claimed: a
note: near-miss of PH-P-003 -- same four option-contents reshuffled; both entries independently pick the "Human biology, Environment, Lifestyle behavior, Health care organization" option despite the different letter.
The four major determinants of health are Select one?
a) Human biology, Environment, Lifestyle, Health care organization.
b) Community organization, Environment, Socio-demographic, culture.
c) Human biology, culture, Behavioural, Health care organization.
d) Human biology, Socio-demographic, Behavioural, Physical.

### PH-P-043
tier: claimed
form: mcq
type: single
claimed: a
Supernatural theory: Disease is caused by the odor of decaying of organic materials?
a) False.
b) True.

### PH-P-044
tier: claimed
form: mcq
type: single
claimed: d
Development is?
a) Encompasses the total well-being of individual, a community or a nation.
b) Must be measured by the rate of economic growth.
c) Concerned with the total person, his economic, social, political, physiological, and psychic and environmental requirements.
d) All of the them.
e) None of them.

### PH-P-045
tier: claimed
form: mcq
type: single
claimed: b
Physicians are the largest group employed in public health?
a) False.
b) True.

### PH-P-046
tier: claimed
form: mcq
type: single
claimed: a
Marginal participation of people in the health programs may be limited and temporary?
a) True.
b) False

### PH-P-047
tier: claimed
form: mcq
type: single
claimed: a
Culture includes knowledge, belief, art, morale, law, customs, habits and other capabilities acquired by man as a member of society?
a) True.
b) False

### PH-P-048
tier: claimed
form: mcq
type: single
claimed: a
Hippocrates is considered the father of eastern medicine?
a) False.
b) True.

### PH-P-049
tier: claimed
form: mcq
type: single
claimed: d
note: source appends a study note after this question, explaining the relative priority of the Mobilizing/Winslow/Ensuring definitions when several appear together as options -- kept as document context, not transcribed as a question.
Which of the following is the best definition of public health?
a) None of them
b) Ensuring the health of the individual by maintaining and improving the health of the community.
c) A complete state of physical, mental and social wellbeing and not merely the absence of disease.
d) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science.
e) All of these are great definitions.

### PH-P-050
tier: claimed
form: mcq
type: single
claimed: a
Culture is one of the determinants of health among the environmental factors.?
a) True.
b) False

### PH-P-051
tier: claimed
form: mcq
type: single
claimed: b
Spiritual health is the ability of expressing emotions in the appropriate way, for example to fear, to be happy, and to be angry.
a) True
b) False.

### PH-P-052
tier: claimed
form: mcq
type: single
claimed: d
Some problematic behaviors are given the status of disease in DSM?
a) Drug abuse
b) Alcohol abuse and dependence.
c) Conduct disorders in children.
d) All of the them.

### PH-P-053
tier: claimed
form: mcq
type: single
claimed: a
Mental disorders represent a "clinically significant behavioral or psychological syndrome or pattern that occurs in an individual and that is associated with present distress (e.g., a painful symptom) or disability?
a) True.
b) False.

### PH-P-054
tier: claimed
form: mcq
type: single
claimed: e
Lifespan is shortest in which of the following regions?
a) United States.
b) Northern Europe.
c) South America.
d) East Asia.
e) Sub-Saharan Africa.

### PH-P-055
tier: claimed
form: mcq
type: single
claimed: a
A family of preschool children encounters all the following tasks, except?
a) adjusting to the role of mother and father.
b) maintain safety of children as they move around in the environment.
c) separation of children from parents and starting school.
d) maintain marital relationship as parents focus more on children and give less time to their marriage.

### PH-P-056
tier: claimed
form: mcq
type: single
claimed: d
Health plays a major role in?
a) Reducing poverty.
b) Disease development.
c) None of them.
d) All of the them.
e) Promoting economic development.
f) Promoting economic development and Reducing poverty.

### PH-P-057
tier: claimed
form: mcq
type: single
claimed: b
Decentralization is?
a) Brings decision closer to the communities served and the field level providers of services & Keeping all of the important decision making powers within head office & Leads to greater efficiency in service provision.
b) Sharing and transferring power and decision away from the center to the periphery &. Brings decision closer to the communities served and the field level providers of services & Leads to greater efficiency in service provision.
c) Keeping all of the important decision making powers within head office.
d) Leads to greater efficiency in service provision.
e) Brings decision closer to the communities served and the field level providers of service.
f) Sharing and transferring power and decision away from the center to the periphery.

### PH-P-058
tier: claimed
form: mcq
type: single
claimed: a
Contagion theory is not accepted because too many instances where people become ill regardless of their isolation from human contact?
a) True.
b) false.

### PH-P-059
tier: claimed
form: mcq
type: single
claimed: c
The effects of Globalization on health are diverse; these can be?
a) Positive.
b) Mixed.
c) All of them.
d) Negative.

### PH-P-060
tier: claimed
form: mcq
type: single
claimed: b
note: near-miss of PH-P-083 -- same stem, reshuffled options with a different combo-answer.
Public health does which of the following?
a) Provides conditions conducive to health.
b) All of them.
c) Mobilizes communities.
d) Promotes healthy lifestyles.
e) Mobilizes communities & Promotes healthy lifestyles.

### PH-P-061
tier: claimed
form: mcq
type: single
claimed: b
The Study of distribution and determinants of disease and injuries in human population is?
a) Research
b) Epidemiology.
c) Demography
d) Ecology

### PH-P-062
tier: claimed
form: mcq
type: single
claimed: c
Primary Health care philosophy includes except?
a) Equity and Justice.
b) Individual and community self-reliance.
c) Reorientation of Health manpower.
d) inter relationship of health and Development.

### PH-P-063
tier: claimed
form: mcq
type: single
claimed: b
Universal package promotes broader support among population and health providers than schemes targeting poor alone -- such support helps to sustain financing over time.?
a) True
b) False.

### PH-P-064
tier: claimed
form: mcq
type: single
claimed: b
Infant mortality rate is measured by?
a) per 100 000 live births.
b) per 1000 live births.
c) None of them.
d) per 10000 live births.

### PH-P-065
tier: claimed
form: mcq
type: single
claimed: f
Health care PROVISION in Palestine consist of?
a) The public sector: the MOH and the security forces medical services & United Nation Relief and Working Agency (UNRWA).
b) United Nation Relief and Working Agency (UNRWA) & NGOs & private for-profit.
c) United Nation Relief and Working Agency (UNRWA).
d) NGOs & private for-profit.
e) The public sector: the MOH and the security forces medical services.
f) All of them.

### PH-P-066
tier: claimed
form: mcq
type: single
claimed: d
It affects the health of a community, include the beliefs, traditions, and social customs in the community. It also involves the economy, politics and religion in the community?
a) physical determinants
b) biological determinants
c) behavioral determinants
d) Socio-cultural determinants.

### PH-P-067
tier: claimed
form: mcq
type: single
claimed: a
Intersectoral Collaboration: Means a joint concern and responsibility of sectors responsible for development in identifying problems, programs and undertaking tasks that have important bearing on human well-being?
a) True.
b) False

### PH-P-068
tier: claimed
form: mcq
type: single
claimed: b
The George Washington of Public Health is....?
a) Willian Harvey.
b) John Snow.
c) Edward Jenner.
d) Louis Pateur.

### PH-P-069
tier: claimed
form: mcq
type: single
claimed: d
PHC components are?
a) Health Education & Provision of essential drugs.
b) Immunization, MCH & FP and Communicable disease control & food supply and proper nutrition Only.
c) Immunization, MCH & FP.
d) All of them.
e) Communicable disease control & food supply and proper nutrition

### PH-P-070
tier: claimed
form: mcq
type: single
claimed: b
The declaration outlined the central concern of the global community and articulated a set of interconnected and mutually reinforcing goals for sustainable development?
a) Health Determinants.
b) Millennium developmental goals.
c) Health Development.
d) Almata declaration.

### PH-P-071
tier: claimed
form: mcq
type: single
claimed: a
Relationship between social attitudes toward mental illness and the course of mental disorders -- effects of stigma, discrimination, and social exclusion are example of social and environmental factors impacting mental health?
a) True.
b) False.

### PH-P-072
tier: claimed
form: mcq
type: single
claimed: b
Industrialization and urbanization in the 19th Century helped to solve public health problems?
a) True
b) False.

### PH-P-073
tier: claimed
form: mcq
type: single
claimed: a
Economic Growth is concerned with the total person, his economic, social, political, physiological, and psychic and environmental requirements?
a) False.
b) True.

### PH-P-074
tier: claimed
form: mcq
type: single
claimed: d
Elements incorporated after Alma-Ata are except?
a) Use of traditional medicine.
b) Mental Health.
c) Occupational health.
d) Social health.
e) Oral Health.

### PH-P-075
tier: claimed
form: mcq
type: single
claimed: a
The Multi Causal Theory concentrates on disease prevention, instead of requiring medical treatments or personal hygiene, demands change in the industrial production?
a) True.
b) False.

### PH-P-076
tier: claimed
form: mcq
type: single
claimed: e
Factors that hinder great involvement of the community in health includes?
a) The professional staff generally takes decisions in health services and there is no tradition of allowing people to be involved in decision making.
b) Lack of flexibility in health service and general unwillingness to change.
c) Rigid professional behavior of health service provides, which need to be strengthened to allow greater community involvement.
d) Wrong assumption by health staff that community does not know what is good for them and that only health staff can determine their needs.
e) All of the them.

### PH-P-077
tier: claimed
form: mcq
type: single
claimed: a
The family is the primary social context in which health promotion and disease prevention take place?
a) True.
b) False.

### PH-P-078
tier: claimed
form: mcq
type: single
claimed: a
Types of community participation/involvement are structural, horizontal and substantial?
a) False.
b) True.

### PH-P-079
tier: claimed
form: mcq
type: single
claimed: b
When the psychological needs of family members are not met, symptoms of family dysfunction result?
a) False.
b) True.

### PH-P-080
tier: claimed
form: mcq
type: single
claimed: d
Dysfunctional families and poor parenting can lead to?
a) Alcoholism and substance-abuse in the family.
b) Overindulgence.
c) Gambling problems.
d) All of the them.
e) Domestic violence
f) Child abuse -- neglect, physical abuse, verbal abuse, sexual abuse.

### PH-P-081
tier: claimed
form: mcq
type: single
claimed: b
What are the criteria for the technology to be appropriate?
a) Efficient.
b) All of them.
c) Equitable.
d) Locally sustainable & Equitable only.
e) Locally sustainable.
f) Affordable.

### PH-P-082
tier: claimed
form: mcq
type: single
claimed: a
The mission of Health Promotion is "fulfilling society's interest in assuring conditions in which people can be healthy?
a) True.
b) False.

### PH-P-083
tier: claimed
form: mcq
type: single
claimed: d
note: near-miss of PH-P-060 -- same stem, reshuffled options with a different combo-answer.
Public health does which of the following?
a) Mobilizes communities.
b) Provides conditions conducive to health.
c) Promotes healthy lifestyles.
d) All of the above.
e) a. and c. above.

### PH-P-084
tier: claimed
form: mcq
type: single
claimed: e
Which of the following is NOT a modern challenge of public health?
a) Emergence of new pathogens.
b) Persistence of old diseases due to drug resistance/mutation.
c) Growing burden of noncommunicable (chronic) diseases.
d) Globalization, social dislocation, and war.
e) All of these are modern challenges of public health.

### PH-P-085
tier: claimed
form: mcq
type: single
claimed: c
note: numbered "4." in the source -- "3." never appears anywhere in this batch, a genuine gap at the p21/p22 page boundary, not a read failure.
The major cause of poor health globally is?
a) Tobacco
b) Lack of exercise
c) Poverty
d) Environmental problems

### PH-P-086
tier: claimed
form: mcq
type: single
claimed: c
note: source appends a study note distinguishing "person, place, time" (the descriptive triad) from "agent, host, environment" (analytical epidemiology) -- kept as document context, not part of the question.
Which of the following is a "holy trinity" of epidemiology?
a) Time, place, agent
b) Person, place environment
c) Agent, host, environment.
d) Agent, environment, time
e) Person, host, environment

### PH-P-087
tier: claimed
form: mcq
type: single
claimed: a
Epidemiology is a body of knowledge gained from previous studies?
a) True.
b) False

### PH-P-088
tier: claimed
form: mcq
type: single
claimed: d
Epidemiologists describe disease factors in terms of?
a) Characteristics of affected individuals
b) Geographic area in which disease occurs
c) Temporal characteristics of the disease
d) All of the above

### PH-P-089
tier: claimed
form: mcq
type: single
claimed: c
note: the source numbers this "8." -- see PH-P-090.
Cohort study designs are?
a) Not suitable for study of infectious diseases.
b) Follow only exposed individuals over time.
c) Expensive and time-consuming to conduct.
d) Based on non-enumerated source populations.
e) Not suitable for study of occupational hazards.

### PH-P-090
tier: claimed
form: mcq
type: single
claimed: e
note: the source numbers this "8." as well -- printed twice in a row, and "9." never appears at all. Both anomalies are in the original document, not introduced here.
A study that compares the prevalence of suspected causal factors between those with and without disease is a/an?
a) Ecologic study
b) Cohort study
c) Experimental study
d) Meta-analysis
e) Case-control study.

### PH-P-091
tier: claimed
form: mcq
type: single
claimed: b
Incidence includes?
a) New cases.
b) New cases occurring in a defined time period.
c) Existing cases present at a single time point.
d) New cases, plus existing cases plus deaths.
e) New cases plus existing cases occurring in a defined time period

### PH-P-092
tier: claimed
form: mcq
type: single
claimed: c
Prevalence includes?
a) New cases.
b) New cases occurring in a defined time period.
c) Existing cases present at a single time point.
d) New cases, plus existing cases plus deaths.
e) New cases plus existing cases occurring in a defined time period.

### PH-P-093
tier: claimed
form: mcq
type: single
claimed: a
Epidemiology is the "core" science of public health?
a) True.
b) False

### PH-P-094
tier: claimed
form: mcq
type: single
claimed: d
note: near-miss of PH-P-040 -- same topic, different option set.
Poverty is associated with?
a) Malnutrition
b) Lower life expectancy
c) Higher infant mortality
d) All of the above
e) b. and c. above

### PH-P-095
tier: claimed
form: mcq
type: single
claimed: a
The goal of public health is to guarantee that all members of society achieve optimal health?
a) True.
b) False

### PH-P-096
tier: claimed
form: mcq
type: single
claimed: a
Health is a state of equilibrium between which of the following?
a) Agent-host-environment
b) Time-place-person
c) Agent-place-person
d) Agent-time-place
e) Host-environment-time

### PH-P-097
tier: claimed
form: mcq
type: single
claimed: a
For measuring prevalence, the numerator is?
a) Number of cases existing in a given population at a single point in time.
b) Number of new cases occurring in a given population in a specified time period.
c) Number of deaths due to a particular cause in a given population in a specified time period.
d) None of the above.

### PH-P-098
tier: claimed
form: mcq
type: single
claimed: e
note: option (e) is printed on the following page (p24/p25 boundary), stitched here.
Epidemiology is useful for?
a) Diagnosing disease in a patient.
b) Describing the clinical characteristics of diseases.
c) Identify precursors and risk factors for disease.
d) Assessing the cost-effectiveness of interventions.
e) b. and c. above.

### PH-P-099
tier: claimed
form: mcq
type: single
claimed: d
The "public health system" includes?
a) Employers
b) The community
c) The media
d) All of the above
e) a. and b. above

### PH-P-100
tier: claimed
form: mcq
type: single
claimed: e
The magnitude of disease burden can be measured by?
a) Morbidity/disability of the disease
b) Mortality of the disease
c) Economic cost from the disease
d) Prevalence
e) All of the above

### PH-P-101
tier: claimed
form: mcq
type: single
claimed: b
Epidemiology is a methodology of studying a health problem; it is not a body of Knowledge?
a) True
b) False

### PH-P-102
tier: claimed
form: mcq
type: single
claimed: d
The role of the public health professional is to?
a) Educate the public about ways to attain maximum health.
b) Alert the public to current health problems.
c) Anticipate future health problems.
d) All of the above
e) a. and b. above

### PH-P-103
tier: claimed
form: mcq
type: single
claimed: d
To avoid getting the flu you should:
a) Wash hands with soap and water or alcohol frequently.
b) Avoid contact with sick people.
c) Avoid crowded environments.
d) All of the above.
e) a. and b. above.

### PH-P-104
tier: claimed
form: mcq
type: single
claimed: b
The underlying cause of the most ill health world-wide is:
a) Smoking
b) Poverty
c) Environmental pollution
d) Inadequate health care
e) Poor nutrition

### PH-P-105
tier: claimed
form: mcq
type: single
claimed: a
The basic measure of functional loss due to disease is:
a) Disability-adjusted life years
b) Years of life lost
c) Incidence
d) Prevalence
e) Case fatality

### PH-P-106
tier: claimed
form: mcq
type: single
claimed: c
What are the three major functions of public health?
a) Assessment, assurance and cost containment
b) Assessment, health insurance, and medical services for the indigent and uninsured
c) Assessment, policy development, and assurance
d) Cost containment, health insurance, and medical services for the indigent
e) Health education, disease surveillance, and infectious disease control

### PH-P-107
tier: claimed
form: mcq
type: single
claimed: a
Which of the following services to advance health requires the least individual initiative?
a) Environmental improvements
b) Personal health services
c) Behavioral change
d) Adoption of good health habits
e) Selection of the optimal health care provider

### PH-P-108
tier: claimed
form: mcq
type: single
claimed: a
In epidemiologic studies, time, place and person(s) are used to characterize the relationship between:
a) Agent, host and environment.
b) Agent, host and person
c) Agent, environment and location
d) Agent, virus and person
e) Person, host and locale

### PH-P-109
tier: claimed
form: mcq
type: single
claimed: c
The numerator of prevalence of a disease in a population at a particular point of time is:
a) The number of new cases of the disease in the population occurring at the particular point in time
b) The total population at that particular point of time
c) The number of existing cases (new and old) of the disease in the population at that particular point in time
d) The number of cases cured of the disease in the population at a particular point in time

### PH-P-110
tier: claimed
form: mcq
type: single
claimed: b
note: option (e) is printed on the following page (p27/p28 boundary), stitched here.
Which of the following parameters is most useful to measure the impact of diseases that rarely cause death?
a) Prevalence
b) Disability-adjusted life years
c) Incidence
d) Mortality
e) Case fatality rate

### PH-P-111
tier: claimed
form: mcq
type: single
claimed: a
The first step in developing a comprehensive health plan for a city is:
a) Assessing the current health situation in the population.
b) Researching correlates of disease occurrence.
c) Disseminating health information.
d) Developing sound policy.
e) Reducing health disparities.

### PH-P-112
tier: claimed
form: mcq
type: single
claimed: b
Which of the following programs contributes to health care costs specifically for the poor and disabled?
a) Medicare
b) Medicaid
c) Veterans Administration
d) Social Security
e) All of the above

### PH-P-113
tier: claimed
form: mcq
type: single
claimed: d
Which of the following public health strategies is used to assess the current health situation in a country?
a) Surveys
b) Surveillance
c) Morbidity and mortality reporting
d) All of the above.
e) a. and b. above

### PH-P-114
tier: claimed
form: mcq
type: single
claimed: b
The major function(s) of public health is/are?
a) Surveillance, disease control, and treatment
b) Assessment, policy development, and assurance.
c) Monitoring, control, and social modification
d) Health education
e) Disease reporting, outbreak investigation, and treatment

### PH-P-115
tier: claimed
form: mcq
type: single
claimed: e
Epidemiology is useful for?
a) Describing the natural history of disease in the individual.
b) Establishing the clinical characteristics/spectrum of a disease.
c) Evaluating the effectiveness of prevention/intervention strategies.
d) Identifying risk factors for disease.
e) All of the above.

### PH-P-116
tier: claimed
form: mcq
type: single
claimed: a
Medicine focuses on the individual with disease, whereas public health focuses on the health of a population?
a) True.
b) False

### PH-P-117
tier: claimed
form: mcq
type: single
claimed: c
Disease is a result of the balance between?
a) Agent, host, and climate
b) Host, environment, and occupation
c) Agent, host and environment.
d) Person, place and environment
e) None of the above.

### PH-P-118
tier: claimed
form: mcq
type: single
claimed: a
note: near-miss of PH-P-008 -- same topic, differently worded question and options.
What is the "epidemiological transition"?
a) The shift from communicable to non-communicable diseases.
b) The shift from non-communicable to communicable diseases
c) The shift from curable to incurable diseases
d) The shift from individual medicine to public health

### PH-P-119
tier: claimed
form: mcq
type: single
claimed: e
Public health?
a) Is the science and art of preventing disease.
b) Is the process of mobilizing local, national and international resources.
c) Guarantees the health of all members of the community.
d) All of the above.
e) a. and b.

### PH-P-120
tier: claimed
form: mcq
type: single
claimed: b
note: option (d) is printed "ymptoms" in the source, a typo for "Symptoms" -- preserved verbatim.
As a health officer, which measure would you use to assess the magnitude of a chronic disease health problem requiring treatment in your area?
a) Incidence
b) Prevalence.
c) Disease characteristics
d) ymptoms

### PH-P-121
tier: claimed
form: mcq
type: single
claimed: b
The objective of public health is to guarantee the health of all, regardless of ethnicity, religion, gender, sexual orientation, country, or political views:
a) True
b) False.

### PH-P-122
tier: claimed
form: mcq
type: single
claimed: e
Which of the following contributed to increased life expectancy globally?
a) Improved sanitation
b) Provision of clean water
c) Improved housing
d) Universal childhood immunization programs
e) All of the above

### PH-P-123
tier: claimed
form: mcq
type: single
claimed: e
Which of the following health behaviors contributes to the morbidity and mortality of a population?
a) Alcohol use
b) Tobacco use
c) Unsafe sex
d) Diet and exercise
e) All of the above

### PH-P-124
tier: claimed
form: mcq
type: single
claimed: a
Improvement of the environment requires primarily behavioral and social change?
a) True.
b) False.

### PH-P-125
tier: claimed
form: mcq
type: single
claimed: a
The media is a major resource for promoting public health?
a) True.
b) False.

### PH-P-126
tier: claimed
form: mcq
type: single
claimed: d
In setting priorities for health policy in developing countries, one needs to consider?
a) The magnitude of the health problem.
b) The severity of the health problem.
c) The impact of the health problem.
d) All of the above.
e) a. and b. above.

### PH-P-127
tier: claimed
form: mcq
type: single
claimed: d
Urbanization promotes the rapid spread of infectious diseases through?
a) Increasing population density (crowding).
b) Creating inadequate resources for safe waste disposal.
c) Creating inadequate provision of safe drinking water.
d) All of the above.
e) b. and c. above.

### PH-P-128
tier: claimed
form: mcq
type: single
claimed: d
note: option (e) is printed on the following page (p31/p32 boundary), stitched here.
The probability of transmission of an infectious agent is associated with?
a) The environment
b) Social factors
c) Genetic and biologic factors
d) All of the above
e) a. and b. above

### PH-P-129
tier: claimed
form: mcq
type: single
claimed: a
Which of the following is NOT a function of epidemiology?
a) Lobbying for reform.
b) Describing the natural history of a disease.
c) Providing community diagnosis.
d) Estimating risk.
e) Evaluating prevention/intervention strategies.

### PH-P-130
tier: claimed
form: mcq
type: single
claimed: c
Which of the following epidemiologic parameters is used to characterize the spread of an infectious disease?
a) Prevalence
b) Disability-adjusted life years
c) Incidence
d) Mortality
e) Case fatality rate

### PH-P-131
tier: claimed
form: mcq
type: single
claimed: a
Which of the following epidemiologic parameters does NOT need to include a specific time interval?
a) Prevalence
b) Incidence
c) Mortality rate
d) Morbidity rate
e) DALYS

### PH-P-132
tier: claimed
form: mcq
type: single
claimed: b
World-wide, the leading infectious cause of death is?
a) HIV/AIDS
b) Respiratory infections
c) Measles
d) Diarrheal diseases
e) Malaria
