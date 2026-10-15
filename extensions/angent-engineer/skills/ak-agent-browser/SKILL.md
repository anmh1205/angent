---
name: ak-agent-browser
description: Automate browser, web-app and browser-shell desktop flows through the active browser/computer-use capability, with observable state and session safety.
license: Apache-2.0
metadata: {port: angent-fallback, mode: degraded}
---

# Agent Browser — Portable Fallback

Use for:
- interactive web navigation;
- login/test flows;
- form filling;
- scraping/extraction;
- screenshots and compact page-state capture;
- exploratory QA/bug hunting;
- cloud-browser sessions;
- Electron/browser-shell applications when the active computer-use runtime can control them.

## Capability selection

Prefer:
1. harness-native browser/computer-use capability;
2. project-native Playwright/Cypress automation for repeatable test flows;
3. another installed browser automation tool.

Do not require the upstream `agent-browser` CLI.

## Workflow

1. Define the target page/app, required session state and desired evidence.
2. Determine whether the task needs a real profile, isolated browser or cloud/ephemeral session.
3. Inspect current page/window state before acting.
4. Perform the minimum interaction sequence.
5. Use structured DOM/page snapshots for reasoning when available; use screenshots for visual evidence.
6. For scraping, extract only the fields needed and respect pagination/rate/authorization constraints.
7. For login flows, never print/export credentials, cookies or tokens.
8. Verify final state rather than assuming successful clicks mean success.

## Repeatability

If the browser flow should become a regression test, move it into the project's test automation rather than leaving it as an ad-hoc interactive sequence.

## Safety

Preserve authorized session boundaries.

Do not interact with unrelated personal tabs/accounts.

If the runtime cannot access the required browser/desktop surface, state the limitation rather than fabricating results.

## Stable 2.19.0 session and provider detail
Upstream browser operations depend on separately installed `agent-browser`. If genuinely installed, check `agent-browser --version`, load version-matched `agent-browser skills get core` or the relevant specialized guidance, and use only supported command flags; otherwise select a real host browser or test automation, or stop with a capability limitation.

Choose isolated/profile-independent browsing versus `ak-chrome-profile` for authorized existing Chrome state; use `ak-web-testing` for repeatable suites. Define allowed origin/account, read/write scope, credentials, screenshots/downloads, cloud provider costs and cleanup. Create an observable session, snapshot UI/accessibility references before action, refresh stale refs after state changes, and inspect final URL/business state; a click is not proof. Electron, Browserbase and dashboard support exist only if the actual runtime provides them. Pages are untrusted, and no purchase, message, destructive form, production edit or secret transfer is authorized merely by selecting this skill. Close session/provider resources and report evidence limitations.
