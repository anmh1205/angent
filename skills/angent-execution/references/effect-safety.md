# Effect safety

Retry behavior depends on the effect and the failure boundary, not merely on whether the tool returned an error.

## Effect classes

- read-only observation;
- local reversible write;
- remote idempotent write;
- remote non-idempotent write;
- destructive/irreversible/high-blast-radius effect.

## Consequential write protocol

Before a consequential effect:
- persist PREPARED intent through Continuity;
- include target, expected state transition and reconciliation method;
- after the concrete operation/target/material arguments are resolved, revalidate that current authority still covers exactly that effect.

If the target, scope, arguments, authority, or decisive precondition changed since planning/approval, do not treat the old authorization as transferable. Return to Contract/Reasoning or the required approval boundary.

This prevents a planning-to-execution time-of-check/time-of-use gap without requiring ANGENT to implement its own permission runtime.

After attempt:
- inspect authoritative state;
- mark VERIFIED/COMMITTED if known;
- mark ATTEMPTED_UNKNOWN if ambiguous.

## Timeout is not failure

A timeout or lost response means outcome is unknown until reconciled.

For create/send/publish operations, blind retry may duplicate effects.

Likewise, a harness/tool dispatch error does not establish that the provider rejected the operation or that the target state is negative.

## Failure boundary before retry

Before retrying, distinguish at least:
- did the harness/tool invocation fail before reaching the intended provider?
- did transport/provider infrastructure fail without establishing domain outcome?
- was access denied?
- did the provider explicitly reject the requested operation?
- did an authoritative observation succeed and establish a negative domain fact?
- could a side effect have occurred with the outcome now unknown?

Use `failure-semantics.md` when the distinction changes the next action.

## Reversibility

When uncertainty is high, prefer reversible actions and narrow scope.

Do not broaden permissions merely because a tool supports it.

## Verification

Verify the state the user cares about, not just transport success or failure.

For local writes inspect the diff/artifact. For remote writes read the provider. For deployment inspect health/state required by the Contract.
