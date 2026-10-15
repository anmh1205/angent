# Plan reconciliation

## Existing-plan scan

Before creating a new plan, identify the project's owning plan/issue/spec system and inspect unfinished work relevant to the same feature/system.

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

Update both sides when the authoritative system supports bidirectional links and the relationship has been established. Do not edit a second source merely to mirror every status.

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

Only when the project **actually separates** a canonical plan from operational task cards should the cards be treated as projections. In issue-first projects, the issues themselves can be the plan and the source of live task state. Identify ownership first, then reconcile any real projections; never generate a redundant plan store as a prerequisite for tracking.
