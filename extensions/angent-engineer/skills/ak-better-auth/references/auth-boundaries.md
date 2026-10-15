# Better Auth boundaries

Define:
- identity source and canonical user identity;
- account linking/merge rules;
- supported login methods and minimal provider scopes;
- exact callback/redirect origins;
- session creation, rotation, expiry and revocation;
- cookie domain/path/SameSite/Secure/HttpOnly policy;
- CSRF/state/nonce behavior for browser OAuth;
- email verification, password reset and recovery;
- MFA/passkey policy when enabled;
- organization/role/permission semantics;
- tenant/resource ownership and authorization;
- user deletion/deactivation semantics.

Keep secrets server-side.

## Schema and migration

Schema generation and migration execution are different effects.

Before applying auth schema changes:
- compare generated tables/columns with enabled plugins and the current database;
- preserve existing user/account/session data compatibility;
- establish backup/recovery and rollout ordering when production is involved;
- do not run production migration merely because generated files exist.

## Tests

Cover session expiry/revocation and disabled/unverified users, not only successful login.

For OAuth, test exact callback/origin behavior and account-linking boundaries.

For email/magic-link/reset flows, use isolated/fake delivery where possible so tests do not send real messages.

Authentication success never substitutes for authorization tests.
