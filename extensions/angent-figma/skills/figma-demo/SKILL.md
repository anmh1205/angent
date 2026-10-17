---
name: figma-demo
description: Specialized demo analysis and editable Figma delivery when runtime support is proven.
---

# Create and verify a stakeholder Figma prototype walkthrough

## Product intent
A demo is a staged review of a realistic user goal and business decision. It must make clear which interactions are real Figma prototype reactions, which behaviors are simulated, and which integrations are not implemented. Do not conflate an animated video with a test of business logic.

## Scenario design
1. Identify the demonstration audience and the concrete outcome: approve a flow, validate information hierarchy, discover missing screens or compare competing interaction designs.
2. Read the accepted userflow, screen inventory, error matrix, roles and requirements. Select a bounded scenario covering normal path plus at least one business-critical alternative.
3. Map every step to frame ID, trigger, expected transition and actual destination. Check navigation graph reachability, restart point, modal dismissals, return paths and state reset.
4. Read existing Figma prototype reactions using actual provider tools. For authorized edits, set prototype reactions and actions using the current Figma API; for dynamic document access, the documented Plugin API requires setReactionsAsync rather than assigning read-only reactions.
5. Inspect the created interactions by read-back, not by assuming the tool call succeeded. Run the walkthrough in prototype mode if available; check target frame, trigger, state and user-visible feedback at every step.
6. Add scenario narration grounded in the approved requirements and a presenter script that names unresolved issues, next decisions and mock limitations.
7. If recording video is requested, verify the current host genuinely supports capture/export and produce an actual file with readable playback. Otherwise provide a self-playing storyboard plan without claiming a video was generated.

## Output
Scenario ID; frame sequence; interaction table; approved claims; mock boundaries; alternate route; verified prototype read-back; recording path only when a real file exists.

## Failure criteria
Unreachable screens, clicks without transitions, broken overlays, surprise loops, missing denial path, falsely claimed live API success or an inaccessible video. The public MIT Reqwise package does not provide the Pro automated recording feature.

## API reference
https://developers.figma.com/docs/plugins/api/properties/nodes-reactions/


## ANGENT coordination

ANGENT Root owns task/authority, BA owns business evidence, Engineer/Frontend provide independent UX or visual specialization when genuinely needed, and Execution/Quality own tool effects and read-back.
