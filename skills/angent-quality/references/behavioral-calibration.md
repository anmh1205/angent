# Behavioral calibration

Use this reference when changing a shared ANGENT method, root/default prompt, routing/owner interface, long-form authoring method, or another behavior that can propagate across many future units/tasks.

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

## Compare to baseline

Ask what changed relative to accepted behavior:

- target failure;
- protected accepted strengths;
- neighboring behavior likely to regress;
- cost/latency only when they actually matter to the task;
- unexpected strategy changes.

Do not optimize one scalar such as brevity, tool count, speed, diagram count, or source count unless the Contract truly makes it the objective.

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
