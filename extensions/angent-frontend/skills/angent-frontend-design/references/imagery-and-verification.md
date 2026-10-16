# Frontend imagery and verification

## Choose visual assets by their actual job

- For product identity, prefer verified product photography, existing brand assets, and accurate device or interface captures.
- For real-world context, use sourced photographs that actually depict the subject.
- For abstract concepts, prefer purposeful illustration or generated assets when requested and available.
- For dense operational interfaces, omit decorative hero imagery when it reduces room for important content.

Never invent image URLs. Verify external asset identity, access and reuse constraints. A text prompt is not a rendered image. Avoid exposing private product data to external generation services without authorization. Provide useful alt text for meaningful images and omit redundant descriptive alt for decoration.

## Levels of frontend verification

1. A visual direction or mockup establishes the proposal, not working code.
2. Compiling project code establishes source-level behavior only.
3. Real browser rendering establishes appearance at the viewports inspected.
4. Exercised interactions establish the specific navigation, states, forms, focus, keyboard, touch and motion paths observed.
5. Measured user-task improvement requires separate contextual evidence when that outcome is claimed.

A static hero preview cannot certify all app screens.

## Inspect one decisive workflow thoroughly

Check typography hierarchy, realistic content length and localization; responsive boundaries and safe areas; loading, empty, error and recovery states; contrast against visual treatments; visible keyboard focus; interactive hit targets; reduced-motion alternatives; asset rendering and layout stability. Preserve an established design system and compare observed output against the accepted reference. Report explicitly when browser inspection is unavailable.
