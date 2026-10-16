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
