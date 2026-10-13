# Continuity protocol — durable state across arbitrary interruption

Continuity reduces lost progress and duplicated side effects; it does not create background execution after the host stops.

## Durable sink

A valid checkpoint store must be independently discoverable in a future session, writable within current permission, readable back and durable enough for the task.

Chat transcript, model memory, pending tool calls and unsynced scratch files are not durable checkpoints.

## Canonical record

Use a stable work key and versioned records. Preserve:
- scope/phase/authorization;
- source-of-truth identifiers/versions;
- verified frontier;
- saved artifact pointers;
- unresolved dependencies;
- pending operation when any;
- exact next action.

## Side-effect transaction

1. **PREPARED** — before an external effect, persist target, intent, expected before/after state and reconciliation query; read it back.
2. **ATTEMPT** — perform one authorized effect.
3. **RECONCILE** — query the authoritative provider.
4. **COMMITTED/VERIFIED** — persist actual result/evidence and advanced frontier.
5. **ATTEMPTED_UNKNOWN** — when provider state remains ambiguous, do not replay blindly.

## Read-only / authoring work

Persist each meaningful completed unit and its durable artifact pointer. Do not wait for a predicted session-risk signal.

## Resume

- recover the highest coherent verified record;
- apply newest user instruction and current authorization;
- reconcile ambiguous effects before replay;
- validate artifact pointers;
- return the frontier to Reasoning for current-state reconstruction.

Continuity state cannot grant permission that the current user instruction no longer grants.
