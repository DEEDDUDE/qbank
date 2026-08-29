---
course: pharmacology
tab: finals
questions: 203
tiers: official 0 | claimed 157 | open 46
forms: mcq 161 | qa 42
needs-eye: 1
disputed: 10
next-id: PHARM-F-205
retired: PHARM-F-151 (duplicate of PHARM-F-020, ID kept as a tombstone rather
  than reused per the no-renumbering rule -- excluded from all counts above)
---

<!-- batch 01 -- raw/finals/2020-2021/ (RUN-PLAN row 15), 55 vision pages after
  prep.py's exact-hash dedupe (4 dropped inside folder 3). Three separate captures
  of ONE sitting, none of them a printed key -- every page is a plain Moodle student
  view ("Answer saved" / "Not yet answered"), so tier tops out at claimed:

    1/Pharma Final 2020-2021.pdf   -- 17 pages, one scanned/exported attempt,
      28 numbered Moodle questions (3 of them EMQ "match" items worth 5 marks
      each -- expanded into individual qa entries per question, same treatment
      as PHARM-P-186/187's split).
    2/received_*.jpeg (Messenger)  -- 14 photos, overwhelmingly one attempt
      (Moodle attempt=439611, cmid=253517) captured across several screenshots
      taken at different points of completion -- the same question sometimes
      appears both "Not yet answered" and later "Answer saved" across different
      photos in this folder. The later, answered state was always taken as the
      real claim; the earlier blank one was not treated as a competing claim.
    3/*.JPG (camera roll)          -- 24 photos of a physical monitor screen,
      spanning what turned out to be at least FOUR more distinct attempts (question
      counts of 20, 33+, 47+, and 54 were each seen as a genuine last page/highest
      number, so they are not all the same run). Same "earlier blank / later
      answered" pattern shows up here too (Q5, Q29, Q37/52, Q44, Q46 all have both
      states across different photos of the same attempt).

  None of these are randomized "models" of a fixed exam in the نموذج sense --
  Moodle drew from a shared/overlapping question bank per attempt, with different
  attempts drawing different subsets, different question ORDER, and different
  in-page OPTION order (sometimes even different distractor sets for the same
  stem -- see PHARM-F-074). Per RUN-PLAN row 15's own instruction, everything was
  merged by matching STEM TEXT across all three folders, not by question number,
  the same technique used for microbiology's finals نموذج 1/5 reconciliation --
  just applied across captures of one shared bank rather than shuffled copies of
  one fixed exam. Where a stem exists in more than one capture:
    - same claimed content (letter differs because options were reshuffled) ->
      recorded once, no note.
    - one capture claimed, the other(s) open -> recorded once as claimed, no
      dispute (an open capture contributes no competing claim).
    - two (or more) captures both claim, and the claimed CONTENT differs ->
      recorded as disputed: true with a claims: list, canonical option order
      taken from whichever capture is listed first.

  Six genuine disputes surfaced this way: PHARM-F-007, 025, 029, 031, 037, 039.

  One fragment dropped rather than guessed: a camera-roll photo (3/58a80d2c...,
  used for PHARM-F-039/067's page) shows a truncated "Question 26" with options
  "b. Transpeptidase enzyme / c. Beta-lactamase and transpeptidase / d. Cell
  membrane synthesis" and a "Clear my choice" line proving something was selected
  -- almost certainly another capture of the Timentin-mechanism question (PHARM-F-
  010), but the stem, option (a), and which radio was filled are all cut off above
  the photo's frame. Since PHARM-F-010 is already fully resolved from two clean
  captures and this fragment can't add a legible claim, it was not turned into a
  separate entry or forced into a match.

  PHARM-F-056/EMQ41's "folic acid synthesis / effective UTI treatment" blank
  claims "Gentamycin" -- checked twice against the photo's own row alignment
  (perspective skew made this worth confirming) and the row match is correct;
  the claim itself just looks pharmacologically wrong. Recorded as-is per hard
  rule 5 (extraction never answers) -- Job C's problem, not this one's.

  PHARM-F-074 (cephalosporins/hepatic route) was seen in two different attempts
  with two different DISTRACTOR SETS for the same stem and correct-seeming answer
  ("Ceftriaxone" present as an option both times) -- not a reshuffle, an actually
  different option list. Both were open (no claim either way), so this isn't a
  dispute; the fuller capture's options are recorded, with a note on the variant.

  Zero questions in this batch depend on a photo/graph for their content -- pure
  text MCQs and EMQs throughout -- so no img: crops were needed except for the two
  needs-eye entries below (missing option text, not an unreadable image). -->

### PHARM-F-001
tier: claimed
form: mcq
type: single
claimed: b
Why are viral infections especially difficult to treat?
a) Because there are many types of viral structures
b) Because they rely upon their host cells for the majority of their metabolic
   functions
c) Because viruses can halt their metabolism when in the presence of an
   antiviral agent
d) Because they can have RNA as their nucleic acid

### PHARM-F-002
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3, 4, 6]
note: Same claim seen in two captures (PDF Q2, folder 2 Q19), reshuffled
  options. Also seen in the 2023-2024 sitting's model 3 (same claim, "The ED50
  is a measure of drug's efficacy") and model 6 (unanswered).
All of the following statements about efficacy and potency are true EXCEPT?
a) Efficacy is the maximum effect of a drug
b) The ED50 is a measure of drug's efficacy
c) Potency is a comparative measure, refers to the different doses of two drugs
   that are needed to produce the same effect
d) Efficacy is usually a more important clinical consideration than potency

### PHARM-F-003
tier: open
form: mcq
type: single
A 38-old patient has primary syphilis. He has a history of penicillin
hypersensitivity, so tetracycline could be used to treat this infection. Which
statement about the proposed drug treatment of this patient is accurate?
a) Azithromycin would not be effective in the treatment of this patient
b) Tetracycline is a potent hepatic cytochrome inhibitor
c) Antacids do not affect absorption of the drug
d) Consumption of milk may decrease tetracycline oral bioavailability

### PHARM-F-004
tier: claimed
form: qa
claimed: Itraconazole
Antifungal drugs producing its effect through inhibition of CYP 450 (EMQ, part
1 of 5)

### PHARM-F-005
tier: claimed
form: qa
claimed: Terbinafine
Squalene epoxidase inhibitor (EMQ, part 2 of 5)

### PHARM-F-006
tier: claimed
form: qa
claimed: Nystatin
Drug that is used orally to treat oral candidiasis and this agent is highly
toxic if given parenterally. (EMQ, part 3 of 5)

### PHARM-F-007
tier: claimed
form: qa
disputed: true
claims:
  - source: PDF capture
    answer: Itraconazole
  - source: Messenger capture (folder 2)
    answer: Amphotericine B
The effect of Amphotericine B will be antagonize by the use of ________. (EMQ,
part 4 of 5)

### PHARM-F-008
tier: claimed
form: qa
claimed: Caspofungin
note: Open ("Choose...") in the PDF capture; filled in by the Messenger capture.
An antifungal drug that used intravenously and produce it effect by inhibiting
the synthesis of fungal cell wall component. (EMQ, part 5 of 5)

### PHARM-F-009
tier: claimed
form: mcq
type: single
claimed: b
Oral bioavailability of the drug could be affected by which of the following?
a) Gastric acidity and gastric enzymes
b) All them
c) Expression of intestinal P-glycoprotein
d) Metabolism by liver enzymes prior to reaching the systemic circulation

### PHARM-F-010
tier: claimed
form: mcq
type: single
claimed: e
note: Same claim content confirmed in two captures (PDF, Messenger), reshuffled
  options.
The primary mechanism of antibacterial action of Timentin® (Ticarcillin +
Clavulanic Acid) involves inhibition of?
a) Cell membrane synthesis
b) Beta-lactamases
c) None
d) Peptidoglycan cross-linking
e) Transpeptidase and beta-lactamases

### PHARM-F-011
tier: claimed
form: mcq
type: single
claimed: d
note: Same claim confirmed in two captures (PDF, Messenger), reshuffled options.
Acyclovir is and mostly used to treat?
a) Reverse transcriptase inhibitor/ hepatitis
b) Protease inhibitor/ AIDS
c) Non-nucleotide analogue/ hepatitis
d) Nucleotide analogue/ herpes

### PHARM-F-012
tier: claimed
form: qa
claimed: Gentamycin
Antimicrobial agents affect protein synthesis in bacteria and belong to
antimicrobial group referred to as 'aminoglycosides': (EMQ, part 1 of 5)

### PHARM-F-013
tier: claimed
form: qa
claimed: Moxifloxacin
An antibiotic which interferes with DNA synthesis: (EMQ, part 2 of 5)

### PHARM-F-014
tier: claimed
form: qa
claimed: trimethoprim
Antimicrobial agent/s that used as bacterial antimetabolite: (EMQ, part 3 of 5)

### PHARM-F-015
tier: claimed
form: qa
claimed: Vancomycin
An antibiotic that is administered orally for the treatment of pseudomembranous
colitis: (EMQ, part 4 of 5)

### PHARM-F-016
tier: claimed
form: qa
claimed: Doxycycline
An antibiotic that is contraindicated in children under 8 years due to risk of
bone malformation: (EMQ, part 5 of 5)

### PHARM-F-017
tier: claimed
form: mcq
type: single
claimed: e
Concerning vancomycin, all the following is correct EXCEPT?
a) Binds to PBPs
b) Of poor oral bioavailability
c) Linezolid could be used in cases of vancomycin resistance
d) Could be used in treatment of infections caused by MRSA
e) Beta lactam containing drug

### PHARM-F-018
tier: claimed
form: mcq
type: single
claimed: c
note: Same claim confirmed in two captures (PDF, Messenger), reshuffled options.
A 33-year-old female is diagnosed as suffering from genital herpes (HSV-2).
Which of the following drugs could be used orally to treat her complain?
a) Foscarnet
b) Amantadine
c) Valacyclovir
d) Ritonavir

### PHARM-F-019
tier: claimed
form: mcq
type: single
claimed: d
note: Open ("Not yet answered") in the PDF capture; a Messenger capture of the
  same attempt later shows it answered.
Which of the following routes of administration would be appropriate and
convenient for home administration of an antimicrobial to treat a systemic
infection?
a) None of them
b) Intra-articular
c) Intravenous
d) Oral
e) Rectal

### PHARM-F-020
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2, 5, 6]
note: Open in the PDF capture; filled in by a Messenger capture. Also seen in
  the 2023-2024 sitting's model 6 (unanswered, same stem/options reshuffled)
  and model 2 (claimed, same content). PHARM-F-151 was a duplicate of this
  entry, retired rather than kept as a live second copy.
Which of the following statements about the fluoroquinolones is LEAST
accurate?
a) A fluoroquinolone is the drug of choice for treatment of an uncomplicated
   urinary tract infection in a 10-year-old girl
b) Modification of fluoroquinolone dosage is required in patients with kidney
   dysfunction
c) Fluoroquinolones inhibit DNA synthesis
d) Antacids may decrease the oral bioavailability of fluoroquinolones

### PHARM-F-021
tier: open
form: mcq
type: single
A 45-year-old patient with asthma, he complains of flu-like symptoms, most
likely the causative agent of his symptoms is influenza virus. Choose the best
appropriate treatment for this patient?
a) Rimantadine
b) Zanamivir
c) Both Oseltamivir and Zanamivir
d) Oseltamivir

### PHARM-F-022
tier: open
form: mcq
type: single
Clindamycin therapeutic uses?
a) In treatment of UTI
b) In treatment of soft tissue infection in combination with erythromycin
c) In treatment of erythromycin resistant infections
d) All
e) In treatment of osteomyelitis in combination with ciprofloxacin

### PHARM-F-023
tier: open
form: mcq
type: single
Choose the drug that inhibits viral proteases?
a) Nevirapine
b) Acyclovir
c) Saquinavir
d) Zidovudine

### PHARM-F-024
tier: claimed
form: mcq
type: single
claimed: e
models: [3, 5]
note: Open in this batch's own captures; the 2023-2024 sitting's model 3
  claims "Information about unwanted effects" (option e here) for the same
  stem/options reshuffled.
Pharmacodynamics involves the following?
a) Information about biological barriers
b) All of them
c) Information about main mechanisms of drug absorption
d) Information about excretion of a drug from the organism
e) Information about unwanted effects

### PHARM-F-025
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: Messenger capture
    answer: c (The final cross-linking reaction to form the bacterial cell
      wall)
  - source: camera-roll capture
    answer: a (The hydrolysis of the four-membered ring present in
      penicillin's)
note: Open in the PDF capture; canonical option order taken from the PDF.
β-lactamase enzyme reaction is?
a) The hydrolysis of the four-membered ring present in penicillin's
b) The biosynthesis of the penicillin structure from the amino acids valine
   and cysteine
c) The final cross-linking reaction to form the bacterial cell wall
d) The hydrolysis of the acyl side chain from penicillin structures

### PHARM-F-026
tier: claimed
form: mcq
type: single
claimed: c
note: Open in the PDF capture; filled in by a Messenger capture.
Clavulanic acid is combined with amoxicillin because?
a) It counteracts the adverse effects of amoxicillin
b) It reduces renal clearance of amoxicillin
c) It inhibits beta lactamases that destroy amoxicillin
d) It kills bacteria that are not killed by amoxicillin

### PHARM-F-027
tier: open
form: mcq
type: single
Patients treated with erythromycin may suffer from?
a) Reversible ototoxicity
b) All
c) GI intolerance
d) Prolongation of QTc interval

### PHARM-F-028
tier: open
form: mcq
type: single
All of the following antibiotics acts by binding with 50S subunit of bacterial
ribosomes except ___?
a) Dalfopristin
b) Clindamycin
c) Erythromycin
d) Tetracycline

### PHARM-F-029
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: a (Inhibiting the release of the virus)
  - source: Messenger capture
    answer: d (Inhibiting nucleic acid synthesis)
Oseltamivir (Tamiflu)® is an antiviral drug that acts by?
a) Inhibiting the release of the virus
b) Inhibiting uncoating
c) Inhibiting attachment
d) Inhibiting nucleic acid synthesis

### PHARM-F-030
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2, 3, 4, 6]
note: Same claim confirmed in two captures (PDF, Messenger), reshuffled
  options. Also seen in the 2023-2024 sitting's model 3 (same claim), model 6
  (unanswered), and model 2 (same claim).
The intensity of the pharmacologic action of drug depend on?
a) Minimum effective concentration of the drug
b) Onset time of the drug after oral administration
c) Elimination half-life of the drug
d) Concentration of the drug and the intrinsic activity of the drug

### PHARM-F-031
tier: claimed
form: qa
disputed: true
claims:
  - source: PDF capture
    answer: Ceftriaxone
  - source: Messenger capture
    answer: Meropenem and Ceftriaxone
Betalactam containing drug that is effective in treatment of bacterial
meningitis (EMQ, part 1 of 5)

### PHARM-F-032
tier: claimed
form: qa
claimed: Moxifloxacin
Fluoroquinolone that has high activity on gram-positive bacterial infection
(EMQ, part 2 of 5)

### PHARM-F-033
tier: claimed
form: qa
claimed: Gentamicin
note: Open in the PDF capture; filled in by a Messenger capture.
Protein synthesis inhibitor that is administered only parenterally for
systemic infections (EMQ, part 3 of 5)

### PHARM-F-034
tier: claimed
form: qa
claimed: Clarithromycin
CYP 3A4 inhibitor (EMQ, part 4 of 5)

### PHARM-F-035
tier: claimed
form: qa
claimed: Clarithromycin
note: Open in the PDF capture; filled in by a Messenger capture.
An antibiotic(s) better be used in a patient who has had an anaphylactic
reaction to penicillin (first choice) (EMQ, part 5 of 5)

### PHARM-F-036
tier: claimed
form: mcq
type: single
claimed: c
Which of the following drugs can be used for varicella zoster virus?
a) Foscarnet
b) Acyclovir
c) Penciclovir
d) All
e) Ganciclovir

### PHARM-F-037
tier: claimed
form: mcq
type: single
disputed: true
models: [1, 2, 3, 4, 5, 6]
claims:
  - source: PDF capture
    answer: e (Sulfasalazine)
  - source: Messenger capture
    answer: b (Trimethoprim)
  - source: model 3 (2023-2024 sitting)
    answer: b (Trimethoprim)
  - source: models 2, 4, and 5 (2023-2024 sitting, agree)
    answer: c (Cotrimoxazole)
note: Model 6 also carries this stem/options reshuffled, unanswered. Model 2
  added a THIRD distinct claim value to an already-disputed question; models 4
  and 5 independently reinforce it. Model 5's radio showed filled despite the
  page's own "Not yet answered" badge -- see the batch 05 header comment for
  this discrepancy, seen on several of model 5's later questions.
Which of the following drugs is a sequential inhibitor of folate metabolism
(foliate antagonists)?
a) Sulfacetamide
b) Trimethoprim
c) Cotrimoxazole
d) Sulfamethoxazole
e) Sulfasalazine

### PHARM-F-038
tier: claimed
form: mcq
type: single
claimed: a
Which of the following adverse effect/s is/are associated with vancomycin?
a) Ototoxicity and red man syndrome
b) All
c) Bone marrow depression
d) Red man syndrome
e) Ototoxicity

### PHARM-F-039
tier: claimed
form: mcq
type: single
disputed: true
claims:
  - source: PDF capture
    answer: a (All)
  - source: Messenger capture
    answer: d (Aztreonam)
Which of the following β-lactams is the most appropriate choice for
gram-negative coverage in penicillin allergic?
a) All
b) Cefepime
c) Ceftaroline
d) Aztreonam

### PHARM-F-040
tier: claimed
form: mcq
type: single
claimed: a
note: Same claim confirmed in two captures (PDF, Messenger), reshuffled options.
Therapeutic index (TI) is?
a) A ratio used to evaluate the safety and usefulness of a drug for indication
b) A ratio used to evaluate the elimination of a drug
c) A ratio used to evaluate the effectiveness of a drug
d) A ratio used to evaluate the bioavailability of a drug

### PHARM-F-041
tier: claimed
form: mcq
type: single
claimed: b
Which sentence about ampicillin is not correct?
a) Antibacterial activity enhanced by sublactam
b) Effective against MRSA
c) Extended spectrum penicillin
d) Acid stable
e) May cause pseudomembranous colitis

### PHARM-F-042
tier: claimed
form: mcq
type: single
claimed: c
note: Also seen open/unanswered in a camera-roll capture with reshuffled
  options -- no competing claim there, so not a dispute.
Which of the following combinations would most likely contribute to the
development of a superinfection?
a) Short-term use of broad-spectrum antimicrobials
b) Long-term use of either narrow or broad-spectrum antimicrobials
c) Long-term use of broad-spectrum antimicrobials
d) Long-term use of narrow-spectrum antimicrobials
e) None of them

### PHARM-F-043
tier: claimed
form: mcq
type: single
claimed: d
Chloramphenicol use is restricted for life threatening infections, because of?
a) Having very narrow spectrum of activity
b) All
c) Its bacteriostatic property
d) Its increased toxicity

### PHARM-F-044
tier: claimed
form: mcq
type: single
claimed: b
note: Same underlying question also seen open/unanswered in a camera-roll
  capture, reworded as "Combination of sulfonamides with trimethoprim will lead
  to?" with the same four options reordered -- no competing claim there.
Sulfamethoxazole with trimethoprim in combination will lead to?
a) Decrease the antimicrobial activity
b) Increase the antimicrobial activity
c) Increase the elimination of sulfonamides
d) Decrease the unwanted effects of sulfonamides

### PHARM-F-045
tier: claimed
form: mcq
type: single
claimed: b
A 3-day-old neonate, born at 37 weeks' gestation, who presents with new onset
fever, lethargy, and decreased desire to feed. Based on his age, which of the
following antibiotics is considered safe to use in neonates?
a) Chloramphenicol
b) Ampicillin
c) Sulfamethoxazole/trimethoprim
d) Tetracycline

### PHARM-F-046
tier: open
form: mcq
type: single
Which of the following terms refers to the ability of an antimicrobial drug to
harm the target microbe without harming the host?
a) Spectrum of activity
b) Mechanism of action
c) Direct toxicity
d) Selective toxicity

### PHARM-F-047
tier: open
form: mcq
type: single
Which of the following antibacterial classes is/are contraindicated during
pregnancy?
a) Aminoglycosides
b) All of them
c) Aminoglycosides and Fluoroquinolones
d) Cephalosporins
e) Fluoroquinolones

### PHARM-F-048
tier: open
form: mcq
type: single
Which of the following antiviral drugs could be used to treat CMV infections?
a) Acyclovir and Ganciclovir
b) Ganciclovir
c) Amantadine
d) Acyclovir

### PHARM-F-049
tier: claimed
form: mcq
type: single
claimed: b
note: Same stem also seen open/unanswered (earlier point of the same attempt).
The following cephalosporins can cross the blood-brain barrier and therefore
can be used in the treatment of meningitis EXCEPT?
a) Cefotaxime
b) All of them can be used effectively against meningitis
c) Ceftazidime
d) Ceftriaxone
e) Cephalexin

### PHARM-F-050
tier: open
form: mcq
type: single
Acidification of urine decreases the reabsorption of?
a) Weakly basic drugs
b) Non-polar drugs
c) Weakly acidic drugs
d) Strong electrolytes

### PHARM-F-051
tier: open
form: mcq
type: single
Linezolid would be a good choice for antibiotic treatment in which of the
following patient scenarios?
a) Bacterial infection caused by MRSA
b) All of them
c) Bacterial infection caused by VRE
d) Bacterial infection caused by VRSA

### PHARM-F-052
tier: open
form: mcq
type: single
Which of the following group of antibiotics in terms of structure and mode of
action is similar to penicillin?
a) Cycloserines
b) Polymyxins
c) Cephalosporins
d) Chloramphenicol

### PHARM-F-053
tier: claimed
form: qa
claimed: Moxifloxacin and ciprofloxacin
An antibiotic that interferes with DNA synthesis by inhibiting DNA synthesis
enzyme and is effective in treatment of respiratory infections, but is
ineffective in treatment of UTI: (EMQ, part 1 of 6)

### PHARM-F-054
tier: open
form: qa
An antibacterial agent affects protein synthesis and considered as the best
choice for penicillin allergic patient: (EMQ, part 2 of 6)

### PHARM-F-055
tier: open
form: qa
An antibiotic that is administered orally for the treatment of
pseudomembranous colitis: (EMQ, part 3 of 6)

### PHARM-F-056
tier: claimed
form: qa
claimed: Gentamycin
note: Row alignment double-checked against the photo's own perspective skew --
  this blank really is claimed Gentamycin, even though that claim looks
  pharmacologically wrong for a folic-acid-synthesis question. Recorded as-is;
  extraction doesn't judge correctness.
An antibiotic which interferes with folic acid synthesis and could be used as
effective treatment for UTI: (EMQ, part 4 of 6)

### PHARM-F-057
tier: open
form: qa
An antibiotic that is contraindicated in children under 8 years due to risk of
bone malformation: (EMQ, part 5 of 6)

### PHARM-F-058
tier: open
form: qa
An aminoglycoside that is used orally to treat hepatic encephalopathy and it
is highly nephrotoxic when it is used as systemic treatment: (EMQ, part 6 of
6)

### PHARM-F-059
tier: claimed
form: mcq
type: single
disputed: true
models: [1, 2, 3, 4, 6]
img: flagged/PHARM-F-059-beta-lactamase-resistance-mechanism-incomplete-options.jpg
claims:
  - source: 2020-2021 sitting (all captures)
    answer: Efflux pump
  - source: models 2, 3, and 4 (2023-2024 sitting, agree)
    answer: Drug inactivation
note: Every 2020-2021 capture of this question crops the option list to just
  "a. Efflux pump" (selected) before the frame or the keyboard cuts it off --
  options b-d were never captured legibly anywhere in that batch, so this
  entry originally carried status: needs-eye for failing the >=2-option
  structural floor. The 2023-2024 sitting's model 3 supplies the full option
  list (below, model 3's own lettering) and claims a DIFFERENT answer --
  b. Drug inactivation -- for the same stem, so needs-eye is resolved (options
  now fully known) but the question is now disputed instead. Models 2 and 4
  independently agree with model 3's claim (same content, "Drug
  inactivation"). Model 6 carries the same stem/options reshuffled,
  unanswered. The original crop stays in flagged/ per the img: rule even
  though the option list is now known from a fuller capture.
Which of the following resistance mechanisms describes the function of
β-lactamase?
a) Drug inactivation
b) None of them
c) Target overproduction
d) Target mimicry
e) Efflux pump

### PHARM-F-060
tier: open
form: mcq
type: single
Widespread and prolonged use of an antibiotic leads to emergence of drug
resistant strains because antibiotics?
a) Induce mutation in the bacteria
b) All of them
c) Promote conjugation among bacteria
d) Allow resistant strains to propagate preferentially

### PHARM-F-061
tier: claimed
form: mcq
type: single
claimed: a
note: Same stem also seen open/unanswered (earlier point of the same attempt),
  fuller stem text recovered from that capture.
A 35-year old female treated with oral clindamycin for respiratory tract
infection, After 3 days of treatment the patient develops diarrhea (10 watery
stools/day), severe abdominal pain, and fever. Which of the following
organisms would you be concerned about as the causative pathogen of diarrhea?
a) Staphylococcus aureus
b) Bacteroides fragilis
c) Clostridium difficile
d) Escherichia coli

### PHARM-F-062
tier: open
form: mcq
type: single
Which clinical situation would be appropriate for treatment with a
narrow-spectrum antimicrobial drug?
a) Prophylaxis against infection after a surgical procedure
b) Empiric therapy of pneumonia while waiting for culture results
c) Treatment of strep throat caused by culture identified Streptococcus
   pyogenes
d) Treatment of intestinal infection caused by a polymicrobe

### PHARM-F-063
tier: claimed
form: mcq
type: single
claimed: c
note: Same stem also seen open/unanswered (earlier point of the same attempt).
You start an IV infusion of a drug to a patient at a rate of 500 mg/hr. The
drug is known to be cleared by first order kinetics. Which single variable
will allow you to determine how long it will take to reach a steady-state drug
level?
a) Dosage rate (mg/hr)
b) Infusion rate
c) Bioavailability
d) Volume of distribution
e) Elimination half life

### PHARM-F-064
tier: open
form: mcq
type: single
Correct statements listing characteristics of a particular route of drug
administration include all the following EXCEPT?
a) Subcutaneous administration may cause local irritation
b) Inhalation provides slow access to the general circulation
c) Intravenous administration provides a rapid response
d) Intramuscular administration requires a sterile technique

### PHARM-F-065
tier: open
form: mcq
type: single
status: needs-eye
img: flagged/PHARM-F-065-steven-johnson-trimethoprim-no-options.jpg
note: Both captures of this question cut off at the stem -- no option text was
  ever captured for it. Structural floor: an mcq needs >=2 visible options.
Steven Johnson disease is a severe condition associated with trimethoprim
drugs?

### PHARM-F-066
tier: claimed
form: mcq
type: single
claimed: a
Lower plasma and urinary concentrations of fluoroquinolones and loss of
antibacterial effectiveness may result if the drug is taken within two hours
of which of the following?
a) Aspirin
b) Calcium supplement
c) Tea
d) Vitamin K

### PHARM-F-067
tier: open
form: mcq
type: single
note: Recovered across two overlapping camera-roll photos -- one caught only
  the tail of the option list (c, d), the other the full question.
Which of the following are the penicillinase-resistant penicillin except?
a) Cloxacillin
b) Nafcillin
c) Ampenicillin
d) Methicillin

### PHARM-F-068
tier: open
form: mcq
type: single
All of the followings are the adverse effects of tetracycline except:
a) Crystal urea
b) Fatal hepatotoxicity
c) Phototoxicity
d) Bone malformation

### PHARM-F-069
tier: open
form: mcq
type: single
Ototoxicity, nephrotoxicity, and muscle paralysis are seen as major adverse
effects of?
a) Fluoroquinolones
b) Macrolides
c) Aminoglycosides
d) All of them

### PHARM-F-070
tier: claimed
form: mcq
type: single
claimed: a
Crystalluria is one of the sulfonamides side effect that can be prevented by
acidification of urine?
a) False
b) True

### PHARM-F-071
tier: open
form: mcq
type: single
note: Stem partially obscured mid-sentence by a floating UI element ("Time
  left...") in the only capture; the gap doesn't affect the answer options.
A scientist discovers that a soil bacterium he has been studying produces an
antimicrobial that kills gram-negative bacteria. She isolates and purifies the
antimicrobial compound. She chemically converts a chemical side chain to a
hydroxyl group. When she tests the antimicrobial properties of this new
version, she finds that this antimicrobial drug can now [text obscured] kill
gram-positive bacteria too. The new antimicrobial drug with broad-spectrum
activity is considered to be which of the following?
a) Natural occurring
b) Resistant
c) Synthetic
d) Semisynthetic

### PHARM-F-072
tier: open
form: mcq
type: single
Pharmacokinetics is a study that involves the following EXCEPT?
a) Information about main mechanisms of drug absorption
b) Information about excretion of a drug from the organism
c) Information about drug distribution in the tissue
d) Information about clinical response

### PHARM-F-073
tier: claimed
form: mcq
type: single
claimed: c
Which of the following combinations is correct?
a) Penicillin: inhibition of cell membrane synthesis
b) Aminoglycoside: inhibition of cell wall synthesis
c) Fluoroquinolones: inhibition of DNA synthesis
d) Cephalosporin: inhibition of protein synthesis
e) None of them

### PHARM-F-074
tier: open
form: mcq
type: single
note: Seen in two attempts with two different distractor sets for the same
  stem ("All of them" / "Ceftriaxone" common to both) -- not a reshuffle, a
  genuinely different option list. Neither attempt claims an answer, so this
  isn't a dispute. Fuller/clearer capture's options recorded; the other capture
  showed b) Cefazoline, c) Cefepime in place of b) Cefotaxime, c) Cefixime.
Which of the following cephalosporins is mainly eliminated via hepatic route?
a) All of them
b) Cefotaxime
c) Cefixime
d) Ceftriaxone

### PHARM-F-075
tier: open
form: mcq
type: single
Methicillin resistant staphylococci bacteria do not respond to another
β-lactam antibiotics because?
a) They release an amidase enzyme which destroys methicillin and related drugs
b) They have mutated penicillin binding protein which has low affinity for
   β-lactam antibiotics
c) They produce a β-lactamase which destroys methicillin and related drugs
d) They are less permeable to β-lactam antibiotics

### PHARM-F-076
tier: open
form: mcq
type: single
Protease inhibitors are the agents that leads to inhibit the enzyme
responsible for cleavage of the viral proteins required for infectious virus
particles?
a) False
b) True

### PHARM-F-077
tier: open
form: mcq
type: single
Your patient is 10-year-old boy with tinea pedis, which one of the following
is the best choice to treatment this patient?
a) Caspofungin
b) Amphotericin B
c) Terbinafine
d) Nystatin

### PHARM-F-078
tier: open
form: mcq
type: single
Gray baby syndrome in neonates can be caused by
a) Quinolones
b) Chloramphenicol
c) Sulfonamides
d) Penicillin

### PHARM-F-079
tier: open
form: mcq
type: single
Fluorinated quinolones are all of the following EXCEPT?
a) None of them
b) Ciprofloxacin
c) Nalidixic Acid
d) Pefloxacin
e) Ofloxacin

<!-- batch 02 -- raw/finals/2023-2024/Medicine/3.pdf + 6.pdf (RUN-PLAN row 17),
  52 vision pages, 26 each. These are models 3 and 6 of the 2023-2024 Medicine
  sitting's 6-model reshuffle (rows 16-19 cover the other four); both are
  plain Moodle student views, no printed key, so tier tops out at claimed.
  Model 3 (3.pdf) is a live-exam capture, mostly "Answer saved" with the
  in-progress timer chrome visible; model 6 (6.pdf) is entirely
  "Not yet answered" -- an unattempted/abandoned run, so it contributes stems
  and option sets but no claims of its own.

  Handled per the job-a-extract.md "reshuffled models" exception: matched by
  STEM TEXT (not question number) across model 3 and model 6, each entry that
  appears in more than one model gaining a models: [..] field. Model 3's 46
  questions and model 6's 49 were also checked by stem against the existing
  batch 01 (2020-2021 sitting) entries -- not a routine step, but justified
  here because six exact stem+option matches turned up (PHARM-F-002, 020,
  024, 030, 037, 059), proving the two sittings draw from the same
  underlying bank rather than being independent question pools. Those six
  existing entries were enriched in place (models: field added, a claim
  reinforced or newly supplied) rather than re-minted as new IDs; everything
  else below is new (PHARM-F-080 onward).

  Two genuine gaps in model 3's own numbering, not read failures: Q3, Q4, Q7
  and Q50 never appear in any of the 26 captured pages. One further ambiguity
  resolved by elimination: page 4 opens on a question with no visible
  "Question N" header (cropped by the page boundary) sitting between the
  captured Q5 and Q8 -- since a later page explicitly labels a different
  question "Question 6", the unlabeled one was assigned Q7 rather than Q6 by
  process of elimination, and is folded into PHARM-F-134 below (which carries
  its own note explaining it's a near-miss, not a match, for PHARM-F-069).

  PHARM-F-059 (β-lactamase resistance mechanism) went from single-option
  needs-eye to disputed: model 3 supplies the full 5-option list this batch's
  own 2020-2021 captures never fully showed, but claims a DIFFERENT answer
  (Drug inactivation vs. the original Efflux pump) -- recorded as a genuine
  disagreement, not silently overwritten. PHARM-F-090 (penicillinase-resistant
  penicillin except) is a near-miss with PHARM-F-067 from batch 01 -- same
  stem, but a smaller and differently-worded option set -- kept as a separate
  entry with a cross-reference note rather than force-merged, same treatment
  as batch 01's own PHARM-F-074 precedent.

  Two multi-part items follow the EMQ/matching convention already used in
  batch 01 (each part its own qa entry, numbered "part X of Y"): model 3's
  Q36 (a 5-drug matching question, seen in both models, PHARM-F-107-111) and
  Q37 (an 8-item EMQ, model 3 only, PHARM-F-112-119); model 6 has its own,
  unrelated 8-item EMQ (Q45, PHARM-F-158-165), entirely unanswered. Model 6's
  matching/EMQ dropdowns show pre-filled-looking text even under "Not yet
  answered" -- a Moodle display default for this question type, not a real
  claim, so none of model 6's own matching/EMQ items carry a claimed: value.

  Zero questions in this batch depend on a photo/graph for their content --
  pure text MCQs, one matching question, and two EMQs throughout, so no img:
  crops were needed.

  CORRECTION (post-write, confirmed against row 16's raw/finals/2023-2024/
  Medicine/1.pdf): 1.pdf and 6.pdf are two captures of the SAME underlying
  Moodle attempt, not two independently-reshuffled models -- word-for-word
  identical stems AND identical option order across every question checked,
  both entirely "Not yet answered." File hashes differ (not literally the
  same file), so this is a re-export/re-capture of one exam instance under
  two different raw filenames, not a coincidence -- confirmed independently
  by both sessions comparing rendered pages directly, not just extracted
  text. The "6-model reshuffle" framing this row and RUN-PLAN rows 16-19
  inherited from the raw folder's 1.pdf-6.pdf naming does NOT reliably mean
  six distinct Moodle models; at least one of the six raw files is a
  duplicate capture. Every models: field that named 6 was updated to also
  name 1 (models: [6] -> [1, 6], models: [3, 6] -> [1, 3, 6]) rather than
  picking one numeral as canonical -- neither raw filename is known to be
  the "true" Moodle model number, so both are kept. Row 16 is skipping
  re-extraction of 1.pdf as a result; see its own RUN-PLAN note. -->

### PHARM-F-080
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 3, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
A 62-year old man recently diagnosed with onychomycosis started a treatment
with terbinafine. Inhibition of which of the following enzymes most likely
mediated the therapeutic effect of the drug in the patient's disease?
a) Lanosterol synthetase
b) Thymidylate synthase
c) Squalene epoxidase
d) Transpeptidase
e) None of them

### PHARM-F-081
tier: claimed
form: mcq
type: single
claimed: e
models: [3]
Which of the following statements is FALSE?
a) Cephalosporin's inhibit the transpeptidation (cross-linking) step in cell
   wall synthesis
b) Ciprofloxacin inhibits DNA gyrase activity in bacterial cells
c) Azithromycin binds to the 50S ribosomal subunit and inhibits the
   translocation step
d) Chloramphenicol binds to the 50S ribosomal subunit and inhibits the
   activity of peptidyl transferase
e) Tetracyclines inhibit the activity of bacterial peptidoglycan synthetase

### PHARM-F-082
tier: claimed
form: mcq
type: single
claimed: c
models: [2, 3]
Two drugs may act on the same tissue or organ through independent receptors,
resulting in effects in opposite directions. This is known as?
a) Chemical antagonism
b) Irreversible antagonism
c) Physiological antagonism
d) Competitive antagonism
e) Inverse agonist

### PHARM-F-083
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3, 5]
note: Header badge for this question wasn't captured (page-crop boundary);
  content is otherwise complete and unambiguous. Also seen in model 2 (same
  claim).
Which of the following inhibit folate metabolism?
a) Ampicillin
b) Trimethoprim
c) Tetracyclines
d) Erythromycin
e) Cephalosporin

### PHARM-F-084
tier: claimed
form: mcq
type: single
claimed: c
models: [3]
What type of side effect is most commonly observed in beta-lactam
antibiotics?
a) Aplastic anaemia
b) Hearing loss
c) Allergic reaction
d) Yellowing of teeth
e) All of them

### PHARM-F-085
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3, 4, 5]
Amoxycillin is similar to Ampicillin in different respects except in its?
a) Penicillinase resistance
b) Oral absorption
c) Hypersensitivity reaction
d) Antibacterial spectrum

### PHARM-F-086
tier: claimed
form: mcq
type: single
claimed: b
models: [3, 5]
Patients with penicillin allergy can use azithromycin for otitis media even
though azithromycin has great potential for drug-drug interactions?
a) True
b) False

### PHARM-F-087
tier: claimed
form: mcq
type: single
claimed: b
models: [3, 4]
Pseudomembranous colitis is caused by which organism?
a) Heliobacter pylori
b) Clostridium difficile
c) Staphylococcus aureus
d) Bacteroides fragilis

### PHARM-F-088
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
For bioequivalence tests, Cmax is a relevant measure to assess whether test
and reference formulation have the same rate of absorption?
a) False
b) True

### PHARM-F-089
tier: claimed
form: mcq
type: single
claimed: e
models: [3]
A 62-year-old man recently was admitted to the hospital for colectomy
surgery. Which of the following drugs would be appropriate to be included in
the oral prophylactic treatment of this patient to prevent surgical
infection?
a) Trimethoprim
b) Penicillin G
c) Streptomycin
d) Vancomycin
e) Neomycin

### PHARM-F-090
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3, 4, 6]
note: Model 6 carries this stem/options reshuffled, unanswered. Possibly
  related to PHARM-F-067 (2020-2021 sitting, same stem) which carries a
  smaller, differently-worded 4-option set (no "Carbenicillin", no "None of
  them") -- not merged since the option lists genuinely differ, not just
  reordered; kept as a separate entry per the same-stem-different-distractors
  precedent already used for PHARM-F-074.
Followings are the penicillinase-resistant penicillin, except?
a) Methicillin
b) Carbenicillin
c) None of them
d) Nafcillin
e) Cloxacillin

### PHARM-F-091
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 3, 4, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Which of the following antimicrobial agents is primary administered
topically?
a) Imipenem+Cilastain
b) Bacitracin
c) Meropenem
d) Penicillin-G

### PHARM-F-092
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 3, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
The following adverse effects are matched with corresponding drug except?
a) Fluroquinolones / QT prolonation
b) Tetracycline / photosensitivity
c) Vancomycin / red man syndrome
d) Sulfonamide / gray baby syndrome
e) Systemic polymyxins / nephrotoxicity and neurotoxicity

### PHARM-F-093
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3]
All of the following statements concerning penicillins are accurate EXCEPT?
a) Nafcillin is resistant to beta-lactamase
b) Probenecid increases penicillin excretion by blocking renal tubular
   reabsorption
c) Patients allergic to one penicillin are allergic to all penicillin's
d) Oral bioavailability of penicillin G is poor
e) Ampicillin achieves high concentration in bile

### PHARM-F-094
tier: claimed
form: mcq
type: single
claimed: a
models: [3, 4]
The time to reach steady state after a constant rate infusion is affected by
the ke of the drug?
a) True
b) False

### PHARM-F-095
tier: claimed
form: mcq
type: single
claimed: c
models: [3, 5]
Which of the following antibiotics is INAPPROPRIATRELY matched with a
clinical indication?
a) Clindamycin - osteomyelitis caused by staphylococcus
b) Ciprofloxacin - urinary tract infection caused by Pseudomonas aearuginosa
c) Ceftriaxone - enterococcal endocarditis
d) Vancomycin - pseudomembranous enterocolitis caused by Clostridium
   difficile

### PHARM-F-096
tier: claimed
form: mcq
type: single
claimed: b
models: [3, 4]
A 46-year-old woman recently diagnosed with UTI treatment with combined
trimethoprim-sulfamethoxazole. Which of the following best explains the main
reason for combining these two drugs?
a) To decreased the risk of allergic reactions
b) To obtain a bactericidal effect and give sequentially effect
c) To increase patient compliance by administered a single preparation
d) To achieve longer duration of action of sulfamethoxazole
e) To related the biotransforming of both drugs

### PHARM-F-097
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 3, 4, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Which of the following antibiotic combinations is inappropriate based on
antagonism at the same site of action?
a) Tigecycline and Azithromycin
b) Clindamycin and erythromycin
c) Doxycycline and Amoxicillin
d) None of them
e) Ciprofloxacin and Amoxicillin

### PHARM-F-098
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 3, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Children younger than 8 years of age should not receive tetracycline's
because these agents?
a) Cause rupture of tendons
b) All of them
c) Do not cross into the CSF
d) Can cause aplastic anemia
e) Deposit in teeth causes permanent discoloration

### PHARM-F-099
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2, 3, 4, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Which Among of the Following Antibiotics Act as Folate Antagonist?
a) Cefotaxime
b) ciprofloxacin
c) Tetracycline
d) Penicillin
e) None of them

### PHARM-F-100
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2, 3, 4, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
In the treatment of a urinary tract infection in a patient known to have a
deficiency of glucose-6-phosphate dehydrogenase, it would not be advisable to
prescribe which of the following?
a) Sulfonamide
b) Vancomycin
c) Cephalexin
d) Erythromycin
e) Amoxicillin

### PHARM-F-101
tier: claimed
form: mcq
type: single
claimed: b
models: [3, 5]
Which of the following antifungal agents is most likely to cause renal
insufficiency?
a) Itraconazole
b) Amphotericin B
c) Posaconazole
d) Fluconazole
e) All of them

### PHARM-F-102
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3, 5]
The time it takes to reach peak plasma concentrations (Tmax) is independent
of the dose and the oral bioavailability?
a) True
b) False

### PHARM-F-103
tier: claimed
form: mcq
type: single
claimed: a
models: [2, 3, 4]
What is the mechanism of action of Chloramphenicol?
a) Protein synthesis inhibitor
b) DNA synthesis inhibition
c) Bacterial cell wall synthesis inhibitor
d) None of them

### PHARM-F-104
tier: claimed
form: mcq
type: single
claimed: d
models: [3, 4]
This drug has the broadest antifungal spectrum but is used only in case of
severe mycoses because of its toxicity?
a) Fluconazole
b) Flucytosine
c) Caspofungin
d) Amphotericin B
e) Griseofulvin

### PHARM-F-105
tier: claimed
form: mcq
type: single
claimed: b
models: [2, 3, 4]
Clindamycin has the following except?
a) Active against anaerobes
b) Active against most gram-negative organisms
c) Associated with diarrhea
d) None of them
e) Active against some gram-positive organism

### PHARM-F-106
tier: claimed
form: mcq
type: single
claimed: d
models: [3]
A 24-year-old man recently diagnosed with severe acne started a treatment
that included tetracycline which of the following best explains the outcome
of the interaction between tetracycline and dairy products?
a) Increased drug elimination
b) Decreased drug binding to bacterial ribosome
c) Decreased bacterial permeability to the drug
d) Decreased drug oral Bioavailability
e) Increase drug toxicity

### PHARM-F-107
tier: claimed
form: qa
disputed: true
models: [1, 2, 3, 4, 5, 6]
claims:
  - source: model 3 (2023-2024 sitting)
    answer: extended-spectrum penicillin
  - source: models 1, 2, and 4 (agree)
    answer: antistaphylococcal penicillin
note: Model 6 carries the same 5-pair matching question, marked "Not yet
  answered" -- its dropdowns show text by default even when unanswered (a
  Moodle display quirk for this question type, confirmed by the "Not yet
  answered" badge itself), so it isn't a competing claim. Models 1, 2, and 4
  independently agree with each other against model 3's claim here.
oxacillin (matching, item 1 of 5)

### PHARM-F-108
tier: claimed
form: qa
claimed: second-generation cephalosporin's
models: [1, 2, 3, 4, 5, 6]
cefuroxime (matching, item 2 of 5)

### PHARM-F-109
tier: claimed
form: qa
claimed: carbapenems
models: [1, 2, 3, 4, 5, 6]
imipenem (matching, item 3 of 5)

### PHARM-F-110
tier: claimed
form: qa
claimed: third-generation cephalosporin
models: [1, 2, 3, 4, 5, 6]
ceftriaxone (matching, item 4 of 5)

### PHARM-F-111
tier: claimed
form: qa
claimed: first-generation cephalosporin
models: [1, 2, 3, 4, 5, 6]
cefazolin (matching, item 5 of 5)

### PHARM-F-112
tier: claimed
form: qa
claimed: Sulfasalazine
models: [3, 5]
A Sulfonamide used for treatment of ulcerative colitis (EMQ, part 1 of 8)

### PHARM-F-113
tier: claimed
form: qa
claimed: Cloxacillin
models: [3, 5]
A penicillinase-resistance penicillin (EMQ, part 2 of 8)

### PHARM-F-114
tier: claimed
form: qa
claimed: Tetracyclines
models: [3, 5]
A protein synthesis inhibitor that cannot be taken with antacids, minerals,
or dairy products because they will bind with each other and not be absorbed
(EMQ, part 3 of 8)

### PHARM-F-115
tier: claimed
form: qa
claimed: Amphoteracin-B
models: [3, 5]
Polyene Anti-fungal agent forms micropore in cell membrane, it has renal
toxicity and hypokalemia (EMQ, part 4 of 8)

### PHARM-F-116
tier: claimed
form: qa
claimed: Cefepime
models: [3, 5]
Fourth-generation cephalosporin active Pseudomonas aeruginosa (EMQ, part 5 of
8)

### PHARM-F-117
tier: claimed
form: qa
claimed: Vancomycin
models: [3, 5]
It used as orally route for clostridium difficile infection and its t1/2 may
reach to 200 hour in renal failure (EMQ, part 6 of 8)

### PHARM-F-118
tier: claimed
form: qa
claimed: Ciprofloxacin
models: [3, 5]
A fluoroquinolone inhibits bacterial topoisomerase II and active against
Gram-negative Pseudomonas aeruginosa (EMQ, part 7 of 8)

### PHARM-F-119
tier: claimed
form: qa
claimed: Moxifloxacin
models: [3, 5]
A fluoroquinolone has very poor activity against Pseudomonas aeruginosa, not
concentrate in urine and not indicated for the treatment of UTIs (EMQ, part 8
of 8)

### PHARM-F-120
tier: claimed
form: mcq
type: single
claimed: d
models: [3]
An 80-year-old woman presents with 2 days of fever and purulent wound
drainage showing gram-positive cocci in chains. She is 5 days post-colostomy
for a diverticular abscess. Select the most appropriate antibiotic regimen?
a) Penicillin
b) Tobramycin
c) Vancomycin plus gentamicin
d) Ampicillin plus gentamicin
e) Ticarcillin

### PHARM-F-121
tier: claimed
form: mcq
type: single
disputed: true
models: [1, 2, 3, 4, 6]
claims:
  - source: model 3 (2023-2024 sitting)
    answer: False
  - source: model 4 (2023-2024 sitting)
    answer: True
note: Model 6 also carries this stem/options reshuffled, unanswered. Was a
  clean reinforced claim (False) through model 3; model 4 claims the opposite
  for the same stem, so this is now a genuine conflict rather than a single
  claim.
The terminal slope of the concentration time profile is always reflective of
the elimination rate constant ke?
a) True
b) False

### PHARM-F-122
tier: claimed
form: mcq
type: single
claimed: c
models: [2, 3, 4]
Clavulanic acid is important because it?
a) Is a potent inhibitor of cell-wall
b) Easily penetrates Gram-negative bacteria
c) Inactivates bacterial B-lactemases
d) All of them
e) Is specific for Gram-positive bacteria

### PHARM-F-123
tier: claimed
form: mcq
type: single
claimed: e
models: [3, 5]
A 32-year-old woman presents to her gynecologist with a 4 days history of
smelly vaginal discharge. The only medication the woman is taking is an oral
contraceptive. A wet preparation of vaginal secretion shows budding yeast
cells. Which of the following drugs, given locally, would be appropriate for
this patient?
a) Metronidazole
b) Griseofulvin
c) Saquinavir
d) Zidovudine
e) Miconazole

### PHARM-F-124
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2, 3, 4, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
What is a common feature among the following group of antibiotics like
Penicillin, Cephalosporins, Carbapenems, and Monobactams?
a) None of them can penetrate the central nervous system
b) All of them
c) They all bind penicillin-binding protein-1 and inhibit their
   transpeptidase activity
d) They all have a β-lactam ring as a part of their biological interaction
e) All of them are eliminated mainly via biliary secretion

### PHARM-F-125
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 3, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
All of the following factors influence the penetration and concentration of
an antibacterial agent in the CSF except?
a) Protein binding of the drug
b) Minimum inhibitory concentration of the drug
c) Lipid solubility of the drug
d) Molecular weight of the drug
e) All of them

### PHARM-F-126
tier: claimed
form: mcq
type: single
claimed: a
models: [3, 4]
Parenteral route administration?
a) Usually produces a more rapid response than oral administration
b) Is too slow for emergency use
c) Cannot be used with unconsciousness patients
d) All of them
e) Generally results in a less accurate dosage than oral administration

### PHARM-F-127
tier: claimed
form: mcq
type: single
claimed: a
models: [2, 3, 5]
The primary mechanism of antibacterial action of the penicillin's involves
inhibition of?
a) Peptidoglycan cross-linking
b) N-acetylmuramic acid synthesis
c) Cell membrane synthesis
d) Beta-Lactmases
e) Transglycosylation

### PHARM-F-128
tier: claimed
form: mcq
type: single
claimed: d
models: [2, 3, 4]
What is meant by antibiotic resistance?
a) None of them
b) Both our bodies and the bacteria
c) It means our body has become resistant to the antibiotic
d) It means the bacteria have developed antibiotic resistance

### PHARM-F-129
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 3, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Which of the following group of antibiotics show bacteriostatic action?
a) Fluoroquinolones
b) Aminoglycosides
c) Macrolides
d) All of them
e) Monobactams

### PHARM-F-130
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 3, 5, 6]
note: Model 6 carries this stem/options reshuffled, unanswered.
Cilastatin is given along with Imipenem for the following reason?
a) Decreasing hydrolysis of Imipenem
b) None of them
c) Inhibition of renal tubular dipeptidase thus preventing hydrolysis of
   Imipenem by renal tubular dipeptidase
d) Blocking of bacterial transpeptidase and preventing degradation of
   Imipenem
e) Inhibition of beta-lactamases thus preventing inactivation of Imipenem

### PHARM-F-131
tier: claimed
form: mcq
type: single
disputed: true
models: [1, 3, 4, 6]
claims:
  - source: model 3 (2023-2024 sitting)
    answer: d (Hemolytic anemia)
  - source: model 4 (2023-2024 sitting)
    answer: a (All of them)
note: Models 1/6 carry this stem/options reshuffled, unanswered. Was a clean
  single claim (Hemolytic anemia) through model 3; model 4 claims a different
  answer for the same stem, so this is now a genuine conflict.
Which adverse effect is appeared with sulfonamides?
a) All of them
b) Skin rash
c) Kernicterus in the newborn
d) Hemolytic anemia
e) Crystalluria and nephrotoxicity

### PHARM-F-132
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2, 4, 6]
note: Open in models 1/6; filled in by models 2 and 4 (agree).
A 63-year-old male presents from a nursing home with fever, increased urinary
frequency and urgency. He has a penicillin allergy of anaphylaxis. Which of
the following B-lactams is the most appropriate choice for gram-negative
coverage of this patient's urinary tract infection?
a) Ertapenem
b) Ceftriaxone
c) Cefepim
d) None of them
e) Aztreonam

### PHARM-F-133
tier: open
form: mcq
type: single
models: [1, 6]
Which of the following statements about beta-lactam antibiotics is false?
a) Ceftriaxone is eliminated mainly via biliary secretion
b) Ticarcillin has activity against several gram negative rods
c) Renal tubular reabsorption of pencillin-G is inhibited by probencid
d) Cephalexin is first generation cephalosporines do not cross the blood
   brain barrier
e) Instability of penicillins in gastric acid can limit their oral absorption

### PHARM-F-134
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4, 5, 6]
note: Open in models 1/6; filled in by model 4 and reinforced by model 5
  (whose radio showed filled despite the page's own "Not yet answered" badge
  -- see the batch 05 header comment). Thematically close to PHARM-F-069
  (2020-2021 sitting, "Ototoxicity, nephrotoxicity, and muscle paralysis" / 4
  options) but not the same question -- different third symptom listed
  (vestibulo-toxic impairment vs. muscle paralysis) and a different, larger
  option set. Kept separate rather than merged.
Ototoxicity, vestibulo-toxic impairment, and nephrotoxicity are seen as major
adverse effects of?
a) Macrolides
b) Meropenem
c) Fluoroquinolones
d) Aminoglycosides
e) All of them

### PHARM-F-135
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
Azithromycin is very convenient for the patient because it is administered
once daily?
a) True
b) False

### PHARM-F-136
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
Through drug metabolism, conjugation is?
a) Coupling of a drug with an endogenous substrate
b) Solubilization in lipids
c) Process of drug reduction by special enzymes
d) Process of drug oxidation by special oxidases
e) All of them

### PHARM-F-137
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 6]
note: Open in models 1/6; filled in by model 2.
Cytochrome P-450 inhibition results in drug-drug interaction potential, a
classic example of strong cytochrome P-450 inhibitor is fluconazole?
a) False
b) True

### PHARM-F-138
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4, 5, 6]
note: Open in models 1/6; filled in by model 4.
Patient needs antibiotic treatment for native valve, culture positive
infective enterococcal endocarditis. His medical history includes sever
anaphylactic reaction to Penicillin G during the last year. The best approach
would be treatment with?
a) Amoxicillin-Clavunate
b) Ceftriaxone
c) Ticarcillin
d) Vancomycin
e) Aztreonam

### PHARM-F-139
tier: open
form: mcq
type: single
models: [1, 5, 6]
What is the characteristic of the intramuscular route of drug
administration?
a) All of them
b) Oily solutions can be injected
c) The action develops slower, than at oral administration
d) Only water solutions can be injected
e) Opportunity of hyperonic solution injections

### PHARM-F-140
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2, 5, 6]
note: Open in models 1/6; filled in by model 2.
Regarding toxicity of antibiotics, The correct statement is?
a) Enamel dysplasia is common with aminoglycosides
b) Disulfiram like reaction can occur with macrolides
c) Gray baby syndrome occurs with rifampicin use
d) Haemolytic anaemias can occur with sulphonamide use
e) Nephritis is the most common adverse reaction with ceftriaxone

### PHARM-F-141
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
An 18-year-old woman presents with urinary frequency, dysuria, and low-grade
fever. Urinalysis shows pyuria and bacilli. Select the most appropriate
treatment?
a) Claithromycin
b) Penicillin G
c) Metronidazole
d) Penicillin G plus tetracycline
e) Sulfamethoxazole plus trimethoprim

### PHARM-F-142
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
A patient has been prescribed Ciprofloxacin. Which of the following is an
important patient teaching for this drug?
a) Take this medication on an empty stomach
b) Protect yourself from sunlight while on this medication
c) Your skin may turn a orangish color while on this medicaion
d) This medication may stain your teeth, rinse with a hydrogen peroxide
   solution to prevent this

### PHARM-F-143
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2, 5, 6]
note: Open in models 1/6; filled in by model 2 and reinforced by model 5
  (whose radio showed filled despite the page's own "Not yet answered" badge
  -- see the batch 05 header comment).
Which of the following drugs would be selected to treat a newborn infant
with bacterial meningitis of unknown etiology?
a) Tetracycline
b) Chloramphenicol
c) Aztreonam
d) Ciprofloxacin
e) Ceftriaxone

### PHARM-F-144
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 2, 5, 6]
note: Open in models 1/6; filled in by model 2.
Your patient has MRSA. You have an order to administer vancomyocin, 1G IV q
12h. You remember that this medication can cause a rash on the face, neck,
and trunk. What intervention would be the BEST to prevent this side effect?
a) Infuse the vancomycin very slowly
b) Obtain an order for an antihistamine and administer concurrently
c) Ask for the order to be changed to an IM injection
d) Obtain an order for PO administration

### PHARM-F-145
tier: open
form: mcq
type: single
models: [1, 6]
A 58-year-old male with a history of hepatitis C, cirrhosis, and ascites
presents with spontaneous bacterial peritonitis. Which of the following
antibiotics requires close monitoring and dosing adjustment in this patient
given his liver disease?
a) All of them
b) Vancomycin
c) Penicillin G.
d) Erythromycin.
e) Tobramycin.

### PHARM-F-146
tier: claimed
form: mcq
type: single
claimed: c
models: [1, 2, 6]
note: Open in models 1/6; filled in by model 2.
Bioavailability is?
a) Amount of a substance obtained orally and quantity of intakes
b) Safety of drug
c) Extent of absorption and hepatic first-pass effect
d) Rheological parameters of blood
e) Glomerular filtration rate

### PHARM-F-147
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
Which of the following antifungal agents could be used during pregnancy?
a) Fluconazole
b) Griseofulvin
c) None of them
d) Amphotericin B and Griseofulvin
e) Amphotericin B

### PHARM-F-148
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2, 6]
note: Open in models 1/6; filled in by model 2.
Which of the following antifungal drugs act by inhibiting ergosterol
synthesis?
a) Terbinafine
b) Amphotericin B
c) Amphotericin B and Fluconazole
d) Fluconazole
e) Fluconazole and Terbinafine

### PHARM-F-149
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 4, 5, 6]
note: Open in models 1/6; filled in by model 4.
A patient is being discharged from the hospital on a 3-week course of
clindamycin. Which of the following potential adverse effects should be
discussed with her?
a) Hyperbilirubinemia
b) Clostridium difficile diarrhea
c) Bone marrow suppression
d) Nephrotoxicity

### PHARM-F-150
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4.
The correct statement concerning Chloramphenicol is?
a) Can cause discoloration of developing teeth when given to children
b) Does not penetrate the blood brain barrier
c) Must be administered parenterally only
d) Can cause suppression of bone marrow function
e) Can be safely used in premature infants

### PHARM-F-151
status: merged
note: Duplicate of PHARM-F-020 -- same stem ("...fluoroquinolones is LEAST
  accurate?"), same 4 options (2 swapped in order), same source (model 1/6).
  Discovered while cross-matching model 2 against the full file. ID retired
  rather than reused or renumbered; see PHARM-F-020 for the live entry
  (claim, models list, and full note).

### PHARM-F-152
tier: open
form: mcq
type: single
models: [1, 5, 6]
For bioequivalence tests, AUC is a relevant measure to assess whether test
and reference formulation have the same rate of absorption?
a) False
b) True

### PHARM-F-153
tier: claimed
form: mcq
type: single
claimed: a
models: [1, 5, 6]
note: Open in models 1/6; filled in by model 5, whose radio showed filled
  despite the page's own "Not yet answered" badge -- see the batch 05 header
  comment.
A 22-year-old female patient, has a severe penicillin allergy, is diagnosed
with community acquired pneumonia (caused by S. pneumonia), which of the
following would be the appropriate treatment for this patient?
a) Moxifloxacin
b) Ciprofloxacin
c) Trimethoprim
d) Ampicillin

### PHARM-F-154
tier: claimed
form: mcq
type: single
claimed: d
models: [1, 2, 5, 6]
note: Open in models 1/6; filled in by model 2.
Regarding the mechanism of action of aminoglycosides, the drugs?
a) Are bacteriostatic
b) Inhibit peptidyltransferase
c) Bind to the 50S ribosomal subunit
d) Bind to the 30S subunit interfere with cause misreading of mRNA

### PHARM-F-155
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 6]
note: Open in models 1/6; filled in by model 2.
Which of the following statements best explains the mechanism of antifungal
action of azoles?
a) Inhibition of squalene synthesis
b) Inhibition of conversion of lanosterol to ergosterol
c) Inhibition of fungal mitosis
d) Inhibition of conversion of squalene to lanosterol
e) Formation of artificial pores in the fungal membrane

### PHARM-F-156
tier: open
form: mcq
type: single
models: [1, 5, 6]
Which statement about vancomycin is accurate?
a) All of them
b) Binds to PBPs
c) Bacteriostatic
d) High orally Bioavailability
e) Active against MRSA

### PHARM-F-157
tier: claimed
form: mcq
type: single
claimed: e
models: [1, 2, 5, 6]
note: Open in models 1/6; filled in by model 2.
Clarithromycin and erythromycin have very similar spectra of antimicrobial
activity. The major advantage of clarithromycin is that it?
a) Eradicates mycoplasmal infections in a single dose
b) Does not inhibit hepatic drug-metabolizing enzymes
c) Is active against MRSA
d) Is active against strains of streptococci that are resistant to
   erythromycin
e) Has greater activity against H-pylori

### PHARM-F-158
tier: claimed
form: qa
claimed: Penicillin V
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4, which carries this same
  8-item EMQ answered (models 1/6's copy is entirely unanswered).
Natural penicillin's has more acid stable and it's route of administration
orally (EMQ, part 1 of 8)

### PHARM-F-159
tier: claimed
form: qa
claimed: Chloramphenicol
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
Broad spectrum and bacteriostatic antibiotic has dose-dependent bone marrow
suppression and aplastic anemia by a non-dose related (EMQ, part 2 of 8)

### PHARM-F-160
tier: claimed
form: qa
claimed: Linezolid
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
Bacteriostatic antibiotic has activity against MRSA, VRE and excellent (100%)
oral Bioavailability (EMQ, part 3 of 8)

### PHARM-F-161
tier: claimed
form: qa
claimed: Cefuroxime sodium
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
Second generation cephalosporin antibiotic crosses the BPB and used for
community acquired pneumonia as parentally (EMQ, part 4 of 8)

### PHARM-F-162
tier: claimed
form: qa
claimed: Ceftazidime
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
Third generation cephalosporin antibiotic is active against Pseudomonas
aeruginosa (EMQ, part 5 of 8)

### PHARM-F-163
tier: claimed
form: qa
claimed: Azithromycin
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
A macrolide antibiotic with a very long half-life (about 40 hours) (EMQ, part
6 of 8)

### PHARM-F-164
tier: claimed
form: qa
claimed: Neomycin
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
An aminoglycoside antibiotic used in hepatic encephalopathy or hepatic coma
(EMQ, part 7 of 8)

### PHARM-F-165
tier: claimed
form: qa
claimed: Doxycycline
models: [1, 4, 6]
note: Open in models 1/6; filled in by model 4 (see PHARM-F-158's note).
A tetracycline antibiotic glucuronide is excreted via bile and used in acne
vulgaris (EMQ, part 8 of 8)

### PHARM-F-166
tier: claimed
form: mcq
type: single
claimed: b
models: [1, 2, 4, 6]
note: Open in models 1/6; filled in by models 2 and 4 (agree).
To treat an upper respiratory infection due to Streptococcus pneumoniae in a
pregnant woman with a known history of penicillin allergy, all of the
following drugs are contraindicated EXCEPT?
a) Metronidazole
b) Azithromycin
c) Ciprofloxacin
d) Ampicillin
e) Tetracycline

### PHARM-F-167
tier: open
form: mcq
type: single
models: [1, 6]
There is only drug absorption until peak plasma concentrations are reached?
a) False
b) True

<!-- batch 03 -- raw/finals/2023-2024/Medicine/1.pdf + 2.pdf (RUN-PLAN row 16),
  51 vision pages, 25 + 26. Models 1 and 2 of the 2023-2024 Medicine sitting's
  reshuffle. 1.pdf turned out to be a duplicate capture of the same attempt as
  batch 02's "model 6" (6.pdf) -- confirmed independently by both this session
  and the one that ran batch 02, word-for-word identical stems AND option
  order throughout, entirely "Not yet answered" in both. Not re-extracted as
  new content; every models:[6] / models:[3, 6] field in the file above was
  corrected to include "1" instead (a mechanical, content-preserving fix, done
  by the batch 02 session once the finding was confirmed). 2.pdf (model 2) is
  a live, mostly-answered attempt and is genuinely new -- cross-matched by
  stem against the ENTIRE file above (both the 2020-2021 sitting and the
  2023-2024 sitting's models 1/3/6), not just against itself.

  Of model 2's 49 numbered questions, Q21 never appears anywhere across all 26
  pages -- a genuine capture gap, not a read failure (same pattern as batch
  02's own numbering gaps). Of the 48 captured: 33 matched an existing stem
  (23 against model 1/6's content, 10 against model 3's) and were merged in
  place -- filling a `tier: open` entry with model 2's claim, reinforcing an
  existing claim, or (twice) adding a new value to an already-disputed entry
  -- rather than re-minted; 15 were genuinely new (PHARM-F-168 onward below).

  Two data-quality issues surfaced during this cross-match, both fixed in
  place rather than left for a later pass:
    - PHARM-F-151 was an exact duplicate of PHARM-F-020 (same stem, same 4
      options, 2 merely reordered) -- a dedup slip from batch 02's own
      extraction. Retired with a one-line tombstone rather than deleted or
      renumbered.
    - PHARM-F-107 (oxacillin's item in the 5-drug matching question) claimed
      "extended-spectrum penicillin" from model 3 alone; both model 1 and
      model 2 independently show "antistaphylococcal penicillin" for the same
      item. Two independent captures disagreeing with one is a genuine
      dispute, not a tie-break -- converted to disputed: true.

  PHARM-F-037's already-disputed folate-antagonist question gained a THIRD
  distinct claim value from model 2 ("Cotrimoxazole", matching neither of the
  two existing claims). PHARM-F-059 (β-lactamase resistance mechanism) gained
  model 2 as a second source agreeing with model 3's "Drug inactivation"
  claim against the original 2020-2021 "Efflux pump" claim -- doesn't change
  the dispute, just its weight.

  PHARM-F-174 (below) is a near-miss with PHARM-F-073 (2020-2021 sitting) --
  same theme (drug-class-to-mechanism matching) and similar options, but
  "cell wall synthesis" vs "cell membrane synthesis" for penicillin and a
  different claimed answer, not just reshuffled -- kept separate per the same
  precedent as PHARM-F-074/090.

  Zero questions in this batch depend on a photo/graph -- pure text MCQs
  throughout, no matching or EMQ items in model 2's new content -- so no img:
  crops were needed. -->

### PHARM-F-168
tier: claimed
form: mcq
type: single
claimed: c
models: [2]
Which of the following statements about trimethoprim-sulfamethoxazole
(cotrimoxazole) is FALSE?
a) Is indicated for treatment of infections of the urinary tract
b) The combination provides synergistic antibacterial effect because of
   sequential blockade of the synthesis of folic acid and tetrahydrofolate
c) Major toxic side effects include cholestatic hepatitis
d) Hemolytic anemia can occur in patients with genetic deficiency of
   glucose-6-phosphate dehydrogenase in red blood cells
e) It is effectively used in the treatment of pneumocystis pneumonia

### PHARM-F-169
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
For bioequivalence tests, Cmax differs between test and reference formulation
if both deliver different doses (assume same rate of absorption for both
formulations)?
a) True
b) False

### PHARM-F-170
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
For bioequivalence tests, AUC is a relevant measure to assess whether test
and reference formulation deliver the same dose?
a) False
b) True

### PHARM-F-171
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
The mechanism of action of this drug involves the inhibition of the
synthesis of B-glucan, an essential constituent of a fungal cell wall?
a) Amphotericin B
b) Fluconazole
c) Flucytosine
d) Caspofungin
e) Griseofulvin

### PHARM-F-172
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
You have a patient with rheumatoid arthritis who takes aspirin, 1.25g q 6h.
She is hospitalized with E. Coli sepsis. Maxiumum doses of gentamicin have
been ordered. Based on this information, what intervention would be a
PRIORITY?
a) Check liver function tests
b) Monitor for skin rashes (Stevens Johnson syndrome)
c) Monitor electrolyte levels
d) Obtain a hearing evaluation

### PHARM-F-173
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
Which of the following statements is true about drug binding to plasma
proteins?
a) Bound drug is pharmacologically inactive.
b) None of them
c) Binding is an irreversible process.
d) Drug-protein complex is effectively excreted in urine.

### PHARM-F-174
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
note: Near-miss with PHARM-F-073 (2020-2021 sitting) -- same theme
  (drug-class to mechanism matching) but "cell wall synthesis" throughout
  here vs "cell membrane synthesis" for penicillin there, and a different
  claimed answer (Penicillin here vs Fluoroquinolones there). Not merged;
  the option sets genuinely differ, not just reshuffled.
Which of the following combinations is correct?
a) Aminoglycoside: inhibition of cell wall synthesis
b) Fluoroquinolones: inhibition of cell wall synthesis
c) All of them
d) Penicillin: inhibition of cell wall synthesis
e) Cephalosporin: inhibition of protein synthesis

### PHARM-F-175
tier: claimed
form: mcq
type: single
claimed: c
models: [2]
Which of the following is not a type of β-lactam antimicrobial?
a) Aztreonam
b) Penicillins
c) Glycopeptides
d) Cephalosporins
e) Monobactams

### PHARM-F-176
tier: claimed
form: mcq
type: single
claimed: c
models: [2]
Which of the following adverse drug reactions precludes a patient from being
re-challenged with that drug in the future?
a) Iching/rash from Penicillin
b) Clostridium difficile superinfection from Moxifloxacin
c) Stevens-Johnson syndrome from sulfamethoxazole +Trimethoprim
d) Gastrointestinal (GI) upset from Clarithromycin
e) All of them

### PHARM-F-177
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
All of the following antibiotics are effectively used as antimicrobial
agents after oral administration EXCEPT?
a) Azithromycin
b) Amikacin
c) Cefaclor
d) Amoxicillin
e) Cephalexin

### PHARM-F-178
tier: claimed
form: mcq
type: single
claimed: a
models: [2]
Clearance (CL) is related with?
a) Volume of distribution, half life and elimination rate constant
b) Only the concentration of drugs in the body
c) Only the elimination rate constant (Ke)
d) None of them
e) Bioavailability and half life

### PHARM-F-179
tier: claimed
form: mcq
type: single
claimed: d
models: [2]
A 45-year-old man hospitalized for staphylococcal endocarditis developed
hypotension, tachycardia, generalized pruritus, and facial flushing 15
minutes after receiving an intravenous injection of an antibiotic. Which of
the following drugs most likely caused the patient's syndrome?
a) Imipenem
b) Ampicillin
c) Oxacillin
d) Vancomycin
e) Cefazolin

### PHARM-F-180
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
A patient develops a penicillin resistant Streptococcal skin infection for
which azithromycin (Zithromax) is ordered. Which of the following patient
teachings is appropriate for this drug?
a) Avoid taking iron with this drug
b) Take this medication on an empty stomach
c) Avoid taking vitamin C within 2-3 hours of this drug
d) Your stools may turn yellow or green while on this medication

### PHARM-F-181
tier: claimed
form: mcq
type: single
claimed: c
models: [2]
A 30 year-old male patient who is HIV-positive has a CD4 count of 300/μL.
His treatment involves a three-drug combination of zidovudine, lamivudine,
and indinavir. He develops severe dysphagia and an endoscopic examination
indicated esophogeal candidiasis. The treatment regimen for this patient
should also include which of the following drugs?
a) Foscarnet
b) Griseofulvin
c) Fluconzole
d) Flucytosine

### PHARM-F-182
tier: claimed
form: mcq
type: single
claimed: b
models: [2]
Cephalosporin efficacy is time dependent; as such, the patients can stop
taking the medications once they feel better?
a) True
b) False

<!-- batch 04 -- raw/finals/2023-2024/Medicine/4.pdf (RUN-PLAN row 18), 41
  vision pages, model 4 of the 6-model set (the longest single model). Plain
  Moodle student view, "Answer saved"/live-exam chrome throughout, so tier
  tops out at claimed. Captured non-monotonically -- the exam's own 5 Moodle
  "pages" (page 5 of 5 down to page 1 of 5) were screenshotted out of order
  and with heavy overlap, so questions were stitched by NUMBER across all 41
  pages rather than assumed sequential; every number 1-49 was eventually
  seen, no gaps this time (unlike batch 02's model 3, which had four genuine
  holes).

  Matched by stem against the entire existing file (2020-2021 sitting +
  2023-2024 models 1/2/3/6), same as batch 03: 37 of 49 questions matched
  existing entries -- 18 reinforced an existing claim unchanged, 15 supplied
  the first real claim to a previously-open model-1/6-only entry, 4 surfaced
  a genuine conflict with an existing claim. 12 were new (PHARM-F-183-194).
  One of the 37 matches was the full 8-item EMQ shared with models 1/6
  (PHARM-F-158-165) -- model 4 is the first source to actually answer it
  (models 1/6's copy is unanswered), so all 8 items went from open to
  claimed in one pass.

  Four genuine conflicts surfaced, each recorded as disputed: true rather
  than silently picking a side:
    - PHARM-F-059 (β-lactamase mechanism): model 4 reinforces the existing
      "Drug inactivation" side (now 3 sources: models 2, 3, 4) against the
      2020-2021 sitting's "Efflux pump" -- not a new conflict, just a
      stronger existing one.
    - PHARM-F-107 (oxacillin's class, matching question): model 4 reinforces
      models 1 and 2's "antistaphylococcal penicillin" against model 3's
      "extended-spectrum penicillin" -- same, a stronger existing side, not
      a new dispute.
    - PHARM-F-121 (terminal slope reflects ke, True/False): model 3 claimed
      False; model 4 claims True. Genuinely new conflict.
    - PHARM-F-131 (sulfonamide adverse effect): model 3 claimed "Hemolytic
      anemia"; model 4 claims "All of them." Genuinely new conflict.

  Two near-misses noted but not merged, same treatment as PHARM-F-074/090:
    - PHARM-F-186 (new): same stem as PHARM-F-073 (2020-2021 sitting,
      "Which of the following combinations is correct?") but a completely
      different, non-overlapping option/answer set.
    - PHARM-F-190 (new): thematically close to PHARM-F-088 (Cmax
      bioequivalence) but asks a different question (whether Cmax differs
      given different doses, not whether Cmax is a relevant measure at all).

  Zero questions in this batch depend on a photo/graph -- pure text MCQs and
  one EMQ throughout, so no img: crops were needed. -->

### PHARM-F-183
tier: claimed
form: mcq
type: single
claimed: e
models: [4]
If vancomycin and bacitracin both target the same step of peptidoglycan
synthesis, then why can't bacitracin be used as a drug of last resort
against systemic infections with multi-drug resistant pathogens?
a) They are similar and alternative to each other
b) Vancomycin kills all known bacteria, Bacitracin dosen't
c) Bacteria are resistant and Bacitracin has systemic toxicity
d) All bacteria are already resistant to bacitracin
e) Bacitracin has toxicity problems when used systemically

### PHARM-F-184
tier: claimed
form: mcq
type: single
claimed: d
models: [4, 5]
Supplementary folinic acid may prevent anemia in folate-deficient persons
who use this drug, it is a weak base achieving tissue levels similar to
those in plasma?
a) Linezolid
b) Ciprofloxacin
c) Levofloxacin
d) Trimethoprim
e) Sulfamethoxazole

### PHARM-F-185
tier: claimed
form: mcq
type: single
claimed: a
models: [4, 5]
Clindamycin is used in very specific infections osteomyelitis due to its
pattern of distribution?
a) True
b) False

### PHARM-F-186
tier: claimed
form: mcq
type: single
claimed: e
models: [4, 5]
note: Same stem as PHARM-F-073 (2020-2021 sitting, "Which of the following
  combinations is correct?") but a different, non-overlapping option set --
  F-073 pairs fluoroquinolones with DNA synthesis inhibition (claimed there);
  this one pairs fluoroquinolones with cell wall synthesis (wrong) and
  claims penicillin/cell wall synthesis instead. Kept separate per the same
  different-distractor-set precedent as PHARM-F-074.
Which of the following combination is correct?
a) All of them
b) Fluoroquinolones: inhibition of cell wall synthesis
c) Cephalosporin: inhibition of protein synthesis
d) Aminoglycoside: inhibition of cell wall synthesis
e) Penicillin: inhibition of cell wall synthesis

### PHARM-F-187
tier: claimed
form: mcq
type: single
claimed: e
models: [4, 5]
The appropriate treatment for pseudomembranous colitis that caused by
Clostridium difficile is administration of?
a) Tetracycline given IM
b) Ampicillin given PO
c) Augmentin given PO
d) Vancomycin given IV
e) Vancomycin given PO

### PHARM-F-188
tier: claimed
form: mcq
type: single
claimed: a
models: [4, 5]
If two formulations of the same drug are tested and product A has a greater
absorption rate than product B, product A will take a longer time to reach
peak concentrations (Tmax)?
a) False
b) True

### PHARM-F-189
tier: claimed
form: mcq
type: single
claimed: b
models: [4, 5]
note: Reinforced by model 5, whose radio showed filled despite the page's
  own "Not yet answered" badge -- see the batch 05 header comment.
The drug of choice for methicillin-resistant Staphylococcus aureus is?
a) gentamicin
b) vancomycin
c) piperacillin
d) oxacillin
e) None of them

### PHARM-F-190
tier: claimed
form: mcq
type: single
claimed: b
models: [4, 5]
note: Thematically close to PHARM-F-088 (2020-2021/model 3/6, "For
  bioequivalence tests, Cmax is a relevant measure...") but a different
  question -- this one asks about Cmax differing when the two formulations
  deliver different doses, not whether Cmax is a relevant measure at all.
  Kept separate.
For bioequivalence tests, Cmax differs between test and reference
formulation if both deliver different doses (assume same rate of absorption
for both formulations)?
a) False
b) True

### PHARM-F-191
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
A 30 year-old male patient who is HIV-positive has a CD4 count of 300/μl.
His treatment involves a three-drug combination of zidovudine, lamivudine,
and indinavir. He develops severe dysphagia and an endoscopic examination
indicated esophogeal candidiasis. The treatment regimen for this patient
should also include which of the following drugs?
a) Griseofulvin
b) Foscarnet
c) Flucytosine
d) Fluconzole

### PHARM-F-192
tier: claimed
form: mcq
type: single
claimed: e
models: [4]
Which of the following adverse drug reactions precludes a patient from being
re-challenged with that drug in the future?
a) All of them
b) Gastrointestinal (GI) upset from Clarithromycin
c) Clostridium difficile superinfection from Moxifloxacin
d) Iching/rash from Pencillin
e) Stevens-Johnson syndrome from sulfamethoxazole +Trimethoprim

### PHARM-F-193
tier: claimed
form: mcq
type: single
claimed: d
models: [4]
A patient develops a penicillin resistant Streptococcal skin infection for
which azithromyocin (Zithromax) is ordered. Which of the following patient
teachings is appropriate for this drug?
a) Avoid taking vitamin C within 2-3 hours of this drug
b) Avoid taking iron with this drug
c) Your stools may turn yellow or green while on this medication
d) Take this medication on an empty stomach

### PHARM-F-194
tier: claimed
form: mcq
type: single
claimed: a
models: [4, 5]
Cell-wall Biosynthesis is inhibited by Antibiotics by Inhibiting the
Biosynthesis of Which of the following?
a) None of them
b) All of them
c) Proteins
d) Cellulose
e) Lipopolysaccharide

<!-- batch 05 -- raw/finals/2023-2024/Medicine/5/ (RUN-PLAN row 19), 27 vision
  pages, a camera-roll photo set (not a PDF export) of model 5 of the 6-model
  set -- a distinct Moodle attempt (attempt=10096078, vs. the other models'
  attempt=1009548x range). Entirely "Not yet answered" through Q40, so tier
  stayed open and reinforced existing entries without adding claims for most
  of the batch. All 49 questions present (Q1-49, no gaps).

  Anomaly: starting at Q41 and continuing through Q46, the page's own badge
  still read "Not yet answered" but the question's radio button was visibly
  filled (a solid, unambiguous selection, not a rendering artifact -- checked
  across multiple questions and re-examined before trusting it). Q47-49
  reverted to genuinely empty radios. Read as: the student began clicking
  answers late in the attempt (timer visible, running low -- 0:23 remaining
  at Q41) faster than Moodle's "Answer saved" badge re-rendered in the
  screenshot, not as noise. Per job-a-extract.md's own rule ("when the page
  carries its own answer state -- a radio... that IS the record"), these six
  selections were recorded as claims: PHARM-F-037 (reinforces the existing
  Cotrimoxazole side), PHARM-F-203 (new), PHARM-F-143, PHARM-F-189,
  PHARM-F-153, PHARM-F-134 (reinforces existing claims/claimed one
  previously-open entry). Every affected entry's own note flags the
  discrepancy explicitly rather than silently treating a filled radio as a
  clean "Answer saved" claim.

  Zero questions in this batch depend on a photo/graph -- pure text MCQs, one
  EMQ, and one matching question (both already-known items, unanswered here)
  -- so no img: crops were needed. -->

### PHARM-F-195
tier: open
form: mcq
type: single
models: [5]
Which of the following statements about aminoglycosides is FALSE?
a) bind to the 30S ribosomal subunit and inhibit bacterial protein synthesis
b) have broad spectrum bactericidal properties against gram-negative bacteria
c) are effective against anaerobic organisms
d) are effectively used in combination with penicillins to treat
   enterococcal endocarditis
e) are not administered orally for treating systemic infections

### PHARM-F-196
tier: open
form: mcq
type: single
models: [5]
note: Same theme as PHARM-F-068 (2020-2021 sitting, "All of the followings
  are the adverse effects of tetracycline except") but a different,
  non-overlapping option set -- F-068 lists Crystal urea/Fatal
  hepatotoxicity/Phototoxicity/Bone malformation; this one lists None of
  them/Phototoxicity/Yellow discoloration of teeth/Ototoxicity/Fatal
  hepatotoxicity. Kept separate per the same different-distractor-set
  precedent as PHARM-F-074/090/186.
All of the followings are the adverse effects of tetracycline, except?
a) None of them
b) Phototoxicity
c) Yellow discoloration of teeth
d) Ototoxicity
e) Fatal hepatotoxicity

### PHARM-F-197
tier: open
form: mcq
type: single
models: [5]
Which one of the following drugs would be the BEST choice to treat oral
Candida in an otherwise healthy patient?
a) Nystatin
b) Amphotericin B
c) Acyclovir
d) Amantadine

### PHARM-F-198
tier: open
form: mcq
type: single
models: [5]
Clearance (CL) is related with?
a) Only the concentration of drugs in the body
b) Bioavailability and half life
c) Volume of distribution, half life and elimination rate constant
d) Only the elimination rate constant (Ke)
e) None of them

### PHARM-F-199
tier: open
form: mcq
type: single
models: [5]
Which of the Following Penicillin has Best Gram-Negative Spectrum?
a) Methicillin
b) Nafcillin
c) Ampicillin
d) None of them
e) Penicillin V

### PHARM-F-200
tier: open
form: mcq
type: single
models: [5]
Therapeutic index (TI) is?
a) A ratio used to evaluate the bioavailability of a drug
b) A ratio used to evaluate the elimination of a drug
c) A ratio used to evaluate the effectiveness of a drug
d) A ratio used to evaluate the safety and usefulness of a drug for
   indication

### PHARM-F-201
tier: open
form: mcq
type: single
models: [5]
Which of the following antibiotics is considered unsafe to use in neonates
except?
a) Chloramphenicol
b) Ciprofloxacin
c) Tetracycline
d) Penicillin G

### PHARM-F-202
tier: open
form: mcq
type: single
models: [5]
Random use of broad-spectrum antibiotics is contraindicated. This is because
they?
a) Can interfere with endogenous microbiota
b) Are extremely nephrotoxic
c) Can produce dependency and psychogenic symptoms
d) Can induce anaphylactic reactions
e) All of them

### PHARM-F-203
tier: claimed
form: mcq
type: single
claimed: d
models: [5]
note: Model 5's radio showed filled despite the page's own "Not yet
  answered" badge -- see the batch 05 header comment. The claim itself is
  pharmacologically self-consistent (caspofungin is the classic
  echinocandin/beta-glucan-synthase-inhibitor answer), which is corroborating
  but not the basis for recording it -- the radio state is.
The mechanism of action of this drug involves the inhibition of the
synthesis of B-glucan, an essential constituent of a fungal cell wall?
a) Amphotericin B
b) Flucytosine
c) Griseofulvin
d) Caspofungin
e) Fluconazole

### PHARM-F-204
tier: open
form: mcq
type: single
models: [5]
Metabolic transformation phase I is?
a) Glucoronidation
b) Transformation of substances due to oxidation, reduction, or hydrolysis
c) Binding to plasma proteins
d) Acetylation and methylation of substances
e) All of them
