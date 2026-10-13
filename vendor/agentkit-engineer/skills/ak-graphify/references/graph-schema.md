# Graph schema

Define a small typed schema before extraction.

Possible node types:
- file/symbol/module;
- concept/requirement;
- API/event/table;
- document/section;
- organization/entity.

Possible edges:
- imports/calls;
- reads/writes;
- depends-on;
- implements;
- satisfies/contradicts;
- references;
- derived-from.

Every important edge should carry provenance and confidence/observation type.
