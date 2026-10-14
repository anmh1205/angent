# Engineer stable-port manifest

Target: **103/103 public Skills + 16/16 Agent roles** available through ANGENT when native AgentKit Engineer is unavailable or unusable.

Native AgentKit remains preferred when the active harness can actually discover/invoke it. This manifest tracks ANGENT's independent portable fallback against the stable semantic/catalog baseline recorded in `UPSTREAM_BASELINE.md`.

## Status meanings

- **IMPLEMENTED** — a discoverable portable fallback Skill exists.
- **PORTABLE** — workflow semantics map directly to ordinary model/tool capabilities.
- **ADAPTED** — AgentKit-specific mechanics are replaced by harness-native capability while preserving the workflow outcome and gates.
- **DEGRADED** — useful semantics remain, but a runtime-dependent part cannot be reproduced; the limitation must be explicit.

Missing runtime capability is not silently counted as parity. A workflow that requires a live browser, renderer, team lifecycle, provider surface, or other runtime must verify that capability or stop/degrade at the documented boundary.

## Public Skills — 103 total

| Skill | Status | Port mode |
|---|---|---|
| `ak-advise` | IMPLEMENTED | PORTABLE |
| `ak-agent-browser` | IMPLEMENTED | ADAPTED |
| `ak-agentize` | IMPLEMENTED | ADAPTED |
| `ak-agentkit` | IMPLEMENTED | ADAPTED |
| `ak-ai-artist` | IMPLEMENTED | ADAPTED |
| `ak-ai-multimodal` | IMPLEMENTED | ADAPTED |
| `ak-ak` | IMPLEMENTED | DEGRADED |
| `ak-ask` | IMPLEMENTED | PORTABLE |
| `ak-autoresearch` | IMPLEMENTED | ADAPTED |
| `ak-backend-development` | IMPLEMENTED | PORTABLE |
| `ak-better-auth` | IMPLEMENTED | PORTABLE |
| `ak-bootstrap` | IMPLEMENTED | ADAPTED |
| `ak-brainstorm` | IMPLEMENTED | PORTABLE |
| `ak-bro` | IMPLEMENTED | PORTABLE |
| `ak-chrome-profile` | IMPLEMENTED | ADAPTED |
| `ak-code-review` | IMPLEMENTED | PORTABLE |
| `ak-codex-goal` | IMPLEMENTED | ADAPTED |
| `ak-coding-level` | IMPLEMENTED | ADAPTED |
| `ak-context-engineering` | IMPLEMENTED | ADAPTED |
| `ak-cook` | IMPLEMENTED | ADAPTED |
| `ak-copywriting` | IMPLEMENTED | PORTABLE |
| `ak-cti-expert` | IMPLEMENTED | ADAPTED |
| `ak-databases` | IMPLEMENTED | PORTABLE |
| `ak-debug` | IMPLEMENTED | PORTABLE |
| `ak-deep-swe` | IMPLEMENTED | DEGRADED |
| `ak-deploy` | IMPLEMENTED | ADAPTED |
| `ak-design` | IMPLEMENTED | PORTABLE |
| `ak-devops` | IMPLEMENTED | PORTABLE |
| `ak-diagram` | IMPLEMENTED | ADAPTED |
| `ak-docs` | IMPLEMENTED | ADAPTED |
| `ak-docs-seeker` | IMPLEMENTED | ADAPTED |
| `ak-document-skills` | IMPLEMENTED | ADAPTED |
| `ak-enhance-ux-ax` | IMPLEMENTED | ADAPTED |
| `ak-excalidraw` | IMPLEMENTED | ADAPTED |
| `ak-explain` | IMPLEMENTED | PORTABLE |
| `ak-fable-thinking` | IMPLEMENTED | ADAPTED |
| `ak-find-skills` | IMPLEMENTED | ADAPTED |
| `ak-fix` | IMPLEMENTED | ADAPTED |
| `ak-folder-context` | IMPLEMENTED | ADAPTED |
| `ak-frontend-design` | IMPLEMENTED | PORTABLE |
| `ak-frontend-development` | IMPLEMENTED | PORTABLE |
| `ak-git` | IMPLEMENTED | PORTABLE |
| `ak-github` | IMPLEMENTED | ADAPTED |
| `ak-gkg` | IMPLEMENTED | DEGRADED |
| `ak-goal-warmup` | IMPLEMENTED | ADAPTED |
| `ak-google-adk-python` | IMPLEMENTED | PORTABLE |
| `ak-graphify` | IMPLEMENTED | ADAPTED |
| `ak-handoff` | IMPLEMENTED | PORTABLE |
| `ak-help` | IMPLEMENTED | ADAPTED |
| `ak-hyperframes` | IMPLEMENTED | DEGRADED |
| `ak-interview-docs` | IMPLEMENTED | PORTABLE |
| `ak-issue-to-plan` | IMPLEMENTED | ADAPTED |
| `ak-journal` | IMPLEMENTED | ADAPTED |
| `ak-llms` | IMPLEMENTED | PORTABLE |
| `ak-loop` | IMPLEMENTED | ADAPTED |
| `ak-markdown-novel-viewer` | IMPLEMENTED | ADAPTED |
| `ak-mcp-builder` | IMPLEMENTED | PORTABLE |
| `ak-media-processing` | IMPLEMENTED | PORTABLE |
| `ak-mermaidjs-v11` | IMPLEMENTED | PORTABLE |
| `ak-mintlify` | IMPLEMENTED | PORTABLE |
| `ak-mobile-development` | IMPLEMENTED | PORTABLE |
| `ak-orchestrate` | IMPLEMENTED | ADAPTED |
| `ak-page-builder` | IMPLEMENTED | ADAPTED |
| `ak-payment-integration` | IMPLEMENTED | PORTABLE |
| `ak-plan` | IMPLEMENTED | ADAPTED |
| `ak-plans-kanban` | IMPLEMENTED | ADAPTED |
| `ak-predict` | IMPLEMENTED | ADAPTED |
| `ak-preview` | IMPLEMENTED | ADAPTED |
| `ak-problem-solving` | IMPLEMENTED | PORTABLE |
| `ak-project-management` | IMPLEMENTED | ADAPTED |
| `ak-project-organization` | IMPLEMENTED | PORTABLE |
| `ak-react-best-practices` | IMPLEMENTED | PORTABLE |
| `ak-remotion` | IMPLEMENTED | PORTABLE |
| `ak-repomix` | IMPLEMENTED | DEGRADED |
| `ak-research` | IMPLEMENTED | PORTABLE |
| `ak-research-prompt` | IMPLEMENTED | PORTABLE |
| `ak-retro` | IMPLEMENTED | ADAPTED |
| `ak-review-pr` | IMPLEMENTED | ADAPTED |
| `ak-scenario` | IMPLEMENTED | PORTABLE |
| `ak-scout` | IMPLEMENTED | PORTABLE |
| `ak-security` | IMPLEMENTED | ADAPTED |
| `ak-shader` | IMPLEMENTED | PORTABLE |
| `ak-ship` | IMPLEMENTED | ADAPTED |
| `ak-shopify` | IMPLEMENTED | PORTABLE |
| `ak-show-off` | IMPLEMENTED | ADAPTED |
| `ak-skill-creator` | IMPLEMENTED | ADAPTED |
| `ak-sowat` | IMPLEMENTED | PORTABLE |
| `ak-stitch` | IMPLEMENTED | DEGRADED |
| `ak-sumup` | IMPLEMENTED | PORTABLE |
| `ak-tanstack` | IMPLEMENTED | PORTABLE |
| `ak-team` | IMPLEMENTED | ADAPTED |
| `ak-tech-graph` | IMPLEMENTED | ADAPTED |
| `ak-test` | IMPLEMENTED | PORTABLE |
| `ak-threejs` | IMPLEMENTED | PORTABLE |
| `ak-ui-styling` | IMPLEMENTED | PORTABLE |
| `ak-ui-ux-pro-max` | IMPLEMENTED | PORTABLE |
| `ak-vibe` | IMPLEMENTED | ADAPTED |
| `ak-watzup` | IMPLEMENTED | ADAPTED |
| `ak-web-frameworks` | IMPLEMENTED | PORTABLE |
| `ak-web-testing` | IMPLEMENTED | PORTABLE |
| `ak-webmcp` | IMPLEMENTED | ADAPTED |
| `ak-worktree` | IMPLEMENTED | PORTABLE |
| `ak-xia` | IMPLEMENTED | ADAPTED |

