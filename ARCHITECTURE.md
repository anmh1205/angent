# ANGENT Architecture

ANGENT is a cognitive layer for agents. Its purpose is not to add process around a model; it is to improve how an agent forms the task model, reasons under uncertainty, chooses actions, adapts to observations, verifies outcomes, communicates, and learns.

## Cognitive loop

```text
Intent
  ↓
Contract ← Context
  ↓
Reasoning ↔ Research
  ↓
Decision / Adaptive Plan
  ↓
Execution
  ↓
Observation
  └──────────────→ Reasoning (update / replan)
  ↓
Quality
  ↓
Authoring / Format when a reader-facing artifact is required
  ↓
Verified outcome
  ↓
Learning
```

Continuity is cross-cutting: it preserves a resumable frontier and reconciles ambiguous effects.

## Ownership

- **Contract**: outcome, boundaries, authorization, success semantics.
- **Context**: reconstruct only the authoritative state needed now.
- **Reasoning**: problem/system models, hypotheses, causal reasoning, decisions, planning and replanning.
- **Research**: targeted evidence acquisition and epistemic state.
- **Execution**: authorized action, observation, retries, provider reconciliation.
- **Quality**: independent solution-integrity and communication-integrity gate.
- **Authoring**: integrated reader model, concept staging, representation and language realization.
- **Format**: destination fidelity and render verification.
- **Learning**: turn failures and successes into falsifiable reusable mechanisms.
- **Continuity**: durable checkpoint protocol and safe resume.
- **Shell**: one compact ANGENT signature.

## Architectural invariants

1. Reasoning is the sole owner of the current problem model and decision state.
2. Research does not decide merely because it found sources; it updates evidence and uncertainty.
3. Execution does not invent strategy when observations invalidate the current plan; it returns evidence for replanning.
4. Authoring cannot hide missing reasoning with fluent prose.
5. Quality does not rewrite the candidate it judges.
6. Learning separates observations from explanations and promotes mechanisms only with transferable support.
7. Context never converts historical momentum into current authorization.
8. Continuity never treats ephemeral chat state as durable persistence.
