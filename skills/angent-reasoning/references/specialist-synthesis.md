# Specialist synthesis

Use specialists to increase expertise, parallel evidence gathering, review independence, or implementation throughput without creating competing strategic brains.

Load `delegation-context.md` when a worker/subagent receives non-trivial task context, authority, raw evidence, or write capability.

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

Give a specialist the smallest **semantic projection** sufficient to perform its bounded job. Do not assume that the harness's default handoff history is the intended task context.

When relevant include:
- objective or work unit it serves;
- exact scope and exclusions;
- canonical source/target and current version/pointer;
- active obligations/project constraints that apply;
- task-relevant working-method expectations only when they change the specialist's method;
- accepted/rejected approaches when repeating one would recreate a known failure;
- expected output type: evidence, proposal, artifact, review, etc.;
- acceptance criteria and verification evidence expected.

Do not dump the whole user profile, full conversation, unrelated project history, or raw tool traces into every worker.

Preserve epistemic/trust boundaries for material evidence. Delegation does not transfer the parent's full effect authority; any allowed effect scope must be explicit and still satisfies invocation-bound authority at execution time.

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

A worker/specialist saying “done”, “tests passed”, or “verified” is an evidence claim, not ground truth. When direct artifact/provider/runtime/test evidence is available, use it.

Re-admit specialist claims through the same evidence/observation boundaries as any other input; do not promote them merely because the specialist was trusted or specialized.

## Fan-out convergence

When several specialist/research branches inform one decision, arrival order is not evidence weight and the first completed branch does not automatically close the decision.

Before or during fan-out, Reasoning should know enough to distinguish:
- branches whose unresolved result can still reverse or materially change the decision;
- branches that are useful but non-blocking because the decision is already robust without them;
- branches that are redundant/correlated rather than independent confirmation.

Do not wait for every branch by ritual. A pending branch stops being decision-blocking when the current decision is robust across its credible remaining outcomes or when its information value no longer justifies the delay.

Do not commit a consequential decision merely because one favorable branch returned first while another still-open branch was specifically launched to discriminate a live alternative that could reverse the choice.

When outputs conflict:
- preserve each claim's provenance, scope and epistemic boundary;
- inspect shared assumptions/source lineage before counting them as independent votes;
- identify the discriminating observation or controlling authority;
- keep the decision unresolved when the conflict is material and cannot yet be adjudicated.

A late result that contradicts a decisive premise reopens only the dependent decision/work. It is not discarded because synthesis already happened, and it does not win merely because it arrived last.

## Roles

Planner proposes implementation structure; Reasoning still checks objective/invariants.

Researcher supplies evidence; Reasoning decides what it changes.

Debugger supplies causal evidence; Reasoning decides whether root cause is established enough to choose a fix.

Advisor/brainstormer broadens alternatives or exposes risks; it does not override explicit constraints or authoritative evidence.

Reviewer/tester provides implementation evidence; Quality still owns task-level acceptance.

Implementer produces artifacts/effects; Execution/Quality verify the resulting state rather than trusting completion narration.

Fan out only when work is meaningfully independent or specialist context isolation adds value. Keep synthesis ownership in Reasoning even when execution is parallel or delegated.
