---
name: ba-prd-epic
description: Define scoped, prioritized product capabilities CAP from approved objectives and user jobs, with measurable acceptance boundaries and honest release dependencies.
---

# Feature PRD: translate outcomes into bounded product capabilities

**Method:** Independently adapted from MIT [Dev BA Kit PRD-epic](https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prd-epic/SKILL.md), Edward Ngo (2026). BA owns the product's capability semantics; ANGENT Root decides scope and final presentation; Engineering and Frontend specialists elaborate implementation and visual constraints when necessary.

## Establish the right altitude

Read the accepted BO/UN decisions, product strategy, current feature map, existing capability specs and userflow, if any. A capability describes what a stakeholder can accomplish, not a particular library, database table, firmware driver, API endpoint or UI widget. A business objective is the value sought, not itself a product capability. The SRS will later define required observable system behavior.

If an approved objective is absent, capabilities can be proposed but cannot be falsely marked as satisfying an existing BO. Keep any source gap visible.

## Shape and prioritize the feature

1. Identify the actor and initiating situation, intended outcome, current limitations and system boundary. Separate user-facing behavior from internal supporting services; note the supporting services only when they change capability feasibility.
2. Enumerate candidate capabilities at comparable size. Give each a stable \`CAP\` ID and a sourced BO (or explicitly unresolved objective), plus the stakeholder and observed outcome it supports. Preserve previously accepted IDs and priority justifications.
3. Define the capability's state and denial boundary: permissions, eligible objects, offline/error condition, user cancellation and recovery. These are not detailed SRS cases yet but must be known enough to prevent the PRD hiding important risk.
4. State non-goals as substantive exclusions, with reason and operational consequence. A non-goal is not a convenient way to ignore safety, privacy, quality or a previously accepted business rule.
5. Prioritize by *value to the defined actor and objective, necessity, risk and dependency*, not a ritual P0/P1/P2 count. If priority is unknown, say so; avoid claiming a hypothetical MVP or launch commitment. Preserve a decision record describing what evidence made an item P0.
6. Identify external capabilities, data ownership, device/network restrictions, vendor/regulatory constraints and integration order. Mark observed existing support versus a proposed future dependency, along with risk if unavailable.
7. Describe an iterative release slice: a coherent customer journey or operator outcome with testable boundaries, not an arbitrary collection of UI components. Distinguish usable review prototype, internally testable pilot and customer release.
8. Check every BO that the feature claims to serve: which CAP supports it, what is out of scope, whether the value metric is measurable, and whether the proposed capability can plausibly affect it. Many-to-many mappings are allowed with explicit justification.
9. Update an existing feature PRD through a scoped, source-linked diff. Surface new/retired CAPs and resulting FR/AC/test impacts; never silently overwrite accepted prioritization or rename IDs after moving rows.

## Deliverable

Use the project's accepted product documentation style. Include problem/buyer and target user; goals and explicit non-goals; release scope; capability table **CAP ID, actor, expected outcome, priority and basis, covers-BO, source/revision and unresolved risks**; dependencies, critical scenarios, exclusions and product decisions. Linking a CAP to a BO is evidence lineage, **not mathematical proof the objective will be achieved**.

With actual Markdown sources, \`extract_markdown_graph.py\` supports \`--urd --brd --prd --srs\` and identifies missing UN→BO→CAP→FR paths. A passing structural trace cannot substitute for stakeholder review or real user testing.

## Example and failure mode

A rental fleet capability might let an operator view vehicles with verified authorization and see last-known telemetry freshness. That is a business-facing CAP candidate. "Implement a Redis cache" is not a CAP; "make every telemetry message available within two seconds" is an NFR candidate requiring measured context and agreed conditions. If the operator cannot inspect faults when the device is offline, the PRD should state whether cached fault history is in scope instead of hiding the degraded case.

## Handoff and completion

List confirmed CAPs, proposal-only CAPs, dependencies and unresolved decisions; identify the subset that can be specified in an SRS now. Do not force a fixed template hierarchy, automatic Jira issue creation or immediate implementation. ANGENT Execution governs authorized files/providers and Quality checks product meaning against cited evidence.
