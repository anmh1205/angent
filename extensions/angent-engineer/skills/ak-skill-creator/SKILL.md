---
name: ak-skill-creator
description: Create, update, audit or optimize portable agent Skills with precise discovery, progressive disclosure, safety/portability boundaries and behavioral validation.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Skill Creator — Portable Fallback

Use for reusable, versioned agent capabilities—not one-off prompts, one personal preference, or ordinary project documentation.

## Load progressively

- `references/skill-design.md` — outcome/owner/boundary/resource design.
- `references/discovery-metadata.md` — activation precision.
- `references/progressive-disclosure.md` — split SKILL/references/scripts/assets.
- `references/validation-calibration.md` — structural + behavioral evaluation.
- `references/portability-and-safety.md` — runtime capability, third-party content, secrets and distribution boundaries.

## Operations

- **create** — scaffold/write a new Skill.
- **update** — make a bounded in-place change while preserving accepted behavior.
- **audit** — inspect inventory, discovery, dated prompt patterns, portability/safety and behavioral gaps; do not modify Skill files.
- **optimize** — propose improvements; write only when apply authority is explicit.

For long-horizon Skills, keep observations, experiments, evals, benchmarks, decisions and gates in a durable project/repository rather than one giant SKILL.md.

New Skills default to project scope unless the user explicitly requests another scope.

## Workflow

1. Capture intended outcomes, realistic trigger examples, expected outputs, non-goals and security boundaries.
2. Decide whether a Skill is the right abstraction instead of AGENTS.md, docs, a plugin, or ordinary model knowledge.
3. Inspect existing Skills/capabilities to avoid duplicate ownership.
4. Research external standards/tools only when needed for the capability.
5. Design core workflow, decision gates, degraded paths and bundled resources.
6. Confirm the output directory before scaffolding/writes.
7. Write metadata from user intent/capability; make discovery specific enough to trigger correctly without hijacking nearby tasks.
8. Keep load-bearing workflow/owner/gates in SKILL.md; move situational depth into references.
9. Use scripts only for deterministic/repeatable mechanics that benefit from code.
10. Validate structure/resource links and run prompt-cruft/static checks that actually apply.
11. Evaluate representative behavior against a no-Skill or accepted baseline and include counter-cases.
12. Iterate from human/Quality feedback without overfitting to literal prompts.
13. Package/distribute only after claimed runtime portability and security boundaries are reviewed.

## Write semantics, not benchmarks

Do not stuff terms, examples or rigid steps into the Skill merely to satisfy a benchmark.

A benchmark/linter is evidence about a dimension, not the capability definition.

If a Skill is shorter than upstream/reference material but preserves the useful workflow and boundaries, brevity is not a defect. If it omits load-bearing domain knowledge or gates, brevity is not a defense.

## Completion by operation

- **create/update** — valid Skill artifacts, no broken resource links, relevant High safety/prompt issues resolved, representative consumer evaluation not blocked/ungraded.
- **audit** — evidence-backed findings + proposed repair direction; no mutation.
- **optimize without apply** — proposed diff only.
- **optimize with apply** — bounded rewrite plus revalidation/regression evidence.

Do not optimize for line count or number of supporting files.
