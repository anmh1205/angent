---
name: ba-preview
description: Specialized ANGENT business analysis preview method.
---

# Navigable feature-preview artifact

## Input and responsibility

A preview is a **read-only stakeholder view** of an already inspected and versioned feature set: goals, approved SRS, business rules, diagrams, screen flow, story coverage and test state. It does not silently write back to Jira, modify docs or infer approval.

## Build method

1. Identify feature ID, language, accepted artifact list and current revision. Validate actual links and prevent path traversal from untrusted document references.
2. Establish an information architecture that follows reader questions: what problem is solved, who uses it, expected behavior, failure/recovery, screens, contract, testing and unresolved decisions.
3. Reuse source artifact IDs as anchors and link back to original files. Provide search/filter by artifact type and confidence; group error codes by the FR/BR they constrain.
4. Render diagrams from verified sources, using actual SVG or browser-renderable content; if source diagrams fail to render, present the original text with an explicit failure notice. Do not replace a broken diagram with an invented screenshot.
5. Escape all untrusted content when generating HTML. No external CDN, hidden network call, dynamic evaluation of uploaded code or arbitrary scripts; keep CSP conservative.
6. Check keyboard navigation, focus, contrast, small-screen layout, table overflow and linked IDs.
7. Reopen the finished HTML and verify its reference count, navigation anchors and sample screen viewport. Report missing source assets separately.

## Suggested sections

Overview (objective, scope, users) → requirements (FR/NFR/BR) → main and alternate process → screens/wireframes → API integration → traceability/coverage → open questions/decision log. Each section links to the authoritative revision.

## Acceptance

A consumer can reach the original evidence for every material claim. Preview does not imply runtime testing or implementation completeness. If only a subset was indexed, state its exact boundaries. The portable renderer in the BA extension can produce HTML from a validated exchange graph; it is a *feature index*, not a full SRS parser.


## Ownership

ANGENT Root/Core retains reasoning, stakeholder intent, source authority and final Quality. This method is a task-specific support skill and does not create a second runtime, memory system or autonomous scheduler.
