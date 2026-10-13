# Handoff redaction patterns

Never persist:
- API keys;
- access/refresh tokens;
- JWTs;
- session cookies;
- passwords;
- private keys;
- credential files;
- secret environment values;
- unrelated personal/private data.

## Prefer pointers

Instead of copying sensitive material, record:
- secret/provider name without value;
- file/key identifier;
- statement that authenticated state exists;
- command/test result with secret values removed.

## Logs and command output

Before embedding snippets:
- remove authorization headers;
- redact query/body secrets;
- remove cookies;
- inspect URLs for tokens;
- avoid full environment dumps.

## Unverified data

Redaction does not make unverified state authoritative.

If evidence is missing, say “not captured” or “not verified” rather than reconstructing from memory.

## Successor rule

The successor gathers fresh sensitive evidence through the authorized provider/tool when needed. Handoff should not become a credential transport mechanism.
