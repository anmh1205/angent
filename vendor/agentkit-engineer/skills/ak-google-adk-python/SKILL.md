---
name: ak-google-adk-python
description: Build and evaluate Python agents using the installed/current Google ADK APIs with explicit tools, workflows, state/memory and deployment boundaries.
license: Apache-2.0
metadata: {port: angent-fallback, mode: portable}
---

# Google ADK Python — Portable Fallback

## Load progressively

- `references/agent-architecture.md` — agent/tool/workflow/state design.
- `references/evaluation-deployment.md` — evaluation and runtime deployment.

## Workflow

1. Identify installed/target ADK version and current official docs.
2. Define agent responsibility and tool boundary.
3. Choose single-agent vs workflow/multi-agent structure based on need.
4. Model session state and memory explicitly.
5. Integrate tools/MCP/A2A with typed contracts.
6. Add callbacks/plugins only for real cross-cutting needs.
7. Evaluate representative tasks/failure cases.
8. Deploy only to an authorized target.

Avoid stale API signatures from memory.
