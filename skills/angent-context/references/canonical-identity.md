# Canonical target identity

An external provider identifier is a locator, not automatically the current source-of-truth target.

A task may refer either to:
- a **current canonical role** such as “the ANGENT private plugin”, “production deployment”, “the XZ project”, or “the current book”;
- an **exact provider identity** such as one specific plugin ID, commit, release, issue, page, deployment, or historical object;
- a **historical/superseded object** intentionally used for comparison, migration, rollback analysis, or cleanup.

Do not silently collapse these intents.

## Resolve before use

When provider identity can be replaced, migrated, superseded, aliased, or versioned and the distinction can change correctness:

1. interpret whether the task wants the current canonical role or an exact identity;
2. find the authoritative current mapping for that role;
3. resolve the provider identity and relevant version/release/state;
4. preserve the mapping provenance;
5. treat remembered IDs, old URLs, archived releases, and prior session identifiers as historical evidence until current source-of-truth confirms them.

Useful mapping sources can include:
- current explicit user instruction;
- project checkpoint/configuration or canonical project artifact;
- provider state that explicitly marks the current object/release;
- a task-specific source-of-truth named by Contract.

No universal provider registry is required.

## Precedence

Current explicit user intent remains authoritative.

If the user explicitly names an exact historical/provider ID, do not remap it merely because a newer canonical object exists.

If the task names a semantic role such as “current/private/production/canonical”, current project/provider mapping outranks stale memory/history.

Provider recency alone does not automatically define project canon. A project may intentionally pin an older exact object/version.

When project and provider mappings disagree in a way that can change action, preserve the conflict and resolve it instead of guessing from timestamps or familiar names.

## Superseded identities

A superseded identity may remain useful for:
- migration comparison;
- cleanup;
- audit;
- release history;
- reconciliation of old effects.

It must not be queried or mutated as the current canonical target merely because it appeared in prior chat, memory, or an old checkpoint.

## Before consequential action

Context supplies the resolved canonical binding when needed.

Execution must act on the resolved target, not substitute a remembered ID.

If the canonical mapping changes after resolution but before mutation, re-enter current authority/mutation-freshness checks.

## Resume

A saved provider identity records what earlier work referred to; it does not prove that the same identity is still canonical.

For work whose intent is “current canonical object”, re-resolve the role on resume and classify compatibility.

For work intentionally bound to one exact historical object, preserve that exact identity unless current authority changes the task.

## Calibration

Correct:
- memory contains plugin A, current checkpoint/provider mapping says canonical plugin B, task asks for “the current ANGENT plugin” → use B;
- task explicitly asks to inspect superseded plugin A → use A and keep its historical status explicit.

Incorrect:
- choose A because it is familiar from prior sessions;
- choose B merely because its provider timestamp is newest when the project explicitly pins A;
- inspect one identity and write another without re-resolution.
