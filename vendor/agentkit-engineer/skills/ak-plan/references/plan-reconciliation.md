# Plan reconciliation

## Existing-plan scan

Before creating a new plan, inspect unfinished plans relevant to the same feature/system.

Look for:
- overlapping files/modules;
- shared schema/interface changes;
- prerequisite outputs;
- mutually incompatible assumptions;
- duplicate work.

Do not create a parallel plan that silently competes with an active one.

## Dependency relationship

Represent dependencies in whatever durable plan format the project uses.

The important semantics are:
- this plan needs an output from another plan;
- this plan changes an assumption another plan depends on;
- both plans must coordinate a shared migration/interface.

Update both sides when the plan format supports bidirectional links.

If the relationship is genuinely ambiguous and changes execution order, surface it as a decision.

## Whole-plan consistency sweep

After validation/red-team/replanning modifies part of a plan, re-read the whole plan and search for:
- renamed files/APIs/fields;
- rejected assumptions still present elsewhere;
- duplicate embedded contracts;
- phase ordering that no longer matches dependencies;
- acceptance criteria based on superseded behavior.

Do not hand a contradictory plan to Cook.

## Task-surface projection

A Jira/GitHub/task board may mirror plan items for coordination.

The durable plan retains implementation meaning; the external task surface provides shared operational status.

Reconcile both rather than assuming either one alone contains everything needed.