## Agent roles — 16 total

The portable role library under `agents/` contains exactly:

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

Agent Plugins v1 does not define a portable Agent component; these files are role semantics projected into a harness-native subagent/worker or applied sequentially when delegation is unavailable.

## Retired routes and internal support

The following historical upstream identities are **not public fallback Skills** and are excluded from the 103 count:

- `ak-security-scan`
- `ak-use-mcp`
- `ak-handover`
- `ak-html-video`
- `ak-sequential-thinking`
- `ak-web-design-guidelines`

Compatibility navigation lives in `retired-routes/README.md`.

`ak-common` is internal fallback guidance and lives under `internal/common.md`, outside the discovery root.

## Integrity

`scripts/select_engineer.py` validates the exact public Skill identity set and exact Agent-role identity set, not only their counts.

Stable catalog identity SHA-256: `fbe4be0fa01ff696fdc783d8e398a4fb157b7c31d831d6eb792dea55ca627a9e`.

A package with the right number of directories but a missing/retired/unexpected identity is not ready.

## Maintenance rule

When upstream stable capability changes:

1. establish the new public identity set and workflow semantics from current official stable documentation;
2. distinguish packaged public Skills from retired routes and internal/runtime helpers;
3. preserve useful workflow outcome, authority/evidence/verification gates and capability boundaries rather than invocation syntax;
4. map runtime-specific mechanics to harness-native capability only when that capability actually exists;
5. hard-stop or mark degraded where missing runtime capability removes a load-bearing workflow property;
6. keep strategic ownership in ANGENT Reasoning;
7. update exact-set integrity/provenance together with the semantic port;
8. calibrate representative changed workflows before claiming parity.

The fallback is an ANGENT implementation, not a mirror of upstream AgentKit source.
