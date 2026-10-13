# Source conflict and version boundaries

Conflicting sources often reflect different boundaries rather than one source being simply wrong.

## Reconcile in this order

Check:
1. exact product/library/runtime version;
2. platform/OS/hardware;
3. configuration/feature flags;
4. normative requirement versus current implementation;
5. publication/observation date;
6. scope/edition/plan/account state;
7. observation quality.

## Source priority is claim-specific

A standard may establish what must happen.

Current source code may establish what an implementation does.

A runtime probe may establish what the user's environment is doing now.

A vendor docs page may establish supported behavior but still lag a just-released implementation.

## Do not hide conflict

If unresolved conflict can change the decision, return it as a live uncertainty.

Authoring should not smooth two incompatible sources into a confident sentence.

## Historical sources

Historical evidence may explain why a design or note exists without describing current state.

Label it accordingly.
