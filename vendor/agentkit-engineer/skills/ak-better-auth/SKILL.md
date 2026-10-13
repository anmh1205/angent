---
name: ak-better-auth
description: Integrate Better Auth with explicit authentication, session, provider, MFA/passkey, RBAC and deployment security boundaries.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Better Auth — Portable Fallback

Read `references/auth-boundaries.md`.

## Workflow

1. Identify installed Better Auth version/current docs.
2. Define authentication methods and account-link behavior.
3. Define session/storage/cookie policy.
4. Configure OAuth/provider secrets through secure environment mechanisms.
5. Model authorization/RBAC separately.
6. Add MFA/passkey/recovery only when required.
7. Add abuse/rate-limit controls.
8. Test login/logout/expiry/callback/error/recovery flows.

Do not infer authorization from successful authentication.
