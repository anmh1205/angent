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

## Skills — 102 identities

| Skill | Status | Note |
|---|---|---|
| `ak-advise` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-agent-browser` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentize` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-agentkit` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ai-artist` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ai-multimodal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-ak` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-ask` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-autoresearch` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-backend-development` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-better-auth` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-bootstrap` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-brainstorm` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-chrome-profile` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-code-review` | REVIEW_PENDING | prior implementation present; semantic review pending |
| `ak-codex-goal` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-coding-level` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-common` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-context-engineering` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-cook` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-copywriting` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-cti-expert` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-databases` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-debug` | REVIEW_PENDING | prior implementation present; semantic review pending |
| `ak-deep-swe` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-deploy` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
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
| `ak-git` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-github` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-gkg` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-goal-warmup` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-google-adk-python` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-graphify` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-handoff` | REVIEW_PENDING | prior implementation present; semantic review pending |
| `ak-handover` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
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
| `ak-orchestrate` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-payment-integration` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-plan` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-plans-kanban` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-predict` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-preview` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-problem-solving` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-project-management` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-project-organization` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-react-best-practices` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-remotion` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-repomix` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-research` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-research-prompt` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-retro` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-review-pr` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-scenario` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-scout` | REVIEW_PENDING | prior implementation present; semantic review pending |
| `ak-security` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-security-scan` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-sequential-thinking` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-shader` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ship` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-shopify` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-show-off` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-skill-creator` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-stitch` | REVIEW_PENDING | prior mode: DEGRADED; semantic review pending |
| `ak-tanstack` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-team` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-tech-graph` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-test` | REVIEW_PENDING | prior implementation present; semantic review pending |
| `ak-threejs` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ui-styling` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-ui-ux-pro-max` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-use-mcp` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-vibe` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-watzup` | REVIEW_PENDING | prior mode: ADAPTED; semantic review pending |
| `ak-web-design-guidelines` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-frameworks` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-web-testing` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
| `ak-worktree` | REVIEW_PENDING | prior mode: PORTABLE; semantic review pending |
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
