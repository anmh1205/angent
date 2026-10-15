# Debug verification

A code change is not proof the original defect is fixed.

## Verification hierarchy

Prefer the strongest available evidence:

1. reproduce the original failure before the fix when possible;
2. apply the fix;
3. rerun the original reproduction path;
4. run targeted regression coverage;
5. widen to affected integration/build/UI scope when the change can propagate.

## Red/green evidence

For a new regression test, a strong check is:
- test fails against the defective behavior;
- test passes with the fix.

Use this when practical; do not create artificial ceremony when the old failure is already captured by an existing reliable test.

## Blast radius

Verify interfaces/consumers materially affected by the fix.

Do not extrapolate a local pass to whole-project correctness.

## Claims

Good:
- “The original reproduction now passes; targeted X/Y regression tests also pass.”

Not enough:
- “Code looks right.”
- “The agent reported success.”
- “Build passes” when the bug was a runtime/UI behavior.
- “One unit test passes” when the defect crossed multiple layers.

## Unavailable verification

If the environment lacks the needed hardware/browser/provider state, say exactly what remains unverified.
