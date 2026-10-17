---
name: ak-shopify
description: Build Shopify apps, extensions and themes against current Shopify APIs/CLI with explicit surface selection, scopes, API versions, webhook lifecycle, development-store testing and deployment/publish gates.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Shopify — Portable Fallback

Use when Shopify itself is the platform boundary.

Read `references/app-lifecycle.md` and `references/platform-surfaces.md`.

## Route the surface first

Distinguish:
- **app/backend integration** — store data, admin/business logic, billing and webhooks;
- **UI/function extension** — code rendered/executed in a Shopify-defined extension surface;
- **theme/theme app extension** — storefront presentation/content integration.

Do not choose an app, extension or theme route merely because a CLI command exists.

## Current-source rule

Shopify APIs, extension targets, CLI commands, scopes and version windows change frequently.

Inspect the current project config and current Shopify docs before prescribing exact commands/API versions.

For new Admin API work, prefer GraphQL Admin; Shopify's [API surface guidance](https://shopify.dev/docs/apps/build/apis) identifies REST Admin as legacy. Inspect compatibility before changing an existing integration.

## Workflow

1. Resolve app/theme/extension type, store/environment, CLI/project/API version and current source of truth.
2. Define exact access scopes and keep them minimal.
3. Keep Admin/API secrets and privileged tokens on trusted server boundaries.
4. Implement installation/auth/session and scope-change behavior for apps.
5. Use current GraphQL patterns, pagination/bulk operations and cost/rate-limit handling appropriate to the API.
6. Verify webhook authenticity, idempotency, API-version handling and uninstall/data-lifecycle obligations.
7. For extensions, preserve the target surface's supported API/components and authentication model.
8. For themes, work against a development/unpublished target unless the user explicitly authorizes live publication.
9. Test uninstall/reinstall, expired/revoked session, missing scope, webhook failure/duplicate, API-version and representative store-plan/surface constraints.
10. Preview/development-test before deploy/publish.
11. Treat deploy, theme push to a live target, publish, billing activation and production-store mutation as separate authorized effects.

## Lifecycle

An installed shop is not proof that its token/scopes are still valid.

Preserve:
- installation and authorization;
- scope changes;
- token/session state;
- webhook registration/verification;
- billing/subscription if used;
- mandatory privacy/data lifecycle where applicable;
- uninstall cleanup;
- reinstallation;
- API version upgrade path.

## Completion

CLI success does not prove the requested Shopify behavior.

Verify the actual app/extension/theme state in the intended development or authorized live surface.
