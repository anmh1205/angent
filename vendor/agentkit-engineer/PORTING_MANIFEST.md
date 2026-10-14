# Engineer portable fallback parity ledger

Upstream packaged baseline: **AgentKit Engineer stable 2.19.0**.

Verified identity surface: **102/102 Skill directories + 16/16 Agent role identities** are present in the ANGENT fallback.

This identity match is not a semantic-parity verdict. Stable 2.19.0 remains under workflow-semantic/support-surface review; each row stays REVIEW_PENDING until its outcome, modes, gates, domain/support knowledge, runtime-specific dependencies, and portable replacement have been checked.

Native AgentKit remains preferred when usable and is installed/managed from the official AgentKit distribution. This manifest tracks ANGENT's portable fallback only.

## Status meanings

- **REVIEW_PENDING** — identity exists, but semantic parity against the pinned upstream package has not yet been accepted.
- **VERIFIED_PORTABLE** — the useful workflow semantics are preserved without material runtime substitution.
- **VERIFIED_ADAPTED** — the useful workflow semantics are preserved through an explicit harness-neutral replacement.
- **VERIFIED_DEGRADED** — the portable fallback preserves the safe/useful subset and records a real capability boundary that cannot be reproduced without native AgentKit/runtime machinery.

A shorter fallback can be better than a literal source copy, but size reduction is not evidence of parity. Acceptance is based on behavior and knowledge required for the workflow outcome.

No Skill/Agent is removed merely because upstream depends on AgentKit CLI, Claude/Codex, hooks, browser tooling, or another runtime-specific surface. Runtime mechanics are adapted; load-bearing workflow/domain semantics are not silently discarded.

## Current audit evidence

- Signed stable changelog resolves Engineer **2.19.0** as the current stable package.
- A fresh stable 2.19.0 portable export resolves **102 Skills** and **16 Agent sidecar roles**.
- Fallback identity diff is exact: no upstream-only or fallback-only Skill directory.
- At the initial inventory baseline, the upstream portable Skill tree contained about **1428 support files** versus **236** in the fallback; only **112** same relative paths overlap.
- At that initial baseline, upstream SKILL.md surfaces contained about **20,150 lines / 545 direct support references** versus fallback **3,632 lines / 136 direct support references**.
- These size/path figures are triage signals only; they do not prove that an independently adapted shorter workflow is wrong.

The old docs-derived assumption of 103 public Skills with eight missing/new identities is superseded by signed package evidence. The stable “choose a Skill” page is a usage guide, not the packaged-identity inventory.

## Semantic review progress

Current accepted coverage: **102 / 102 Skill identities reviewed semantically**.

- **74 VERIFIED_ADAPTED**: `ak-advise`, `ak-agentize`, `ak-agentkit`, `ak-autoresearch`, `ak-backend-development`, `ak-better-auth`, `ak-bootstrap`, `ak-brainstorm`, `ak-code-review`, `ak-codex-goal`, `ak-coding-level`, `ak-context-engineering`, `ak-cook`, `ak-copywriting`, `ak-databases`, `ak-debug`, `ak-deploy`, `ak-devops`, `ak-docs`, `ak-docs-seeker`, `ak-document-skills`, `ak-fable-thinking`, `ak-find-skills`, `ak-fix`, `ak-folder-context`, `ak-frontend-design`, `ak-frontend-development`, `ak-git`, `ak-github`, `ak-goal-warmup`, `ak-google-adk-python`, `ak-handoff`, `ak-handover`, `ak-help`, `ak-html-video`, `ak-interview-docs`, `ak-issue-to-plan`, `ak-llms`, `ak-loop`, `ak-mcp-builder`, `ak-media-processing`, `ak-mermaidjs-v11`, `ak-mobile-development`, `ak-orchestrate`, `ak-payment-integration`, `ak-plan`, `ak-predict`, `ak-project-management`, `ak-project-organization`, `ak-react-best-practices`, `ak-research`, `ak-research-prompt`, `ak-retro`, `ak-review-pr`, `ak-scenario`, `ak-scout`, `ak-security`, `ak-security-scan`, `ak-sequential-thinking`, `ak-shader`, `ak-ship`, `ak-shopify`, `ak-skill-creator`, `ak-tanstack`, `ak-tech-graph`, `ak-test`, `ak-ui-styling`, `ak-use-mcp`, `ak-vibe`, `ak-web-design-guidelines`, `ak-web-frameworks`, `ak-web-testing`, `ak-worktree`, `ak-xia`.
- **25 VERIFIED_DEGRADED**: `ak-agent-browser`, `ak-ai-artist`, `ak-ai-multimodal`, `ak-ak`, `ak-chrome-profile`, `ak-cti-expert`, `ak-deep-swe`, `ak-design`, `ak-excalidraw`, `ak-gkg`, `ak-graphify`, `ak-hyperframes`, `ak-journal`, `ak-markdown-novel-viewer`, `ak-mintlify`, `ak-plans-kanban`, `ak-preview`, `ak-remotion`, `ak-repomix`, `ak-show-off`, `ak-stitch`, `ak-team`, `ak-threejs`, `ak-ui-ux-pro-max`, `ak-watzup`.
- **3 VERIFIED_PORTABLE**: `ak-ask`, `ak-common`, `ak-problem-solving`.
- **0 REVIEW_PENDING**: no identities await first-pass workflow review; runtime and full support-corpus parity remain separate verification gates.

