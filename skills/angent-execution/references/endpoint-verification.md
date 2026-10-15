# Verification from action to requested endpoint

Use when the user asks for completion across several files, services, runtime layers, people or time-dependent effects, or when a narrowly passing check risks supporting an overbroad completion claim. This is a choice of evidence, not a prescribed test pyramid.

## Follow the asserted claim

Distinguish observable propositions:

- Source/artifact: an intended change is present in the correct live target and preserves unrelated state.
- Structural: parsing, lint, build or schema checks establish their own scoped property.
- Component/contract: a local behavior or interface conforms under tested inputs.
- Integrated path: a meaningful stimulus produces the expected result through affected boundaries under stated conditions.
- Operational/value: the deployed system or affected stakeholder exhibits the intended outcome, when that was required and observable.

A higher observation can establish some lower claims but only within its actual context and scope. A passed command cannot be promoted directly to the next untested level. Do not require every level if the Contract requests only a bounded edit.

## Select meaningful evidence efficiently

Trace the requested behavior and credible regression paths. Identify the smallest available observation that verifies each load-bearing boundary. Prefer deterministic cheap checks early; delay expensive coherent suites where that reduces redundant work without permitting unsafe propagation. For embedded/cloud systems distinguish simulated behavior, hardware assumptions, firmware/runtime logs, network/queue conditions, service persistence and UI read-back.

A collection of isolated successes is not by itself end-to-end coverage. Preserve negative paths that determine correctness: timeout, reconnection, duplicate delivery, stale configuration, authorization and partial failure as relevant. Do not invent hardware, staging, production access or results.

## Carry progress and stop accurately

After each material action, update only the verified proposition. A newly discovered defect that affects an earlier accepted unit makes that dependency RECHECK, not globally FAILED or silently still VERIFIED. Before marking a task complete, reconcile the user's endpoint against the verified evidence and actual inspection scope.

If a long external job is pending, keep its handle and next informative check condition; advance independent runnable tasks. If an action effect is ambiguous, inspect canonical provider state before replay. An unavailable required environment or permission blocks only the dependent verification/action, not independent safe work.

Report clearly what changed, what was actually checked, what remains unverified, and which condition would resolve the gap. CI success, a reviewer sign-off and a model self-report are each limited evidence, not automatic acceptance.
