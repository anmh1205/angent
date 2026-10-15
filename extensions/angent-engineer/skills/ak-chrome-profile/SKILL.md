---
name: ak-chrome-profile
description: Use an authorized real Chrome profile when the active browser runtime supports it; otherwise fall back to an isolated session without extracting credentials.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# Chrome Profile — Portable Fallback

Read `references/profile-safety.md`.

## Preferred behavior

If the harness can attach to an authorized real Chrome profile:
1. enumerate/select by observable profile/tab identity;
2. attach through supported browser/DevTools integration;
3. reuse existing authenticated state only for the authorized task;
4. verify the target page/account before consequential action.

## Fallback

When profile attachment is unavailable:
- use isolated browser;
- ask the user to authenticate normally when appropriate;
- or mark authenticated-profile capability unavailable.

Do not copy browser profile files or export cookies/tokens as a workaround.

## Stable 2.19.0 signed-in profile requirements
Use this route when existing real Chrome authentication, extensions or tabs are essential; otherwise prefer isolated browsing. Identify and confirm a supported browser/DevTools attachment, exact profile/tab/account and permitted navigation/effects before acting. Browser profiles hold high-value cookies, downloads and unrelated accounts: never copy profile files, export tokens/cookies, scrape all tabs or substitute a different logged-in profile.

Refresh account/tab identity after navigation and before consequential actions. When the runtime has no authorized profile attachment, explicitly mark capability unavailable or ask the user to sign in normally in a permitted isolated browser; do not claim to have preserved the profile. Verify final page state and release/detach browser resources.
