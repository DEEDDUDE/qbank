---
description: Report progress across all courses from RUN-PLAN.md — done, in progress, next, and anything left unfinished.
---

Read `RUN-PLAN.md`. This is a read-only report — don't edit the file, don't run
any job, don't touch git.

For each course, summarize:

- **Done** — how many rows, and (if the notes carry it) a rough total question
  count and conflict count for the tabs that are fully built
- **In progress** — any `doing` row: what it is, and what its note says about
  where it stopped
- **Next** — the next `todo` row `/subjectnext` would pick up for this course
- **Unfinished** — anything past that `next` row still sitting as `todo`,
  summarized as a count rather than listed row-by-row unless the user asks for
  detail

Then give one overall line: how many courses are untouched (still on their
single `sort` row), how many are mid-pipeline, how many tabs across all
courses are fully `done`.

Keep it tight — this is a status report, not a re-print of the table. If the
user wants the raw table, point them at `RUN-PLAN.md` rather than reproducing
all of it in chat.
