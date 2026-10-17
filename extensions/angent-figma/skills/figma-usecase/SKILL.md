---
name: figma-usecase
description: Specialized usecase analysis and editable Figma presentation when actual host tools permit.
---

# Use case model in Figma, not a renamed userflow

## Semantics before geometry
The system boundary encloses services the product promises. Human or external actors remain outside. Each ellipse names an actor-visible goal at the correct level of abstraction, not a UI click. Association expresses actor participation. Include is mandatory reused sub-behavior; extend is optional or conditional addition with an explicit extension point. Generalization requires real substitutability.

## Construct
1. Use current actor, use-case and scope inventory from BA usecase/SRS. Separate primary actor from external authorization/payment services.
2. Create actor IDs and use-case IDs with accepted project names. Record trigger, result, preconditions and minimal guarantee for each.
3. Build association, include, extend and inheritance edge tables. Every include and extend edge needs a defensible semantic reason. The system boundary must not include an externally owned service.
4. Audit completeness: every P0 capability has at least one actor goal; every actor has a justified interaction; no goal is a decorative screen label.
5. For Figma, inspect target file, existing page and diagram tool availability. A Pro-style use-case diagram is not supported by Reqwise OSS six-kind figma_diagram. Use an actually available native Figma write tool with explicit frame/shape primitives only when authorized; otherwise provide a verified model and renderable UML source.
6. Arrange actors outside, use cases inside, relation labels readable; preserve editing and stable IDs. After a native write, read back and check missing edges and clipping.

## Deliverable
A machine-readable actor/usecase/relationship list and a reviewable diagram or renderable fallback; source SRS references and outstanding business boundary questions.

## Quality failure examples
A login button is not a goal. Password reset is a standalone goal when the user wishes to recover access. Sending an email may be an included service step, not necessarily an actor goal. Do not fabricate regulatory actors or assume a relationship exists merely because two diagrams share a noun.

## Reference
OMG UML use-case semantics; source of system/actor decisions must be from the approved BA artifact, not from diagram aesthetics.


## ANGENT authority

Root selects capabilities; BA owns source business decisions, Frontend supports art direction when necessary, Execution performs authorized Figma calls and read-back, Quality verifies semantics and rendering.
