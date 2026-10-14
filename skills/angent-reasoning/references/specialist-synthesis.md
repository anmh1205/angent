# Specialist synthesis

Use specialists to increase expertise, parallel evidence gathering, or implementation throughput without creating competing strategic brains.

## Treat output by type

A specialist output may be:
- evidence;
- causal analysis;
- plan proposal;
- implementation artifact;
- review verdict;
- risk/advice;
- unresolved question.

It is not automatically the current decision or verified state.

## Delegation contract

Give a specialist the smallest context sufficient to perform its bounded job.

When relevant include:

- objective or decision/work unit it serves;
- exact scope and exclusions;
- canonical source/target and current version or pointer;
- active obligations and project constraints that apply;
- task-relevant collaboration/working-method expectation only when it changes the specialist's method;
- accepted or rejected approaches when repeating one would recreate a known failure;
- expected output type: evidence, proposal, artifact, review, etc.;
- acceptance criteria;
- verification/evidence expected from the specialist.

Do not dump the whole user profile, full conversation, or unrelated project history into every worker.

A worker may propose scope expansion when evidence demands it, but Reasoning retains authority to widen strategic scope.

## Synthesis checks

Compare:
- provenance;
- assumption overlap;
- whether evidence is actually independent;
- contradictions;
- dependency between conclusions;
- what observation would resolve disagreement.

Two agents repeating the same assumption are not independent confirmation.

A worker or specialist saying “done”, “tests passed”, or “verified” is an evidence claim, not ground truth. When the artifact, provider, runtime, or test result can be inspected directly, direct evidence outranks the report.

## Roles

Planner proposes implementation structure; Reasoning still checks objective/invariants.

Researcher supplies evidence; Reasoning decides what it changes.

Debugger supplies causal evidence; Reasoning decides whether root cause is established enough to choose a fix.

Advisor/brainstormer broadens alternatives or exposes risks; it does not override explicit constraints or authoritative evidence.

Reviewer/tester provides implementation evidence; Quality still owns task-level acceptance.

Implementer produces artifacts/effects; Execution/Quality verify the relevant resulting state instead of trusting completion narration.

Fan out only when work is meaningfully independent or specialist context isolation adds value.
