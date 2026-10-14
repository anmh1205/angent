# Page-builder contract

A reusable page builder needs explicit contracts for:

- block identity/version and props/content schema;
- composition/order/nesting rules;
- content/data bindings;
- editor state and validation;
- persistence and migrations;
- draft versus preview versus published state;
- responsive/touch editing;
- permissions and publication authority;
- renderer parity between editor/preview/public page;
- project-specific operator/agent interface when requested.

Prefer existing application components and tokens.

Do not fork a second design system merely to make blocks editor-friendly.

## Verification

Use a representative real page:
1. add/edit/reorder a real block;
2. persist and reload it;
3. inspect preview;
4. verify target responsive states;
5. verify publication boundary separately;
6. check the operator/agent interface if one was requested.

Missing browser/provider access means the corresponding state is unverified, not complete.
