# Job C — Verify

Decide the real answer to every question, and record why.

This is where last year's problem gets fixed. A circulating answer file is a record of
what some student clicked, not what is true. Job C treats every claimed answer as an
accusation to be tested, never as information.

---

## Input

- the extract from Job A
- `source.md` and `source.index.md` from Job B

## Who needs work

| tier | action |
|---|---|
| **official** | pass through untouched — Moodle or the professor already stated it |
| **claimed** | verify: decide independently, then compare |
| **open** | answer from the source |

Roughly a third of a typical pile is `official` and costs nothing here.

---

## Routing — how this stays cheap

Never load the whole source. For each question:

1. Read `source.index.md` (small, loads whole).
2. Match the question's terms against chapter entries → pick the chapter.
3. **Group every question that routed to the same chapter**, then load that chapter
   once and verify the whole group against it.

Grouping by chapter rather than question order means each chapter is read once per
course instead of once per question. On a 325-question course that is the difference
between a few passes and a few hundred.

If routing is ambiguous, take the two best chapters. If still unresolved after that,
the question is `not-in-source` — do not go fishing through the whole file.

---

## The rule that makes this work

**Answer first. Look at the claim second.**

For every claimed question:

1. Read the question and the chapter.
2. Decide the answer from the source. Write it down.
3. *Only then* look at what the student claimed.
4. Compare.

Reversing this order destroys the whole job. Shown a claimed answer first, it is far
too easy to find a reason the source supports it — and that is exactly how a wrong
answer survives into a study file and gets memorized. The independent answer must exist
before the claim is visible.

---

## Evidence is mandatory

Every resolved answer carries proof:

```
status: verified
answer: b
basis: Ch. 6 — Antimicrobial Agents {#ch06}
evidence: MBC is defined as the lowest antibiotic concentration that kills the
  isolated organism, distinct from MIC which only inhibits growth.
```

- `basis` is the chapter anchor — the citation the app links to.
- `evidence` is a short quote or tight paraphrase from that chapter, enough to check
  the verdict without opening the source.

A verdict with no evidence is an opinion. If no supporting passage can be found, the
status is `not-in-source`, not `verified`.

---

## The five statuses

| status | meaning |
|---|---|
| **verified** | the source supports this answer, evidence attached |
| **conflict** | the source contradicts the claimed answer |
| **external** | not in the source; answered from outside knowledge |
| **not-in-source** | not in the source and not confidently answerable |
| **needs-eye** | the question itself is unreadable or ambiguous |

### conflict

Source wins. Both answers stay:

```
status: conflict
answer: c
claimed: b
basis: Ch. 4 — Bacterial Growth {#ch04}
evidence: Penicillin acts on cells actively building peptidoglycan, which occurs
  during exponential growth.
note: The circulating file marks b. The source supports c.
```

Never silently correct. Seeing the wrong answer next to the right one is how you avoid
re-learning the mistake, and it is also how you catch *my* errors — if you think the
claim was right, the evidence line is right there to check.

### external

Some questions are fair game but simply absent from your slides — standard facts the
lecturer assumed. Don't dead-end on those; answer them, and label the source honestly:

```
status: external
answer: a
basis: external — not covered in course material
evidence: Yersinia pestis is a Gram-negative coccobacillus.
```

Hard rules for `external`:

- It **never** overrides the source. If the chapter covers it, the chapter decides. Full
  stop.
- It is never called `verified`. The app displays it differently, because your exam
  follows your lecturer, not general knowledge.
- Only for facts that are settled and standard. Anything genuinely contested is
  `not-in-source`.

### not-in-source

A real gap. Not a failure — it tells you the slides don't cover something the exam did,
which is worth knowing before the exam rather than during it.

---

## Building options for `qa` questions

When a question arrived as question-and-answer with no options, Job C may build them:

- Distractors come from **the same chapter** — real, related concepts, so the question
  tests understanding instead of pattern-matching.
- Never invent facts to fill an option.
- The result is always marked:

```
form: mcq
options: generated
```

A fabricated distractor mistaken for a real exam option teaches you something that was
never on any exam. The label is what prevents that.

---

## Cross-checking duplicates

The same question often appears in several exam models with different students' answers.
When two claims for one question disagree, that alone is a signal — verify it first and
note the disagreement. Free error detection, no extra reading.

---

## Output

Verified questions plus `report.md`:

> **microbiology / quizzes — 46 questions**
> verified 38 · conflict 4 · external 2 · not-in-source 2 · needs-eye 0
>
> **Conflicts** — the circulating file is wrong on these 4: MICRO-Q-008, 015, 022, 041
> **Not in source** — MICRO-Q-011, 034. Slides may be incomplete here.
> **Chapter coverage** — Ch.6 heaviest (14 questions), Ch.9 untested.

The conflicts are the most valuable output of the entire pipeline. Read them first.

---

## Done when

Every question has a status, every `verified` and `conflict` carries a chapter anchor
and evidence, every `external` is labelled as such, and no question was silently
changed, dropped, or answered without a reason recorded.
