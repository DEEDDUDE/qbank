---
description: Do the next row of RUN-PLAN.md — one job, one course, one tab or batch — then stop and commit.
---

Read `CLAUDE.md` at the repo root first, then `RUN-PLAN.md`.

## Pick the row

Scan every course table top to bottom. If any row is `doing`, that is the row
to run — a previous session started it and stopped early; resume exactly
where its note says it left off. Otherwise take the first `todo` row you find
(top of the file first, i.e. earliest course listed, top row of that course's
table). If a `todo` row's target depends on an earlier `todo` row in the same
tab (e.g. a `D` row that needs a `C` row above it done first), skip it and
take the next eligible row instead — never run a row out of order.

If there are no `doing` or `todo` rows anywhere, tell the user the plan is
fully done and stop.

## Announce it

Before doing anything else, state which row you're running: course, job,
target, size. This is the one-sentence "what I'm about to do" — don't skip it.

## Mark it `doing`

Edit that row's status to `doing` in `RUN-PLAN.md` before starting work, so a
crash or interruption mid-row leaves an honest trail for the next session.

## Do the row — and only the row

Invoke the qbank skill for the job this row names (A/B/C/D), scoped to exactly
this row's target — one course, one tab, one batch, per CLAUDE.md and the
skill's own stateless-jobs rule. Do not:

- continue on to another row after this one finishes
- pull in other tabs' or other courses' material "while you're at it"
- carry vision work from a different tab into this session (CLAUDE.md: one tab
  per session)

If the row is a Job A session with a page budget noted in `Size` (e.g. "~65 of
132 files"), stay inside that budget even if more material is sitting right
there in the same folder — that's what the next row is for.

If you get through the row's target and it's genuinely small enough to also
close out the next row or two with negligible extra cost (e.g. an 8-file Job C
verify immediately followed by its Job D build, both trivial), you may fold
them in — but say so explicitly when you report back, and mark every row you
actually touched.

## If you stop early

Work doesn't always finish cleanly — a source file turns out corrupted, the
user needs to weigh in on a disputed claim, context runs long. If you stop
before the row is fully done, leave it as `doing` (not `todo`, not `done`) and
write a note precise enough that a cold session could resume from it: what's
done, what's left, any open question blocking it.

## Close out

Once the row is actually complete:

1. Update its status to `done` with a one-line note (question count, conflict
   count, whatever the equivalent of the microbiology rows above already show
   — match that style).
2. If the job produced committable output (Job B's source files, Job D's
   `out/` file + ledger entry, or any fix along the way), commit it — this is
   also where `RUN-PLAN.md`'s own edit gets committed, same commit or a
   trailing one. Follow the git safety rules: review staged changes, don't
   force anything, don't amend history.
3. Report to the user what got done and what row is next in line. Stop —
   `/subjectnext` never chains into a second row on its own.
