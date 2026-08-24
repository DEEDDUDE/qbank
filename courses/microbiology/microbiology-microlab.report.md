# microbiology / microlab — 90 questions

verified 52 · conflict 2 · external 31 · not-in-source 3 · needs-eye 2

**Disputed entries, resolved first (as asked):**
- **MICRO-LAB-009** (EMB metallic green sheen) — answer **c** (E. coli). Originally
  `external` (margin claim, settled outside knowledge); now `verified` directly —
  see the Lab 6 patch below.
- **MICRO-LAB-010** (Klebsiella colony trait) — `external`, answer **b** (mucoid
  colonies). Checked specifically for a source hole here too (see below) — none
  found. Margin wins on settled outside knowledge.
- **MICRO-LAB-012** (S. viridans hemolysis) — `verified`, answer **b** (alpha).
  Actually resolvable: Lab 6 defines alpha hemolysis as "greenish/brownish," Ch.6
  independently calls viridans colonies green. Margin wins.
- **MICRO-LAB-067** (oil immersion purpose) — `verified`, answer **b**. Lab 1 states
  oil *reduces* refraction by matching refractive index; the other circled option
  has the mechanism backwards. 

Margin won all three inline-vs-margin disputes (009, 010, 012) — the third
independent data point supporting the "corrected key, not a second student" reading
from Job A's original note on that page.

**Conflicts (2)** — the circulating file is wrong on both:
- **MICRO-LAB-074** — claimed Blue for an acid-fast organism's stain color; the
  source states acid-fast organisms stain red (blue is explicitly the non-acid-fast
  color). Answer: **a** (Red).
- **MICRO-LAB-075** — claimed (b) as the false Gram-stain statement (a true
  statement about S. pyogenes); the source instead identifies (c) as false — it
  attributes Mycoplasma's Gram-invisibility to a "waxy coat," which is actually
  Mycobacterium's reason, not Mycoplasma's (Mycoplasma has no cell wall at all).
  Answer: **c**.

**Not-in-source (3)** — MICRO-LAB-039 (which stain/organism pairing is "incorrect" —
genuinely ambiguous, all four pairings are individually defensible), 079
(Burkholderia cepacia — not covered, and I'm not confident enough to call it
external), 082 (transport medium — source confirms the concept but not enough detail
to pick the false option among four).

**Needs your eyes (2)** — down from 6. Two remain, both carried from Job A and
genuinely unrecoverable: 022 (option physically obscured by a crease/correction
fluid) and 057 (the question stem itself missing from the capture, a real gap in
the source). The other four (038, 049, 059, 060) were a Job A bug, not a real gap
— see below.

**Job A bug found and fixed: images referenced but never saved.** Four questions
(038, 049, 059, 060) had an `img:` field that was a prose description
("(question shows a photo of...)") instead of an actual saved crop — the image
existed in the original capture but was never written to `flagged/`, so nothing
downstream could ever see it. Traced each back to its raw file (`نموذج 2` Dentistry
for 038; `Lab 2 + 3 quiz` نموذج 1 and نموذج 2 for 049/059/060) using the already-
cached Stage 0 renders from the original Job A session, and matched each to its
question by exact stem/option text. All four are now saved to `flagged/` and
resolved:
- **038** — a streaked-plate photo; visually consistent with a selective-and-
  differential medium, but resolved `external` rather than `verified` since there's
  no source photo to check it against.
- **049 and 059** — the same novobiocin-test question captured twice (نموذج 1 and
  نموذج 2). Both plates show no zone of inhibition at all — by Lab 8's own R/S
  definition that's resistant, confirming the claimed answer in both. `verified`.
- **060** — the H/X hemolysis-plate comparison. Plate X shows visibly more complete
  clearing around colonies than H, matching Lab 6's definition of beta hemolysis.
  `verified`, with a noted caveat that grayscale limits full certainty against a
  heavily-cleared alpha reaction.

Fixed the underlying rule in `job-a-extract.md`: `img:` must always be an actual
saved crop, on any question whose answer depends on a photo — not just `needs-eye`
ones. Job A never resolves answers, so it can't reliably predict in advance which
images will turn out to be load-bearing for verification; the old rule only
required a save for genuinely-unreadable content, which is exactly the gap that let
these four slip through unsaved for an entire session.

**Lab spine hole found and patched.** Checked whether the underlying slide decks
(specifically Rawan Ayyad's, and the already-partially-used `2024 Slides/Lab 1.pdf`)
cover organism traits like EMB appearance and Klebsiella colony morphology, per your
question. Answer: **yes for EMB, no for Klebsiella.** Lab 6's identification-algorithm
section (`2024 Slides/Lab 1.pdf` pp. 41–66) is almost entirely near-textless photo
slides with one-word titles ("Moraxella," "Novobiocin," etc.) — the original Job B
pass summarized these by topic label without transcribing what the photos actually
show. Two of them turned out to carry real facts: a labeled EMB photo (p. 17) showing
E. coli's metallic green sheen next to non-sheening Enterobacter cloacae, and a
Moraxella photo (p. 48) showing pinpoint colonies. Rendering the EMB photo needed a
color view, not grayscale — Stage 0's default grayscale is right for Job A exam
captures but would have erased the one thing that page exists to show, so `prep.py`'s
patch mode now takes a `--color` flag. Klebsiella, by contrast, isn't named anywhere
in the text layer of any of the four decks checked — no hole there, MICRO-LAB-010,
051, and 072 stay external. Patched into `source.lab.md` at {#lab06-3};
**MICRO-LAB-008, 009, and 037 flipped from external to verified** as a direct result
(009 being the disputed entry above). 048 and 052 (Moraxella's *aerobic* status, a
different fact than colony shape) were checked and correctly stay external — the
patched photo doesn't address oxygen requirement.

**External (31) — still the headline finding even after the patch and the image
recovery.** Roughly a third of this batch answers from settled outside knowledge
rather than the lab manual itself. The pattern is consistent: the manual is
thorough on *procedures and mechanisms* (media
classification, Gram stain steps, Kirby-Bauer theory, ELISA formats) but thin on the
specific *organism-identification trivia* these quiz questions actually test —
which pigment, which colony texture, which antibiotic a given genus is resistant to.
Every Lab 8 (antibiotic sensitivity) question that's covered is directly and
thoroughly supported (verified); nearly every Lab 6 (growth characteristics/ID)
question about a specific organism's distinguishing trait had to be answered
externally, since Lab 6's own worksheet asks students to *fill in* those
organism-trait pairings during the exercise rather than supplying them as text.

**Chapter load:** 8 lab chapters used, each loaded once, plus 3 lecture chapters
(Ch.2, Ch.4, Ch.6, Ch.10) for lab-index-silent facts, per the lab-first/
lecture-fallback rule. Lab 8 was heaviest (18 questions, all but 2 verified/external
split cleanly); Lab 6 second (about 25 questions, dominated by external answers per
the pattern above).

---

Full per-question resolutions: [microbiology-microlab.verify.md](microbiology-microlab.verify.md)
