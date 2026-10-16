---
name: ba-usecase-diagram
description: Source-driven UML use-case diagram design, with optional verified offline rendering and no surprise remote uploads.
---

# Business use-case model and diagram source

**Origin:** MIT Dev BA Kit by Edward Ngo (2026), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/usecase-diagram/SKILL.md. ANGENT retains user authority.


## Business semantics

A UML use-case diagram expresses *actor-visible goals* at the actual system boundary, not a UI navigation map or list of internal services. Actors stand outside; each use case names a meaningful result. Include means mandatory reused behavior, extend requires an optional extension point, and generalization must reflect valid substitution.

## Method

1. Read accepted SRS/URD/use cases and identify system scope, actors, goals, external systems and requirement IDs.
2. Capture stable use-case ID, actors, trigger, observable outcome, preconditions, error guarantee and linked FR/BR/AC. Keep internal algorithms in the specification, not necessarily separate ellipses.
3. Validate actor associations, include/extend/generalization semantics, coverage of priority capabilities, authorization boundaries and contradictions.
4. Produce a typed actor/usecase/relation model first. Reuse existing IDs and labels; do not invent user goals solely to fill a graphic.
5. When PlantUML is requested, author an editable source file using a real local source editor. A hosted renderer is never the default.
6. Render only with an installed, vetted LOCAL PlantUML JAR/CLI (for example java -jar PATH_TO_PLANTUML_JAR -tsvg INPUT.puml) and an authorized command. No Java/PlantUML binary is bundled or guaranteed by ANGENT. A source file is not a rendered image.
7. For Figma, check whether a genuine provider can create and read back use-case shapes. Reqwise OSS's six diagram kinds do not include Pro use cases; never invent a native Pro endpoint. If unavailable, deliver source and report not written.
8. Examine any real output for actor placement, omitted goals, wrong include/extend direction, illegible labels, leaked sensitive wording and broken boundary.
9. Before changing an accepted file, present a source-scoped diff and use ANGENT Execution's actual permission and read-back rules.

## Example (unrendered PlantUML source)

    @startuml
    left to right direction
    actor "Rental operator" as Operator
    actor "Maintenance technician" as Technician
    rectangle "Fleet management" {
      usecase "Review vehicle status" as UC_Status
      usecase "Inspect fault history" as UC_Fault
      usecase "Verify vehicle ownership" as UC_Owner
    }
    Operator --> UC_Status
    Technician --> UC_Fault
    UC_Status ..> UC_Owner : <<include>>
    @enduml

This is an illustrative candidate only. Whether ownership verification deserves a separate actor-visible use case must be decided from the accepted product semantics; authorization is often better modeled as an SRS guard.

## Security and boundaries

Do not send customer policy, role descriptions, process source or proprietary diagrams to plantuml.com or another third-party service without explicit permission. Do not claim compilation when no local renderer exists. Use ba-d2-activity or another verified offline representation for different modeling needs but never mislabel it as exact UML equivalence.

ANGENT Root owns source authority and intent, BA owns UML semantics, Execution owns files/providers and Quality verifies the real artifact. There are no mandatory Claude L1/L3 gates or fictional render.sh tool.
