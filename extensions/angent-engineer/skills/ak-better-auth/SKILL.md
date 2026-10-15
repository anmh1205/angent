---
name: ak-better-auth
description: Plan and implement a Better Auth integration in an existing JavaScript/TypeScript application while keeping credentials, schema changes, sessions, provider scope and production rollout explicit.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Better Auth — Portable Fallback

Use only when Better Auth is already selected or present in the application. Use Brainstorm/Advise when the authentication product is still undecided, Backend Development for general auth/backend work, and Security for an independent security review.

Read `references/auth-boundaries.md`.

## Contract

Resolve from the actual project:
- framework/runtime/package-manager and Better Auth version;
- database/ORM and current user/session schema;
- route/handler layout and cookie/origin policy;
- sign-in methods and provider scopes;
- session lifetime, account-linking, verification, reset/recovery and deletion behavior;
- organization/role/permission semantics when used;
- allowed package install, schema generation, migration execution, email/provider calls, provider-console changes and deployment;
- required server/client/callback/session/authorization evidence.

Keep auth secrets, database URLs, OAuth client secrets, mail-provider credentials and production tokens out of prompts, logs, code and Git.

## Workflow

1. Inspect the installed Better Auth and framework versions plus the project's existing auth/session conventions.
2. Define the user-visible flow and identity/account-linking policy before changing code.
3. Configure the server/client integration using the current project pattern; examples are patterns, not proof that an API/helper exists in this version.
4. Preserve minimal provider scopes, constrained redirects/callbacks, secure cookies/session rotation/revocation and CSRF/state/nonce behavior where applicable.
5. Keep authentication separate from resource authorization and tenant ownership.
6. Generate schema artifacts only within the authorized file boundary.
7. Treat migration execution as a separate effect; do not apply generated migrations merely because schema generation was requested.
8. Use fake/local mail capture and test tenants/accounts when possible; do not send real recovery/verification messages during tests without explicit authority.
9. Test success and failure paths: invalid input, duplicate/account-link cases, expiry/revocation, disabled/unverified users, callback mismatch, recovery, and signed-out access.
10. Report changed files/packages, environment-variable **names** only, generated/unapplied migration artifacts, test evidence and production rollout checklist.

## Production boundary

Provider-console changes, production credentials, live email/SMS, database migration, commit/push, publication and deployment are separate effects.

A successful login proves authentication, not authorization.

If the installed Better Auth/project version differs from a bundled example, preserve the project and current official API rather than creating shims only to match the example.
