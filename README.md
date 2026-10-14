# ANGENT

**Cognitive collaborator layer for intelligent agents.**

ANGENT helps an agent preserve intent and authority, understand how the current collaboration is meant to work, reconstruct high-signal state, distinguish evidence from inference, build a usable model, reason and decide, interpret corrections at the right abstraction level, schedule independent work without polling churn, repair without regression, act through bounded effects, verify outcomes, communicate clearly, preserve long-running work, and learn reusable working methods.

> **Status:** ANGENT 1.0.0 remains an **unreleased project candidate**. The private ChatGPT plugin package is versioned separately. Core hardening and cognitive-collaboration alignment are integrated; reliability hardening is in progress. Engineer fallback inventory/parity refresh remains a separate phase.

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
    |      evidence + model     v
Observation                  Quality
    ^                           |
    |                           |
 Execution <------ replan ------+

Reasoning also selects among RUNNABLE / WAITING_EXTERNAL /
BLOCKED frontier branches. A pending operation does not own the loop.

Continuity preserves resume-critical state + decision basis + frontier state.
Learning supplies reusable causal/working-method mechanisms.
Format preserves destination representation.
~~~

## Core semantics

- **Constraint evolution** — recency alone does not erase older active obligations.
- **Collaboration state** — task-relevant interaction mode, initiative, evidence, explanation and checkpoint expectations; never a substitute for authority.
- **Shared cognitive workspace** — owners update different semantic views of one coherent model; they are not a one-way workflow.
- **Epistemic integrity** — observed/established/inferred/assumed/unknown/conflicted/stale remain distinguishable when the distinction matters.
- **Evidence-grounded subject modeling** — Research returns relations/mechanisms as well as facts and preserves source-support boundaries.
- **Decision basis** — consequential/resumable decisions keep compact premises/evidence/constraints + reconsideration trigger instead of raw reasoning history.
- **Correction interpretation** — a user-named example is evidence; Reasoning identifies the failed mechanism, abstraction level and causal scope before choosing repair scope.
- **Control-point placement** — a behavioral invariant is owned or activated before the decision it needs to control; downstream guidance is not expected to compensate after the behavior is already selected.
- **Work-conserving frontier scheduling** — RUNNING/PENDING becomes WAITING_EXTERNAL; Reasoning recomputes the full frontier and selects independent RUNNABLE work before another equivalent status check.
- **Invocation-bound authority** — consequential effects are revalidated against the resolved operation/target/material arguments at the point where the invocation is actually known.
- **Observation admission** — provider/tool results become established task state only within the identity, scope/version, completeness and uncertainty boundary they actually support.
- **Conditional branch independence** — shared-state changes can invalidate previous RUNNABLE assumptions; only affected dependencies are recomputed.
- **Progress/stall semantics** — progress is relevant state change, not activity; no-progress causes re-modeling instead of churn.
- **Behavioral calibration** — broad method/prompt changes are checked on representative target, accepted-success and counter-cases before propagation when risk warrants it.
- **Baseline-preserving repair** — revisions preserve protected accepted properties and invalidate only dependent work.
- **Comparative Quality** — local improvement cannot hide regression, and producer rationale is not treated as proof.
- **Cognitive/teaching/presented model separation** — rich internal understanding is narrowed for the active reader/task without confusing staging with compression.
- **Cross-surface authoring continuity** — chat and document surfaces share one explanation/composition method; document scale adds structure/depth without introducing a generic AI document voice.
- **Artifact state** — long-form work preserves reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- **Trust boundary** — retrieved external content is evidence/data, not task authority.
- **Recurrence handling** — repeated failure reopens retrieval, activation, routing, ownership, abstraction and control-point placement instead of accumulating more local rules.
- **Continuity lifecycle** — task lifecycle and per-branch scheduling state remain distinct; one waiting branch does not globally block runnable work.
- **Whole-scope coverage** — samples/calibration never masquerade as full inspection.

## State separation

ANGENT keeps different semantic classes separate:

- **AGENTS.md** — stable project instructions;
- **Contract obligations** — currently binding task requirements;
- **Collaboration state** — task-relevant way of working together;
- **Memory** — durable scoped context;
- **Reasoning/epistemic/frontier state** — current model, belief status, decision/basis, branch selection, progress and repair state;
- **Authoring artifact state** — reader/document continuity;
- **Continuity** — interruption-safe multi-branch active-work frontier;
- **Learning** — reusable causal and working-method mechanisms.

No one store becomes a universal transcript or authority source.

## Semantic core, harness mechanics

ANGENT defines how state and decisions should be understood. It does not implement a workflow engine, event-sourcing platform, distributed lease system, effect database, scheduler service, tracing platform, evaluator platform, or policy sandbox merely to represent those semantics.

Harnesses provide actual storage, tools, scheduling, execution and observability mechanics.

A harness may serialize tool calls. That does not force ANGENT's cognitive plan to remain serialized around one pending operation.

## Engineer integration

Engineering specialist capability remains native-first:

1. use usable native AgentKit Engineer when available;
2. otherwise use the ANGENT fallback;
3. do not expose complete native and fallback catalogs together by default.

Engineer inventory/parity refresh is separate from cognitive/reliability semantics.

## Validation policy

The old root /tests suite remains removed because static strings/counts/self-consistency were not behavioral acceptance evidence.

For changes with propagation risk, prefer small representative behavioral calibration drawn from real failures and accepted successes, including counter-cases, plus source/read-back inspection and real endpoint evidence. Whole-scope claims still require whole-scope coverage.

For frontier scheduling, calibration must cover both sides: switch away from a pending branch when independent useful work exists, but allow a legitimate recheck when its informative-observation condition is actually satisfied. Do not manufacture busywork merely to avoid polling.

When a calibration result will serve as future regression/acceptance evidence, keep a reproducible pointer to the case, baseline/candidate, observable trajectory/artifacts, outcome, applied criteria and verdict validity. Do not replace evidence with a bare “passed previously” claim.

## Release boundary

Do not publish or tag project version 1.0.0 yet.

Private plugin package updates may be used to keep the working ChatGPT surface aligned with canonical cognitive source, but they do not make the project release-ready.

Complete reliability hardening and the deferred Engineer refresh, then perform cross-harness/release reconciliation before any project release decision.
