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
| `ba-code-to-srs` | Observed implemented behavior at pinned commit | method | Runtime and stakeholder intent not inferred from code |

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
| `ba-prototype-next` | Next.js routed interactive prototype | unverified | No reproducible generated Next.js build verified |
| `ba-figma` | Screen controls as editable native Figma frames | provider-blocked | Real frame/node editing and read-back not verified |

## API

| Skill | Output | Evidence | Missing acceptance |
|---|---|---|---|
| `ba-api-assess` | Vendor or build choice with business tradeoffs | method | Live pricing/SLAs and providers need research |
| `ba-api-doc` | Versioned source-linked API contract summary | method | Requires real inspected provider specification |
| `ba-api-design` | Orchestration and webhook recovery plan | method | Live retries and idempotency not verified |
| `ba-api-map` | Provider domain UI field mappings | method | Field transformations need schema and test evidence |
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
| `ba-export` | Markdown HTML PDF or DOCX stakeholder package | unverified | No tested Pandoc/PDF/DOCX export path |
| `ba-preview` | Read-only HTML source evidence navigation | source-validated | Full multi-document visual fidelity not proven |
| `ba-reverse-preview` | Provenance-aware reverse spec HTML preview | unverified | Distinct runnable reverse preview not proven |
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
3. `ba-figma` previously implied the Reqwise OSS diagram API could deliver arbitrary editable screen frames; that is not the same capability. Screen delivery now requires actual Figma frame/node provider actions and read-back.
4. Synthetic D2, Bruno, Playwright and BPMN checks verify local implementations, NOT real customers, production backends or provider writes.
5. Live Jira/Confluence/Figma, Next.js generation, full export and reverse-preview need independent proof rather than a successful packaging check.

## Core evidence

`tests/test_ba_full_lifecycle.py` checks the full UN→BO→CAP→FR→test chain from Atlas URD/BRD/PRD/SRS/test Markdown.
`tests/integration/check_bpmn_official_xsd.py` uses actual OMG 2.0.2 XSD; `tests/integration/check_d2_cli.py` renders actual SVG.
`tests/integration/check_generated_playwright.py` uses Chrome with a deliberate failing mutation; `tests/integration/check_bruno_cli.py` checks four mock HTTP calls.
`tests/test_reqwise_adapter.py` checks Reqwise OSS semantics without claiming Figma canvas edits.

**Branch policy:** No merge into main. Individual open acceptance criteria must be resolved, constrained or explicitly disclosed before any release.
