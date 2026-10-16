---
name: ba-brainstorm
description: Evidence-driven business analysis for brainstorm with approved source identity, testable outcomes and non-destructive handoff.
---

# BA brainstorming: move from an uncertain idea to testable decisions

**Background:** Independently adapted from the MIT Dev BA Kit brainstorm method by Edward Ngo (2026) (https://github.com/nv-minh/dev-ba-kit/blob/main/skills/brainstorm/SKILL.md); informed by the public AI4BA BA-Kit. ANGENT Root remains responsible for the user's actual intent and accepted project context.

## What this method is for

Brainstorming is a focused exploration of *a decision that is not yet ready to be specified*. It may concern a new product, one unresolved business rule, an alternative process or a failed assumption. A brainstorm is not automatically a customer interview, PRD, SRS or license to implement a solution.

## Discover what's already known

1. Identify the decision: the opportunity, affected stakeholder, present behavior, intended value and why a choice matters now. Start from the user's latest request and existing source, not a compulsory two-round interview or a fixed new feature slug.
2. Distinguish evidence from hypotheses. Label each input as an accepted user decision, recorded stakeholder observation, source fact, analyst inference or unresolved assumption, with links/revisions where available.
3. Inspect earlier brainstorms, product documents, meeting decisions and technical constraints to avoid re-asking answered questions. Keep existing terminology and IDs stable; a project may not use the Dev BA Kit's folder hierarchy.
4. Choose **one or two appropriate elicitation techniques**, not an obligatory menu: stakeholder perspective reversal, alternative solution analysis, process walkthrough, boundary/exception exploration, causal analysis or a lightweight SCAMPER variation. Evaluate against the concrete problem rather than generating creative ideas for their own sake.

## Drive reasoning toward a decision

5. Produce genuinely distinct options, including process/non-software alternatives when pertinent. For each option state the expected stakeholder benefit, source evidence, dependencies, safety/privacy cost, testability and reasons it might fail.
6. Trace major consequences: normal use, denial, cancellation, data ownership, unavailable integration, rollout/operations and what changes when the number of users or devices increases. Do not invent quotas, prices, regulatory rules or lockout thresholds.
7. Surface conflicts between stakeholder incentives. Keep conflicting evidence visible instead of averaging it away. A user preference is not necessarily an approved business policy.
8. Select the smallest evidence action capable of distinguishing the live options: stakeholder confirmation, operational observation, prototype, A/B pilot, vendor contract read or a targeted technical experiment. Define an observable acceptance or rejection signal before performing it.
9. Ask a concise clarifying question only if a consequential decision cannot proceed; otherwise give the best bounded recommendation and mark open questions with their impact and next owner.

## Output and continuity

Produce a coherent decision brief: **problem and context, known evidence, competing explanations or options, consequences, recommended hypothesis, falsifiable next step, decisions confirmed, open questions and source references**. If the user specifically requests a document, adapt the current project's accepted document style. Never create \`docs/{feature}/brainstorms/\` by default, never assume \`resolve-oqs.md\` exists and never auto-promote a suggestion to an approved product requirement.

If an accepted need emerges, hand its real source to \`ba-urd\`; if a business objective is approved, to \`ba-brd\`; if a release feature is being defined, to \`ba-prd-epic\`; use \`ba-discover\` first when market demand itself remains the central uncertainty.

## Example and quality boundary

For a hypothetical rental-vehicle operator, a brainstorming question is *what decision would most reduce loss of control over a vehicle while respecting driver privacy?* Alternatives might include better rental handoff procedures, existing trackers or a custom GPS/CAN product. This is a framing example, not actual customer testimony. The output fails when it is a long list of ideas without a decision, when assumed policy is presented as fact, or when all alternatives are secretly variations of the implementation the analyst wanted from the start.

ANGENT Core handles final reasoning and writing; BA contributes structured elicitation. Provider writes, experiments and delegations require actual authorized Execution tools and subsequent verification.
