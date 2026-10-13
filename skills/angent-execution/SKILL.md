---
name: angent-execution
description: Execute authorized ANGENT actions, choose native or fallback specialist capability, observe real effects, reconcile ambiguity and return evidence for reasoning.
---

# ANGENT Execution — Actuator and Observer

Execution owns action realization, tool/specialist selection, retry safety, observation and provider reconciliation. Harness-specific capability discovery/activation follows the Root `harness-contract.md` rather than a separate execution architecture per client.

It does not own strategic reasoning after evidence invalidates the model.

## Load references progressively

- references/action-semantics.md — ActionNode requirements, observation and replanning boundaries.
- references/effect-safety.md — idempotency, PREPARED/RECONCILE and retry policy.
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

Do not execute a specialist proposal that contradicts current Contract/Reasoning invariants.

## Choose the route

Prefer the smallest sufficient route that preserves correctness and observability.

For engineering specialist work:
1. use native AgentKit Engineer when installed and usable;
2. otherwise use the canonical fallback port;
3. do not silently mix generations;
4. otherwise fall back to direct harness tools/single-agent work when the required capability does not depend on Engineer.

A specialist is a capability provider, not strategic authority.

## Execute

Advance the current frontier.

Respect user-requested tool boundaries and project AGENTS.md.

For low-risk reads, avoid heavy transaction ceremony.

For consequential writes, use Continuity PREPARED/reconcile semantics.

Do not blindly replay timed-out or response-lost non-idempotent writes.

When Format supplies destination representation requirements, Execution performs the external write; Format does not gain independent effect authority.

For whole-scope reads, preserve pagination/cursor closure, truncation state, filters, and expected/observed counts when known. A first page, top-N result, or partial response is not complete inventory evidence.

## Observe

Return an observation delta that describes the world, not merely tool output:
- attempted action;
- actual observed state;
- changed identifiers/versions;
- checks performed;
- expectation match/mismatch;
- residual uncertainty;
- evidence/artifact pointers.

Exit code 0 is evidence about the command, not automatically the requested endpoint.

## Adaptive boundary

Execution may change mechanical tactics inside the accepted action: retry a read, alter a search query, choose an equivalent tool.

Classify failures when retry behavior differs: transient, rate-limited, authentication/permission, missing target, schema/capability mismatch, stale state, or semantic failure. Retry only when another attempt can plausibly change the result. If repeated attempts produce no new observation, return to Reasoning instead of churning equivalent actions.

Return to Reasoning when:
- a precondition is false;
- a model assumption is contradicted;
- a new constraint appears;
- expected observation differs materially;
- a specialist proposes a strategic change.

## Completion

Continue while an authorized runnable next step remains and the requested endpoint is not verified.

Stop only at verified completion, genuine blocker, required user decision, authority/safety boundary or unavailable capability.

A progress update is communication, not a stop condition.
