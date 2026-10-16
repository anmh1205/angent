# Visual direction mechanisms

Source inspiration: [ClaudeKit Frontend Design Pro Demo, v02](https://github.com/claudekit/frontend-design-pro-demo/tree/main/demos-v02). This is an ANGENT analytical guide based on studied examples, **not copied master prompts or a style prescription**.

These eleven aesthetic families show how typography, spatial composition, material surface and interaction can reinforce one another. The design objective is a believable product interface, not maximal novelty.

| Direction | Distinct mechanism | Good fit or important caution |
| --- | --- | --- |
| Swiss / editorial minimal | Grid discipline, asymmetrical editorial proportion, typographic contrast, calm negative space | Strong for information-led brand sites; keep scanning/navigation obvious |
| Neumorphic / soft extrusion | Highlight/shadow pairs create apparent depth on uniform backgrounds | Restrict to noncritical surfaces; subtle controls may fail affordance/contrast |
| Glass / translucent layering | Backdrop blur, layered elevation and contrasting background fields | Check over-text contrast, GPU costs and low-power/mobile devices |
| Brutalist graphic | Expressive contrast, hard edges, oversized type and intentional tension | Match brand and content; preserve keyboard states and reading order |
| Clay / soft 3D | Soft rounded inflated shapes, layered shading and playful tactile cues | Better for friendly storytelling than dense professional admin tables |
| Aurora / gradient field | Slow color movement and bright-dim layering create atmospheric depth | Do not make decorative motion or saturated fields obscure content |
| Retro-futuristic | Display typography, coded-grid/CRT cues, vivid color and spatial chrome | Restrict special effects so data legibility and accessibility remain intact |
| 3D material realism | Shading, material gradients, perspective and lighting suggest physicality | Expensive assets/animations need fallback and a product reason |
| Maximalist color block | Deliberate large color regions, bold visual contrast, assertive grouping | Avoid gratuitous noise for complex forms, analytics and instructions |
| Dark OLED | Deep surface hierarchy, restrained glow, nuanced text contrast | Black surfaces alone are not hierarchy; avoid washed-out secondary text |
| Organic / biomorphic | Curved geometry, natural palettes, uneven rhythms and gentle motion | Support calm human-centered brands; avoid interfering with dense content |

## Choose by mechanism, not label

- **What is the reader/user trying to do?** A data-dense operations dashboard typically needs hierarchy and quick comparison before expressive effects.
- **Which constraints are already accepted?** Reuse typography, spacing tokens, product identity, component kit and previous successful screens when they are binding.
- **What creates distinctiveness?** A coherent typography system, editorial composition, restrained color tension or meaningful illustration can be enough.
- **Where is it likely to fail?** Compare one realistic mobile viewport, long/localized text, no-content state, focus order, reduced motion and a real primary workflow before accepting the direction.

The reference demos use CSS custom properties, fluid units, grid/flex composition, motion and responsive breakpoints. Their code is illustrative rather than a universal production guarantee. A style catalogue should not override an actual accessibility audit or performance trace.
