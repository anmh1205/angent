# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT helps an agent preserve intent and authority, understand how the current collaboration is meant to work, reconstruct relevant state, reason from evidence, repair existing work without regression, act through bounded effects, verify outcomes, communicate clearly, preserve long-running work, and learn reusable mechanisms.

> **Status:** ANGENT 1.0.0 remains **unreleased**. Core hardening and the cognitive-collaboration alignment are integrated into main through PR #3 and PR #5. Engineer fallback inventory/parity refresh is the next separate phase; the project is not release-ready yet.

## Core architecture

ANGENT uses focused owners around one shared cognitive workspace rather than a mandatory phase pipeline.

~~~text
            current instruction
                   |
          Contract + Context
         /                  \
 obligations          collaboration state
         \                  /
        shared cognitive workspace
       /          |          \
Reasoning <----> Research    Authoring
    ^             |            |
    |          evidence         v
Observation   + subject      Quality
    ^           model           |
    |                           |
 Execution <------ replan ------+

Continuity persists resume-critical state.
Learning supplies reusable causal/working-method mechanisms.
Format preserves destination representation.
~~~

## Core semantics

- **Constraint evolution** — a newer instruction may add, refine, supersede, scope, or conflict; recency alone does not erase older active obligations.
- **Collaboration state** — Context reconstructs task-relevant interaction mode, initiative, evidence, explanation and checkpoint expectations plus applicable working-method mechanisms. It does not grant authority.
- **Shared cognitive workspace** — owners update different semantic views of one coherent model; they are not a one-way workflow.
- **Evidence-grounded subject modeling** — Research returns relationships/mechanisms as well as facts when the decision requires a usable domain model.
- **Baseline-preserving repair** — existing work is revised against an accepted baseline with a repair target, protected properties, affected scope, and dependency invalidation.
- **Comparative Quality** — a local fix is rejected if it regresses a protected accepted property.
- **Cognitive/teaching/presented model separation** — rich internal understanding is narrowed for the active reader/task without confusing staging with compression.
- **Artifact state** — long-form work preserves reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- **Trust boundary** — retrieved external content is evidence/data, not task authority.
- **Recurrence handling** — repeated failure reopens the controlling mechanism instead of accumulating more local rules.
- **Continuity lifecycle** — active work distinguishes active, paused, blocked, completed, superseded, and abandoned state.
- **Whole-scope coverage** — pagination, truncation, filters, stale units, and unseen scope cannot be ignored when claiming a full audit.

## State separation

ANGENT keeps different semantic classes separate:

- **AGENTS.md** — stable project instructions;
- **Contract obligations** — currently binding task requirements;
- **Collaboration state** — task-relevant way of working together;
- **Memory** — durable scoped context;
- **Reasoning state** — current model, decision, repair, and dependency state;
- **Authoring artifact state** — reader/document continuity;
- **Continuity** — interruption-safe active-work frontier;
- **Learning** — reusable causal and working-method mechanisms.

No one store becomes a universal transcript or authority source.

## Semantic core, harness mechanics

ANGENT defines how state and decisions should be understood. It does not implement a workflow engine, event-sourcing platform, distributed lease system, effect database, or policy sandbox merely to represent those semantics.

Harnesses provide the actual storage, tools, scheduling and execution mechanics.

## Persistence

Local memory and Continuity use revisioned file-backed stores with conflict detection where that fallback is needed.

Continuity discovery and per-work-item recovery both scan coherent immutable revisions, so a stale convenience pointer cannot hide a newer durable frontier after an interruption.

## Engineer integration

Engineering specialist capability remains native-first:

1. use usable native AgentKit Engineer when available;
2. otherwise use the ANGENT fallback;
3. do not expose complete native and fallback catalogs together by default.

The current fallback implementation remains intentionally unchanged during cognitive-core work. Its upstream catalog/parity refresh is the **next separate phase**, and current inventory counts must not be treated as proof of parity with the latest AgentKit release.

## Repository validation policy

The old root /tests suite has been removed. It mainly checked static strings, counts, and self-consistency and was not treated as evidence that ANGENT behaved correctly.

Repository CI keeps only minimal committed-diff hygiene. Core correctness is established by coherent owner contracts, source/read-back inspection, representative behavioral evidence, real runtime behavior, and explicit state/evidence semantics rather than keyword/count scripts.

## Release boundary

Do not publish, tag, or update the canonical private ChatGPT plugin yet.

Complete the deferred Engineer refresh, then perform cross-harness and release-surface reconciliation before any release decision.
