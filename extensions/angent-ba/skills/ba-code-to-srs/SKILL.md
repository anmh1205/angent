---
name: ba-code-to-srs
description: Specialized ANGENT business-analysis procedure for code-to-srs.
---

# Reverse engineering source code into a defensible SRS

## Outcome and epistemic boundary

Reconstruct **current observable behavior** from the checked-out source, not the author's presumed intentions. An implementation may be defective or incomplete; its behavior is not an approved business requirement. Deliver a source-indexed reconstruction, a candidate SRS and a discrepancy register, with explicit confidence categories: VERIFIED IN SOURCE, INFERRED, UNCONFIRMED, CONTRADICTORY.

## Method

1. Fix a commit SHA and enumerate deployables, packages, API routes, databases, migrations, configs, queues, scheduled jobs, device/edge protocols, tests and feature flags. Limit analysis to the requested feature before traversing dependencies.
2. Follow entrypoint to domain decision to persistence to outbound integration. Do not equate a route name or UI label with implemented behavior; inspect guards, early returns, error handling and data side effects.
3. Record observations in an evidence ledger with stable claim ID, relative file path, function/symbol, real line range, commit, observed predicate and the exact consequence. When lines are unavailable, cite symbol and commit and mark line-level verification missing.
4. Reconstruct actors, preconditions, trigger, ordered flow, states, authorization boundaries, business constraints, timeouts, retries, deduplication and error contracts. Classify each claim independently.
5. Compare tests to implementation: tests are evidence of intended expectations, not proof of deployed behavior. Check whether test paths are skipped, mocked or detached from production wiring.
6. Derive FR/NFR/BR candidates only after the behavior ledger. For every FR, add a reference to at least one source observation or explicit stakeholder decision. Include negative and recovery paths.
7. Resolve contradictions through actual config precedence and call paths where possible. Otherwise maintain alternative observations in a conflict table; do not invent which version won.
8. Separate validated implementation facts, unsupported policy guesses and a recommended future target specification. Ask for business approval before promoting an observation to the approved SRS.
9. Conduct source read-back at the pinned commit and link each open question to the smallest useful next inspection or test.

## Output contract

- System boundary and deployment assumptions, including what was NOT inspected.
- Source ledger: Claim | Revision | Path/symbol/line | Observed behavior | Confidence | Contradiction.
- Functional specification FR, business rules BR, error matrix E, state transitions and data effects.
- Confidence summary by claim, not one blanket document confidence.
- Implementation vs desired-product differences with owner/decision status.
- Reproduction or test plan for high-risk assumptions.

## Worked micro-example

Observation: the vehicle-status handler reads a vehicle by ID before checking the requesting user's ownership. This supports an **investigation finding**, not a statement that ownership checks are intentionally optional. Document: 'FR candidate: status must only be visible to authorized user' (proposed). Confirm guard execution, service-level policy and test behavior before calling it implemented.

## Negative controls

Reject fabricated file paths, line numbers, production claims from mocked unit tests, imagined business policies and edits to source code under an audit-only request. Delegate implementation only after separately authorized change work.


## ANGENT cooperation

ANGENT Root/Reasoning owns interpretation and decisions; Authoring owns narrative quality; Execution handles authorized external effects; Quality verifies the outcome. Method selection is optional and context-dependent, never a forced workflow.

## Executable pinned-code evidence verification

The kit includes a **read-only** command that reads an exact Git commit blob and checks whether each declared code witness is present at the stated path and line range. The full 40-hex Git revision, requirement ID, source path and expected excerpt must all match. Optional SHA-256 detects stale snippets. It is a bounded evidence verifier, not automatic requirements inference.

    python extensions/angent-ba/scripts/verify_code_witness.py extensions/angent-ba/examples/code-evidence/synthetic-code-witness.json --repo . --revision FULL_GIT_COMMIT_SHA --evidence-graph extensions/angent-ba/examples/rental-fleet-traceability.json

The example is a synthetic access guard committed in ANGENT; it **is not a scan of a real IVTS firmware, ECU or cloud repository**. Existing BA source IDs are resolved against the same validated graph used by SRS, tests and Figma. Missing files, missing excerpts, wrong revision and escaping the repo path fail rather than becoming an ALIGNED claim.

After a witness is verified, reason independently about input guards, business outcomes, error paths, feature flags, actual runtime and deploy. The script reports \`semantic_alignment=not-assessed\` and \`deployment_verified=false\` even when it finds the literal code. Use this witness in \`ba-doc-drift\` only as **part** of the comparison, not as the verdict itself.
