# Web test environment and data

## Environment identity

Before tests that can mutate state, resolve:
- base URL/environment;
- provider/account/project;
- test user/account;
- backend/data store if shared;
- feature flags/config that materially affect behavior.

A local browser pointed at production is still a production effect boundary.

## Authentication

Prefer project-native test auth/fixtures.

If an authorized real browser/profile is used:
- do not export cookies/tokens;
- preserve the user-selected account/environment;
- stop for required manual login rather than invent credentials.

## Test data

Prefer:
- isolated fixtures;
- seeded disposable records;
- idempotent setup/cleanup.

Do not delete unrelated data during cleanup.

## External services

Mock/fake when the acceptance claim allows it.

Use real provider integration only when required and authorized; preserve cost/rate-limit/side-effect boundaries.

## Visual artifacts

Screenshots/traces/video can contain sensitive user/project data. Store/share only when authorized and redact when needed.
