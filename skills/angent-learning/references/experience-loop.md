# Experience loop

## Candidate experience

Capture only events with plausible future value: correction, failure, success, rejected hypothesis, provider behavior, repeated decision pattern, repeated working-method pattern, review finding, or specialist evidence.

## Reconstruction

Preserve:
- context/task class;
- decision/action taken;
- observed outcome;
- evidence/source pointer;
- expected outcome;
- material difference.

When the event is a correction, also preserve whether the user's named example was local evidence or a signal of a broader method/owner failure.

## Mechanism

A useful mechanism predicts another case instead of restating the symptom.

Weak: “too many bullets make writing bad.”

Stronger: “when propositions have dependency/causal flow, flattening them into peer bullets removes relational structure and increases reader reconstruction cost.”

Weak: “the user dislikes the phrase ‘Điểm quan trọng là’.”

Stronger: “when authoring inserts meta-teaching commentary that announces significance instead of advancing the technical model, prose becomes generic/AI-shaped and paragraph cohesion weakens.”

Likewise, avoid turning collaboration history into preferences without a causal model.

Weak: “the user prefers autonomous work.”

Stronger: “for already-authorized multi-step work with clear next actions, repeated routine confirmations interrupt the critical path without reducing material risk; continue until a real decision, authority, or safety boundary.”

Weak: “poll less while a process runs.”

Stronger: “when a wait/poll invariant is encoded only in the downstream owner that performs status checks, it cannot reliably prevent the upstream planner from selecting the same pending branch again. Put the controlling invariant at the earliest owner that chooses the behavior, and let downstream owners report the state needed for that choice.”

## Control-point placement

A reusable rule must be owned or activated at the earliest decision point that can actually prevent the failure.

If a behavior is selected by Reasoning/Root before Execution sees it, an Execution-only rule cannot reliably govern that selection.

If correction scope is chosen before Authoring receives a candidate, an Authoring-only rule cannot prevent local-patch routing.

If accepted work can advance before Quality is consulted, a Quality-only statement cannot protect the baseline.

When a rule exists but failure recurs, ask not only “was it retrieved?” but also:

- Was it active before the controlling decision?
- Is it owned by a component with authority over that decision?
- Does the upstream interface expose the state needed to apply it?
- Is a downstream owner being asked to compensate after the behavior has already been chosen?

Prefer moving the invariant to the real control point over duplicating stronger wording across every downstream skill.

A related timing failure occurs when a decision is valid when planned but stale when committed. If target, arguments, authority, dependency state or provider state can change between planning and execution, the controlling invariant must be revalidated at the boundary where those concrete values are known.

Likewise, a tool result should not become established state merely because it arrived after an authorized call. Observation identity, scope/version, completeness and uncertainty determine what the result can safely update.

## Prompt-accumulation failure

A correct mechanism can still degrade ANGENT if every discovered lesson is copied into the always-visible bootstrap.

When reliability rules accumulate:
- keep genuinely cross-cutting invariants always active;
- move decision-class-specific detail to the owner/reference that controls the behavior;
- add an activation condition at Root/Context instead of duplicating the full rule globally;
- use activation evidence when later recurrence diagnosis needs to know whether the mechanism ran.

Do not equate “important” with “must occupy every prompt”. The objective is reliable activation with minimal irrelevant control context.

## Alternative cause

Ask whether another cause could explain the same outcome.

This matters especially for success: the workflow may have succeeded despite a step rather than because of it.

## Boundary and transfer

State where the mechanism applies and where it should not.

When consequence warrants it, test a new case where it should help and a negative-control case where it should not apply.

A working-method mechanism must specify the task/decision class in which it should affect collaboration state. It must not become a universal personality rule.

## Promotion

Promote only after evidence is sufficient for the intended scope.

Keep original experience evidence separately so future contradictions can reopen the mechanism.

Retire narrower guards when a stronger invariant subsumes them.

When several complaint wordings share one generating failure, promote one mechanism rather than accumulating lexical/style prohibitions.

## Activation

A promoted mechanism must identify the decision or failure class it applies to, the owning ANGENT component, its boundary, and an observation that would disconfirm it.

Context should retrieve it because the current decision matches that class, not merely because the wording looks similar.

Working-method mechanisms can be activated into collaboration state when they materially change how the current task should proceed.

When activation materially affects a decision, correction interpretation, or collaboration method, preserve compact activation evidence:
- mechanism pointer/topic;
- current decision/failure class;
- applicability facts that matched the mechanism boundary;
- owner/control point where it became active;
- effect on the current plan/collaboration/quality expectation;
- competing instruction or boundary that suppressed it, when relevant.

This is diagnostic semantic state, not an event log. Do not record every retrieved lesson. Persist a pointer/subset only when later resume, recurrence diagnosis or acceptance depends on knowing whether the mechanism actually activated.

A stored lesson that is not activated at the relevant decision is not operational learning. If activation evidence is absent when recurrence diagnosis depends on it, treat activation status as UNKNOWN rather than inferring from the final outcome.

## Recurrence

Repeated failures are evidence about the controlling mechanism:

- FIRST_OBSERVED — repair the task and capture the experience;
- REPEATED_BEFORE_PROMOTION — investigate a shared systemic cause before adding another local guard;
- RECURRED_AFTER_PROMOTION — reopen the mechanism and inspect why activation/routing/ownership failed;
- PERSISTENT_RECURRENCE — stop adding local rules and audit the controlling owner, interface, state model, retrieval path, positive baseline, and control-point placement.

If a promoted rule existed but behavior still recurred, do not simply strengthen the wording. Ask whether the rule was not retrieved, was routed too late, conflicted with another owner, encoded the wrong abstraction, or lived downstream of the decision it needed to control.

Group wording variants when they expose the same mechanism.
