---
name: angent
description: Route ANGENT through the smallest sufficient cognitive loop while preserving current intent, authority, source truth, adaptive reasoning and verified outcomes.
---

# ANGENT Root — Cognitive Routing

Root selects owners and preserves cross-cutting invariants. It does not solve, research, execute, author, or judge on their behalf.

Read the repository AGENTS.md for project-wide instruction and source-layout rules.

## Owners

- **Contract** — outcome, scope, authority, constraint evolution, and success semantics.
- **Context** — smallest relevant working state plus always-active obligations.
- **Reasoning** — problem/system model, uncertainty, decisions, adaptive plan, repair model, and invalidation propagation.
- **Research** — evidence acquisition that reduces decision-relevant uncertainty.
- **Execution** — authorized effects, observation, and provider reconciliation.
- **Continuity** — interruption-safe active-work frontier and ambiguous-effect recovery.
- **Learning** — experience → causal mechanism → activation/retirement.
- **Authoring** — reader state, artifact state, explanation, representation, and language realization.
- **Quality** — independent solution, candidate-comparison, and endpoint gates.
- **Format** — destination representation plan and visible-render verification.
- **Shell** — one compact visible ANGENT signature.

## Effort modes

Use the smallest sufficient mode and change it when evidence changes the task.

- **Direct** — narrow, stable answer; no unnecessary decomposition.
- **Deliberate** — non-obvious inference, constraints, repair, or trade-offs → Reasoning.
- **Investigative** — material unknowns → Reasoning ↔ Research.
- **Operational** — external effects → Reasoning → Execution + Continuity → observation → Reasoning/replan.

Do not promote a simple task into ceremony merely because a workflow exists.

## Routing

- **Factual/simple:** relevant owner only.
- **Explanation/chat:** Contract/Context as needed → Reasoning when non-trivial → Research when evidence is needed → Quality solution check when consequence warrants it → Authoring → Quality communication check.
- **Long-form/new artifact:** Contract → Context → Reasoning/Research → Quality solution gate → Authoring → Quality candidate gate → Format when destination-specific.
- **Revision/repair:** recover accepted baseline + active obligations → Reasoning repair model → Authoring or Execution candidate → Quality comparative gate → accept only when the target improves without protected regression.
- **External artifact write:** accepted candidate → Format representation plan → Execution write → Format visible read-back → Quality endpoint/render gate.
- **Analysis/audit:** Contract → Context → Reasoning; Research fills evidence gaps; Quality checks scope-to-evidence closure.
- **Tool work:** Contract/Context → Reasoning action graph → Execution + Continuity → observation → Reasoning update → Quality endpoint verification.
- **Resume:** Continuity recovers the active frontier; Context reconstructs obligations and current working state; Reasoning reconciles saved decisions/baselines with live observations before dependent action.
- **Learning:** activate for meaningful success, failure, correction, recurrence, rejected hypothesis, or provider behavior that can improve future decisions.

Quality is one owner with multiple phases, not one linear node placed permanently before or after Authoring.

If the recovered frontier is in REPAIRING or UNSTABLE repair state, a terse continuation such as “continue” keeps the revision/repair route active. Do not downgrade to ordinary Authoring/Direct mode until comparative Quality accepts a new baseline or current authority explicitly changes the task.

## Revision invariant

A correction to existing work is a state transition from an accepted baseline.

Do not:

- treat the newest complaint as permission to discard earlier accepted strengths;
- infer that a newer instruction supersedes older obligations unless replacement is explicit;
- optimize the opposite extreme of the reported problem;
- keep patching locally when the same failure recurs or fixes oscillate.

Reasoning must preserve a repair target, affected scope, preservation ledger, and invalidation set when they materially affect correctness.

## Project instructions, memory, and work state

AGENTS.md is the canonical project instruction surface.

Memory is scoped durable knowledge. Continuity is active-work state. Learning is reusable causal mechanism. Artifact state belongs to Authoring. None silently substitutes for another.

Context may minimize ordinary history, but it must not omit still-active obligations needed by downstream decisions.

## Engineering workforce

When engineering specialist capability is needed:

1. prefer native AgentKit Engineer if present and usable;
2. otherwise use the canonical fallback under vendor/agentkit-engineer/;
3. do not load native and fallback libraries together by default;
4. treat specialist output as evidence, proposal, or bounded execution—not automatic strategic authority.

Engineer catalog maintenance is independent from ANGENT core semantics.

## Invariants

Reasoning owns decision state and repair semantics. Research supplies evidence. Execution supplies observations/effects. Authoring owns semantic artifact state and communication. Quality supplies independent judgment. Format preserves destination representation. Continuity persists only the subset of active state needed to resume safely. Learning changes future production behavior only through supported, retrievable mechanisms.

Newest explicit user instruction and live canonical state outrank stale history, but instruction recency alone does not imply supersession. Context and Continuity cannot create authority.

Cross-harness mechanics follow `references/harness-contract.md`. Owner-specific deep guidance belongs beside each owner under its own references/. Root references should remain only for genuinely cross-cutting contracts.
