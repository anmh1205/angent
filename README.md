# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT helps an agent understand a task, reconstruct the relevant state, model systems and uncertainty, seek evidence, reason about alternatives, decide, act, verify outcomes, communicate clearly, and learn from experience.

## Core architecture

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
  └──────────────→ Reasoning
  ↓
Quality
  ↓
Authoring / Format
  ↓
Verified outcome
  ↓
Learning
```

**Continuity** is cross-cutting: it preserves resumable state and reconciles ambiguous external effects.

## Core capabilities

- **Task understanding** — separate the requested action from the underlying outcome and preserve scope, constraints, and authority.
- **State reconstruction** — recover only the authoritative user, project, task, and conversation state needed now.
- **Systems reasoning** — model components, interfaces, flows, ownership, dependencies, invariants, failure boundaries, and observability.
- **Hypothesis reasoning** — maintain competing explanations, predictions, discriminating evidence, and unresolved uncertainty.
- **Decision making** — reason from constraints, consequences, uncertainty, reversibility, and cost of being wrong.
- **Adaptive planning** — plan by dependency and information value, then replan when observations change the model.
- **Research** — seek evidence that reduces decision-relevant uncertainty instead of maximizing source count.
- **Execution** — perform authorized actions, observe real provider state, and return evidence to the reasoning loop.
- **Quality** — verify solution integrity before communication quality.
- **Authoring** — turn established reasoning into clear reader-facing explanations without using prose to hide unresolved logic.
- **Learning** — learn from corrections, failures, successful strategies, rejected hypotheses, and provider behavior.
- **Continuity** — preserve a durable frontier for long-running and side-effecting work.

## Design principles

1. Current user intent and live source truth outrank historical context.
2. Reasoning owns the current problem model and decision state.
3. Research supplies evidence; it does not substitute source collection for reasoning.
4. Execution acts on an explicit plan and returns observations for replanning.
5. Fluent output does not compensate for invalid reasoning.
6. Quality remains independent of the component that produced the candidate.
7. Learning promotes causal mechanisms, not copied complaints or project-specific wording.
8. Context never turns history into current authorization.
9. Continuity never treats ephemeral chat state as durable persistence.

## Version

Current initial release line: **1.0.0**.
