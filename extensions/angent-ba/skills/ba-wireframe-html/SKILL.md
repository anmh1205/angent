---
name: ba-wireframe-html
description: Produce auditable static HTML wireframes from accepted userflow and screen-control specifications, and verify the rendered result.
---

# BA static HTML wireframe — implemented method

**Provenance.** Adapted from the MIT Dev BA Kit wireframe-html method (Edward Ngo, 2026). Source: https://github.com/nv-minh/dev-ba-kit/blob/main/skills/wireframe-html/SKILL.md. The ANGENT renderer is independently written, not the original Claude plugin's iframe-based navigator.

## Scope and authority

Produce one standalone, static, JavaScript-free HTML review page per JSON screen model. It renders every declared screen with controls and linked FR/BR requirement IDs. It deliberately disables input and cannot authenticate, persist or make API calls. ANGENT Root and Execution retain intent and authorization; this Skill does not own new host tools.

1. Read actual accepted SRS/userflow, available wireframe-ascii, error matrix and naming conventions. Pin the source revision and identify all screen IDs, controls, their labels, action targets, failure paths and source FR/BR/AC references.
2. Convert the agreed model into the portable JSON structure described in references/screen-model.md. **No arbitrary ASCII-to-JSON conversion is currently implemented**: verify this transcription manually against original evidence. Do not invent CAPTCHA, login thresholds, error wording or device widths.
3. The structural checker refuses duplicate screen/control IDs, missing labels, unsupported controls, unreachable screens, dangling navigation and missing mock outcome scenarios. It cannot discover an omitted business scenario if absent from the source JSON.
4. With actual filesystem access, generate static HTML from the accepted JSON:

    python extensions/angent-ba/scripts/build_wireframe.py INPUT.json --mode wireframe --output output/wireframe.html

5. Confirm command exit status and open the saved file. Inspect narrow/wide viewports, disabled control labels, screen order, title, source requirements, wrapping, keyboard behavior and actual visible completeness.
6. Record source revision and file path, the controls and states actually observed, and any unverified policy. Avoid overwriting a previous approved wireframe without a scoped diff.

## Limits and realistic example

The repository ships a synthetic three-screen Authentication model at extensions/angent-ba/examples/authentication-screen-model.json. Static output lists the screens and requirement references but does **not** include the original Dev BA Kit's per-flow iframe index, fixed device-width frames, automatic deep-link numbering, or a full ASCII wireframe converter. Do not claim those features exist.

For interactive mock navigation using the same accepted source, select ba-prototype-html. Figma editing, visual design and real backend implementation belong to their respective authorized specialists.
