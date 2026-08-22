# Job A — Extract

Turn a pile of exam screenshots and photos into one structured batch file.

**This job transcribes. It does not answer.** No medical reasoning, no filling gaps,
no guessing a key that isn't printed on the page. A question Job A can't resolve
leaves here unresolved and labelled — that is a success, not a failure.

---

## Input

Anything that carries questions: `.pdf`, `.jpg`, `.png`, `.docx`, `.txt`, `.md`,
pasted text. Exam screenshots are the common case, not the only one.

**Never refuse an input because it isn't the expected shape.** Identify what it is,
read it with the right method, and label whatever you can't resolve. Getting stuck is
a failure mode; an item marked `unknown` is not.

### Material types

| type | what it looks like | how to read it |
|---|---|---|
| **screenshot** | Moodle exam captures, photos of screens | Stage 0 prep → vision |
| **document** | Word/PDF/text with real text | read the text directly, no vision |
| **mixed** | document with embedded question images | text where possible, vision for the images |

Text-bearing files skip Stage 0 entirely — no images, no tokens spent on pixels.
A `.docx` from a professor is read straight through.

The user supplies two things at the start:

- **course** — e.g. `microbiology`
- **tab** — `quizzes` | `midterm` | `finals`

If either is missing, ask once. Don't guess from filenames.

---

## Stage 0 — Local prep (no tokens)

Runs before anything is sent to the model.

1. **Flatten to pages.** PyMuPDF renders PDF pages at 200 dpi. Loose images pass through.
2. **Check for a text layer.** PyMuPDF (`page.get_text()`) per page — a real text layer
   comes back as actual prose, not a handful of stray characters; pull it directly and
   skip vision for those pages entirely. Free, exact, and Unicode-safe on Arabic
   filenames, which the poppler `pdftotext` on this machine cannot open at all.
3. **Auto-rotate** using EXIF, then correct obvious skew.
4. **Crop to content.** Detect the lit screen / white page region and cut the bezel,
   keyboard, desk and taskbar. On phone-photo sources this alone removes 40–50% of
   the pixels.
5. **Grayscale, downscale to 1000px long edge, JPEG q85.**
6. **Order the pages** by filename timestamp so the sequence matches capture order.

Verified on real input: the filled radio button survives step 5 even on the worst
angled photo of a laptop screen. Do not go below 1000px — that marker is the floor.

---

## Stage 1 — Read

Pages go up in batches of 6–8. Continuous sequence, **not page by page** — questions
run across page boundaries and must be stitched before being closed.

### Step 1: classify each question on two axes

