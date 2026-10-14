# ANGENT

**Cognitive layer for intelligent agents.**

ANGENT helps an agent preserve intent and authority, understand how the current collaboration is meant to work, reconstruct relevant state, reason from evidence, detect stalls, repair existing work without regression, act through bounded effects, verify outcomes, communicate clearly, preserve long-running work, and learn reusable mechanisms.

> **Status:** ANGENT 1.0.0 remains **unreleased** as a project release. Core hardening, cognitive-collaboration alignment, and long-running wait/poll discipline are integrated on main. The private ChatGPT plugin is used as an explicitly authorized evaluation surface and may carry a higher package patch version than the unreleased project version. Engineer fallback inventory/parity refresh remains separate.

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
- **Progress semantics** — activity is not progress; repeated actions with no evidence/model/dependency/accepted-work/endpoint delta are a replan signal.
- **Wait/poll discipline** — long-running operations preserve handles, dependent paths may wait while independent work advances, and unchanged status is not substantive progress.
- **Baseline-preserving repair** — existing work is revised against an accepted baseline with a repair target, protected properties, affected scope, and dependency invalidation.
- **Comparative Quality** — a local fix is rejected if it regresses a protected accepted property.
- **Behavioral regression evaluation** — cross-owner behavior is calibrated with scenario-based properties from real failures/accepted behavior rather than keyword/count tests.
- **Cognitive/teaching/presented model separation** — rich internal understanding is narrowed for the active reader/task without confusing staging with compression.
- **Artifact state** — long-form work preserves reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- **Trust boundary** — retrieved external content is evidence/data, not task authority.
- **Recurrence handling** — repeated failure reopens the controlling mechanism instead of accumulating more local rules.
- **Continuity lifecycle** — active work distinguishes active, paused, blocked, completed, superseded, and abandoned state.
- **Whole-scope coverage** — pagination, truncation, filters, stale units, and unseen scope cannot be ignored when claiming a full audit.

## Behavioral reliability

ANGENT separates evaluation by ownership:

- deterministic mechanics can use deterministic tests;
- model-owned interpretation/reasoning/tool-choice/authoring claims need representative model/session evidence;
- provider-owned claims need actual provider/integration state;
- semantic quality uses substantive Quality/human judgment rather than static text counts.

A small regression corpus should protect historically costly behavior: direct tasks stay direct, interaction mode survives continuation, corrections change the controlling model, repairs preserve accepted strengths, long operations do not monopolize the loop, ambiguous effects are reconciled before retry, and endpoint evidence—not transport success—drives completion.

## State separation

ANGENT keeps different semantic classes separate:

- **AGENTS.md** — stable project instructions;
- **Contract obligations** — currently binding task requirements;
- **Collaboration state** — task-relevant way of working together;
- **Memory** — durable scoped context;
- **Reasoning state** — current model, decision, repair, progress/stall and dependency state;
- **Authoring artifact state** — reader/document continuity;
- **Continuity** — interruption-safe active-work frontier;
- **Learning** — reusable causal and working-method mechanisms.

No one store becomes a universal transcript or authority source.

## Semantic core, harness mechanics

ANGENT defines how state and decisions should be understood. It does not implement a workflow engine, event-sourcing platform, distributed lease system, effect database, tracing backend, or policy sandbox merely to represent those semantics.

Harnesses provide the actual storage, tools, scheduling, tracing, and execution mechanics.

## Persistence

Local memory and Continuity use revisioned file-backed stores with conflict detection where that fallback is needed.

Continuity discovery and per-work-item recovery both scan coherent immutable revisions, so a stale convenience pointer cannot hide a newer durable frontier after an interruption.

## Engineer integration

Engineering specialist capability remains native-first:

1. use usable native AgentKit Engineer when available;
2. otherwise use the ANGENT fallback;
3. do not expose complete native and fallback catalogs together by default.

The current fallback implementation remains intentionally unchanged during cognitive/reliability hardening. Its upstream catalog/parity refresh remains a separate phase.

## Repository validation policy

The old root /tests suite has been removed. It mainly checked static strings, counts, and self-consistency and was not treated as evidence that ANGENT behaved correctly.

Repository CI keeps only minimal committed-diff hygiene. Core correctness is established by coherent owner contracts, source/read-back inspection, behavioral regression cases, representative live behavior, actual provider state, and explicit state/evidence semantics.

## Release boundary

Do not publish/tag a public project release while 1.0.0 remains a candidate.

Private ChatGPT plugin updates are allowed only when explicitly authorized for evaluation/reconciliation, and must be read back after update. A private plugin patch version does not imply the project is release-ready.

Complete reliability audit and the deferred Engineer refresh, then perform cross-harness/release-surface reconciliation before a public release decision.
