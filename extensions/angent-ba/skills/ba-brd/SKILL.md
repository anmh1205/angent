---
name: ba-brd
description: Build and validate measurable business objectives, scope, value model and policy decisions tied to actual user needs, without invented finances or approvals.
---

# Business Requirements Document: why change and how value is measured

**Method background:** Independently adapted from MIT [Dev BA Kit BRD](https://github.com/nv-minh/dev-ba-kit/blob/main/skills/brd/SKILL.md), Edward Ngo (2026), aligned with the [IIBA BACCM](https://www.iiba.org/knowledgehub/the-business-analysis-standard/2-understanding-business-analysis/2-2-a-model-for-effective-analysis-baccm/). A business objective (BO) is a desired, measurable business outcome; it must not be confused with a technical implementation ticket or a claimed benefit without evidence.

## Source and decision boundary

Read the accepted business problem, stakeholder needs, operating baseline, sponsor decisions, existing BRD/URD, relevant regulations and actual commercial constraints. Existing evidence outranks templates. If a URD does not exist, a BRD can still be drafted from direct stakeholder/operational evidence; record absent need links as unresolved rather than inventing UN IDs. The business owner, payer, operational user and risk/compliance owner may disagree.

Separate business **need**, desired **objective**, operational **policy**, proposed **solution**, and implementation **mechanism**. A policy such as "who may control a rented vehicle" has business ownership and safety/privacy consequences; it cannot be invented by a BA skill or inferred from an endpoint's presence.

## Build the actual case

1. State the current problem with an operational baseline: who experiences it, frequency, cost or severity, workaround and limitations of the evidence.
2. For each BO assign an existing or new stable ID (e.g., \`BO-fleet-001\`), list the UNs it serves, business decision owner, target outcome and time horizon. Preserve the original source link even if later documents change.
3. Define **measurement**: numerator/denominator or units, observation window, data source, baseline, target and measurement owner. "Reduce investigation time" without baseline and measurement definition remains an aspiration, not a demonstrated KPI.
4. Define scope in/out with affected customer segments, roles, workflows, assets, regions and integration obligations. Distinguish an MVP boundary from explicitly deferred work. Non-goals should answer real ambiguities rather than fill a minimum count.
5. Model business constraints and policies with actor, applicable conditions, permitted/forbidden outcome, exception and who may approve changes. Capture cross-stakeholder conflict and unresolved approvals.
6. Evaluate options: process change, manual control, integration with an existing vendor, incremental technical solution or a new platform. Describe trade-offs and operational dependencies without automatically favoring software development.
7. For cost-benefit, separate observed amounts, quotations, sourced estimates and unknowns. Identify time horizon, units, recurring support/service costs, adoption cost, risk and sensitivity. Never fabricate ROI, SLA or payback periods. A future target is not an achieved benefit.
8. Record specific risks (privacy, compliance, safety, data quality, network outage, third-party dependency, on-site support) with consequence, owner and evidence needed. Include negative operational paths, not merely sunny-day scenarios.
9. On revision, trace added/changed/removed BO back to source UN and downstream CAP/FR. Compare the current accepted BRD, preserve unrelated decisions and request approval only for genuinely undecided material changes.

## Deliverable and validation

A readable BRD includes problem and current baseline; actors/sponsor; business goals/objectives; BO table with **ID, outcome, measurement, baseline/target, owner, covers-UN and source**; scope/non-scope; policy decisions; options and cost/benefit basis; risks; unresolved questions and change history. Adapt to current project structure, not a mandated one-file \`docs/{feature}\` path.

For an actual Markdown-based BA source, the shared parser supports \`--brd\`, \`--urd\`, \`--prd\` and \`--srs\` inputs. The \`BO → UN\` edge is valid only when explicitly present in the reviewed document, and typed-link validation prevents downstream tests from being mistaken for sources of business objectives. No computed coverage number means stakeholder approval.

## Illustrative example

A rental operator *might* want to shorten the time from abnormal vehicle behavior to operator investigation. A proposed BO can define median minutes from a well-specified telemetry alert to an acknowledged investigation, compared with a measured baseline over an agreed period. Without pilot observations, both the baseline and target must be labeled pending, and costs such as device installation/support cannot be quietly treated as zero. "Deploy MQTT with 99.99% uptime" is an engineering decision or NFR candidate—not the business objective itself.

## Gate

Every objective must answer: whose value, in which situation, how measured, sourced from which need or direct business decision, who owns the decision and what would falsify its benefit. Root retains business judgment and permission; BA owns objective/constraint analysis; Execution changes only authorized documents; Quality checks coherent, defensible results. A BRD is not automatically approved because its table is complete.
