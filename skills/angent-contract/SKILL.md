---
name: angent-contract
description: Define the current task boundary, success semantics, authoritative sources and authorization without solving the task.
---

# ANGENT Contract

Define only what materially changes correctness.

Capture:
- requested outcome and underlying objective when distinguishable;
- target and canonical source(s) of truth;
- hard constraints, soft preferences and explicit exclusions;
- current phase: answer-only, read-only/audit, or authorized mutation;
- permitted external effects and relevant privacy boundaries;
- success state and evidence needed to claim it;
- unresolved ambiguity only when it blocks correct work.

Do not turn a literal action into the goal if the user's real objective is clear. Example: reuse of a template is a means; fidelity and user experience may be the outcome.

Pass the contract to Reasoning. Contract does not choose the solution, teaching path or execution plan.
