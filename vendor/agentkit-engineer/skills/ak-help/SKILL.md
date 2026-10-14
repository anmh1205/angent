---
name: ak-help
description: Explain available ANGENT fallback capabilities and point native AgentKit users to the official AgentKit help/documentation surfaces.
metadata: {port: angent-fallback, mode: adapted}
---

# Help — Portable Fallback

Use when the user asks what Engineer/ANGENT can do or which workflow to run.

## Native AgentKit

When native AgentKit is usable, point to:
- https://agentkit.best
- https://docs.agentkit.best/en/stable
- the installed/native AgentKit help surface.

Do not reproduce the entire upstream help index inside ANGENT.

## Fallback

Use `PORTING_MANIFEST.md` and active fallback catalog to explain:
- implemented Skills;
- available Agents;
- known degraded capabilities;
- recommended workflow for the user's outcome.

Prefer task-oriented help over dumping a list of 102 names.

## Stable 2.19.0 outcome router
Select by result rather than dumping every installed name: `ak-ask` for a narrow architecture answer; `ak-advise` for guided problem reframing; `ak-brainstorm` for choices; `ak-scout`/`ak-research` for evidence; `ak-plan`/`ak-issue-to-plan` for planning; `ak-cook` for authorized implementation; `ak-debug` for cause; `ak-fix` for proven repair; `ak-test`/`ak-code-review` for validation; `ak-ship`/`ak-deploy` for delivery.

Prefer actually installed native AgentKit help and its live CLI/catalog when usable. In fallback, `PORTING_MANIFEST.md` gives semantic review and degraded boundaries: a packaged directory or sidecar agent name never establishes browser/CLI/worker availability. Return an actionable shortest supported workflow, relevant invocation and honest limitations, rather than generic skill advertising.
