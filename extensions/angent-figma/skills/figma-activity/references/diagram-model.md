# Figma portable diagram representation

Use `type`, `nodes`, `edges`, `metadata`, and `source_refs` as a narrow exchange model. Node IDs must be stable for same-meaning objects; edges use `from` and `to` stable IDs. Include optional `lane`, `guard`, `shape` and `kind` for semantic meaning. Do not fabricate Figma node IDs from these portable IDs.

```json
{
  "type": "activity",
  "nodes": [
    {"id":"start","kind":"start","label":"Start"},
    {"id":"verify","kind":"task","label":"Verify available seat","lane":"System"},
    {"id":"end","kind":"end","label":"Booking complete"}
  ],
  "edges":[{"from":"start","to":"verify"},{"from":"verify","to":"end","guard":"seat available"}],
  "metadata":{"status":"proposed","artifact_id":"FLOW-CINEMO-01"},
  "source_refs":["FR-BOOK-01"]
}
```

Runtime validation under `extensions/angent-figma/scripts/validate_diagram_model.py` can detect graph inconsistencies but cannot establish layout quality. Native Figma mutations require a live connector, active file permissions and target read-back.
