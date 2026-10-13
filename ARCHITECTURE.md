# ANGENT Architecture

ANGENT is a cognitive layer for intelligent agents. Its job is to improve how an agent understands a task, reconstructs relevant state, models systems and uncertainty, seeks evidence, reasons, decides, plans, acts, adapts, verifies, communicates and learns.

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

Continuity is cross-cutting: it persists the verified frontier and reconciles ambiguous effects.

## Ownership

- **Contract**: task boundary, constraints, authorization and success semantics.
- **Context**: reconstruct only authoritative state needed now.
- **Reasoning**: problem/system model, hypotheses, causal inference, decisions, planning and replanning.
- **Research**: acquire evidence that changes decision-relevant uncertainty.
- **Execution**: perform authorized actions and return observations from real provider state.
- **Quality**: independently verify solution integrity before communication integrity.
- **Authoring**: transform established reasoning into reader-facing explanation and language.
- **Format**: preserve semantics in the destination and verify rendering.
- **Learning**: turn meaningful experience into falsifiable reusable mechanisms.
- **Continuity**: persist/resume durable task state safely.
- **Shell**: emit one compact ANGENT signature.

## Interface principle

Owners exchange semantic deltas rather than long narrative hand-offs. The canonical contracts live in `interface-contracts.md`.

The decisive loop is:

```text
Reasoning --EvidenceQuery--> Research
Reasoning <--EvidenceDelta--- Research

Reasoning --ActionNode------> Execution
Reasoning <--ObservationDelta Execution
```

This prevents source collection or tool execution from silently becoming the decision-maker.

## Architectural invariants

1. Reasoning is the sole owner of the current problem model and decision state.
2. Research cannot turn source count into a decision; it returns evidence and uncertainty.
3. Execution cannot continue a stale dependent plan after observations invalidate its assumptions.
4. Authoring cannot hide missing reasoning with fluent prose.
5. Quality cannot rewrite the candidate it judges.
6. Learning separates experience from causal explanation and only promotes transferable mechanisms.
7. Context cannot convert historical momentum into current authorization.
8. Continuity cannot treat ephemeral chat state as durable persistence.
9. Direct tasks stay direct; architecture complexity must not leak into trivial answers.

## Canonical references

Owner-specific guidance lives beside the owning Skill under `skills/angent-*/references/`.

The Root reference directory keeps only genuinely cross-cutting contracts such as:
- owner interface contracts;
- core fixtures;
- the cross-harness adapter contract.

This keeps Reasoning, Context, Continuity, Authoring and the other owners independently evolvable without turning Root into a shared instruction dump.