This batch was judged by primary outcome, materially distinct modes, critical gates, reusable support/domain knowledge, runtime assumptions and the explicit portable replacement. Same-path support-file absence remains an audit lead rather than an automatic failure: several accepted portable Skills intentionally reorganize upstream knowledge into smaller harness-neutral references.

No status is promoted solely from identity, line count, reference count, or textual similarity.

### Context, documentation and research support batch

Reviewed `ak-context-engineering`, `ak-folder-context`, `ak-docs`, `ak-docs-seeker`, `ak-interview-docs`, `ak-research-prompt` and `ak-project-organization` against the signed stable 2.19.0 export. The adapted fallback retains context quality evaluation, runtime-aware signal limits, subtree instruction authority, four distinct docs operations, versioned official documentation discovery, interview ownership, a standalone research-brief contract and a separated advisory/authorized-move workflow. Upstream-only telemetry hooks and docs-fetch scripts are not represented as available runtime tools.

### Native CLI, browser, consultation and content workflows

Reviewed the stable 2.19.0 published workflows for browser, authenticated profile, native CLI, Codex goal, advice, agentization, help and issue-to-plan; paired with upstream export evidence for copywriting and journal. Verified adapted advisory and tooling contracts, while external browser/profile, AgentKit CLI and journal/social mechanics are explicitly degraded when unavailable. No shell/browser/session effect is implied by the presence of its Markdown fallback.

### Delivery/runtime batch

The second accepted batch reviewed `ak-ship`, `ak-deploy`, `ak-git`, `ak-github`, `ak-handover` and `ak-worktree`.

Key corrections included:
- Handover now preserves the selected-runtime contract and blocks instead of silently falling back to another execution path.
- Deploy retains provider-family recognition while treating current project/provider docs and live help as authority for commands, product limits and pricing.
- Git/GitHub preserve live identity/state, history safety, issue/PR/Actions/admin boundaries and untrusted-provider-content handling.
- Ship preserves official/beta/dry-run/optional publication semantics without inheriting the upstream convenience rule that automatically sweeps unrelated uncommitted work into shipping.
- Worktree preserves create/list/status/remove/prune, exact-branch/base/monorepo/submodule semantics while cleanup remains fail-safe.



### Causal-repair and decision-workflow batch

This batch reviewed `ak-fix`, `ak-scout`, `ak-autoresearch`, `ak-brainstorm` and `ak-advise`.

Key corrections:
- Fix restores bounded intent, scout-before-diagnose, evidence-backed root cause, mode semantics, blast-radius/no-side-effect verification and non-convergence escalation.
- Scout remains read-only reconnaissance, with explicit delegation and external-provider data-sharing boundaries rather than equating scouting with subagent spawning.
- Autoresearch is a router for the measurable iteration contract; Loop/Predict/Scenario/Security own executable workflows.
- Brainstorm stays proportional and contract-first, while Advise preserves its manually invoked one-question-at-a-time pressure-test and confirmed reframing. They are intentionally not collapsed into one interaction pattern.

### UI / frontend / web-quality batch

This batch reviewed `ak-design`, `ak-frontend-design`, `ak-frontend-development`, `ak-ui-styling`, `ak-ui-ux-pro-max` and `ak-web-testing`.

Key acceptance findings:
- Design preserves authentic brand/source-of-truth inspection, concept-first exploration, production constraints and exported-result review; upstream packaged generator/search datasets remain an explicit degraded boundary.
- Frontend Design preserves the visual-thesis → complete states/responsive behavior → implementation/rendered verification loop and rejects generic template-mode collapse without turning heuristics into style bans.
- Frontend Development derives React/router/data/component/styling contracts from the current project instead of forcing upstream-specific MUI/TanStack choices.
- UI Styling preserves project tokens/primitives, mutation boundaries around shadcn/Tailwind generators, representative interaction states, accessibility and rendered verification.
- UI/UX Pro Max preserves product-level design reasoning, systemic-vs-local findings, persistent approved rules and implementation re-verification; packaged recommendation datasets are explicitly not claimed.
- Web Testing preserves layer selection, environment/account/test-data boundaries, flakiness diagnosis, browser/visual/a11y/performance distinctions and exact coverage reporting.

The stable public guides support these workflow boundaries; acceptance still rests on the pinned 2.19.0 package plus the portable fallback implementation, not documentation text alone.

### Backend / data / DevOps / security batch

This batch reviewed `ak-backend-development`, `ak-databases`, `ak-devops` and `ak-security`. `ak-security-scan` was provisionally treated as a docs-level compatibility route here, then reopened and corrected by direct package-artifact review in the package-truth batch below.

Key corrections and acceptance findings:
- Backend Development now preserves bounded implementation against the current stack, external contract/state ownership, explicit migration/deployment authority and verification proportional to the runtime claim.
- Databases now preserves engine/environment identity, least-privilege access, production recovery evidence, coexistence-aware migrations and the distinction between analysis/preparation and production mutation.
- DevOps now preserves source-of-truth/current-vs-desired state, plan/apply separation, create/update/replace/delete consequences, GitOps/controller ownership, runtime readiness and rollback/forward-fix boundaries.
- Security now preserves stable fast-mode precedence, default comprehensive audit, red-team perspectives, user-bounded iterations, fix guards, redaction and network/advisory evidence boundaries.
- The docs-level retirement route for `ak-security-scan` was not accepted as package truth; later direct inspection of the signed 2.19.0 portable artifact showed a substantive standalone scan workflow and superseded that provisional interpretation.

