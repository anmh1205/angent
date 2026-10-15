# Monorepo and build graph

Track:
- package ownership;
- dependency direction;
- shared config;
- build outputs;
- task cache inputs;
- generated code;
- versioning/publish boundaries.

Avoid circular dependencies hidden by path aliases.

When build caching is used, ensure cache keys include all material inputs.
