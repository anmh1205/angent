# Backend operations and tests

Test:
- core domain/service behavior;
- transport validation;
- auth/authorization;
- persistence integration;
- external provider failure;
- idempotency/retry;
- migration compatibility when relevant.

Observe:
- request/error rate;
- latency;
- queue/background failures;
- database/provider errors;
- correlation/request IDs when useful.

Operational visibility should help explain failure mechanisms, not just produce logs.
