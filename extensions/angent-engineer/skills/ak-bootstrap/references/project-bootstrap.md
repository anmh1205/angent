# Project bootstrap workflow

## Destination safety

Before writing:
- inspect the destination;
- distinguish empty/new workspace from an existing project;
- preserve existing Git/branch conventions and user files;
- do not overwrite unrelated content as "scaffolding".

## Research and decisions

Research only choices that can change implementation materially:
- runtime/framework/database;
- deployment constraints;
- auth/security model;
- platform/API compatibility;
- design/interface requirements.

Record the selected choice, decisive evidence, trade-offs and reconsideration trigger.

## Design evidence

For visual products, establish enough design system/layout/interaction guidance that implementation is not guessing.

For non-visual products, establish the equivalent interface contract: commands, routes, schemas, public API/tool behavior.

## Planning and implementation

Use the smallest planning boundary that protects the accepted bootstrap contract:
1. pass the accepted brief, research, stack, design, interface and acceptance evidence to Cook;
2. Cook decomposes its own runnable implementation units and owns coding, tests and code review;
3. use a separate Plan Skill **when** risk, unresolved design, migration, multi-owner work or the user-requested approval warrants a durable reviewable plan before coding;
4. whether planning is separate or within Cook, do not implement through an unapproved material design choice or overwrite an existing project.

The transferable skill is knowing **when a separate plan contributes a decision/verification boundary**. Do not make two planning passes a ritual simply because two Skills exist.

Do not duplicate Plan/Cook bodies inside Bootstrap.

## Thin vertical proof

Before expanding optional framework surface, prove one real path end to end:
- startup/build;
- one meaningful user/client flow;
- persistence/network/tool boundary if part of the product;
- project-native test/verification path.

This catches stack incompatibility earlier than broad boilerplate generation.

## Review and UX/AX

After implementation, independently review production risk.

For a web/UI surface, run the available UX/accessibility/AI-experience review capability when it is part of the accepted workflow and capability exists. Re-review material resulting changes.

Do not apply UI-specific ceremony to CLI/API/library projects.

## Documentation and onboarding

Update the smallest authoritative docs needed for:
- setup/run/test;
- architecture/public contracts;
- environment/config requirements;
- known constraints/decisions.

Guide the user through any manual credentials or external setup without requesting secrets into ordinary chat/artifacts.

## Release boundary

Local verification and live release are different endpoints.

Deploy/publish/provision only when:
- included in the accepted contract;
- current provider/target is identified;
- authority covers the effect;
- post-effect verification/rollback path is available.

## Completion

Report:
- implemented surfaces;
- verification performed;
- review status;
- setup/onboarding;
- live/local endpoint status;
- unresolved decisions/risks.

Avoid mandatory journaling when no reusable historical lesson exists.
