---
name: ba-srs
description: Reconstruct or author a rigorous source-linked SRS with testable FR/NFR/BR, error matrix, stable IDs and real artifact checks.
---

# Software Requirements Specification — ANGENT BA

**Source methodology:** maintained adaptation of the MIT [Dev BA Kit SRS skill](https://github.com/nv-minh/dev-ba-kit/blob/main/skills/srs/SKILL.md), copyright (c) 2026 Edward Ngo. The actual portable validators and Markdown graph extractor referenced below are ANGENT implementations, not the upstream Claude plugin's hooks or subagents.

## Scope and authority

An SRS states precisely how a bounded system or feature is required to behave. It is distinct from a Product PRD (product outcomes and scope), BRD (business objectives and policies), URD (user needs), code-to-SRS (reconstructed *observed* behavior), use cases (actor-goal narratives) and test cases (concrete validation procedures). ANGENT Root/Core retains intent and reasoning, Execution owns any project writes and provider actions, and Quality checks artifact correctness.

Do not require creation of every upstream document before writing a useful SRS. Read what already exists; identify which missing decisions truly prevent a testable statement and keep the remaining draft qualified.

## Evidence intake and source baseline

1. Pin the feature name, intended readers, system boundary, accepted revision and external dependencies. Read the current project scope plus approved stakeholder decisions, URD/BRD/PRD, API contracts and existing SRS if present. Existing accepted source identifiers and glossary take precedence over any kit examples.
2. Build a small fact ledger: observed stakeholder need or explicit business decision, source/revision, affected actor, state transition and unresolved alternatives. An observation in source code is not automatic approval of a requirement.
3. Identify actor classes, authorization boundaries, tenancy/data ownership, normal user journeys and operational exception paths. Distinguish behavior intended for the initial release from later capability proposals.

## Derive the requirements

4. Assign each functional requirement a **stable** FR identifier already consistent with the project. State actor/precondition/trigger and a directly observable required outcome using testable language. Link the rule to its upstream capability or user need; record priority only when accepted.
5. Write NFRs separately with dimension, workload, target value and unit, measurement method, environment and confidence. "Secure", "fast" or "scalable" without a measurable contract is an open issue, not a finished NFR.
6. Formalize enforceable business rules as BR identifiers. Name scope, guards, applicable roles, limits, exceptions and source/owner. Never silently introduce lockout duration, number of retries, financial thresholds or retention windows from examples or generic best practice.
7. Build an explicit error matrix E with trigger, business/system condition, machine-facing error where specified, user-visible response where accepted, persistence/state side effect, retry/recovery guidance and linked FR. A single generic failure row is not enough when authorization denial, invalid input and infrastructure outage have different semantics.
8. Record data model responsibilities and integration boundaries: identity/keys, relevant state machines, external calls and trust boundaries, idempotency and consistency implications. Link separate sequence/activity/state/ERD diagrams if needed; diagrams do not replace the contract.
9. Mark every ambiguous or unapproved behavioral choice as an open question with consequence and next evidence required. Do not convert user silence into approval.

## Source-backed output shape

A reviewable Markdown SRS should contain: Overview, scope and actors; FR table (ID, Requirement, Covers, Priority, Source); NFR table (ID, Category, Requirement, Measure); BR table (ID, Rule, Applies to, Source); E table (ID, Condition, System behavior, User sees, Related FR); data/integration notes; related diagrams; glossary and open questions. This structure is compatible with the actual BA Markdown graph extractor. The attributed template at ../ba-kg/references/templates/doc-srs.md provides a concise starting point; the project may already have a better approved format.

For each FR, make it possible to derive at least one Given/When/Then acceptance criterion and to identify meaningful negative/boundary tests. Preserve distinct identities across updates; never renumber approved requirements simply because a row moved.

## Verification with actual ANGENT tools

10. Show a scoped change preview when an accepted SRS already exists. State which IDs are unchanged, new, superseded or uncertain and why. Update only authorized content; preserve unaffected decisions, links and stakeholder material.
11. When there is a real filesystem, validate the **completed** Markdown, not the unfilled template:

    python extensions/angent-ba/scripts/validate_documents.py docs/FEATURE/srs/FEATURE-spec.md --root .

12. Where SRS, checklist and test case Markdown follow the declared table contracts, extract the actual typed evidence graph:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --srs docs/FEATURE/srs/FEATURE-spec.md --checklist docs/FEATURE/test/checklist.md --cases docs/FEATURE/test/test-cases.md --root . --output output/feature-traceability.json

   Source documents may be missing; use only existing supported arguments and report external/unresolved references. A graph link is not proof a test was executed, and empty coverage is not an invitation to fabricate a test.
13. Review independently for contradiction, unusable error behavior, missing authorization paths, unmeasurable NFRs and source freshness. Use the current provider's actual approval state and tests before claiming production readiness.

## Worked reasoning example

For a rental-car fleet status API, a valid *proposed* FR could require denial when the requesting account is not authorized for the vehicle. The error matrix should state the observable denial and any permitted data exposure, while the associated test should assert that no vehicle status is disclosed. This is not evidence that a deployed cloud currently enforces the rule; code and runtime paths must be inspected separately.

Likewise, a temporary upstream telemetry outage must not be described as invalid credentials. Its recovery, last-known data and freshness semantics require business decisions and source evidence.

## Acceptance and handoff

Report inspected sources/revision, accepted and proposed requirement counts (computed from the actual document), unresolved questions, requirement-to-capability links, meaningful failure coverage and validation commands/results. Offer follow-on activity/state/sequence/ERD, user story, AC and test work only where it genuinely advances the user's goal. Do not claim that a standalone SRS has been approved, implemented or tested simply because the document is formatted and parsable.

## Whole-lifecycle evidence instead of SRS-only statistics

When accepted URD, BRD and PRD documents exist, use the same source-backed graph extractor across all stages rather than treating CAP/BO/UN references as external guesses:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --urd extensions/angent-ba/examples/docs/atlas-re/atlas-re-urd.md --brd extensions/angent-ba/examples/docs/atlas-re/atlas-re-brd.md --prd extensions/angent-ba/examples/docs/atlas-re/atlas-re-prd.md --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output out/atlas-full-lifecycle.json

The real Atlas regression verifies 6 UN, 4 BO, 6 CAP and 8 FR. **8/8 FR have explicit FR→CAP→BO→UN ancestry, but only 4/8 FR link downstream to a TC artifact.** Four source-to-test gaps remain visible; structural reference existence does not prove execution or business approval. Do not change test counts or fabricate CHK/TC artifacts to satisfy a release threshold.

Some real projects have no complete URD/BRD/PRD sequence. In those cases, mark upstream coverage unknown/uninspected rather than insisting the user create redundant documents. ANGENT Root decides the appropriate evidence depth and which missing links genuinely matter.
