---
course: public-health
tab: practice
questions: 307
tiers: claimed 291 | open 16
forms: mcq 256 | qa 51
needs-eye: 0
disputed: 0
next-id: PH-P-308
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
<!-- batch 02 -- same file, pages 33-64 of 64. RUN-PLAN row 6.

  Confirms the batch-01 correction: this document's real answer-mark is bold
  text, and it must be checked per-question rather than assumed. Two further
  wrinkles turned up in this half of the file that batch 01 never hit:

  1. A run of pages (bottom of p50 through p53 -- the Incidence/Prevalence/
     Incidence definitions, the DALY question, the "influenza in a calendar
     year" question, and the whole 10-question Alma-Ata Declaration block)
     is entirely Calibri-Bold, stems AND every option alike -- a different
     source pasted in with its own default-bold style. Uniform bold across
     every option in a question carries no distinguishing information at all
     and was read as unmarked: PH-P-216, PH-P-217 and PH-P-218-227 are tier
     open despite every character on their pages being bold.
  2. From p54 to p62 the format itself changes again: options drop their
     letter prefixes entirely and are printed as bare bulleted lines. Bold
     still discriminates cleanly question-to-question here, so these were
     transcribed as ordinary mcq entries with option letters assigned by
     the order they're printed in (positional, nothing invented) -- same
     precedent as PH-P-027 in batch 01.

  Section-by-section (numbering restarts noted same as batch 01's convention):
    p33-37  continuation of batch 01's unlabeled fifth section -- Q52 picks up
            exactly where PH-P-132 (Q51) left off, no restart. PH-P-133 through
            PH-P-151 (19 Q), all claimed.
    p37-48  new unlabeled section, restarts at 1 (49 Q after merging one
            in-source duplicate, see below). PH-P-152 through PH-P-200, all
            claimed. PH-P-199 is a third reshuffled copy of the "Public health
            does which of the following" stem already seen at PH-P-060 and
            PH-P-083 -- kept separate again, same near-miss precedent.
    p48-50  12 unnumbered "scenario? Study design: X" statements -- the
            compiler stating a fact directly rather than posing a choice, so
            transcribed as form: qa with the stated design as the answer, tier
            claimed (compiler-asserted, same as any other claimed-tier answer
            in this zero-official-tier course). PH-P-201 through PH-P-212.
            PH-P-207 (HIV/TB mortality in Kenya) restates row 5's PH-P-022
            almost verbatim as a qa fact rather than an mcq -- cross-referenced,
            not merged, since the form differs.
    p50-51  a 3-item matching exercise (three numbered definitions, each
            answered by a single lettered term: A. Incidence rate / B.
            Prevalence / C. Incidence) -- split into three individual qa
            entries per the microbiology/pharmacology matching-block precedent
            rather than treated as one 3-option mcq. PH-P-213 through PH-P-215.
    p51     DALY question and the "influenza in a calendar year" question --
            both uniform-bold (see above), tier open. PH-P-216, PH-P-217.
    p51-53  Alma-Ata Declaration quiz, 10 Q, its own "A) / B- / C)" option
            style (only 3 options each) -- also uniform-bold throughout, tier
            open for all ten. PH-P-218 through PH-P-227.
    p54-62  unlettered bulleted-option block, 39 Q, all claimed (see format
            note above). PH-P-228 through PH-P-266. PH-P-263 restates
            PH-P-251's "temporal relationship means exposure precedes
            outcome/disease" with a different distractor set -- cross-noted,
            kept separate.
    p63     final unlabeled section, restarts at 1, back to lettered a-e
            options, 5 Q. PH-P-267 through PH-P-271.

  One in-source duplicate merged (same stem, one entry, per the batch-merge
  rule): the p37-48 section's own numbering reuses "34." for two unrelated
  questions -- the second of the two ("The following criteria are necessary
  to establish a causal relationship between two variables Except?") is a
  near-verbatim restatement of that same section's Q28, its four statements
  merely reordered, and both copies' bold marks agree on the same answer.
  Merged into PH-P-179; the genuine "34. Which of the following can be an
  observational study?" keeps its own entry (PH-P-185).

  PH-P-176 preserves a source typo where options c and d are printed with
  identical text ("Observational case-control") -- not corrected. PH-P-147's
  option c carries an Arabic annotation ("على سلايد. بيان" -- "stated on a
  slide") landing on the bold/correct option, same pattern as batch 01's
  PH-P-023. No embedded images anywhere in pages 33-64 turned out load-bearing
  -- the only one found (a decorative closing motivational photo on p64) was
  checked and discarded. -->

### PH-P-133
tier: claimed
form: mcq
type: single
claimed: e
Which of the following does NOT contribute to the emergence of new diseases?
a) Ecologic factors.
b) Social, political and economic factors.
c) Genetic and biological factors.
d) Physical environmental factors.
e) All of the above contribute to the emergence of new diseases.

### PH-P-134
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is NOT a primary responsibility of public health professionals?
a) Implementing immunization programs.
b) Maintaining a disease reporting system.
c) Identifying and containing outbreaks of disease.
d) Treating non-communicable diseases.
e) Educating the public about disease threats to the community.

### PH-P-135
tier: claimed
form: mcq
type: single
claimed: d
How do epidemiologists describe occurrence of disease in populations?
a) Characteristics of infected persons
b) Geographic distribution of cases
c) Time characteristics of disease occurrence
d) All of the above
e) b. and c. above

### PH-P-136
tier: claimed
form: mcq
type: single
claimed: b
Prevalence describes the rate of disease progression in a community?
a) True
b) False

### PH-P-137
tier: claimed
form: mcq
type: single
claimed: b
Prevalence measures rate in change of number of cases per unit time?
a) True
b) False

### PH-P-138
tier: claimed
form: mcq
type: single
claimed: d
Successful efforts to reduce smoking include:
a) Taxation of cigarettes
b) Physician counseling
c) Social pressure
d) All of the above

### PH-P-139
tier: claimed
form: mcq
type: single
claimed: a
Epidemiology uses time, place, and person to describe the relationship of agent, host and environment?
a) True.
b) False

### PH-P-140
tier: claimed
form: mcq
type: single
claimed: d
Improving worker health and safety results in which of the following?
a) Improved health status
b) Increased productivity
c) Decreased health care/related costs
d) All of the above.
e) a. and c. above

### PH-P-141
tier: claimed
form: mcq
type: single
claimed: d
Regular physical exercise results in:
a) An increase in average life span.
b) Reduced incidence of cardiovascular diseases.
c) Reduced risk of breast and colon cancer.
d) All of the above.
e) a. and b. above.

### PH-P-142
tier: claimed
form: mcq
type: single
claimed: e
Which of the following do NOT determine morbidity and mortality?
a) The social and spatial organisation of a population.
b) The individual's genetic endowment and exposure to a range of risk factors.
c) The physical environment, including patterns of relationships and mobility.
d) All of the above.
e) None of the above.

