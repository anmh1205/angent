# R17: Real runtime and provider evidence

## Operational contract

A tool's exit status or MCP acknowledgement is not the same as the user's desired outcome. Confirm actual created/modified objects, readable content, precise provider identity and the relevant postcondition.

## Checks before accepting an artifact

Before reporting a runnable feature, record the concrete tool/version, executed command, input revision, environment, count of operations, verified assertions and any skipped paths.

## Failure response

Never silently replace unavailable tools with simulated output; label offline source generation, candidate payload and mock fixtures honestly. For Figma, require real canvas node read-back; for Jira, read back actual issue fields.

## Grounded example

An editable Figma diagram cannot be claimed from `to_reqwise_payload.py`: it produces JSON candidate arguments only. A real connected plugin must create and then read the nodes.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
