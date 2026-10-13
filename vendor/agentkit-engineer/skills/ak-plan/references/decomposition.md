# Plan decomposition

Good work units:
- produce one coherent behavior/outcome;
- have clear prerequisites;
- have bounded ownership;
- can be verified independently enough to know progress.

Bad decomposition:
- one task per file;
- mixed unrelated cleanup;
- giant phase with no verification;
- “frontend/backend” split when both share an unresolved contract;
- parallel writes to one shared generated artifact.

Use dependency order before chronological wish lists.
