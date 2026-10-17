---
name: ba-api-map
description: Business analysis api-map specialist.
---

# ANGENT BA: api-map

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-map/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /api-map — 3-layer field mapping (API chain [3])

## Goal

Map every field end to end across three layers — the **provider payload** (their request/response shape) ↔ **our data model** (the entity fields from the ERD) ↔ the **UI** (what the user sees/edits) — with the source-of-truth owner per field (ours / theirs / derived). **Single output**: `docs/{feature}/integration/api-map.md` (type `api-map`).

## Constraints

- **Step [3], skippable** (`api-integration.md`): a pure trigger/webhook integration with no data to map → tell the user it's skippable; otherwise needs `api-summary*.md` (+ the design's source-of-truth decisions).
- **Reads the ERD/DBML** — our-model column names come from `srs/{feature}-erd.md` / `dbdiagram/`; mismatched names are a finding, not silent fixes. ERD missing → soft warn.
- **Three columns, one row per field** — provider field · our model field · UI element; plus the owner + transform (if any) + direction.
- **Source-of-truth owner is mandatory** — every row declares ours / theirs / derived (+ the derivation if derived). No owner → flag (a drift field).
- **Direction per row** — `out` (we send) / `in` (we receive) / `bi` (both, e.g. an id we send and they echo back).
- **Transforms explicit** — unit conversion, date format, enum mapping, currency rounding: name the transform, don't hide it.
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/api-map <feature>                       # map all summary endpoints
/api-map <feature> --provider catmodel   # one provider (multi-partner)
```

## Approach

1. **Gate.** No summary → refuse + route `/api-doc`. Read the summary (payload shapes) + the design (source-of-truth decisions) + the ERD/DBML (our field names).
2. **Per endpoint → field rows** — request fields (out) + response fields (in); each row: provider field · our-model field · UI element · owner · direction · transform.
3. **Owner + transform interview** — only the gaps (owners the design didn't decide, transforms the ERD/types imply); one batched round.
4. **Fact-list** — every mapping + owner + transform + source.
5. **Draft** the 3-layer table per the template; flag ownerless + name-mismatch rows.
6. **scoped change preview** — field count + ownerless flags + name-mismatches + transforms.
9. **Output report** — coverage + ownerless/mismatch flags + next (`/api-checklist`).

## Gotchas

- **Name mismatches are findings, not edits** — if the provider calls it `cust_id` and we call it `customer_id`, map them; don't silently rename our field.
- **Derived fields need the formula** — "total = subtotal + tax" written as "derived" with no formula is useless; spell out the derivation.
- **Skip honestly** — a webhook-only integration with no payload to persist has no map; say so and move to `/api-checklist`.
- **Enums map, not rename** — their `status: 'A'|'I'` → our `active|inactive` is a transform row, not a data-model change.

## Executable contract-to-UI mapping check

The portable BA kit now implements \`extensions/angent-ba/scripts/audit_api_field_mapping.py\`. It takes a **real inspected OpenAPI 3.1 JSON source contract** and an explicit field mapping; it transforms a supplied sample response into a nested UI view model and checks that the output matches its reviewed fixture. A field cannot pass merely because its name looks similar to a UI label.

    python extensions/angent-ba/scripts/audit_api_field_mapping.py extensions/angent-ba/examples/synthetic-fleet-api-map.json --openapi extensions/angent-ba/examples/synthetic-fleet-openapi.json --evidence-graph extensions/angent-ba/examples/rental-fleet-traceability.json

Implemented transforms are deliberately bounded to \`copy\` and exact \`enum\` mapping; missing source/target fields, incompatible type, unmapped enum, unsafe destination names and mismatched UI examples fail. The result contains the tested field inventory, explicit requirement-ID matching and \`live_api_calls=0\`. It **does not** execute provider requests, inject code into the frontend or guarantee that a live component consumes the same view model.

After this check, select \`ba-api-test\` for actual authorized sandbox request/response assertions, and \`ba-prototype-html\` or Frontend/Engineer for binding real application state. Preserve distinct evidence for each step.