No status was promoted from docs alone; public stable guides were used to check workflow meaning against the pinned 2.19.0 package and the fallback implementation.

### Auth / framework / React-performance batch

This batch reviewed `ak-better-auth`, `ak-web-frameworks` and `ak-react-best-practices` against stable public workflow guidance plus the pinned 2.19.0 package boundary.

Key acceptance findings:
- Better Auth preserves project/version discovery, credentials isolation, account/session/authorization boundaries, minimal provider scope, schema-generation versus migration-execution separation, isolated email/provider testing and explicit production rollout authority.
- Web Frameworks is now correctly bounded to the stable Next.js/Turborepo-oriented workflow instead of pretending to be a universal framework cookbook; render/cache/build graph, SEO/GEO, scaffold/migration and deployment boundaries remain explicit.
- React Best Practices preserves evidence-led optimization: compatible installed versions, audit-only versus mutation mode, comparable baseline, ranked findings, semantic risk of parallelism/cache/server-client changes and same-method before/after verification.

Payment, Shopify, TanStack and mobile remain REVIEW_PENDING in this pass because the available stable documentation evidence was not sufficiently detailed to promote their semantic parity verdicts; beta documentation was not used as a substitute for the pinned stable baseline.

### Package-truth legacy workflow batch

Direct inspection of the resolved stable 2.19.0 portable artifact reopened identities that the public navigation/docs can present as retired or redirected.

Key acceptance findings:
- `ak-security-scan` is a substantive packaged read-only workflow, not merely an alias: secret scanning, dependency audit, code-pattern analysis, repository exposure checks, validation, redaction and report-only semantics are restored independently from the broader `ak-security` workflow.
- `ak-handover` package truth confirms the already accepted thin composition: Handoff capture/validation → one selected-runtime Orchestrate job → reconciliation/reporting, with no silent runtime substitution.
- `ak-use-mcp` restores the runtime-native versus deterministic-direct-client paths, exact schema discovery, project config/credential boundaries, catalog freshness and protocol/transport error semantics without copying upstream bundled client scripts.
- `ak-html-video` restores toolchain preflight, template/project discovery, Studio/preview path, explicit render output and media-artifact verification while keeping installation/source-checkout mechanics harness-dependent.
- `ak-sequential-thinking` restores revision, branching, hypothesis testing, uncertainty and meta-stall semantics while adapting the upstream visible-thought format to ANGENT's privacy boundary: no private chain-of-thought transcript is exposed or persisted.
- `ak-web-design-guidelines` restores fresh retrieval of the canonical Web Interface Guidelines source on each review plus exact source-scope/evidence reporting; source review remains distinct from rendered-browser verification.

This batch demonstrates the evidence hierarchy: docs navigation can describe migration/routing, but the resolved signed package artifact remains authoritative for what stable 2.19.0 actually packages.

### Payment / commerce / TanStack / mobile batch

This batch reviewed `ak-payment-integration`, `ak-shopify`, `ak-tanstack` and `ak-mobile-development` using the pinned package artifact plus current provider/framework documentation for facts that are intentionally volatile.

Key acceptance findings:
- Payment Integration preserves SePay/Polar/Stripe provider roles, internal-vs-provider state machines, idempotent/authenticated webhooks, ambiguous-outcome reconciliation, subscription/refund lifecycle and multi-provider accounting while refusing package-era API/rate-limit values as permanent truth.
- Shopify preserves app/extension/theme distinctions, minimal scopes, install/session/webhook/billing/uninstall lifecycle and preview/deploy/publish gates; current GraphQL Admin guidance supersedes package-era REST/version snapshots for new work.
- TanStack preserves exactly the packaged Start/Router/Form/AI capability. The previous fallback drift that treated TanStack Query as owned by this Skill was removed; current installed package/docs control version-sensitive APIs and maturity.
- Mobile preserves React Native/Flutter/native iOS/native Android selection, lifecycle/offline/permissions/security/device-testing/store boundaries while removing package-era popularity percentages and universal performance targets from the decision model.

These ports deliberately preserve workflow/domain semantics while treating provider/framework versions, rate limits, maturity labels and platform requirements as refreshable evidence.

### Diagram authoring and queryable knowledge graphs

Direct inspection of the stable 2.19.0 Mermaid Skill and five source references restored diagram selection, flow/sequence/state/ER and advanced v11 type semantics, Markdown/CLI/JS rendering, security/ARIA, exporter preflight and rendered-layout verification. The fallback now has two focused reference files rather than claiming the upstream docs and renderer are installed. Experimental diagram types must be checked against the destination's actual Mermaid version.

Graphify's stable 2.19.0 beta workflow includes graphifyy native CLI, graph.json/HTML/report/cache artifacts, AST and semantic extraction, query_graph/get_node/get_neighbors/shortest_path operations, incremental invalidation and source provenance. The portable graph substitute retains the decision/query workflow, but native parser/transcriber/web/MCP runtime parity is explicitly degraded. Documents/images sent to an external model require a visible privacy boundary; marketing token-savings numbers are not guarantees.

