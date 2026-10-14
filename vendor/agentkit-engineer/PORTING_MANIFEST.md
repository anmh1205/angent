# Engineer stable-port manifest

Target: **103/103 current stable public Skills + 16/16 Agent roles** available through ANGENT when native AgentKit Engineer is unavailable or unusable.

Native AgentKit remains preferred when usable and is installed/managed from the official AgentKit distribution. This manifest tracks ANGENT's independent portable fallback only.

## Upstream basis

- channel: **stable**
- catalog retrieved: **2026-10-14**
- Skill catalog: https://docs.agentkit.best/en/stable/kits/engineer/skills
- Engineer Kit composition: https://docs.agentkit.best/en/stable/kits/engineer
- Agent roster: https://docs.agentkit.best/en/stable/kits/engineer/agents
- machine-readable fallback expectation: `STABLE_CATALOG.json`

Current stable documentation resolves **103 public Skill identities** and **16 Agent roles**.

The fallback is parity-targeted to workflow semantics and public identity, not byte-for-byte upstream source or runtime mechanics.

## Portability meanings

- **PORTABLE** — behavior can be expressed with ordinary agent/project capabilities without relying on one AgentKit runtime implementation.
- **ADAPTED** — preserves workflow semantics but maps upstream helpers/runtime surfaces to capabilities actually provided by the active harness.
- **DEGRADED** — preserves the contract and explicit limitations when a native runtime capability cannot be reproduced safely.

A DEGRADED route must not claim native runtime guarantees it does not have.

## Skills — 103 current public identities

| Skill | Portability | Fallback state |
|---|---|---|
| `ak-advise` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-agent-browser` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-agentize` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-agentkit` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-ai-artist` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-ai-multimodal` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-ak` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-ask` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-autoresearch` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-backend-development` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-better-auth` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-bootstrap` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-brainstorm` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-bro` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-chrome-profile` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-code-review` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-codex-goal` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-coding-level` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-context-engineering` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-cook` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-copywriting` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-cti-expert` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-databases` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-debug` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-deep-swe` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-deploy` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-design` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-devops` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-diagram` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-docs` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-docs-seeker` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-document-skills` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-enhance-ux-ax` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-excalidraw` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-explain` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-fable-thinking` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-find-skills` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-fix` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-folder-context` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-frontend-design` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-frontend-development` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-git` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-github` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-gkg` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-goal-warmup` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-google-adk-python` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-graphify` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-handoff` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-help` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-hyperframes` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-interview-docs` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-issue-to-plan` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-journal` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-llms` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-loop` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-markdown-novel-viewer` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-mcp-builder` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-media-processing` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-mermaidjs-v11` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-mintlify` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-mobile-development` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-orchestrate` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-page-builder` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-payment-integration` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-plan` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-plans-kanban` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-predict` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-preview` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-problem-solving` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-project-management` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-project-organization` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-react-best-practices` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-remotion` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-repomix` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-research` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-research-prompt` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-retro` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-review-pr` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-scenario` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-scout` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-security` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-shader` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-ship` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-shopify` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-show-off` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-skill-creator` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-sowat` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-stitch` | DEGRADED | Implemented as ANGENT portable fallback |
| `ak-sumup` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-tanstack` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-team` | ADAPTED | Live-team lifecycle is required; unsupported harnesses hard-stop rather than emulate Team |
| `ak-tech-graph` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-test` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-threejs` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-ui-styling` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-ui-ux-pro-max` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-vibe` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-watzup` | ADAPTED | Implemented as ANGENT portable fallback |
| `ak-web-frameworks` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-web-testing` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-webmcp` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-worktree` | PORTABLE | Implemented as ANGENT portable fallback |
| `ak-xia` | ADAPTED | Implemented as ANGENT portable fallback |

## Removed from public discovery

These historical routes are **not** packaged current Skill identities and therefore are not kept under `skills/`:

- `ak-security-scan`
- `ak-use-mcp`
- `ak-handover`
- `ak-html-video`
- `ak-sequential-thinking`
- `ak-web-design-guidelines`

Migration routes live in `COMPATIBILITY.md`.

`ak-common` is internal support rather than a user workflow and now lives under `internal/common-conventions.md`.

## Agents — 16 portable role definitions

All 16 fallback role definitions remain under `agents/`:

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

The official Engineer roster uses runtime-specific projection and includes a canonical `Explore` display identity; the portable file/role ID remains `explore`.

## Readiness semantics

Fallback readiness requires more than a count:

1. fallback plugin manifest is valid;
2. `STABLE_CATALOG.json` is valid and internally consistent;
3. discovered public Skill identity set exactly matches the expected 103;
4. discovered Agent role set exactly matches the expected 16;
5. no retired/internal identity leaks into public Skill discovery.

`scripts/select_engineer.py` checks the exact sets and reports missing/extra identities.

## Maintenance rule

When stable Engineer changes:

1. establish the current stable resolved catalog from official sources;
2. separate public identities, retired routes, aliases and nested support files;
3. identify behavior/gates that materially changed;
4. preserve useful workflow semantics rather than invocation syntax or raw upstream runtime code;
5. adapt runtime-specific mechanics to the active harness only when the semantics remain honest;
6. keep explicit limitations where parity is impossible;
7. update `STABLE_CATALOG.json`, affected Skills/routers, selector readiness and this manifest together;
8. calibrate changed behavior on real representative cases before claiming parity.

Do not claim parity from a directory count alone.
