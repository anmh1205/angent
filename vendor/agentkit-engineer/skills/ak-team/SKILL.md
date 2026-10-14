---
name: ak-team
description: Coordinate independent live teammate sessions with shared work, direct communication, explicit ownership, verification, shutdown, and cleanup when the active harness truly supports that lifecycle.
metadata: {port: angent-fallback, mode: degraded}
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

If the required lifecycle is unavailable, **do not silently substitute ordinary subagents or sequential role-play and call it Team**.

Return a blocked/degraded result and offer a separate explicit route such as `ak-orchestrate`, ordinary bounded delegation, or sequential owner work.

## When Team fits

Use for:
- several genuinely independent research/review scopes;
- competing debugging hypotheses;
- non-overlapping implementation ownership;
- work requiring ongoing teammate communication.

Avoid for short sequential chains or overlapping writers.

## Lead workflow

1. Define one combined outcome and acceptance evidence.
2. Partition independent work with explicit dependencies.
3. Give each teammate a bounded contract: role, scope, inputs, ownership, effects, output, checks.
4. Keep concurrent writers disjoint; worktrees are collision isolation, not sandboxes.
5. Coordinate through live shared state/messages.
6. Treat idle as waiting, not completion.
7. Integrate only completed prerequisites.
8. Verify the combined result independently; teammate messages are handoffs/evidence, not proof.
9. Shut down and clean up using the live lifecycle; report cleanup failure rather than guessing state directories.

Team does not create new authority. Use the smallest team that creates real value.
