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
- The upstream portable Skill tree contains about **1428 support files** versus **236** in the fallback; only **112** same relative paths overlap.
- Upstream SKILL.md surfaces contain about **20,150 lines / 545 direct support references** versus fallback **3,632 lines / 136 direct support references**.
- These size/path figures are triage signals only; they do not prove that an independently adapted shorter workflow is wrong.

The old docs-derived assumption of 103 public Skills with eight missing/new identities is superseded by signed package evidence. The stable “choose a Skill” page is a usage guide, not the packaged-identity inventory.

## Semantic review progress

Current accepted coverage: **31 / 102 Skill identities reviewed semantically**.

- **28 VERIFIED_ADAPTED**: `ak-advise`, `ak-agentkit`, `ak-autoresearch`, `ak-bootstrap`, `ak-brainstorm`, `ak-code-review`, `ak-cook`, `ak-debug`, `ak-deploy`, `ak-fix`, `ak-frontend-design`, `ak-frontend-development`, `ak-git`, `ak-github`, `ak-goal-warmup`, `ak-handoff`, `ak-handover`, `ak-orchestrate`, `ak-plan`, `ak-research`, `ak-review-pr`, `ak-scout`, `ak-ship`, `ak-skill-creator`, `ak-test`, `ak-ui-styling`, `ak-web-testing`, `ak-worktree`.
- **3 VERIFIED_DEGRADED**: `ak-design` and `ak-ui-ux-pro-max` preserve the load-bearing design/UX workflow but do not reproduce upstream packaged generator/search datasets; `ak-team` cannot truthfully reproduce a live-team lifecycle without harness support.
- **71 REVIEW_PENDING**: no semantic acceptance claim yet.

This batch was judged by primary outcome, materially distinct modes, critical gates, reusable support/domain knowledge, runtime assumptions and the explicit portable replacement. Same-path support-file absence remains an audit lead rather than an automatic failure: several accepted portable Skills intentionally reorganize upstream knowledge into smaller harness-neutral references.

No status is promoted solely from identity, line count, reference count, or textual similarity.

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

## Skills — 102 identities

| Skill | Status | Note |
|---|---|---|
| `ak-advise` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-agent-browser` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentize` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentkit` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-ai-artist` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ai-multimodal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ak` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-ask` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-autoresearch` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-backend-development` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-better-auth` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-bootstrap` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-brainstorm` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-chrome-profile` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-code-review` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-codex-goal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-coding-level` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-common` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-context-engineering` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-cook` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-copywriting` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-cti-expert` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-databases` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-debug` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-deep-swe` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-deploy` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-design` | VERIFIED_DEGRADED | stable 2.19.0 design workflow reviewed; bundled generator/search datasets are an explicit portable capability boundary |
| `ak-devops` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-docs` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-docs-seeker` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-document-skills` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-excalidraw` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-fable-thinking` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-find-skills` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-fix` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-folder-context` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-frontend-design` | VERIFIED_ADAPTED | stable 2.19.0 visual-direction/state/render-verification semantics preserved with harness-native implementation/render tools |
| `ak-frontend-development` | VERIFIED_ADAPTED | stable 2.19.0 frontend implementation semantics preserved while project-specific libraries are derived from the current codebase |
| `ak-git` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-github` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-gkg` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-goal-warmup` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-google-adk-python` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-graphify` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-handoff` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-handover` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-help` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-html-video` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-hyperframes` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-interview-docs` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-issue-to-plan` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-journal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-llms` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-loop` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-markdown-novel-viewer` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-mcp-builder` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-media-processing` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-mermaidjs-v11` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-mintlify` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-mobile-development` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-orchestrate` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-payment-integration` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-plan` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-plans-kanban` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-predict` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-preview` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-problem-solving` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-project-management` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-project-organization` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-react-best-practices` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-remotion` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-repomix` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-research` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-research-prompt` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-retro` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-review-pr` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-scenario` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-scout` | VERIFIED_ADAPTED | stable 2.19.0 decision/discovery/repair semantics reviewed; runtime mechanics adapted explicitly |
| `ak-security` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-security-scan` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-sequential-thinking` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-shader` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ship` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-shopify` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-show-off` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-skill-creator` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-stitch` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-tanstack` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-team` | VERIFIED_DEGRADED | true live-team lifecycle is load-bearing; hard-stop/route elsewhere when harness lacks it |
| `ak-tech-graph` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-test` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-threejs` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ui-styling` | VERIFIED_ADAPTED | stable 2.19.0 component/tokens/shadcn-Tailwind mutation and rendered-accessibility gates preserved |
| `ak-ui-ux-pro-max` | VERIFIED_DEGRADED | stable 2.19.0 product UX decision workflow preserved; packaged recommendation dataset/search engine is not reproduced |
| `ak-use-mcp` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-vibe` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-watzup` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-web-design-guidelines` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-frameworks` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-testing` | VERIFIED_ADAPTED | stable 2.19.0 layered web-test/environment/data/flakiness/browser evidence semantics preserved |
| `ak-worktree` | VERIFIED_ADAPTED | stable 2.19.0 delivery/runtime semantics reviewed; provider/harness mechanics adapted explicitly |
| `ak-xia` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |

## Agents — 16 identities

All 16 role identities are present under `vendor/agentkit-engineer/agents/`. Upstream portable export preserves Agent files as inert sidecar reference content rather than a portable runtime component, so ANGENT compares role semantics rather than claiming runtime-agent parity. Agent semantic review is still pending.

- advisor
- brainstormer
- code-reviewer
- code-simplifier
- debugger
- docs-manager
- explore
- fullstack-developer
- git-manager
- journal-writer
- kongming
- planner
- project-manager
- researcher
- tester
- ui-ux-designer

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
