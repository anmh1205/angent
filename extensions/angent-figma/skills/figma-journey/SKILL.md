---
name: figma-journey
description: Specialized journey analysis and editable Figma presentation when actual host tools permit.
---

# Evidence-grounded journey map with service and user perspectives

## Boundary
Journey maps describe a real or hypothesized user experience over time: user goals, contexts, actions, touchpoints, pain, perceived effort and opportunities. Userflow describes navigational states; service blueprint describes frontstage and backstage service responsibilities. These are related but not interchangeable.

## Research first
1. Name the user segment and end-to-end job, timeframe and exact beginning and ending conditions. Check actual research/interview/analytics evidence and avoid invented behavior.
2. Split the journey into meaningful stages and record entry, action, motivation, expectation, touchpoint, system/service response and outcome.
3. Record evidence references for each observed pain, quote or emotion. Inferred opportunities get hypotheses and validation experiments, never fabricated certainty or emotional scores.
4. Incorporate failure and recovery stages, interruptions, cross-device transitions, accessibility barriers and handoffs to support teams or third parties when relevant.
5. Evaluate which opportunities have demonstrated frequency/severity and which are low-confidence ideas. Avoid using numerical priority or satisfaction without source data.
6. Translate stage cards to Figma using existing typography, spacing and approved visual tokens when an authorized Figma writing tool exists. Use editable frames/text nodes and preserve stable stage IDs.
7. Read back node inventory and view at stakeholder width; check text truncation, mobile readability and source footnotes.

## Output schema
Journey ID; actor or segment; stage ID; stage goal; observed action; touchpoint; evidence and confidence; user pain/positive outcome; service response; opportunity; testable next decision.

## Quality checks
Do not duplicate a userflow box-per-screen. Do not assume every stage feels frustrating. A support escalation may be a major interaction even if there is no app screen. Journey output must expose unknowns and research gaps.

## Figma execution
There is no journey kind in the public Reqwise OSS figma_diagram API. Do not call a fictional Pro tool; construct only if actual native Figma capabilities are available and permission granted, otherwise deliver the structured map and alternate HTML/diagram specification.


## ANGENT authority

Root selects capabilities; BA owns source business decisions, Frontend supports art direction when necessary, Execution performs authorized Figma calls and read-back, Quality verifies semantics and rendering.