### PH-P-143
tier: claimed
form: mcq
type: single
claimed: e
For what reasons do we monitor health and disease?
a) To determine priorities for public health programs (e.g., burden of disease).
b) To understand change over time in causes of death and disease (e.g., pandemic influenza, motor vehicle accidents, suicide).
c) To measure the positive or negative effects of community health programs and services (e.g., community health promotion, expansion of paramedic services).
d) To improve the quality of the science underlying clinical medicine, nutrition, emergency healthcare, nursing, and allied healthcare.
e) All of the above.

### PH-P-144
tier: claimed
form: mcq
type: single
claimed: a
Which of the following terms can be defined as follows: 'the number of new cases of disease, injury or death in a population during a specified time period'?
a) Incidence
b) Cumulative incidence
c) Point prevalence
d) Prevalence
e) Mortality rate

### PH-P-145
tier: claimed
form: mcq
type: single
claimed: b
In Public Health, we define "health" as the absence of disease.
a) True
b) False

### PH-P-146
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is not one of the five steps in the public health approach?
a) Define the health problem.
b) Identify risk and/or protective factors associated with the problem.
c) Assess public perceptions of the intervention.
d) Develop and test community-level interventions to control or prevent the causes of the problem.

### PH-P-147
tier: claimed
form: mcq
type: single
claimed: c
note: option c carries an Arabic annotation in the source, "على سلايد. بيان" ("stated on a slide") -- the compiler confirming this answer against the lecture slides.
The standard medical definition of health refers to health as?
a) interesting, though not particularly important.
b) maximising the wellbeing of populations.
c) the absence of disease.
d) and elusive concept that defies definition.
e) both b. and c.

### PH-P-148
tier: claimed
form: mcq
type: single
claimed: d
The term used to describe measurable differences in attaining health is?
a) Health equity
b) Health inequity
c) Health gradient
d) Health inequality

### PH-P-149
tier: claimed
form: mcq
type: single
claimed: b
Health is best described as a resource that allows a person to have?
a) A social and spiritual life
b) A productive social and economic life
c) Economic well-being
d) Physical capacity

### PH-P-150
tier: claimed
form: mcq
type: single
claimed: c
What distinguishes primary health care from primary care?
a) A focus on primary, secondary and tertiary intervention.
b) Provision of interventions specific to the health need.
c) Works within a multidisciplinary framework.
d) Planning and operation of services is centralized.

### PH-P-151
tier: claimed
form: mcq
type: single
claimed: c
The main aim of public health is to improve health by:
a) Providing medical intervention appropriate for the individual.
b) Performing research to compare the effectiveness of treatments.
c) Promoting health and preventing disease in populations.
d) Providing advice on risk markers and genetics to families.

### PH-P-152
tier: claimed
form: mcq
type: single
claimed: b
Identify what this situation reflects: Over 20 million people worldwide died from influenza in 1918-1919?
a) Epidemic disease
b) Pandemic disease.

### PH-P-153
tier: claimed
form: mcq
type: single
claimed: b
A person working as a health educator use an approach that views health as related to?
a) Pathological processes.
b) Behavioral change.
c) Health screening.
d) Minimize complication.

### PH-P-154
tier: claimed
form: mcq
type: single
claimed: c
Which of the following studies apply to this: Persons diagnosed with new-onset Lyme disease were asked how often they walk through woods, use insect repellant, wear short sleeves and pants, etc. Twice as many patients without Lyme disease from the same physician's practice were asked the same questions, and the responses in the two groups were compared?
a) Observational cross-sectional.
b) Observational cohort.
c) Observational case-control.
d) Experimental.

### PH-P-155
tier: claimed
form: mcq
type: single
claimed: d
In which one of the following circumstances will the prevalence of a disease in the population increase, all else being constant?
a) If the incidence rate of the disease falls.
b) If the population in which the disease is measured increases.
c) If recovery of the disease is faster.
d) If survival time with the disease increases.

### PH-P-156
tier: claimed
form: mcq
type: single
claimed: d
The ....... rate is the average number of children per women in reproductive age?
a) growth.
b) family.
c) birth.
d) fertility.

### PH-P-157
tier: claimed
form: mcq
type: single
claimed: b
Health Equality is the opportunity for everyone to attain his or her full health potential?
a) True
b) False.

### PH-P-158
tier: claimed
form: mcq
type: single
claimed: b
The individual's culture does not impact his/her views towards health issues?
a) True
b) False.

### PH-P-159
tier: claimed
form: mcq
type: single
claimed: b
Health promotion became a core policy for the World Health Organization with the Alma-Ata Declaration in 1978 and the 'Health-for-All by the Year 2000' Program?
a) False
b) True.

### PH-P-160
tier: claimed
form: mcq
type: single
claimed: b
A person's health and wellbeing is dependent on a good start, good future, good care and support. These influences, social, economic, physical and environmental factors are known as
a) Health care.
b) Determinants of Health.
c) Health promotion.
d) Public Health.

### PH-P-161
tier: claimed
form: mcq
type: single
claimed: b
Which of the following studies apply to this: Representative sample of residents were telephoned and asked how much they exercise each week and whether they currently have (have ever been diagnosed with) heart disease.
a) Observational cohort.
b) Observational cross-sectional.
c) Observational case-control.
d) Experimental.

### PH-P-162
tier: claimed
form: mcq
type: single
claimed: a
Which is not a type of Epidemiology study?
a) Scientific.
b) Descriptive.
c) Experimental.
d) Observational.

### PH-P-163
tier: claimed
form: mcq
type: single
claimed: a
Identify what this situation reflects: Cases of infectious disease occurred within 3 weeks among residents of a particular neighborhood (usually 0 or 1 per year)?
a) Epidemic disease.
b) Pandemic disease.

### PH-P-164
tier: claimed
form: mcq
type: single
claimed: a
The decentralization of administrative and decision making functions is considered a way to involve the community in public health development?
a) True
b) False

### PH-P-165
tier: claimed
form: mcq
type: single
claimed: b
Pathogenicity refers to the ability of an organism to cause disease?
a) False
b) True

### PH-P-166
tier: claimed
form: mcq
type: single
claimed: a
Primary Health care philosophy includes the following EXCEPT?
a) Treating health as commodity.
b) Equity and Justice.
c) Inter relationship of Health and Development.
d) individual and community self-reliance.

### PH-P-167
tier: claimed
form: mcq
type: single
claimed: a
Health literacy is best defined as the capacity of a person to?
a) Recognize and know how to find information about a health problem.
b) Follow medical instruction for specific health care problem.
c) Read health-related literature.
d) Access the internet.

### PH-P-168
tier: claimed
form: mcq
type: single
claimed: b
Which of the following statements about exposures is true?
a) Dietary intake is not an 'exposure' because individuals make a choice about what they eat.
b) Exposure refers to contact with some factor that may be harmful or beneficial to health.
c) An exposed individual has a greater risk of disease.
d) High body mass index is a risk factor for a range of health conditions; therefore, it cannot be treated as a single exposure.

