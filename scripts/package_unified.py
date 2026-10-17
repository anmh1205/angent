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
import posixpath
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import zipfile

# Also support importlib loading of this standalone builder in validation tests.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from hub_registry import build_registry, method_entries, HubError

CORE_ROOT = "skills/"
ENGINEER_ROOT = "extensions/angent-engineer/"
ENGINEER_SKILLS = ENGINEER_ROOT + "skills/"
FRONTEND_ROOT = "extensions/angent-frontend/"
FRONTEND_SKILLS = FRONTEND_ROOT + "skills/"
FRONTEND_NAMES = frozenset({"angent-frontend-design"})
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
EXPECTED_DISCOVERABLE = EXPECTED_CORE + EXPECTED_ENGINEER - len(SUPPRESSED_PUBLIC_ENGINEER) + len(FRONTEND_NAMES)
EXPECTED_OPENAI_DISCOVERABLE = 1
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
# Package text has canonical LF bytes even in a CRLF working checkout. Binary
# resources are copied byte-for-byte; local tracked edits remain build inputs.
TEXT_SUFFIXES = frozenset({".md", ".json", ".py", ".yaml", ".yml", ".txt",
                           ".sh", ".csv", ".toml", ".svg"})


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
    if not parts.parts or parts.is_absolute() or ".." in parts.parts or "\\" in relative or ":" in relative:
        raise PackagingError(f"Unsafe tracked path: {relative}")
    root = repo.resolve(strict=True)
    path = root
    for part in parts.parts:
        path = path / part
        info = path.lstat()
        # Reject every symlink/reparse point, including Windows junction parents.
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise PackagingError(f"Unsupported tracked file/symlink: {relative}")
    if not path.is_file() or not path.resolve(strict=True).is_relative_to(root):
        raise PackagingError(f"Tracked file escapes source checkout: {relative}")
    payload = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        try:
            payload = payload.decode("utf-8").replace("\r\n", "\n").encode("utf-8")
        except UnicodeError as exc:
            raise PackagingError(f"Package text must be UTF-8: {relative}") from exc
    return payload


