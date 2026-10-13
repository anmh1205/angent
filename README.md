# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT helps an agent understand the requested outcome, reconstruct the relevant working state, model systems and uncertainty, seek evidence, decide, act, verify, communicate clearly, preserve long-running work, and learn from experience.

> **Status:** 1.0.0 is an **unreleased merged candidate**. Implementation, integration review, cross-harness acceptance, and representative Authoring/Quality acceptance are complete; publication remains a separate explicit release action.

## Architecture

```text
Current instruction + AGENTS.md + scoped context
                    ↓
                 Contract
                    ↓
       Context → Reasoning ↔ Research
                    ↓
          Decision / Adaptive Plan
                    ↓
                Execution
                    ↓
               Observation
                    └────────→ Reasoning / replan
                    ↓
                 Quality
                    ↓
            Authoring / Format

Cross-cutting:
- Continuity — active-work frontier and ambiguous-effect recovery
- Learning — experience → causal mechanism → reusable guidance
```

## Core capabilities

- **Task understanding** — separate requested action, underlying objective, constraints, authority, and success state.
- **Context reconstruction** — assemble only the current high-signal working set from instruction, active task state, AGENTS.md, scoped memory, and authoritative sources.
- **Systems reasoning** — model components, interfaces, ownership, flows, dependencies, invariants, failure boundaries, and observability.
- **Hypothesis reasoning** — preserve credible alternatives until evidence separates them.
- **Decision making** — reason from constraints, consequences, uncertainty, reversibility, and cost of error.
- **Adaptive planning** — plan by dependency and information value, then revise the model/plan when observations invalidate assumptions.
- **Research** — acquire the smallest evidence set that can change the current decision.
- **Execution** — perform authorized actions, observe real state, and reconcile uncertain external effects.
- **Quality** — verify solution/outcome integrity before communication quality.
- **Authoring** — create coherent chat and long-form explanations from established reasoning.
- **Learning** — learn reusable causal mechanisms from meaningful success, failure, correction, and specialist/runtime evidence.
- **Continuity** — proactively preserve active-work frontier across interruption instead of waiting for a predicted disconnect.

## Project instructions and memory

`AGENTS.md` is the canonical project instruction surface.

ANGENT intentionally separates:

- **AGENTS.md** — stable project instructions and conventions;
- **Memory** — scoped dynamic knowledge that survives sessions;
- **Continuity** — the active frontier of work in progress;
- **Learning** — promoted reusable mechanisms.

Local memory is designed around **capture → synthesis/update → scoped retrieval**, not append-only notes.

For local harnesses, ANGENT now includes small revisioned file backends for scoped memory and Continuity. They provide atomic persistence and stale-writer conflict detection while leaving semantic synthesis/reconciliation to Context and Continuity.

## Skill architecture

ANGENT uses progressive disclosure.

Each owner Skill keeps its operating model in `SKILL.md` and deeper guidance in owner-local `references/`. Deterministic helpers belong in `scripts/` only when they add real value.

This keeps the core understandable without loading every rule/reference into every task.

## AgentKit Engineer integration

ANGENT uses a **native-first / port-fallback** strategy for engineering specialist capability.

- If AgentKit Engineer is installed and usable, prefer the native upstream Skills/Agents.
- If native Engineer is unavailable or unusable, expose the canonical fallback under `vendor/agentkit-engineer/`.
- Native and fallback libraries are not loaded together by default.
- The fallback is packaged as a **companion plugin root** with portable Agent Plugins and ChatGPT/Codex manifests pointing to one Skill tree.
- The fallback port preserves workflow behavior while replacing AgentKit/Claude-specific runtime dependencies.
- The active harness proves native Engineer visibility; an `ak` binary or cache alone is not enough.

The ANGENT fallback now has **102/102 Engineer Skill targets implemented and 16/16 portable Agent roles**. Native AgentKit usage remains the preferred path when usable; the fallback exists so ANGENT retains the complete engineering capability surface when AgentKit is unavailable. The fallback is an independent portable implementation, not a raw upstream mirror. See `vendor/agentkit-engineer/PORTING_MANIFEST.md`.

## Design principles

1. Current explicit user intent and current authority outrank historical momentum.
2. Reasoning owns the decision state; specialists provide evidence, proposals, or bounded execution.
3. Research reduces decision-relevant uncertainty instead of maximizing source count.
4. Execution verifies real effects and never blindly replays ambiguous non-idempotent writes.
5. Continuity stores the meaning/progress of active work; provider state is used for reconciliation.
6. Context retrieves the smallest relevant working set rather than dumping history/memory.
7. Learning promotes causal mechanisms, not copied complaints or one-off examples.
8. Authoring preserves reader-state progression and representation fidelity.
9. Quality remains independent from the producer it evaluates.
10. A progress token is not the requested endpoint unless the Contract defines it that way.

## Version status

Current line: **1.0.0 — merged, validated, unreleased**.

The implementation/acceptance gates for the 1.0.0 candidate have completed and the upgrade is on `main`. Do not publish, tag, or describe 1.0.0 as released until an explicit release decision is made from the exact merged source and the intended release surface is verified.
