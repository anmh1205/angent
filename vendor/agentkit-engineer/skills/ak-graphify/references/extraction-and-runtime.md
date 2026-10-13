# Graph extraction and runtime

## Code

Prefer parser/AST/symbol-index relationships for:
- imports;
- calls;
- inheritance/implementation;
- definitions/usages;
- file/module ownership.

Text matching can supplement but should not masquerade as semantic certainty.

## Documents

Extract named concepts/requirements/relations with source location.

Semantic edges should carry provenance and confidence.

## Media

Only extract from audio/video/images when the active runtime actually has a suitable local or authorized multimodal path.

## Incremental updates

For large graphs, track source hashes/versions so unchanged artifacts do not need full reprocessing.

An incremental graph must remove/update stale nodes/edges when source changes.

## MCP exposure

A graph server may expose operations such as:
- query/search;
- get node;
- neighbors;
- shortest path / impact path.

Do not require MCP when local direct graph queries are sufficient.
