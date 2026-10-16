---
name: ba-activity-swimlane
description: ANGENT BA specialist for activity-swimlane with source evidence, host authorization and real tool boundaries.
---

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


# Multi-actor activity/swimlane process diagrams
**Source:** Maintained adaptation of the MIT Dev BA Kit by Edward Ngo (2026), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/activity-swimlane/SKILL.md. ANGENT Root/Core retains final authority.



## Use the right representation

Swimlane diagrams distinguish responsibility, handoffs and alternative outcomes. When the user wants a rendered image from the installed portable ANGENT kit, use ba-d2-activity and the tested local D2 compiler. For actual PlantUML lane syntax, produce a reviewable editable .puml file and render only if a vetted LOCAL PlantUML runtime is present. Use ba-bpmn for real BPMN interchange.

## Model the business, not the layout

1. Read the accepted source (SRS, UC, approved process owner decisions) and record revision. Identify trigger, owner for each task, decision guards, all normal and failure outcomes, cancellations and recovery.
2. Assign a true owner to every task; switching lanes denotes a real handoff. Do not place an API call in the customer's lane simply because the customer initiated the flow.
3. Confirm ambiguous actors only if the missing actor changes the model. Do not use a compulsory interview or force a fresh feature folder.
4. Make decisions complete: every branch has a guard and an outcome. Do not invent retry limits, refund policy or lockout thresholds. Model loops and parallels only with semantics supported by the chosen notation and renderer.
5. Use stable IDs for an independent model, or preserve approved labels from an existing PlantUML source. Compare source-to-diagram behavior before rendering.
6. For D2, create JSON with type activity, nodes carrying id/kind/label/lane and edges carrying from/to/guard for decisions. The portable compiler checks lane ownership, target IDs, guards and reachability.
7. For PlantUML, place a lane marker immediately before its owned activity. Re-declare owner lanes inside if/else branches and loops. Terminate every path or show an explicitly justified continuation.
8. Open the actual SVG/PNG if generated. Verify lane boundaries, edge direction, readability, visible labels, decision coverage, dead ends and handoffs. A valid image does not prove the correct business process.
9. Preserve existing source and diagrams on revision. Present an authorized scoped diff before overwriting files; report the renderer actually used and unrendered outputs honestly.

## Verified local D2 route

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-activity.json --output output/activity.d2 --svg output/activity.svg --d2 PATH_TO_D2

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

D2 successfully rendered an example activity with lane ownership and authorization decision. The fixture is synthetic and not proof of production process correctness.

## PlantUML-specific alternative

Editable source example:

    @startuml
    |Customer|
    start
    :Request vehicle return;
    |System|
    :Validate agreement;
    if (Return permitted?) then (yes)
      |Agent|
      :Inspect condition;
      stop
    else (no)
      :Explain rejection;
      stop
    endif
    @enduml

Only if LOCAL Java and a trusted PlantUML JAR actually exist, run an authorized equivalent of java -jar PATH_TO_PLANTUML_JAR -tsvg INPUT.puml. Inspect the resulting file and all paths. Neither Java nor a PlantUML JAR is guaranteed in the ANGENT packages.

**Privacy:** Never send project/process source to plantuml.com or another remote rendering service as a default or hidden operation. If no offline renderer exists, present source explicitly as unrendered or use the tested D2 renderer.

ANGENT Root retains task authority, Execution handles file writes and real tools, and Quality compares diagram semantics to the accepted business evidence. No Claude L1/L3 gates, fictional render.sh helper or automatic remote rendering.
