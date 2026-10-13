# Render fidelity

Formatting is correct only when the visible destination preserves intended meaning.

## Semantic checks

Verify that:
- heading hierarchy matches conceptual hierarchy;
- ordered procedures remain ordered;
- table axes remain aligned;
- diagrams preserve real relationships;
- code/equations are not corrupted;
- citations/links point to the intended evidence;
- captions/references remain attached to the right object.

## Destination checks

Inspect where possible:
- actual rendered blocks/pages/slides;
- pagination/overflow;
- missing assets;
- unsupported syntax fallbacks;
- duplicate content;
- raw transport tokens.

## Failure ownership

If the destination cannot express a representation without changing meaning, return to Authoring for an alternative representation.

Do not silently simplify away information.

A successful write API call proves transport, not visible correctness.
