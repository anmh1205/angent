---
name: ba-prd
description: Evidence-driven business analysis for prd with approved source identity, testable outcomes and non-destructive handoff.
---

# Product PRD: decide what product should accomplish, for whom, and why

**Method origin:** An independently maintained adaptation of the MIT Dev BA Kit product PRD workflow by Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prd/SKILL.md. Requirements principles follow IIBA business analysis concepts. The document is subordinate to the user's current project sources, not a compulsory global singleton.

## Product versus capability specification

A product-level PRD explains market/problem context, target buyers and operators, product boundaries, differentiated value, outcomes, major features and adoption/risk assumptions. It is broader than \`ba-prd-epic\`, which specifies one CAP-level capability; \`ba-srs\` describes testable system behavior. Do not force a second whole-product PRD when an accepted product PRD already exists, or require creation of \`docs/_product/prd.md\` if the project uses Notion/Confluence or another layout.

## Ground every consequential decision

1. Inspect current accepted product vision, discovery notes, buying stakeholder evidence, any existing PRD, roadmap, business objectives, deployed feature facts and external constraints. Pin the revision and distinguish observed, approved, proposed and unknown statements.
2. State the job/problem at the buyer/user level, the present alternatives and specific friction. Separate paying customer from daily operator and affected third parties; distinguish marketing promises from verifiable operating outcomes.
3. Identify candidate product positioning, critical user segments and defensible differentiation. Market size, pricing, competitors, willingness to pay and forecasts must use actual current evidence or remain hypotheses.
4. Translate needs and BOs into a **feature map**: stable feature/CAP identity, actor, desired outcome, supporting business objective, in/out scope and evidence/status. Do not mint canonical slugs or renumber accepted IDs merely because the source kit prefers folders.
5. Define concrete success measures with baselines, units, observation window, owner and source; unknown values are research actions, not fabricated targets. Keep leading adoption signals separate from demonstrated customer value.
6. Document first-release boundaries and scenarios: successful core job, access denials, outage/degraded operation, data ownership and privacy, integrations, installation/support where physical products are involved. Do not omit high-consequence exceptions because the PRD sits above the SRS.
7. Assess feasible delivery options and constraints: customer recruitment, hardware supply/service, engineering capacity, provider contracts, compliance, cost/risk and actual roadmap commitments. Product goals can remain ambitious while the first pilot remains bounded.
8. Explain alternative product strategies and the resulting trade-offs, e.g., build versus integrate, feature breadth versus reliability, self-serve versus assisted onboarding. Tie recommendations back to the user's objective, not a generic template score.
9. On update, compare against the approved baseline: which capabilities or assumptions were added, modified, removed or deferred, and what URD/BRD/SRS/roadmap downstream review they imply. Preserve unaffected paragraphs and real human decisions.

## Deliverable and verification

Write in the project's existing style: concise product thesis, evidence-based customer/problem analysis, outcome/measurement model, value proposition and alternatives, current/product scope, feature-map with source IDs, minimum usable pilot, key scenario boundaries, dependencies, risks, open decisions and next validation. A reader should understand what is intended, how it would create value, and what is still unproven without reading a chain of generated checklists.

The PRD is successful when a stakeholder can challenge its assumptions, trace important features to actual buyer needs, and decide the next investment/test. **A detailed implementation specification, an approved release and a tested product are not implied by a written PRD.** If the user only asks for a focused feature PRD, route to \`ba-prd-epic\` instead of writing a whole-product document.

For a hypothetical rental fleet product, the operator's ability to investigate location/usage anomalies and ECU diagnostic needs is a plausible opportunity; GPS/CAN architecture is a technical solution candidate. Claims about local customer pain, costs and adoption must be validated, not copied from this example.
