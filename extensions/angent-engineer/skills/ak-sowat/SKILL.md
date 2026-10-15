---
name: ak-sowat
description: Turn recent verified implementation evidence and related issues into a concise product-impact judgment and up to three measurable next steps.
metadata: {port: angent-fallback, mode: portable}
---

# So What — Portable Fallback

Use after implementation when the user needs to decide **what matters next**, not merely what changed.

## Inputs

Prefer current evidence:
- intended user/business outcome;
- verified implementation behavior;
- tests, runtime or shipment evidence;
- known regressions/blockers/dependencies;
- related issues or follow-up opportunities.

Historical conversation is context, not proof of current state.

## Workflow

1. Reconstruct the intended outcome.
2. Separate verified user-visible capability from internal work, polish, or unverified claims.
3. Identify the highest-impact gap, blocker, regression, or opportunity.
4. Challenge weak priorities when the evidence shows they do not move the intended outcome.
5. Recommend at most three next actions, each tied to an observable result.

## Output

Keep the result short:
- product/user meaning of the work;
- strongest risk or missed opportunity;
- up to three prioritized measurable next steps.

Do not mutate code, issues, roadmaps, or provider state. Route accepted actions to the appropriate implementation/project workflow.

Use `ak-sumup` for a factual implementation recap and `ak-watzup` for live project/worktree status.
