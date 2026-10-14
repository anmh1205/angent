---
name: angent-format
description: Translate accepted content into destination representation requirements and verify the final visible result without bypassing Execution for external effects.
---

# ANGENT Format — Destination Fidelity

Format owns destination representation and visible-render verification. It does not own solution logic, prose authorship, or external-effect authority.

## Reference

- references/render-fidelity.md

## Before write

Receive accepted content from Authoring/Quality plus:

- representation intent;
- hierarchy/block requirements;
- citation/link requirements;
- destination constraints.

Produce the destination representation needed to preserve meaning.

If the destination cannot express the content without changing meaning, return to Authoring instead of silently simplifying.

When applying the representation requires an external write, Execution performs the authorized effect.

## Preserve semantics

Do not flatten causal/dependency structure for scanability, change code/equation meaning, replace authentic evidence with a generic visual, or restructure a comparison/procedure into a weaker form.

## After write

Inspect/read back the actual destination when possible.

Verify:

- heading/page/block hierarchy;
- tables and ordered procedures;
- code/equations, including language tags matched to the actual language (e.g. CMake is not JavaScript), literal symbols, intended line breaks and execution semantics;
- rendered diagrams, including actual arrow/label relationships rather than only block presence;
- image/diagram compatibility with the target renderer and its supported syntax version; figure clarity at the actual display size;
- figures/captions;
- citations/links, including whether source markers became real readable references rather than unrendered internal tokens;
- missing/duplicated blocks;
- destination artifacts or overflow.

A successful write proves transport, not visible fidelity. For structured pages (including Notion), inspect the actual published heading nesting, readable code/diagram blocks, ordered lists and links. If the destination only displays a Mermaid source fence rather than a figure, report that explicitly rather than claiming a rendered diagram. Never repair absent technical depth by manipulating blocks: return the problem to Authoring.

Return representation/render defects to Format. Return content/meaning defects to Authoring. Return provider/effect ambiguity to Execution.
