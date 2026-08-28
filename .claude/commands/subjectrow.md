---
description: Do one named row of RUN-PLAN.md instead of the next todo one. Refuses if it's already done (unless told to redo) or if a row it depends on isn't done yet.
argument-hint: <row number>
---

Read `CLAUDE.md` at the repo root first, then `RUN-PLAN.md`. The row number is
`$1` — it's the `#` column value within a course's table, not a line number in
the file, and row numbers restart at 1 in each course's table. If `$1` is
missing or not a number, stop and ask which row (and which course, if the
number alone is ambiguous across tables — `#` is only unique within a table).

This is the same engine as `/subjectnext`, aimed at one specific row instead
of "whatever's next." Everything in `/subjectnext` about announcing the row,
marking it `doing`, doing only that row, handling an early stop, and closing
out with `done` + commit applies here unchanged — read that file's Do the
row / If you stop early / Close out sections and follow them. This file only
covers what's different: picking the row and the checks before starting it.

## Find the row

Locate row `$1` in the course table the user means. If more than one course
plausibly matches (they didn't say which, and the number exists in more than
one table), stop and ask which course.

## Refuse if it's already done

If the row's status is `done`, do not redo it. Tell the user what the row is
and that it's already done, and stop — unless their request explicitly said
to redo it (e.g. "redo row 17", "rerun", "do it again"). A bare `/subjectrow
17` is not that — treat it as a mistake to flag, not a request to overwrite
verified work. If they did ask for a redo, treat the existing output as
superseded, not as something to merge with: rerun the job clean and replace
what's there, same as if the row were fresh, and say clearly in your report
that this was a redo and what changed from the previous pass.

## Refuse if a dependency isn't done

Pipeline order is fixed within a tab: B (source) before C (verify), C before
D (build); A (extract) has no upstream dependency inside this file (its input
is raw captures, not another row) but C and D both need A's extract to exist
first. Before starting, check every row upstream of this one that this row's
job actually needs:

- **Job C** row → needs both an **A** row for this tab/batch and the
  course's **B** row(s) to be `done`. If either isn't, refuse and say
  specifically which one is missing (e.g. "Row 19 is a C row for finals batch
  02 — it needs row 18 (Job A, same batch) done first, which it is, but also
  needs the course's Job B row done, which it is").
- **Job D** row → needs the matching **C** row `done`.
- **A** and **B** rows → no dependency check; they're the start of a chain.

If a dependency row is `doing` (not `todo`, not `done`), treat that the same
as not-done: refuse, and say the blocking row is mid-flight rather than
unstarted, so the user knows to finish or check on that one instead.

If everything checks out, proceed exactly as `/subjectnext` would once it had
already picked this row.
