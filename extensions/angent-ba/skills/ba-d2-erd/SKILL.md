---
name: ba-d2-erd
description: Source-traceable BA d2-erd D2 modeling using tested JSON-to-D2 and real SVG rendering when available.
---

**Method origin:** maintained independent adaptation of the MIT Dev BA Kit /d2-erd skill, copyright 2026 Edward Ngo, https://github.com/nv-minh/dev-ba-kit/blob/main/skills/d2-erd/SKILL.md. Original ANGENT generator; no commercial AI4BA source included.

# D2 ERD with logical keys, constraints and field-accurate relations

## Outcome

Create a D2 sql_table logical data diagram, then use the actual D2 CLI to render a standalone SVG. An ERD is a statement of modeled business data; it does not imply that tables have been migrated, populated or deployed.

## Derive the model

1. Read the accepted SRS and data dictionary or inspect the actual versioned database schema if the request concerns current behavior. Decide whether entities are conceptual or actual tables.
2. Enumerate entities, ownership boundaries, identities, data fields, types, uniqueness and optionality. Do not fabricate SQL types when only conceptual information is known.
3. Assign stable entity IDs. Each non-external entity must declare a primary key. Model each attribute with name, type and optional key (pk, fk or unique).
4. Describe every relationship using actual source/target entities, the source and target field names and defensible cardinality. A foreign key without a corresponding target has no verified data meaning.
5. Prepare JSON with type erd, title, nodes (id, kind entity, label and attributes) and edges (from, to, fromField, toField and cardinality). Refer to extensions/angent-ba/examples/d2-erd.json.
6. Compile using ANGENT build_d2.py. It rejects duplicate fields, undeclared endpoints, missing primary keys, unsafe data type syntax and omitted cardinalities. It emits native D2 sql_table column type and PK/FK/unique constraints.
7. Render the actual source through an installed D2 CLI. Read back SVG table labels and column rows and compare the rendering with the accepted semantic model.
8. Inspect privacy classification, tenancy/data ownership, null semantics, lifecycle constraints and differences between the conceptual diagram and real migration files if material.

## Real commands

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-erd.json --output output/erd.d2

    python extensions/angent-ba/scripts/build_d2.py INPUT.json --output output/erd.d2 --svg output/erd.svg --d2 PATH_TO_D2

## Acceptance and limits

No orphan relationship, duplicated field, missing PK for ordinary entities, unsupported constraint or unsourced cardinality. SVG success requires zero renderer errors and legible keys/links. Diagram validity does not certify normalization, physical migrations or deployment. The original D2 sql_table syntax is documented at https://d2lang.com/tour/sql-tables/.

## ANGENT responsibility

Root chooses specialist use; BA supplies entity and relationship reasoning; Execution controls authorized files/provider changes; Quality checks results. Never create or modify a database because an ERD was requested.
