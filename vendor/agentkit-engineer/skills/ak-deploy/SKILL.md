---
name: ak-deploy
description: Resolve the project's actual deployment target, perform an explicitly authorized provider deployment, verify the resulting endpoint, and record rollback/operational evidence.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Deploy — Portable Fallback

Deployment is a high-impact external effect.

Credentials, a configured CLI, or an existing provider project prove capability/state—not authority.

## Load progressively

- `references/environment-detection.md` — resolve provider/account/project/environment/artifact.
- `references/deployment-gate.md` — preflight and invocation-bound authority.
- `references/release-verification.md` — provider + user-facing endpoint evidence.

## Workflow

1. Resolve the exact target: provider, account/organization, project/service, environment, region/domain when material.
2. Identify the artifact/source/version that would be deployed.
3. Establish config, secrets, migrations, dependencies, cost/traffic impact, and rollback/forward-fix requirements.
4. Run required build/tests/release gates.
5. Build the concrete provider command/action.
6. **Immediately before invocation**, revalidate that current authority covers the resolved account/project/environment, material arguments, artifact, and outward-facing effect.
7. Deploy through project/provider-native tooling.
8. Verify provider release state and the actual URL/endpoint users/clients reach.
9. Record deployed version plus rollback/forward-fix/operational guidance in the project's established documentation when in scope.

If target resolution, provider state, or command arguments drift after approval, stop/revalidate rather than transferring old approval to the changed effect.

## Completion

A successful upload/CLI exit is transport evidence, not deployment completion.

Do not report success while provider state is still failed/ambiguous/converging unless the Contract explicitly defines an asynchronous handoff endpoint.

Do not infer production authority from staging authority.
