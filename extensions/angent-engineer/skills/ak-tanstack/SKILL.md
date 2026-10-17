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

Use the installed package contract and the [official AI overview](https://tanstack.com/ai/latest/docs/getting-started/overview); a maturity label from the pinned upstream snapshot cannot establish the installed release's suitability.

## Start / Router

Preserve:
- file/route tree ownership and generated-file boundaries;
- loader/beforeLoad/error/pending behavior;
- SSR/data-only/client rendering mode actually configured;
- server function versus public server-route boundary;
- server-only secrets and database/provider access;
- middleware/auth/CSRF/origin behavior.

The [Start server-functions guide](https://tanstack.com/start/latest/docs/framework/react/guide/server-functions) distinguishes same-origin application RPC from server routes intended for outside callers; inspect the configured origin/CSRF protection.

## Form

Preserve:
- typed field/form state;
- sync/async validation;
- correct validation event timing;
- submit-state and server-side business invariants;
- accessibility of errors/submission state;
- installed schema-library compatibility.

Match validation timing and schema integration to the installed version using [Form and field validation](https://tanstack.com/form/latest/docs/framework/react/guides/validation), rather than copying a package-era adapter pattern.

## AI

Preserve:
- server/provider credential boundary;
- streaming transport and cancellation/error behavior;
- typed output/tool contracts;
- client/server tool execution boundary;
- persistence/sandbox/subagent/MCP behavior only when supported by the installed version;
- provider/model selection as current runtime configuration.

Consult the [AI overview](https://tanstack.com/ai/latest/docs/getting-started/overview) and installed release before judging maturity; neither an old warning nor a marketing claim establishes this project's production readiness.

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
