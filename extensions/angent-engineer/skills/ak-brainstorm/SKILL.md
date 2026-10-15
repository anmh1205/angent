---
name: ak-brainstorm
description: Turn incomplete delivery intent into an accepted outcome contract and compare materially different approaches before planning or implementation.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Brainstorm — Portable Fallback

Use at the opening of multi-step delivery or after diagnosis when several materially different solutions remain.

Do not invoke a design interview for a direct answer/read-only utility or when an accepted contract already settles the relevant choices.

## Opening contract

Capture or reuse:
- **Outcome** — user-visible/operational end state;
- **Constraints** — safety, compatibility, time, technology, ownership;
- **Non-goals** — adjacent work this delivery will not absorb;
- **Acceptance criteria** — observable evidence that proves completion.

If an accepted brief/plan already contains these, reuse it and resolve only material gaps.

## Proportional behavior

- Concrete request → summarize the contract briefly and continue.
- Ask only when a missing answer changes outcome, safety, public contract or architecture and cannot be discovered.
- Explicit autonomous mode does not require routine approval once the contract is concrete.
- Resolve discoverable uncertainty from repository/docs/provider evidence instead of asking the user to restate facts.
- Preserve uncertainty that is genuinely future/external/user-owned.

## Bug path

For a failure:
1. frame expected repaired behavior, constraints, non-goals and acceptance;
2. Scout the affected path;
3. Debug/prove root cause;
4. compare cause-aligned repairs only if a real choice remains;
5. hand the accepted direction to Fix.

Brainstorm must not choose fixes from symptoms.

## Option exploration

When a real design choice exists:

1. inspect the smallest relevant source/docs/tests/current plans;
2. establish constraints/evidence gaps;
3. produce up to a few materially distinct mechanisms, not cosmetic variants;
4. for each, state decisive assumption, first failure condition, meaningful cost/trade-off, migration/switching cost when relevant;
5. eliminate options violating active constraints;
6. prefer the smallest approach satisfying the **full accepted scope**;
7. resolve a user-owned choice before implementation.

Do not silently cut requested scope in the name of YAGNI. Scope reduction is an explicit opt-in or user instruction.

## Optional modes

- **advice** — use an independent advisor to pressure-test a high-risk/stuck decision; advice never owns the final decision or effect.
- **html brief** — when requested, produce a self-contained visual decision brief containing the contract, approaches, recommendation, implementation flow, and UI mockups when the problem is visual.
- **YAGNI opt-in** — challenge/cut scope not needed for the accepted outcome, while still surfacing any blocking missing scope.

These are optional outputs/decision aids, not permission to mutate product code.

## Handoff

Pass to Plan/Cook/Fix:
- the four contract fields;
- selected direction;
- decisive evidence/assumptions;
- unresolved risks/decisions;
- YAGNI/scope mode only when explicitly selected.

Write a durable brief only when it must survive the session or feed downstream planning.

## Boundary

Brainstorm shapes intent and solution choices. It does not implement the solution.

Never infer current product behavior from intent alone, and never expose secrets/unrelated private data during evidence gathering.
