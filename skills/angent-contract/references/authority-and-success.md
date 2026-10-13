# Authority and success — act only inside the current task boundary

Capability, authority and correctness are separate questions.

A harness may be able to perform an action that the user did not authorize. An authorized action may still be the wrong decision.

## Effect classes

Reason about authority/risk in terms of effects:
- read-only observation;
- local reversible change;
- repository mutation;
- remote idempotent update;
- remote non-idempotent action;
- destructive/irreversible action;
- public communication/release/deployment;
- credential/privacy-sensitive operation.

Higher blast radius requires stronger evidence, containment and sometimes explicit approval.

## Authority expiry

Authority is scoped to the current task/instruction.

A previous session's permission to deploy, publish or delete does not automatically persist into a new task.

Continuity records work state; it cannot manufacture permission.

## Success state

Define completion by the requested world/artifact state, not by the mechanism used.

Examples:
- “PR merged with tests passing” is different from “commit pushed”.
- “all Jira tasks Done” is different from “code implemented”.
- “Notion book rewritten and read back” is different from “pages updated”.
- “deployment healthy” is different from “deploy command exited 0”.

## Evidence

Specify the strongest reasonable evidence:
- authoritative provider read-back;
- exact artifact/version;
- passing test/build;
- rendered output inspection;
- whole-scope coverage;
- user-visible state.

Do not require heavyweight evidence that cannot change the task verdict.
