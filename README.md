# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT helps an agent preserve intent and authority, reconstruct relevant state, reason from evidence, repair existing work without regression, act through bounded effects, verify outcomes, communicate clearly, preserve long-running work, and learn reusable mechanisms.

> **Status:** ANGENT 1.0.0 remains **unreleased**. Core hardening is integrated into `main` through PR #3. Engineer fallback inventory/parity refresh is the next separate phase; the project is not release-ready yet.

## Core architecture

```text
Current instruction + active obligations + scoped context
                         ↓
                      Contract
                         ↓
              Context → Reasoning ↔ Research
                         ↓
              Decision / Repair Model
                         ↓
                Solution Quality Gate
                  ↙                 ↘
        Execution/Observation       Authoring
                  ↓                    ↓
             Reasoning/replan    Comparative Quality
                                       ↓
                              Format / external write
                                       ↓
                                Endpoint Quality
                                       ↓
                                  Verified state
                                       ↓
                                    Learning
```

Continuity is cross-cutting. It persists only resume-critical task state, accepted baseline pointers, invalidated dependent work, provider/source versions, and ambiguous effects.

## Core semantics

- **Constraint evolution** — a newer instruction may add, refine, supersede, scope, or conflict; recency alone does not erase older active obligations.
- **Baseline-preserving repair** — existing work is revised against an accepted baseline with a repair target, protected properties, affected scope, and dependency invalidation.
- **Comparative Quality** — a local fix is rejected if it regresses a protected accepted property.
- **Artifact state** — long-form work preserves reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- **Trust boundary** — retrieved external content is evidence/data, not task authority.
- **Recurrence handling** — repeated failure reopens the controlling mechanism instead of accumulating more local rules.
- **Continuity lifecycle** — active work distinguishes active, paused, blocked, completed, superseded, and abandoned state.
- **Whole-scope coverage** — pagination, truncation, filters, stale units, and unseen scope cannot be ignored when claiming a full audit.

## State separation

ANGENT keeps different semantic classes separate:

- **AGENTS.md** — stable project instructions;
- **Contract obligations** — currently binding task requirements;
- **Memory** — durable scoped context;
- **Reasoning state** — current model, decision, repair, and dependency state;
- **Authoring artifact state** — reader/document continuity;
- **Continuity** — interruption-safe active-work frontier;
- **Learning** — reusable causal mechanisms.

No one store becomes a universal transcript or authority source.

## Persistence

Local memory and Continuity use revisioned file-backed stores with conflict detection.

Continuity discovery and per-work-item recovery both scan coherent immutable revisions, so a stale convenience pointer cannot hide a newer durable frontier after an interruption.

## Engineer integration

Engineering specialist capability remains native-first:

1. use usable native AgentKit Engineer when available;
2. otherwise use the ANGENT fallback;
3. do not expose complete native and fallback catalogs together by default.

The current fallback implementation was intentionally left unchanged during core hardening. Its upstream catalog/parity refresh is the **next separate phase**, and current inventory counts must not be treated as proof of parity with the latest AgentKit release.

## Repository validation policy

The old root `/tests` suite has been removed. It mainly checked static strings, counts, and self-consistency and was not treated as evidence that ANGENT behaved correctly.

Repository CI now keeps only minimal committed-diff hygiene. Core correctness is established by coherent owner contracts, source/read-back inspection, real runtime behavior, and explicit state/evidence semantics rather than keyword/count scripts.

## Release boundary

Do not publish, tag, or update the canonical private ChatGPT plugin yet.

Core hardening is now canonical. Complete the deferred Engineer refresh next, then perform cross-harness and release-surface reconciliation before any release decision.
