---
name: ak-fable-thinking
description: Apply an evidence-first high-rigor reasoning protocol for deceptive, constrained or high-consequence problems without exposing private chain-of-thought.
metadata: {port: angent-fallback, mode: adapted}
---

# High-Rigor Thinking — Portable Fallback

This Skill preserves useful reasoning discipline from the upstream workflow. It does **not** claim to clone a proprietary model or expose hidden reasoning.

## Load progressively

- `references/floor-and-constraints.md` — cheap trap detection and mechanical output verification.
- `references/claim-discipline.md` — separate observation, prior knowledge, assumption and inference.
- `references/reasoning-moves.md` — frame, ground, reason, attack and deliver.

## Proportionality

Apply enough rigor for the consequence:

- **direct** — simple/reversible/familiar task after a quick floor check;
- **standard** — normal debugging/review/analysis/decision work;
- **full** — high-consequence, irreversible, contested, security/data/money or unfamiliar work.

A mechanically constrained output is never “direct” if success can be checked exactly.

## Core behavior

- derive the real requested end-state instead of copying the user's proposed mechanism;
- verify load-bearing facts with stronger evidence when cheap;
- preserve credible competing hypotheses only when they change the next observation;
- simulate concrete representative/edge inputs;
- search for evidence that would kill the preferred conclusion;
- match confidence and wording to evidence;
- mechanically verify strict surface constraints.

## Output

Expose the useful conclusion, evidence, model, trade-offs and uncertainty.

Do not emit a private step-by-step chain-of-thought transcript.

Do not over-apply this Skill to trivial requests.
