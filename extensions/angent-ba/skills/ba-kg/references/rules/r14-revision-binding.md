# R14: Source freshness and revision binding

## Operational contract

Identify the exact revision of every source artifact (commit, page version, provider timestamp or stable release) used to derive a claim. Maintain a comparison basis and detect material changes before write.

## Checks before accepting an artifact

Do not treat a file's latest modification time as an authoritative acceptance decision. A new SRS row can be proposed while an older approved rule remains binding.

## Failure response

On a changed source, report which derived artifacts must be reviewed and why; do not blindly propagate wording or overwrite provider edits.

## Grounded example

A generated API contract test from OpenAPI v1 cannot be reported valid against v2 until routes, response models and authorization are inspected again.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
