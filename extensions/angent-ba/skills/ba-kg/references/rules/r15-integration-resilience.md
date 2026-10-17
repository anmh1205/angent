# R15: External integration correctness and recovery

## Operational contract

For each external action record initiating event, contract revision, authentication, authorized fields, idempotency key, retry budget, timeout handling, backoff, duplicate message strategy and reconciliation owner.

## Checks before accepting an artifact

Test the difference among rejected business request, retriable transport error, accepted-but-unconfirmed operation and confirmed persistent state. A success HTTP status without read-back may not establish the side effect.

## Failure response

Pair webhook/event consumption with missed-event reconciliation and actual observability: latency, backlog, dead-letter, reprocessing and data freshness. Avoid inventing retry durations or SLOs.

## Grounded example

If a payment webhook arrives twice, writing the same refund twice is a failure even if both requests return 200. Verify dedupe and source-of-truth ownership.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
