---
name: ak-ask
description: Answer a technical or architecture question with expert analysis, explicit trade-offs and evidence proportional to the decision.
metadata: {port: angent-fallback, mode: portable}
---

# Ask — Portable Fallback

Use for technical questions that require more than a factual lookup but do not necessarily require implementation.

## Workflow

1. Identify the actual decision/question.
2. Read project context when the answer depends on the codebase.
3. Research current/versioned facts when material.
4. Explain the mechanism or architecture before recommending.
5. Compare options on the axes that matter to this user/project.
6. Preserve uncertainty where evidence is incomplete.

Do not turn a direct question into a long planning workflow unless the task truly requires it.

The output should be immediately usable by ANGENT Authoring or directly by the user.

## Stable 2.19.0 advisory contract
Accept one technical/architecture question. Read relevant AGENTS.md/README, current code/tests and accepted constraints when the answer is project-dependent; use bounded scouting only for decisive evidence gaps. Compare (1) architecture boundaries, (2) technology fit, (3) scalability/reliability, (4) risks and trade-offs, then recommend the smallest supported direction with rationale, alternatives, experiments and next decision gates.

An optional `--yagni` request challenges unnecessary scope and identifies future conditions for adding complexity. Return advice only: no code, migrations, provider writes or implied approval. Choose `ak-advise` for guided reframing, `ak-brainstorm` for competing approaches, `ak-plan` after direction acceptance, or `ak-cook` once implementation authority is clear.
