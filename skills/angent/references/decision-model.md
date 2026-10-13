# Decision model — choose through consequences, not feature counts

Use a decision model when multiple viable actions or architectures remain.

## Decision state

- **goal** — outcome being optimized;
- **hard constraints** — eliminate invalid options;
- **soft preferences** — dimensions that may trade off;
- **candidate options** — materially distinct alternatives;
- **consequences** — expected effects under relevant scenarios;
- **uncertainty** — unknowns that could reverse ranking;
- **reversibility** — cost of changing course;
- **cost of error** — impact if the choice is wrong;
- **decision** — selected option and why;
- **reconsideration trigger** — new evidence/state that should reopen it.

## Shared axes, not generic pros/cons

Compare alternatives on dimensions derived from the actual objective and constraints. A feature list is useful only when each feature changes the decision.

## Dominance and elimination

Eliminate options that violate hard constraints before fine-grained scoring. If one option is no worse on all material dimensions and better on at least one, say so rather than inventing artificial balance.

## Uncertainty-aware choices

When evidence is incomplete, prefer:
- reversible steps;
- experiments that reduce decisive uncertainty;
- architecture that preserves future options when switching costs are high.

Do not pretend uncertain estimates are precise numbers unless there is a real measurement model.

## Decision trace

The user usually needs the conclusion and decisive trade-offs, not private deliberation. Expose a concise decision trace when it improves trust or enables the user to challenge assumptions.
