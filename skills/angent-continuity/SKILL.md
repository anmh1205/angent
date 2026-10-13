---
name: angent-continuity
description: Proactively persist the frontier of active work, support interruption-safe resume and reconcile ambiguous external effects across chat and local harnesses.
---

# ANGENT Continuity — Active-Work Frontier

Continuity owns persistence and resume semantics, not task strategy.

Its job is broader than saving a checkpoint before chat disconnects. The storage backend may differ by harness, but the frontier/revision/reconciliation semantics do not.

## Load references progressively

- references/active-work-frontier.md — recognize non-trivial work and advance a durable frontier.
- references/continuity-protocol.md — persist revisioned work state and side-effect records.
- references/resume-reconciliation.md — resume after interruption or concurrent external change.
- references/frontier-lifecycle.md — lifecycle, baseline pointers and invalidated dependent work.

## Recognize active work early

A task needs continuity when it is costly or unsafe to reconstruct from a prompt alone: multi-step repository/project work, long research, multi-chapter authoring, broad audits, or multi-stage tool effects.

Do not wait for a predicted interruption signal.

## Maintain a living frontier

Keep enough durable state to answer:
- what outcome is being pursued and lifecycle state;
- what scope/invariants apply;
- what is verified complete;
- what is unfinished;
- what decisions affect later work;
- which accepted baseline/artifact-state pointer later work depends on;
- which previously verified units are stale/recheck after dependency changes;
- where artifacts/evidence live;
- which coverage ledger a broad audit/inspection depends on;
- what blockers/dependencies remain;
- whether an external effect is ambiguous;
- what the next safe action is.

Advance at meaningful work boundaries, not after every tool call.

## External sources are reconciliation evidence

GitHub, Jira, Notion, deployment state, and provider APIs establish outside-world facts.

They do not replace the active-work frontier.

On resume, recover the frontier first, then inspect external sources that may have changed and reconcile accordingly.

## Consequential side effects

Before a consequential/non-idempotent effect, persist PREPARED intent with enough information to identify/reconcile the operation.

Afterward inspect authoritative state and mark VERIFIED/COMMITTED or ATTEMPTED_UNKNOWN.

Never blindly replay an uncertain write.

## Read-only / authoring work

Persist meaningful completed units, artifact pointers, curriculum/research frontier, and next unfinished unit even when there is no external write.

## Resume

1. recover the highest coherent frontier;
2. apply newest instruction/current authority;
3. inspect unresolved effects before replay;
4. validate artifact/source pointers;
5. reconcile external state likely to have changed;
6. return the current frontier to Context/Reasoning.

A transcript, model context, or unsynced scratch file is not durable continuity by itself.

ANGENT cannot continue after the host stops unless another runtime actually schedules/runs it.
