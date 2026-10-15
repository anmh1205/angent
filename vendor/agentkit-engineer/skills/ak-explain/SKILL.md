---
name: ak-explain
description: Build a grounded explanation or mental model of a concept, code path, system, failure, or decision in Markdown by default, with optional simplified wording or self-contained HTML when supported.
metadata: {port: angent-fallback, mode: portable}
---

# Explain — Portable Fallback

Use when the desired outcome is **understanding** rather than implementation.

## Establish the subject model

Gather only the evidence needed for the requested explanation:
- current project/source facts when the question is repository-specific;
- authoritative external evidence when platform/version facts matter;
- the objects, states, relations, mechanisms, and boundaries that make the topic understandable.

Keep observed/established facts distinct from inference.

## Compose

1. Identify what the reader needs to be able to explain, trace, predict, or diagnose afterward.
2. Choose one dominant explanatory spine.
3. Introduce prerequisites when they become necessary.
4. Use code, trace, table, or diagram only when it makes a load-bearing relation easier to inspect.
5. Interpret every representation instead of dropping it into the answer.
6. Preserve uncertainty and version/platform boundaries.

Default to Markdown.

If the user requests simplified/ELI5 wording, simplify vocabulary and analogy without removing material warnings or changing the technical claim.

If the user requests HTML, compose a self-contained local visual explanation. Reuse `ak-frontend-design` for layout/visual system and `ak-diagram` for load-bearing visual relations when those Skills/capabilities are actually available; otherwise use semantic HTML/CSS/SVG directly. Report the written artifact path and which route was used.

If file-writing or required render capability is unavailable, return the grounded explanation in Markdown and state the exact missing capability instead of claiming HTML completion.

## Boundary

Do not silently implement the system being explained.

Use `ak-diagram` when the desired artifact is primarily an interactive/editorial system map rather than an explanation with optional visuals.
