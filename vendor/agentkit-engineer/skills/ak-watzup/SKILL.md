---
name: ak-watzup
description: Reconstruct concise current work status from Git, worktrees, plans, Continuity and roadmap/task artifacts, then rank the next unfinished work.
metadata: {port: angent-fallback, mode: adapted}
---

# Watzup — Portable Fallback

Use when the user asks what is in flight, what remains, or what to do next—especially in a fresh session/worktree.

## Gather

- current branch/HEAD/status;
- active worktrees;
- Continuity frontier;
- files-first plan/progress;
- connected issue/project state;
- recent relevant artifacts/commits.

## Reconcile

Do not simply concatenate statuses.

Resolve which work is verified complete, currently active, blocked, stale or abandoned.

## Output

Return a short priority-ranked status:
- current mission;
- completed/verified;
- in progress;
- blockers/decisions;
- next 1–3 actions with rationale.

Historical Git activity is evidence, not the task frontier by itself.
