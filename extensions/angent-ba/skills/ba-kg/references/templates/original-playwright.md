# Source-derived browser test generation and execution

**Accepted screen model, requirement revision and target:**
**Fixture namespace and test-only origin:**
**Browser, Playwright runtime and project test baseline:**

## Source to test mapping

| Case ID | FR/BR/AC source | Initial screen and path to reach it | User action/data | Expected UI/state | Negative result | Execution state |
|---|---|---|---|---|---|---|
| TC-PROT-… | | | | | | not-run |

Record every navigation edge, required validation, role-specific denial, error, loading, empty and recovery state where specified. Every generated case needs a route to its precondition; source ID existence alone does not establish business meaning.

## Locators and environment

Prefer roles, accessible names and deterministic test IDs, not fragile CSS positions. Block external requests in mock-only mode. Do not embed real passwords or tokens. Use browser-native validation when the model demands it. Playwright assertions must auto-wait for the expected text/focus/route rather than snapshot the DOM immediately.

## Run evidence

| Command/version | Case count | Pass/fail/skip | Captured error | External calls | Negative mutation |
|---|---|---|---|---|---|
| | | | | | |

For a bounded ANGENT HTML screen model, use build_playwright.py then the generated test_prototype.py against its local HTML prototype. Run check_generated_playwright.py as a smoke: it mutates one mock error and demands the original assertion fail. Do not claim production login or actual backend verification from this fixture.
