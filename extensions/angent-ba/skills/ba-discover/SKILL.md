---
name: ba-discover
description: Investigate product opportunity, competitors, customer need and go/no-go experiments; or inspect a brownfield project when requested.
---

# Product opportunity discovery and project discovery

**Origins:** The public AI4BA BA-Kit describes \`/discover\` as investigating an uncertain idea, customer need, competitors and whether to pursue it (https://ai4ba.com/ba-kit). The MIT Dev BA Kit (Edward Ngo, https://github.com/nv-minh/dev-ba-kit/blob/main/skills/discover/SKILL.md) instead discovers an **existing repository**. ANGENT supports both with explicit mode selection; they must not be conflated.

## Select the question to answer

**Opportunity mode — default for a new or uncertain idea.** Answer: *Whose problem is serious enough to solve, what alternatives exist, why could our solution win, and which evidence would justify investing?* Deliver a decision with unknowns, not automatically a PRD or a commitment to build.

**Project mode — for an existing product/codebase.** Answer: *How does this system currently work, which product decisions are accepted, and what can be reused without inventing facts?* Use only when the user asks about an existing repo, system or historic project. This is the narrower Dev BA Kit method.

## Opportunity mode — disciplined investigation

1. **Frame the opportunity** in terms of IIBA's need, stakeholder, context, proposed change, value and candidate solution. Name the buyer, user and affected operators separately. Avoid starting with a component list or technical implementation.
2. **Describe the job and observed friction:** triggering situation, existing workarounds, frequency, consequences, willingness or ability to pay and decision-maker. Capture actual quotes or records only from inspected sources, with participant/date/context; a plausible persona is a hypothesis.
3. **Research the present market and substitutes:** direct competitors, incumbent processes/spreadsheets/in-house systems and "do nothing". For each claim record product/provider, the current source URL and retrieval date, audience, offered capability, pricing basis if verified and source limitations. An unsourced vendor comparison cannot support a go/no-go verdict. Avoid invented market-share numbers and false feature comparisons.
4. **Distinguish evidence levels** for each need: observed customer behavior, verbatim interview, quantified operations record, verified market source, documented inference or untested assumption. A competitor feature or a high search result ranking does **not** establish demand from the intended buyer.
5. **Map alternative solutions:** non-product/process change, minimum technical intervention, whole platform, partnership/buy/build. Record cost/risk/operational trade-offs without fabricating estimates. The best pilot is often narrower than the end-state architecture.
6. **Assess commercial and operational viability:** reachability of first customers, buying process, installation/service obligations, competition, support/safety/privacy/regulatory constraints, dependency on external data or integrations, adoption friction and exit cost. A technical demo alone does not validate willingness to pay.
7. **Design falsifiable next evidence:** interview or observation questions that do not lead respondents, a specific workflow pilot, customer recruitment basis, measured baseline, decision threshold and time/budget owner. Never assert that an experiment ran because its plan exists.
8. **Conclude with a qualified decision:** PROCEED-TO-DISCOVERY (sufficient signal for a bounded pilot), PIVOT-HYPOTHESIS (evidence favors another segment or intervention), HOLD-UNTIL-EVIDENCE (material unknowns), or STOP (observed disproving evidence). These are decision recommendations, not automatically authorized development or business investments.

## Expected opportunity output

A readable opportunity brief should state: problem and current alternatives; buyer/users and setting; evidence ledger (claim, type, source/date, uncertainty); competitor/substitute comparison; distinct solution hypotheses; value/risk model; falsifiable experiment plan; options with trade-offs; **why the decision follows from the evidence**; and the unresolved questions that could reverse it.

If no user/customer evidence exists, favor HOLD-UNTIL-EVIDENCE or a bounded discovery pilot. Do not fill empty fields with fictitious interviewees, fake pricing or a fabricated survey.

## Existing-project mode

1. Fix exact repo/branch/source revision, intended system scope and accepted project documentation. Read existing README, AGENTS.md, relevant requirements, decisions, issues, architecture and implementation evidence.
2. Trace important actor jobs and accepted business rules through actual code paths (entrypoint, authorization, domain logic, persistence, async integration) only to the depth relevant to the task. Distinguish approved future behavior from implemented and deployed behavior.
3. Mark every material finding as accepted decision, direct source observation, inference, runtime observation or unknown, with exact source path/version. Surface conflicting sources rather than choosing the newest file automatically.
4. Produce a compact reuse-oriented project profile and list consequential unknowns. Only update existing project docs when authorized; do not impose a new \`docs/_shared\` tree or shadow memory service.

## Worked decision framing

For a *hypothetical* GPS/CAN rental-fleet product, the buyer may be the fleet rental operator, whereas the driver is an affected user. The job is reliable oversight of vehicle location, misuse, faults and maintenance—not "use FreeRTOS" or "optimize the energy budget." Alternatives include spreadsheet coordination, existing trackers and existing fleet software, **which must be researched in the target market**. A bounded pilot could measure incident detection delay and operator interventions across a few vehicles. This example is not a market finding, customer interview or tested business opportunity.

## Hand-off without forced workflow

Opportunity evidence can inform \`ba-prd\`, \`ba-roadmap\`, \`ba-urd\`, \`ba-brd\` or a deliberate STOP. Do not manufacture UN, BO or CAP IDs from hypotheses or silently upgrade them to accepted requirements. Existing project findings feed \`ba-srs\` or \`ba-doc-drift\` where genuinely needed. ANGENT Root keeps strategic judgment, research authority, project continuity and final explanation; the specialist adds the domain method.

**Official conceptual sources:** IIBA Business Analysis Core Concept Model (https://www.iiba.org/knowledgehub/the-business-analysis-standard/2-understanding-business-analysis/2-2-a-model-for-effective-analysis-baccm/) and BABOK knowledge area overview (https://www.iiba.org/).
