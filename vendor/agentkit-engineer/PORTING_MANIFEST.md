# Engineer full-port manifest

Target: **102/102 Skills + 16/16 Agents** available through ANGENT when native AgentKit Engineer is unavailable.

Native AgentKit remains preferred when usable and is installed/managed from the official AgentKit distribution. This manifest tracks ANGENT's portable fallback only.

## Status meanings

- **IMPLEMENTED** — portable fallback exists in this repository.
- **ADAPTED** — implemented with runtime/tool replacement while preserving capability semantics.
- **DEGRADED** — implemented with an explicit limitation because the original runtime capability cannot be reproduced in the active harness.

No Skill/Agent is removed from the target merely because upstream depends on AgentKit CLI, Claude/Codex, hooks, browser tooling, or a runtime-specific surface.

## Skills — 102 total

| Skill | Status | Note |
|---|---|---|
| `ak-advise` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-agent-browser` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-agentize` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-agentkit` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-ai-artist` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-ai-multimodal` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-ak` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-ask` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-autoresearch` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-backend-development` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-better-auth` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-bootstrap` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-brainstorm` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-chrome-profile` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-code-review` | IMPLEMENTED | Portable fallback present |
| `ak-codex-goal` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-coding-level` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-common` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-context-engineering` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-cook` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-copywriting` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-cti-expert` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-databases` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-debug` | IMPLEMENTED | Portable fallback present |
| `ak-deep-swe` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-deploy` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-design` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-devops` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-docs` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-docs-seeker` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-document-skills` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-excalidraw` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-fable-thinking` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-find-skills` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-fix` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-folder-context` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-frontend-design` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-frontend-development` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-git` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-github` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-gkg` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-goal-warmup` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-google-adk-python` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-graphify` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-handoff` | IMPLEMENTED | Portable fallback present |
| `ak-handover` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-help` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-html-video` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-hyperframes` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-interview-docs` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-issue-to-plan` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-journal` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-llms` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-loop` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-markdown-novel-viewer` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-mcp-builder` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-media-processing` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-mermaidjs-v11` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-mintlify` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-mobile-development` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-orchestrate` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-payment-integration` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-plan` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-plans-kanban` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-predict` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-preview` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-problem-solving` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-project-management` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-project-organization` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-react-best-practices` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-remotion` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-repomix` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-research` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-research-prompt` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-retro` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-review-pr` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-scenario` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-scout` | IMPLEMENTED | Portable fallback present |
| `ak-security` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-security-scan` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-sequential-thinking` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-shader` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-ship` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-shopify` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-show-off` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-skill-creator` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-stitch` | IMPLEMENTED | DEGRADED fallback implemented |
| `ak-tanstack` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-team` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-tech-graph` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-test` | IMPLEMENTED | Portable fallback present |
| `ak-threejs` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-ui-styling` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-ui-ux-pro-max` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-use-mcp` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-vibe` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-watzup` | IMPLEMENTED | ADAPTED fallback implemented |
| `ak-web-design-guidelines` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-web-frameworks` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-web-testing` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-worktree` | IMPLEMENTED | PORTABLE fallback implemented |
| `ak-xia` | IMPLEMENTED | ADAPTED fallback implemented |

## Agents — 16 total

All 16 portable role definitions are implemented under `vendor/agentkit-engineer/agents/`.

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
