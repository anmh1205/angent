# Browser evidence

Useful artifacts include:
- screenshot for visual state;
- trace/video for interaction sequence;
- console logs;
- network request/response metadata;
- DOM/accessibility snapshot;
- storage/session state only when safe and relevant.

## Auth

Prefer test accounts/fixtures.

If using an authorized real session, do not export cookies/tokens.

## Evidence discipline

State what the artifact proves.

A screenshot proves rendered appearance at one viewport/time, not backend correctness.

A network 200 does not prove the UI handled the response correctly.
