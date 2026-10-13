# Orchestration capture and recovery

Each job should have durable enough state to answer:

- what was attempted;
- runtime/agent selected;
- input scope and cwd;
- current status;
- evidence/artifacts produced;
- exit/error/timeout state;
- whether effects may have occurred;
- what remains runnable.

## Interruption

On resume:
1. load the job graph and captured states;
2. keep verified successful outputs;
3. revalidate runtime availability and mutable external state;
4. reconcile ambiguous effects before retrying;
5. redispatch only unfinished/interrupted jobs whose prerequisites remain valid.

Do not replay a consequential write merely because the previous response was lost.

## Failure

- timeout → retain bounded output, mark failed/interrupted and block dependents as needed;
- permission boundary → stop that job and surface the required authority;
- invalid runtime/tool invocation → re-discover rather than guessing;
- overlapping write ownership → sequence or isolate, then define integration explicitly.

Worker transcript retention is not a recovery mechanism.
