---
name: ak-plan
description: Produce a durable files-first implementation plan with dependencies, phases, acceptance evidence, risks and explicit unresolved decisions.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Plan — Portable Fallback

## Load progressively

- `references/files-first-plan.md` — durable plan representation.
- `references/decomposition.md` — split work by dependency/ownership/outcome.
- `references/plan-validation.md` — check completeness and execution readiness.
- `references/plan-reconciliation.md` — overlapping plans, dependencies and whole-plan consistency.

## Entry condition

The main technical direction must be understood well enough that planning is not hiding unresolved architecture.

## Workflow

1. Read AGENTS.md, relevant source/evidence and any active unfinished plans.
2. Restate objective, hard constraints and non-goals.
3. Detect overlap/dependencies with existing work before creating a competing plan.
4. Record accepted decisions and live assumptions.
5. Decompose by dependency and coherent outcome.
6. Add implementation intent, not only filenames.
7. Mark shared interfaces, migrations and generated artifacts.
8. Add acceptance/verification per work unit.
9. Mark parallelism only where ownership is separable.
10. Validate the entire plan against the original outcome.
11. Persist it as a normal readable file/artifact.

Before handing the plan to Cook, perform a whole-plan consistency sweep if any decision/phase changed during validation.

Do not require AgentKit CLI, plan database, HTML/wiki output or GitHub issue projection for plan correctness.
