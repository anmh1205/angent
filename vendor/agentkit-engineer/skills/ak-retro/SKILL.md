---
name: ak-retro
description: Generate an evidence-backed engineering retrospective from Git history, plans, incidents and delivery outcomes without reducing productivity to commit counts.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Retro — Portable Fallback

Use for sprint/project/quarterly engineering reflection.

## Evidence

Possible inputs:
- Git history and PRs;
- issue/task completion;
- Continuity/journal incidents;
- tests/build/release outcomes;
- review findings;
- major architecture decisions.

## Analyze

Separate:
- delivered outcomes;
- recurring blockers/rework;
- quality/regression patterns;
- process/tool friction;
- useful practices;
- unresolved technical debt.

Commit count and LOC are context, not performance judgments.

## Output

Return what changed, what worked, what repeatedly failed, causal hypotheses, actions worth trying and metrics/evidence for the next retrospective.

Learning may later promote a mechanism; Retro itself does not turn every observation into a global rule.
