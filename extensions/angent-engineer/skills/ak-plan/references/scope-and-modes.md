# Scope challenge and planning modes

## Scope challenge

Before investing in design, ask:

1. **What already exists?**
   - inspect reusable code/services/patterns;
   - identify an existing plan or implementation that already owns part of the request.

2. **What is actually requested?**
   - preserve the full requested outcome/scope;
   - separate requested work from attractive but unrequested additions;
   - surface deferable work as a choice, not an automatic cut.

3. **Where is complexity coming from?**
   - too many files/services/phases are a smell only when they do not correspond to real ownership/dependency boundaries;
   - challenge accidental complexity, not legitimate scope.

A trivial, fully specified local change may skip this ceremony.

Do not reduce scope unless the user explicitly authorizes it. A "fast" mode reduces planning depth, not product scope.

## Modes

Choose the smallest mode that protects correctness.

### fast

Use for clear, low-risk work with little external uncertainty.

- inspect repository state;
- skip broad external research;
- create a compact plan;
- preserve acceptance/verification;
- usually skip adversarial review/interview unless a material contradiction appears.

### hard

Use for complex or unfamiliar work.

- focused Research and Scout;
- architecture and dependency analysis;
- adversarial review;
- material-plan validation;
- explicit risks and verification.

### deep

Use for major refactors or broad cross-system work.

In addition to hard:
- inspect each phase's affected files/interfaces/state;
- identify existing tests and missing protection;
- include migration/rollback or compatibility state when material;
- expose per-phase dependency and verification detail.

### parallel

Use only when there are genuinely independent workstreams.

Include:
- exclusive or safely composable ownership;
- dependency graph;
- shared-interface coordination;
- integration/whole-result verification.

Do not declare parallelism merely because tasks look different.

### two-approach

Use when two materially different implementation approaches remain credible.

For each approach compare:
- constraints satisfied/violated;
- complexity and switching cost;
- migration/rollback implications;
- operational/security/performance consequences;
- uncertainty.

Select one before hydrating execution work.

## TDD modifier

When tests-first structure materially reduces regression risk, add to each affected phase:
- current-behavior/regression test;
- implementation/refactor step;
- new-behavior test;
- compile/type/test gate.

Do not force TDD onto work where it provides no meaningful signal.

## Auto selection

When the user did not name a mode, select from task evidence. Ask only when the mode changes a user-owned trade-off such as scope, cost, or required review depth.
