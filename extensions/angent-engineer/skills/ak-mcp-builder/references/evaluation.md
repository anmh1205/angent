# MCP evaluation

Evaluation should test the agent-facing contract, not only server unit functions.

## Representative cases

Include the relevant subset:
- tool discovery from descriptions;
- valid invocation;
- invalid/missing arguments;
- provider error;
- timeout/cancellation;
- authentication failure;
- read-only behavior;
- consequential write and read-back;
- duplicate/retry behavior;
- large/paginated result.

## What to inspect

- Did the model choose the right tool?
- Were arguments valid without hidden prompt knowledge?
- Is the result structured enough to continue reasoning?
- Are errors recoverable/actionable?
- Are write effects unambiguous?
- Is sensitive information kept out of schemas/results?
- Does the tool description distinguish it from overlapping tools?

## Version boundary

Record MCP SDK/protocol/client versions when behavior is version-sensitive.

Do not declare the server portable because it worked in only one client if the intended deliverable promises broader compatibility.
