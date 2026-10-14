# Resume binding and compatibility

A saved frontier is valid only while the live world can still be mapped to the semantics it depended on.

This is not byte-for-byte checkpoint equality. Preserve and compare only identities/boundaries whose drift could change safe continuation.

## Resume binding

When needed, bind:
- stable work identity and revision;
- canonical target/source identity and version/digest;
- accepted baseline/artifact pointer;
- decisive evidence pointers used by a saved decision;
- pending effect identity and reconciliation key;
- long-running operation/provider identity;
- capability/tool semantic identity when drift could change a pending action;
- branch dependency/shared-state assumptions.

## Compatibility

- **COMPATIBLE** — relevant live state still maps to the saved semantics, or changes are known to be disjoint.
- **REVALIDATE** — relevant state changed but affected premises/dependencies can be re-established safely.
- **AMBIGUOUS** — mapping is not strong enough to know whether dependent continuation or replay is safe.
- **INCOMPATIBLE** — saved work no longer describes the same target/effect/baseline/capability semantics.

## Required behavior

COMPATIBLE may continue after ordinary freshness and authority checks.

REVALIDATE marks only affected work stale/recheck, refreshes the changed premises/dependencies, and returns to Reasoning before dependent action.

AMBIGUOUS fails closed for the dependent transition. Inspect authoritative state; do not infer completion or replay from missing evidence.

INCOMPATIBLE does not continue the old dependent plan. Establish a new baseline/action model or explicit migration.

Exact identity is required only where replay/effect safety depends on it. A new unrelated commit need not invalidate a saved frontier, while one changed dependency may.

A later timestamp never wins automatically. Preserve independently verified disjoint work and classify only the overlapping dependency closure.

Resume compatibility cannot grant authority. Current Contract authority still governs the next effect.

ANGENT defines these semantics; the harness owns any checkpoint, transaction, journal, or durable-execution mechanics.
