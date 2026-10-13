---
name: ak-skill-creator
description: Create or update portable agent Skills with accurate discovery metadata, progressive disclosure, deterministic helpers and behavioral validation.
metadata: {port: angent-fallback, mode: adapted}
---

# Skill Creator — Portable Fallback

Use for reusable capabilities, not one-off task instructions.

## Load progressively

- `references/skill-design.md` — overall capability design.
- `references/discovery-metadata.md` — make activation precise.
- `references/progressive-disclosure.md` — split SKILL/references/scripts/assets.
- `references/validation-calibration.md` — prove the Skill improves behavior.

## Workflow

1. Define the outcome/failure mode the Skill solves.
2. Decide whether a Skill is actually needed instead of AGENTS.md/project docs.
3. Write metadata from user intent/capability.
4. Put operating model, owner boundary, workflow and major decision points in SKILL.md.
5. Move situational depth into references.
6. Add scripts only for deterministic computation/file operations.
7. Add fallback/degraded behavior for unavailable capabilities.
8. Test discovery and representative behavior.
9. Remove redundant instructions that the model already performs reliably.

Do not optimize for line count or number of supporting files.
