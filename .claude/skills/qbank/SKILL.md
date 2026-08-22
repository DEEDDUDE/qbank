---
name: qbank
description: Turns previous-exam captures and lecture slides into a verified, cited question bank. Use for extracting exam questions from raw captures (Job A), building a study source from slides (Job B), verifying claimed answers against that source (Job C), or building the final committed batch file (Job D).
---

# qbank pipeline

Read `CLAUDE.md` at the repo root first — it has the folder layout, conventions,
and hard rules that govern every job below. This file only routes to the specs.

Four independent, stateless jobs. Run one course, one tab, one batch at a time.
Never load previous batches — accumulation is the site's job, not the skill's.

| job | spec | in | out |
|---|---|---|---|
| **A — Extract** | [job-a-extract.md](job-a-extract.md) | `courses/<course>/raw/<tab>/` | structured questions, tiered and formed, never answered |
| **B — Source** | [job-b-source.md](job-b-source.md) | `courses/<course>/slides/` | `source.md` + `source.index.md` |
| **C — Verify** | [job-c-verify.md](job-c-verify.md) | Job A's extract + Job B's source | every question resolved, with a chapter citation |
| **D — Build** | [job-d-build.md](job-d-build.md) | Job C's verified questions | `courses/<course>/out/<course>-<tab>-<NN>.md`, committed |

Before Job A on fresh input, run `scripts/prep.py <course> <tab>` — Stage 0 local
prep (hash, dedupe, text-layer detection, crop, downscale). No tokens spent.

Hard rules that apply across every job: nothing deleted, nothing invented,
generated content labelled, the source outranks the students, extraction never
answers, checks are arithmetic not judgement, cheapest capable method first,
check the ledger before spending anything. Full detail in `CLAUDE.md`.
