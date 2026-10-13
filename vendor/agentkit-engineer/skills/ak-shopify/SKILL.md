---
name: ak-shopify
description: Build Shopify apps, themes and extensions using the current Shopify APIs/CLI with explicit auth, webhook, billing and deployment lifecycle.
metadata: {port: angent-fallback, mode: portable}
---

# Shopify — Portable Fallback

Read `references/app-lifecycle.md`.

## Workflow

1. Identify app/theme/extension type and API version.
2. Read current Shopify docs/toolchain.
3. Model install/auth/session/scopes.
4. Implement webhooks idempotently.
5. Integrate billing where required.
6. Build UI/extension using supported platform constraints.
7. Test uninstall/reinstall/expired-session/error paths.
8. Preview before publishing.

Publishing to a live store is a separate authorized effect.
