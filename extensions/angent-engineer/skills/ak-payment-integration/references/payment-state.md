# Payment state model

Keep internal business state separate from provider transport state.

Possible internal states depend on the product, for example:

```text
created → awaiting_payment → paid → fulfilled
                     ↘ failed / expired
paid → refund_pending → refunded
```

Map provider event/status to internal transitions explicitly.

Record provider identifiers needed for reconciliation.

Never allow a client-supplied “paid” flag to drive fulfillment.
