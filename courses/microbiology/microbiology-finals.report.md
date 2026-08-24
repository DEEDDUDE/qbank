# microbiology / finals (نموذج 1 partial + نموذج ٥) — 58 questions

verified 50 · conflict 1 · external 7 · not-in-source 0 · needs-eye 0

**Conflicts** — the circulating file is wrong on this 1: **MICRO-F-050**. Claimed
Clostridium perfringens and Staphylococcus aureus as the ADP-ribosylating exotoxin
producers; the source supports Corynebacterium diphtheriae and Escherichia coli
instead — C. perfringens's toxin is a lecithinase, not ADP-ribosylating.

**Not in source** — none. Every question either matched a chapter or was answerable
as `external` (settled, standard fact the slides don't happen to cover).

**External (7)** — settled facts absent from the lecture spine: MICRO-F-005 (ID50
comparison), 012 (JC virus/PML — Ch.13 defines "slow virus infection" but doesn't name
it), 020 (rabies as zoonotic), 025 (handwashing/S. aureus), 028 (precipitation
definition), 034 (prion/spore/bacteria resistance ranking), 054 (food intoxication
timing).

**Ch.8 patched, re-verified — 3 of 6 flipped to verified.** Ch.8 had 8 pages logged
as image-only diagrams with no extractable caption text; re-read via `prep.py`'s new
patch mode, they turned out to be five dense reference tables, not uncaptioned
diagrams (only page 19, a "Typhoid Mary" illustration, and page 35, an unlabeled
micrograph, still add nothing new — see the patch note at {#ch08-5} in source.md).
**MICRO-F-026** (Chlamydia trachomatis, vertical transmission) and **MICRO-F-056**
(Legionella pneumophila, water-aerosol transmission) are directly confirmed by the
new tables. **MICRO-F-020** (rabies) and **MICRO-F-025** (handwashing) stayed
external — the new tables don't happen to cover either fact. **MICRO-F-048** (HIV,
Rubella — transplacental) is now verified too, on review: the new table lists each
pathogen under its single most prominent route rather than every route it uses, so
HIV appearing under "birth canal" there doesn't rule out transplacental transmission
— and Rubella's transplacental role is separately settled (TORCH group). The table's
narrower categorization is kept visible in a note rather than silently dropped, per
job-c-verify.md's new divergence rule.

**Chapter coverage** — Ch.7 (Pathogenic Mechanisms) heaviest by far: 17 questions
(001, 009, 011, 017, 030, 032, 036, 039, 041, 043, 044, 050, 051, 052, 053, 055, 058).
Ch.4 (Diagnostic Methods) 8; Ch.6 (Normal Flora) 6; Ch.10 (Sterilization) and Ch.12
(Viral Replication) 5 each; Ch.2, Ch.11, Ch.14 covered 2 each; Ch.8 (026, 048, 056, after patching) covered 3;
Ch.13 covered 1. Untested in this batch: Ch.1, Ch.3, Ch.5, Ch.9, Ch.15, Ch.16 — expected,
since only 2 of 5 exam models have been extracted so far, well under a third of the
full finals/Medicine question pool.

**Needs your eyes** — nothing. No question was unreadable or left unresolved; every
verdict carries a chapter anchor and evidence, or is explicitly labelled external.

---

Full per-question resolutions: [microbiology-finals.verify.md](microbiology-finals.verify.md)
