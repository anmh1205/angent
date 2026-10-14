# Behavioral calibration

Use this reference when changing a shared ANGENT method, root/default prompt, routing/owner interface, long-form authoring method, frontier scheduling method, or another behavior that can propagate across many future units/tasks.

This is behavioral evidence, not a replacement for reasoning and not a return to static keyword/count tests.

## Why calibrate

A broad change can improve the reported failure while silently degrading a different accepted behavior.

A local example may also make a bad method look good by accident.

Calibrate the **generating method** before propagating it when failure cost and propagation scope justify the effort.

## Build the smallest useful case set

Prefer real cases from:

- user-reported failures;
- accepted positive baselines;
- recurrence/oscillation history;
- known boundary conditions.

Cover distinct mechanisms rather than collecting many near-duplicates.

When over-triggering is plausible, include both:
- a positive case where the behavior should activate;
- a negative/counter-case where it should not.

For long-form or multi-unit work, choose representative units across meaningful difficulty/dependency classes rather than only the easiest first unit.

## Correction-routing calibration

When changing how ANGENT handles corrections, calibrate the abstraction decision itself.

Useful distinct cases include:

- **genuinely local defect** — one incorrect fact/sentence with no recurrence/shared mechanism evidence; repair should stay local;
- **shared artifact mechanism** — several units exhibit the same generating error; repair should cover causal peers rather than only the latest example;
- **method-level recurrence** — the user has reported the same underlying failure across outputs/tasks; retrieve history/positive baseline and inspect the generating method before editing;
- **rule-exists-but-failure-recurs** — inspect retrieval, activation, routing, ownership and competing state before strengthening the rule;
- **positive-baseline divergence** — current behavior is worse than an explicitly accepted earlier behavior; reconstruct what mechanism changed rather than copying surface wording from the old output.

A correction system fails calibration if it always stays local or always escalates globally. The target is the correct causal abstraction level.

## Frontier-scheduling calibration

When changing long-running-operation behavior, judge branch selection rather than only poll interval.

Use distinct cases such as:

- **pending + independent work** — operation A is running while branch B can advance independently; A becomes WAITING_EXTERNAL and B is selected before another equivalent poll;
- **pending + dependent work only** — everything else genuinely depends on A; preserve the wait state and do not invent busywork or rapid polls;
- **wait trigger becomes eligible** — the documented interval/event/dependency condition is now satisfied; rechecking A is valid;
- **several runnable branches** — select useful work by the task model rather than recency of tool calls;
- **resume with saved handle** — reconstruct WAITING_EXTERNAL state and do not relaunch or aggressively poll merely because context was lost;
- **short operation completes immediately** — do not overcomplicate a direct completion with unnecessary frontier machinery.

Fail the method if:
- the most recently launched operation keeps being selected merely because it is active;
- WAITING_EXTERNAL is treated as RUNNABLE before its observation condition is satisfied;
- a waiting branch turns the whole task idle while independent useful work exists;
- the repair only increases a sleep/poll interval without changing branch-selection semantics.

## Cross-surface authoring calibration

When chat/response quality is accepted but document quality regresses, compare the same subject relation across surfaces.

Preserve:
- technical relation;
- paragraph cohesion;
- stable referents;
- semantic/epistemic strength;
- explanation depth.

Allow document-only additions only when scale requires them:
- curriculum continuity;
- section architecture;
- cross-reference/navigation;
- figures/tables/code;
- citations;
- larger examples and prerequisite repair.

Fail the method if document mode introduces generic teaching narration, detached fact sentences, ceremonial transitions, or a separate “formal AI” persona not required by the subject.

Do not solve this with a phrase blacklist.

## Compare to baseline

Ask what changed relative to accepted behavior:

- target failure;
- protected accepted strengths;
- neighboring behavior likely to regress;
- cost/latency only when they actually matter to the task;
- unexpected strategy changes.

Do not optimize one scalar such as brevity, tool count, speed, poll interval, diagram count, or source count unless the Contract truly makes it the objective.

## Judge the mechanism, not only the score

For agentic behavior, inspect enough trajectory/state to understand why the result passed or failed.

A passing endpoint can hide:
- lucky success;
- an invalid shortcut;
- stale assumptions;
- repeated waste;
- a grader that rewards the wrong thing.

A failing case can also expose a bad task/grader rather than bad agent behavior.

Use authoritative endpoint checks where objective. For semantic quality use independent review/rubric and calibrate it against human/user judgments when available.

## Capability vs regression

Keep two questions distinct:

- **capability:** does the new method solve a class it previously could not?
- **regression:** does it still preserve behavior that was already accepted?

A capability win does not excuse regression.

## Ablation

When a small instruction/prompt change plausibly caused a broad behavior shift, compare with and without that change when feasible before adding compensating rules elsewhere.

Prefer identifying the responsible mechanism over stacking another guard.

## Scale

After the method is calibrated, scale it to the intended scope.

The representative cases establish confidence in the method. They do not establish that every untouched unit is correct; whole-scope claims still require coverage evidence.

## Maintenance

A calibration case can be retired, narrowed or replaced when the underlying mechanism changes.

Do not let the case bank grow into an unowned museum of historical complaints.