### Publish-grade SVG and semantic code navigation

The stable 2.19.0 Tech Graph bundle adds detailed architecture/UML/network/state/sequence layout and seven styles, SVG validation/export scripts, marker/arrow routing, typography, collision and PNG visual review gates. The adapted fallback now restores those behaviors through explicit source/renderer/tool selection and a style/layout reference without falsely claiming the bundled SVG templates or rasterizer exist. GKG preserves its seven MCP discovery/definition/reference/index/navigation operations and supported-language/incremental-index limitations; the portable fallback accurately degrades to language-server/AST/checked source tracing when GKG is unavailable.

### Optimization loops, risk forecasting and problem framing

The stable 2.19.0 Loop preserves its numeric goal/scope/verify/guard contract, sequential one-change experiments, Git memory, keep/discard result log, directional Min-Delta/noise management and nonconvergence stops. The portable replacement additionally refuses destructive resets or unapproved commits on shared/dirty branches; safety and user branch authority take precedence over the upstream convenience of committing every trial. Predict restores the five explicit architecture/security/performance/UX/devil's-advocate lenses, worst-case conflicts, advisory GO/CAUTION/STOP gates and two non-standalone reason/probe chain modes. Scenario restores all 12 candidate dimensions and distinct one-shot, bounded-iteration and two-round saturation/novelty modes without presenting generated scenarios as executed tests. Problem Solving restores the six technique families and selection/validation processes without mandatory runtime tools or artificial extra agents.

### Skill discovery, presentation calibration and plan coordination

Direct 2.19.0 package review restored explicit 0–5 coding-level selection with native Claude style-injection/persistence treated as a conditional runtime effect rather than hidden fallback behavior. Common remains internal-only; it does not introduce an independent user-facing skill. Find Skills preserves its two separate paths: choosing among actually installed AgentKit/ANGENT capabilities and using the external Skills CLI with explicit installation/update authority and source inspection. Project Management retains durable files-first plans, optional ephemeral runtime hydration, verified whole-plan phase backfill/sync-back, progress evidence and documentation-impact routing. No update to project or global user configuration is implied by any of these skill Markdown changes.

### Git retrospectives, branch handoff, plans dashboard and repository packaging

Retro restores actual Git period metrics and optional equal-length comparison, source-aware plan/issue evidence, Markdown/HTML outputs and honest missing-data handling; its metrics are descriptive, never an individual productivity score. Watzup retains the native package's scanner semantics for local/remote branches, worktrees, plans/roadmaps and priority ranking, but degrades without its Node scanner and never fetches or switches branches implicitly. Plans Kanban is specifically an integrated AgentKit CLI dashboard launcher with health/feature probes and project/global scope; a portable board is not certified native parity. Repomix preserves format/filter/remote/token/security contracts but cannot claim its CLI, batch Python script or built-in scanner exist; all three optional-runtime skills remain DEGRADED.

### AI-readable documentation, Mintlify, repository feature port and showcases

The stable 2.19.0 llms skill retains index/full file modes, project docs/title/URL extraction, format constraints, validation and exact authoring output while degrading only missing helper scripts to manual generation. Mintlify retains configuration/MDX/navigation/API/AI/CLI/deploy contracts but remains explicitly DEGRADED without its six extensive bundled versioned references/native CLI. Xia's earlier fallback incorrectly implemented source features inside Xia; this batch restores the six-phase analysis/challenge/plan handoff with compare/copy/improve/port variants and implementation only through an authorized execution owner. Show Off restores original user preferences, language modes, content-to-HTML and capture prerequisites but does not treat the upstream default publishing toggle as consent, and correctly marks native screenshot helpers/AgentWiki absent.

### External model benchmarking and deterministic media conversion

DeepSWE preserves its third-party Pier/OpenRouter runner, task/model/version preflight, single-task and fixed-subset smoke, explicit full-corpus spend authorization and real score/artifact reporting; without the actual runner/provider it remains DEGRADED. Media Processing preserves FFmpeg/ImageMagick/RMBG task routing, codec/container and metadata decisions, non-destructive batch operation, HLS/DASH manifests and output playback/perceptual verification through genuinely available tools.

### Multimodal and creative image backend boundaries

The stable Multix runtime pins an exact CLI and routes image/video/audio/music/document tasks through different provider capabilities. This portable skill resolves only actually available modalities, retains page/frame/audio provenance, tests result media and does not silently fetch executables or expose private media to third-party providers. AI Artist preserves the 129-prompt search/creative/wild catalog workflow, brief gate and rendering provider contract, but explicitly degrades without the curated scripts/data. Both require runtime validation for genuine provider parity; neither asserts an unavailable script or prompt database exists.

### CTI case, editable Excalidraw and office document routing

CTI Expert preserves AEAD case handling, evidence time/source/identity confidence and real defensive scope; its much larger specialist collection corpus remains outside the portable bundle, so the mode is DEGRADED. Excalidraw preserves live canvas versus editable .excalidraw JSON with rendered validation and a source-backed codebase auto-diagram route; its real MCP/browser tool must still be present. Document Skills acts as a high-fidelity destination router to installed DOCX/PDF/PPTX/XLSX authoring and validation engines, not an imaginary built-in replacement for over a hundred upstream helper documents.

### Proportional reasoning, Google ADK and MCP builder contracts

