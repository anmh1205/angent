# BA-Kit and Figma Kit: audit of all 67 specialist capabilities

This inventory compares the current extension source with public AI4BA BA-Kit, the MIT Dev BA Kit and Reqwise Figma OSS. It is an evidence inventory, NOT an assertion of commercial source parity, deployed product functionality or a completed Figma canvas write.

**Evidence:** method = source-grounded specialist approach; source-validated = structural local verification only; runtime-mock = real CLI/browser against synthetic fixture; payload-verified = checked Reqwise candidate only; provider-blocked = live provider outcome missing; unverified = expected output not demonstrated.

## Product

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-prd` | Product vision and sourced feature map | method | Unverified buyer data and stakeholder acceptance |
| `ba-roadmap` | Prioritization, justified scores and release dependencies | method | No verified forecasts or approved resource commitments |
| `ba-discover` | Opportunity competitor buyer discovery or existing repo context | method | Needs fresh actual buyer and competitor research |

## Requirements

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-brainstorm` | Elicited decisions and unresolved business questions | method | Only real stakeholders can approve outcomes |
| `ba-urd` | UN needs, user context and observed jobs | method | Persona/interview evidence must be sourced |
| `ba-brd` | BO business value, scope, risks and ROI | method | Financial assumptions and approval unverified |
| `ba-prd-epic` | CAP feature capability and priority | method | Business authorization and cost basis unverified |
| `ba-srs` | FR/NFR/BR/error matrix with stable IDs | source-validated | Parser and syntax do not prove requirements accurate |
| `ba-reverse-doc` | Legacy source-linked inferred requirements | method | Requires original source and conflict reconciliation |
| `ba-code-to-srs` | Code source snippets at a pinned Git commit with verified requirement IDs | source-validated | Pinned blob/excerpt verified; actual behavior, deployment and stakeholder intent unverified |

## Diagrams

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-sequence` | Message ordering with error and retry fragments | method | Renderer and real protocol semantics not verified |
| `ba-activity` | Decision process and alternate paths | method | No generic source-to-renderer parity evidence |
| `ba-activity-swimlane` | Role-owned workflow and guarded paths | runtime-mock | D2 sample proven; PlantUML runtime still optional |
| `ba-bpmn` | BPMN XML with lane and gateway semantics | runtime-mock | OMG XSD passes; BPMN engine import untested |
| `ba-state` | Entity state transitions and guards | method | No live state machine conformance evidence |
| `ba-erd` | Conceptual relations and optionality | method | No actual database schema or Mermaid render proof |
| `ba-d2-erd` | Typed D2 sql_table model and SVG | runtime-mock | Real D2 CLI passes on synthetic schema only |
| `ba-d2-activity` | D2 guarded decision flow and SVG | runtime-mock | Synthetic workflows not production rules |
| `ba-d2-architect` | D2 device/services flow and SVG | runtime-mock | No deployment or network traffic verification |
| `ba-dbdiagram` | DBML source and relation definitions | source-validated | Real SQL migration and dbdiagram import not proven |
| `ba-usecase-diagram` | UML actors and goal boundaries | method | Real PlantUML render and Figma Pro tools absent |

## Backlog

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-usecase` | Full actor goal with alternates and failures | method | Stakeholder acceptance is not automatable here |
| `ba-userstory` | Sourced slices, outcomes and AC identifiers | method | No live acceptance/backlog synchronization |
| `ba-ac` | Given When Then conditions and negative cases | method | Needs actual actor and edge-case validation |

## Screen

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-user-flow` | Screen navigation and branches | source-validated | Only mock screen runtime tested |
| `ba-wireframe-ascii` | ASCII layout keyed to user flow | method | Not a functional or editable screen |
| `ba-wireframe-html` | Standalone offline low-fidelity HTML | runtime-mock | Synthetic Chrome fixture only |
| `ba-prototype-html` | Clickable mock HTML with errors and focus | runtime-mock | No real user backend or persistence |
| `ba-prototype-next` | Next.js routed interactive prototype | runtime-mock | Real Next 16.4.2 production build and Chrome 3× at 2 viewports; production/backend unverified |
| `ba-figma` | Screen controls as editable native Figma frames | provider-blocked | Real frame/node editing and read-back not verified |

## API

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-api-assess` | Vendor or build choice with business tradeoffs | method | Live pricing/SLAs and providers need research |
| `ba-api-doc` | Versioned source-linked API contract summary | method | Requires real inspected provider specification |
| `ba-api-design` | Orchestration and webhook recovery plan | method | Live retries and idempotency not verified |
| `ba-api-map` | Provider domain UI field mappings | source-validated | OpenAPI-based sample transformation tested; actual frontend bindings/live provider still unverified |
| `ba-api-checklist` | Integration behavior coverage inventory | method | No real integration target configured |
| `ba-api-test` | Bruno cases and status/body checks | runtime-mock | 4/4 mock CLI calls, not provider E2E |
| `ba-api-readiness` | Go-live, rollback and deployment risks | method | Staging SLO and provider launch not tested |

