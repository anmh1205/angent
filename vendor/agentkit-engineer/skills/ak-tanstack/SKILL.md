---
name: ak-tanstack
description: Build with the installed TanStack packages using explicit router/server-state/form/AI boundaries and current version documentation.
metadata: {port: angent-fallback, mode: portable}
---

# TanStack — Portable Fallback

Read `references/package-boundaries.md`.

## Establish the actual stack

Identify which packages and versions exist: Start, Router, Query, Form, AI or others.

Do not assume that a project using one TanStack package uses the rest.

## Workflow

1. Read current package versions and official documentation.
2. Assign ownership correctly: routing, server state, form state and streaming/tool transport are separate concerns.
3. Follow the project's existing route/query/form conventions.
4. Model loading, error, invalidation and mutation states explicitly.
5. Keep server-only and client behavior separated where the framework requires it.
6. Add focused tests for loaders/server functions, cache invalidation or validation behavior that changed.
7. Verify runtime behavior in the actual application.

TanStack packages evolve quickly.

Do not mix patterns from Next.js, React Router or older TanStack generations without checking compatibility.
