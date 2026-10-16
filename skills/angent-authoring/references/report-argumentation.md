# Report argumentation — findings that support decisions

Use for research, audit, status, technical incident and strategic recommendation reports. This is a method, not a compulsory outline. The reader's decision and the evidence determine sections and depth.

## Establish the decision

Identify who uses the report, which decision or understanding they need, the exact target/version/scope and the uncertainty that could reverse the conclusion. Start a substantial report with a bounded supported result and its stakes, not an inventory of activities.

Build the argument from real evidence:
- Claim/condition: what is observed, at which target, version and scope?
- Criterion: what requirement or comparison makes that state significant?
- Warrant: why does the evidence support the finding? Which alternative explanation would change it?
- Cause: what mechanism is established? If unknown, treat causes as hypotheses.
- Effect: what consequence is observed, plausibly inferred or unmeasured?
- Recommendation: what action addresses the cause or constraint, and how would its effect be verified?

Do not invent any of those components merely to complete a template. A difference is not automatically a defect, and a passing test establishes only its tested property.

## Genres and reader purpose

Research: synthesize claims across sources and reconcile disagreement rather than reporting one source after another. Separate evidence, model, inference and decision-changing uncertainty.

Audit: distinguish actual condition from governing criterion, prioritize findings by supported consequence and repair dependencies, and identify what was sampled or uninspected. A sample cannot certify a whole system.

Operational status: lead with verified completion and remaining/unverified work. Distinguish attempted, pending, failed, blocked and confirmed operations. An opened PR or a successful tool response is not necessarily a deployed user-facing outcome.

Technical incident: establish symptoms and scope, reconstruct the relevant data path or timeline, compare competing causes and distinguish mitigation from verified remediation.

Recommendation: start with the underlying need, compare viable options on decision-reversing constraints and explain what evidence would change the choice. A generic pros/cons table is not sufficient.

## Report-wide coherence

The opening makes a bounded claim, the body earns it, and the ending integrates action or remaining uncertainty without repeating the table of contents. Sections need a real decision, mechanism or evidence boundary. Use paragraphs for connected reasoning, lists for genuinely parallel findings, tables for comparable measures and figures only when they expose a material relation.

Place citations at the claim they support; evidence for an observation does not by itself prove a proposed cause. Severity and completeness must stay within the inspected scope. If the claim-to-action link fails, return the missing mechanism to Research or Reasoning, not a cosmetic prose revision.

## Revision and evaluation

Preserve accepted strengths and repair the dependency that generated the problem, rather than changing only the cited sentence. Evaluate candidate and baseline on real matched model/host outputs across substantive reports, short responses and negative controls. Skill text and CI source checks cannot demonstrate behavioral superiority.