Every question gets a **tier** (how much the answer can be trusted) and a **form**
(what shape it's in). These are independent — judge them separately.

**Tier — where the answer came from:**

| tier | meaning | examples |
|---|---|---|
| **A — official** | stated by an authority | Moodle's `The correct answer is:`, a professor's answer sheet, a textbook key |
| **B — claimed** | a student marked it | Moodle `Answer saved`, a circled option in a shared file |
| **C — open** | no answer present | Moodle `Not yet answered`, a bare question list |

Tier A is finished when transcribed. Tiers B and C go to Job C for verification.

When the tier is ambiguous, drop to the lower one. Treating a guess as official is
the expensive mistake; the reverse just costs one verification pass.

In Moodle tier A, `Mark 0.00 out of 1.00` means the selected radio is **wrong** —
record it as a distractor, never as the answer.

**Form — what shape the question is in:**

| form | meaning |
|---|---|
| **mcq** | stem + options |
| **qa** | question + answer, no options |
| **fact** | a statement with no question wrapped around it |
| **unknown** | couldn't be resolved — kept anyway, flagged |

`qa` is common in material a professor hands out. It is a perfectly valid entry. Job A
records it as-is and **does not invent options** — that is Job C's decision, and any
options it generates are marked as generated so you always know which came from a real
exam and which didn't.

### Step 2: transcribe

Anchors depend on the format. Detect which set applies from the first few items, then
hold it for the rest of the batch.

**Moodle** (English or Arabic interface):
- opens: `Question N` / `سؤال N`
- options: `a. b. c. d.`
- closes: `Clear my choice` / `أخل اختياري` / the correct-answer box

**Plain documents:** numbering (`1.` `Q1` `١-`), blank lines, or bold stems. Answers
may sit inline (`— answer: B`), in a trailing key, or in a parallel column.

**No anchors at all:** fall back to meaning. A question ends where the next one starts.
This is slower and less certain, so mark such items `needs-eye` if the split is
genuinely doubtful — but split them anyway rather than merging two questions into one.

A question is only closed when its terminator is seen. No terminator means it
continues onto the next page or block.

### Step 3: hard rules

- **Ignore hand-drawn marks.** Green ticks, pen circles, highlighter — these are a
  student's annotations, not Moodle's. Only the radio/checkbox state and the printed
  answer line count.
- **Decode HTML entities.** `&gt;` → `>`, `&lt;` → `<`, `&amp;` → `&`. Moodle leaks
  raw entities; left alone they make questions meaningless.
- **Detect multi-answer.** Checkboxes instead of radios, or `The correct answers are:`
  (plural) means `type: multi`. Record every correct option.
- **Preserve text exactly.** Typos in the original stay. Do not clean, rephrase, or
  correct grammar — a reworded question no longer matches its duplicates.
- **Arabic is interface, never content.** Course material is English. Arabic appears
  only as Moodle chrome — `سؤال 3`, `أخل اختياري`, `الوقت المتبقي` — and sometimes as
  Arabic-Indic numerals in question numbers. Read it as an anchor, then discard it.
  Never carry it into a stem or an option.
- **RTL layouts.** Some pages run the Arabic interface with English question text and
  option letters on the right. Same question, mirrored. Read normally, output
  left-to-right.

---

## Anti-loss checks

Run after Stage 1. All three are arithmetic — no judgement, no trust.

1. **Number continuity** — *when the material is numbered.* Numbers must run unbroken
   within a source. A gap means a question was dropped → re-read that region.
   Unnumbered material skips this check rather than failing it.
2. **Count reconciliation** — *always.* State the number of questions visible in each
   page or block before transcribing. Mismatch with the number returned → re-read it.
3. **Structural floor** — *always.* Flag anything malformed: no stem, or `form: mcq`
   with fewer than 2 options. A `qa` or `fact` entry with no options is **not**
   malformed — that is its correct shape.
4. **Language check** — *always.* Question text is English. Arabic characters inside a
   stem or an option mean interface text leaked in or the read failed → flag it.
   Arabic-Indic digits in question *numbers* are normal and just get converted.

A question never leaves the batch because it was hard to read. It leaves with a status.

---

## Stage 2 — Recovery

Only failures from the checks above. Do **not** resend the page.

Crop the single question's region from the **full-resolution original** and send just
that. A one-question crop at native resolution costs less than half a downscaled page,
so the hard cases get the best possible image for the least cost.

If the crop still fails, the question is written out with `status: needs-eye` and its
crop saved to `flagged/`. Then it is shown to the user — all of them together at the
end, in one pass, never interrupting mid-batch.

---

## Output

One file: `<course>-<tab>.extract.md`

```
---
course: microbiology
tab: quizzes
questions: 46
tiers: official 31 | claimed 12 | open 3
forms: mcq 42 | qa 4
needs-eye: 0
---

### MICRO-Q-014
tier: official
form: mcq
type: single
answer: b
Which of the following methods is used to quantify the number of infectious
viruses in body fluid?
a) Hemagglutination
b) Plaque assay
c) Polymerase chain reaction
d) Enzyme immunoassay

### MICRO-Q-015
tier: claimed
form: mcq
type: single
claimed: d
MBC defined as?
a) MBC is the lowest concentration of antibiotic in the patient's serum that
   inhibits the activity of a standard dose of antibiotic.
...

### MICRO-Q-016
tier: official
form: qa
answer: Plaque assay
Which method quantifies infectious virus in body fluid?
```

Field rules:

- `answer:` appears only for tier A — it came from an authority and is trusted.
- `claimed:` appears only for tier B — a student's guess, nothing more.
- Tier C has neither.
- `type:` applies to `form: mcq` only. `type: multi` lists every correct option:
  `answer: a, b`
- `form: qa` puts the answer text in `answer:` with no option letters.
- `needs-eye` adds `img:` pointing into `flagged/` (screenshots) or quotes the raw
  text block (documents).

Duplicates are merged **within this batch only** — same stem, one entry. Cross-batch
matching is the app's job, not this one.

---

## Done when

Every question in the input appears exactly once in the output, with a tier, and the
three anti-loss checks pass clean.

Nothing invented. Nothing dropped. Nothing answered that wasn't already answered on
the page.