Fable Thinking retains its always-run floor, proportional depth, five evidence/decision moves and mechanically checked exact-output constraints without private reasoning disclosure or a proprietary model claim. Google ADK restores versioned Python entrypoint/agent graph selection, session versus durable state/memory, MCP/A2A contracts and eval/deployment proof. MCP Builder restores four separate user-workflow research, typed SDK implementation, live client integration and agent-facing verification phases, including server lifecycle, read/write authorization and error recovery. SDK compatibility is verified in the executing project rather than presumed from this portable text.

### HTML-first video, long-form reader and preview modes

HyperFrames retains its pinned HTML composition timing, lint-before-render, local MP4 QA and separate authorized HeyGen cloud pathway. Markdown Novel Viewer retains source-root/localhost-safe file/directory HTTP reader behavior, reading navigation, responsive rendering and Mermaid support without pretending its Node server package is installed. Preview now distinguishes read-only view, Markdown/HTML explanation/diagram/slides, visual Git diff, plan review and recaps with exact source and rendered acceptance; its upstream HTML templates/server are not bundled. All three remain DEGRADED until their native runtimes are verified, while a host-native substitution may still fulfill a specific user-facing output.

### Frame-exact video and shader rendering

Remotion now preserves composition/frame counts, useCurrentFrame deterministic motion, asset/caption/audio alignment and real rendered-video acceptance; the upstream 33-rule pack and renderer remain absent in the fallback, so it is DEGRADED. Shader preserves target GLSL version/fragment output, UV/aspect/SDF/noise and explicit shader compile, framebuffer visual and performance checks, adapted to runtime-provided graphics tools. Both avoid claiming graphics output from unexecuted source code.

### UI design provider, Three.js scene graph and end-to-end Vibe orchestration

Stitch retains its project-aware quota/generate/edit/export and design-to-code normalization, with provider/account/cost and actual artifact gates; it remains DEGRADED without the native SDK/provider. Three.js retains the WebGL/WebGPU scene, asset loading/disposal, interactions and visual/GPU performance gates but honestly distinguishes an absent 556-example search corpus from native knowledge search. Vibe retains worktree/plan/Cook/Fix/review/PR and explicitly authorized --ship, --beta, --both and --advice modes with PR/CI read-back; user- and branch-level restrictions always override workflow convenience. These three complete the **first-pass semantic identity review of all 102 skills**, not a claim that optional vendor runtimes or all upstream auxiliary scripts have been installed and exercised.

## Skills — 102 identities

