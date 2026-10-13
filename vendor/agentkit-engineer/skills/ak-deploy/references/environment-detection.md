# Deployment environment detection

Use evidence in this order:
- explicit current user target;
- AGENTS.md/project deployment docs;
- provider config files;
- CI/CD workflows;
- connected provider state.

Resolve:
- environment name;
- provider/account/project;
- region;
- artifact/image/build source;
- domain/endpoint;
- migration/config dependencies.

Never deploy to “the obvious default” when multiple environments exist and target is material.
