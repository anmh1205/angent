# ADK agent architecture

Keep:
- agent instruction/role;
- tools;
- session state;
- memory;
- workflow/agent delegation;
- external protocol integration

as explicit concerns.

Use workflow agents when control flow is part of the application contract.

Use specialist agents when context/expertise separation creates value.

Avoid recursive delegation with unclear stop/ownership.
