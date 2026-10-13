# Shopify app lifecycle

Handle:
- installation/authorization;
- scope changes;
- session/token storage;
- webhook registration/verification;
- billing/subscription;
- uninstall cleanup;
- reinstallation;
- API version upgrades.

Do not assume an installed shop still has valid scopes/session state.

Keep Admin API secrets/tokens on trusted server-side boundaries.
