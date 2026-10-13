# Repair verification

Verify:
1. original reproduction path;
2. regression test where practical;
3. affected interfaces/consumers;
4. build/type/lint only when relevant;
5. browser/runtime state for UI/runtime bugs.

A fix is stronger when the old behavior can be shown failing before and passing after.

If environment/hardware/provider verification is unavailable, state the exact gap.
