#!/usr/bin/env python3
"""Compare source release identity against an actual provider observation.

Source structure alone never proves which plugin is activated in the host.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from package_unified import collect_entries, gateway_entries

ROOT = Path(__file__).resolve().parents[1]
PROBED_FILES = (
    "skills/angent/SKILL.md",
    "skills/angent/references/catalog/angent-authoring/SKILL.md",
    "skills/angent/references/catalog/ak-agentkit/SKILL.md",
    "skills/angent/references/catalog/angent-frontend-design/SKILL.md",
)


class ActivationError(ValueError):
    pass


def source_identity(root: Path = ROOT) -> dict[str, Any]:
    primary = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    secondary = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if primary.get("name") != "angent" or primary.get("name") != secondary.get("name"):
        raise ActivationError("source name mismatch")
    if primary.get("version") != secondary.get("version"):
        raise ActivationError("source manifest version mismatch")
    if primary["extensions"]["com.openai"]["interface"]["defaultPrompt"] != secondary["interface"]["defaultPrompt"]:
        raise ActivationError("bootstrap prompt mismatch")
    core = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    compiled = gateway_entries(collect_entries(root))
    registry = json.loads(compiled["hub/registry.json"])
    if len(core) != 12 or core & set(registry["published_skills"]):
        raise ActivationError("unexpected source/Core collision")
    expected = ["skills/angent/SKILL.md"]
    selected = set(PROBED_FILES)
    selected.add("skills/angent/references/hub/registry.json")
    selected.update("skills/angent/references/catalog/" + e["skills"][0] + "/SKILL.md"
                    for e in registry["extensions"])
    fingerprints = {name: hashlib.sha256(compiled[name]).hexdigest() for name in sorted(selected)}
    return {"name": "angent", "version": primary["version"],
            "expected_paths": expected, "probed_sha256": fingerprints}


def verify_provider(source: dict[str, Any], observed: dict[str, Any] | None) -> dict[str, Any]:
    result = {"source_version": source["version"], "expected_skills": len(source["expected_paths"]),
              "status": "PROVIDER_NOT_CHECKED", "evidence_level": "source_only"}
    if observed is None:
        return result
    if observed.get("name") != source["name"] or observed.get("version") != source["version"]:
        return {**result, "status": "IDENTITY_MISMATCH", "observed_version": observed.get("version")}
    if observed.get("complete_listing") is not True or not isinstance(observed.get("paths"), list):
        return {**result, "status": "INCOMPLETE_PROVIDER_INVENTORY"}
    paths = observed["paths"]
    if any(not isinstance(p, str) for p in paths) or len(paths) != len(set(paths)):
        return {**result, "status": "INVALID_PROVIDER_INVENTORY"}
    skillpaths = sorted(p for p in paths if p.startswith("skills/") and p.endswith("/SKILL.md") and p.count("/") == 2)
    if skillpaths != source["expected_paths"]:
        return {**result, "status": "CATALOG_MISMATCH", "observed_skills": len(skillpaths)}
    active = observed.get("other_active_plugins", [])
    if not isinstance(active, list) or any(not isinstance(x, str) for x in active):
        return {**result, "status": "INVALID_ACTIVE_PLUGIN_LIST"}
    if "angent-engineer-fallback" in active:
        return {**result, "status": "DUPLICATE_ENGINEER_ACTIVE"}
    fingerprints = observed.get("sha256_by_path")
    if not isinstance(fingerprints, dict) or any(x not in fingerprints for x in source["probed_sha256"]):
        return {**result, "status": "CATALOG_AND_VERSION_ONLY", "evidence_level": "provider_inventory"}
    if any(fingerprints.get(path) != sha for path, sha in source["probed_sha256"].items()):
        return {**result, "status": "SOURCE_CONTENT_MISMATCH", "evidence_level": "provider_content"}
    return {**result, "status": "MATCHED_PROBED_CONTENT",
            "evidence_level": "provider_inventory_and_selected_method_hashes",
            "note": "Not proof of every skill file or behavioral activation."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observed", type=Path, help="Normalized live provider observation JSON; do not commit it.")
    args = parser.parse_args()
    try:
        source = source_identity()
        observed = json.loads(args.observed.read_text(encoding="utf-8")) if args.observed else None
        print(json.dumps(verify_provider(source, observed), indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "INVALID_EVIDENCE", "error": str(exc)}))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
