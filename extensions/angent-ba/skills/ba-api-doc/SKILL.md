---
name: ba-api-doc
description: Business analysis api-doc specialist.
---

# ANGENT BA: api-doc

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-doc/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /api-doc — Digest the 3rd-party contract (API chain [1])

## Goal

Read the provider's OpenAPI/spec/docs and write an internal summary of what THEY actually offer — endpoints, auth model, webhooks, rate limits, error responses — each with provenance (which spec page / version). **Single output**: `docs/{feature}/integration/api-summary.md`, or `api-summary-{provider}.md` for multi-partner (`api-integration.md` provider-suffix rule). Consumed by `/api-design`.

## Constraints

- **Step [1], never skip** (`api-integration.md`): the design can't be sound without the real contract. **Refuses to fabricate** — no source provided → ask for it; never invent an endpoint, an auth flow, or a rate limit.
- **Group A-variant\*** (`feature-bootstrap.md`): source-driven like `/reverse-doc` — needs the provider docs (a URL, an OpenAPI file, a PDF); refuses to invent a contract from a description alone.
- **Provenance on every row** — endpoint / auth / webhook / limit cites the spec page or version it came from; a row with no provenance is a guess.
- **Unknowns → OQ** — the spec doesn't say X → OQ, never a confident entry. (Same discipline as `/reverse-doc`'s confidence markers.)
- **Multi-provider** — one summary file per provider; the design + map stay single.
- **Validate before done** — doc-validate (step 8).

## Inputs

```
/api-doc <feature> --provider catmodel ./legacy/cat-model-openapi.yaml
/api-doc <feature> https://provider.example.com/docs/openapi.json
/api-doc <feature> ./provider-api-guide.pdf
```

## Approach

1. **Read the source** — OpenAPI (parse endpoints/schemas/auth), a docs URL (fetch + extract), or a PDF (extract). Note the spec version + date.
2. **Extract** — endpoints (method/path/purpose), auth model, webhooks (if any), rate limits, pagination, error response shape.
3. **Provenance + gaps** — every entry cites its source; anything absent from the spec → OQ (e.g. "rate limit not documented → OQ: ask provider").
4. **Draft** the summary per the template — sections per concern, each row provenance-tagged, an OQ section for the gaps.
5. **L1 plan preview** — endpoint count + auth model + webhook presence + provenance coverage + gap count.
7. **If a section can't be sourced** → OQ, never a guess; HARD STOP only if the whole contract is missing.
9. **Output report** — coverage + gaps + next (`/api-design`).

## Gotchas

- **The source is the truth** — if your summary and the spec disagree, the spec wins; fix the summary.
- **Undocumented ≠ absent** — a rate limit the spec doesn't state is an OQ to confirm with the provider, not an assumption of "unlimited".
- **Version matters** — record the spec version; a v2→v3 bump can break the design silently.
- **Don't design here** — orchestration/retry/degraded-UX belong to `/api-design`; this skill is the faithful digest.
