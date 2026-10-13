# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT is the canonical source for the system previously developed as Cogent. It is being redesigned around a stronger cognitive core: task understanding, system modeling, reasoning, evidence-seeking, decision-making, adaptive planning, execution, verification, communication, continuity, and learning.

## Core architecture

```text
Intent
  ↓
Contract ── Context
  ↓
Reasoning ↔ Research
  ↓
Decision / Adaptive Plan
  ↓
Execution
  ↓
Verification
  ↓
Learning

Authoring and Format turn validated models and evidence into reader-facing artifacts.
Continuity preserves resumable state across long-running work.
```

## Design principles

- Current user intent and live source truth outrank historical context.
- Reasoning owns problem/system models, hypotheses, causal inference, decisions, planning, and replanning.
- Research seeks discriminating evidence; it does not substitute source collection for reasoning.
- Execution acts on an explicit state/plan and returns observations to reasoning.
- Quality verifies solution integrity before communication quality.
- Authoring remains an integrated explanation engine rather than a chain of competing editors.
- Learning promotes causal mechanisms only when evidence supports transfer beyond the original incident.
- Continuity never pretends a chat transcript is a durable checkpoint.

## Status

This repository is the canonical source for the ANGENT redesign. The first major milestone migrates the useful Cogent 16 capabilities and introduces the new Reasoning Core.
