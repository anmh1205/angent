---
name: ba-api-assess
description: Business analysis api-assess specialist.
---

# ANGENT BA: api-assess

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-assess/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /api-assess — Build-vs-buy / provider selection (API chain [0])

## Goal

Decide whether to build or buy, and if buy, which provider — as a scorecard: candidates × weighted criteria (coverage of our need, cost, reliability/SLA, auth model, data residency, sunset risk). **Single output**: `docs/{feature}/integration/api-assess.md` (type `api-assess`), consumed by `/api-doc` (the chosen provider's contract).

## Constraints

- **Step [0], skippable** (`api-integration.md`): provider already fixed → tell the user to skip to `/api-doc`; don't fabricate a decision that was already made.
- **Group A\*** (`feature-bootstrap.md`): integration-first feature entry point; can create the feature.
- **No fabrication** — every scorecard cell needs a basis (provider docs, a quote, a known limitation); unknowns → OQ. A provider scored on a guessed SLA is the worst kind of decision record.
- **Weighted, not flat** — criteria carry weights the user confirms; a flat "X is best" with no weights isn't a defensible choice.
- **Read the need first** — from `srs/{feature}-spec.md` (what FRs demand of the integration) or the `<need>` arg; the scorecard scores against the need, not in the abstract.
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/api-assess <feature> "<need>"          # score providers against the stated need
/api-assess <feature>                   # derive the need from the SRS
```

## Approach

1. **Resolve the need** — from the SRS (FRs touching an external service) or the `<need>` arg. State it in one line.
2. **Candidate + criteria interview** (one batched round): candidate providers; the weighted criteria (coverage / cost / SLA / auth / residency / sunset); per-candidate notes with their basis.
3. **Fact-list** — every score + basis; unknowns → OQ.
4. **Score** — per candidate × criterion (the weights sum to 100%); compute the totals.
5. **Draft** the scorecard + a one-paragraph recommendation citing the winning margin + the biggest risk of the winner.
6. **scoped change preview** — candidates + the winner + the deciding criterion + open risks.
9. **Output report** — the choice + next (`/api-doc <feature> --provider <winner>`).

## Gotchas

- **Don't pick for the user** — present the scored recommendation; the choice is theirs (a cost-led choice over a coverage-led one is legitimate).
- **Sunset/deprecation is a criterion** — a provider EOL-ing in 6 months scoring high on coverage is a trap; weight it.
- **Skip honestly** — if the provider is fixed, say so and route to `/api-doc`; a faux-assessment of one candidate is theater.
