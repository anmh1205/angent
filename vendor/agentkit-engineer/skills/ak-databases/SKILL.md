---
name: ak-databases
description: Design and operate PostgreSQL/MongoDB data models, queries, indexes and migrations using workload evidence and safe rollout practices.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Databases — Portable Fallback

## Load progressively

- `references/data-modeling.md` — ownership, constraints and access patterns.
- `references/schema-and-migrations.md` — rollout-safe schema/data transitions.
- `references/query-performance.md` — plans, indexes and measured tuning.

## Workflow

1. Identify engine/version and workload.
2. Define data invariants and lifecycle.
3. Model access patterns/transaction boundaries.
4. Write correct queries first.
5. Measure query behavior before optimization.
6. Treat migrations as production state transitions.
7. Verify application compatibility across rollout phases.
8. Protect destructive changes with backup/recovery evidence when required.

Avoid database advice detached from the actual engine, schema and workload.
