# qbank

Turns previous-exam questions into a verified question bank, then publishes it as a
study site.

Built and maintained by one medical student. Read this before touching anything.

---

## Layout

```
qbank/
  CLAUDE.md                  ← this file
  .claude/skills/qbank/      ← the skill: Jobs A–D
  scripts/                   ← local prep: crop, downscale, hash, OCR
  courses/
    <course>/
      raw/
        quizzes/ midterm/ finals/ microlab/ practice/   ← original captures, gitignored
      slides/                        ← lecture material, gitignored
      source.md                      ← clean study source (Job B)
      source.lab.md                  ← lab study source, own anchor namespace (Job B)
      out/                           ← verified batch files (Job D)
      flagged/                       ← image evidence: crops any verdict depends on
      .ledger.json                   ← hashes of everything already processed
  site/                      ← the published app
```

**The folder path is the metadata.** `courses/microbiology/raw/quizzes/` means course
`microbiology`, tab `quizzes`. Never ask the user to type what the path already says.

Courses this semester: `microbiology`, `pharmacology`, `public-health`,
`molecular-genetics`, `metabolic-biochem`, `pathology`.

---

## What gets committed

**Committed:** `source.md`, everything in `out/`, `.ledger.json`, the skill, scripts,
the site, and `flagged/`.

**`flagged/` holds image evidence, not a pending queue.** Any question whose verdict
depends on a photo — a zone of inhibition, a colony plate, a stain result — keeps its
crop committed permanently, resolved or not. It's the visual equivalent of Job C's
evidence line: a `verified` or `external` answer that cites what a photo shows is only
checkable if the photo is still there to check. Pending review (`needs-eye`) is a
status on the question, recorded in the extract/verify files — not a property of the
folder. Don't delete a crop because its question got resolved.

**Never committed:** `raw/`, `slides/`, any generated PDF or built HTML, any file with
a version suffix. Git history is the version history — there is no `_v2`, no `_final`.

Raw captures stay local because they are large binaries and git keeps every version of
them forever. They are input, consumed once.

---

## The pipeline

| job | in | out |
|---|---|---|
| **A — Extract** | `raw/<tab>/` | structured questions, each tagged with tier and form |
| **B — Source** | `slides/` | `source.md`, chapter structure intact |
| **C — Verify** | extract + source | answers resolved, each with a chapter citation |
| **D — Build** | verified questions | `out/<course>-<tab>.md` |

Full specs live in `.claude/skills/qbank/`. Jobs run independently — one course, one
tab, one batch at a time.

The skill is **stateless**. It never loads previous batches. Accumulation is the site's
job, not the skill's.

---

## Conventions

**IDs** — `MICRO-Q-014`: course, tab, number. Assigned at extraction, permanent, never
reused, never renumbered. The `microlab` tab uses `MICRO-LAB-NNN` (e.g. `MICRO-LAB-007`)
instead of a single-letter tab code.

**Routing** — the lab tab (`microlab`) routes to `source.lab.index.md` first. If no
`{#labNN}` chapter supports the question, fall back to `source.index.md` and its
`{#chNN}` chapters. Only when neither index has it is the question `not-in-source`. Cite
whichever chapter actually answered — a lab question resolved from a lecture chapter
carries that `{#chNN}` anchor, not a lab one. Lecture tabs (`quizzes`, `midterm`,
`finals`, `practice`) route to `source.index.md` first and may fall back to
`source.lab.index.md` the same way. The order matters, not the exclusivity: the lab
manual is the better authority for a lab question, but the lecture chapters are not
off-limits when it is silent.

**Tier** — how much the answer can be trusted:
- `official` — an authority stated it (Moodle's printed key, a professor's answer sheet)
- `claimed` — a student marked it; unverified
- `open` — no answer present

**Form** — what shape the question is in: `mcq`, `qa`, `fact`, `unknown`.

**Status after verification** — `verified`, `conflict`, `not-in-source`, `needs-eye`.

**Citation** — chapter only: `basis: Ch. 6 — Antimicrobial Agents`. No filenames, no
line numbers.

---

## Hard rules

1. **Nothing is ever deleted.** A question that can't be read or answered gets a status,
   not the trash. Loss is the failure mode this whole project exists to prevent.

2. **Nothing is invented.** No guessed answers, no reconstructed stems, no plausible
   filler. If it wasn't on the page or in the source, it doesn't exist.

3. **Generated content is labelled.** When Job C builds options for a `qa` question,
   they are marked generated. A fabricated distractor mistaken for a real one teaches
   something that was never on any exam.

4. **The source outranks the students.** When a claimed answer contradicts `source.md`,
   the source wins, both are kept, and the note explains why.

5. **Extraction never answers.** Job A transcribes only. Answering is Job C's job, and
   keeping them apart is what stops confident wrong answers.

6. **Checks are arithmetic, not judgement.** Number continuity, count reconciliation,
   structural floor. A dropped question is caught by subtraction, not by care.

7. **Cheapest capable method first.** Text layer → OCR → vision. Most lecture PDFs have
   real text and cost nothing. Vision is only for images where the answer is a *mark*,
   not a character — no OCR engine reports a filled radio button.

8. **Check the ledger before spending anything.** Already-hashed files are skipped.
   New material is simply what isn't in the ledger yet.

---

## Working style

- One piece at a time. Show it, get agreement, then continue.
- Report before spending: page count, how many are free via text layer, estimated tokens.
- Batch the questions for the user — collect everything needing human eyes and present
  it once at the end, never interrupting mid-run.
- Filenames carry capture order (`PHOTO-2022-12-27-16-39-37.jpg`). Never rename raw files.
- Arabic filenames from Google Drive zips often arrive mangled (`#U0646#U0645...`).
  Repair the encoding, don't rename by hand.
- **One tab per session; start fresh for large vision batches.** Cost tracks conversation
  length — turn count and how much context has already accumulated — not page count. A
  page processed late in a long-running session costs far more than the same page
  processed in a short, fresh one, because every turn re-sends or rebuilds the whole
  conversation so far. Don't carry Job A or Job B vision work for one tab into the next
  tab's session.
- **All vision input goes through `prep.py`'s Stage 0.** Never render pages directly into
  context. Stage 0's downscale keeps each page's image tokens near the API's minimum; a
  raw render can run well past it and cost several times more per page for no benefit.
- **Job A appends to the extract file per batch**, rather than holding prior batches'
  results in context, so the conversation doesn't grow past what the current batch needs.
