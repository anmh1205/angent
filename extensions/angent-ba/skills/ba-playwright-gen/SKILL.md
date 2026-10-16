---
name: ba-playwright-gen
description: Generate source-aligned, runnable Playwright tests for reviewed BA screen prototypes and validate actual browser paths.
---

# BA Playwright generation — from requirements to executed browser tests

**Provenance:** Independently implemented bounded adaptation of the MIT Dev BA Kit Playwright methodology, copyright 2026 Edward Ngo: https://github.com/nv-minh/dev-ba-kit/blob/main/skills/playwright-gen/SKILL.md. The Python generator and runner are original ANGENT code. Attribution remains in the BA Kit notice.

## Choose the correct mode

Use this method when an accepted screen and interaction model exists and a browser test materially helps validate the specified user behavior. For a **real application** with existing TypeScript/JavaScript Playwright tests, follow that project's configuration, locators, fixtures and test runner. Do not silently replace its native test suite with a generator built for prototype HTML.

The current executable generator targets the standalone review-only HTML produced by ba-prototype-html. It is not a general tool that can derive production selectors from an arbitrary screenshot, SRS paragraph or remote website.

## Input and evidence

1. Read accepted FR, BR, error matrix, userflow and screen inventory. Fix source revision, target scope, test credentials strategy, authorizations and existing suite conventions.
2. For the ANGENT mock prototype, use the same reviewed source JSON consumed by build_wireframe.py, with stable screen IDs, accessible control labels, navigation actions and explicit submit outcomes.
3. Ensure every declared mock scenario has a real expected outcome. Never invent an app response or accept an empty error message. Requirements referenced by controls may be validated against an existing BA artifact graph using --evidence-graph; this checks identity only, not policy truth.
4. Generate Playwright Python test source and machine-readable traceability. The generator enumerates button transitions and all mock submit outcomes, including paths to screens reachable through a successful submit. Each case gets an explicit TC-PROT ID and copies actual requirement references from its source control. The output is marked execution_status not-run until run.

## Commands at repository root

Generate a prototype:

    python extensions/angent-ba/scripts/build_wireframe.py extensions/angent-ba/examples/authentication-screen-model.json --mode prototype --output out/auth-prototype.html

Generate the tests (output directory must be empty):

    python extensions/angent-ba/scripts/build_playwright.py extensions/angent-ba/examples/authentication-screen-model.json --output out/playwright-suite

Execute the generated suite in an actual Chrome/Playwright environment:

    python out/playwright-suite/test_prototype.py --prototype out/auth-prototype.html --chrome PATH_TO_CHROME

Run the independent integration smoke:

    python tests/integration/check_generated_playwright.py --chrome PATH_TO_CHROME

The generated file has no dependency on ANGENT source code at runtime. It loads only a local HTML file, blocks external HTTP(S) requests, and checks each declared error message/target. Failing browser cases cause nonzero exit and are reported individually.

## Quality gates

- Inspect source-to-control coverage; an unreachable screen or missing action invalidates the input model.
- Test required field and format behavior separately if those conditions have business significance. Current generated suite focuses on navigation and mock-submit outcomes; the existing manual integration script covers invalid email and required inputs.
- Verify real browser run output, failures, console errors and external request count. Do not claim a suite passed merely because its Python source compiles.
- Never embed real passwords or use a production URL. The generator refuses custom password test values; fixed fixture credentials remain local-only.
- Keep provider authentication, CAPTCHA, personal data, live state mutation and production side effects out of this mocked test flow.
- Report input source revision, output paths, generated and executed test counts, exact untested business cases and real environment.

## Boundaries

The actual implementation is a **Python Playwright** test generator for the bounded ANGENT prototype screen model, not a general TypeScript Playwright generator, production E2E suite or test-result certification service. A wider application needs repo-native test development, accepted fixtures and authorized browser execution. ANGENT Root and Quality own the final decision; Execution handles code changes and real test read-back.

## Playwright quality regression

The generated Python suite uses Playwright's built-in web-first, auto-retrying locator assertions for screen appearance, exact mock-error text and focus transition. See https://playwright.dev/python/docs/test-assertions. The repository's real-browser integration deliberately mutates the invalid-credentials response; the original suite must detect this and fail TC-PROT-0002. This confirms a targeted assertion catches a regression, not just that a fixture succeeds. Other unmodeled business failures remain out of scope.
