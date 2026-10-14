---
name: ak-autoresearch
description: Route a measurable optimization, prediction, scenario, or security objective to the installed workflow that owns the loop, with a bounded evidence contract.
metadata: {port: angent-fallback, mode: adapted}
---

# Autoresearch — Portable Fallback

Use when the user has a measurable objective but the correct iterative workflow is not yet clear.

Autoresearch is a router, not a universal self-improvement loop.

## Contract

Establish:
- objective and why it matters;
- mechanical metric or observable success state;
- baseline;
- guard conditions;
- allowed change/search surface;
- iteration/time/cost bound when relevant;
- stop condition;
- authority boundary.

Reject or reframe proxy metrics that no longer represent the real objective.

## Route

Discover the live fallback/installed catalog, then route by outcome:
- measurable optimization/experiment → `ak-loop`;
- prediction → `ak-predict`;
- scenario exploration/coverage → `ak-scenario`;
- bounded security review/iteration → `ak-security`;
- another installed owner when it clearly fits better.

If no installed Skill owns the objective, return blocked with the closest normal workflow for approval rather than fabricating a loop.

## Handoff

Pass the accepted metric/baseline/guards/bounds/evidence state to the selected owner.

From that point the selected Skill owns its artifacts and completion rules.

Autoresearch does not weaken effect authority, hide failed iterations, or claim convergence.
