# Setup — moving to Claude Code

Everything below happens once. After this, sessions start themselves.

---

## 1. Make the folder

```bash
mkdir -p qbank/{scripts,site,.claude/skills/qbank}
cd qbank && git init
```

## 2. Drop in the five files

```
qbank/
  CLAUDE.md                        ← repo root
  .claude/skills/qbank/
    job-a-extract.md
    job-b-source.md
    job-c-verify.md
    job-d-build.md
```

## 3. Gitignore

```gitignore
courses/*/raw/
courses/*/slides/
site/dist/
site/node_modules/
*.pdf
!courses/*/out/*.md
.DS_Store
```

## 4. Organize one course

Start with microbiology only. Prove the loop before touching the other five.

```
courses/microbiology/
  raw/
    quizzes/      ← the Virology + Pathogenesis quiz captures
    midterm/      ← نموذج ١–٤ and the 2021/2022 photos
    finals/
  slides/         ← microbiology lectures
```

Unzip with something UTF-8 aware so Arabic filenames survive. **Don't rename anything**
— timestamps in names like `PHOTO-2022-12-27-16-39-37.jpg` are what restores page order.

---

## 5. First session

Open Claude Code in `qbank/` and say:

> Read CLAUDE.md and the four job specs in .claude/skills/qbank/.
> Then write scripts/prep.py — the Stage 0 local prep from Job A: hash and dedupe,
> detect text layers, auto-rotate, crop to content, grayscale, downscale to 1000px.
> No model calls, no tokens. Run it on courses/microbiology/raw/ and show me the
> pre-flight report before we extract anything.

That gives you the page count, how many are free via text layer, the duplicates it
dropped, and the token estimate — before spending anything.

---

## 6. Then, in order

1. **Job A** on `raw/quizzes/` — the smallest pile. Read the output properly before
   scaling up. This is the moment to fix the spec, while it's 40 questions and not 325.
2. **Job B** on `slides/` — produces `source.md` + `source.index.md`.
3. **Job C** — verification. Read the conflicts first; they're the payoff.
4. **Job D** — build and commit.
5. Only then the other five courses.
6. The app last, once real files exist for it to display.

---

## Open items

- **`CLAUDE.md` lists four statuses.** Job C added a fifth, `external` — for standard
  facts your slides don't cover, answered but never labelled `verified`. Add it.
- **Job A's Stage 0 numbers were measured on your microbiology photos.** Different
  courses may photograph differently; re-check the 1000px floor if a new course's
  captures are worse.
- **The app plan** isn't written yet. Build it after a real course exists — designing a
  UI for imaginary data is how you end up rebuilding it.

---

## The rules worth remembering without opening a file

1. Nothing deleted — unreadable gets a status, not the bin.
2. Nothing invented — generated options are labelled as generated.
3. Extraction never answers; verification never sees the claim before deciding.
4. The source outranks the students; conflicts keep both answers.
5. Checks are arithmetic, not care.
6. Text layer → OCR → vision, first one that works.
