---
name: ba-api-map
description: Business analysis api-map specialist.
---

# ANGENT BA: api-map

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-map/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


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
- **Validate before done** — doc-validate (step 8).

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
6. **L1 plan preview** — field count + ownerless flags + name-mismatches + transforms.
9. **Output report** — coverage + ownerless/mismatch flags + next (`/api-checklist`).

## Gotchas

- **Name mismatches are findings, not edits** — if the provider calls it `cust_id` and we call it `customer_id`, map them; don't silently rename our field.
- **Derived fields need the formula** — "total = subtotal + tax" written as "derived" with no formula is useless; spell out the derivation.
- **Skip honestly** — a webhook-only integration with no payload to persist has no map; say so and move to `/api-checklist`.
- **Enums map, not rename** — their `status: 'A'|'I'` → our `active|inactive` is a transform row, not a data-model change.
