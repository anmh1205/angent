# Effect safety

Retry behavior depends on the effect, not on whether the tool returned an error.

## Effect classes

- read-only observation;
- local reversible write;
- remote idempotent write;
- remote non-idempotent write;
- destructive/irreversible/high-blast-radius effect.

## Consequential write protocol

Before a consequential effect:
- persist PREPARED intent through Continuity;
- include target, expected state transition and reconciliation method.

After attempt:
- inspect authoritative state;
- mark VERIFIED/COMMITTED if known;
- mark ATTEMPTED_UNKNOWN if ambiguous.

## Timeout is not failure

A timeout or lost response means outcome is unknown until reconciled.

For create/send/publish operations, blind retry may duplicate effects.

## Reversibility

When uncertainty is high, prefer reversible actions and narrow scope.

Do not broaden permissions merely because a tool supports it.

## Verification

Verify the state the user cares about, not just transport success.

For local writes inspect the diff/artifact. For remote writes read the provider. For deployment inspect health/state required by the Contract.
