---
name: ba-api-design
description: Business analysis api-design specialist.
---

# ANGENT BA: api-design

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-design/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /api-design — Integration Blueprint (API chain [2])

## Goal

Design how our system orchestrates the integration — the call sequence, where state lives (source-of-truth per field), how webhooks are received + reconciled, the retry policy, and the degraded UX when the provider is down. **Single output**: `docs/{feature}/integration/api-design.md` (type `api-design`). `/api-map` is a part underneath this (field-level detail), and the checklist converges under the design.

## Constraints

- **Step [2]** (`api-integration.md`): reads `api-summary*.md` (their contract). Summary missing → refuse + route `/api-doc` (can't orchestrate a contract you haven't digested).
- **Six mandatory concerns** — orchestration (the call sequence + who triggers each), state-map (which entities hold integration state + their fields), source-of-truth (per synced field: ours / theirs / derived), webhook handling (receive → verify → idempotent apply → reconcile), retry + reconciliation (the polling fallback for a missed webhook), degraded-UX (what the user sees when the provider is down).
- **No fabrication** — every decision cites the summary or the SRS; an invented endpoint or a guessed retry policy is BLOCKING.
- **Source-of-truth is explicit** — every synced field declares its owner; a field with no owner is a drift bug (flag it).
- **Webhook ⇄ reconciliation pair** — every webhook has a reconciliation path; a webhook with no fallback is a silent data-loss path.
- **Reads the SRS** — the FRs/NFRs (latency, availability) constrain the design (retry budget, sync vs async).
- **Validate before done** — doc-validate (step 9).

## Inputs

```
/api-design <feature>          # reads api-summary*.md + srs/{feature}-spec.md
```

## Approach

1. **Gate.** No `api-summary*.md` → refuse + route `/api-doc`. Read the summary (endpoints/auth/webhooks/limits) + the SRS (FRs/NFRs that constrain the integration).
2. **Interview gaps** (one batched round): the call trigger per endpoint · sync vs async · where state lives · webhook verify + idempotency key · retry policy (attempts/backoff) + reconciliation endpoint+interval · degraded-UX surfaces.
3. **Fact-list** — every design decision + its source (summary row / SRS FR / interview); the source-of-truth owner per synced field.
4. **Draft** per the template — the six concerns, each decision sourced; a state-map (which entities/fields); a retry/reconciliation table per webhook.
5. **L1 plan preview** — endpoint count orchestrated + webhook⇄reconciliation pairs + degraded-UX surfaces + any ownerless field flagged.
7. **Self-check** — every webhook has a reconciliation partner; every synced field has an owner; retry budget fits the NFR latency.
10. **Output report** — concerns covered + next (`/api-map` for field detail; `/api-checklist` for the test outline).

## Gotchas

- **Webhook without reconciliation = data loss** — the most common integration bug; the self-check exists to catch it.
- **Ownerless fields drift** — "who's right when both sides have a value?" must be answered per field at design time, not at the first conflict.
- **Retry budget vs NFR** — a 5-retry exponential backoff can blow a 2s latency NFR; check the budget against the SRS.
- **Don't restate the summary** — the design adds orchestration decisions, not a second copy of their endpoints.
