---
name: ak-project-management
description: Track implementation progress against durable plans and provider state, coordinate workstreams and keep the active project frontier accurate across sessions.
metadata: {port: angent-fallback, mode: adapted}
---

# Project Management — Portable Fallback

Use when a project has multiple work units, agents, issues or phases whose status must remain coherent.

Read `references/plan-task-reconciliation.md`.

## Sources

Use together as appropriate:
- files-first plan;
- ANGENT Continuity frontier;
- authoritative issue/project system;
- Git/artifact state;
- verification evidence.

Do not treat worker status messages as completion evidence.

## Workflow

1. Recover the current active plan/frontier.
2. Discover the live task/project surface if one exists.
3. Hydrate missing operational tasks from unfinished plan work when useful.
4. Reconcile completed/in-progress/blocked work against actual artifacts and verification.
5. Sync verified status back to all affected plan phases/items, not only the current one.
6. Update provider task state when authorized.
7. Recompute dependencies when prerequisite state changed.
8. Surface the first unfinished valid work unit, blockers and unresolved mappings.

## Boundary

Project Management coordinates delivery state.

It does not own product/architecture decisions.

A dashboard/task board is an operational projection; it must not erase the durable implementation meaning stored in the plan and Continuity.
