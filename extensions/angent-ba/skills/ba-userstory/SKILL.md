---
name: ba-userstory
description: Evidence-driven business analysis for userstory with approved source identity, testable outcomes and non-destructive handoff.
---

# User story slicing from accepted outcomes

**Origin:** Independently adapted from MIT Dev BA Kit \`userstory\` (Edward Ngo, 2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/userstory/SKILL.md. Uses INVEST-style quality judgment without forcing an unrelated project into fixed story files or a Claude approval pipeline.

## Sources and identity

1. Read the currently accepted capability, FR/BR, use case, error matrix, existing story/backlog and actual stakeholder outcomes. A formal SRS may be absent: source evidence can be a reviewed decision, accepted process specification or approved ticket. If there is **no accepted behavior source at all**, do not invent requirements.
2. Locate existing US IDs and Jira keys; preserve them. Use project-local conventions with enough context to prevent collisions across features and documents. A path-local \`US-001\` or \`AC-001\` is ambiguous unless its namespace is always carried through export, Jira and test traceability.
3. Distinguish product outcome from technical implementation. One story should deliver a coherent observable benefit to an actor; technical enablers may become engineering tasks beneath the story, rather than separate fake business value.

## Slice for verifiable increments

4. Inventory the target FR/CAP scope and high-risk behavior: actor permissions, normal flow, denial, boundary, downtime and recovery. Map each candidate story back to its specific source; one FR may need several slices, or closely related FRs may belong in one coherent story.
5. Slice vertically by meaningful actor scenario, value boundary or rule when possible. Avoid splitting into front-end/backend/database tickets masquerading as independent user value. Check INVEST critically: independent enough, negotiable, valuable, estimable with current evidence, small for the actual delivery context, and testable.
6. Express actor, context, intention and benefit clearly. The common "As a / I want / So that" format is useful when it conveys meaning, but not mandatory if a better product-approved style exists.
7. Add acceptance criteria from accepted FR/BR/E boundaries: success, at least one relevant failure/denial path and important observable state changes. Criteria must not introduce new policy thresholds or provider behavior absent from sources.
8. Record linked FR/CAP/BR/AC IDs, dependency to other stories, candidate priority with evidence, scope exclusions and unanswered questions. Preserve independent acceptance versus overall feature release readiness.
9. For existing stories, compare updated source and issue version, propose a **field-level** diff and preserve unrelated human edits. Do not copy source kit's fixed \`docs/{feature}/userstories/us-NNN.md\` layout or auto-create Jira issues unless requested and authorized.

## Acceptance and handoff

A useful story maps to a real stakeholder job, has independently inspectable acceptance, stable provenance and a bounded delivery slice. Check coverage of every requested FR without claiming all missing stories must be created now. A requirement deliberately deferred or covered by another accepted story is not necessarily a defect.

For a fleet status page, the operator's ability to view only vehicles they may access is a distinct permission boundary. A possible acceptance case is an unauthorized user being denied without disclosure of vehicle data; that is an illustrative requirement and not evidence of an implemented authorization guard.

Hand accepted stories and their actual IDs to \`ba-ac\`, \`ba-test-checklist\`, \`ba-jira\` or Engineer only when useful. A story written to Markdown is not deployed functionality; a Jira issue in Done is not acceptance evidence. ANGENT Root retains final scope, source-of-truth and authorization.