### PH-P-169
tier: claimed
form: mcq
type: single
claimed: b
In a case-control study, the Odds Ratio (OR) is the Ratio of the odds of exposure among the cases to the odds in favor of exposure among the controls?
a) False
b) True

### PH-P-170
tier: claimed
form: mcq
type: single
claimed: d
The ............ is an international health organization that compiles statistics of diseases and investigates health problems?
a) Food and Drug Administration
b) Occupational Safety and Health Administration
c) Center for Disease Control
d) World Health Organization.

### PH-P-171
tier: claimed
form: mcq
type: single
claimed: d
A process by which people gain control and mastery over their own lives is called?
a) Sustainability.
b) Intersectoral.
c) Equity.
d) Empowerment.

### PH-P-172
tier: claimed
form: mcq
type: single
claimed: a
........... is used to describe a small, localized epidemic, often contained to a village or a small town?
a) An outbreak.
b) A pandemic.
c) A sporadic disease.
d) An epidemic.

### PH-P-173
tier: claimed
form: mcq
type: single
claimed: a
Primary health care is usually practiced in?
a) Community health services and NGOs.
b) Health education units only.
c) Specialized health services and NGOs.
d) Community and acute care clinics.

### PH-P-174
tier: claimed
form: mcq
type: single
claimed: b
Public health services are given adequate attention in the financing of health care in Palestine.?
a) True
b) False.

### PH-P-175
tier: claimed
form: mcq
type: single
claimed: b
Social Justice refers?
a) social inclusion.
b) An ethical concept based on human rights and fairness.
c) An ethical concept based on autonomy.
d) Ensuring the punishment fits the crime.

### PH-P-176
tier: claimed
form: mcq
type: single
claimed: a
note: options c and d are printed with identical text ("Observational case-control") in the source -- a compiler typo, preserved as-is.
Which of the following studies apply to this: Occurrence of cancer was identified between April 1991 and July 2002 for 50,000 troops who served in the first Gulf War (ended April 1991) and 50,000 troops who served elsewhere during the same period?
a) Observational cohort.
b) Experimental.
c) Observational case-control.
d) Observational case-control.

### PH-P-177
tier: claimed
form: mcq
type: single
claimed: b
By basing programs and services in communities, organizations, and schools where most people spend most of their time, you can Increase the likelihood of long-term success to the road of health and wellness?
a) False
b) True.

### PH-P-178
tier: claimed
form: mcq
type: single
claimed: a
A study is done to examine whether is an association between the daily use of vitamins and risk of coronary artery disease (heart attack) over a 10-year period. When subjects who took, both vitamins were compared to those who took no vitamins at all, the risk ratio was found to be 0.07. Which of the following is a correct interpretation of this Finding?
a) Those who take vitamins C & E daily have 0.7 times the risk of heart attack compared to those who do not take vitamins.
b) The risk difference in this study is 0.70 per 100 vitamin users over ten years.
c) The risk difference in this study is 70 per 100 vitamin users over ten years.
d) The incidence of coronary artery disease in those who take vitamins C & E daily is 0.70 (or 70%).

### PH-P-179
tier: claimed
form: mcq
type: single
claimed: d
note: merged with a near-verbatim repeat of this question printed later in the source under a duplicate "34." (same four statements, reordered) -- both copies' bold marks agree on this answer.
The following criteria are necessary to establish causal relationship between two variables except?
a) The exposure to this factor should precede the development of the disease.
b) The factor is present in all subjects with the disease.
c) Elimination of the factor reduces risk of the disease.
d) One exposure to this factor is always enough to develop the disease.

### PH-P-180
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is the best definition of public health?
a) The science and art of preventing disease, prolonging life, and promoting health through the organized efforts of medical science.
b) None of these.
c) All of these.
d) The process of mobilizing local, state provincial, national and international resources to assure the conditions in which all people can be healthy.
e) Ensuring the health of the individual by maintaining and improving the health of the community.

### PH-P-181
tier: claimed
form: mcq
type: single
claimed: b
What is the best way to prevent the spread of infection?
a) Avoid contact with ill patients.
b) Wash your hands.
c) Use alcohol wipes to clean surfaces.
d) Use personal protective equipment.

### PH-P-182
tier: claimed
form: mcq
type: single
claimed: b
Which of the following studies apply to this: Subjects were children enrolled in a health maintenance organization. At 2 months, each child was randomly given one of two types of a new vaccine against rotavirus infection. Parents were called by a nurse two weeks later and asked whether the children had experienced any of a list of side-effects?
a) Observational cohort
b) Experimental.
c) Observational case-control
d) Observational cross-sectional.

### PH-P-183
tier: claimed
form: mcq
type: single
claimed: d
Health Promotion Action means EXCEPT?
a) Reorient health services to focus on people empowerment.
b) Strengthen community-wide health action.
c) Building public healthy policy.
d) Develop highly specialized medical services.
e) Create supportive social environment.

### PH-P-184
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is an example of a non-communicable condition with multiple social determinants and causes?
a) Violence Including suicide and homicide.
b) Alcohol related deaths and disease.
c) Obesity.
d) All are correct.
e) Teen/unplanned parenthood.

### PH-P-185
tier: claimed
form: mcq
type: single
claimed: b
Which of the following can be an observational study?
a) Community trial.
b) Cross-sectional.
c) Randomized controlled trial.
d) Field trial.

### PH-P-186
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is true of the determinants of health?
a) If a pathogenic organism can be shown to cause a disease then no other determinants are present.
b) One determinant is operating to bring about each disease.
c) They reflect multiple, interconnected underlying forces that influence health and the subsequent development of disease.
d) Each determinants can usually be traced to specific disease.

### PH-P-187
tier: claimed
form: mcq
type: single
claimed: a
Primary health care is?
a) The first point of contact for people with the health care services.
b) Care provided in the acute setting.
c) Care provided in hospices.
d) Care provided by GPs only.

### PH-P-188
tier: claimed
form: mcq
type: single
claimed: b
If a disease is endemic that means it is at the normal, expected level within the population?
a) False.
b) True.

### PH-P-189
tier: claimed
form: mcq
type: single
claimed: a
In a case control study, the Odds Ratio (OR) is the Ratio of the odds of exposure among the cases to the odds in favor of exposure among the controls?
a) True
b) False

### PH-P-190
tier: claimed
form: mcq
type: single
claimed: a
Availability means that the cost should be within the means and resources of the individual and the country?
a) True.
b) False.

### PH-P-191
tier: claimed
form: mcq
type: single
claimed: a
Epidemiological measures of effect assess the _______ between an exposure and an outcome.?
a) Strength of the association
b) Strength of the causal mechanisms.
c) Strength of the reversibility.
d) Strength of a confounding factor.

