# ANGENT Business Analysis — maintained specialist extension

**Scope:** 55 ANGENT BA skills, 48 structured artifact templates, 19 ANGENT-specific review probes, 21 MIT reference rule documents and six runnable Python helpers for extracting/validating Markdown evidence, building BPMN XML, change impact and HTML preview. The source material is **45 maintained adaptations of MIT [Dev BA Kit](https://github.com/nv-minh/dev-ba-kit)** and **10 independently authored specialist methods**. Forty templates are adapted from the same MIT project; eight are original. This is not a reproduction of proprietary AI4BA BA-Kit source, which was not available.

## What actually works

- ANGENT Hub manifest resolves each specialist capability while Core retains intent, reasoning, authority and final Quality.
- Project evidence graph: extensions/angent-ba/scripts/validate_artifacts.py (refs, cycles, requirement-to-test reachability).
- Source-driven extraction: extensions/angent-ba/scripts/extract_markdown_graph.py parses real SRS, checklist and test-case tables, retains explicit source links and reports unresolved external references; it never manufactures requirements.
- BPMN XML+DI compiler: extensions/angent-ba/scripts/build_bpmn.py supports one acyclic process with task/start/end and exclusive gateways, optionally multiple lanes; it rejects unimplemented semantics and audits node/connector collisions.
- Read-only change impact: extensions/angent-ba/scripts/change_impact.py (reverse dependencies and paths).
- Actual Markdown review: extensions/angent-ba/scripts/validate_documents.py (unfilled template markers, broken local links, IDs and metadata; heuristic, not a full semantic reviewer).
- Safe self-contained HTML evidence preview: extensions/angent-ba/scripts/render_preview.py, tested for escaping and non-HTTP URL rejection.

## How to operate

A typical path is ba-brainstorm to ba-srs to ba-userstory/ba-ac to ba-test-checklist/ba-test-cases. Each method must consume accepted project evidence and may execute only in a host with the relevant tools. Do not impose file paths from the upstream Claude plugin onto an existing project. The feature-specific templates are under skills/ba-kg/references/templates; their double-brace variables are expected in templates but must be filled in a completed artifact. The full MIT citation and license appear in THIRD_PARTY_NOTICES.md.

## Limits and improvement boundaries

The imported methods preserve meaningful rules, examples and procedures but **do not automatically port the original Claude hooks, TypeScript validators, custom BPMN/D2/render engines or install scripts**. Those require deliberate dependencies, host adapter verification and end-to-end tests. Native Jira/Confluence/Figma writes, Bruno/Playwright execution and design rendering must not be claimed solely from the existence of skill instructions. A current source tree can guide a specialist; it is not itself proof of product or runtime quality.

See ../../hub/research/ba-figma-parity.md for feature evidence, mapped source and remaining acceptance checks.

## Real SRS-to-preview workflow

The Atlas worked example under extensions/angent-ba/examples/docs/atlas-re/ provides a pinned sample SRS, checklist and testcases from the MIT source. From the repository root, run:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output out/atlas-graph.json

    python extensions/angent-ba/scripts/validate_artifacts.py out/atlas-graph.json

    python extensions/angent-ba/scripts/render_preview.py out/atlas-graph.json --output out/atlas-preview.html

In the *inspected three-file scope*, the extractor finds 38 artifacts, 8 FR and only 4 FR with explicit chains to TC. The prose summary of the original checklist says 6/8, but that relies on additional AC/US context. The extractor reports these links unresolved rather than inflating verified coverage. A reviewed test-case document is not a test execution.

