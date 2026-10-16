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

## Concrete mapping and quality controls

- **Model entrypoint:** \`start\` identifies an existing screen ID and every secondary screen must be reachable by an explicit navigation or submit outcome.
- **Review scope:** enumerate actor, use case, FR/BR/AC source, screen states and user-visible effect before transcribing any controls into JSON.
- **Input controls:** preserve \`id\`, \`type\`, \`label\`, \`required\`, supported placeholder and source \`requirements\`; labels must describe the actual value being requested.
- **Checkbox state:** a checkbox models a true/false input, not a text field; the current renderer does not infer consent policy or acceptance from its mere presence.
- **Display-only copy:** render \`note\` as semantic noninteractive text, not as a simulated API result or an accessible action.
- **Plain navigation:** \`button.action\` has \`type: navigate\` and a real target ID; the model checker must reject dangling targets.
- **Submission:** each \`submit.outcomes\` has every declared scenario key, with either \`navigate\` to an existing screen or \`error\` with a nonempty message.
- **Error separation:** distinguish credential rejection, user authorization denial and transport failure when the approved requirements differentiate them.
- **Static wireframe:** inputs and buttons are disabled to prevent misleading interaction; this mode shows screen content for review, not successful form submission.
- **Control provenance:** preserve each supplied requirement ID next to its rendered control, and validate the ID against the actual requirement source outside the renderer.
- **Coverage audit:** compare the screen inventory with accepted userflow; the structural validator detects unreachable screens but cannot detect a missing scenario never entered into JSON.
- **Security:** the HTML renderer escapes input-derived text; never inject supplied strings directly into executable script text or untrusted inline attributes.
- **Responsive inspection:** view the generated file on a narrow mobile width and a desktop width; inspect actual wrapping, horizontal overflow and clipping.
- **Accessibility inspection:** check visible labels, screen heading hierarchy, focus indication, contrast and meaning without color; automated structural checks alone do not prove WCAG compliance.
- **Export consistency:** preserve deterministic IDs and rendered order so screenshots, requirement references and review comments can target the same screen across revisions.
- **Review update:** compare new JSON with the previously approved model; inspect which screens and business rules changed rather than regenerating unrelated pages.
- **Verification evidence:** run the generator, open the resulting HTML and record a real file path or browser result; never equate a CLI zero exit code with visual correctness.
- **Boundary:** use \`ba-prototype-html\` for simulated navigation, and actual product/frontend implementation for persistent state or integration; never imply this static page is executable application logic.

