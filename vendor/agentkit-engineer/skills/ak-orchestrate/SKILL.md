---
name: ak-orchestrate
description: Coordinate a verified dependency-aware job graph across available runtimes or workers, with explicit ownership, bounded evidence, isolation, resume semantics, and independent synthesis.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Orchestrate — Portable Fallback

Use when one outcome benefits materially from staged dependencies, parallel work, runtime diversity, isolation, or an independent arbiter.

Use `ak-team` instead when ongoing live teammate discussion/shared team lifecycle is the load-bearing requirement.

## Load progressively

- `references/orchestration-model.md` — job graph and ownership.
- `references/runtime-routing.md` — live capability discovery and route validation.
- `references/capture-recovery.md` — durable job state, interruption and retry.
- `references/safety-arbiter.md` — effect boundaries and independent synthesis.

## Core rule

Do not fan out when one agent can complete the work with lower coordination cost.

A runtime/provider name is a candidate route, not evidence that the route is currently usable.

## Workflow

1. Convert the accepted outcome into a dependency-aware job graph.
2. Discover and verify candidate runtimes/workers and their controls **now**.
3. Route each job by capability, risk, context, authority, and isolation requirements.
4. Confirm cwd, writable ownership, expected effects, timeout/stop condition, and required output/evidence for each job.
5. Isolate concurrent writers with disjoint ownership/worktrees when appropriate; worktrees do not provide OS sandboxing.
6. Capture bounded status/evidence/artifacts needed to join or resume.
7. Do not advance dependent jobs through ambiguous/failed prerequisites.
8. Use independent arbitration when consequence or conflicting results warrant it.
9. Reconcile accepted results into ANGENT Reasoning and Continuity.

## Runtime adaptation

The native AgentKit CLI can provide deterministic plan state/process supervision on supported hosts. The fallback must not claim those mechanics unless the active harness actually provides equivalent observable guarantees.

When a durable supervisor is unavailable:
- use a verified harness-native worker/subagent/process route when available;
- preserve the job graph and dependency semantics;
- disclose interruption/resume gaps;
- use Continuity only for ANGENT semantic frontier state, not as a fake process supervisor.

A sequential route is acceptable only when jobs need not overlap and the selected outcome does not depend on parallel elapsed time, runtime diversity, concurrent isolation, or detached durability.

If a load-bearing orchestration requirement cannot be preserved, return BLOCKED/DEGRADED with the missing capability instead of silently converting the workflow.

Do not emulate background durability, process ownership, sandbox guarantees, or parallelism the host does not provide.