| Skill | Status | Note |
|---|---|---|
| `ak-advise` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-agent-browser` | VERIFIED_DEGRADED | stable 2.19.0 session/snapshot/browser effect semantics; external CLI/specialized provider absent |
| `ak-agentize` | VERIFIED_ADAPTED | stable 2.19.0 agent tool CLI/MCP design, effect safety and consumer verification preserved |
| `ak-agentkit` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-ai-artist` | VERIFIED_DEGRADED | native 129-prompt catalog/BM25/provider modes mapped, backend and catalog unavailable |
| `ak-ai-multimodal` | VERIFIED_DEGRADED | pinned Multix 0.2.0 modality/provider contracts, evidence/privacy and native substitutes; CLI unavailable |
| `ak-ak` | VERIFIED_DEGRADED | stable 2.19.0 native AgentKit CLI control-plane without emulated lifecycle |
| `ak-ask` | VERIFIED_PORTABLE | stable 2.19.0 one-question, evidence-led, four-perspective consultation with no implementation |
| `ak-autoresearch` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-backend-development` | VERIFIED_ADAPTED | stable 2.19.0 bounded backend/API/data-access workflow reviewed; migration/deploy and runtime verification boundaries preserved |
| `ak-better-auth` | VERIFIED_ADAPTED | stable 2.19.0 Better Auth workflow reviewed; credentials, schema/migration, session/provider and production rollout boundaries preserved |
| `ak-bootstrap` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-brainstorm` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-chrome-profile` | VERIFIED_DEGRADED | stable 2.19.0 profile-identity/sensitive-state safeguards; real Chrome attachment runtime-dependent |
| `ak-code-review` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-codex-goal` | VERIFIED_ADAPTED | stable 2.19.0 goal frontier, stop criteria and honest harness-independent execution bounds |
| `ak-coding-level` | VERIFIED_ADAPTED | stable 2.19.0 explicit 0–5 reader levels and runtime-specific style/persistence limits retained |
| `ak-common` | VERIFIED_PORTABLE | stable 2.19.0 internal-only shared support role; no phantom scripts or user invocation |
| `ak-context-engineering` | VERIFIED_ADAPTED | stable 2.19.0 Measured context/runtime boundaries, four-bucket lifecycle and decision-quality evaluation retained; no fabricated provider telemetry |
| `ak-cook` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-copywriting` | VERIFIED_ADAPTED | stable 2.19.0 conversion patterns, channel composition, evidence and style boundaries reviewed |
| `ak-cti-expert` | VERIFIED_DEGRADED | AEAD cases, provenance, scope/privacy and defensive reporting; specialist 113-file support pack not ported |
| `ak-databases` | VERIFIED_ADAPTED | stable 2.19.0 data-model/query/migration workflow reviewed with least-privilege, recovery and production-mutation gates |
| `ak-debug` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-deep-swe` | VERIFIED_DEGRADED | stable 2.19.0 Pier/OpenRouter one-task/subset/full-cost gates and confidential benchmark evidence; native runner absent |
| `ak-deploy` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-design` | VERIFIED_DEGRADED | stable 2.19.0 design workflow reviewed; bundled generator/search datasets are an explicit portable capability boundary |
| `ak-devops` | VERIFIED_ADAPTED | stable 2.19.0 infrastructure/CI/CD/GitOps workflow reviewed with plan/apply/delete/replace and readiness/recovery gates |
| `ak-docs` | VERIFIED_ADAPTED | stable 2.19.0 Init/update/summarize/agent-context modes plus drift-resistant ownership and verification restored |
| `ak-docs-seeker` | VERIFIED_ADAPTED | stable 2.19.0 Versioned canonical docs and llms.txt discovery preserved; unbundled Node scripts explicitly non-operative |
| `ak-document-skills` | VERIFIED_ADAPTED | format-specific native Word/PDF/Slides/Sheets capability dispatch, source and render gates |
| `ak-excalidraw` | VERIFIED_DEGRADED | native MCP canvas and editable JSON/Playwright modes, semantic maps and render QA; backend not bundled |
| `ak-fable-thinking` | VERIFIED_ADAPTED | floor/proportional FRAME-GROUND-REASON-ATTACK-DELIVER, strict exact-output checks and truthful evidence |
| `ak-find-skills` | VERIFIED_ADAPTED | stable 2.19.0 local domain routing versus external Skills CLI discovery/install authority retained |
| `ak-fix` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-folder-context` | VERIFIED_ADAPTED | stable 2.19.0 Subtree-only sanity/approval gate and canonical AGENTS.md compatibility restored |
| `ak-frontend-design` | VERIFIED_ADAPTED | stable 2.19.0 visual-direction/state/render-verification semantics preserved with harness-native implementation/render tools |
| `ak-frontend-development` | VERIFIED_ADAPTED | stable 2.19.0 frontend implementation semantics preserved while project-specific libraries are derived from the current codebase |
| `ak-git` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-github` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-gkg` | VERIFIED_DEGRADED | stable 2.19.0 GKG definition/reference/impact workflow and MCP/search semantics retained; native AST/index server remains optional |
| `ak-goal-warmup` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-google-adk-python` | VERIFIED_ADAPTED | ADK package entrypoint, workflows, state/memory, MCP/A2A, eval and deployed-runtime gates |
| `ak-graphify` | VERIFIED_DEGRADED | stable 2.19.0 graph build/query, provenance, media privacy and MCP/native capability boundaries restored; external Graphify runtime not bundled |
| `ak-handoff` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-handover` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-help` | VERIFIED_ADAPTED | stable 2.19.0 outcome based routing and true native/fallback capability boundaries |
| `ak-html-video` | VERIFIED_ADAPTED | stable 2.19.0 html-video template/project/preview/render workflow restored; renderer/toolchain mechanics remain harness-dependent |
| `ak-hyperframes` | VERIFIED_DEGRADED | pinned HyperFrames HTML timing/preflight/lint/MP4/cloud workflow; CLI unavailable |
| `ak-interview-docs` | VERIFIED_ADAPTED | stable 2.19.0 Vision versus structured-doc modes, user-owned decisions and per-answer read-back restored |
| `ak-issue-to-plan` | VERIFIED_ADAPTED | stable 2.19.0 issue evidence, implementation-ready plan and stop-before-code decision gate |
| `ak-journal` | VERIFIED_DEGRADED | stable 2.19.0 local journal and optional publication semantics; Zernio/media scripts not packaged |
| `ak-llms` | VERIFIED_ADAPTED | stable 2.19.0 llms.txt/llms-full.txt sources, URL scope, optional sections, generator preflight and validation |
| `ak-loop` | VERIFIED_ADAPTED | stable 2.19.0 sequential atomic, numeric/guard/noise-aware optimization, Git experiment history and safe rollback bounds |
| `ak-markdown-novel-viewer` | VERIFIED_DEGRADED | Node HTTP reader/file-dir/theme/Mermaid/plan routing with localhost and path safety; server absent |
| `ak-mcp-builder` | VERIFIED_ADAPTED | four-phase research/typed implementation/client handshake and evaluation workflow, effect semantics |
| `ak-media-processing` | VERIFIED_ADAPTED | stable 2.19.0 FFmpeg/ImageMagick/RMBG routes, codec/batch/stream quality and output verification restored |
| `ak-mermaidjs-v11` | VERIFIED_ADAPTED | stable 2.19.0 diagram families, v11 syntax, CLI/JS/Markdown targets, security, accessibility and rendered-result gates restored |
| `ak-mintlify` | VERIFIED_DEGRADED | stable 2.19.0 docs.json/MDX/navigation/OpenAPI/AI/CLI/deployment flows retained; full refs/native CLI absent |
| `ak-mobile-development` | VERIFIED_ADAPTED | stable 2.19.0 React Native/Flutter/native mobile workflow preserved while stale adoption/performance figures are excluded from architectural decisions |
| `ak-orchestrate` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-payment-integration` | VERIFIED_ADAPTED | stable 2.19.0 SePay/Polar/Stripe and multi-provider payment semantics reviewed; volatile provider APIs are refreshed from current docs and internal/provider state reconciliation is preserved |
| `ak-plan` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-plans-kanban` | VERIFIED_DEGRADED | stable 2.19.0 integrated CLI plans dashboard feature-probe/launcher contract; fallback cannot run native UI |
| `ak-predict` | VERIFIED_ADAPTED | stable 2.19.0 five-perspective debate, worst-case GO/CAUTION/STOP verdict and reason/probe follow-on modes |
| `ak-preview` | VERIFIED_DEGRADED | view versus explain/diagram/slides/HTML diff/plan-review/recap modes; template/viewer runtime absent |
| `ak-problem-solving` | VERIFIED_PORTABLE | stable 2.19.0 six technique families restored with diagnosis, concrete probes and no runtime dependency |
| `ak-project-management` | VERIFIED_ADAPTED | stable 2.19.0 durable plan hydration, all-phase sync-back, verified progress and docs-impact routing retained |
| `ak-project-organization` | VERIFIED_ADAPTED | stable 2.19.0 Advisory versus organize modes, move approval, collision protection and project naming conventions restored |
| `ak-react-best-practices` | VERIFIED_ADAPTED | stable 2.19.0 evidence-led React/Next performance workflow reviewed with compatible-version and comparable-measurement gates |
| `ak-remotion` | VERIFIED_DEGRADED | stable 2.19.0 33-rule React frame timeline, media, captions and render QA; rule pack/runtime absent |
| `ak-repomix` | VERIFIED_DEGRADED | stable 2.19.0 bounded packaging formats, remote/token/security workflow; native CLI/batch helper absent |
| `ak-research` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-research-prompt` | VERIFIED_ADAPTED | stable 2.19.0 Research-assignment-only boundary and one-paragraph evidence brief contract restored |
| `ak-retro` | VERIFIED_ADAPTED | stable 2.19.0 period/team comparisons, raw Git metrics, evidence caveats and Markdown/HTML reporting restored |
| `ak-review-pr` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-scenario` | VERIFIED_ADAPTED | stable 2.19.0 12-dimension one-shot and bounded/saturation novelty modes with test-oracle output |
| `ak-scout` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-security` | VERIFIED_ADAPTED | stable 2.19.0 comprehensive/fast/red-team/fix semantics reviewed; runtime scanners and advisory access remain harness-dependent |
| `ak-security-scan` | VERIFIED_ADAPTED | stable 2.19.0 packaged standalone read-only security-scan semantics restored from artifact truth; not collapsed into ak-security |
| `ak-sequential-thinking` | VERIFIED_ADAPTED | stable 2.19.0 revision/branch/hypothesis/uncertainty semantics preserved while private chain-of-thought exposure is intentionally omitted |
| `ak-shader` | VERIFIED_ADAPTED | GLSL version-aware fragment/SDF/noise/coordinate pipeline with compile/visual/GPU QA |
| `ak-ship` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-shopify` | VERIFIED_ADAPTED | stable 2.19.0 app/extension/theme lifecycle reviewed with current GraphQL-first API, scope/webhook/version and deploy/publish boundaries |
| `ak-show-off` | VERIFIED_DEGRADED | stable 2.19.0 prefs/plan/bilingual HTML/screenshots/publishing gates; capture/helper/AgentWiki unavailable |
| `ak-skill-creator` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-stitch` | VERIFIED_DEGRADED | Stitch quota/generate/edit/export and per-project identity with design-to-code handoff; provider absent |
| `ak-tanstack` | VERIFIED_ADAPTED | stable 2.19.0 Start/Router/Form/AI scope restored; unrelated TanStack Query/Table/Virtual expansion removed and volatile package APIs bound to current installed docs |
| `ak-team` | VERIFIED_DEGRADED | true live-team lifecycle is load-bearing; hard-stop/route elsewhere when harness lacks it |
| `ak-tech-graph` | VERIFIED_ADAPTED | stable 2.19.0 diagram views, seven style families, SVG/PNG workflow, routing/label/layout and rendered QA retained with runtime tool substitution |
| `ak-test` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-threejs` | VERIFIED_DEGRADED | Three.js scene/WebGL-WebGPU/runtime QA; upstream 556-example search corpus absent |
| `ak-ui-styling` | VERIFIED_ADAPTED | stable 2.19.0 component/tokens/shadcn-Tailwind mutation and rendered-accessibility gates preserved |
| `ak-ui-ux-pro-max` | VERIFIED_DEGRADED | stable 2.19.0 product UX decision workflow preserved; packaged recommendation dataset/search engine is not reproduced |
| `ak-use-mcp` | VERIFIED_ADAPTED | stable 2.19.0 runtime-native/direct-client discovery and MCP config/protocol/effect semantics preserved without vendoring upstream scripts |
| `ak-vibe` | VERIFIED_ADAPTED | issue-to-worktree-plan-implement-review-PR with optional explicitly authorized beta/stable shipping and CI |
| `ak-watzup` | VERIFIED_DEGRADED | stable 2.19.0 branch/worktree/plan/roadmap scanning and priority ranking; native scanner not bundled |
| `ak-web-design-guidelines` | VERIFIED_ADAPTED | stable 2.19.0 fresh canonical-guideline retrieval and source-evidence review contract preserved |
| `ak-web-frameworks` | VERIFIED_ADAPTED | stable 2.19.0 Next.js/Turborepo workflow reviewed; version, render/cache/build, SEO-GEO and deployment boundaries preserved |
| `ak-web-testing` | VERIFIED_ADAPTED | stable 2.19.0 layered web-test/environment/data/flakiness/browser evidence semantics preserved |
| `ak-worktree` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-xia` | VERIFIED_ADAPTED | stable 2.19.0 compare/copy/improve/port modes, source challenge and Plan/Cook handoff, no direct Xia implementation |

