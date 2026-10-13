# Edge cases and impact

Use this reference when the change has non-trivial state, shared consumers, asynchronous behavior, or boundary risk.

## Candidate areas

Consider only what fits the code:
- null/empty/missing data;
- minimum/maximum/off-by-one boundaries;
- malformed/untrusted input;
- retries/timeouts/partial failure;
- concurrency/races/order;
- resource cleanup;
- stale caches/state;
- authorization/tenant boundaries;
- migration/backward compatibility;
- cancellation/restart/recovery;
- locale/timezone/encoding;
- UI loading/error/empty/auth states.

## Indirect consumers

Search callers/importers/schema consumers when a shared contract changes.

Do not invent hypothetical callers when repository evidence shows none.

## Security

Prioritize trust-boundary defects:
- unchecked external input;
- authorization bypass;
- secret exposure;
- unsafe command/query construction;
- data-scope leakage.

## Performance

Only raise performance findings with a plausible material path, not generic micro-optimization preferences.

## Evidence standard

An edge case becomes a finding when code behavior and consequence can be explained concretely.