### PH-P-192
tier: claimed
form: mcq
type: single
claimed: c
Which of the following models of health is the primary health care approach based on?
a) Behavioural.
b) Economic.
c) Social.
d) Education.

### PH-P-193
tier: claimed
form: mcq
type: single
claimed: c
Sustainability refers to the ability of a program to?
a) Be uncompromising when disturbances occur in social and environmental systems.
b) Identify and reduce risk factors and lifestyle behaviours affecting health.
c) Meet current needs without affecting the ability of people in the future to meet their needs.
d) Focus on the social, political, economic and ecological dimensions of health.

### PH-P-194
tier: claimed
form: mcq
type: single
claimed: b
The key elements the World Health Organization sees as necessary to achieve better health for all include?
a) Decreasing inclusion in health care coverage.
b) Increasing stakeholder participation.
c) Centralising and standardising health service delivery.
d) Reducing use of collaborative models.

### PH-P-195
tier: claimed
form: mcq
type: single
claimed: a
What role were health professionals seen as fulfilling in health promotion?
a) Enabling and nurturing health promotion.
b) Controlling the health promotion agenda.
c) Monitoring the health care team.
d) Working with teachers.

### PH-P-196
tier: claimed
form: mcq
type: single
claimed: a
What factors besides land degradation affect the ability to create supportive environments?
a) Rapid population growth and climate events.
b) Productive food harvests.
c) Political and social accord.
d) Economic stability.

### PH-P-197
tier: claimed
form: mcq
type: single
claimed: b
Health promotion advocates did NOT view health as?
a) A resource for life.
b) The reason for living.
c) A positive concept.
d) Including personal resources.

### PH-P-198
tier: claimed
form: mcq
type: single
claimed: c
How does health promotion affect general policy formulation?
a) Policy makers outside health will be directed by health departments.
b) Health policy makers need to ensure that they have considered all possible policy areas.
c) All policy makers need to consider how they can contribute to health promotion.
d) Policies need to be legislated so everyone will follow them.

### PH-P-199
tier: claimed
form: mcq
type: single
claimed: e
note: near-miss of PH-P-060/PH-P-083 -- a third reshuffled copy of this stem, its own "all of them"-style answer.
Public health does which of the following?
a) Mobilizes communities.
b) Provides conditions conducive to good health.
c) Promotes healthy lifestyles.
d) All of the above.
e) a. and c.

### PH-P-200
tier: claimed
form: mcq
type: single
claimed: b
What is the science of protecting populations and improving the health of human communities called?
a) Epidemiology.
b) Public Health.
c) Preventive Medicine.
d) Sociology.

### PH-P-201
tier: claimed
form: qa
claimed: Cross-sectional
The growth patterns of infants aged 6-24 months were assessed on the basis of a single measurement of height, weight and head circumference of the population receiving care at the Family Health Centers in the northern and southern regions of Jordan?

### PH-P-202
tier: claimed
form: qa
claimed: Ecological
The association between levels of air pollution and mortality rate in different European countries was studied?

### PH-P-203
tier: claimed
form: qa
claimed: Case-control
The reduction in the likelihood of experiencing myocardial infraction (MI) amongst women who stopped smoking was shown by comparing the smoking habits of women who had experienced a MI with the smoking habits of women free of MI?

### PH-P-204
tier: claimed
form: qa
claimed: Retrospective (case-control)
A proposal was recently accepted to study the association between exposure to radiation as a treatment for trichophytiasis (a dermatological condition of the scalp) and brain tumors, the proposed study will compare the rate of brain tumors among persons who had received the radiation treatment in the 1950s with the rate of brain tumors among persons who received other modes of treatment during those same years?

### PH-P-205
tier: claimed
form: qa
claimed: Prospective cohort
The study of type A personality as a predictor of the risk for stroke?

### PH-P-206
tier: claimed
form: qa
claimed: Cohort study
An investigator takes a sample of healthy individuals, record their ongoing solar exposure, and relate that to the subsequent occurrence of skin cancer in the same group?

### PH-P-207
tier: claimed
form: qa
claimed: Cohort study
note: cross-references PH-P-022 (row 5, same tab) -- the same HIV/TB-in-Kenya scenario, here presented as a direct study-design statement rather than an mcq; not merged, since the form differs.
A study was conducted to investigate the effect of HIV infection on mortality among people in Kenya with TB. Individuals with TB were recruited from hospitals and their HIV status determined. They were then followed-up over ten years to compare mortality rates in the HIV positive group and HIV negative group?

### PH-P-208
tier: claimed
form: qa
claimed: Clinical Trial
A study was conducted to determine whether recurrences of urinary tract infection (UTI) can be prevented with cranberry-lingonberry juice?

### PH-P-209
tier: claimed
form: qa
claimed: Program Trial
A study was conducted to examine the effectiveness of a community-based multimodal intervention program for suicide prevention in regions where the suicide rate was relatively high compared to control regions?

### PH-P-210
tier: claimed
form: qa
claimed: Clinical Trial
A study was conducted to assess the effect of vitamin supplementation on the intelligence development of 6-8-year-old children?

### PH-P-211
tier: claimed
form: qa
claimed: Program review
An evaluation was conducted for participant after 3 months of intervention to Increase awareness for hypertension.?

### PH-P-212
tier: claimed
form: qa
claimed: Cross-Sectional Studies
Survey a sample of people with a written questionnaire or physical exam for habits, activities, characteristics, current state of health; provides a health snapshot of a target population (unknown what came before or after)?

### PH-P-213
tier: claimed
form: qa
claimed: Incidence rate
note: first of a 3-item matching exercise in the source (each numbered definition answered by one lettered term) -- split into individual qa entries per the microbiology/pharmacology matching-block precedent rather than treated as one mcq.
Number of new health-related events in a defined population within a specified period of time; includes numerator (# new cases), denominator (population at risk) and time?

### PH-P-214
tier: claimed
form: qa
claimed: Prevalence
Measure the number of people in a population who have the disease at a given point in time?

### PH-P-215
tier: claimed
form: qa
claimed: Incidence
Measures the rate at which people without the disease develop the disease during a specified period of time; used to study disease etiology (risk)?

### PH-P-216
tier: open
form: mcq
type: single
note: every option is bold in the source -- uniform formatting carries no distinguishing signal, so this is genuinely unmarked despite appearing fully bold.
The term DALY means?
a) Disabled ability for life years.
b) Do a lot of yoga.
c) Disabled-adjusted life years.
d) Disabled-adjusted for last year.
e) Disability-added lost years.

### PH-P-217
tier: open
form: mcq
type: single
note: every option is bold in the source, same uniform-bold pattern as PH-P-216 -- no distinguishing signal.
A study that measures the number of persons with influenza in a calendar year?
a) Cross sectional
b) Case control
c) Cohort study
d) Case report

