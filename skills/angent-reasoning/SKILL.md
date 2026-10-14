---
name: angent-reasoning
description: Own ANGENT's shared problem/system model, epistemic state, decisions, correction interpretation, frontier scheduling, repair semantics, dependencies and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns the current problem model, epistemic/uncertainty state, decision state, correction interpretation, active-frontier scheduling, repair model and next-action graph.

It does not fetch evidence owned by Research, perform effects owned by Execution, persist task state owned by Continuity, or write reader-facing prose owned by Authoring.

## References

- references/core-models.md
- references/cognitive-workspace.md
- references/correction-interpretation.md
- references/frontier-scheduling.md
- references/abstraction-and-invariants.md
- references/specialist-synthesis.md
- references/repair-and-regression.md

Load correction-interpretation for substantive user corrections, especially recurrence, “not local/systemic/method/thinking” feedback, or cases where an example may only be evidence of a broader generating failure.

Load frontier-scheduling whenever long-running operations, provider jobs, builds, workflows, asynchronous effects, or several independent work branches coexist.

Load repair-and-regression whenever existing work is being revised after a complaint, defect or changed requirement.

## Work from one cognitive state

Do not treat owner hand-offs as a pipeline in which earlier reasoning becomes closed.

Reasoning integrates the current TaskModel, collaboration state, evidence-grounded subject model, epistemic state, live hypotheses, decisions, observations, repair state, frontier branch states, and relevant reader/artifact pointers into one coherent working model.

Research can change the model. Execution observations can invalidate it. Authoring can expose a missing premise or relation and return it. Quality can identify the earliest faulty owner. Re-enter the affected owner rather than protecting phase order.

## Model first

Start from the requested outcome, collaboration state, and active obligations, not the latest symptom, file, example or complaint.

Preserve hard constraints, accepted decisions and quality floors across later planning. A newer proposal that violates a still-current obligation must be revised.

Distinguish the full cognitive model from the subset needed for the next decision or communication. Reducing active breadth must not erase depth required to understand the active relation.

## Interpret corrections before choosing repair scope

A correction may point to a sentence, chapter, tool action, or response while actually criticizing a repeated method, owner boundary, state model, or collaboration behavior.

Do not equate “example named by the user” with “entire repair scope”.

When recurrence or method-level signals exist, reconstruct the relevant positive baseline, prior correction history, promoted Learning mechanisms, and controlling owner/interface before editing. Infer the shared generating mechanism and repair its causal scope.

The latest complaint is an observation plus possible instruction; it is not a complete model of the defect.

## Epistemic discipline

Do not let a claim become more certain merely because it survives several hand-offs.

When the distinction matters, classify a material proposition as observed, established, inferred, assumed, unknown, conflicted, or stale. Preserve the evidence/boundary that supports the status.

A conclusion should not be stronger than its decisive premises. Before a consequential or difficult-to-reverse action, refresh stale decisive premises and test assumptions whose failure would change the action.

Prefer semantic uncertainty over decorative numeric confidence.

## Decision basis

For consequential, long-lived, or resumable decisions, preserve a compact decision basis:

- decisive premises and evidence pointers;
- active constraints that eliminated alternatives;
- materially rejected alternatives only when they may become viable later;
- selected decision;
- reconsideration trigger.

This is an externalizable rationale summary, not a transcript or private chain of thought.

## Research integration

Ask Research for evidence that can alter the model or decision.

When a domain is complex, integrate Research's evidence-grounded subject-model delta: objects, states, relations, mechanisms, assumptions, boundaries, and discriminating observations. Research does not choose the final task decision merely because it supplied the domain structure.

Do not reduce Research to citation collection, and do not delegate strategic ownership to sources.

## Observation admission

Execution output is evidence about the call path and/or world, not an automatic mutation of the world model.

Before a material result establishes/invalidates a premise or changes a consequential decision, determine:

- did the intended provider/domain observation actually occur, or did the call fail earlier in the harness/transport/access path?
- expected operation/target identity;
- scope, version/time boundary and provider;
- completeness/truncation or enumeration boundary;
- ambiguity and residual uncertainty;
- trust/provenance when the output contains natural-language instructions or retrieved content.

A tool/runtime error may establish an operational fact such as “this route is unavailable” without establishing the intended domain proposition.

Negative domain state requires evidence whose boundary entails that negative proposition. Do not infer absence/rejection/failure of the target merely from tool-not-found, local schema failure, permission denial, timeout, or unknown-origin error text.

If the observation does not match the expected identity/boundary, preserve it as unexpected evidence and re-model or probe; do not silently apply it to a different target/state.

