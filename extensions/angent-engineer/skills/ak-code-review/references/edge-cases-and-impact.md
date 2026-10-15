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

## Cross-boundary causality

For a change spanning layers, reconstruct one real input through producer → representation/transport → consumer → observed result. Check whether each layer agrees on units, data shape, optionality, ordering, version, error handling and recovery. A defect at the final consumer may originate at the first producer that violated an invariant. Conversely, correcting a producer can break a legitimate older consumer. Trace actual call sites, protocol schemas and tests before deciding which owner should change.

Ask which passing tests might conceal the bug. Mock-driven unit tests can certify an invented peer contract; a green build cannot certify hardware timing; a reviewed cloud handler cannot establish that field devices transmit valid payloads. Report these as unverified boundaries unless there is an observable failure mechanism and enough evidence for a finding. Propose the smallest discriminating test at the **missing** boundary, not a blanket demand for more tests.

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
