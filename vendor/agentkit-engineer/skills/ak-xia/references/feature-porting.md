# Feature porting

Compare source and destination on:

- user-visible behavior;
- input/output contract;
- state model;
- dependency assumptions;
- data/schema shape;
- error/recovery behavior;
- security/auth boundary;
- performance expectations;
- UI states;
- tests/acceptance evidence.

Build a semantic crosswalk:

```text
source mechanism → required behavior → destination owner/mechanism
```

Preserve behavior, not accidental source structure.

If the source license restricts copying, reimplement from behavior/specification rather than copying protected code.
