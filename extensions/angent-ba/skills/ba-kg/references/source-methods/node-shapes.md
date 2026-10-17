# Semantic shapes supported by ANGENT diagrams

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


**Provenance:** Adapted from MIT Dev BA Kit / rules/node-shapes.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Shape names below reflect current ANGENT's bounded JSON-to-D2 compiler rather than the complete D2 shape library.

## Select kind from actual meaning

| Diagram source kind | Actual emitted D2 shape | Meaning and verification |
|---|---|---|
| Activity start or end | circle | Start trigger or terminal outcome |
| Activity task | rectangle | Real action owned by an actor/lane |
| Activity decision | diamond | Guarded branches, at least two outgoing |
| Architecture user | person | External actor rather than internal process |
| Architecture service/external/device/boundary | rectangle | Explicit component; grouped boundary when specified |
| Architecture database | cylinder | Durable data store |
| Architecture queue | queue | Event/message transport |
| ERD entity | sql_table | Declared fields, primary/foreign/unique constraints |

The Python compiler in extensions/angent-ba/scripts/build_d2.py validates these kinds and field/edge relationships. It does not implement every native D2 shape or AWS/Azure stencil, and it does not automatically derive technology from dependencies.

## Selection rules

Choose the closest supported honest type; never relabel a queue as database or a decision as a task merely for a visual effect. Distinguish external service from an owned backend by grouping/boundary and labels, not just colors.

For an ERD, preserve actual column and relationship semantics; a pretty table that omits the owner foreign key is incorrect. For process lanes, every actor-owned step needs a declared lane when lanes are used.

## Icons and styles

Decoration is optional. This kit does not ship an automatic icon resolver with default network downloads. See icon-map.md for licensing and privacy. Use the project's real design system or restrained accessible defaults instead of hard-coded provider palettes.

## Test the result

A valid input JSON and D2 source are only structural evidence; run the official D2 CLI and inspect SVG geometry and labels to claim rendering. The synthetic three-diagram smoke can run via tests/integration/check_d2_cli.py --d2 PATH_TO_D2. Verify actual project business meaning independently.
