---
name: ak-research
description: Conduct decision-focused technical research with authoritative sources, version boundaries, conflict reconciliation and clear architectural consequences.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Research — Portable Fallback

Use when a technical decision depends on facts outside the current project or when multiple implementation approaches require evidence.

## Workflow

1. Define the decision/question and what evidence could change it.
2. Prefer normative, primary implementation and vendor sources.
3. Use runtime/project observations when they establish the user's real environment.
4. Compare alternatives through consequences, not feature counts.
5. Reconcile version/platform/config conflicts explicitly.
6. Stop when remaining uncertainty no longer changes the decision.

## Output

Return established facts, source roles, boundaries, conflicts, options/trade-offs, recommendation implications and residual uncertainty.

This Skill can delegate to the Researcher agent when context isolation or parallel source work is useful.

Do not confuse source volume with research quality.