def collect_entries(repo: Path, tracked: list[str] | None = None) -> dict[str, bytes]:
    """Keep authoritative Core/kit source and derive public Skill projections."""
    paths = _tracked(repo) if tracked is None else tracked
    entries: dict[str, bytes] = {}
    core_names: set[str] = set()
    for path in paths:
        if path in CORE_FILES or path.startswith(("assets/", CORE_ROOT, "hub/")):
            if path in {"hub/registry.json", "hub/catalog.md", "hub/bindings.json"} or path.startswith("hub/methods/"):
                raise PackagingError("Hub registry/cards/bindings must be generated, not committed")
            target = path
            if re.fullmatch(r"skills/[^/]+/SKILL\.md", path):
                core_names.add(path.split("/")[1])
        elif path.startswith("extensions/"):
            if re.fullmatch(r"extensions/[^/]+/\.codex-plugin/plugin\.json", path):
                continue
            if re.fullmatch(r"extensions/[^/]+/plugin\.json", path):
                target = path.rsplit("/", 1)[0] + "/source-manifest.json"
            else:
                target = path
        else:
            continue
        data = _safe_file(repo, path)
        if target in entries:
            raise PackagingError(f"Duplicate package path: {target}")
        entries[target] = data

    if len(core_names) != EXPECTED_CORE or "angent" not in core_names:
        raise PackagingError(f"Unexpected Core skill catalog: {sorted(core_names)}")
    if not CORE_FILES <= entries.keys():
        raise PackagingError("Missing root plugin manifest or AGENTS.md")
    try:
        registry = build_registry(entries)
    except HubError as exc:
        raise PackagingError(str(exc)) from exc

    # Project arbitrary validated Kit Skills; kit source and roles stay intact.
    for ext in registry["extensions"]:
        for skill in ext["skills"]:
            source_prefix = f"extensions/{ext['id']}/skills/{skill}/"
            for path, content in list(entries.items()):
                if path.startswith(source_prefix):
                    target = "skills/" + path[len(f"extensions/{ext['id']}/skills/"):]
                    if target in entries:
                        raise PackagingError(f"Skill collision: {target}")
                    entries[target] = content
    entries["hub/registry.json"] = (json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    entries.update(method_entries(entries))
    entries["hub/bindings.json"] = bindings(registry, "hub", "skills", "broad")
    try:
        root = json.loads(entries["plugin.json"])
        codex = json.loads(entries[".codex-plugin/plugin.json"])
    except (ValueError, UnicodeError) as exc:
        raise PackagingError("Invalid root manifest") from exc
    if root.get("name") != "angent" or codex.get("name") != "angent" or root.get("version") != codex.get("version"):
        raise PackagingError("One ANGENT plugin identity/version is required")
    for ext in registry["extensions"]:
        if f"extensions/{ext['id']}/plugin.json" in entries or f"extensions/{ext['id']}/.codex-plugin/plugin.json" in entries:
            raise PackagingError("Nested installable kit manifest")
    return entries


def bindings(registry: dict, hub_path: str, skill_path: str, profile: str,
             role_prefix: str | None = None) -> bytes:
    """Resolve method resources in the actual artifact, relative to this Hub copy."""
    data = {"profile": profile, "methods": {
        name: posixpath.relpath(f"{skill_path}/{name}/SKILL.md", hub_path)
        for name in registry["published_skills"]}, "roles": {
        f"{ext['id']}:{role}": posixpath.relpath(
            f"{role_prefix}/{ext['id']}/{role}.md" if role_prefix else
            f"extensions/{ext['id']}/agents/{role}.md", hub_path)
        for ext in registry["extensions"] for role in ext["roles"]}}
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()


def gateway_entries(source: dict[str, bytes]) -> dict[str, bytes]:
    """One OpenAI Root gateway, with all Core and kit methods as internal references."""
    root = "skills/angent/"
    if root + "SKILL.md" not in source or "hub/registry.json" not in source:
        raise PackagingError("Missing ANGENT Root or Hub registry")
    registry = json.loads(source["hub/registry.json"])
    extension_names = set(registry["published_skills"])
    core_names = {p.split("/")[1] for p in source
                  if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)} - extension_names
    if len(core_names) != EXPECTED_CORE or "angent" not in core_names:
        raise PackagingError("Core/extension inventory mismatch")
    output: dict[str, bytes] = {}
    names = set()
    for path, content in sorted(source.items()):
        if path.startswith("skills/") and not path.startswith(root):
            relative = path[len("skills/"):]
            target = root + "references/catalog/" + relative
            if relative.endswith("/SKILL.md") and relative.count("/") == 1:
                names.add(relative.split("/")[0])
        else:
            target = path
        if target in output:
            raise PackagingError(f"Gateway collision: {target}")
        output[target] = content
    if names != (core_names - {"angent"}) | extension_names:
        raise PackagingError("Incomplete Hub gateway library")

    suffix = """
## ANGENT Hub gateway

This is the only discoverable Skill in the OpenAI plugin. First apply the
full ANGENT cognitive baseline. When specialist work adds value, read
`references/hub/routing.md` and search `references/hub/catalog.md` (or its
read-only `discover.py` helper). Inspect the candidate's method card and
`references/hub/bindings.json` before loading it, then use
the selected `references/catalog/<skill>/SKILL.md` as internal guidance.
Kit Adapters translate expert methods but never control reasoning,
authorization, final Quality or tool permissions.

The static package does not suppress independently installed plugins
or force ANGENT activation on every host turn. A bundled Skill or role is
not proof of native CLI, subagent, tool or filesystem capability.
"""
    output[root + "SKILL.md"] = source[root + "SKILL.md"] + suffix.encode()
    for p, data in sorted(source.items()):
        if p.startswith("hub/"):
            output[root + "references/" + p] = data
    output["hub/bindings.json"] = bindings(registry, "hub", root + "references/catalog", "gateway", root + "references/roles")
    output[root + "references/hub/bindings.json"] = bindings(
        registry, root + "references/hub", root + "references/catalog", "gateway", root + "references/roles")

    index = ["# ANGENT internal capability catalog", "",
             "ANGENT Root selects optional methods; Core keeps final responsibility.",
             "Start with [Hub routing](hub/routing.md) and [capability registry](hub/registry.json).",
             "", "## Core", ""]
    index.extend(f"- [{n}](catalog/{n}/SKILL.md)" for n in sorted(core_names - {"angent"}))
    for ext in registry["extensions"]:
        index += ["", f"## {ext['name']} ({ext['id']})", "",
                  "These are specialist methods, not independently activated agents.", ""]
        index.extend(f"- [{n}](catalog/{n}/SKILL.md)" for n in ext["skills"])
        if ext["roles"]:
            index += ["", "### Optional role references (not running agents)", ""]
            for role in ext["roles"]:
                src = f"extensions/{ext['id']}/agents/{role}.md"
                target = root + f"references/roles/{ext['id']}/{role}.md"
                output[target] = source[src]
                index.append(f"- [{role}](roles/{ext['id']}/{role}.md)")
    output[root + "references/INDEX.md"] = ("\n".join(index) + "\n").encode()
    discovered = [p for p in output if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)]
    if discovered != [root + "SKILL.md"]:
        raise PackagingError(f"Unexpected discoverable Skill: {discovered}")
    return output


