---
name: angent-continuity
description: Proactively persist a multi-branch frontier of active work, preserve resume-critical decision basis and long-running operation identity, support interruption-safe resume and reconcile ambiguous external effects across chat and local harnesses.
---

# ANGENT Continuity — Active-Work Frontier

Continuity owns persistence and resume semantics, not task strategy or branch selection.

Its job is broader than saving a checkpoint before chat disconnects. The storage backend may differ by harness, but the frontier/revision/reconciliation semantics do not.

## Load references progressively

- references/active-work-frontier.md — recognize non-trivial work, preserve branch scheduling state, and advance a durable frontier.
- references/continuity-protocol.md — persist revisioned work state and side-effect records.
- references/resume-reconciliation.md — resume after interruption or concurrent external change.
- references/resume-binding.md — classify whether saved semantics remain compatible with live state before dependent continuation/replay.
- references/frontier-lifecycle.md — task lifecycle, branch scheduling states, baseline/decision-basis pointers and invalidated dependent work.

## Recognize active work early

A task needs continuity when it is costly or unsafe to reconstruct from a prompt alone: multi-step repository/project work, long research, multi-chapter authoring, broad audits, multi-stage tool effects, or long-running operations whose handles/results matter later.

Do not wait for a predicted interruption signal.

## Maintain a living frontier

Keep enough durable state to answer:
- what outcome is being pursued and lifecycle state;
- what scope/invariants apply;
- what is verified complete;
- which unfinished branches remain;
- which branch is RUNNABLE, WAITING_EXTERNAL, BLOCKED or DONE when that distinction changes safe next action;
- what decisions affect later work;
- which compact decision basis/pointer later work depends on;
- which accepted baseline/artifact-state pointer later work depends on;
- whether a task-relevant collaboration-state pointer/subset must survive resume;
- which previously verified units are stale/recheck after dependency or decisive-evidence changes;
- which long-running operations are active, with handle/identity, last observed state, dependents and next informative observation condition when needed;
- where artifacts/evidence live;
- which coverage ledger a broad audit/inspection depends on;
- which behavioral-calibration evidence pointer a later acceptance/regression decision depends on;
- what blockers/dependencies remain;
- whether an external effect is ambiguous;
- what the next safe action or runnable-set pointer is.

A decision basis contains only the decisive premises/evidence pointers, constraints, decision and reconsideration trigger needed to resume correctly. Do not persist raw private reasoning.

Persist collaboration state only when losing it could materially change how the task resumes. When recurrence diagnosis or resumed behavior depends on whether a promoted mechanism actually activated, carry only the relevant mechanism/activation pointer or compact subset. Do not duplicate a full user profile or Learning store into Continuity.

Advance at meaningful work boundaries, including branch scheduling-state changes that alter safe next work, not after every tool call or unchanged poll.

## External sources are reconciliation evidence

GitHub, Jira, Notion, deployment state, running processes/jobs, and provider APIs establish outside-world facts.

They do not replace the active-work frontier.

On resume, recover the frontier first, then inspect external sources, saved operations, and decisive premises that may have changed and reconcile accordingly.

## Consequential side effects

Before a consequential/non-idempotent effect, persist PREPARED intent with enough information to identify/reconcile the operation.

Afterward inspect authoritative state and mark VERIFIED/COMMITTED or ATTEMPTED_UNKNOWN.

Never blindly replay an uncertain write.

## Long-running operations

Persist a process/job/workflow handle when later work or safe resume depends on it.

Continuity does not choose polling frequency or the next branch. Reasoning owns active-frontier selection; Execution owns observation of external operation state.

A running/pending operation is represented as WAITING_EXTERNAL until its next informative observation condition is satisfied. A waiting branch does not block independent RUNNABLE branches.

An unchanged RUNNING/PENDING observation normally updates neither completed-work count nor the semantic frontier unless a wait condition, dependency or other material state changed.

## Read-only / authoring work

Persist meaningful completed units, artifact pointers, controlling decision basis, curriculum/research frontier, independent unfinished branches, and next runnable work even when there is no external write.

## Resume

1. recover the highest coherent frontier;
2. apply newest instruction/current authority;
3. establish resume compatibility for the saved dependency/effect bindings as COMPATIBLE, REVALIDATE, AMBIGUOUS or INCOMPATIBLE;
4. fail closed for dependent replay/continuation when the binding is AMBIGUOUS or INCOMPATIBLE;
5. inspect unresolved effects before replay;
6. restore branch scheduling state and saved long-running operation handles;
7. inspect an external operation only when reconciliation is required or its informative-observation condition is now eligible;
8. validate artifact/source pointers;
9. reconstruct or refresh collaboration state when it affects the next action;
10. refresh stale/time-sensitive decisive premises;
11. reconcile external state likely to have changed;
12. return the frontier to Context/Reasoning so Reasoning can recompute RUNNABLE/WAITING_EXTERNAL/BLOCKED branches before action selection.

A transcript, model context, or unsynced scratch file is not durable continuity by itself.

ANGENT cannot continue after the host stops unless another runtime actually schedules/runs it.