### PH-P-218
tier: open
form: mcq
type: single
note: this and the remaining 9 Alma-Ata Declaration questions (through PH-P-227) are printed entirely in bold -- stems and every option alike, the source's own default style for this block, not an answer mark. All ten are genuinely unmarked.
When was the Alma-Ata Declaration signed?
a) 1977.
b) 1978.
c) 1987.

### PH-P-219
tier: open
form: mcq
type: single
Where was the Alma-Ata Declaration signed?
a) Kazakhstan.
b) Pakistan.
c) Uzbekistan.

### PH-P-220
tier: open
form: mcq
type: single
What did the Alma-Ata Declaration state about the right to health?
a) That access to healthcare is a luxury that not everyone can afford.
b) That governments have a responsibility to ensure that everyone has access to adequate healthcare.
c) That healthcare is not a right but a privilege.

### PH-P-221
tier: open
form: mcq
type: single
What did the Alma-Ata Declaration focus on as the appropriate method of assuming adequate access to healthcare for all?
a) Minor health care.
b) Lesser health care.
c) Primary health care.

### PH-P-222
tier: open
form: mcq
type: single
What is the definition of primary health care according to the Alma-Ata Declaration?
a) A healthcare system that focuses only on individual patients.
b) A healthcare system that includes not only curative care, but also preventive and promotive approaches, and aims to integrate healthcare in all sectors.
c) A healthcare system that only focuses on outpatient care.

### PH-P-223
tier: open
form: mcq
type: single
What was the Alma-Ata Declaration's goal for the year 2000?
a) To ensure that everyone has access to health insurance.
b) To ensure that everyone has access to adequate healthcare.
c) To cure all diseases.

### PH-P-224
tier: open
form: mcq
type: single
What did the Alma-Ata Declaration state about health personnel?
a) There should be a high number of health personnel.
b) Health personnel should be trained in medical curative care.
c) Health personnel should receive comprehensive training and education in all aspects of primary health care.

### PH-P-225
tier: open
form: mcq
type: single
What is the underlying principle of the Alma-Ata Declaration?
a) Health is a fundamental human right.
b) The focus of healthcare should be on curative care usually.
c) Health is a luxury that not everyone can afford.

### PH-P-226
tier: open
form: mcq
type: single
What impact did the Alma-Ata Declaration have on healthcare systems around the world?
a) It was ignored by most countries and had little impact.
b) It became a catalyst for transformative change, inspiring nations to reevaluate their healthcare systems and strive for comprehensive, people-centered care.
c) It caused governments to restrict access to healthcare.

### PH-P-227
tier: open
form: mcq
type: single
What is the ultimate goal of the Alma-Ata Declaration?
a) To achieve universal health coverage.
b) To create a shortage of healthcare services and resources.
c) To reduce access to healthcare.

### PH-P-228
tier: claimed
form: mcq
type: single
claimed: a
note: options in this and the following entries through PH-P-266 are unlettered bulleted lines in the source -- letters assigned positionally in print order, nothing invented, same precedent as PH-P-027.
Which of the following sentence/s could best describe/s Endemic health problem?
a) Consistency reporting of cases at same rate over time in certain area.
b) Reporting of cases more than the normally reported at certain area.
c) Reporting of cases more than the normally reported all over the world.
d) All of the answers are correct.

### PH-P-229
tier: claimed
form: mcq
type: single
claimed: c
People with asthma were 3.6 times as likely as people without asthma to own a cat. What measure of association does this statement describe?
a) Population attributable risk
b) Relative risk
c) Odds ratio
d) Risk difference

### PH-P-230
tier: claimed
form: mcq
type: single
claimed: c
Which of the following statements is Incorrect?
a) Prevalence is mainly estimated in cross-sectional studies.
b) Case control studies are susceptible to Recall bias.
c) Causality can be assessed using cross sectional study.
d) The Relative Risk is mainly calculated in cohort studies.

### PH-P-231
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is a measure of association in a case control study?
a) P-value
b) Risk difference
c) Odds ratio
d) Relative risk

### PH-P-232
tier: claimed
form: mcq
type: single
claimed: b
A double blind randomized controlled trail was performed to assess the effect of vitamins on preventing cardiovascular diseases. 250 were given vitamins while 285 were not. Among those who have been given vitamins, 85 developed the disease while only 40 did not develop the disease from those who were not given the vitamins. Please calculate the relative risk (RR) for vitamin intake compared to non-vitamin intake:
a) 3.9
b) 0.39
c) 0.49
d) 4.9

### PH-P-233
tier: claimed
form: mcq
type: single
claimed: b
John established a study to investigate the association between smoking and lung cancer. He assigned two groups; one is exposed to smoking and the other is not exposed to smoking. The two groups were followed over time to investigate the incidence of lung cancer. This study is:
a) Case-Control study
b) Cohort study
c) Cross-sectional study
d) Randomized control trial

### PH-P-234
tier: claimed
form: mcq
type: single
claimed: b
All of the following can be considered as non-communicable disease EXCEPT?
a) High blood pressure.
b) Malaria.
c) Cancer.
d) Diabetes.

### PH-P-235
tier: claimed
form: mcq
type: single
claimed: d
These studies allow to measure the effect of aggregate measures of exposure when measurement are not available at individual level or difficult to obtain?
a) Case control studies
b) Cohort studies
c) Case study
d) Ecological studies

### PH-P-236
tier: claimed
form: mcq
type: single
claimed: c
Public health surveillance is?
a) Used to guide the public health decision.
b) Ongoing systematic collection of data.
c) All of the answers are correct.
d) Used to evaluate public health programs.

### PH-P-237
tier: claimed
form: mcq
type: single
claimed: a
Which of the following statement/s would best describe/s the outbreak?
a) Occurrence of more cases of disease than expected in a given area among a specific group of people over a particular period of time.
b) Constant presence of disease in a population within a specific geographical area.
c) None of the above is correct.
d) Spread of disease cases between continents.

### PH-P-238
tier: claimed
form: mcq
type: single
claimed: c
If the relative risk value is less than one then this indicates that?
a) All of the above are correct.
b) The risk of developing the health event in the exposed group is similar to that in the non-exposed group.
c) The risk of developing the health event in the exposed group is less than that in the non-exposed group (Protective effect).
d) The risk of developing the health event in the exposed group is higher than that in the non-exposed group.

### PH-P-239
tier: claimed
form: mcq
type: single
claimed: a
A double blind randomised controlled trail was performed to assess the effect of vitamins on preventing cardiovascular diseases. 250 were given vitamins while 285 were not. Among those who have been given vitamins, 85 developed the disease while only 40 did not develop the disease from those who were not given the vitamins. Please calculate the risk difference (RD) or attributed risk (AR) for vit-intake compared to non-vit-intake?
a) -0.52
b) -0.39
c) 5.2
d) 0.49

### PH-P-240
tier: claimed
form: mcq
type: single
claimed: d
Which of the following statement/s is/are best describing descriptive epidemiology studies?
a) Studies that set up to answer the question who is getting the disease.
b) Studies that set up to answer the causes of a diseases.
c) Studies that set up to answer the questions where the disease is mostly distributed.
d) A and C are correct.

