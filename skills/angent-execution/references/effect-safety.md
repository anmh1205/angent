# Effect safety

Retry behavior depends on the effect and the failure boundary, not merely on whether the tool returned an error.

## Effect classes

- read-only observation;
- local reversible write;
- remote idempotent write;
- remote non-idempotent write;
- destructive/irreversible/high-blast-radius effect.

## Consequential write protocol

For a consequential effect that could be duplicated or left ambiguous after interruption, preserve a PREPARED intent in an authorized durable store when available. Include the exact target, expected transition and reconciliation method; revalidate current authority against the concrete operation and arguments immediately before dispatch.

If the store is unavailable, first ask whether a provider-native idempotency key, conditional write, transaction or authoritative read-back makes replay/recovery equivalently safe. Use it only when the operation's actual semantics support that claim. Otherwise do not dispatch an irreversible, non-idempotent or otherwise unreconcilable effect whose outcome would be unsafe after interruption. Report the specific blocked effect; unrelated reads, reasoning and safely recoverable operations can continue. Never write checkpoint metadata into an audit-only target or public issue without separate authorization.

A missing journal is a stated durability limitation, not permission to invent a checkpoint, and not a global failure of every task.
If the target, scope, arguments, authority, or decisive precondition changed since planning/approval, do not treat the old authorization as transferable. Return to Contract/Reasoning or the required approval boundary.

This prevents a planning-to-execution time-of-check/time-of-use gap without requiring ANGENT to implement its own permission runtime.

After attempt:
- inspect authoritative state;
- mark VERIFIED/COMMITTED if known;
- mark ATTEMPTED_UNKNOWN if ambiguous.

## Authority/objective change after attempt

Once ATTEMPT occurs, a later instruction cannot be treated as if dispatch never happened.

If current authority or requested outcome changes while an operation is in flight:
1. stop selecting new dependent effects whose authority/goal no longer holds;
2. preserve the original operation identity and effect state;
3. determine whether the provider has already committed/completed, is still running, failed, or is ambiguous;
4. when current authority calls for cancellation/compensation and the provider supports it, model that cancellation/compensation as a separate effect and revalidate its exact invocation;
5. verify the resulting state that now matters to the user.

Do not blindly retry, relaunch, or “cancel” by dropping the handle.

Cancellation may itself be non-idempotent, partial, or too late. Apply the same reconciliation discipline to it.

## Mutation basis and concurrent drift

When a write is derived from previously inspected canonical state, protect the read→modify→write boundary when stale overwrite is material.

Use a provider-native expected revision/SHA/version/precondition when available. If the live target changed, refresh and reconcile the semantic delta instead of replaying an old full replacement.

Preserve unrelated concurrent changes. Return overlapping or ambiguous drift to Reasoning.

Read `mutation-freshness.md` for the full semantic boundary.

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
