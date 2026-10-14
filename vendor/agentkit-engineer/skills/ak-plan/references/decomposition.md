# Plan decomposition

Good work units:
- produce one coherent behavior/outcome;
- have clear prerequisites;
- have bounded ownership;
- preserve public/shared contracts explicitly;
- can be verified independently enough to know progress.

Bad decomposition:
- one task per file;
- mixed unrelated cleanup;
- giant phase with no verification;
- "frontend/backend" split while a shared contract remains unresolved;
- parallel writes to one shared generated artifact;
- phases ordered only by narration rather than dependency.

## Dependency-first decomposition

Trace:
- schema/state prerequisite;
- public API/interface prerequisite;
- generated artifact prerequisite;
- migration/compatibility ordering;
- runtime/deployment ordering;
- test/verification dependencies.

A phase can be RUNNABLE only when its prerequisites are established.

## Parallel decomposition

Parallel phases require:
- non-overlapping or safely composable writes;
- no hidden shared-state dependency;
- clear integration owner;
- independent verification plus final combined verification.

If two branches both depend on an unresolved shared interface, resolve that interface first instead of labeling them parallel.
