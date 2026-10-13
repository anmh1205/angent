---
name: ak-goal-warmup
description: Prepare a long-running autonomous goal by locking outcome, constraints, evidence, authority and execution readiness before the run starts.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Goal Warmup — Portable Fallback

Use before a long-running autonomous/multi-session goal when failure to lock the outcome or authority could cause drift.

## Outcome contract

Establish:
- requested final state;
- hard constraints and explicit non-goals;
- authorized effects and authority boundaries;
- acceptance evidence;
- budget/time/compute constraints when relevant;
- known blockers and user-only decisions.

Do not turn “autonomous” into permission for unrestricted side effects.

## Preflight

1. Scout/research only unknowns that affect feasibility or routing.
2. Build a dependency-aware plan.
3. Review every phase against the outcome contract so planning does not silently shrink or expand scope.
4. Identify external/destructive effects and where fresh authorization/reconciliation is required.
5. Define verification for the goal and for high-risk intermediate transitions.
6. Define recovery/replan behavior for interrupted work and failed steps.
7. Ensure Continuity has a durable goal identity, current frontier and artifact pointers.

## Readiness matrix

Check the relevant rows:

| Area | Ready means |
|---|---|
| Outcome | final state and exclusions are unambiguous enough to execute |
| Plan | dependencies and critical interfaces are coherent |
| Authority | effect boundaries are known |
| Evidence | completion can be proven |
| Recovery | interruption/ambiguous effects have a safe resume path |
| Runtime | required capabilities are actually available or have an explicit fallback |
| Decisions | no unresolved user-only decision blocks the first runnable stage |

## Terminal state

End warmup as one of:

- **READY** — execution may start when separately requested/authorized;
- **BLOCKED** — a capability/precondition is unavailable;
- **DECISION REQUIRED** — a user-owned choice materially changes execution.

Include the exact blocker/decision and first runnable next step.

Do not auto-start the goal merely because warmup completed.
