# UI styling mutation and visual gates

## Mutation boundary

Before a generator/package command, know whether it may touch:
- package manifest/lockfile;
- component files;
- global CSS;
- Tailwind/build config;
- aliases/imports;
- generated assets.

Use dry-run/validate-only routes when supported and the effect needs review.

Existing customized files are protected state, not disposable generator output.

## State verification

Inspect representative:
- normal;
- hover/focus/active;
- disabled;
- loading;
- error;
- long/overflow content;
- light/dark;
- mobile/desktop;
- reduced motion.

Only test states relevant to the component/flow.

## Accessibility

Check semantics, keyboard order/focus visibility, labels/errors, contrast, color-only meaning, zoom/reflow and touch target where applicable.

Automated checks are supporting evidence; inspect critical interactions manually/browser-wise when possible.

## Render evidence

Capture screenshot/browser state only when it proves the relevant property.

Source/CSS correctness does not prove the final browser rendering.
