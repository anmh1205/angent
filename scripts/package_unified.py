#!/usr/bin/env python3
"""Build one installable ANGENT plugin from Core and the Engineer source module.

Only Git-tracked files are packaged. Engineer source remains unchanged, while
its public Engineer Skills are projected into one discoverable root `skills/`.
Core-equivalent Skill identities are preserved as Engineer source but not exposed
as independently discoverable ANGENT Skills.
The nested Engineer plugin manifests are NOT emitted as installable plugins.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import zipfile

CORE_ROOT = "skills/"
ENGINEER_ROOT = "extensions/angent-engineer/"
ENGINEER_SKILLS = ENGINEER_ROOT + "skills/"
CORE_FILES = {"plugin.json", ".codex-plugin/plugin.json", "AGENTS.md"}
ENGINEER_SOURCE_MANIFEST = ENGINEER_ROOT + "source-manifest.json"
ENGINEER_PACKAGE_MANIFEST = ENGINEER_ROOT + "plugin.json"
ENGINEER_CODEX_MANIFEST = ENGINEER_ROOT + ".codex-plugin/plugin.json"
EXPECTED_CORE = 12
EXPECTED_ENGINEER = 103
EXPECTED_ROLES = 16
# Only canonical Core owns generic explanation. Keep upstream AgentKit identity
# under extensions/ but do not project it into the ANGENT Skill discovery root.
SUPPRESSED_PUBLIC_ENGINEER = frozenset({"ak-explain"})
EXPECTED_DISCOVERABLE = EXPECTED_CORE + EXPECTED_ENGINEER - len(SUPPRESSED_PUBLIC_ENGINEER)
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


class PackagingError(ValueError):
    pass


def _tracked(repo: Path) -> list[str]:
    try:
        raw = subprocess.check_output(
            ["git", "-C", str(repo), "ls-files", "-z"],
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise PackagingError("Requires a readable Git checkout") from exc
    return [p.decode("utf-8") for p in raw.split(b"\0") if p]


def _safe_file(repo: Path, relative: str) -> bytes:
    parts = PurePosixPath(relative)
    if parts.is_absolute() or ".." in parts.parts or "\\" in relative:
        raise PackagingError(f"Unsafe tracked path: {relative}")
    path = repo.joinpath(*parts.parts)
    if path.is_symlink() or not path.is_file():
        raise PackagingError(f"Unsupported tracked file/symlink: {relative}")
    return path.read_bytes()


def collect_entries(repo: Path, tracked: list[str] | None = None) -> dict[str, bytes]:
    paths = _tracked(repo) if tracked is None else tracked
    entries: dict[str, bytes] = {}
    source_core: set[str] = set()
    source_engineer: set[str] = set()
    for path in paths:
        if path in CORE_FILES or path.startswith(("assets/", CORE_ROOT)):
            target = path
            if re.fullmatch(r"skills/[^/]+/SKILL\.md", path):
                source_core.add(path.split("/")[1])
        elif path.startswith(ENGINEER_ROOT):
            if path == ENGINEER_CODEX_MANIFEST:
                continue
            if path == ENGINEER_PACKAGE_MANIFEST:
                target = ENGINEER_SOURCE_MANIFEST  # internal data, not a second plugin
            else:
                target = path
        else:
            continue

        data = _safe_file(repo, path)
        if target in entries:
            raise PackagingError(f"Duplicate package path: {target}")
        entries[target] = data
        if path.startswith(ENGINEER_SKILLS):
            skill_name = path[len(ENGINEER_SKILLS):].split("/", 1)[0]
            if skill_name not in SUPPRESSED_PUBLIC_ENGINEER:
                projected = CORE_ROOT + path[len(ENGINEER_SKILLS):]
                if projected in entries:
                    raise PackagingError(f"Skill projection collision: {projected}")
                entries[projected] = data
            if re.fullmatch(r"extensions/angent-engineer/skills/[^/]+/SKILL\.md", path):
                source_engineer.add(skill_name)

    if len(source_core) != EXPECTED_CORE or len(source_engineer) != EXPECTED_ENGINEER:
        raise PackagingError(f"Unexpected Skills: core={len(source_core)}, engineer={len(source_engineer)}")
    if not SUPPRESSED_PUBLIC_ENGINEER <= source_engineer:
        raise PackagingError("Suppressed Engineer Skill is missing from maintained source")
    if source_core & source_engineer:
        raise PackagingError(f"Core/Engineer Skill names overlap: {sorted(source_core & source_engineer)}")
    if ENGINEER_SOURCE_MANIFEST not in entries:
        raise PackagingError("Missing internal Engineer catalog manifest")
    for manifest in CORE_FILES:
        if manifest not in entries:
            raise PackagingError(f"Missing required plugin file: {manifest}")
    root_manifest = json.loads(entries["plugin.json"])
    codex_manifest = json.loads(entries[".codex-plugin/plugin.json"])
    if root_manifest.get("name") != "angent" or codex_manifest.get("name") != "angent":
        raise PackagingError("Unified plugin identity must be angent")
    if root_manifest.get("version") != codex_manifest.get("version"):
        raise PackagingError("Manifest version mismatch")
    if ENGINEER_PACKAGE_MANIFEST in entries or ENGINEER_CODEX_MANIFEST in entries:
        raise PackagingError("Nested installable manifests are forbidden")
    role_files = [p for p in entries if re.fullmatch(r"extensions/angent-engineer/agents/[^/]+\.md", p) and not p.endswith("/README.md")]
    if len(role_files) != EXPECTED_ROLES:
        raise PackagingError(f"Expected {EXPECTED_ROLES} Engineer role files, got {len(role_files)}")
    return entries


def verify_zip(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise PackagingError("Corrupt ZIP data")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise PackagingError("Duplicate ZIP entry")
        discovered = [p for p in names if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)]
        if len(discovered) != EXPECTED_DISCOVERABLE or any(
            f"skills/{name}/SKILL.md" in names for name in SUPPRESSED_PUBLIC_ENGINEER
        ):
            raise PackagingError(f"Wrong discoverable Skill count: {len(discovered)}")
        if ENGINEER_PACKAGE_MANIFEST in names or ENGINEER_CODEX_MANIFEST in names:
            raise PackagingError("Two separately installable manifests found")
        if not all(x in names for x in CORE_FILES | {ENGINEER_SOURCE_MANIFEST}):
            raise PackagingError("A required manifest or AGENTS.md is missing")
        for name in discovered:
            contents = archive.read(name).decode("utf-8")
            expected = name.split("/")[1]
            if not re.search(r"^name:\s*" + re.escape(expected) + r"\s*$", contents, re.M):
                raise PackagingError(f"Discovery/frontmatter mismatch: {name}")
        return {
            "plugin_name": json.loads(archive.read("plugin.json"))["name"],
            "core_skills": EXPECTED_CORE,
            "engineer_skills": EXPECTED_ENGINEER,
            "discoverable_engineer_skills": EXPECTED_ENGINEER - len(SUPPRESSED_PUBLIC_ENGINEER),
            "discoverable_skills": len(discovered),
            "engineer_roles": EXPECTED_ROLES,
            "zip_entries": len(names),
            "proof_level": "structural_only",
        }


def build(repo: Path, output: Path) -> dict[str, object]:
    entries = collect_entries(repo)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Deterministic, host-independent archive byte order, timestamps and permissions.
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, entries[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return verify_zip(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist/angent-chatgpt.zip"))
    args = parser.parse_args()
    repo = args.repo.resolve()
    output = args.output if args.output.is_absolute() else repo / args.output
    try:
        print(json.dumps(build(repo, output), sort_keys=True))
    except (PackagingError, OSError, json.JSONDecodeError) as exc:
        print(f"Unified package invalid: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
