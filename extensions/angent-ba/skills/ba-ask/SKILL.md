---
name: ba-ask
description: Specialized ANGENT business-analysis procedure for ask.
---

# Answer project-specific business questions using evidence

## Routing

Use ba-ask only when the question depends on the project's documented policies, feature behavior, actor rights or decision history. Ordinary definitions, tutorials and explanations remain ANGENT Core responsibility. The result is a grounded answer, not a new independent chat assistant.

## Retrieval strategy

1. Identify the feature, actor, scenario and which state of the project is being asked about (current production, code, approved future scope or past decision).
2. Find the smallest authoritative source set: current product decision, SRS, error matrix, Jira/Confluence record, source code, live deployment logs if permitted. Prefer accepted versioned sources over old brainstorm drafts.
3. For each material factual assertion, capture explicit source path/version/section or actual tool result. If sources disagree, show the competing statements with date/revision instead of picking a convenient one.
4. Trace the pertinent chain business objective → capability → FR/BR → UI flow → API/state/test only as far as the question needs.
5. Explain the rule in natural terms: who may act, when, what observable system behavior follows, and what happens on rejection/failure. Separate the user's question from a proposed requirement modification.
6. If a referenced term could mean two different things, identify the consequential distinction and ask only if the answer truly depends on it.
7. Include unresolved questions and precise next source to inspect when important. Do not pad a narrow answer with the entire SRS.

## Example

Question: 'Khách hàng nhập sai mật khẩu năm lần thì sao?' A defensible answer states the actual accepted failed-login policy, its applicability to account/device/IP, lock duration, CAPTCHA, network-failure exclusions and source. It must not infer a 24-hour lock merely because a public sample used that number.

## Failure gates

If the source is inaccessible, say so and offer a bounded explanation or verification plan. Never imply live deployment behavior from an old spec; do not fabricate stakeholder decisions or citations.


## ANGENT cooperation

ANGENT Root/Reasoning owns interpretation and decisions; Authoring owns narrative quality; Execution handles authorized external effects; Quality verifies the outcome. Method selection is optional and context-dependent, never a forced workflow.
