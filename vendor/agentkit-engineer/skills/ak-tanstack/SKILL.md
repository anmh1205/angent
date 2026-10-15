---
name: ak-tanstack
description: Build with the installed TanStack Start, Router, Form and AI packages using current package-specific server/client, validation, streaming and security contracts.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# TanStack — Portable Fallback

The pinned stable workflow covers **TanStack Start, Router, Form and AI**.

It does **not** claim TanStack Query/Table/Virtual as part of this Skill's packaged capability. Route those concerns to project-native guidance or another appropriate skill.

Read `references/package-boundaries.md` and current official docs for the installed versions.

## Establish the actual stack

Identify exactly which packages/versions are installed.

Do not assume:
- Start because Router is present;
- Form because Start is present;
- AI because the application has chat;
- package APIs from the 2.19.0 snapshot are still current.

TanStack AI was alpha in the pinned package snapshot but current official docs have advanced beyond that; use the installed/current package contract, not the old maturity label. citeturn852002search4turn852002search11

## Start / Router

Preserve:
- file/route tree ownership and generated-file boundaries;
- loader/beforeLoad/error/pending behavior;
- SSR/data-only/client rendering mode actually configured;
- server function versus public server-route boundary;
- server-only secrets and database/provider access;
- middleware/auth/CSRF/origin behavior.

Current Start docs describe server functions as same-origin RPC and distinguish them from public server routes; preserve that security boundary. citeturn852002search3turn852002search15

## Form

Preserve:
- typed field/form state;
- sync/async validation;
- correct validation event timing;
- submit-state and server-side business invariants;
- accessibility of errors/submission state;
- installed schema-library compatibility.

Validation behavior changes across versions; inspect current docs instead of pasting a package-era adapter pattern. citeturn852002search1turn852002search8

## AI

Preserve:
- server/provider credential boundary;
- streaming transport and cancellation/error behavior;
- typed output/tool contracts;
- client/server tool execution boundary;
- persistence/sandbox/subagent/MCP behavior only when supported by the installed version;
- provider/model selection as current runtime configuration.

Do not keep the package-era “Alpha/not production-ready” label as current truth. citeturn852002search9turn852002search11

## Workflow

1. Inspect installed package versions and project conventions.
2. Assign the concern to Start/Router, Form or AI.
3. Read the current official package docs for the exact feature.
4. Reuse generated-file/project conventions; never hand-edit generated route trees.
5. Implement loading/error/security/validation/streaming states that apply.
6. Add focused tests for the changed package boundary.
7. Verify runtime behavior in the real application.
8. Report version-specific assumptions and unresolved upgrade risk.

Do not mix patterns from Next.js, React Router, older TanStack generations or unrelated TanStack packages without checking compatibility.
