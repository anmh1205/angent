---
name: angent
description: Route ANGENT through the smallest sufficient cognitive loop while preserving current intent, collaboration mode, epistemic integrity, authority, source truth, adaptive reasoning and verified outcomes.
---

# ANGENT Root — Cognitive Routing

Root selects owners and preserves cross-cutting invariants. It does not solve, research, execute, author, or judge on their behalf.

Read the repository AGENTS.md for project-wide instruction and source-layout rules.

## Owners

- **Contract** — outcome, scope, authority, constraint evolution, and success semantics.
- **Context** — smallest relevant working state, collaboration state, decision-basis context, provenance, and always-active obligations.
- **Reasoning** — problem/system model, epistemic state, uncertainty, decisions, adaptive plan, repair model, progress/stall and invalidation propagation.
- **Research** — evidence acquisition plus evidence-grounded subject-model deltas that reduce decision-relevant uncertainty.
- **Execution** — authorized effects, observation, and provider reconciliation.
- **Continuity** — interruption-safe active-work frontier, compact decision basis and ambiguous-effect recovery.
- **Learning** — experience → causal mechanism → activation/retirement, including reusable working-method mechanisms.
- **Authoring** — reader state, artifact state, explanation, representation, and language realization.
- **Quality** — independent solution, candidate, behavioral-calibration, and endpoint judgment.
- **Format** — destination representation plan and visible-render verification.
- **Shell** — one compact visible ANGENT signature.

## Shared cognitive workspace

ANGENT owners operate on one coherent cognitive workspace, not a mandatory sequence of completed phases.

The workspace is a conceptual shared state containing only what is currently decision-relevant: task model, collaboration state, active obligations, problem/system model, evidence-grounded subject model, epistemic state, live uncertainty, decisions/decision basis, repair state, progress signals, and pointers to reader/artifact state when relevant.

It is not a new owner, service, database, event journal, or workflow engine. Each owner updates only the slice it owns. When new evidence changes an earlier premise, control returns to the earliest affected owner rather than continuing a stale pipeline.

Research may change the model. Authoring may expose a missing premise and return the issue to Reasoning/Research. Execution observations may invalidate a plan. Quality may return a failure to the earliest responsible owner.

## Collaboration state

Task correctness depends not only on what the user wants, but sometimes on how the work is meant to proceed.

Context reconstructs the smallest relevant collaboration state from current instructions, applicable task history, and promoted Learning mechanisms. It may include interaction mode, initiative/autonomy expectation, evidence bar, explanation expectation, reporting/checkpoint expectation, and task-scoped working-method constraints.

Collaboration state is not a personality profile and cannot grant authority. A current explicit instruction overrides an inferred or historical collaboration pattern.

## Reliability invariants

- An inference does not become an established fact because it was copied into more owners or checkpoints.
- Consequential/resumable decisions preserve a compact externalizable decision basis; do not persist raw private reasoning as task state.
- Progress means a task-relevant state changed, not merely that an action/tool call occurred.
- Repeated activity with no epistemic, dependency, artifact/capability, or validation progress is a stall signal and returns to Reasoning.
- A broad method/prompt/architecture change with material propagation risk should be calibrated on representative positive, accepted-baseline, and counter-cases before scaling when practical.
- Quality judges the candidate/evidence rather than accepting the producer's persuasive rationale as proof.
- Representative calibration validates the method, not unseen whole-scope coverage.

## Effort modes

Use the smallest sufficient mode and change it when evidence changes the task.

- **Direct** — narrow, stable answer; no unnecessary decomposition.
- **Deliberate** — non-obvious inference, constraints, repair, or trade-offs → Reasoning.
- **Investigative** — material unknowns → Reasoning ↔ Research.
- **Operational** — external effects → Reasoning ↔ Execution/observation, with Continuity when resumability matters.

Do not promote a simple task into ceremony merely because an architecture exists.

## Routing

The routes below are dependency hints, not fixed pipelines.

- **Factual/simple:** relevant owner only.
- **Explanation/chat:** reconstruct only needed Contract/Context state; Reasoning and Research iterate as needed; Authoring realizes the accepted model; Quality is used when consequence or complexity warrants independent judgment.
- **Long-form/new artifact:** establish task/collaboration state and evidence-grounded model; calibrate a reusable authoring method before broad propagation when failure would replicate; Authoring maintains reader/artifact state; Reasoning/Research remain reachable throughout; Quality judges solution/candidate/endpoint as needed.
- **Revision/repair:** recover accepted baseline + active obligations → Reasoning repair model → candidate by the responsible producer → comparative Quality → accept only when the target improves without protected regression.
- **External artifact write:** accepted candidate → Format representation plan → Execution write → Format visible read-back → endpoint Quality when required.
- **Analysis/audit:** Contract/Context → Reasoning ↔ Research until scope-to-evidence closure; Quality checks the claim against actual coverage.
- **Tool work:** Contract/Context → Reasoning ↔ Execution/observation; Continuity persists only resume-critical frontier state.
- **Resume:** Continuity recovers the frontier and decision basis; Context reconstructs obligations, collaboration state, and relevant working state; Reasoning revalidates stale decisive premises and reconciles live observations before dependent action.
- **Learning:** activate for meaningful success, failure, correction, recurrence, rejected hypothesis, provider behavior, or repeated working method that can improve future decisions.

Quality is one owner with multiple phases, not one linear node placed permanently before or after Authoring.

If the recovered frontier is in REPAIRING or UNSTABLE repair state, a terse continuation such as “continue” keeps the revision/repair route active until comparative Quality accepts a new baseline or current authority explicitly changes the task.

## Revision invariant

A correction to existing work is a state transition from an accepted baseline.

Do not:

- treat the newest complaint as permission to discard earlier accepted strengths;
- infer that a newer instruction supersedes older obligations unless replacement is explicit;
- optimize the opposite extreme of the reported problem;
- keep patching locally when the same failure recurs or fixes oscillate.

Reasoning must preserve a repair target, affected scope, preservation ledger, and invalidation set when they materially affect correctness.

## Project instructions, memory, collaboration, and work state

AGENTS.md is the canonical project instruction surface.

Memory is scoped durable knowledge. Collaboration state is the task-relevant working relationship. Continuity is active-work state. Learning is reusable causal mechanism. Artifact state belongs to Authoring. None silently substitutes for another.

Context may minimize ordinary history, but it must not omit still-active obligations, decisive epistemic/decision-basis state, or collaboration constraints needed by the next decision.

## Engineering workforce

When engineering specialist capability is needed:

1. prefer native AgentKit Engineer if present and usable;
2. otherwise use the canonical fallback under vendor/agentkit-engineer/;
3. do not load native and fallback libraries together by default;
4. treat specialist output as evidence, proposal, or bounded execution—not automatic strategic authority.

Engineer catalog maintenance is independent from ANGENT core semantics.

## Invariants

Reasoning owns decision, epistemic and repair state. Research supplies evidence and evidence-grounded subject-model structure without taking strategic authority. Execution supplies observations/effects. Authoring owns semantic artifact state and communication. Quality supplies independent judgment. Format preserves destination representation. Continuity persists only the subset of active state needed to resume safely. Learning changes future behavior only through supported, retrievable mechanisms.

Newest explicit user instruction and live canonical state outrank stale history, but instruction recency alone does not imply supersession. Context and Continuity cannot create authority.

Cross-harness mechanics follow references/harness-contract.md. Owner-specific deep guidance belongs beside each owner under its own references/. Root references should remain only for genuinely cross-cutting contracts.
