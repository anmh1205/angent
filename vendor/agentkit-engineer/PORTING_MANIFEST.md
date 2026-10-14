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

Current accepted coverage: **20 / 102 Skill identities reviewed semantically**.

- **19 VERIFIED_ADAPTED**: `ak-agentkit`, `ak-bootstrap`, `ak-code-review`, `ak-cook`, `ak-debug`, `ak-deploy`, `ak-git`, `ak-github`, `ak-goal-warmup`, `ak-handoff`, `ak-handover`, `ak-orchestrate`, `ak-plan`, `ak-research`, `ak-review-pr`, `ak-ship`, `ak-skill-creator`, `ak-test`, `ak-worktree`.
- **1 VERIFIED_DEGRADED**: `ak-team` because a real live-team lifecycle is load-bearing and cannot be truthfully emulated by ordinary subagents/sequential roles.
- **82 REVIEW_PENDING**: no semantic acceptance claim yet.

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


## Skills — 102 identities

| Skill | Status | Note |
|---|---|---|
| `ak-advise` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-agent-browser` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentize` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentkit` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-ai-artist` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ai-multimodal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ak` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-ask` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-autoresearch` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-backend-development` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-better-auth` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-bootstrap` | VERIFIED_ADAPTED | stable 2.19.0 workflow semantics reviewed; portable runtime substitution explicit |
| `ak-brainstorm` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
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
| `ak-design` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-devops` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-docs` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-docs-seeker` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-document-skills` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-excalidraw` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-fable-thinking` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-find-skills` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-fix` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-folder-context` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-frontend-design` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-frontend-development` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
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
| `ak-scout` | REVIEW_PENDING | prior implementation present; semantic review pending |
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
| `ak-ui-styling` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ui-ux-pro-max` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-use-mcp` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-vibe` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-watzup` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-web-design-guidelines` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-frameworks` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-testing` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
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
