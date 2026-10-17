# Runnable D2 diagram adapter

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


The ANGENT BA D2 adapter converts **independent, source-reviewed JSON** into editable D2 scripts and optionally SVG via the actual D2 CLI. It implements a narrow, validated subset of three model families:
- Activity: start/task/guarded decision/end with optional swimlanes; checks reachability, missing guards and terminal behavior.
- ERD: entities with column types, PK/FK/unique constraints, foreign key endpoints and explicit cardinality labels.
- Logical architecture: typed components, optional subsystem groups and labeled protocol/data flows.

The emitter quotes untrusted labels, uses deterministic opaque D2 identifiers and validates graph relations. It does not automatically infer business intent from Markdown/SRS, invent database types, support D2 animations, generate arbitrary infrastructure diagrams or guarantee aesthetic quality from a successful compile. D2 layout and resulting SVG still require visual review.

## Commands from repository root

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-activity.json --output output/activity.d2

To actually render when the official D2 CLI is installed:

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-erd.json --output output/erd.d2 --svg output/erd.svg --d2 PATH_TO_D2

Optional regression run against the real renderer:

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

The generator **will not overwrite** existing source or SVG files. A controlled update should inspect the previous source/visual output, present the scoped diff and obtain permission from ANGENT Execution first. The integration test uses temporary files and verifies actual D2 exit status, nonempty SVG, useful viewBox, expected labels, and absence of active script/foreignObject elements.

D2 CLI 0.9.0 was tested on Windows with activity/ERD/architecture fixtures; source documentation and CLI invocation: https://d2lang.com/tour/man/ and https://d2lang.com/tour/sql-tables/.

D2 source generation is not proof of a real Figma canvas update. Preserve the distinction between BA semantic models, D2 SVG rendering, editable Figma nodes, and deployed application behavior.
