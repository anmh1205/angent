---
name: ba-prototype-html
description: Generate and verify a standalone click-through HTML mock prototype from accepted screens, with form validation and explicit failure responses.
---

# BA interactive HTML prototype — implemented method

**Provenance.** Adapted from the MIT Dev BA Kit prototype-html method (Edward Ngo, 2026). Source: https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prototype-html/SKILL.md. A runnable ANGENT generator and Chrome integration check implement a bounded subset independently.

## Purpose

Validate screen navigation, form affordances and agreed error outcomes through a real browser. All results are explicitly mocked. The prototype cannot issue real tokens, log in a user, persist sessions, send email, call APIs or prove backend security. ANGENT Root owns intent and Quality; Execution owns authorized file edits and browser observations.

## Procedure

1. Inspect approved userflow, SRS, business rules, error matrix and any existing ASCII/HTML wireframes. Enumerate every required screen and scenario before coding, including error, denial, network outage, cancellation and recovery.
2. Prepare one JSON screen model following the stable ID, control, action, scenario and outcome contract documented in ../ba-wireframe-html/references/screen-model.md. Submit controls need a declared result for each scenario. Resolve important unknown business behavior rather than silently assigning a convenient default.
3. Inspect generated model for coverage and semantic correctness; the structural validator is not a replacement for comparing the actual requirement and userflow.
4. Run the actual tool when Python and filesystem are available:

    python extensions/angent-ba/scripts/build_wireframe.py INPUT.json --mode prototype --output output/prototype.html

5. In the page, choose a visible **Mock response** and submit. Browser-native required/email validation precedes the mock outcome. Success navigates to the declared screen; failures display a role=alert response. A navigate control explicitly routes to another screen. No request is sent to a backend.
6. Verify the HTML in an actual browser, including required-field denial, bad email, each mock failure, success navigation, recovery/back route, keyboard focus and narrow/wide layouts. Record console errors.
7. For the included synthetic example, a reproducible optional Playwright/Chrome test exists:

    python tests/integration/check_wireframe_browser.py --chrome PATH_TO_CHROME

8. Deliver the real HTML file location, source revision, scenarios checked and any unverified business branches. If no runtime was available, report a proposed source model rather than a working prototype.

## Guardrails

The generator embeds the JSON safely and renders dynamic screen text with DOM textContent. It does not use external JS packages, remote CDNs or API calls. Accessible labels, browser validation and alert regions are implemented but do not constitute a full WCAG audit. The engine supports text/email/password/checkbox input, static notes, navigation buttons and mocked submit outcomes. No support for OAuth, server-side locking, advanced form logic, multi-user testing, screenshot capture by default or Figma writes is implied.

In the example, the result categories success, invalid, locked and offline are synthetic demonstration states, not actual requirements for the user's product.
