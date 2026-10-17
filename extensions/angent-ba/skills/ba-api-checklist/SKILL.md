---
name: ba-api-checklist
description: Business analysis api-checklist specialist.
---

# ANGENT BA: api-checklist

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-checklist/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /api-checklist — Integration test outline (API chain [4])

## Goal

Derive the integration test outline from the design (orchestration/webhook/retry) + the map (field transforms) — `CHK-{NNN}` rows carrying `test_layer` (own/3rd/mixed) and `direction` (out/in) per `api-integration.md`. **Single output**: `docs/{feature}/test/api/api-checklist.md` (type `api-checklist`). Expanded by `/api-test` into Bruno requests.

## Constraints

- **Step [4]** (`api-integration.md`): needs `api-design.md` (+ `api-map.md` if present). Design missing → refuse + route `/api-design`.
- **Path-scoped `CHK-`** under `test/api/` (`test-conventions.md`) — no collision with the feature-wide `test/checklist/` (different folder).
- **Two integration-specific columns** — `test_layer` (own/3rd/mixed) + `direction` (out/in) on every row, per `api-integration.md`.
- **Webhook ⇄ reconciliation coverage** — every webhook row has a "happy" check AND a "missed-webhook → reconciliation" check (the pair the design mandated).
- **Degraded-UX coverage** — the design's degraded paths get `test_layer: own` rows (we can test our fallback without the provider).
- **Every row Covers a design/map decision** — a row with no source is fabrication.
- **The `TC` column starts empty** — `/api-test` fills it.
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/api-checklist <feature>          # derive from design + map
```

## Approach

1. **Gate.** No design → refuse + route `/api-design`. Read the design (orchestration/webhooks/retry/degraded) + the map (transforms to verify).
2. **Derive candidates** — per endpoint: an `out` functional + an error (their error response); per webhook: happy `in` + reconciliation `mixed`; per degraded path: an `own` fallback; per transform: a boundary check.
3. **Classify** — assign `test_layer` + `direction` per row.
4. **Assign `CHK-` IDs** — scan the existing api-checklist for max (path-scoped, independent of the feature-wide checklist's max).
5. **Draft** per the template — rows with test_layer/direction, `Covers` filled, `TC` empty.
6. **scoped change preview** — row count by layer + direction + the webhook⇄reconciliation pairs + degraded coverage.
9. **Output report** — layer/direction breakdown + next (`/api-test`).

## Gotchas

- **Webhook reconciliation is the high-value row** — the "happy webhook" check almost always passes; the "missed webhook → reconciliation polls" check catches the data-loss bug. Don't drop it.
- **`3rd` rows may be unautomatable** — testing their sandbox availability is real but flaky; flag those for manual/periodic, not the CI gate.
- **Don't merge with the feature checklist** — different folder, different scope; `/gap` joins both via the CHK/TC spine.
- **Degraded-UX is `own`-testable** — that's the point of testing it: our fallback works without the provider.