### PH-P-241
tier: claimed
form: mcq
type: single
claimed: d
The proportion of exposed persons who become infected after exposure to a certain agent can be defined as?
a) All answers are correct.
b) Virulence
c) Pathogenicity.
d) Infectivity.

### PH-P-242
tier: claimed
form: mcq
type: single
claimed: a
Which of the following statement/s is/are best describing the objectives of public health surveillance?
a) All of the answers are correct.
b) To set priorities for health planning.
c) To assess public health status.
d) To provide and interpret data to facilitate the prevention and control of disease.

### PH-P-243
tier: claimed
form: mcq
type: single
claimed: d
A study in which children are randomly assigned to receive either a newly formulated vaccine or the currently available vaccine, and are followed to monitor for side effects and effectiveness of each vaccine, is an example of which type of study?
a) Case-control.
b) Observational.
c) Cohort.
d) Randomized controlled trial.

### PH-P-244
tier: claimed
form: mcq
type: single
claimed: c
From healthcare provider to health department?
a) Screening
b) Randomization
c) Passive surveillance.
d) Indirect standardization

### PH-P-245
tier: claimed
form: mcq
type: single
claimed: a
Epidemiology is defined as?
a) The study of factors that determine the occurrence and distribution of disease in a population.
b) Individual patient level of clinical medicine care.
c) A real science since the time of Hippocrates that investigate bacterial infections.
d) Scientific study of disease in the sub molecular and molecular level.

### PH-P-246
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is a measure of association in a cohort study?
a) Prevalence rate
b) Odds ratio
c) Relative risk
d) Population attributable risk

### PH-P-247
tier: claimed
form: mcq
type: single
claimed: a
Which of the following statements is TRUE with regard to randomized controlled trial?
a) It is the gold standard of study designs.
b) Are always double blinded.
c) The participants are communities.
d) All of the answers are correct.

### PH-P-248
tier: claimed
form: mcq
type: single
claimed: c
Which of the following is an advantage of a cohort study?
a) People are less likely to be lost to follow up.
b) Relatively cheap and easy to conduct.
c) Can establish temporal sequencing.
d) Good for rare outcomes.

### PH-P-249
tier: claimed
form: mcq
type: single
claimed: c
The control group in RCT may receive?
a) No treatment.
b) A placebo.
c) All of the answers are correct.
d) A standard treatment.

### PH-P-250
tier: claimed
form: mcq
type: single
claimed: b
Which of the following diseases does not currently present a significant health challenge in Palestine?
a) Cardiovascular diseases.
b) HIV/AIDS.
c) Diabetes.
d) Cancer.

### PH-P-251
tier: claimed
form: mcq
type: single
claimed: d
Temporal relationship means that?
a) Exposure must be strongly associated with the outcome.
b) Alternative explanations are considered.
c) The higher the exposure the huger the outcome.
d) Exposure must precede outcome.

### PH-P-252
tier: claimed
form: mcq
type: single
claimed: d
If you want to know the proportion of the disease that could be prevented by eliminating the exposure in the entire study population, you should calculate the?
a) Prevalence rate.
b) Relative risk.
c) Incidence rate.
d) Population attributable risk.

### PH-P-253
tier: claimed
form: mcq
type: single
claimed: b
Epidemiology cannot study any health event in a specified population?
a) True
b) False

### PH-P-254
tier: claimed
form: mcq
type: single
claimed: b
In ecological study, associations on population levels might reflect associations on individual levels?
a) True
b) False

### PH-P-255
tier: claimed
form: mcq
type: single
claimed: a
When the disease is maintained in the population without the needs for external outputs, it is referred to as?
a) Endemic.
b) All answers are correct.
c) Pandemic.
d) Epidemic.

### PH-P-256
tier: claimed
form: mcq
type: single
claimed: c
Used to generate hypothesis?
a) Cohort study
b) Randomized control trial
c) Ecological study
d) Case-control study

### PH-P-257
tier: claimed
form: mcq
type: single
claimed: d
Investigate if rate of Asthma is higher in cities with higher level of air pollution, is an example on?
a) Case series.
b) Case report.
c) None of the answers is correct.
d) Ecological study.

### PH-P-258
tier: claimed
form: mcq
type: single
claimed: c
Modern epidemiology started with?
a) Hippocrates oath.
b) John Snow investigations.
c) Doll and Hill investigations.
d) Covid-19 transmission in Wuhan province.

### PH-P-259
tier: claimed
form: mcq
type: single
claimed: d
The most elementary study in the literature?
a) Case series
b) Ecological study
c) None of the above
d) Case report

### PH-P-260
tier: claimed
form: mcq
type: single
claimed: d
Criteria of causation?
a) Replication of the findings.
b) Study design.
c) Consistency with other knowledge.
d) All of the answers are correct.

### PH-P-261
tier: claimed
form: mcq
type: single
claimed: a
Epidemiology science concerns by?
a) All answers are correct.
b) Distribution of a health event
c) Studying the determinants of a health event.
d) Control of a health event.

### PH-P-262
tier: claimed
form: mcq
type: single
claimed: d
Which of the following is considered as an achievement of epidemiology?
a) None of the answers is correct.
b) Discovery of Gold in Sudan.
c) COVID-19 eradication.
d) Methyl mercury poisoning outbreak

### PH-P-263
tier: claimed
form: mcq
type: single
claimed: a
note: near-duplicate of PH-P-251 -- same underlying "exposure must precede outcome/disease" concept, reworded distractor set, kept separate.
Temporal relationship means that?
a) Exposure must precede disease.
b) None of the answers is correct.
c) Disease must precede exposure.
d) Magnitude of association between exposure and disease.

### PH-P-264
tier: claimed
form: mcq
type: single
claimed: d
Ecological study?
a) Suitable for testing hypothesis
b) Unit of analysis individual
c) An example on analytical study
d) Unit of analysis clusters

### PH-P-265
tier: claimed
form: mcq
type: single
claimed: b
Experimental study designs are an example of analytical epidemiology study design?
a) False
b) True

### PH-P-266
tier: claimed
form: mcq
type: single
claimed: d
Descriptive epidemiology describes?
a) Why was the population affected.
b) How was the population affected.
c) None of the answers is correct.
d) When was the population affected.

### PH-P-267
tier: claimed
form: mcq
type: single
claimed: e
The definition of epidemiology includes all of the following, EXCEPT?
a) study of determinants.
b) study of disease frequency.
c) study of disease patterns.
d) health-related states or events.
e) All of these are included in the definition of epidemiology.

### PH-P-268
tier: claimed
form: mcq
type: single
claimed: b
Descriptive epidemiology involves identifying and quantifying associations, testing hypotheses, and identifying causes of health-related states or events?
a) True
b) False.

