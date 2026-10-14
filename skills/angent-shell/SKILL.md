---
name: angent-shell
description: Project ANGENT's already-established cognitive/work state into compact, truthful START/PROGRESS/END status signs without owning task logic.
---

# ANGENT Shell — Status Projection

Shell makes ANGENT's live work state legible to the user. It is a **projection layer**, not a planner, scheduler, checkpoint store, verifier, or source of truth.

Read `references/status-projection.md` for the projection contract.

## START

At the first visible output for an ANGENT task, emit the familiar compact signature:

`[Used ANGENT] [angent + angent-reasoning + angent-research]`

List only owners actually active for the current work. Do not advertise every available skill.

For a substantial, long-running, multi-branch, repair, repository/project, or externally mutating task, add one compact status line when it materially helps the user understand the live frontier, for example:

`[ANGENT Status] ACTIVE | work=engineer-refresh | verified=runtime 1.0.5 synced | next=stable catalog migration`

Direct/simple answers normally need only the first signature or no extra state line.

## PROGRESS

Emit a new status line only when semantic state materially changes, such as:
- a meaningful unit becomes verified;
- the active work/frontier changes;
- RUNNABLE / WAITING_EXTERNAL / BLOCKED composition changes materially;
- a consequential effect is reconciled;
- a required Quality verdict changes a dependent transition;
- canonical/runtime synchronization changes;
- a real blocker or required user decision appears.

A progress sign is communication, not permission to stop unfinished work.

Do not repeat the same sign after routine reads, tool calls, unchanged polls, or cosmetic progress.

## END

For substantial operational work, finish with the verified endpoint state. When versioned source/runtime identity matters, include the verified canonical pointer and runtime/package revision.

Do not claim VERIFIED, SYNCED, DONE, PASS, complete coverage, or zero blockers unless the underlying owner/evidence established it.

## Boundary

Shell may read already-established public status fields from Contract, Context, Reasoning, Execution, Continuity, Quality, and package/source metadata.

Shell must not:
- infer completion from activity;
- turn a worker report into verified state;
- create or mutate frontier/checkpoint state;
- decide which branch runs next;
- upgrade uncertainty;
- expose hidden reasoning or private chain-of-thought;
- dump internal logs, tool-call counts, or a full owner graph into the user-facing sign.
