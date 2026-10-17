---
name: ba-api-readiness
description: Source-driven BA api-readiness method with independent decision evidence, output validation and safe provider boundaries.
---

# API readiness: evidence gates for a safe integration rollout

**Method background:** Maintained independent adaptation of MIT Dev BA Kit \`api-readiness\` by Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-readiness/SKILL.md. This method advises launch decisions; ANGENT Root and authorized operators control production deployment.

## Establish the exact release unit

1. Identify the integration, target environment, provider/API version, intended users, owning team, release scope and consequences of failure. Check accepted FR/BR/NFR and the provider's current contract/terms before proposing a cutover.
2. Read actually performed tests and the environments in which they ran. Distinguish generated Bruno/Playwright files, loopback mocks, sandbox/provider integration and production canary probes. A file named \`api-tests.md\` is **not evidence** merely because it exists, and its absence is not proof that no tests ran.
3. Verify contract shape against the actual OpenAPI/provider docs; note OAuth/API key scopes, tenant separation, secrets handling, expiration, throttling/rate limits, error behavior, idempotency and webhook authenticity where applicable.
4. Define the enablement sequence with owners and a **verified** off/degraded state: feature flag or runtime configuration, rollback switch, migration compatibility and safe behavior if an upstream provider is unavailable.
5. Establish operational monitoring: user-impacting latency/errors, provider health signals, queue/retry backlog, key business outcomes, actionable alerts, runbook owner and realistic detection/response criteria. Unknown thresholds are release risks, not numbers to invent.
6. Check downstream data effects and reconciliation: retries, duplicate webhooks, partial writes, compensating operations, irreversible provider actions and what happens to already-written data after disabling a flag. A kill switch alone is not rollback.
7. Check provider reliability/deprecation, key rotation and contractual boundaries from current supported sources, not stale marketing. Distinguish vendor commitments from your own SLA/SLO.
8. Assess test coverage of negative cases at the *actual* required level: access denial, invalid payload, provider timeout, partial response, duplicate delivery, transient rate limit, expired authorization and recovery. A local mock pass only demonstrates the mock behavior.
9. Build a clear gate matrix for **contract**, **authorization**, **test evidence**, **data safety**, **observability**, **operational ownership**, **cutover**, **rollback** and **provider dependencies**. For each gate record current evidence, environment, verified/unverified status, risk and exact owner.
10. Recommend GO only when every *material* release gate is supported by the required environment and approved risk owner. Otherwise explicitly recommend HOLD/NO-GO and name the smallest next observation required to lift each blocker. Do not automatically flip a flag or submit a release.

## Useful tooling already present

\`ba-api-test\` can generate real Bruno requests and execute them in an authorized sandbox. \`extensions/angent-ba/scripts/audit_api_contract.py\` checks a conservative OpenAPI 3.1 subset, and \`extensions/angent-ba/scripts/audit_api_field_mapping.py\` verifies source-to-UI mappings using a supplied fixture. None of these establish a successful real provider rollout. For a high-risk integration, provider-level results, deployment health and rollback rehearsals remain necessary.

## Deliverable and acceptance

Produce the current release recommendation, concise evidence-backed gate table, blocked/unknown items, owners, cutover and rollback plan, failure handling and recheck triggers. Show the difference between "not required", "not measured" and "failed"; never hide a risk by merging these categories.

For a hypothetical vehicle telemetry provider, a 4/4 Bruno test result against localhost is useful contract regression evidence, **not** proof of live GPS device ownership or cloud authorization. ANGENT Root owns the final decision and permission scope; BA documents readiness criteria, Engineer/Operations supplies deployment evidence and Execution verifies consequential changes.
