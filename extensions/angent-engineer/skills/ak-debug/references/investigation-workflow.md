# Investigation workflow

Use this for multi-component, intermittent, CI, performance, or otherwise long-running incidents.

## 1. Establish the incident boundary

Record:
- impacted behavior;
- unaffected behavior;
- version/environment;
- onset/change window when known;
- user-visible severity;
- current reproducibility.

## 2. Gather evidence by boundary

Possible evidence:
- source and tests;
- application/runtime logs;
- CI logs;
- network/database state;
- metrics/profiles;
- configuration;
- provider state.

Gather only evidence that can change the causal model.

## 3. Preserve attempts

If a probe/fix fails, record:
- hypothesis tested;
- change/probe performed;
- observed result;
- what the result weakens/rejects;
- next discriminator.

Repeated failed attempts should trigger model review, not a fixed-count ritual that automatically stops the task.

## 4. Performance cases

For performance defects:
- measure before changing;
- locate the dominant resource/time boundary;
- distinguish CPU, I/O, allocation, lock/contention, network, database, and algorithmic causes;
- re-measure the same workload after intervention.

## 5. CI-only failures

Compare:
- environment/runtime version;
- filesystem/case/permissions;
- timing/concurrency;
- dependency lock state;
- secret/config availability;
- test ordering/isolation.

Do not “fix CI” by weakening a test unless the test itself is proven wrong.

## 6. Coordination

Use Continuity for durable investigation state.

Use multiple workers only for disjoint evidence sources and return concise evidence/artifact pointers rather than full transcripts.
