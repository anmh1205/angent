---
name: ak-cook
description: Implement an accepted feature, plan or fix through a disciplined inspect → change → verify workflow, using specialists when they add real value.
metadata: {port: angent-fallback, mode: adapted}
---

# Cook — Portable Fallback

Cook is the main implementation workflow.

Read `references/implementation-workflow.md`.

## Entry conditions

Have enough of:
- accepted objective/plan;
- applicable AGENTS.md;
- known constraints;
- owned files/modules;
- acceptance evidence;
- stop/replan conditions.

If the problem is still unclear, route to Scout/Research/Brainstorm/Plan instead of coding through uncertainty.

## Modes

- **direct** — one agent implements a coherent work unit.
- **parallel** — delegate disjoint work with explicit ownership.
- **fast** — minimize ceremony, not verification.
- **no-test** — only when the user explicitly requests deferring tests; record the debt.
- **auto** — continue through authorized runnable units until the endpoint/blocker.

## Boundary

Cook may adapt implementation tactics.

When evidence invalidates the accepted architecture/plan, return to Reasoning before broad redesign.
