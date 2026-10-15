# CTI case state

A long investigation needs durable case state independent of one chat session.

Store the relevant subset of:
- case question/scope;
- entities with aliases and identity uncertainty;
- findings with unique IDs;
- source/provenance;
- timestamps;
- confidence/status;
- relationships;
- timeline;
- collection gaps;
- next investigative question.

## Resume

On resume:
1. load current case state;
2. re-check stale-sensitive public evidence when it matters;
3. keep historical observations with their original dates;
4. distinguish changed reality from a prior collection error.

## Finding states

Useful states:
- observed;
- inferred;
- contradicted;
- stale;
- unverified;
- resolved/mitigated.

Do not silently overwrite old evidence when a finding changes; preserve enough history to explain the transition.
