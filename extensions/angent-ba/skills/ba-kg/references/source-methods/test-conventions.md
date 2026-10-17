# Acceptance criteria, test checklists and executable evidence

**Provenance:** Adapted from MIT Dev BA Kit / rules/test-conventions.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit.

## Relationship of AC, CHK and TC

An AC is an observable condition under which a stakeholder accepts a behavior. CHK asks which behaviors/boundaries/errors must be verified. TC provides concrete preconditions, test data, actions and expected results. Many TCs may verify one CHK; do not limit a boundary requirement to a single happy-path case.

Preserve stable project-local identifiers and real FR/BR/E links. A TC with no genuine requirement coverage may still be valid exploratory work, but it must not be counted as FR-completion evidence.

## Test case quality

For each case, specify precondition and role/tenant, data fixture, trigger, exact expected response or state change, cleanup, relevant environment and whether execution is possible. Include positive, denied, invalid input, boundary, upstream failure, retry and recovery states when materially required.

Security-sensitive behavior requires verifying **absence** of unauthorized data and side effects, not only an error status. A timeout should not be represented as a business denial if the contract distinguishes them.

## Test artifacts versus actual results

- Test specified means an expected outcome has been written.
- Test generated means code or collection file exists.
- Test executed-pass means an actual runner observed the expected state in the stated environment.
- Mock pass means only the simulated fixture was verified; it is not automatically production pass.

No fixed number of pass rows is a universal acceptance threshold. Use exact scope and denominator.

## Runnable ANGENT tools

The portable BA Kit can compile reviewed mock screen models to HTML and generate Python Playwright cases. It can also generate Bruno collections checked against a bounded OpenAPI contract and run them only against authorized loopback/sandbox services. D2/BPMN validators cover diagram-specific structural quality.

These tools cannot invent the target application's business rules or live credentials. A generated collection is not successful test execution.

## Review

Report concrete missing FR/AC/CHK links, untested failure paths, data constraints, execution status, observed errors and next actions. Never mark a case passed solely because the issue was closed or the test file was created.