## Agents — 16 identities

All 16 role identities are present under `vendor/agentkit-engineer/agents/`. In the portable AgentKit export, agents are inert sidecar role references rather than active runtime agents. ANGENT therefore evaluates transferable role behavior, not live teammate scheduling parity.

Current role-semantic review: **16/16 VERIFIED_ADAPTED; 0/16 REVIEW_PENDING**. Live team claims, permissions and agent memory remain host-specific.

| Role | Review status | Semantic evidence |
|---|---|---|
| `advisor` | VERIFIED_ADAPTED | one-question relay, confirmation gate, verified scouting and advisory-only boundary |
| `brainstormer` | VERIFIED_ADAPTED | assumption challenge, distinct architectures, feasibility, trade-offs and confirmed direction |
| `code-reviewer` | VERIFIED_ADAPTED | scout-first, critical/informational passes, evidence and read-only team boundary |
| `code-simplifier` | VERIFIED_ADAPTED | behavior-preserving recent-change refactor, ownership and before/after checks |
| `debugger` | VERIFIED_ADAPTED | incident evidence, causal timelines, hypothesis elimination, bounded diagnostics and repair |
| `docs-manager` | VERIFIED_ADAPTED | WHY/WHERE ownership, docs deletion gate and source/proof accuracy |
| `explore` | VERIFIED_ADAPTED | bounded read-only repository/symbol tracing with evidence and secret safeguards |
| `fullstack-developer` | VERIFIED_ADAPTED | phase/dependency ownership, failure handling, tests and live-team capability boundary |
| `git-manager` | VERIFIED_ADAPTED | exact staging, authorization, branch lease safety and read-back verification |
| `journal-writer` | VERIFIED_ADAPTED | grounded incident diary, evidence and human impact; verified CLI/local persistence boundary |
| `kongming` | VERIFIED_ADAPTED | single-run no-interview counsel, confidence/flip conditions and true model boundary |
| `planner` | VERIFIED_ADAPTED | file:line/consumer verification, state lifetime, risk/dependency/migration and phase contracts |
| `project-manager` | VERIFIED_ADAPTED | definition-of-done progress, risk/dependency, scope and provider status reconciliation |
| `researcher` | VERIFIED_ADAPTED | source/versions, independent evidence, adoption risks and fit-based recommendations |
| `tester` | VERIFIED_ADAPTED | diff-aware mapping, targeted/full escalation, observed evidence |
| `ui-ux-designer` | VERIFIED_ADAPTED | UX, brand/visuals, Vietnamese typography, accessibility and rendered review |

