---
name: ak-vibe
description: Run a complete engineering delivery pipeline from request intake through planning, implementation, verification, review and the authorized repository endpoint.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Vibe — Portable Fallback

Use when the user wants a substantial feature/bug request carried end to end.

Read `references/pipeline-state.md`.

## Pipeline

1. Contract / Context / Scout.
2. Research or Brainstorm only where uncertainty requires it.
3. Plan.
4. Worktree/isolation when useful.
5. Cook or Fix.
6. Test.
7. Code Review.
8. Ship to the authorized repository endpoint.
9. Review PR / required CI convergence when that endpoint includes a PR or merge.
10. Maintain Continuity throughout.

## Rules

- skip unnecessary stages rather than following ritual;
- do not stop at progress reports while a safe authorized next step remains;
- do not merge, release or deploy without authority;
- failed checks return to the owning stage and then resume the pipeline;
- new evidence that invalidates architecture/plan returns to Reasoning;
- use native AgentKit pipeline when usable, fallback Skills otherwise.

The endpoint is defined by the task—not by the word “vibe”.
