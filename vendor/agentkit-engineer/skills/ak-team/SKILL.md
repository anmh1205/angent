---
name: ak-team
description: Coordinate a small team of independent specialist agents for research, implementation, review or debugging when parallelism or context isolation adds real value.
metadata: {port: angent-fallback, mode: adapted}
---

# Team — Portable Fallback

Use only when multiple independent teammates improve quality or elapsed time enough to justify coordination.

Read `references/team-protocol.md`.

## Runtime capability

Discover what the active harness actually supports:
- persistent team/teammate sessions;
- one-shot subagents;
- isolated worktrees/files;
- messaging/task surfaces;
- no delegation.

This workflow requires a **live team lifecycle** when the requested job depends on team creation, shared work/task state, teammate messaging, waiting/joining, shutdown, or cleanup.

If those lifecycle capabilities are unavailable, stop the `ak-team` workflow and report the missing capability. Do not substitute ordinary one-shot subagents or sequential role execution and call it Team.

Use `ak-orchestrate` or direct Reasoning/Execution instead when the user's real requirement is merely decomposition, context isolation, or sequential specialist roles and live team semantics are not required.

## Lifecycle

1. Define the parent outcome and why a team is useful.
2. Partition independent jobs with explicit dependencies.
3. Give each teammate a narrow context contract: role, job, inputs, ownership, allowed effects, acceptance evidence and return format.
4. Isolate concurrent writers and avoid overlapping ownership.
5. Track blocked/completed jobs durably enough to recover from interruption.
6. Join evidence/artifacts, not full transcripts.
7. Preserve disagreement until ANGENT Reasoning resolves it.
8. Reconcile integrated results and update Continuity.

## Lead responsibilities

The lead/synthesizer owns:
- job decomposition;
- dependency order;
- authority propagation;
- conflict/integration handling;
- checking that worker claims match artifacts/evidence.

Workers do not become independent strategic owners.

## Failure handling

- blocked worker → re-scope or supply missing context; do not resend unchanged;
- worker failure → keep useful partial evidence and reassess routing;
- overlapping writes → stop/sequence or isolate before continuing;
- conflicting conclusions → compare evidence or use independent arbiter; do not majority-vote.

## Resource policy

Use the smallest team that creates real value.

Do not duplicate the same context across many agents only to obtain more opinions.

## Boundary

Team does not create new authority.

ANGENT Reasoning remains the strategic owner and Continuity remains the active-work state owner.
