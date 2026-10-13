---
name: ak-fix
description: Route a known software failure to the correct diagnostic and implementation path, then verify the original failure and regression surface.
metadata: {port: angent-fallback, mode: adapted}
---

# Fix — Portable Fallback

## Load progressively

- `references/failure-routing.md` — choose direct fix, Debug, Scout or broader Reasoning.
- `references/repair-verification.md` — verify the original path and blast radius.

## Workflow

1. Capture the failure and current evidence.
2. Decide whether root cause is already established.
3. Scout ownership/flow when needed.
4. Debug when competing causes remain.
5. Apply the smallest correction at the earliest correct owner.
6. Add/update regression evidence.
7. Run targeted verification then widen by blast radius.
8. Use Code Review for material changes.

Do not hide unknown cause behind retries/suppression.

Repeated failed fixes are a signal to revisit the model, not to keep changing code blindly.
