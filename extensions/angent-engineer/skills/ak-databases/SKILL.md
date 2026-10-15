---
name: ak-databases
description: Design and change PostgreSQL/MongoDB data models, queries, indexes and migrations with workload evidence, least-privilege access, rollout compatibility and explicit production recovery gates.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Databases — Portable Fallback

Use when data structure, query behavior, migration or database administration is the primary outcome.

Use Backend Development when the database work is incidental to a broader API implementation, DevOps when cloud/infrastructure is primary, and Fix for diagnosis that should remain read-only until a correction is approved.

## Load progressively

- `references/data-modeling.md` — ownership, constraints and access patterns.
- `references/schema-and-migrations.md` — rollout-safe schema/data transitions.
- `references/query-performance.md` — plans, indexes and measured tuning.

## Prepare

Resolve:
- engine/version and exact environment;
- database/schema/collection owner;
- representative reads/writes and workload/volume;
- data sensitivity, retention and consistency requirements;
- transaction/lock tolerance and maintenance window;
- application versions that may coexist;
- least-privilege access;
- mutation authority and recovery evidence.

Keep connection strings, passwords and tokens out of prompts, logs, shell history and committed files.

For production mutation, require an appropriate current backup/snapshot, a tested or credible restore route, forward/rollback-or-compensating plan, and post-change verification. If these are absent, prepare/analyze but do not claim the production change is safe to execute.

## Workflow

1. Inspect the real engine/schema/workload and current access patterns.
2. Define data invariants, identity/ownership/lifecycle and consistency boundary.
3. Model transactions/relationships from real access patterns.
4. Write correct queries first.
5. Measure plans/locks/cardinality before performance changes.
6. Design migrations as application+data state transitions, not isolated DDL.
7. Prefer compatibility-safe expand → migrate/backfill → contract where versions coexist.
8. Preview/validate destructive or replacement operations before execution.
9. Apply only to the explicitly authorized target with suitable privilege.
10. Verify schema/data/application behavior after the transition.

## Boundaries

Bundled/native utilities may depend on Python drivers, database CLIs and network access. Tool presence and connectivity are runtime facts; do not claim utility parity when they are unavailable.

A read-only diagnosis does not authorize writes. A migration prepared in code does not authorize running it against production.

Avoid database advice detached from the actual engine, schema, workload and recovery boundary.
