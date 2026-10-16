---
name: ba-api-test
description: Build real Bruno API test collections from approved endpoint contracts, with explicit assertions and optional authorized sandbox/loopback execution.
---

# BA API tests — executable Bruno artifacts

**Provenance.** Method adapted from the MIT Dev BA Kit api-test skill, copyright (c) 2026 Edward Ngo: https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-test/SKILL.md. ANGENT adds an independently written collection generator and optional local integration fixture. No paid AI4BA source code is included.

## Contract and authority

API testing should verify exact effects implied by accepted FR/BR/AC and endpoint contracts, not merely produce a list of HTTP requests. ANGENT Root decides scope, Execution owns generated files and any real call, Quality checks actual assertions and side effects.

1. Read approved API checklist, versioned contract/OpenAPI, environment boundaries, endpoint method/path, authentication scopes, expected error states and stable test-case IDs.
2. Build one request per actual automatable scenario. Assign exact expected HTTP status and **observable response fields**; include negative authorization, duplicate request, validation and transient provider failure where required. The current minimal generator supports exact top-level JSON scalar assertions, not comprehensive nested JSON Schema or side-effect reconciliation.
3. Reject guesses about response schema or business thresholds. Ask for missing consequential contracts or label the test draft unverified.
4. Define a reviewed JSON request model analogous to the synthetic example at extensions/angent-ba/examples/synthetic-fleet-api-tests.json. It includes collection name, environment values and requests containing id, name, method, path, expected_status and expected_json. A request can optionally declare headers and body_json for POST/PUT/PATCH/DELETE.
5. Generate an actual Bruno v1 collection with a separate environment file and .bru tests using a Python runtime:

    python extensions/angent-ba/scripts/build_bruno.py INPUT.json --output output/bruno-collection

6. Inspect the output and ensure credentials are never committed. Use an explicit environment variable/secret store for tokens; never treat synthetic host/user values as real. The generator only writes files. Its successful exit proves neither connectivity nor test success.
7. Only with an authorized **sandbox or loopback** endpoint and a real Bruno CLI, execute the collection. Never run destructive, external or production endpoints by default. A loopback-only integration fixture is available:

    python tests/integration/check_bruno_cli.py --cli PATH_TO_BRU

8. Verify the CLI exit code and executed request count, expected statuses and response-field assertions. When an operation mutates state, additionally read back actual side effects and perform cleanup. Record skipped/blocked tests separately.
9. Provide generated paths, stable case IDs, run environment, actual test output and unresolved contract gaps. Do not claim green production readiness from an isolated mock service.

## Current capability limits

Supported: GET, POST, PUT, PATCH and DELETE collection definitions; explicit environment variables; optional JSON bodies/headers; exact status and top-level JSON scalar comparisons. Every generated request includes runnable Bruno tests. It does **not** currently implement full schema validation, chained request variables, idempotency verification, timeouts, side-effect assertions, authorization provisioning or live provider synchronization. Bruno CLI must be installed separately.

The example fleet suite is **synthetic** and tests only an in-process localhost mock: one successful vehicle status, one forbidden access and one unavailable telemetry response. It neither authenticates a real device nor validates production fleet authorization.

## Review failures

Generated tests without real execution evidence, invented response fields, hard-coded secrets, unchecked external write effects, false security assurances, and a simplistic positive-only suite all fail the task's intended quality.
