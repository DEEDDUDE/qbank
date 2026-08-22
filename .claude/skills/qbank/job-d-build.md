# Job D — Build

Write the finished batch to disk in the shape the app consumes.

Smallest of the four jobs. It decides nothing — Job C already did. Job D formats,
names, records, and commits.

---

## Naming

```
courses/<course>/out/<course>-<tab>-<NN>.md
```

`NN` is the batch number for that course and tab: `microbiology-quizzes-01.md`, then
`-02.md` when new quiz questions arrive months later.

Job D picks `NN` by reading the **filenames** already in `out/` — the only moment
anything in this pipeline looks at previous output, and it never reads their contents.
Batches stay independent.

Question IDs carry the batch so they can never collide:
`MICRO-Q2-014` = microbiology, quizzes batch 2, question 14.

---

## The file

```markdown
---
course: microbiology
tab: quizzes
batch: 02
built: 2026-08-22
questions: 46
verified: 38 | conflict: 4 | external: 2 | not-in-source: 2 | needs-eye: 0
source: microbiology/source.md
---

## MICRO-Q2-014
status: verified
form: mcq
type: single
answer: b
basis: Ch. 6 — Antimicrobial Agents {#ch06}
evidence: MBC is the lowest antibiotic concentration that kills the isolated
  organism, unlike MIC which only inhibits growth.
seen: quiz 2

MBC is defined as?
a) The lowest concentration in serum that inhibits a standard dose
b) The lowest concentration that kills the bacteria isolated from the patient
c) The lowest concentration that inhibits growth of the isolated bacteria
d) The lowest concentration of bacteria that inhibits a standard dose

## MICRO-Q2-015
status: conflict
form: mcq
type: single
answer: c
claimed: b
basis: Ch. 4 — Bacterial Growth {#ch04}
evidence: Penicillin acts on cells actively building peptidoglycan, which happens
  during exponential growth.
note: The circulating file marks b. The source supports c.

Penicillin is effective when bacterial cells are making peptidoglycan, so its
optimal action will be during?
a) Death phase
b) Exponential phase
c) Stationary phase
d) Lag phase
```

Rules:

- One `##` block per question, ID as the heading.
- Metadata lines first, then a blank line, then stem and options.
- Every block is self-contained. No references to other files, no shared footnotes.
- `options: generated` appears on any question whose distractors Job C built.
- Human-readable as-is. You should be able to open this file and study from it with no
  tooling at all.

---

## One format only

Markdown is the source of truth. The site parses it at build time and generates
whatever JSON it wants — and that JSON is never committed.

Two hand-maintained formats always drift apart, and then you have two answers to the
same question and no way to tell which is current. That is exactly the failure this
project exists to prevent.

---

## Ledger

Append every processed input file to `courses/<course>/.ledger.json`:

```json
{
  "batches": [
    { "id": "quizzes-02", "built": "2026-08-22", "questions": 46,
      "files": [
        { "name": "PHOTO-2022-12-27-16-39-37.jpg", "sha1": "a3f9...", "pages": 1 }
      ]
    }
  ]
}
```

This is what makes the second run cheap. On any re-run, hash the folder, skip anything
already listed, process only what's new. It is also your proof of what has been done —
no wondering whether a folder was already handled.

---

## Commit

One commit per batch:

```
microbiology/quizzes: batch 02 — 46 questions (4 conflicts)
```

Committed: the batch file, `report.md`, `.ledger.json`, any unresolved `flagged/` crops.
Not committed: raw captures, slides, anything generated.

Never amend or rewrite an earlier batch. New information is a new batch.

---

## Hand off to the app

The app scans `courses/*/out/*.md`, reads the frontmatter, and files each batch under
its course and tab. Nothing else to configure — the header carries everything the site
needs.

Cross-batch duplicate merging happens **there**, not here. When the same question shows
up in a later batch, the site merges them into one entry and extends `seen:`. A question
appearing across four years running is not one you skip.

---

## Done when

The batch file exists and parses, every question has a status, the ledger lists every
input file with its hash, `report.md` is written, and the commit is made.

Then tell the user: the counts, the conflicts by ID, and anything still needing their
eyes — once, at the end, in one message.
