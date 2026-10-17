---
name: ba-d2-architect
description: Source-traceable BA d2-architect D2 modeling using tested JSON-to-D2 and real SVG rendering when available.
---

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


**Method origin:** maintained independent adaptation of the MIT Dev BA Kit /d2-architect skill, copyright 2026 Edward Ngo, https://github.com/nv-minh/dev-ba-kit/blob/main/skills/d2-architect/SKILL.md. Original ANGENT generator; no commercial AI4BA source included.

# D2 logical architecture and data-flow diagrams

## Scope

Show logical actors, devices, services, queues, stores, integration boundaries and data transfer responsibilities. Do not confuse this with a measured production topology, cloud provider configuration or complete security-threat model.

## Modeling procedure

1. Determine the exact system, feature, revision and intended reader. Inspect accepted product capabilities, protocol contracts and current implementation evidence where relevant.
2. Distinguish observed real components from proposed alternatives. Assign unique stable IDs and descriptive labels to each logical component.
3. Use supported component kinds: service, database, queue, user, external, device or boundary. Group them into an actual functional or ownership area only where justified.
4. Declare directed edges with source, destination and explicit protocol/data meaning. Examples include MQTT/TLS telemetry, HTTPS status read and fault-event delivery, but only use these if they match inspected project sources.
5. Identify trust boundaries, data sensitivity, tenant ownership, authentication and downstream failure behavior where materially relevant.
6. Build JSON of type architecture with title, direction, nodes with id/kind/label/optional group, and edges with from/to/protocol. See extensions/angent-ba/examples/d2-architecture.json.
7. Run the ANGENT D2 compiler; validate all edges and labels. Where the official D2 CLI is present, render actual SVG and inspect clipping, group labels, arrow direction, cross-boundary semantics and logical component relationships.
8. On revisions, preserve accepted stable IDs and unaffected components. Present the scoped diff before any authorized source overwrite or publication.

## Executable commands

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-architecture.json --output output/architecture.d2

    python extensions/angent-ba/scripts/build_d2.py INPUT.json --output output/architecture.d2 --svg output/architecture.svg --d2 PATH_TO_D2

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

## Acceptance and uncertainty

Each component is observed or expressly proposed; arrows have direction and meaningful labels; boundaries reflect genuine responsibility; images are legible when rendered; no unsupported deployed-environment claim is made. The tool compiles a bounded logical model, not exhaustive C4, deployment IaC or verified live traffic.

## ANGENT cooperation

Root owns intent, selected methods and permission scope. BA models logical dependencies and the business data exchange. Engineer may supply implementation/topology evidence when requested; Execution invokes a real D2 renderer and inspects the output. Quality compares it with the accepted source, not only the drawing.
