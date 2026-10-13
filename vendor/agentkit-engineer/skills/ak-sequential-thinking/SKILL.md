---
name: ak-sequential-thinking
description: Apply structured multi-step internal analysis with revision and mechanical constraint verification for complex or deceptive problems.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Sequential Thinking — Portable Fallback

Read `references/constraint-verification.md`.

## Internal workflow

1. Restate objective and hard constraints.
2. Decompose only dependencies needed for the conclusion.
3. Check material intermediate assumptions.
4. Revise earlier reasoning when contradiction appears.
5. Simulate representative/edge cases.
6. Mechanically verify exact output constraints.
7. Return the conclusion, decisive evidence and uncertainty.

Do not expose private chain-of-thought as a numbered transcript.

Do not invoke for ordinary low-risk questions.
