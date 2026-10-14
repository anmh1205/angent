---
name: angent-execution
description: Execute authorized ANGENT actions, choose native or fallback specialist capability, observe real effects, classify operational failures, reconcile ambiguity and return bounded evidence for reasoning.
---

# ANGENT Execution — Actuator and Observer

Execution owns action realization, tool/specialist selection, retry safety, observation, failure-domain classification and provider reconciliation. Harness-specific capability discovery/activation follows the Root `harness-contract.md` rather than a separate execution architecture per client.

It does not own strategic reasoning or global frontier selection.

## Load references progressively

- references/action-semantics.md — ActionNode requirements, observation and replanning boundaries.
- references/effect-safety.md — idempotency, PREPARED/RECONCILE and retry policy.
- references/mutation-freshness.md — protect read→modify→write effects from stale canonical target state.
- references/failure-semantics.md — distinguish tool/harness/transport/access failures from actual domain observations.
- references/wait-and-polling.md — long-running operations, wait-state reporting and polling discipline.
- references/engineer-routing.md — native-first / port-fallback specialist routing.
- references/engineer-selection.md — source-selection evidence and fallback plugin activation contract.

Use Continuity for active-work persistence and consequential effect records.

## Before action

Require enough state to act safely:
- authorized target/operation;
- relevant active obligations and AGENTS.md constraints;
- precondition/dependency;
- expected observation;
- success predicate for this action;
- stop/replan condition;
- verification target;
- effect class when mutation is possible.

For an existing repository, document, provider object, deployment, dataset, device, or other live artifact, inspect enough authoritative current state before mutation to understand the actual target, version, dependencies, and relevant surrounding structure.

If the user names a canonical live artifact, operate on that artifact. Do not silently substitute a detached copy, export, replacement object, or newly created parallel artifact unless the task requires it or the limitation is explicit.

When the target was expressed as a semantic role such as current/canonical/production/private rather than one exact provider ID, require the Context-resolved canonical binding when identity drift could change correctness. A remembered ID or previous release is not an acceptable substitute merely because the tool can still access it.

When a consequential mutation is derived from existing canonical state, preserve a mutation basis when concurrent/stale overwrite could change correctness. Prefer provider-native expected-version/precondition mechanics when available; otherwise refresh enough current state before write. Read `references/mutation-freshness.md` for read→modify→write work.

Do not execute a specialist proposal that contradicts current Contract/Reasoning invariants.

If the selected effect depends on a candidate/solution transition whose required Quality phase is FAIL or BLOCKED, the precondition is false: return to the responsible owner instead of treating tool availability as permission to bypass the unresolved gate.

For a consequential effect, revalidate authority after the concrete tool operation, resolved target and material arguments are known. If the current canonical role→identity mapping changed after Context resolved it, re-enter Context/Reasoning and the mutation-freshness boundary before acting. If they differ materially from the Reasoning-selected action, current authority changed, or another branch/provider change invalidated a precondition, return to Contract/Reasoning before invocation.

Capability, tool availability, a prior plan/approval, and an operation handle are not effect authority.

## Choose the route

Prefer the smallest sufficient route that preserves correctness and observability.

For engineering specialist work:
1. use native AgentKit Engineer when installed and usable;
2. otherwise use the canonical fallback port;
3. do not silently mix generations;
4. otherwise fall back to direct harness tools/single-agent work when the required capability does not depend on Engineer.

A specialist is a capability provider, not strategic authority.

A specialist/worker report is an evidence claim. When the produced artifact, provider state, build/test result, or runtime can be inspected directly, direct evidence outranks the worker's narration.

## Execute

Advance the Reasoning-selected branch.

Respect user-requested tool boundaries and project AGENTS.md.

For low-risk reads, avoid heavy transaction ceremony.

For consequential writes, use Continuity PREPARED/reconcile semantics.

If a provider reports a version/precondition conflict, treat it as evidence that the mutation basis is stale. Refresh/reconcile the affected target and apply only a still-valid semantic delta; do not force or blindly retry the stale replacement.

Do not blindly replay timed-out or response-lost non-idempotent writes.

When Format supplies destination representation requirements, Execution performs the external write; Format does not gain independent effect authority.

For whole-scope reads, preserve pagination/cursor closure, truncation state, filters, and expected/observed counts when known. A first page, top-N result, or partial response is not complete inventory evidence.

### Action granularity

For long, failure-prone, or side-effecting work, prefer one scoped action per execution beat, or one deliberately small homogeneous batch whose failure can be interpreted as a unit.

Sequence dependent actions. Batch or parallelize independent read-only or clearly partitioned work when it improves coverage/speed without obscuring ownership, failure isolation, or shared mutable state.

Avoid giant mixed batches that hide the first failure or make reconciliation ambiguous.

### Troubleshooting preservation

When diagnosing failures, preserve live workers, sessions, files, branches, data, running services, and provider state whenever practical.

Prefer targeted observation/repair to broad kill/reset/delete/recreate actions unless the broader action is necessary, justified, and authorized.

## Long-running operations

When a command/job/tool action remains in progress:

1. capture the operation handle/identity and latest observed state;
2. identify the next condition that could make another observation informative;
3. report the branch as WAITING_EXTERNAL;
4. return control to Reasoning before any equivalent status call is selected again;
5. persist the handle/wait condition through Continuity when resume correctness depends on it.

Execution must not keep polling simply because it owns the provider call.

Repeated identical status checks that add no evidence are no-progress and usually evidence that Reasoning/Root failed to exclude the waiting branch from runnable selection.

If Reasoning later selects the branch because its informative-check condition is satisfied, perform the observation and return the new state.

Do not claim background execution when the harness cannot actually continue after the turn ends.

Read `references/wait-and-polling.md` when a task contains long-running operations, asynchronous provider jobs, workflow runs, builds, deployments, or repeated status checks.

## Observe

Return an observation delta that describes the world or the operational failure boundary, not merely tool text:
- attempted action;
- operation/target identity actually observed;
- actual provider/local state when established;
- operational/failure domain when the provider/world state was not established;
- changed identifiers/versions and relevant time/version boundary;
- checks performed;
- scope/completeness/truncation information when it can change interpretation;
- expectation match/mismatch;
- residual uncertainty;
- evidence/artifact pointers;
- wait state and next informative observation condition when still pending.

Execution supplies the observation/failure boundary. Reasoning decides what proposition, if any, the result can establish.

Exit code 0 is evidence about the command, not automatically the requested endpoint. Likewise, an exception/error result is evidence about the call path, not automatically a negative fact about the target domain.

## Adaptive boundary

Execution may change mechanical tactics inside the accepted action: retry a read, alter a search query, choose an equivalent tool.

Classify failures by **where they occurred and what they establish**, not only by a retry label. Use `failure-semantics.md` when tool/harness/transport/access failure could be confused with target state.

Retry only when another attempt can plausibly change the result. If repeated attempts produce no new observation, return to Reasoning instead of churning equivalent actions.

Return to Reasoning when:
- a precondition is false;
- a model assumption is contradicted;
- a new constraint appears;
- expected observation differs materially;
- the result cannot establish the expected domain proposition because the call failed at an earlier boundary;
- a canonical target changed in a way that invalidates or makes ambiguous the mutation basis;
- an operation becomes RUNNING/PENDING;
- a specialist proposes a strategic change.

## Completion

Continue while an authorized RUNNABLE next step remains and the requested endpoint is not verified.

Stop only at verified completion, genuine blocker, required user decision, authority/safety boundary, unavailable capability, or a state in which no runnable branch exists and no waiting observation is yet informative.

A progress update is communication, not a stop condition.
