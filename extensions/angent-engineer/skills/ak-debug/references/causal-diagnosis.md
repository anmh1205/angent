# Causal diagnosis

Use this reference when the failure mechanism is not obvious from one observation.

## Separate observation, mechanism, and fix

Keep three layers distinct:

- **observation** — what actually happened;
- **mechanism** — how system state produced the observation;
- **intervention** — what change should break that mechanism.

A proposed fix is not proof of the mechanism.

## Find the first divergence

Trace from a known-good input or prior invariant until actual state first differs from expected state.

Useful questions:
- where is this state created?
- who owns mutation?
- where is representation converted?
- which boundary first shows invalid data/control flow?
- which earlier assumption must be true for this failure to appear?

## Hypothesis discipline

Use a compact record:

- hypothesis;
- predicted evidence;
- discriminator;
- status;
- what would reject it.

Prefer a probe that separates two live mechanisms over another broad source-code read.

## Root cause quality

A strong root cause explains:
- the observed failure;
- why it appears under the observed conditions;
- why nearby unaffected cases still work;
- why the proposed fix should remove the mechanism.

## Common traps

- treating correlation as cause;
- fixing the crash site rather than the corrupt producer;
- changing several variables before observing the effect;
- trusting one stale log;
- assuming test failure location equals ownership;
- accepting a reviewer/agent conclusion without independent evidence.
