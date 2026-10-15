---
name: ak-google-adk-python
description: Design, implement, evaluate and deploy version-verified Google ADK Python agents, workflows, MCP/A2A tools and correct state/artifact lifecycles.
license: Apache-2.0
metadata: {port: angent-fallback, mode: adapted}
---

# Google ADK Python — Portable Fallback

Use for Python applications powered by Google's Agent Development Kit: single agent, dynamic subagents, deterministic sequential/parallel/loop workflows, remote A2A, MCP-tool bridges, session state, durable memory, callbacks/plugins, evaluations and Cloud Run/Vertex/GKE deployment. Exact API signatures and model names vary by installed ADK release; **current package and official documentation outrank pinned examples**.

Read `references/agent-architecture.md`, `references/evaluation-deployment.md` and `references/runtime-contracts.md` when state, concurrency or integrations matter.

## Entrypoint and workflow selection

Stable Engineer 2.19.0 conventions: a Python package with `__init__.py` importing `agent` and `agent.py` exporting `root_agent = Agent(...)` or `app = App(...)`. Confirm current ADK discovery conventions before scaffolding.

Choose LlmAgent/Agent for model-selected tool use, SequentialAgent when order is a contract, ParallelAgent only for independently owned concurrent work, LoopAgent with a real termination bound, and RemoteA2aAgent when another networked agent is actually needed. Use App for legitimate plugin/event-compaction/lifecycle ownership, not speculative layers.

## Tool and state contracts

Separate **session state** (e.g., `tool_context.state`) from durable MemoryService, recorded artifacts, request/task context and shared provider resources. Specify tenant isolation, serialization, concurrent write ownership, timeout/cancellation and recovery. A session-scoped object does not become durable by calling it memory.

Register typed tools with authorization, argument constraints, structured errors and safe retry/idempotency. MCPToolset, connection transports and A2A identities/network paths must be verified for the real installed SDK. Capture trace/metrics in callbacks/plugins without exposing secrets or sensitive raw interactions. Human confirmation remains necessary for consequential effects.

## Verification and delivery

Run representative tool-choice, permission denial, state isolation, artifact persistence, concurrency/failure tests and an ADK evalset where usable. Confirm real CLI `adk web`, `adk run`, `adk eval` or `adk api_server` commands with installed help before use. Deployment to Cloud Run, Vertex AI Agent Engine or GKE requires separately authorized access and actual endpoint/monitoring smoke after rollout; a successful import or build is not deployment verification.

Report exact files/API versions, actual test/eval results, provider/runtimes exercised, deployment effect status and remaining compatibility uncertainty.
