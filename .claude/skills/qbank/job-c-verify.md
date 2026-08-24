# Job C — Verify

Decide the real answer to every question, and record why.

This is where last year's problem gets fixed. A circulating answer file is a record of
what some student clicked, not what is true. Job C treats every claimed answer as an
accusation to be tested, never as information.

---

## Input

- the extract from Job A
- `source.md` and `source.index.md` from Job B, plus `source.lab.md` and
  `source.lab.index.md` where the course has a lab track — see Routing below for which
  index a given tab checks first

## Who needs work

| tier | action |
|---|---|
| **official** | pass through untouched — Moodle or the professor already stated it |
| **claimed** | verify: decide independently, then compare |
| **open** | answer from the source |

Roughly a third of a typical pile is `official` and costs nothing here.

A `claimed` question may carry `disputed: true` from Job A — two or more competing
claims from the same source page rather than one. It still goes through the same
independent-answer-first process as any claimed question; see `### disputed input`
below for how the comparison step differs.

---

## Routing — how this stays cheap

Never load the whole source. For each question:

1. Read the tab's **primary** index first (small, loads whole) — `source.lab.index.md`
   for a lab tab, `source.index.md` for a lecture tab. See CLAUDE.md's Routing entry for
   which is primary per tab.
2. Match the question's terms against chapter entries → pick the chapter.
3. If the primary index has no supporting chapter, check the **other** index before
   giving up — a lab question is occasionally answered only in a lecture chapter (e.g. a
   biochemical-test fact that the lecture covers but the lab manual assumes), and the
   reverse happens too. Cite whichever chapter actually answered — `{#labNN}` or
   `{#chNN}`, not necessarily the tab's own namespace.
4. **Group every question that routed to the same chapter**, then load that chapter
   once and verify the whole group against it. Group across both indexes if both were
   used — a chapter is still read once, regardless of which index named it.

Grouping by chapter rather than question order means each chapter is read once per
course instead of once per question. On a 325-question course that is the difference
between a few passes and a few hundred.

If routing is ambiguous, take the two best chapters. If still unresolved after checking
both indexes, the question is `not-in-source` — do not go fishing through the whole
file.

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

### disputed input

A question arriving with `disputed: true` carries two or more competing claims from a
single source page — this is the within-page counterpart to
[Cross-checking duplicates](#cross-checking-duplicates) below, which handles the same
kind of disagreement across exam models instead of within one page.

**The answer-first rule applies with extra force here.** Decide from the source before
looking at either claim, precisely because two claims sitting side by side make it twice
as easy to find a reason to agree with one of them.

Then compare:

- If the source supports one claim, the status is `verified`, and `answer:` is that
  claim. The `note:` records which claim system won and which lost — do not just drop
  the loser silently.
- If the source supports neither, the status is `conflict`. Both losing claims stay
  recorded in `note:`, same as any conflict.

```
status: verified
answer: c
basis: Ch. 4 — Bacterial Growth {#ch04}
evidence: Penicillin acts on cells actively building peptidoglycan, which occurs
  during exponential growth.
note: Disputed source (inline mark: b, margin mark: c). The source supports the
  margin claim, c.
```

Never treat a dispute as a reason to hedge or average — decide the same way you would
for a single claim, then say which claim was right.

**Margin outranks inline when the source can't decide.** For the specific two-mark-
system dispute job-a-extract.md documents — an inline ring drawn tight on the option
itself, versus a larger digit circled in the margin — margin is the higher-trust
claim. Confirmed across every such dispute checked so far (three, all on one page,
microbiology microlab batch: MICRO-LAB-009, 010, 012 — margin was correct in all
three, including one, 012, that was directly source-verifiable rather than decided
on outside knowledge). This is a tie-breaker only, not a replacement for the rule
above: decide from source first, and if the source actually supports one claim over
the other, that decides it regardless of which mark made it. Margin only gets the
benefit of the doubt when the source is silent and the question has to be answered
`external` or left `not-in-source`.

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

### When the source and standard teaching diverge

Occasionally the source is genuinely narrower than settled outside knowledge — e.g. a
table that categorizes each pathogen under its single most prominent transmission
route reads, on a narrow view, as if it's denying every other route. **The source
decides the answer.** But the divergence is a fact worth knowing, not noise — record
it in `note:`, never drop it silently. This is the same instinct as `conflict`'s
"never silently correct," applied to source-vs-outside-knowledge instead of
source-vs-claim: whichever way the verdict lands, the tension that produced it stays
visible.

This is not license to override the source with outside knowledge whenever they
disagree — `external`'s own rule still holds: the source wins whenever it actually
covers the topic, full stop. This applies only to how a covered topic is read when
its phrasing is narrower than what it plainly supports (e.g. one route listed doesn't
imply an exclusive claim about every other route) — a judgment call, and one to make
carefully and note explicitly, not a general permission to reach past the source.

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
