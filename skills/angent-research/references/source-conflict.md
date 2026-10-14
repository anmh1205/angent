# Source conflict and version boundaries

Conflicting sources often reflect different boundaries rather than one source being simply wrong.

Apparent agreement can also be misleading when several sources share the same upstream lineage.

## Reconcile in this order

Check:
1. exact product/library/runtime/model version;
2. platform/OS/hardware;
3. configuration/feature flags/resource conditions;
4. normative requirement versus current implementation;
5. publication/observation date;
6. scope/edition/plan/account state;
7. observation/measurement quality;
8. source lineage and whether apparently independent reports share one origin.

## Source priority is claim-specific

A standard may establish what must happen.

Current source code may establish what an implementation does.

A runtime probe may establish what the user's environment is doing now.

A vendor docs page may establish supported behavior but still lag a just-released implementation.

An evaluator can establish a judgment only within the validity of its rubric, references and measurement environment.

## Do not hide conflict

If unresolved conflict can change the decision, return it as a live uncertainty.

Authoring should not smooth two incompatible sources into a confident sentence.

If evidence disagrees, do not assume the subject is wrong before considering evaluator or environment confounders.

## Shared lineage

Before treating multiple agreeing sources as corroboration, ask whether they depend on the same upstream fact, benchmark, generated reference, dataset or provider observation.

Correlated repetition improves discoverability more than independence.

## Historical sources

Historical evidence may explain why a design or note exists without describing current state.

Label it accordingly.
