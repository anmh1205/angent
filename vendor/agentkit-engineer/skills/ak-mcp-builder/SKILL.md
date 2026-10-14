---
name: ak-mcp-builder
description: Build workflow-oriented, typed, least-privilege MCP servers and verify them in a real client with realistic agent tool-use evaluations.
metadata: {port: angent-fallback, mode: adapted}
---

# MCP Builder — Portable Fallback

Stable Engineer 2.19.0 MCP Builder defines **four phases**: research & plan, implementation, review/build, and evaluations. It optimizes for AI agents accomplishing real workflows, not exhaustively mirroring HTTP API endpoints. For current protocol, transports and SDK signatures, consult the installed official MCP Python/TypeScript SDK and current specification. Upstream contains language-specific guides and an evaluation reference; this adaptation retains their decision gates without representing those guides/scripts as bundled.

Read `references/mcp-contracts.md` and `references/evaluation.md`.

## 1. Design for useful tasks

Inventory actual target API/auth models, rate limits, pagination, error codes and capability gaps. Identify the **few cohesive workflow tools** that complete real user actions. Choose Resources for retrievable state, Prompts when supported/needed, and Tools for bounded operations; do not expose a broad 'arbitrary command' escape hatch. Map each tool to end-to-end agent intent, clear input validation and readable structured output.

Plan concise/detailed output modes where useful, pagination, bounded output size, naming that helps tool selection, actionable errors and supported retry/timeout/idempotency semantics. Identify read-only, destructive, irreversible and open-world effects independently rather than trusting a vague write/read label.

## 2. Implement

Use the current **FastMCP/Python SDK with Pydantic** or **TypeScript MCP SDK with Zod**, depending on project. Read actual installed APIs, not stale `registerTool` examples. Implement a thin provider adapter, typed schemas and argument constraints, secure credential resolution, client-scope/tenant authorization, bounded pagination and consistent error taxonomy. Tool annotations (read-only, destructive, idempotent, open-world) are declarative hints; enforce actual server-side permission checks as well.

Preserve user-facing data fidelity, avoid stringifying arbitrary provider JSON into unbounded blobs, and document which tool to use, what parameters mean and how to recover from invalid requests.

## 3. Build, run and inspect

Check imports/build/type/static tests, provider failure paths, invalid arguments, auth, duplicate writes and timeout/cancellation. MCP servers may block indefinitely on stdio/HTTP when run as the main process; start via test harness or controlled child process, with lifecycle timeout/cleanup, rather than treating an idle server as a hung task.

Use actual transport/client handshake and tool/resource listing to verify discovery, schema and output. Secure logging and never expose provider keys to the model.

## 4. Evaluate with agents

Define **realistic multi-tool, stable and independently verifiable** user tasks (the pinned original suggests 10 representative read-only questions as one evaluation strategy). Check tool discovery, argument selection, result interpretability, pagination, recoverable errors and full task outcome. Use safe/mock environments for destructive-path tests; don't execute unintended external writes during an evaluation.

Deliver tool inventory/schema and effects, tested SDK/protocol/client versions, evaluation cases with outcomes, auth/data risks and known unsupported operations. A server that starts successfully but cannot reliably complete the intended workflow fails acceptance.

## Execution boundary

Creating/updating deployment, external service credentials or remote resources requires actual authorization. Never assert MCP client compatibility without the handshake and tests on that client. No unnecessary separate MCP framework is needed when the project already supplies an owner for its business logic.
