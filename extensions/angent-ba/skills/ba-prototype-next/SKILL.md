---
name: ba-prototype-next
description: Generate and test an isolated real Next.js App Router mock from approved BA screen models, preserving navigation, error states and accessible labels.
---

# BA Next.js prototype — a built and browser-verified review app

The source-aligned executable is \`extensions/angent-ba/scripts/build_next_prototype.py\`. This implements a narrow but genuine Next.js App Router application with generated page routes, native form validation, explicit mock outcomes and a visible simulation boundary. It is **not** a production login, real API integration or modification of an existing app without authorization.

## Decide what to build

Read the accepted FR/BR/error matrix, userflow and screen/control inventory and pin the revision. When working in an existing Next.js project, first inspect its app router, component system, dependencies, variants, deployment and available tests. *Do not replace an established app with the isolated example generator.* Instead adapt the underlying screen-state method to the existing stack under ANGENT Execution.

For a standalone BA review artifact, prepare the independently accepted JSON screen model documented under \`ba-wireframe-html/references/screen-model.md\`. The same model can drive static HTML and generated Playwright tests. Structural checks reject broken routes and scenario outcomes, but they cannot infer a missing customer requirement.

## Generate the actual app

From the ANGENT repository root, with authorized filesystem and Python:

    python extensions/angent-ba/scripts/build_next_prototype.py extensions/angent-ba/examples/authentication-screen-model.json --output out/next-prototype

This creates 8 source files, including package.json, model.json, review-manifest.json, a dynamic App Router screen and CSS. The output directory must be empty. The example uses a synthetic three-screen Authentication flow. Do not rewrite model values with real passwords, personal data or unstated security policy.

The generator reports \`compile_status: not-run\` and \`browser_status: not-run\` until a real runtime test is performed. Generating files alone does not prove a functional Next.js prototype.

## Compile and observe in a real browser

With Node.js 20.9+ and network/package installation authorized:

    cd out/next-prototype
    npm install --no-audit --no-fund
    npm run build
    npm run start

Check \`http://localhost:3000\`, all reachable screen IDs, native required/email validation, successful submit, every declared mock error, forgotten-password navigation, reset, keyboard focus, labels and mobile/desktop scrolling. The application disables interactive controls until React hydration attaches client handlers, preventing early clicks from appearing to work when no handler exists.

The repository has an isolated Chrome regression harness, which uses only localhost and can test a prebuilt project without installing dependencies:

    python tests/integration/check_next_prototype_browser.py --project PATH_TO_GENERATED_BUILT_PROJECT --chrome PATH_TO_CHROME

Omit \`--project\` to have the harness create, install and build a disposable fixture before browser testing. The harness checks two viewports (390×844 and 1366×850), four mock outcomes, recovery/reset, focus and accidental network calls. A passing localhost test is **not a deployed application smoke test**.

## Traceability and acceptance

Deliver the actual model revision, route map, generated path, \`npm run build\` result and real browser observations. Compare controls, labels, transitions, error wording and data handling with the accepted screen model and userflow. Include unresolved states such as loading, expiry, OAuth, password recovery email or server-side denial when not modeled. Do not silently invent them or imply that mock sessionStorage flags prove user authentication.

ANGENT Root owns interpretation/permissions and outcome quality; BA maps requirements to screens; Frontend handles art direction; Execution builds/opens the real app; Figma Kit is only used where editable Figma nodes have a genuinely available provider.
