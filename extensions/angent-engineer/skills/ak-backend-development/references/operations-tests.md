# Backend operations and verification

Choose evidence that matches the claim.

## Tests

Consider:
- core domain/service behavior;
- transport/schema validation;
- authentication and resource authorization;
- persistence integration and transaction behavior;
- cache/queue/event duplicate or ordering semantics;
- external-provider failure and timeout behavior;
- idempotency/retry;
- migration compatibility when relevant;
- load/latency behavior only when performance is part of the contract.

A green unit suite does not establish provider integration or production readiness.

## Migration boundary

When code depends on a schema/data change:
- identify current and target application/schema versions;
- preserve coexistence/rollout compatibility when required;
- keep migration execution separately authorized;
- verify the application against the intended pre/post migration state.

Do not treat implementation authority as production-migration authority.

## Observability

Observe only what helps explain required behavior:
- request/error rate;
- latency;
- queue/background failures;
- database/provider errors;
- health/readiness;
- correlation/request IDs where useful.

Logs/metrics/traces are evidence, not a requirement to add observability infrastructure to every task.

## Runtime verification

When a runtime claim matters, capture the exact environment/config boundary.

A process starting is weaker evidence than a representative request/flow completing with the expected state transition and failure behavior.
