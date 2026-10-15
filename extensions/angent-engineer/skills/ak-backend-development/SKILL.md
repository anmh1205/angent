---
name: ak-backend-development
description: Design and implement a bounded production backend, API or data-access change while preserving the current stack, external contracts, state ownership, security, migration boundaries and operational evidence.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Backend Development — Portable Fallback

Use when the main outcome is a backend service/API/data-access change. Use Databases when schema/migration safety is the primary problem, DevOps when infrastructure/deployment is primary, and Fix when the task is still diagnosis rather than approved implementation.

## Load progressively

- `references/service-contracts.md` — API/event/state ownership and compatibility.
- `references/auth-errors.md` — authentication/authorization/validation/error behavior.
- `references/operations-tests.md` — migration/integration/load/observability and runtime evidence.

## Contract

Resolve from the current project rather than imposing a preferred stack:

- runtime/framework/package-manager versions;
- current API/event contract and non-goals;
- data ownership and database/cache/queue dependencies;
- authentication/authorization boundary;
- expected load/latency/reliability requirements when material;
- file/dependency/network/process authority;
- migration/deployment boundary;
- required verification.

The Skill may implement when write/process capability is available. It does not itself authorize package installation, live-provider calls, production migration, commit, release or deployment.

## Workflow

1. Inspect repository instructions, current stack, service boundaries, tests and runtime conventions.
2. Define the external contract, state ownership, compatibility boundary and failure behavior.
3. Keep transport thin enough that domain/state transitions remain inspectable.
4. Validate untrusted input; separate authentication from resource-level authorization.
5. Make transactions, idempotency, retries and duplicate/event ordering explicit where side effects cross boundaries.
6. Preserve existing data-access/cache/queue conventions unless changing them is part of the task.
7. Add the cheapest tests that establish contract, domain, persistence/provider and failure behavior.
8. Check migration compatibility when code expects schema/data changes; do not silently run a production migration.
9. Add/verify observability only for states operators need to diagnose.
10. Run type/build/test/integration/load or runtime checks proportional to the acceptance claim.
11. Report exact changed files/dependencies, verification evidence, migration/runtime implications and remaining gaps.

## Operational boundaries

A successful local build does not prove a deployed service is healthy.

Calls to real databases, queues, email/payment/provider APIs or production-like environments can mutate remote state or incur cost. Resolve the endpoint/account/fixture and current authority before such effects.

If a backend change depends on a schema transition, preserve compatibility across the rollout phases or route the database phase through Databases.

Do not introduce microservices, queues, caches or infrastructure merely because the Skill knows them.
