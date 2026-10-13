---
name: ak-frontend-development
description: Implement maintainable React/TypeScript frontends using the project's actual framework, component system, data layer and performance constraints.
metadata: {port: angent-fallback, mode: portable}
---

# Frontend Development — Portable Fallback

## Workflow

1. Inspect existing component/data/router/design-system patterns.
2. Read applicable AGENTS.md.
3. Define UI states: loading, empty, success, error, auth/permission and responsive behavior.
4. Reuse project components/tokens before creating new abstractions.
5. Keep server/client/state boundaries appropriate to the framework version.
6. Implement accessibility and keyboard behavior where relevant.
7. Add component/integration tests and runtime/browser verification.
8. Measure performance before applying non-trivial optimizations.

Do not blindly apply framework patterns from another version.

Do not infer UI quality from source code when rendered inspection is available.
