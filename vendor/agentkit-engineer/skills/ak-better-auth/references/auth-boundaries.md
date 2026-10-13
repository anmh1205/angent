# Authentication boundaries

Define:
- identity source;
- account linking;
- session creation/rotation/revocation;
- cookie security;
- CSRF/state/nonce behavior for browser auth;
- provider callback validation;
- MFA/recovery;
- authorization roles/permissions;
- tenant/resource ownership.

Keep secrets server-side.

Test session expiry and revoked/disabled-user behavior, not only successful login.
