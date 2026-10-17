# BA-Kit / Reqwise research and implementation status

Research references: [AI4BA BA-Kit](https://ai4ba.com/ba-kit), [Reqwise Pro](https://ai4ba.com/figma-mcp), [SRS preview](https://ai4ba.com/skills-pack-examples/srs-preview.html), [test cases viewer](https://ai4ba.com/skills-pack-examples/test-cases/preview.html), [CineMo public demo](https://ai4ba.com/demo-reqwise-mcp-oss), MIT source repositories [Dev BA Kit](https://github.com/nv-minh/dev-ba-kit), [Reqwise Figma MCP](https://github.com/hoangpm96/reqwise-figma-mcp). The public site lists 55 BA skills, 48 templates, 19 rules and Reqwise 12 Pro methods. No license to view or reproduce the paid ZIP/Pro source is assumed.

## Verified source work and original work

| Capability | Source/provenance | Implementation level | Required external proof |
|---|---|---|---|
| 45 BA specialist methodologies | 45 adapted Dev BA Kit MIT SKILL.md methods | Detailed method texts / no native Claude hooks | Representative generated documents and specialist evaluation |
| 10 other BA specialist methods | Independent ANGENT procedures, informed by public requirements and domain standards | Detailed plans and several runnable helpers | Feature outputs and host interactions for each skill |
| 48 templates | 40 MIT structures + 8 independent additions | Template files, not filled project evidence | Reviewer acceptance on generated artifacts |
| Source business rules | 21 attributed MIT reference rules + 19 ANGENT BA review probes | Reference methodology / not second authority layer | Test realistic change and consistency disputes |
| Traceability and CR impact | Original Markdown extractor, graph validator and reverse dependency traversal | Runs on actual MIT Atlas SRS/checklist/test corpus; 38 artifacts and 4/8 strictly traceable FR-to-TC | Add broader source formats and resolve external AC/US/CAP documents before expanded coverage claims |
| Artifact revision and change impact | Original ANGENT two-version graph comparator with transitive dependency traversal | Tested changed BR → FR → AC → TC, added/removed IDs and source-version review triggers; read-only | Does not establish source-code drift or stakeholder approval |
| Markdown validation | Original Python document scanner | Runs locally; structural checks | Real SRS/BRD/PRD examples and false-positive review |
| Feature HTML preview | Original standard-library safe renderer | Runs locally on scoped graph | Visual/browser accessibility and richer semantic sections |
| Static wireframe / interactive mock prototype | Independently authored HTML generator and synthetic Authentication screen model | JS-free static page and a mobile-tested Chrome prototype with required/email validation, mock locked/invalid/offline/success states and focus handling; no external requests | Project-specific source-to-screen semantic mapping, desktop/responsive audit and advanced states |
| Generated Playwright coverage from reviewed HTML prototypes | Original ANGENT Python Playwright suite builder and traceability manifest | 7/7 synthetic Authentication browser cases passed on real Chrome; local file only, no network requests | Production E2E selectors, authenticated test accounts, external app tests and cross-browser evidence remain unverified |
| Bruno/OpenAPI contract alignment | Original ANGENT conservative OpenAPI 3.1 JSON auditor; local $ref resolver | Tests match actual mock paths, status, JSON field types/const/enum, required body and bearer declarations; remote/cyclic/composed refs fail closed | Not complete JSON Schema/OpenAPI validation; sandbox runtime and provider-specific contracts remain unverified |
| Bruno API generation and local execution | Independently authored .bru generator, explicit test models and a local HTTP fixture | Bruno CLI 4.2.1 ran 4/4 requests and 10/10 tests including a POST JSON body and mock side effect; generated traceability manifest can validate existing BA evidence IDs | Independent real sandbox contracts, idempotency, auth provisioning, schema/side-effect checks and production parity |
| Three D2 business diagram families | Original ANGENT JSON-to-D2 generator and real D2 0.9.0 CLI integration | Activity with ownership/guarded branches, sql_table ERD with PK/FK/unique rows, and logical architecture all render valid SVG; node labels and visible PNG output inspected | Project-specific semantic traceability, complex layouts, visual accessibility and larger graphs remain unverified |
| Six Figma OSS diagram kinds | Six MIT specialist methods + request compiler | Six examples passed Reqwise OSS 0.3.0 actual Zod validators at commit 4ee65b7; dry-run only | Live MCP plugin canvas edit/read-back and visual inspection |
| Six additional Figma kinds | Original skills informed by OMG BPMN, Figma APIs and WCAG | Specialized methodology, not a full implementation | Native editability, render proof, interoperability and video where relevant |
| Cross-host packages | ANGENT 2.0 Hub dynamic registry | Structural package build and local tests | Install smoke test in each real host and check root routing |

## Discriminating benchmark

Use at least four separate input families, not only the public Authentication demo:

1. Authentication: conflicting lockout policy, account-enumeration defense, session expiry, OAuth and network-failure paths; verify FR/BR/E alignment with screen and test cases.
2. Payment/booking: bounded holds, idempotent retries, timeout, compensation, cross-service sequence, BPMN and ERD consistency.
3. IoT fleet telemetry: multi-tenant vehicle authorization, delayed/disconnected telemetry, ECU fault events and incident history; separate device/cloud/user concerns.
4. Legacy code reconstruction: feature flag conflict, outdated SRS, mock tests vs deployed behavior, source symbol proof and uncertain business owner decision.

Every benchmark should produce an accepted source ledger, an artifact diff, executable validator outcomes, missing evidence, review notes and semantic acceptance measurements. Structural unit tests and package counts alone are NOT product parity or business correctness evidence.

## Priority remaining work

- Replace Claude-specific choreography in migrated methods with tested, host-native instructions where it remains operationally relevant; keep original author's attribution.
- Extend the independently implemented **bounded** BPMN XML/DI compiler (now parsed without warnings by bpmn-moddle@9 and checked for geometry collisions) to supported advanced constructs via a real engine, and expand D2 beyond the three now-rendered bounded diagram families; verify Mermaid/PlantUML rendering and harder visual layouts.
- Extend **already verified** Bruno and HTML fixtures to more consequential business domains, richer API schema/side-effect checks, requirement-driven screen generation, and genuine end-to-end Playwright against a running product. The current mock prototype and Bruno fixture are not a real Next.js application or a production API.
- Create/read/update Figma artifacts in an authorized live environment; validate responsive/accessibility and source-to-canvas consistency.
- Verify Jira/Confluence bidirectional synchronization with conflict handling, idempotency and audit read-back.
- Test full task behavior and cross-host ANGENT activation before any release/merge.

## Standards and implementation references

IREB CPRE Requirements Engineering handbooks: https://cpre.ireb.org/en/downloads-and-resources/downloads

BPMN 2.0.2 normative specification and schemas: https://www.omg.org/spec/BPMN/2.0.2/

Figma variables and component properties: https://developers.figma.com/docs/plugins/working-with-variables/ and https://developers.figma.com/docs/plugins/working-with-component-properties/

W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/

Bruno CLI: https://github.com/usebruno/bruno/blob/main/packages/bruno-cli/readme.md

## Verified cross-kit evidence reference handling

D2 generation and Reqwise OSS payload compilation now optionally resolve source_refs using the **same validated BA artifact graph**. A shared FR identity can be retained without a duplicated memory service or new Hub runtime. Missing/duplicate references fail before output. The checked result is only ID existence; meaningful semantic alignment, reviewed changes, actual Figma canvas mutation and production behavior still require their independent sources and verification. Executable tests: tests/test_ba_d2.py, tests/test_reqwise_adapter.py, tests/test_ba_figma_trace_chain.py.

## Standards and upstream fidelity audit — 2026-10-16

The ANGENT specialist sources are **adaptations**, not a copy of a closed AI4BA package. Public comparators inspected: MIT Dev BA Kit (https://github.com/nv-minh/dev-ba-kit) and MIT Reqwise Figma MCP (https://github.com/hoangpm96/reqwise-figma-mcp). This comparison does not claim parity with paid Reqwise Pro. The OSS Figma MCP exposes activity, userflow, state, sequence, ERD and sitemap; BPMN, usecase, journey, persona, design-system generation and demo recording require separately verified Pro/native capabilities.

1. **OpenAPI 3.1.2** — https://spec.openapis.org/oas/v3.1 : security requirements are OR across alternatives and AND inside an alternative; anonymous operation overrides and empty security are supported. Response precedence is explicit status > class pattern (2XX, 4XX, etc.) > default. ANGENT's bounded auditor now checks these rules and local references; unsupported authentication forms and schema compositions cannot earn a green contract-check result.
2. **JSON Schema draft 2020-12** — https://json-schema.org/draft/2020-12/json-schema-validation : scalar types include union types, numeric/string bounds and exact enum/const semantics. ANGENT validates the supported subset, rejects unimplemented composition, dynamic/remote refs and other unsupported constraints, including meaningful constraints alongside a local $ref, rather than silently ignoring them. It is **not a complete JSON Schema implementation**.
3. **Playwright Python** — https://playwright.dev/python/docs/test-assertions : use web-first retrying assertions instead of instant DOM snapshots. The generated Python suite uses locator assertions and has passed on real Chrome. A deliberately changed error message made TC-PROT-0002 fail, showing a negative mutation detected by the same generated suite. Production application E2E and real authentication are still out of scope.
4. **OMG BPMN 2.0.2** — https://www.omg.org/spec/BPMN/2.0.2/ : official BPMN20/Semantic/BPMNDI/DC/DI XSD files validate the limited, non-executable Atlas BPMN XML+DI generated by ANGENT. Test tests/integration/check_bpmn_official_xsd.py uses local normative files and verifies that removing required sourceRef makes XSD validation fail. No Camunda/modeler import or executable semantics are claimed.
5. **Figma plugin API** — https://developers.figma.com/docs/plugins/working-with-text/ : editable text-node changes require actual plugin context and font loading. The ANGENT OSS adapter generates candidate figma_diagram arguments only, without a Figma read-back/write. Reqwise's actual native server/plugin session must be available before any editable result is claimed.

These are independent, evidence-scoped checks for **Atlas BA requirements, a synthetic fleet API and a synthetic Authentication prototype**. They are not a single deployed product; passing them does not establish end-to-end production fidelity or paid AI4BA/Reqwise Pro parity.

## Screen-to-Figma handoff built separately from diagram support

The source-driven low-fidelity BA screen model can now be compiled to a candidate Reqwise figma_write scene-tree program by extensions/angent-ba/scripts/build_figma_screens.py. Tests compare every generated control label/name with the source and check JavaScript syntax in Node. This is a genuine editable-FRAME candidate, not another figma_diagram type. Native Figma creation, idempotent frame reconciliation, prototype interactions, token/component reuse and canvas/screenshot read-back remain unverified. No commercial Reqwise Pro capability is implied.

## Source-by-source regression deepening (2026-10-17)

This audit keeps **portable model validity**, **actual provider schema acceptance**,
**real generated-app execution**, **domain correctness** and **Figma canvas
mutations** as distinct claims.

### Confirmed defects corrected

- **Reqwise userflow control semantics:** a `return` edge was previously
  converted into an ordinary edge. Explicit cancel/back/retry routing is now
  preserved, and unsupported kinds cannot be silently converted into a
  provider-accepted type.
- **State and relational semantics:** `choice` branches now check guard
  ambiguity; ERD validates the OSS cardinality enumeration and preserves the
  identifying-relationship flag. A state machine with no final state is
  permitted only when `metadata.continuous=true` is explicit, reachable
  states have exits and the nontermination policy remains a surfaced review
  warning.
- **Provider-supported annotations:** previously dropped state entry/do/exit,
  transition actions, message notes, diagram visual classes, userflow screen
  links and sitemap screenId lists now survive the conversion to the pinned
  MIT schema. Optional fields and conflicting guard/label combinations have
  invalid-shape tests.
- **Source document fidelity:** invalid requirement IDs are no longer ignored
  when extracting Markdown tables; example code fences no longer count as
  real requirements/links. Index-managed UC/story bodies must actually be
  referenced from an adjacent valid index. Calendar dates are parsed.
- **Prototype action identity:** the Next.js generator previously routed
  every submit control through the first form submit. The generated app now
  locates the actual clicked submitter and selects that control's declared
  scenario-specific outcome.

### Fresh independent acceptance signals

- GitHub Actions
  [run 39016056646](https://github.com/anmh1205/angent/actions/runs/39016056646)
  passed source regression and an actual build of the generated isolated
  Next.js application.
- The same run fetched **Reqwise MIT 0.3.0 at exact commit
  `4ee65b7a037578690cfcd4006257c4f25e458eea`** and passed all **six
  original Zod schema validators** for dry-run activity, state, sequence,
  ERD, userflow and sitemap payloads. This is a native upstream *request
  contract* check; no provider/plugin session or canvas is claimed.
- A browser-level Next.js integration job is separately checked through
  `tests/integration/check_next_prototype_browser.py`, and must be judged
  only by a successful CI execution including live-route/viewport evidence;
  source-level assertions and a Next build do not independently establish it.

### Remaining independent acceptance boundaries

1. No real Reqwise MCP session plus authorized Figma file/page has yet
   established node creation, linkScreens reactions, layout legibility,
   rollback behavior or native read-back.
2. Synthetic Atlas/Fleet/Authentication fixtures cannot prove the 67 methods
   produce semantically correct, accepted documents on a customer's genuine
   scope, or that optional providers and paid Pro-only features exist.
3. Source-linked test artifacts cannot prove tests were run; code witness
   hashes and validated graph edges cannot approve implementation behavior.
4. Continue per-specialist acceptance with independently reviewed outputs
   and negative examples, not counts of `SKILL.md`, placeholders or
   structural validation alone.


### Browser and bounded-renderer follow-through

- [Run 39016100037](https://github.com/anmh1205/angent/actions/runs/39016100037)
  verified the **actual started production Next.js server** using Chromium
  at **390×844** and **1366×850**. It checked authentication-mock validation,
  invalid/locked/offline/success variants, home/recovery/reset routes, focus,
  hydration, no horizontal overflow, zero page errors and **zero external
  HTTP requests**. It does not test production authorization.
- The BA D2 ERD validator rejects nonboolean `external` flags. Previously,
  a truthy string such as `"false"` could exempt an entity from the
  primary-key rule. This is also regression-tested against a valid
  explicitly external entity.
- The bounded BPMN XML compiler now rejects nonstring or blank
  `sequenceFlow.name` rather than accepting a converted object as a
  gateway guard and failing during XML serialization.

These changes narrow concrete false-valid model cases without claiming
complete BPMN process semantics, actual downstream SQL constraints or
customer-reviewed Figma diagrams.


## Second detailed file-by-file audit — 17 October 2026

This pass re-read all 67 specialist `SKILL.md` files, 48 BA templates,
19 independent BA review rules and 42 BA/Figma example files. It also
revisited the 20 BA Python scripts, two Figma Python scripts, Hub manifests
and routing, source-level tests, upstream Reqwise request schemas, and
existing integration evidence. **Reading and static checks are not claims
that 67 skills have passed real model-behavior acceptance.**

### Corrected root causes and negative controls

| Layer | False-valid or broken behavior found | Change and check |
|---|---|---|
| Artifact lineage | An `FR-*` ID could be labeled `TEST` and disappear from counted FR coverage; source identities accepted embedded whitespace | Require recognized ID prefix and canonical artifact kind to agree, preserving explicit custom `NOTE-*` kinds; validate source identifiers; mutation tests in `test_ba_typed_lineage.py` |
| OpenAPI fixture checker | A Python nonfinite float could pass a numeric JSON Schema type; malformed path items, components, request-body content or enum containers could crash the checker or treat a string enum as characters | Validate finite numeric values and structural schema contracts with informative errors; mutation tests in `test_ba_api_contract.py` |
| Local evidence | A legitimate `spec.md#section` URI was checked as a literal filesystem basename, falsely reporting the source missing | Remove fragments only from file-existence checks; retain root-containment and missing-path rejection in `test_ba_local_source_evidence.py` |
| Mermaid specialist workflow | ERD, State and Sequence skills asserted that Mermaid cannot render in chat; some also forced a fixed file destination and unnecessary post-write review | Select native host preview where available, preserve source-first verification, choose an authorized output destination and do not claim a nonexistent render; regression in `test_ba_portability.py` |
| DBML sample | The source example used `cards.id` without declaring `cards`; file-review flow assumed original-host approval rituals | Add the missing table and check that all example FK targets are declared; compiler availability is still a separate requirement and no SQL migration is asserted |
| Reverse specification | `SOURCE-OBSERVED` claim could list no source; duplicate refs and malformed approval ID were accepted; a prior HTML assertion was unreachable code | Require distinct real source IDs, bounded approval decision IDs, and explicitly state that source citation does not independently verify stakeholder authority; tests in `test_ba_reverse_preview.py` |
| Static screen reviewer | Existing unit test contained a conditional expression that prevented an assertion from running | Assert actual HTML email-input semantics, disabled static controls and no executable `script` in the wireframe; regression in `test_ba_wireframe.py` |
| Integration coverage | The complete multi-kit acceptance script existed but was not called by the continuous PR validation pipeline | Add `tests/integration/check_kits_acceptance.py` to the BA/Figma job; leave provider-native and semantic evaluation separate |

### What the green pipeline now actually proves

- Source-level BA/Figma, core distribution and interface tests run under
  GitHub Actions. Native Reqwise MIT 0.3.0 schema checks fetch pinned
  `4ee65b7a037578690cfcd4006257c4f25e458eea`, validating six
  dry-run requests without creating a Figma object.
- The Next.js sample is installed and production-built, then an actual
  Chromium process verifies it at mobile and desktop viewports, with
  invalid, locked, offline and success behaviors and no external HTTP
  requests. This is a synthetic Authentication demo, not fleet production
  or customer account security.
- Source-to-prototype integration now verifies the Atlas evidence graph,
  Fleet API fixtures, read-only code witness, D2 source, Bruno requests,
  Figma candidate models, and browser/Next source generation in one
  execution. All integrations are limited to supplied synthetic/open
  sample corpora.
- 67 skills are covered by **13 planned expert/agent behavior scenarios**.
  As checked this pass, all 13 have `execution_status: not-run`.
  A successful unit test does not permit promotion of those scenarios
  to passed, or reclassification of provider-blocked skills.

### Further findings and priorities

1. **P0 — Provider-native read-back.** No authorized real Figma canvas
   session has demonstrated screen frames, text/fonts, component variants,
   prototype actions, live Reqwise diagram layout or rollback. A mock
   idempotency test and six upstream schema accepts do not replace that.
   The commercial Reqwise Pro-only six methods have no proven Pro runtime.
2. **P0 — Specialist semantic trials.** Each of the 13 scenario groups
   needs actual agent output, independent review of required and forbidden
   behaviors, verified source identities and an honest revision trail.
   Target unclear user requirements, contradictory business rules,
   denial/retry state flows, partial API contracts and missing evidence.
3. **P1 — Real Jira/Confluence acceptance.** Test bounded user-authorized
   read/write/read-back in a suitable test space, preserving existing
   macros/content and detecting provider version conflicts. Method
   instructions alone cannot establish provider behavior.
4. **P1 — Host portability.** Test the packaged ANGENT root + specialist
   routing in representative hosts, rather than inferring invocation
   from a manifest or requiring uninstalled Claude-only tools.
5. **P2 — Visual/editorial quality.** Review real Mermaid/D2/DBML output,
   image collection choices and the finished BA documents as a reader;
   source links and valid schemas establish neither communication quality
   nor business correctness.

**Branch discipline:** Changes remain in `feat/ba-figma-kits` with Draft
PR #65. Nothing in this report is a release approval or merge instruction.


## Third-pass findings and bounded live Figma probe — 2026-10-17

### Verified runtime and implementation changes

- Bruno `expected_json` validation now rejects nonfinite Python numbers
  (`NaN`, `Infinity`) before the request generator tries to serialize
  them as strict JSON. A negative regression reproduces the former
  validate-then-raise mismatch.
- Reqwise diagram metadata `title` and `artifact_id` must be nonempty
  strings if supplied. Invalid user input can no longer silently fall
  back to a convincing synthetic `ANGENT <type>` title.
- The Reqwise sequence adapter now preserves explicit message IDs and
  typed `fragments[]` for `alt`, `opt`, `loop`, `par` and `break`.
  The test corpus has separate authorized and denied fleet-status
  responses; the alt branch references the intended message IDs.
  Validation rejects unknown/duplicate messages, duplicate cross-branch
  references, non-contiguous message blocks and missing alt else
  branches. The deployed upstream request validator must still be
  checked at the pinned revision; no Figma Reqwise diagram was actually
  written by the adapter.
- At branch `a0020605470619e19ec3500f12ded804b556b7aa`,
  [GitHub Actions run 39025474218](https://github.com/anmh1205/angent/actions/runs/39025474218)
  passed Core, BA/Figma regression, pinned upstream Reqwise validator and
  generated Next.js production/browser tests. The earlier failing runs
  in this sequence contained an erroneous Python test assertion that
  was corrected, not a Figma canvas execution fault.

### First isolated real Figma Plugin API probe

- **Target (purpose-built, not an existing user design):**
  [ANGENT BA-Figma isolated adapter acceptance](https://www.figma.com/design/zQRnq4uANZBdSGkHBxEAXo).
- Live Figma provider returned file key `zQRnq4uANZBdSGkHBxEAXo`.
  A hand-authored native Plugin API probe created frame ID `1:2`
  (`ANGENT BA / login / Fleet operator access`) and four child TEXT
  nodes `1:3`–`1:6` named `screen:title`, `label:email`,
  `label:password` and `label:submit`. Their read-back values
  matched the written labels; font load and bounded frame creation
  succeeded. `get_screenshot` returned a 390×156 PNG render
  for frame ID `1:2`.
- **Proved:** Live Figma file access and the basic
  `createFrame/createText/loadFontAsync/getNodeByIdAsync` native
  creation/read-back path, plus screenshot availability on an isolated file.
- **Not proved:** The generated `figma-native-plugin.js` itself was
  *not* executed on this live file; no live mock-accurate identity
  reconciliation, rollback, whole-screen layout quality, prototype
  interactions, Reqwise `figma_diagram` provider session or live
  Jira/Confluence sync was tested. Do not promote the BA `ba-figma`
  capability to fully provider-verified from this probe.
- **Source/runtime distinction:** The screenshot and returned node IDs
  are live provider evidence, not output of ANGENT's unexecuted
  generated script. Native Figma APIs and Reqwise's Figma sandbox
  remain different contracts.

### Expert evaluations still required

All 13 tracked BA/Figma specialist scenarios remained marked `not-run`
at this checkpoint. Their acceptance is behavioral: each needs an
actual agent-produced output, independent grading against the documented
`must` and `reject` criteria, and a traceable source or provider
receipt when appropriate. Offline unit/regression pass counts cannot
establish that outcome.
