# Job B — Source

Turn lecture material into `source.md`: the thing every answer gets checked against.

**Do not write this from scratch.** Extraction is already solved by the
`book-to-study-source` skill — faithful full extraction, slide and textbook handling,
unclear text flagged rather than guessed. Its fidelity rules and qbank's hard rules are
the same rules.

Job B = that skill, plus three things it doesn't do.

---

## Input

`courses/<course>/slides/` — whatever the lectures came as. PowerPoint exports, PDFs,
scanned chapters, photographed book pages.

### Read in this order, take the first that works

1. **Text layer** — `pdffonts` lists fonts → `pdftotext -layout`. Exact, instant, free.
   Most PowerPoint-exported PDFs land here, which is most of your material.
2. **OCR** — image-only PDFs and scans. `pdftoppm` at 300 dpi → Tesseract with `-l eng`;
   med course material is English throughout. Slower and imperfect, but source prose is
   redundant enough to survive it.
3. **Vision** — only what OCR mangles badly: diagrams with embedded labels, tables that
   collapse, handwriting.

Report the split before starting: *"142 slides — 118 have text layers (free), 24 need
OCR, ~0 need vision."*

---

## Addition 1 — Anchored chapters

The whole point of `source.md` is that Job C can cite a chapter. So every chapter
heading carries a stable anchor:

```markdown
## Ch. 6 — Antimicrobial Agents {#ch06}
### 6.3 Mechanisms of Resistance {#ch06-3}
```

Rules:

- Numbering comes from the source. If the lectures start at Chapter 4, it starts at
  Chapter 4. Never renumber.
- Anchors never change once written. Job C's citations and the app's links both depend
  on them.
- No chapter numbering in the material? Use lecture numbers (`{#lec03}`). Neither?
  Number the topics in order and say in the file that the numbering is ours, not the
  source's.

---

## Addition 2 — The index

This is the piece that makes Job C possible at all.

A full source is far too large to hold in context alongside a few hundred questions.
So Job B also writes `source.index.md` — small enough to load whole, detailed enough to
route a question to the right chapter:

```markdown
# microbiology — index

## {#ch06} Ch. 6 — Antimicrobial Agents
covers: MIC, MBC, bacteriostatic vs bactericidal, beta-lactams, resistance
mechanisms, efflux pumps, beta-lactamase, selective toxicity
terms: penicillin, cephalosporin, vancomycin, MRSA, ESBL

## {#ch07} Ch. 7 — Sterilization and Disinfection
covers: autoclave, pasteurization, filtration, antiseptics
terms: D-value, spore, ethylene oxide
```

One entry per chapter: the anchor, the concepts covered, and the specific terms that
appear. Job C reads only this, picks the chapter, then loads that chapter alone.

Aim for roughly 3–5% of the source's size. If the index is getting long, the chapters
are too coarse — split them.

---

## Addition 3 — Fixed output location

```
courses/<course>/
  source.md          ← the full study source
  source.index.md    ← the routing index
```

Fixed names, committed to git, one per course. Adding a later lecture deck **merges
into the same file** as a new chapter and the index is regenerated. There is never a
`source_v2.md`.

If a merge would renumber existing chapters, don't — append the new material with its
own numbering and note the origin. Existing citations must never break.

---

## What carries over unchanged

From `book-to-study-source`, and non-negotiable here:

- Only what's in the material. Nothing added from outside knowledge.
- A statement that looks wrong stays as written and gets flagged, not corrected.
- Illegible text is marked, never guessed.
- Detail is preserved — this is a source, not revision notes. Small details are exactly
  what becomes exam questions.
- Lists, tables, figure labels, values and units kept intact.
- Content split across slides is rejoined.

---

## Done when

`source.md` and `source.index.md` both exist, every chapter has a stable anchor, the
index routes to all of them, and the coverage report is written:

> 142 slides across 6 files → 8 chapters. 118 slides read from text layer, 24 via OCR.
> 3 passages flagged unclear. Index: 8 entries.

The flagged passages get shown to you once, at the end, together.
