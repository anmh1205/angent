---
name: ak-coding-level
description: Calibrate code explanation, abstraction and examples to the user's demonstrated technical level without storing a brittle global level setting.
metadata: {port: angent-fallback, mode: adapted}
---

# Coding Level — Portable Fallback

Infer the minimum useful explanation depth from the current user/task and explicit preferences.

Possible calibration dimensions:
- terminology assumed;
- amount of prerequisite explanation;
- code completeness;
- abstraction level;
- discussion of trade-offs;
- debugging guidance;
- production-hardening depth.

Prefer observed competence in the current domain over one global “beginner/intermediate/expert” label.

When the user explicitly sets a preferred level, Context/Memory may preserve that preference with scope/provenance.

Do not persist it into AGENTS.md unless it is intentionally a project-level writing instruction.
