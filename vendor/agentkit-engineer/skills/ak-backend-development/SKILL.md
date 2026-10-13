---
name: ak-backend-development
description: Design and implement production backend services across common stacks while preserving API contracts, state ownership, security and operational behavior.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Backend Development — Portable Fallback

## Load progressively

- `references/service-contracts.md` — API/event/state ownership.
- `references/auth-errors.md` — authentication/authorization/validation/error behavior.
- `references/operations-tests.md` — observability, transactions, tests and production behavior.

## Workflow

1. Identify framework/runtime/database versions.
2. Define external contract and state ownership.
3. Implement validation and auth boundaries.
4. Keep transport thin and domain/service behavior explicit.
5. Make transactions/idempotency explicit around side effects.
6. Add tests at appropriate boundaries.
7. Add observability for failures that operators must diagnose.
8. Verify deployment/runtime implications.

Do not introduce microservices/queues/infrastructure merely because the Skill supports them.
