# Continuity protocol

Continuity reduces lost progress and duplicate effects; it does not create background execution after the host stops.

## Store

A continuity store must be discoverable in a future session, readable/writable within current permissions, and durable enough for the task.

Backends may differ across ChatGPT/local harnesses. Canonical semantics do not depend on one backend.

## Frontier record

Use a stable work identity and revisioned records. Preserve the relevant outcome, scope, constraints, verified work, unfinished unit, decisions, artifact/source pointers, dependencies, pending effects and next safe action.

## Local file backend

For local harnesses, `scripts/frontier_store.py` provides a small revision store under `<project>/.angent/runtime/continuity/`.

Each save:

1. acquires a short writer lock;
2. checks `--expected-revision`;
3. writes an immutable revision record;
4. atomically refreshes `current.json`.

Resume scans coherent revision files rather than trusting a single current pointer.

A stale concurrent writer receives a revision conflict and must reload/reconcile.

The store intentionally accepts a flexible frontier object; Continuity owns semantics and decides which fields matter for the current task.

## Side-effect transaction

1. **PREPARED** — persist target, intent, expected before/after state and reconciliation method.
2. **ATTEMPT** — perform one authorized effect.
3. **RECONCILE** — inspect authoritative provider state.
4. **VERIFIED/COMMITTED** — persist actual result and advance frontier.
5. **ATTEMPTED_UNKNOWN** — preserve uncertainty and do not replay blindly.

Side-effect state may live inside the frontier record; the storage helper does not execute or retry effects.

## Read-only / authoring work

Persist meaningful completed units and durable artifact pointers even when there is no external write.

Do not wait for a warning that the session may end.

## Limitations

The local backend protects writers on one filesystem and detects stale revisions. It is not a distributed consensus system.

Cross-machine/cloud backends must implement equivalent revision/conflict semantics appropriate to their environment.

Continuity state cannot grant permission that the current user instruction no longer grants.