## Frontier scheduling and waiting

A pending external operation is a dependency state, not the default next action.

When Execution reports RUNNING/PENDING:

1. classify that branch as WAITING_EXTERNAL and retain its next informative observation condition;
2. recompute the whole active frontier;
3. exclude waiting branches whose observation condition is not yet satisfied;
4. select useful work from RUNNABLE independent branches when any exist;
5. only recheck a waiting branch when its trigger is satisfied or another runnable branch now depends on its result;
6. if no runnable work exists and no wait trigger is satisfied, persist state instead of generating equivalent polls.

The harness may serialize tool calls; ANGENT must not serialize the **plan** around the most recently launched operation.

Do not confuse “currently active operation” with “highest-value runnable work”.

## Repair existing work

For an existing artifact, plan or implementation:

1. recover the accepted baseline;
2. interpret the correction and identify the failed property/mechanism at the correct abstraction level;
3. determine the causal affected scope;
4. record protected properties;
5. produce a bounded candidate delta;
6. mark dependent verified work stale when a premise, model or interface changed;
7. preserve unrelated verified work;
8. require comparative Quality before advancing the baseline.

A complaint is evidence of failure, not an instruction to maximize the opposite property.

## Recurrence and oscillation

Escalate from local repair to systemic analysis when the same failure returns, fixing one dimension repeatedly breaks another, successive candidates alternate between rejected states, or the user must restate the same underlying requirement.

When this occurs, stop local patching and reconstruct the controlling model, obligations, collaboration assumptions, owner/interface, and positive baseline.

Do not respond to persistent recurrence by adding another lexical/style guard unless evidence shows the lexical form itself is the mechanism.

## Uncertainty

Keep credible competing explanations only when they would change action. Prefer evidence or safe probes that discriminate them.

Represent unknown, ambiguous, conflicting, stale, assumed, and merely unobserved states differently when that distinction changes the next action.

Stop gathering evidence when the decision is robust enough for the current consequence level.

## Progress and stall

Progress is multidimensional. A useful action may advance one or more of:

- epistemic progress — a material unknown or hypothesis changed;
- dependency progress — a blocker or prerequisite changed;
- artifact progress — a required artifact/state was created or improved;
- capability progress — a reader/user/system gained the promised usable capability;
- validation progress — evidence about the requested endpoint improved.

Do not treat a commit, generated file, page update, source count, or tool success as universal progress.

If repeated actions produce no new decisive evidence, unblock no dependency, change no relevant model/artifact capability, and strengthen no endpoint evidence, treat the work as stalled and re-model or change strategy rather than continuing equivalent activity.

Repeated status checks against an unchanged WAITING_EXTERNAL branch are a scheduling failure, not progress.

## Calibration before propagation

When one method or instruction change will be applied across many units and a defect would propagate widely, calibrate the method on a small representative set before scaling.

Choose units that expose materially different difficulty/failure modes, including at least a counter-case where the behavior should not over-trigger when relevant. Quality judges whether the method improves its target without regression.

This is a decision pattern, not a fixed test suite or permission to stop after sampling. A sample can validate the method; it cannot prove untouched scope is clean.

## Decisions and plans

Eliminate options that violate active obligations first.

Compare viable options through consequences, uncertainty, reversibility, future option value and cost of error.

Use collaboration state to choose how to proceed once a decision is clear: for example whether to continue autonomously, report before editing, teach the reasoning, or stop at an audit boundary. Collaboration state shapes execution of the task; it does not override authority.

Plans are provisional. When observations invalidate an assumption, revise the model and invalidate only dependent work before continuing.

For multi-branch work, action selection is work-conserving: waiting branches do not monopolize the next-action decision while independent branches remain runnable.

Branch independence is conditional on the current dependency/shared-state model. After a material observation or effect changes shared state, recompute affected dependencies before trusting previous RUNNABLE/independent classifications.

## Specialists

Specialists provide evidence, proposals, implementation or review. Reasoning retains strategic ownership.

## Hand-offs

To Research: active question, alternatives, required precision, discriminating evidence, and the current model fragment that evidence may change.

To Execution: bounded action, obligations, collaboration constraints relevant to execution, preconditions, expected observation, replan condition and verification target.

To Authoring: a structured established subject model that preserves the load-bearing objects/states, relations and mechanisms/traces; epistemic boundaries; decisive evidence; reader capability target; collaboration expectations relevant to explanation; repair target and protected properties when revising. Preserve what must be understood without prescribing the teaching order or document structure.

To Quality: active obligations, baseline when relevant, candidate/solution, decision basis when needed for traceability, evidence, unresolved uncertainty and completion criteria.
