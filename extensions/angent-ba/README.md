# ANGENT Business Analysis — maintained specialist extension

**Scope:** 55 ANGENT BA skills, 48 structured artifact templates, 19 ANGENT-specific review probes, 21 MIT reference rule documents and four Python helpers for graph/document checking, change impact and HTML preview. The source material is **45 maintained adaptations of MIT [Dev BA Kit](https://github.com/nv-minh/dev-ba-kit)** and **10 independently authored specialist methods**. Forty templates are adapted from the same MIT project; eight are original. This is not a reproduction of proprietary AI4BA BA-Kit source, which was not available.

## What actually works

- ANGENT Hub manifest resolves each specialist capability while Core retains intent, reasoning, authority and final Quality.
- Project evidence graph: extensions/angent-ba/scripts/validate_artifacts.py (refs, cycles, requirement-to-test reachability).
- Read-only change impact: extensions/angent-ba/scripts/change_impact.py (reverse dependencies and paths).
- Actual Markdown review: extensions/angent-ba/scripts/validate_documents.py (unfilled template markers, broken local links, IDs and metadata; heuristic, not a full semantic reviewer).
- Safe self-contained HTML evidence preview: extensions/angent-ba/scripts/render_preview.py, tested for escaping and non-HTTP URL rejection.

## How to operate

A typical path is ba-brainstorm to ba-srs to ba-userstory/ba-ac to ba-test-checklist/ba-test-cases. Each method must consume accepted project evidence and may execute only in a host with the relevant tools. Do not impose file paths from the upstream Claude plugin onto an existing project. The feature-specific templates are under skills/ba-kg/references/templates; their double-brace variables are expected in templates but must be filled in a completed artifact. The full MIT citation and license appear in THIRD_PARTY_NOTICES.md.

## Limits and improvement boundaries

The imported methods preserve meaningful rules, examples and procedures but **do not automatically port the original Claude hooks, TypeScript validators, custom BPMN/D2/render engines or install scripts**. Those require deliberate dependencies, host adapter verification and end-to-end tests. Native Jira/Confluence/Figma writes, Bruno/Playwright execution and design rendering must not be claimed solely from the existence of skill instructions. A current source tree can guide a specialist; it is not itself proof of product or runtime quality.

See ../../hub/research/ba-figma-parity.md for feature evidence, mapped source and remaining acceptance checks.
