---
name: ba-reverse-preview
description: Present reconstructed business claims with provenance, uncertainty and contradictions in an actual safe read-only HTML viewer.
---

# Reverse-specification preview with visible evidence classes

## Purpose

Legacy code and archives frequently disagree. A reverse preview must let stakeholders distinguish a direct inspected witness, a plausible inference, an unresolved statement, a conflict and a genuinely approved decision. A polished HTML page must not silently promote hypotheses to approved requirements.

## Build a claim ledger from actual sources

1. Read the relevant reverse-doc/code-to-SRS evidence, pinned commit or original document revision, affected actor and known conflicts. Do not pull private records outside the user's authorized scope.
2. For each claim assign a unique ID, a concrete business-behavior statement, an explicit class: SOURCE-OBSERVED, INFERRED, UNCONFIRMED, CONTRADICTORY or APPROVED-DECISION, and inspected source IDs. Contradictions require *at least two* distinct source witnesses and a verification action.
3. An APPROVED-DECISION requires an actual decision ID and cited approval source; a code method name or model interpretation alone is not approval.
4. State the impact if wrong, next source or runtime check, and any contradictory text. Do not collapse uncertainty into an arbitrary global confidence percentage.
5. Pass the reviewed ledger JSON to the **actual** ANGENT reverse-preview renderer. It validates references, rejects unsupported status/invalid approvals, escapes source HTML, and never embeds scripts or fetches third-party assets.

## Commands

    python extensions/angent-ba/scripts/render_reverse_preview.py extensions/angent-ba/examples/reverse-evidence-synthetic.json --output out/reverse-review.html --title "Reconstructed evidence"

The example JSON is deliberately synthetic; replace its source URLs and claims with evidence actually inspected for the user's project. The exporter refuses to overwrite an existing output file.

Run a real Chrome smoke:

    python tests/integration/check_reverse_preview_browser.py --chrome PATH_TO_CHROME

The browser test exercises three source classes including conflicting witnesses, claim-index navigation, no external HTTP requests and absence of JavaScript runtime errors.

## Review and limits

Open the HTML and verify every source link is correct for the reader's permissions. Only HTTP(S) URLs become clickable; local and untrusted schemes remain text. The output is an **evidence review**, not a validated SRS, Figma asset or production status report. ANGENT Root owns interpretation, Execution handles any authorized publication and Quality compares the finished page to the actual source ledger.
