---
name: ak-sequential-thinking
description: Apply adaptive multi-step internal reasoning with revision, branching, hypothesis testing, uncertainty handling and mechanical constraint verification for complex problems.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Sequential Thinking — Portable Fallback

Use when a problem genuinely benefits from multi-step decomposition, revision or competing hypotheses.

Do not invoke for ordinary low-risk questions.

## Load progressively

- `references/thinking-patterns.md` — revision, branching, hypothesis and stall recovery.
- `references/constraint-verification.md` — exact mechanical constraints.

## Internal method

1. Establish objective, hard constraints and currently known/unknown state.
2. Start with a provisional decomposition rather than a fixed step count.
3. Carry earlier evidence/assumptions forward explicitly in the internal model.
4. Expand or contract the plan as complexity becomes clearer.
5. Revise an earlier premise when new evidence invalidates it, then re-evaluate downstream conclusions that depended on it.
6. Branch only when alternatives/hypotheses materially change the decision; converge after discriminating them.
7. Under uncertainty, seek a robust action or the minimum information needed to distinguish cases.
8. Detect circular/no-progress reasoning and change strategy or obtain missing evidence.
9. Mechanically verify exact output constraints when possible.
10. Return the conclusion, decisive evidence, relevant alternatives/boundaries and residual uncertainty.

## Privacy boundary

The upstream package supports visible numbered thought transcripts. The portable ANGENT fallback **does not expose private chain-of-thought**.

When the user needs inspectable reasoning, provide an externalizable decision basis, assumptions, evidence, calculations, alternatives, tests and concise rationale rather than a hidden internal transcript.

Optional upstream thought-history scripts are not required for semantic parity because their role can be preserved by the active Reasoning/Continuity model without storing private reasoning.

## Completion

Do not declare success merely because the provisional sequence ended.

Completion requires the requested conclusion/action to be supported and material constraints/uncertainty to be resolved or surfaced.