### PH-P-269
tier: claimed
form: mcq
type: single
claimed: b
Application of the study of the distribution and determinants of health-related states or events in order to prevent and control health problems is not included in the role of epidemiology?
a) True
b) False.

### PH-P-270
tier: claimed
form: mcq
type: single
claimed: b
Epidemiology involves studying only infectious communicable disease, not events like injury, obesity, mental health disorders, seat belt use, etc.?
a) True.
b) False.

### PH-P-271
tier: claimed
form: mcq
type: single
claimed: b
Which of the following is not usually an aim of epidemiology?
a) To describe the health status of the population.
b) To fund new public health programs.
c) To explain the etiology of disease.
d) To predict the occurrence of disease.
e) To control the distribution of disease.
<!-- batch 03 -- raw/practice/exercises/, 7 vision pages (JPEGs, no text layer).
  RUN-PLAN row 7.

  Not a Moodle capture -- these are photos of a printed instructor worksheet
  packet, three separate exercises stapled/shot together in one folder, all
  qa/fact form (no mcq options anywhere). No embedded images beyond the pages
  themselves; nothing decorative to discard.

    Exercise (unlabeled, 2 pages, numbered "1."/"2." questions about
    exposure/disease 2x2 tables): PH-P-272-275 (caffeine/MI case-control) and
    PH-P-276-278 (asthma/smoking incidence/RR). Both tables are load-bearing
    for every sub-question -- each entry's `img:` points to the full page
    photo saved to `flagged/`, since the printed 2x2 table IS the question,
    per this row's own RUN-PLAN note. Job A transcribed the work already
    shown on the page (unsimplified fractions, cross-multiplications) rather
    than computing anything itself -- PH-P-275's "Interpret the measure of
    association" was left genuinely blank by the student, so it's tier open.
    PH-P-277 has a real internal inconsistency worth flagging rather than
    fixing: its own "incidence in unexposed" line divides by 990 (the
    "no disease" column), but the relative-risk line two lines below divides
    the same unexposed count by 1310 (the correct row total) -- both
    transcribed exactly as printed, not reconciled.

    "Exercise I" (2 pages, 12 items, matching prevention level -- Primordial/
    Primary/Secondary/Tertiary -- to a scenario): PH-P-279-290, all claimed,
    the level printed in bold under each scenario. Page 2 cites
    https://phprimer.afmc.ca/en/part-i/chapter-4/ as its source.

    "Screening test" (1 page, a worked Hepatitis B sensitivity/specificity
    exercise with the 2x2 truth table already filled in -- 95/490/585 top
    row, 5/4410/4415 bottom row, 100/4900/5000 totals -- consistent with the
    stated 95% sensitivity and 90% specificity): PH-P-291-296. The four raw
    cell counts (true/false positive/negative) are direct table lookups, not
    computation, so recorded as claimed; the two derived measures (PPV, NPV)
    are never actually calculated anywhere on the page, so they're tier open
    rather than Job A doing the division itself. `img:` on all six entries
    points to the full page photo in `flagged/`.

    "Exercise II" (2 pages, 11 short-abstract-to-study-design items, its own
    lettered key A-G at the top of page 1): PH-P-297-307, all claimed. This
    is the same scenario set as row 6's PH-P-201 through PH-P-211 (the PYQ
    bank's own unlettered "scenario -> Study design: X" block) -- 11 of
    row 6's 12 entries reappear here verbatim, missing only row 6's 12th
    ("Survey a sample of people with a written questionnaire..."). Each entry
    below is cross-noted to its row-6 counterpart rather than merged, per
    the cross-batch-matching-is-the-app's-job rule; every answer agrees with
    its row-6 twin. -->

### PH-P-272
tier: claimed
form: qa
claimed: 64/242
img: flagged/PH-P-272-caffeine-MI-2x2-table.jpg
A study was conducted to determine whether there is an association between caffeine consumption and Myocardial Infarction. The study included 230 incident cases of MI and 455 controls from the general population. After interviewing all subjects, it was found that 64 of the cases had high daily consumption of caffeine (exposed) prior to diagnosis and 277 of the controls had low daily consumption of caffeine (unexposed) prior to the date of the matched case's diagnosis. (2x2 table: Exposed -- 64 cases, 178 controls; Unexposed -- 166 cases, 277 controls.) Calculate the odds of being a case among the exposed.

### PH-P-273
tier: claimed
form: qa
claimed: 166/443
img: flagged/PH-P-272-caffeine-MI-2x2-table.jpg
Same caffeine/MI study as PH-P-272. Calculate the odds of being a case among the unexposed.

### PH-P-274
tier: claimed
form: qa
claimed: (64/166) / (178/277) = 64x277 / 166x178
img: flagged/PH-P-272-caffeine-MI-2x2-table.jpg
Same caffeine/MI study as PH-P-272. Calculate the odds ratio for disease given exposure to high daily intake of caffeine (versus low daily intake of caffeine).

### PH-P-275
tier: open
form: qa
img: flagged/PH-P-272-caffeine-MI-2x2-table.jpg
Same caffeine/MI study as PH-P-272. Interpret the measure of association.

### PH-P-276
tier: claimed
form: qa
claimed: 110/324
img: flagged/PH-P-276-asthma-smoking-2x2-table.jpg
A study was conducted to examine risk factors for Asthma and smoking. 430 emergency room cases were identified from Al-Maqased hospital in 2017, and 1204 controls were sampled from the patients admitted to the emergency room for shortness of breath. It was found that 110 of the cases and 214 of the controls were smoker. The remaining cases and controls did not smoke. (2x2 table: Exposed (smoked) -- 110 cases, 214 controls; Unexposed (not smoked) -- 320 cases, 990 controls.) What is the incidence in exposed?

### PH-P-277
tier: claimed
form: qa
claimed: 320/990
img: flagged/PH-P-276-asthma-smoking-2x2-table.jpg
note: the source's own relative-risk line for this same study (PH-P-278) divides this same unexposed-cases count by 1310 instead of 990 -- an internal inconsistency in the source, both readings transcribed exactly as printed rather than reconciled.
Same asthma/smoking study as PH-P-276. What the incidence is in unexposed?

### PH-P-278
tier: claimed
form: qa
claimed: (110/324) / (320/1310)
img: flagged/PH-P-276-asthma-smoking-2x2-table.jpg
Same asthma/smoking study as PH-P-276. What is the relative risk or risk ratio?

### PH-P-279
tier: claimed
form: qa
claimed: Tertiary
note: first of a 12-item "Exercise I" matching sheet -- each scenario matched to one of Primordial/Primary/Secondary/Tertiary prevention. Source cites https://phprimer.afmc.ca/en/part-i/chapter-4/.
Follow-up exams to identify recurrence of metabolic disease: physical examination, liver enzyme test, chest x-ray, etc....

### PH-P-280
tier: claimed
form: qa
claimed: Primary
Education about healthy eating exercising regularly.