The accepted role batches compared each selected stable 2.19.0 sidecar with its ANGENT fallback and explicitly restored the domain-specific steps while preserving read-only review, source ownership and host/runtime limitations.

The advisory, diagnostic, implementation and planning batch preserves the upstream advisor's interview/reframing-confirmation and relay safety without assuming Claude model or state hooks; debugger's incident triage, timelines, data/CI/performance diagnostics and evidence-backed root-cause gates; fullstack-developer's strict parallel phase/file ownership with bounded implementation and observed verification; and planner's source revalidation, caller/flow/lifetime tracing, dependency sequencing, migration, risk and rollback contracts.

The exploration and Git batch restores Brainstormer's architecture/feasibility debate and explicit decision consensus; Code Simplifier's behavior-preserving, recent-change refinement and file ownership; Explore's strictly read-only symbol-first reconnaissance; and Git Manager's narrow staging, conventional history and checked remote-ref updates. Source edits, plan creation, team coordination and native model execution are never inferred from an inert role file.

The final role batch restores Journal Writer's concrete chronological engineering failures, real human impact, CLI/local persistence and publication boundary; Kongming's one-shot advice with stated confidence and model/runtime limitations; Project Manager's acceptance-backed task state and explicit risk/dependency/scope reconciliation; and Researcher's source credibility, version verification, adoption risk and architecture-fit comparisons. All 16 role identities are now semantically reviewed; this does **not** certify live runtime/team/model equivalence. Inert sidecars still do not establish a live team or native agent relay.

## Upstream evidence boundary

See `UPSTREAM_BASELINE.md` for the exact stable release/artifact evidence and why documentation navigation is not used as packaged-inventory authority.

The upstream portable export is audit/source material only. ANGENT does not vendor a raw upstream mirror.

## Maintenance rule

When an upstream Engineer capability changes or a fallback regression is found:

1. identify the capability and quality gates that changed;
2. preserve the useful behavior rather than upstream invocation syntax;
3. map runtime-specific mechanics to harness-native capability when available;
4. keep a sequential/local replacement when parallel/native machinery is unavailable;
5. state real limitations instead of pretending parity;
6. keep strategic ownership in ANGENT Reasoning;
7. verify the changed behavior before updating the manifest.

The fallback is an ANGENT implementation, not a mirror of upstream AgentKit source.
