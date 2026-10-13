---
name: angent-contract
description: Define the current task boundary, authoritative sources, constraints, authorization and state-based success semantics without solving the task.
---

# ANGENT Contract

Contract compiles the user's current request into the smallest task model that materially affects correctness.

Read `task-model.md`.

Capture when relevant:
- requested outcome;
- underlying objective when it is clear and changes the solution;
- target and source(s) of truth;
- hard constraints, soft preferences and exclusions;
- current phase and external-effect authorization;
- privacy/security boundaries;
- success state and evidence required to claim it;
- ambiguity only when it blocks correct work.

Do not silently replace an explicitly required means with another strategy even when the underlying objective is obvious. Preserve the instruction and expose conflicts only when needed.

Output a compact task model to Reasoning/Execution/Quality. Contract does not choose the solution, teaching path or action graph.
