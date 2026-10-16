# Portable screen-model contract

This is independently authored ANGENT JSON input for both static wireframe and interactive mock prototype modes. It is not extracted from paid AI4BA files.

## Required structure

- title: nonempty review title
- start: screen ID used as entrypoint
- scenarios: unique list of mock response names, for example success, invalid, locked and offline
- screens: array of objects with unique id, title, optional description and controls
- controls: objects with id, type, label and optional requirements array of source requirement IDs
- supported input types: text, email, password, checkbox. Optional required and placeholder fields
- note: static text
- button: a navigate action holding an existing target screen ID
- submit: outcomes map with one entry for **each** scenario, each outcome either navigate with an existing target, or error with a nonempty message

The validator rejects missing input/labels, duplicate screen/control IDs, invalid targets, unreachable screens, unsupported control types and scenario mismatches. However, it cannot prove a screen model represents every accepted business rule: source comparison remains a mandatory semantic review.

## Reference implementation and executable checks

Example JSON: extensions/angent-ba/examples/authentication-screen-model.json
Renderer: extensions/angent-ba/scripts/build_wireframe.py
Unit tests: tests/test_ba_wireframe.py
Live browser test: tests/integration/check_wireframe_browser.py

Commands at the ANGENT repository root:

    python extensions/angent-ba/scripts/build_wireframe.py INPUT.json --mode wireframe --output output/wireframe.html
    python extensions/angent-ba/scripts/build_wireframe.py INPUT.json --mode prototype --output output/prototype.html
    python tests/integration/check_wireframe_browser.py --chrome PATH_TO_CHROME

The browser integration checks only the synthetic Authentication fixture's scenario contract. A new userflow needs its own input evidence, expected results and browser-level tests. The prototype has no working production backend and may not be used to authenticate actual users.