def verify_zip(path: Path) -> dict[str, object]:
    """Validate actual packaged methods against the complete generated inventory."""
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise PackagingError("Corrupt ZIP data")
        names = archive.namelist()
        present = set(names)
        if len(names) != len(present):
            raise PackagingError("Duplicate ZIP entries")
        discovered = sorted(p for p in names if re.fullmatch(r"skills/[^/]+/SKILL\.md", p))
        if discovered != ["skills/angent/SKILL.md"]:
            raise PackagingError(f"OpenAI requires one ANGENT gateway, got {discovered}")
        registry_path = "hub/registry.json"
        if registry_path not in present:
            raise PackagingError("Missing generated Hub registry")
        registry = json.loads(archive.read(registry_path))
        extensions = registry["extensions"]
        published = {name for ext in extensions for name in ext["skills"]}
        if len(published) != sum(len(ext["skills"]) for ext in extensions):
            raise PackagingError("Overlapping public Skill identities")
        if published != set(registry["published_skills"]):
            raise PackagingError("Hub registry inventory mismatch")
        required = {"skills/angent/references/INDEX.md",
                    "skills/angent/references/hub/routing.md",
                    "skills/angent/references/hub/registry.json",
                    "skills/angent/references/catalog/angent-reasoning/SKILL.md",
                    "plugin.json", ".codex-plugin/plugin.json", "AGENTS.md"}
        for ext in extensions:
            required.add(f"extensions/{ext['id']}/extension.json")
            for skill in ext["skills"]:
                required.add(f"hub/methods/{skill}.json")
                required.add(f"skills/angent/references/hub/methods/{skill}.json")
                required.add(f"skills/angent/references/catalog/{skill}/SKILL.md")
                required.add(f"extensions/{ext['id']}/skills/{skill}/SKILL.md")
            for role in ext["roles"]:
                required.add(f"skills/angent/references/roles/{ext['id']}/{role}.md")
        if not required <= present:
            raise PackagingError(f"Missing packaged Hub methods: {sorted(required - present)[:10]}")
        for hub_path in ("hub", "skills/angent/references/hub"):
            binding = json.loads(archive.read(hub_path + "/bindings.json"))
            if set(binding["methods"]) != published:
                raise PackagingError("Incomplete method bindings")
            for entry, relative in binding["methods"].items():
                resolved = posixpath.normpath(hub_path + "/" + relative)
                expected = f"skills/angent/references/catalog/{entry}/SKILL.md"
                if resolved != expected or resolved not in present:
                    raise PackagingError(f"Wrong gateway binding: {entry}")
        if any(re.fullmatch(r"extensions/[^/]+/plugin\.json", p) or
               re.fullmatch(r"extensions/[^/]+/\.codex-plugin/plugin\.json", p)
               for p in present):
            raise PackagingError("Nested installable kit plugin manifests are forbidden")
        for name in discovered:
            contents = archive.read(name).decode("utf-8")
            expected = name.split("/")[1]
            if not re.search(r"^name:\s*" + re.escape(expected) + r"\s*$", contents, re.M):
                raise PackagingError(f"Discovery/frontmatter mismatch: {name}")
        engineer = next((e for e in extensions if e["id"] == "angent-engineer"), None)
        frontend = next((e for e in extensions if e["id"] == "angent-frontend"), None)
        return {
            "plugin_name": json.loads(archive.read("plugin.json"))["name"],
            "core_skills": EXPECTED_CORE,
            "engineer_skills": engineer["source_skill_count"] if engineer else 0,
            "discoverable_engineer_skills": 0,
            "internal_engineer_methods": len(engineer["skills"]) if engineer else 0,
            "internal_frontend_methods": len(frontend["skills"]) if frontend else 0,
            "discoverable_skills": len(discovered),
            "engineer_roles": len(engineer["roles"]) if engineer else 0,
            "internal_specialist_methods": len(published),
            "extensions": [e["id"] for e in extensions],
            "capability_count": len(registry["capabilities"]),
            "zip_entries": len(names),
            "proof_level": "structural_only",
        }


def build(repo: Path, output: Path) -> dict[str, object]:
    entries = gateway_entries(collect_entries(repo))
    output.parent.mkdir(parents=True, exist_ok=True)
    # Deterministic, host-independent archive byte order, timestamps and permissions.
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
            info.create_system = 3  # Canonical Unix metadata, independent of the build host.
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
