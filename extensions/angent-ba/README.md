# ANGENT Business Analysis — maintained specialist extension

**Scope:** 55 ANGENT BA skills, 48 structured artifact templates, 19 ANGENT-specific review probes, 21 MIT reference rule documents and eight runnable Python helpers for extracting/validating Markdown evidence, building BPMN XML, change impact and HTML preview. The source material is **45 maintained adaptations of MIT [Dev BA Kit](https://github.com/nv-minh/dev-ba-kit)** and **10 independently authored specialist methods**. Forty templates are adapted from the same MIT project; eight are original. This is not a reproduction of proprietary AI4BA BA-Kit source, which was not available.

## What actually works

- ANGENT Hub manifest resolves each specialist capability while Core retains intent, reasoning, authority and final Quality.
- Project evidence graph: extensions/angent-ba/scripts/validate_artifacts.py (refs, cycles, requirement-to-test reachability).
- Source-driven extraction: extensions/angent-ba/scripts/extract_markdown_graph.py parses real SRS, checklist and test-case tables, retains explicit source links and reports unresolved external references; it never manufactures requirements.
- BPMN XML+DI compiler: extensions/angent-ba/scripts/build_bpmn.py supports one acyclic process with task/start/end and exclusive gateways, optionally multiple lanes; it rejects unimplemented semantics and audits node/connector collisions.
- Read-only change impact: extensions/angent-ba/scripts/change_impact.py (reverse dependencies and paths).
- Actual Markdown review: extensions/angent-ba/scripts/validate_documents.py (unfilled template markers, broken local links, IDs and metadata; heuristic, not a full semantic reviewer).
- Safe self-contained HTML evidence preview: extensions/angent-ba/scripts/render_preview.py, tested for escaping and non-HTTP URL rejection.
- HTML screen renderer: extensions/angent-ba/scripts/build_wireframe.py generates JS-free static wireframes or self-contained mock prototypes from an explicit screen model. Browser-level verification covers required/email validation, four simulated outcomes, navigation/focus, XSS and zero external requests.
- **D2 compiler:** extensions/angent-ba/scripts/build_d2.py now generates validated activity/swimlane, sql_table ERD and logical architecture diagrams. The official D2 0.9.0 CLI rendered 3/3 SVGs; XML geometry/labels and PNGs were inspected. The output models remain synthetic fixtures, not proof of a user's project design.
- Bruno generator: extensions/angent-ba/scripts/build_bruno.py generates HTTP collections with status and nested JSON tests, write-safe auth references, plus a requirement traceability manifest with optional read-only evidence-ID checking. The optional loopback-only Bruno CLI 4.2.1 fixture verified four requests, ten passing test assertions and one mock diagnostic ACK side effect.

## Verify D2 sources and rendered diagrams

At the repository root, use extensions/angent-ba/examples/d2-activity.json, d2-erd.json or d2-architecture.json. Run:

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-erd.json --output out/erd.d2 --svg out/erd.svg --d2 PATH_TO_D2

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

A renderer is required for the SVG; a generated .d2 file alone is not rendering evidence. Review the actual picture and source business relationships before using it. Local/Claude/Gemini CLI/OpenAI plugin packages include the Python scripts; **Gemini Web is reference-only** and does not bundle CLI scripts.


- Playwright test generator: extensions/angent-ba/scripts/build_playwright.py creates runnable Python Playwright test files and traceability from a reviewed screen model; 7/7 generated Chrome cases passed for the synthetic Authentication fixture. This is **local HTML only**, not production end-to-end.

## Generate and run browser tests

    python extensions/angent-ba/scripts/build_playwright.py extensions/angent-ba/examples/authentication-screen-model.json --output out/playwright-suite

    python out/playwright-suite/test_prototype.py --prototype out/auth-prototype.html --chrome PATH_TO_CHROME

    python tests/integration/check_generated_playwright.py --chrome PATH_TO_CHROME

## How to operate

A typical path is ba-brainstorm to ba-srs to ba-userstory/ba-ac to ba-test-checklist/ba-test-cases. Each method must consume accepted project evidence and may execute only in a host with the relevant tools. Do not impose file paths from the upstream Claude plugin onto an existing project. The feature-specific templates are under skills/ba-kg/references/templates; their double-brace variables are expected in templates but must be filled in a completed artifact. The full MIT citation and license appear in THIRD_PARTY_NOTICES.md.

## Limits and improvement boundaries

The imported methods preserve meaningful rules, examples and procedures but **do not automatically port the original Claude hooks, TypeScript validators, custom BPMN/D2/render engines or install scripts**. Those require deliberate dependencies, host adapter verification and end-to-end tests. Native Jira/Confluence/Figma writes and professional diagrams still require actual provider runtime evidence. Bruno CLI and Chrome/Playwright were tested on **synthetic localhost/UI fixtures only**; this does not establish parity with real authentication, cloud systems, production APIs or device integrations. A current source tree can guide a specialist; it is not itself proof of product or runtime quality.

See ../../hub/research/ba-figma-parity.md for feature evidence, mapped source and remaining acceptance checks.

## Real SRS-to-preview workflow

The Atlas worked example under extensions/angent-ba/examples/docs/atlas-re/ provides a pinned sample SRS, checklist and testcases from the MIT source. From the repository root, run:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output out/atlas-graph.json

    python extensions/angent-ba/scripts/validate_artifacts.py out/atlas-graph.json

    python extensions/angent-ba/scripts/render_preview.py out/atlas-graph.json --output out/atlas-preview.html

In the *inspected three-file scope*, the extractor finds 38 artifacts, 8 FR and only 4 FR with explicit chains to TC. The prose summary of the original checklist says 6/8, but that relies on additional AC/US context. The extractor reports these links unresolved rather than inflating verified coverage. A reviewed test-case document is not a test execution.


## Reproducible UI and API acceptance smoke

Review-only wireframe or interactive HTML mock from the same evidence-linked screen JSON:

    python extensions/angent-ba/scripts/build_wireframe.py extensions/angent-ba/examples/authentication-screen-model.json --mode wireframe --output out/auth-wireframe.html
    python extensions/angent-ba/scripts/build_wireframe.py extensions/angent-ba/examples/authentication-screen-model.json --mode prototype --output out/auth-prototype.html
    python tests/integration/check_wireframe_browser.py --chrome PATH_TO_CHROME

Generate Bruno HTTP tests against reviewed evidence and run the optional localhost fixture when Bruno CLI is installed:

    python extensions/angent-ba/scripts/build_bruno.py extensions/angent-ba/examples/synthetic-fleet-api-tests.json --evidence-graph extensions/angent-ba/examples/rental-fleet-traceability.json --output out/bruno
    python tests/integration/check_bruno_cli.py --cli PATH_TO_BRUNO_CLI

The schema-to-UI and spec-to-API mappings still need actual project stakeholder verification: the models in this repository are deliberately synthetic. The Bruno manifest lists linked ID validation separately from test execution.

## Evidence-connected diagram generation

Three D2 families now compile and render through the official D2 0.9.0 CLI, with actual PNG visual review of synthetic Activity, ERD and Architecture examples. To check SRS/traceability IDs while compiling, pass an **already validated evidence graph**:

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-activity.json --evidence-graph extensions/angent-ba/examples/rental-fleet-traceability.json --output out/verified-activity.d2

The report explicitly says source_link_check=ids-resolved-only. An accepted ID proves that a reference exists, not that a diagram embodies its semantics or that its implementation was tested. The Figma Reqwise payload adapter accepts the same optional evidence graph and applies this boundary separately.
