# Verification and verdict

Review verdicts should be tied to the requested gate.

## Fresh verification

When practical, run or inspect checks that can confirm material review claims:
- targeted tests;
- type/build/lint checks;
- integration tests;
- browser/runtime verification;
- migration/schema checks.

Use the project-native commands from AGENTS.md/config/CI where possible.

## Finding verification

Before keeping a blocking finding:
- trace the relevant path;
- confirm project/version context;
- check whether another layer already enforces the invariant;
- verify that the impact is reachable.

## Verdict

Examples:
- **ready for requested gate** — no unresolved material finding in reviewed scope and required verification passed;
- **not ready** — material findings remain;
- **blocked / insufficient evidence** — required environment or evidence unavailable.

Avoid universal claims like “code is correct”.

## Coverage

State what was reviewed and what was not.

A review of a PR/diff cannot certify the entire repository unless whole-repo coverage was actually performed.
