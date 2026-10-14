---
name: ak-cook
description: Implement a clear task or accepted plan through inspect → change → verify → review, preserving scope, authority and evidence across interactive, autonomous and parallel modes.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Cook — Portable Fallback

Cook is the main code-delivery workflow once the desired behavior is clear.

Read `references/implementation-workflow.md`.

## Opening contract

Establish or reuse:
- outcome;
- accepted scope and non-goals;
- hard constraints;
- acceptance criteria;
- known design/plan decisions;
- authority boundary for writes, commits, pushes, external effects;
- stop/replan conditions.

If an accepted plan already carries these, reuse it instead of interviewing again.

If the problem or architecture is still materially unclear, route to Brainstorm/Research/Scout/Plan rather than coding through uncertainty.

## Modes

- **interactive/direct** — implement coherent work with meaningful review gates.
- **auto** — continue through authorized runnable units without routine confirmation; authority/safety gates still apply.
- **fast** — reduce research/coordination overhead, not verification or requested scope.
- **parallel** — use independent workers only for proven disjoint ownership/dependencies; integrate before final verification.
- **tdd** — add tests-first protection where regression risk warrants it.
- **no-test** — only when the user explicitly authorizes test deferral; preserve the debt and do not claim tested/verified status.

Mode is an execution policy, not permission to expand scope or perform unrelated side effects.

## Core rules

- Inspect existing implementation, adjacent patterns, tests and project instructions before editing.
- Use Scout when ownership/data/control flow is unclear.
- Reuse existing helpers/interfaces before creating parallel abstractions.
- Implement the smallest coherent change that satisfies the contract.
- Keep unrelated cleanup outside the work unit.
- Revalidate plan/authority when an observation changes a decisive premise.
- Run verification proportional to blast radius.
- Use independent code review for material changes.
- Reconcile the durable plan/task/Continuity state before completion.

Cook may adapt implementation tactics. It may not silently redesign the accepted architecture or widen authority.

## Completion

Do not equate generated code, a green command, a commit, or a worker "done" report with completion.

Return the requested endpoint with:
- implemented scope;
- fresh verification;
- independent review status when required;
- unresolved/deferred items;
- exact artifact/provider state that establishes completion.
