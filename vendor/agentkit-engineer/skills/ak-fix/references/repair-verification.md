# Repair verification

Verification should prove both **target repair** and **protected behavior**.

## Original path

Re-run the strongest available pre-fix reproduction:
- exact failing test/command;
- request/input;
- runtime/UI path;
- CI/provider condition.

Compare before/after evidence when available.

## Regression prevention

Add/update a test or guard that captures the actual bug class when practical.

A useful regression test:
- fails on the faulty state;
- passes with the repair;
- tests the causal contract rather than incidental implementation detail.

Do not create a test merely to raise count/coverage.

## Blast-radius sweep

From diagnosis, identify consumers/paths that:
- call the changed interface;
- share the faulty producer/state;
- rely on the public contract;
- can regress due to the repair.

Run targeted tests or inspect/manual-walk those flows proportional to consequence.

## Contract preservation

Check as relevant:
- function/public API signatures;
- schemas/persistence/migrations;
- response/event shapes;
- environment/config;
- permissions/security behavior;
- timing/concurrency/ordering assumptions.

Any intentional contract change returns to the accepted decision/plan rather than being hidden as a "fix".

## Build/static/runtime evidence

Run only checks that can establish a relevant property:
- type/static/lint;
- build;
- unit/integration/e2e;
- browser/UI/runtime;
- provider/CI.

Do not confuse one green layer with endpoint proof.

## Side-effect failure

If the repair fixes the symptom but breaks protected behavior:
- preserve both observations;
- explain the causal conflict;
- return to Reasoning for a new repair model or a genuine user-owned trade-off.

Do not silently optimize the opposite extreme or patch the failing dependent until the controlling contract is clear.

## Final verdict

Use precise state:
- verified repair;
- implemented but verification incomplete;
- blocked by unavailable environment/provider;
- root cause/repaired behavior still uncertain.
