---
name: ba-urd
description: Elicit, verify and maintain stakeholder needs with stable UN identities, situation evidence and explicit sources; preserve accepted URD structure.
---

# User Requirements Document: stakeholder needs, not implementation

**Method background:** Independent adaptation of the MIT [Dev BA Kit URD method](https://github.com/nv-minh/dev-ba-kit/blob/main/skills/urd/SKILL.md), Edward Ngo (2026). The IIBA [Business Analysis Standard BACCM](https://www.iiba.org/knowledgehub/the-business-analysis-standard/2-understanding-business-analysis/2-2-a-model-for-effective-analysis-baccm/) defines need relative to stakeholder, value and context. The URD records sourced representations of those needs; it does not grant automatic approval to build a solution.

## What to learn before drafting

Read the user's requested feature or product scope, existing URD/research notes, meeting decisions, valid user feedback and relevant code/product evidence. Pin version/date. Distinguish **buyer**, **operating user**, affected non-user and decision owner; they may have competing needs. Describe the triggering situation and what stakeholders presently do without the proposed solution. A technology preference is not automatically a user need.

For each proposed UN, collect: role/stakeholder, situation or trigger, current job/workaround, observable friction or opportunity, expected value/outcome, boundary constraints, evidence type, exact source and confidence/approval state. Interviews must be real interviews: do not fabricate personas, quotes, market statistics or user research.

## Derivation and judgment

1. Cluster observations by stakeholder goal, not proposed button/API. Split a broad need only when different outcome measures, actors, permissions or operating circumstances demand it. Keep conflicts visible: a fleet operator's desire for visibility can conflict with driver privacy restrictions.
2. Differentiate *observed need*, *stakeholder-stated requirement*, *analyst inference* and *proposed design*. Do not relabel an unverified analyst inference as accepted simply because it sounds plausible.
3. Assign stable IDs such as \`UN-fleet-001\` following project conventions. Reuse existing IDs; moving rows never renumbers them. On removal record supersession and affected BO/CAP instead of recycling the ID.
4. Phrase each need as user-visible value in its context, with clear scope and negative constraints. "Operator must detect a vehicle missing from its expected area promptly" is a stakeholder need candidate; "install a CAN bus chip" is an implementation choice, and "show a map marker" is a design candidate.
5. Separate priority from unverified enthusiasm. Record whose urgency, consequences, frequency and evidence support it. If frequency/number is unknown, leave an explicit unknown rather than inventing it.
6. Capture unresolved conflicts and the next useful evidence to resolve them: observation, interview, operational log, feasibility study or legal review. Not every unknown requires a user question now.
7. Compare with any already approved URD before editing. Present the exact added/changed/retired UN list and any altered sources, owners or use contexts; preserve unaffected paragraphs and accepted language.

## Practical output

Adapt to the project's approved document style. A useful URD includes product/scope and source revision; stakeholders and operating settings; user jobs and current alternatives; a UN table with **ID, actor/context, required outcome, value, source/evidence, confidence/status and priority basis**; constraints (accessibility, device, privacy, environment); contradictions/open questions; decisions and trace links. Never create fixed \`docs/{feature}\` paths or automatic interview worksheets merely because a source kit assumes them.

The accepted URD can become a real \`UN\` input in the shared BA source graph. With actual project Markdown tables, \`extract_markdown_graph.py\` accepts \`--urd\`, alongside optional BRD/PRD and SRS sources. An ID's presence verifies existence only; it does not certify the need was validated.

## Grounded example and counterexample

For a hypothetical self-drive rental service: \`UN-fleet-001\`: a fleet operator needs to identify vehicles with abnormal operation during an active rental so staff can investigate before damage escalates. Source state: *hypothesis until operators confirm the situations, frequency and response needs*. Wrong: "Every rental needs real-time CAN at 1 Hz and GPS at 10 Hz"—unaccepted implementation decisions disguised as user needs. Whether drivers can view or opt out is a separate stakeholder/privacy constraint, not a silently resolved engineering choice.

## Completion

Report supported UNs and their evidence, which are still hypotheses, questions material to the next decision, coverage by any existing BO, and the exact inspected source revision. Root retains purpose, dialogue and authority; the BA specialist owns need analysis; Execution makes only authorized document changes and reads them back; Quality verifies sources and usable prose. Do not demand a compulsory upstream brainstorm or proceed automatically to a BRD when the user only asked for the needs.
