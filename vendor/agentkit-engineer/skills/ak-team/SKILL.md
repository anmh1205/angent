---
name: ak-team
description: Coordinate independent live teammate sessions with shared work, direct communication, explicit ownership, verification, shutdown, and cleanup when the active harness truly supports that lifecycle.
metadata: {port: angent-fallback, mode: adapted}
---

# Team — Portable Fallback

Use only when genuine live teammate collaboration creates value.

## Required capability

Before starting, verify that the active harness exposes the lifecycle required by the requested team work:
- team/session creation;
- shared work/task state;
- bounded delegation;
- direct messaging/coordination;
- waiting/status observation;
- shutdown;
- cleanup;
- write/isolation controls when implementation is involved.

If any load-bearing lifecycle capability is unavailable, **hard-stop this Team workflow**.

Do not silently substitute ordinary subagents, sequential role-play, or an Orchestrate job graph and still call the result Team. Offer that as a separately named route only after making the semantic difference explicit.

## When Team fits

Use for:
- several genuinely independent workstreams that need ongoing direct coordination;
- competing debugging hypotheses that need live cross-checking;
- non-overlapping implementation ownership with shared work state;
- work where teammates must message, wait on, and react to each other.

Avoid for short sequential chains or overlapping writers.

## Lead workflow

1. Define one combined outcome and acceptance evidence.
2. Partition independent work with explicit dependencies.
3. Give each teammate a bounded contract: role, scope, inputs, ownership, effects, output, checks.
4. Keep concurrent writers disjoint; worktrees are collision isolation, not sandboxes.
5. Coordinate through the verified live shared state/messages.
6. Treat idle as waiting, not completion.
7. Integrate only completed prerequisites.
8. Verify the combined result independently; teammate messages are handoffs/evidence, not proof.
9. Shut down and clean up using the verified lifecycle; report cleanup failure rather than guessing state directories.

Team does not create new authority.

Use the smallest team that creates real value.