## Testing

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-test-checklist` | CHK coverage of FR/BR/errors | source-validated | Coverage links are not executed tests |
| `ba-test-cases` | TC data, steps and expected results | source-validated | Execution requires target/runtime evidence |
| `ba-playwright-gen` | Generated browser test cases from source model | runtime-mock | Chrome mock 7/7, real app not tested |

## Quality

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-gap` | Requirement chain gap and coverage summary | source-validated | Full links do not establish true business correctness |
| `ba-doc-drift` | Observed spec versus code disagreements | method | No generic live repo execution provided |
| `ba-ask` | Evidence-grounded business answer | method | Requires current project documents and sources |
| `ba-cr` | Source revision impacts and dependent re-review | source-validated | Graph diff is not authorized document application |
| `ba-dashboard` | Coverage and risk evidence rollup | source-validated | Live delivery/provider status not checked |
| `ba-kg` | Graph of artifacts and explicit references | source-validated | Cannot invent missing semantic source links |

## Handoff

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-jira` | Accepted US to real Jira issues with read-back | provider-blocked | No actual provider write/read verification |
| `ba-confluence` | Version-safe scope-limited page update | provider-blocked | No real macro-preserving page update test |
| `ba-export` | Markdown HTML PDF or DOCX stakeholder package | runtime-mock | Pandoc MD/HTML/DOCX plus real Chromium PDF tested; production accessibility and typography still require review |
| `ba-preview` | Read-only HTML source evidence navigation | source-validated | Full multi-document visual fidelity not proven |
| `ba-reverse-preview` | Provenance-aware reverse spec HTML preview | runtime-mock | Three synthetic confidence classes rendered in Chrome; source provenance must be independently checked |
| `ba-userguide` | Role-based operating guide with actual failures | method | Actual app screens and behavior not verified |
| `ba-meet` | Meeting actions decisions and provenance | method | Raw transcript and stakeholder decisions unverified |
| `ba-update-overview` | Scoped overview update based on source changes | source-validated | Real document/provider mutation requires read-back |
| `ba-delegate` | Bounded independent second-opinion review | provider-blocked | No autonomous worker runtime can be presumed |

## Figma OSS

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `figma-activity` | Activity diagram model and native candidate request | payload-verified | No Figma canvas write or read-back |
| `figma-userflow` | Userflow graph and native candidate request | payload-verified | No real Figma editing/read-back |
| `figma-sequence` | Sequence model and native candidate request | payload-verified | No live Figma sequence render |
| `figma-state` | State machine model and native candidate request | payload-verified | No Figma canvas lifecycle audit |
| `figma-erd` | ERD entities keys and candidate request | payload-verified | No canvas node/key read-back |
| `figma-sitemap` | Site IA model and candidate request | payload-verified | No real Figma frame hierarchy read-back |

## Figma Pro

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `figma-usecase` | Native UML usecase nodes and relationships | provider-blocked | Reqwise OSS does not implement Pro type |
| `figma-bpmn` | Editable BPMN representation and event shapes | provider-blocked | No Figma Pro renderer; XML XSD separate |
| `figma-journey` | Editable journey map and research evidence | provider-blocked | No OSS supported native journey type |
| `figma-persona` | Editable research-grounded persona cards | provider-blocked | No real study source or native write |
| `figma-design-system` | Variables styles and reusable components | provider-blocked | No tested live library changes and read-back |
| `figma-demo` | Prototype reaction walkthrough and recording | provider-blocked | No verified Pro recording or interaction write |

## Critical cross-kit findings

1. BA graph historically omitted the early UN/BO/CAP levels; this was repaired to read URD, BRD and PRD, with actual Atlas cross-document regression.
2. `ba-discover` had inherited the Dev BA Kit's repository investigation, not AI4BA's business opportunity and competitor discovery. Both modes now have distinct methods.
3. `ba-figma` previously implied the Reqwise OSS diagram API could deliver arbitrary editable screen frames; that is not the same capability. Screen delivery now requires actual Figma frame/node provider actions and read-back. A separate official Plugin API candidate now exists, tested with a Node mock for idempotency/conflict/rollback; this is not live canvas proof.
4. Synthetic D2, Bruno, Playwright and BPMN checks verify local implementations, NOT real customers, production backends or provider writes.
5. Local Next.js App Router generation and Chrome execution, scoped stakeholder MD/HTML/DOCX export and a reverse-preview browser demonstration now have independent test evidence. PDF and all live Atlassian/Figma mutation/read-back paths still need separate proof; never mix these evidence tiers.

## Core evidence

`tests/test_ba_full_lifecycle.py` checks the full UN→BO→CAP→FR→test chain from Atlas URD/BRD/PRD/SRS/test Markdown.
`tests/integration/check_bpmn_official_xsd.py` uses actual OMG 2.0.2 XSD; `tests/integration/check_d2_cli.py` renders actual SVG.
`tests/integration/check_generated_playwright.py` uses Chrome with a deliberate failing mutation; `tests/integration/check_bruno_cli.py` checks four mock HTTP calls.
`tests/test_reqwise_adapter.py` checks Reqwise OSS semantics without claiming Figma canvas edits.

`tests/test_ba_figma_screens.py` checks a real common screen model across HTML, Next and Reqwise editable frame candidates, including accepted source IDs in the synthetic fleet example. The script only prepares `figma_write` node trees: it has not created or verified live Figma canvas elements. `tests/integration/check_kits_acceptance.py` checks 58 real Atlas artifact rows across URD/BRD/PRD/SRS/TC and 4/8 FR structural test links, plus separate local UI/API/Figma candidates. Example coverage is not stakeholder approval or production verification.

The BA Markdown extractor excludes fenced code examples to avoid promoting tutorial requirements into actual source graph nodes; its negative test is in `tests/test_ba_markdown_traceability.py`.

**Branch policy:** No merge into main. Individual open acceptance criteria must be resolved, constrained or explicitly disclosed before any release.

### New cross-kit contracts

- `ba-api-map` now has a runnable OpenAPI → UI mapping checker for exact copy and enum fields, with explicit source graph validation and negative cases. Output is a source-aligned sample mapping, not a live frontend. See `tests/test_ba_api_field_mapping.py`.
- `ba-figma` now supports two separately generated code candidates: Reqwise `figma_write` and the official Figma Plugin API. The latter is exercised with an API-shaped Node mock for creation, idempotency, conflict and rollback, but has no verified live canvas edit. See `tests/test_ba_figma_native.py`.

### New pinned code evidence

`extensions/angent-ba/scripts/verify_code_witness.py` now reads actual Git blobs using a full pinned SHA, checks allowed source paths, exact line ranges, required snippets, optional SHA-256 and BA requirement identity. Negative tests reject fabricated witnesses, old line locations, invalid revisions and traversal. No execution or semantic compliance is inferred. See `tests/test_ba_code_witness.py`.

## Whole-lifecycle audit update

A single read-only, **distributed** graph auditor now checks stage evidence for UN→BO, BO→CAP, CAP→FR, FR/NFR/BR/error/AC/checklist→TC. It emits actual witness paths and IDs for known handoff gaps, while deliberately marking absent corpus stages as **not-inspected** rather than incorrectly declaring 0% coverage or success. This is a shared verification instrument for \`ba-kg\`, \`ba-gap\` and \`ba-dashboard\` without adding state, agents or an alternative Hub. Tests: \`tests/test_ba_lifecycle_handoffs.py\` and packaged verification in \`tests/integration/check_distributed_kits.py\`.

The Atlas corpus contains more test-case records than FRs traceable to a TC; the report keeps test artifact count and FR coverage distinct. None of this establishes business validation or any runtime test success. Additional live user, provider and Figma evidence remains required before claiming full kit parity.

## Independently inspectable evidence source registry

The machine-readable sibling \`ba-figma-audit-67.json\` now associates each **promoted** source-validated/runtime-mock/payload-verified capability with the existing, exact test source(s) that exercise it. All 67 rows have an explicit \`proof_scope\`; method-only, unverified and provider-blocked items have **no fabricated proof refs**. The regression check \`tests/test_all_kit_evidence_inventory.py\` fails if a referenced test disappears or a promoted row lacks proof.

A proof file existing is not evidence that the test was recently run. Runtime and live-provider results must additionally be obtained from an actual checked commit and execution log. Candidate Figma payload checks cannot be promoted to live canvas status.

**Export validation update:** The Chromium+Playwright PDF path produced a real 7-page PDF from three synthetic source documents. PyPDF extracted selectable Unicode text; unlike the optional TeX engine path, this does not require TeX. Source-only test: `tests/integration/check_ba_chromium_pdf.py`. This is not a production editorial signoff.
