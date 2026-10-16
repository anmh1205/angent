# An evidence-based external API integration chain

**Provenance:** Adapted from MIT Dev BA Kit / rules/api-integration.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT exposes specialist methods, not a compulsory seven-stage workflow.

## When each method matters

| Decision | ANGENT BA method | Required concrete evidence |
|---|---|---|
| Build, buy or choose a provider | ba-api-assess | Current provider terms, feasibility, security and commercial comparison |
| Understand an external interface | ba-api-doc | Real versioned provider API docs, schemas and actual endpoint/error contracts |
| Define business and technical orchestration | ba-api-design | Authoritative field ownership, normal/failure flow, retries, timeout, recovery |
| Map provider fields into domain and UI | ba-api-map | Versioned provider schema, transform types, example payloads and ownership |
| Find missing integration tests | ba-api-checklist | Accepted FR/BR/API failures, inbound/outbound directions and test layer |
| Exercise authorized request/response assertions | ba-api-test | Real sandbox/loopback target, keys provisioned outside artifacts and test results |
| Make an enable/rollback decision | ba-api-readiness | Measured rollout, access control, monitoring, support and cutover evidence |

A fixed provider need not be reassessed without reason. A webhook-only integration may have no data transform. If live API access is unavailable, tests can be specified without claiming execution.

## Critical integration semantics

Specify upstream source of truth, local domain ownership, which side may mutate each field, mappings of provider-specific error/status values, durable idempotency keys, retry/backoff and reconciliation. A webhook can be delivered twice or out of order; a field transform can lose nullable information or enum meaning.

Separate test_layer: own system, third-party provider or mixed end-to-end; direction: outbound request, inbound event or bidirectional. The test environment must be named and secrets must never be committed to generated Bruno files.

## Existing executable checks

The portable BA adapter can check a bounded OpenAPI 3.1 JSON schema with audit_api_contract.py, verify source-linked UI field transforms via audit_api_field_mapping.py and generate Bruno collections with build_bruno.py. Unsupported schema constructs fail closed. A passing mock API proves only the fixture and expected assertions in that environment.

Before claiming readiness, confirm the target actually processed requests and side effects, plus actor authorization, release flag, rollback and real provider error scenarios. A conforming OpenAPI document is not evidence of a deployed service.

## Handoff and limits

Use accepted actual project paths and stable FR/BR/TC IDs. Do not impose a single fixed integration file or mandatory provider-specific filename. ANGENT Root chooses method depth; Execution controls API/provider writes; Quality verifies source, output and running behavior.
