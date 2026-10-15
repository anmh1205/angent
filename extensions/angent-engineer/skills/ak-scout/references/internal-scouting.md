# Internal scouting with optional delegated workers

Delegation is an optimization, not a requirement.

## Use delegation when

- the harness exposes a real worker/subagent capability;
- scopes can be separated cleanly;
- each worker has useful independent work;
- parallelism meaningfully reduces context/time cost.

Otherwise scout directly in the main agent.

## Partition work

Good partitions:
- independent packages/modules;
- frontend vs backend ownership;
- implementation vs tests/config;
- separate hypotheses requiring different code paths.

Bad partitions:
- several workers all searching the same repository for the same keyword;
- workers with vague “inspect everything” prompts;
- parallel writes during a read-only scouting phase.

## Worker brief

Give:
- exact question;
- exact scope;
- relevant AGENTS.md constraints;
- requested evidence;
- what not to modify;
- expected concise return format.

## Synthesis

The main agent combines worker findings by:
- deduplicating repeated evidence;
- distinguishing independent confirmation from shared assumptions;
- preserving contradictions;
- building one file/flow/ownership map.

A worker summary is evidence, not automatic authority.
