# Progressive disclosure

Use layers:

## SKILL.md

Always-loaded after activation:
- operating model;
- boundaries;
- core workflow;
- major branches/gates;
- reference routing.

## references/

Load only for a specific deep branch.

Each reference should answer a real operational question, not merely move text out of SKILL.md.

## scripts/

Use when deterministic code is safer/cheaper than language reasoning:
- validation;
- parsing;
- conversion;
- repository inspection;
- repeatable checks.

## assets/templates

Use for reusable non-instruction material.

Do not split a 30-line Skill into ten tiny files for appearance.
