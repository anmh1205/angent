---
name: ba-kg
description: Specialized ANGENT business analysis kg method.
---

# Knowledge graph of evidence and BA artifacts

## What the graph represents

Use a directed, typed, project-scoped graph, not a second memory backend. Nodes are user needs, business outcomes, capabilities, FR/NFR/BR, actors, stories, acceptance criteria, tests, UI screens, API contracts, source observations and stakeholder decisions. Edges describe *derives_from*, *constrains*, *implements*, *verifies*, *visualizes*, *supersedes* or *depends_on*. IDs and revisions are stable. The current project repository or connected provider remains source of truth.

## Build algorithm

1. Inventory authoritative artifacts and define a bounded feature scope plus explicit project revision. Parse frontmatter, index tables, anchored links, source references, acceptance criteria and IDs.
2. Resolve aliases and duplicate identifiers. Never silently unify two requirements solely because their titles sound similar.
3. Record typed edges; store the original textual citation or source row for each relation. Relationship without a citation is an inferred edge and must be labeled.
4. Verify referential integrity: every local edge endpoint exists or declares a resolvable external provider target. Detect self-links, cycles in derivation and dangling version references. Some business feedback loops are legitimate; do not conflate them with derivation cycles.
5. Compute reverse dependencies for changes and requirement-to-test reachability. Report coverage with actual numerator and denominator, plus exclusions or unverifiable gaps.
6. When a source changes, mark dependent derived artifacts stale or review-required. Do not automatically overwrite their approved content or adjust user decisions.
7. Support queries by feature, actor, rule, error code and change request, returning the smallest relevant subgraph plus direct source links.

## Output

A serializable graph with nodes, typed edges, source revision and uncertainty; a query answer names the linked artifacts and explains why the relation is valid. An optional diagram is a view of that graph, not evidence that all files were inspected.

## Required negative checks

Broken references, renamed ID without mapping, copied requirements without original provenance, test links that do not verify the stated predicate, ambiguous current vs archived versions, and apparent coverage inflated by generic test-case links.

## Portable implementation

Use the existing BA artifact exchange validator, change-impact script and example graph where available. No mandatory vector DB, agent-run scheduler or new ANGENT Core memory layer is introduced.


## Ownership

ANGENT Root/Core retains reasoning, stakeholder intent, source authority and final Quality. This method is a task-specific support skill and does not create a second runtime, memory system or autonomous scheduler.

## Working directly from real SRS and QA files

When the source consists of Markdown project documents rather than an already serialized graph, use the implemented extractor at extensions/angent-ba/scripts/extract_markdown_graph.py. Pass the actual SRS and optionally its linked checklist and test-case files with the project root; the tool parses only explicit ID/link columns and records which CAP/AC/US references could not be resolved within the inspected inputs.

Follow with validate_artifacts.py, change_impact.py for a proposed BR/FR/AC change, and render_preview.py when a reviewer needs a safe HTML artifact index. Never mark a test as executed because the source file calls its status approved. A source document's own coverage summary is commentary to reconcile, not a substitute for a verified path through the inspected graph.

The MIT Atlas example deliberately produces 4/8 strictly linked FR-to-test coverage when only its SRS, checklist and cases are loaded; extending the corpus and resolving AC/US references is a separate authorized analysis step. Neither incomplete input nor ambiguous implicit links should be converted into fake nodes.

## Whole-lifecycle evidence instead of SRS-only statistics

When accepted URD, BRD and PRD documents exist, use the same source-backed graph extractor across all stages rather than treating CAP/BO/UN references as external guesses:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --urd extensions/angent-ba/examples/docs/atlas-re/atlas-re-urd.md --brd extensions/angent-ba/examples/docs/atlas-re/atlas-re-brd.md --prd extensions/angent-ba/examples/docs/atlas-re/atlas-re-prd.md --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output out/atlas-full-lifecycle.json

The real Atlas regression verifies 6 UN, 4 BO, 6 CAP and 8 FR. **8/8 FR have explicit FR→CAP→BO→UN ancestry, but only 4/8 FR link downstream to a TC artifact.** Four source-to-test gaps remain visible; structural reference existence does not prove execution or business approval. Do not change test counts or fabricate CHK/TC artifacts to satisfy a release threshold.

Some real projects have no complete URD/BRD/PRD sequence. In those cases, mark upstream coverage unknown/uninspected rather than insisting the user create redundant documents. ANGENT Root decides the appropriate evidence depth and which missing links genuinely matter.

## Full lifecycle evidence auditor (distributed and optional)

The portable command \`python extensions/angent-ba/scripts/audit_lifecycle_handoffs.py PROJECT_GRAPH.json\` inspects the **same graph** already produced by BA; there is no new truth store. It traces explicit UN→BO, BO→CAP, CAP→FR and verifiable requirement/rule/error/acceptance/checklist→TC relationships. Each finding includes the shortest witnessed path or an exact missing source ID. Entirely absent stages are labeled *not-inspected* rather than showing fictitious 0% compliance. Use it for \`ba-gap\`, \`ba-dashboard\` and change-impact scoping. Do not treat link presence as valid stakeholder intent or a passing test.
