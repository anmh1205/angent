---
name: ak-research
description: Conduct decision-focused technical research with current authoritative evidence, explicit source/support boundaries, conflict reconciliation and actionable implications.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Research — Portable Fallback

Use when a technical decision depends on facts outside the current project, current best practice, versioned platform behavior, or evidence comparing materially different approaches.

Use Scout instead for repository-local discovery. Use Docs Seeker for one library/API documentation question. Use Research Prompt when the deliverable is only a self-contained research assignment.

## Research contract

Before retrieval, establish:
- decision/question;
- alternatives when known;
- constraints and non-goals;
- recency/version/platform/geography/deployment boundary;
- evaluation criteria;
- evidence strong enough to change the decision;
- confidential/private context that must not be emitted into external queries;
- artifact/report path when the user/task requires a durable report.

Do not force a report artifact when the user asked only for an in-chat answer.

## Bounded search

Keep retrieval bounded and information-seeking rather than exhaustive.

The pinned upstream workflow uses a maximum of five research/search calls and respects a lower user limit. In a harness where one logical research step requires several open/click/read operations, preserve the **bounded-budget intent** rather than counting mechanics blindly.

Spend the budget on questions that can distinguish alternatives, establish versions, expose conflicts, or change the recommendation.

## Evidence strategy

1. Prefer normative, primary implementation and vendor sources for claims they can establish.
2. Use canonical provider/runtime/project observations for the user's actual deployed state.
3. Use independent analysis/community evidence for operational experience and disputed areas.
4. Preserve source lineage; repeated copies of one upstream claim are not independent corroboration.
5. Separate direct support from ANGENT inference.
6. Reconcile conflicts by version, platform, configuration, scope and freshness instead of averaging them.

For security, compatibility, deprecation, performance, or availability claims, check current authoritative evidence and state the relevant boundary.

## Synthesis

Build the smallest useful subject model:
- relevant objects/states;
- mechanisms and dependencies;
- alternatives/trade-offs;
- decisive evidence;
- conflicts/unknowns;
- implications for the current decision.

Do not produce a source dump whose relationships are left for the next agent to reconstruct.

## Stop

Stop when remaining uncertainty cannot change the current decision at the required consequence level, or the research budget is exhausted.

If a decisive conflict remains unresolved, return that uncertainty rather than manufacturing consensus.

## Output

Return:
- established findings with citations/provenance;
- source roles and version boundaries;
- alternative consequences/trade-offs;
- recommendation implications;
- residual uncertainty;
- actionable next steps.

For durable-report mode, save to the authorized path and keep unresolved questions visible at the end.

Do not confuse source volume with research quality.
