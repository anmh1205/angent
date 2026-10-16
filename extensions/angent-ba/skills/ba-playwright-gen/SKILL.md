---
name: ba-playwright-gen
description: Specialized ANGENT business-analysis procedure for playwright-gen.
---

# Derive robust Playwright tests from approved test cases

## Preconditions

Read actual test-case IDs, acceptance criteria, app URL, test credentials provisioning, environment, data isolation and known accessibility selectors. Verify the repo already contains Playwright and identify its config. A proposed test cannot be labeled passing until executed against an actual target.

## Conversion algorithm

1. Construct traceability table: TC ID, covered AC and FR, initial state, actors, fixtures, action sequence, assertions, cleanup, source revision.
2. Convert every action to a single purposeful Playwright step. Prefer getByRole, getByLabel, getByPlaceholder only when labels are unique; use stable test IDs only if semantic locators cannot identify the element. Never rely on fragile CSS nth-child chains.
3. Assert the state change that matters, not only navigation or HTTP status. Verify user-visible error text or state as accepted; for persisted actions check the authoritative backend only if a safe test API is available.
4. Isolate accounts/tenants and fixtures; avoid global mutable state and hardcoded production credentials. Use project helpers to provision and cleanup test data, and make failure cleanup idempotent.
5. Use Playwright auto-waiting assertions. Do not introduce sleep-based races. Handle deliberate virtual time or mocked network responses using Playwright fixtures and clear scenario naming.
6. Test network-failure, duplicate-submit, access-denial, validation boundaries and cancellation for the actual business rule. For browser testing of real provider login flows, respect authorization and CAPTCHA boundaries; do not bypass authentication mechanisms.
7. Run the focused test, inspect trace, screenshot and console/network diagnostics on failure; fix selectors or app defects according to evidence, not by weakening assertions.
8. Report tested browser project, targeted spec, pass/fail/skip counts and unsatisfied environment prerequisites separately. Provide links to test artifacts.

## Minimal idiom

```ts
import { test, expect } from '@playwright/test';
test('TC-AUTH-014: shows an approved invalid-credentials outcome', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('test-user@example.test');
  await page.getByLabel('Password').fill('incorrect-fixture-password');
  await page.getByRole('button', { name: /sign in/i }).click();
  await expect(page.getByRole('alert')).toContainText(/invalid credentials/i);
});
```

This illustrates locator and assertion style, **not** a working test until fixture account, product labels and exact error contract are verified.

## Failure modes to avoid

A generated code file is not a passed test; test IDs are not inferred from unrelated UI controls; no blanket retries hide real flakiness; browser text expectations are not invented. Preserve the host-approved app framework and test suite.


## ANGENT cooperation

ANGENT Root/Reasoning owns interpretation and decisions; Authoring owns narrative quality; Execution handles authorized external effects; Quality verifies the outcome. Method selection is optional and context-dependent, never a forced workflow.
