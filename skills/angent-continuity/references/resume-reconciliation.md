# Resume and reconciliation

Resume is not “read an old summary and continue”.

## Recovery sequence

1. identify the active work item;
2. read the highest coherent continuity revision;
3. apply newest explicit instruction/current authority;
4. inspect pending/ambiguous effects;
5. validate artifact/source pointers;
6. refresh external state that may have changed;
7. resolve conflicts/divergence;
8. return the reconciled frontier to Context/Reasoning;
9. continue from the first unfinished valid unit.

## External change

A provider may have changed while ANGENT was interrupted: branch HEAD advanced, issue moved, page edited, deployment changed, or another session completed work.

Do not discard the stored frontier. Reconcile it so completed/remaining work still has meaning.

## Concurrent sessions

A later timestamp does not automatically win.

Compare source versions, identify overlap, preserve independently verified disjoint work, and reconcile conflicting frontier/decision state before dependent action.

## Ambiguous effects

If a prior session may have performed a write but response was lost, query by target/operation identity and determine actual state before retry.

## Stale artifacts

A saved pointer is not proof an artifact still exists or matches the saved version.

Validate before using it as current context.
