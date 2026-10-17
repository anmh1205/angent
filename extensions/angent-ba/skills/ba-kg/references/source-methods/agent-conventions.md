# Specialist review perspectives within ANGENT

**Provenance:** Adapted from MIT Dev BA Kit / rules/agent-conventions.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. This is a review *method*, not a declaration of installed agents.

## Divide review by material questions

A business analyst checks actor goals, rule sources, scope boundaries and exceptions. A product reviewer checks value, prioritization and decision owner. UX examines navigation, information architecture and loading/empty/error states. QA examines observable acceptance criteria, negative and boundary cases. An engineer examines feasibility, integration, data ownership and security. A change reviewer traces source revisions to affected artifacts.

ANGENT Root chooses only the perspectives that add value to the current decision. One person or one agent can apply several perspectives sequentially, so a runtime capable of spawning subagents is never mandatory.

## Inputs, outputs and source priority

Read the actual document/feature, its source revision, accepted decisions and linked requirements. Review each questionable claim against those sources before raising a finding. An uncited preference for a different writing style is not automatically a business defect.

For each finding report affected ID/section, source witness, impact, a specific correction or verifying question and confidence. Separate factual contradictions, unverified assumptions, missing coverage and design preferences; they require different actions.

## Independence, disagreement and action

If multiple real reviewers are available, their findings can be compared. Count distinct **evidence**, not votes. Two reviewers repeating the same unsupported assumption do not increase its credibility; a single source-backed privacy defect can be blocking.

Never claim an independent agent ran unless the host actually executed one. Never let a specialist reviewer assume Root authority, write external provider state or approve requirements. Execution follows user scope and tool permissions. Quality checks whether a proposed fix resolves the underlying evidence.

## Example

A fleet access story may be syntactically complete yet fail QA review if it lacks a denied-user test. Business review checks who may view which vehicles; engineering review checks how tenant ownership is enforced; UX checks that the denial reveals no sensitive data. These are complementary questions, not three fictitious subagents.
