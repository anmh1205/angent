---
name: ba-api-test
description: Build real Bruno API test collections from approved endpoint contracts, with explicit assertions and optional authorized sandbox/loopback execution.
---

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


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

## Optional OpenAPI contract gate (implemented)

Before creating Bruno files, inspect the actual accepted OpenAPI 3.1 **JSON** document. Compare the proposed request model against it:

    python extensions/angent-ba/scripts/audit_api_contract.py CONTRACT.json TEST_MODEL.json

Or enforce the check during collection generation:

    python extensions/angent-ba/scripts/build_bruno.py TEST_MODEL.json --openapi CONTRACT.json --output out/verified-bruno

The checker resolves declared paths and methods, exact HTTP statuses, scalar JSON assertions (including nested properties), required JSON request body fields and declared bearer security. It can resolve **bounded local** JSON-pointer references to schema/response/requestBody components and rejects remote references, reference cycles and unsupported oneOf/anyOf/allOf composition rather than manufacturing a pass. It does not make HTTP requests or validate server behavior.

A synthetic example is provided in extensions/angent-ba/examples/synthetic-fleet-openapi.json, paired with the local four-request fleet tests. The checker is a deliberately conservative *subset* of OpenAPI 3.1, not a general-purpose validator or implementation verifier; JSON Schema constraints beyond supported type/const/enum/required need a fuller parser and independent review. Generated files still require an actual Bruno CLI run against an authorized sandbox or loopback target to report test success.

## Standards-aligned contract interpretation

The conservative OpenAPI 3.1 JSON checker follows the official exact-status / class-range / default response precedence and operation-level security override, including alternative security requirements. For response scalar fields and JSON object request bodies it enforces supported local schema references, type unions, const/enum, string lengths and numeric bounds. It **does not** implement full JSON Schema 2020-12, OAuth scopes, remote $ref, composed oneOf/anyOf/allOf, arbitrary pattern or extended conditional schemas. Such constraints fail closed rather than being silently accepted. Official references: https://spec.openapis.org/oas/v3.1 and https://json-schema.org/draft/2020-12/json-schema-validation.

Always run this separate static contract check before using live Bruno API tests, then assess the provider response and side effects independently. The static checker must never be presented as a production contract validator or proof of actual API behavior.