### PH-P-281
tier: claimed
form: qa
claimed: Secondary
Diet and exercise programs to prevent further heart attacks or strokes.

### PH-P-282
tier: claimed
form: qa
claimed: Secondary
Getting a young person to quit smoking is an example of.

### PH-P-283
tier: claimed
form: qa
claimed: Tertiary
Vocational rehabilitation programs to retrain workers for new jobs when they have recovered as much as possible.

### PH-P-284
tier: claimed
form: qa
claimed: Secondary
In the public health community, _________ prevention aims to identify practices and situations that put certain individuals at risk for illness or injury.

### PH-P-285
tier: claimed
form: qa
claimed: Primordial Prevention
It was observed that children with smoking parents, would wrongly consider smoking as a good lifestyle choice in their lives, thus it was concluded that parents should be advised to quit smoking.

### PH-P-286
tier: claimed
form: qa
claimed: Primary
The municipality decided to legislate and enforce a rule to ban or control the use of hazardous products (e.g. asbestos).

### PH-P-287
tier: claimed
form: qa
claimed: Primordial Prevention
The ministry of health conducted a rule to improve sanitation, so that exposure to infectious agents does not occur.

### PH-P-288
tier: claimed
form: qa
claimed: Primordial Prevention
The preventive measures comprise the maintenance of normal body weight through the adoption of healthy nutritional habits and physical exercise.

### PH-P-289
tier: claimed
form: qa
claimed: Tertiary
Screening of patients with diabetes for diabetic retinopathy to prevent progression to blindness through prompt treatment.

### PH-P-290
tier: claimed
form: qa
claimed: Primary
Initiation of an exercise program with the goal of disease prevention.

### PH-P-291
tier: claimed
form: qa
claimed: 95
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
note: first of 6 sub-questions on a worked Hepatitis B screening exercise. The source's own 2x2 truth table (test result x true status) is already filled in: test+/truth+ 95, test+/truth- 490 (row total 585); test-/truth+ 5, test-/truth- 4410 (row total 4415); column totals 100, 4900, grand total 5000 -- consistent with the stated 95% sensitivity and 90% specificity. A test is used to screen people for hepatitis B. The sensitivity of the test is 95% and the specificity of the test is 90%. Assume that the total number of persons being tested for hepatitis B is 5000. Assume that the true prevalence of hepatitis B in the population is 100 per 5000. # of true positive?

### PH-P-292
tier: claimed
form: qa
claimed: 4410
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
Same Hepatitis B screening exercise as PH-P-291. # of true negative?

### PH-P-293
tier: claimed
form: qa
claimed: 490
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
Same Hepatitis B screening exercise as PH-P-291. # of false positive?

### PH-P-294
tier: claimed
form: qa
claimed: 5
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
Same Hepatitis B screening exercise as PH-P-291. # of false negative?

### PH-P-295
tier: open
form: qa
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
note: unlike PH-P-291-294 (direct table lookups), this measure is never actually calculated anywhere on the page -- left open rather than Job A performing the division itself.
Same Hepatitis B screening exercise as PH-P-291. Positive predictive value?

### PH-P-296
tier: open
form: qa
img: flagged/PH-P-291-hepatitis-screening-2x2-table.jpg
note: same as PH-P-295 -- never calculated on the page, left open.
Same Hepatitis B screening exercise as PH-P-291. Negative predictive value?

### PH-P-297
tier: claimed
form: qa
claimed: Cross-sectional
note: "Exercise II", an 11-item short-abstract-to-study-design matching sheet with its own lettered key (A. Prospective cohort, B. Retrospective (case-control), C. Cross-sectional, D. Program Trial, E. Program Review, F. Clinical Trial, G. Ecological). Cross-references row 6's PH-P-201 -- same scenario, same answer, not merged (different batch).
The growth patterns of infants aged 6-24 months were assessed on the basis of a single measurement of height, weight and head circumference of the population receiving care at the Family Health Centers in the northern and southern regions of Jordan.

### PH-P-298
tier: claimed
form: qa
claimed: Ecological
note: cross-references PH-P-202 (row 6) -- same scenario, same answer.
The association between levels of air pollution and mortality rate in different European countries was studied.

### PH-P-299
tier: claimed
form: qa
claimed: Case-control
note: cross-references PH-P-203 (row 6) -- same scenario, same answer.
The reduction in the likelihood of experiencing myocardial infraction (MI) amongst women who stopped smoking was shown by comparing the smoking habits of women who had experienced a MI with the smoking habits of women free of MI.

### PH-P-300
tier: claimed
form: qa
claimed: Retrospective (case-control)
note: cross-references PH-P-204 (row 6) -- same scenario, same answer.
A proposal was recently accepted to study the association between exposure to radiation as a treatment for trichophytiasis (a dermatological condition of the scalp) and brain tumors, the proposed study will compare the rate of brain tumors among persons who had received the radiation treatment in the 1950s with the rate of brain tumors among persons who received other modes of treatment during those same years.

### PH-P-301
tier: claimed
form: qa
claimed: Prospective cohort
note: cross-references PH-P-205 (row 6) -- same scenario, same answer.
The study of type A personality as a predictor of the risk for stroke.

### PH-P-302
tier: claimed
form: qa
claimed: Cohort study
note: cross-references PH-P-206 (row 6) -- same scenario, same answer.
An investigator takes a sample of healthy individuals, record their ongoing solar exposure, and relate that to the subsequent occurrence of skin cancer in the same group.

### PH-P-303
tier: claimed
form: qa
claimed: Cohort study
note: cross-references PH-P-207 (row 6) and PH-P-022 (row 5) -- same HIV/TB-in-Kenya scenario, same answer.
A study was conducted to investigate the effect of HIV infection on mortality among people in Kenya with TB. Individuals with TB were recruited from hospitals and their HIV status determined. They were then followed-up over ten years to compare mortality rates in the HIV positive group and HIV negative group.

### PH-P-304
tier: claimed
form: qa
claimed: Clinical Trial
note: cross-references PH-P-208 (row 6) -- same scenario, same answer.
A study was conducted to determine whether recurrences of urinary tract infection (UTI) can be prevented with cranberry-lingonberry juice.

### PH-P-305
tier: claimed
form: qa
claimed: Program Trial
note: cross-references PH-P-209 (row 6) -- same scenario, same answer.
A study was conducted to examine the effectiveness of a community-based multimodal intervention program for suicide prevention in regions where the suicide rate was relatively high compared to control regions.

### PH-P-306
tier: claimed
form: qa
claimed: Clinical Trial
note: cross-references PH-P-210 (row 6) -- same scenario, same answer.
A study was conducted to assess the effect of vitamin supplementation on the intelligence development of 6-8 year old children.

### PH-P-307
tier: claimed
form: qa
claimed: Program review
note: cross-references PH-P-211 (row 6) -- same scenario, same answer.
An evaluation was conducted for participant after 3 months of intervention to increase awareness for hypertension.
