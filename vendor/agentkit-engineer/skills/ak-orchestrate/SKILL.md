---
name: ak-orchestrate
description: Coordinate staged or parallel jobs across available agent runtimes/workers with explicit dependencies, isolation, capture and independent synthesis.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Orchestrate — Portable Fallback

Use when several jobs are independent enough that parallelism, context isolation, runtime diversity or independent arbitration creates real value.

## Load progressively

- `references/orchestration-model.md` — job graph and ownership.
- `references/runtime-routing.md` — live capability discovery and route validation.
- `references/capture-recovery.md` — durable job state, interruption and retry.
- `references/safety-arbiter.md` — effect boundaries and independent synthesis.

## Without `ak orchestrate`

Read `references/cli-free-dispatch.md` for the verb-to-capability map. Plan reasoning and task decomposition never require the `ak` executable. Runtime process dispatch, status, events, cancellation and replay safety depend on a verified host mechanism and ANGENT Continuity; do not implement a shadow AgentKit coordinator just to preserve command names.

## Core rule

Do not fan out when one agent can do the work with lower coordination cost.

## Workflow

1. Convert the accepted outcome into a dependency-aware job graph.
2. Discover and verify runtimes/agents that actually exist now.
3. Route jobs by capability, risk, context and isolation requirements.
4. Confirm cwd, writable scope, expected effects and timeout for each job.
5. Isolate parallel writers using disjoint ownership/worktrees when appropriate.
6. Capture each job's status, evidence and artifacts durably enough to resume.
7. Join only after required dependencies settle.
8. Run independent arbitration when consequence or conflicting results warrant it.
9. Reconcile accepted results into ANGENT Reasoning and Continuity.

## Degraded path

If no delegation/runtime supervisor exists, execute the same graph sequentially while preserving dependency, capture and verification semantics.

Do not emulate background durability or sandbox guarantees the host does not provide.
