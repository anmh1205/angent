# Continuity protocol

Continuity reduces lost progress, lost decision basis and duplicate effects; it does not create background execution after the host stops.

## Store

A continuity store must be discoverable in a future session, readable/writable within current permissions, and durable enough for the task.

Backends may differ across ChatGPT/local harnesses. Canonical semantics do not depend on one backend.

## Frontier record

Use a stable work identity and revisioned records.

Preserve only resume-critical semantics: outcome, scope, constraints, verified work, unfinished unit/branches, consequential decisions, compact decision basis/pointers, artifact/source pointers, dependencies, pending effects, next safe action, and the minimal resume binding needed to know whether saved work still maps safely to live state.

For a consequential decision, persisting only the selected action may be insufficient. Preserve enough basis to know which premise/evidence would invalidate it after resume.

Do not persist raw private chain-of-thought or full transcripts as a substitute for semantic state.

## Local file backend

For local harnesses, scripts/frontier_store.py provides a small revision store under <project>/.angent/runtime/continuity/.

Each save:

1. acquires a short writer lock;
2. checks --expected-revision;
3. writes an immutable revision record;
4. atomically refreshes current.json.

Resume scans coherent revision files rather than trusting a single current pointer.

A stale concurrent writer receives a revision conflict and must reload/reconcile. Reload does not mean blindly adopting the newest summary: dependent saved work is resumed only after its live mapping is classified through resume compatibility.

The store intentionally accepts a flexible frontier object; Continuity owns semantics and decides which fields matter for the current task.

## Side-effect transaction

1. **PREPARED** — persist target, intent, expected before/after state, reconciliation method and the authority basis needed to know what effect was intended.
2. **BIND** — when the concrete operation/target/material arguments become known, revalidate that they still match current authority and decisive preconditions. If they materially differ from PREPARED and resume/replay safety depends on the distinction, persist the revised prepared intent before attempt.
3. **ATTEMPT** — perform one authorized effect.
4. **RECONCILE** — inspect authoritative provider state.
5. **VERIFIED/COMMITTED** — persist actual result and advance frontier.
6. **ATTEMPTED_UNKNOWN** — preserve uncertainty and do not replay blindly.

If current instruction/authority changes after ATTEMPT, keep the attempted/in-flight effect record until reconciled even when the forward task no longer wants that effect. A later cancellation or compensation is a distinct effect record, not a rewrite of the original attempt.

Side-effect state may live inside the frontier record; the storage helper does not execute or retry effects.

## Read-only / authoring work

Persist meaningful completed units, durable artifact pointers and controlling decision basis when later units depend on them, even when there is no external write.

Do not wait for a warning that the session may end.

## Resume compatibility

The storage layer preserves revision coherence; it does not prove that external state still matches the saved work.

When interruption/concurrency can change the meaning of dependent work, Continuity reconstructs the minimal resume binding and classifies it through `resume-binding.md`.

Do not require global exact equality. Bind only the identities, versions/digests, effect keys, capability semantics, and dependency assumptions whose drift can change continuation.

AMBIGUOUS and INCOMPATIBLE bindings block only their dependent transitions; unrelated verified/runnable work may continue.

## Limitations

The local backend protects writers on one filesystem and detects stale revisions. It is not a distributed consensus system.

Cross-machine/cloud backends must implement equivalent revision/conflict semantics appropriate to their environment.

Continuity state cannot grant permission that the current user instruction no longer grants.
