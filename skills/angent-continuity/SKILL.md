---
name: angent-continuity
description: Proactively persist the frontier of active work, preserve resume-critical decision basis and long-running operation identity, support interruption-safe resume and reconcile ambiguous external effects across chat and local harnesses.
---

# ANGENT Continuity — Active-Work Frontier

Continuity owns persistence and resume semantics, not task strategy.

Its job is broader than saving a checkpoint before chat disconnects. The storage backend may differ by harness, but the frontier/revision/reconciliation semantics do not.

## Load references progressively

- references/active-work-frontier.md — recognize non-trivial work and advance a durable frontier.
- references/continuity-protocol.md — persist revisioned work state and side-effect records.
- references/resume-reconciliation.md — resume after interruption or concurrent external change.
- references/frontier-lifecycle.md — lifecycle, baseline/decision-basis pointers and invalidated dependent work.

## Recognize active work early

A task needs continuity when it is costly or unsafe to reconstruct from a prompt alone: multi-step repository/project work, long research, multi-chapter authoring, broad audits, multi-stage tool effects, or long-running operations whose handles/results matter later.

Do not wait for a predicted interruption signal.

## Maintain a living frontier

Keep enough durable state to answer:
- what outcome is being pursued and lifecycle state;
- what scope/invariants apply;
- what is verified complete;
- what is unfinished;
- what decisions affect later work;
- which compact decision basis/pointer later work depends on;
- which accepted baseline/artifact-state pointer later work depends on;
- whether a task-relevant collaboration-state pointer/subset must survive resume;
- which previously verified units are stale/recheck after dependency or decisive-evidence changes;
- which long-running operations are active, with handle/identity and last observed state when needed;
- where artifacts/evidence live;
- which coverage ledger a broad audit/inspection depends on;
- what blockers/dependencies remain;
- whether an external effect is ambiguous;
- what the next safe action is.

A decision basis contains only the decisive premises/evidence pointers, constraints, decision and reconsideration trigger needed to resume correctly. Do not persist raw private reasoning.

Persist collaboration state only when losing it could materially change how the task resumes. Do not duplicate a full user profile or Learning store into Continuity.

Advance at meaningful work boundaries, not after every tool call or every unchanged poll.

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

Continuity does not choose polling frequency. Execution owns wait/poll behavior.

An unchanged RUNNING/PENDING observation normally updates neither the semantic frontier nor the completed-work count unless some other material state changed.

## Read-only / authoring work

Persist meaningful completed units, artifact pointers, controlling decision basis, curriculum/research frontier, and next unfinished unit even when there is no external write.

## Resume

1. recover the highest coherent frontier;
2. apply newest instruction/current authority;
3. inspect unresolved effects before replay;
4. inspect saved long-running operations before relaunching or polling aggressively;
5. validate artifact/source pointers;
6. reconstruct or refresh collaboration state when it affects the next action;
7. refresh stale/time-sensitive decisive premises;
8. reconcile external state likely to have changed;
9. return the current frontier to Context/Reasoning.

A transcript, model context, or unsynced scratch file is not durable continuity by itself.

ANGENT cannot continue after the host stops unless another runtime actually schedules/runs it.
