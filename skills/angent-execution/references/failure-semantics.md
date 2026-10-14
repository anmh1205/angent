# Failure semantics

A failed tool call is not automatically a negative fact about the target world.

Separate the **failure domain** before deciding what the result means or whether retry can help.

## Failure domains

Use only when the distinction changes reasoning or retry behavior:

- **HARNESS_OR_ROUTING** — tool unavailable/not found, adapter/capability mismatch, local schema/serialization/dispatch failure before a trustworthy provider observation;
- **TRANSPORT_OR_TRANSIENT_PROVIDER** — timeout, connection failure, rate limit, temporary provider/server failure, or another condition where the domain outcome is not established;
- **AUTHORIZATION_OR_ACCESS** — authentication/permission/policy denial; this establishes lack of usable access, not target absence;
- **PROVIDER_OPERATION** — the intended provider handled the request and explicitly rejected/failed the requested operation;
- **DOMAIN_OBSERVATION** — an authoritative observation succeeded and its documented semantics establish a domain fact, including a legitimate negative fact;
- **AMBIGUOUS_EFFECT** — a side effect may have occurred but the response/outcome is unknown and must be reconciled.

These labels are semantic categories, not a mandatory runtime enum.

## Negative evidence

Do not infer:

- “target does not exist” from tool-not-found;
- “record absent” from authentication failure;
- “deployment failed” from a client timeout;
- “operation was rejected by the domain” from local schema validation;
- “provider state is false” from an error payload whose boundary/meaning is unknown.

A negative domain claim is admissible only when:
1. the observation reached the authoritative source/provider needed for that claim;
2. target identity and scope are known;
3. the response semantics actually entail the negative proposition;
4. completeness/version/freshness are sufficient for the claim.

For example, a canonical provider lookup returning a documented “not found” for the exact object may establish absence. A missing local tool named `get_object` does not.

## Error-as-result

Some harnesses return tool/runtime failures as model-visible result text instead of raising an exception.

Classify the envelope before interpreting the message content.

Model-visible text such as “not found”, “failed”, or “permission denied” is not automatically a domain observation. Preserve where the error originated.

## Retry

Retry according to both effect safety and failure domain:

- HARNESS_OR_ROUTING — discover/fix the route or capability; repeating the same unresolved dispatch usually adds no evidence;
- TRANSPORT_OR_TRANSIENT_PROVIDER — retry only when another attempt can plausibly change the result; reconcile side effects first when outcome may be unknown;
- AUTHORIZATION_OR_ACCESS — refresh/obtain legitimate access or change to an authorized route; repeated identical attempts are not progress;
- PROVIDER_OPERATION — inspect the provider-reported reason and change the action/model if appropriate;
- DOMAIN_OBSERVATION — treat as evidence; retry only when freshness/change over time is decision-relevant;
- AMBIGUOUS_EFFECT — reconcile before replay.

## Boundary with Reasoning

Execution identifies the operational boundary and returns the failure/evidence class.

Reasoning decides what proposition, if any, the result can establish.

Do not convert an operational failure into a domain belief merely to keep the plan moving.
