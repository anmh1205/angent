---
name: ba-discover
description: ANGENT BA specialist for discover with source evidence, host authorization and real tool boundaries.
---

# Project discovery and source-grounded BA context
**Source:** Maintained adaptation of the MIT Dev BA Kit by Edward Ngo (2026), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/discover/SKILL.md. ANGENT Root/Core retains final authority.



## Goal

Build a compact and useful model of the product, actual actors, business rules and system boundaries by reading authoritative sources. This method does not introduce a second memory service, compulsory interview, scheduled loader or project checkpoint.

## Investigation

1. Fix the requested product/repository and revision; read the existing README, AGENTS.md, approved product/SRS/BRD, issue decisions and architecture documentation. Respect the user's source-of-truth choices.
2. Derive the user job, paying customer, operational actors and decision ownership. Trace accepted needs to capabilities and relevant FR/BR only as far as this task requires.
3. Inspect real code where current implementation matters: entrypoints, routes/permission guards, domain services, storage schemas, async work, device/cloud protocols and tests. Pin commit/source paths. Avoid an exhaustive scan when a small decision path is sufficient.
4. Mark every material conclusion as accepted stakeholder decision, documented proposal, source-observed behavior, inference or runtime-unverified. Code behavior is not automatic business approval.
5. Detect naming collisions, missing business owner, stale documents, contradictory revisions, untested exceptions and genuine external integration assumptions. Keep the specific evidence behind each.
6. Ask only questions that can change a consequential decision or prevent an incorrect requirement. There is no mandatory set of five questions and no required artificial approval stage for read-only discovery.
7. Deliver a readable profile with product goal, paying/user audience, process stages, actors, business rules, data ownership, integration boundaries, current implementation limits and open questions, each grounded where material.
8. If a durable artifact is requested, adapt the profile to existing project docs or accepted handbook. Preserve human-edited sections and prior decisions; do not invent a forced docs/_shared hierarchy or overwrite AGENTS.md.
9. On refresh, compare current sources with the previous accepted artifact, propose a bounded diff and mark uncertain claims for review rather than auto-promoting guesses.

## Evidence and execution

Use actual available tools, not uninstalled Claude Task subagents or scripts/context-load.sh. Independent reviewers are optional only if an authorized runtime exists. Do not claim an exhaustive source scan when only selected modules were read.

For a self-drive rental fleet product, the operator need is to locate vehicles, identify abnormal operation and ECU diagnostic faults and manage maintenance. FreeRTOS/CAN/GPS are technical means that support those business capabilities, not automatically the buyer's desired outcomes. Verify which pieces exist before saying the platform is deployed.

ANGENT Root retains context continuity and interpretation; this BA method provides specialist business-domain evidence rather than a new local memory layer.
