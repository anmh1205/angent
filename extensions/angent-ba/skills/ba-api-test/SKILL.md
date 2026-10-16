---
name: ba-api-test
description: Business analysis api-test specialist.
---

# ANGENT BA: api-test

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-test/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /api-test — Bruno collection + API test table (API chain [5])

## Goal

Expand each `CHK-` in the integration checklist into a Bruno request (`.bru`) + a row in the test table (request summary + expected response: status + the key field to assert). **Outputs**: `docs/{feature}/test/api/api-tests.md` (type `api-tests`) + `docs/{feature}/bruno/` (one collection per provider).

## Constraints

- **Step [5]** (`api-integration.md`): needs `test/api/api-checklist.md`. Checklist missing → refuse + route `/api-checklist`.
- **Back-fill the checklist's `TC` column** — each generated request links back to its `CHK-`.
- **One collection per provider** — mirrors the `api-summary-{provider}.md` split; environment variables for base URL/auth, never hardcode secrets in `.bru`.
- **`.bru` only for automatable rows** — `test_layer: own` rows that test only our code may stay as unit tests outside Bruno; `3rd`/`mixed` rows become Bruno requests hitting the sandbox.
- **Expected = status + key field** — not the whole body; the one field that proves the call (e.g. `200 + response.claim_id`), plus the error-case expectations.
- **No live production calls** — sandbox/test environment only; flag if the only environment is prod.
- **Migration on rerun** — legacy test files still under `integration/` move to `test/api/` (naming-conventions line 60).
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/api-test <feature>          # expand every api-checklist CHK- with no TC yet
```

## Approach

1. **Gate.** No api-checklist → refuse + route `/api-checklist`. Read it (every `CHK-`, its layer/direction, what it covers) + the summary (request shapes/auth).
2. **Per `CHK-` → a request plan** — method/path, the env vars, the body, the expected status + key assertion field. `own`-only rows → note as unit-test, no `.bru`.
3. **Fact-list** — per request: the endpoint, the assertion, the provider, the env.
4. **Generate Bruno** — one collection per provider; one `.bru` per automatable row; env vars for base URL + auth (placeholders, never secrets).
5. **Draft `api-tests.md`** — the table (CHK · title · `.bru` · method/path · expected status · key assertion · provider).
6. **scoped change preview** — request count by provider + the assertions + any `own`-row skipped-as-unit.
9. **Output report** — requests generated + next (`/api-readiness`).

## Gotchas

- **Secrets never in `.bru`** — env var placeholders only; a committed token is a security incident.
- **Sandbox ≠ prod behavior** — some providers' sandboxes differ from prod (rate limits, webhook delivery); note where you can't prove prod parity.
- **Don't run against prod** — the skill generates requests; running them against prod from the doc is the user's explicit, careful choice.
- **Assertion economy** — assert the one field that proves success; asserting the whole brittle body makes the test fail on every cosmetic provider change.
