#!/usr/bin/env python3
"""Build isolated ANGENT v1.5 packages from one tracked Core/Engineer source.

Never edit generated package files: they are deterministic projections. The
legacy scripts/package_unified.py remains the OpenAI compatibility builder.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
import zipfile

from package_unified import collect_entries, gateway_entries, PackagingError, FIXED_TIMESTAMP, EXPECTED_DISCOVERABLE, EXPECTED_OPENAI_DISCOVERABLE, EXPECTED_ENGINEER, FRONTEND_NAMES, SUPPRESSED_PUBLIC_ENGINEER

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ("local-agent", "gemini-web", "gemini-skills", "gemini-extension", "claude-code", "openai-plugin")
SKILL_PREFIX = {
    "local-agent": ".agents/skills/",
    "gemini-skills": ".gemini/skills/",
    "gemini-extension": "skills/",
    "claude-code": "skills/",
    "openai-plugin": "skills/",
}
TEMPLATES = {
    "local-agent": ("platforms/universal/AGENTS.md", "AGENTS.md"),
    "gemini-skills": ("platforms/gemini/GEMINI.md", "GEMINI.md"),
    "gemini-extension": ("platforms/gemini/GEMINI.md", "GEMINI.md"),
    "claude-code": ("platforms/claude/CLAUDE.md", "bootstrap/CLAUDE.md"),
    "openai-plugin": ("platforms/openai/AGENTS.md", "AGENTS.md"),
}
DOCS = {
    "local-agent": """# ANGENT — local agent workspace bundle

Copy this bundle's contents (including the hidden `.agents` directory) into
a project root that does **not** already contain `AGENTS.md`. For existing
projects, copy `.agents/` and merge `AGENTS.md` into your existing project
rules manually. Never overwrite project instructions.

The target agent must actually support the Agent Skills standard and
`.agents/skills` discovery. The `ak-*` fallback is already bundled;
16 role contracts under `extensions/` are not automatically spawned agents.
""",
    "gemini-skills": """# ANGENT — Gemini CLI workspace Skills

Copy `.gemini/` into the workspace root, then **merge** the provided
`GEMINI.md` into the project's own root `GEMINI.md` (or put it there only
if there is no existing file). Do not copy this file into `.gemini/GEMINI.md`
and assume that Gemini will treat it as a project-root context file.

Gemini CLI discovers workspace `.gemini/skills` or the interoperable
`.agents/skills`. Use `/skills list` and `/memory show` to check
discovery and persistent-context loading.
""",
    "gemini-extension": """# ANGENT — Gemini CLI extension

Install the directory containing `gemini-extension.json`:
`gemini extensions install /absolute/path/to/packages/gemini-extension`.

Extension `GEMINI.md` is loaded through `contextFileName`. Verify
Skills with `/skills list` and agents with the installed CLI's available
preview features. Engineer role projections do not promise native
subagent support in every Gemini version.
""",
    "claude-code": """# ANGENT — Claude Code plugin

Use `claude --plugin-dir /absolute/path/to/packages/claude-code`
or register this directory in a supported plugin marketplace.

The plugin installs Skills and projected agents. **Claude Code does not
automatically load a CLAUDE.md from the plugin root.** For the always-on
ANGENT baseline, merge `bootstrap/CLAUDE.md` with the *project's existing*
`CLAUDE.md`, preserving its instructions; do not overwrite that file.
No hooks or ambient auto-activation are implied by installing Skills alone.
""",
    "openai-plugin": """# ANGENT — single OpenAI Agent Plugin

Use this assembled plugin root (or its ZIP release) in the supported
ChatGPT/Codex plugin installation flow. There is exactly ONE publicly
discoverable Skill: `skills/angent/SKILL.md`. Core specialists, the
portable Engineer fallback and ANGENT Frontend visual methods are included
under `skills/angent/references/catalog/` for ANGENT to select. They are
not independently discoverable plugin Skills. Extension source and Engineer
role definitions remain available under `extensions/`.

Installing the package and verifying live provider activation are separate
steps. Use `scripts/verify_activation.py` with an actual observation
rather than assuming source version equals installed version.
""",
}


def _read_template(repo: Path, name: str) -> bytes:
    return (repo / name).read_bytes()


def _manifest(version: str, platform: str) -> bytes:
    if platform == "gemini":
        manifest = {
            "name": "angent", "version": version,
            "description": "ANGENT cognitive layer with portable Engineer Skills",
            "contextFileName": "GEMINI.md",
        }
    else:
        manifest = {
            "name": "angent", "version": version,
            "description": "ANGENT cognitive layer with portable Engineer Skills",
        }
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()


def _agent_projection(path: str, raw: bytes) -> bytes:
    """Remove source-only keys; do not claim unavailable tools or memory."""
    source = raw.decode("utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", source, re.S)
    if not match:
        raise PackagingError(f"Missing agent frontmatter: {path}")
    front = match.group(1)
    meta = {}
    for key in ("name", "description"):
        found = re.search(r"^" + key + r":\s*(.+?)\s*$", front, re.M)
        if not found:
            raise PackagingError(f"Missing agent {key}: {path}")
        meta[key] = found.group(1).strip()
    name = PurePosixPath(path).stem
    if meta["name"] != name or not re.fullmatch(r"[a-z][a-z0-9-]*", name):
        raise PackagingError(f"Invalid agent identity: {path}")
    if not meta["description"] or any(c in meta["description"] for c in ("\n", "\r")):
        raise PackagingError(f"Invalid agent description: {path}")
    # Quoted scalars avoid YAML syntax collisions; source body remains intact.
    header = "---\nname: " + name + "\ndescription: " + json.dumps(meta["description"], ensure_ascii=False) + "\n---\n"
    return (header + source[match.end():]).encode("utf-8")


def assemble(repo: Path, package: str, source: dict[str, bytes] | None = None) -> dict[str, bytes]:
    """A complete, independently extractable package; no source-tree symlinks."""
    if package not in PACKAGES:
        raise PackagingError(f"Unknown package: {package}")
    source = collect_entries(repo) if source is None else source
    if package == "gemini-web":
        return _assemble_gemini_web(source)
    primary = json.loads(source["plugin.json"])
    secondary = json.loads(source[".codex-plugin/plugin.json"])
    version = primary["version"]
    if primary["name"] != "angent" or version != secondary["version"]:
        raise PackagingError("OpenAI source manifests disagree")
    template, destination = TEMPLATES[package]
    projection = gateway_entries(source) if package == "openai-plugin" else source
    files: dict[str, bytes] = {}
    skills: set[str] = set()
    roles: set[str] = set()
    for path, content in projection.items():
        if path.startswith("skills/"):
            target = SKILL_PREFIX[package] + path[len("skills/"):]
            if re.fullmatch(r"skills/[^/]+/SKILL\.md", path):
                skills.add(path.split("/")[1])
        elif path.startswith("extensions/"):
            target = path  # portable relative support and selector paths survive
            if re.fullmatch(r"extensions/angent-engineer/agents/[^/]+\.md", path) and not path.endswith("/README.md"):
                roles.add(PurePosixPath(path).stem)
        elif package == "openai-plugin" and (path in ("plugin.json", ".codex-plugin/plugin.json") or path.startswith("assets/")):
            target = path
        else:
            continue
        if target in files:
            raise PackagingError(f"Collision: {target}")
        files[target] = content
    required = EXPECTED_OPENAI_DISCOVERABLE if package == "openai-plugin" else EXPECTED_DISCOVERABLE
    if len(skills) != required or len(roles) != 16 or SUPPRESSED_PUBLIC_ENGINEER & skills:
        raise PackagingError(f"Incomplete ANGENT catalog: {len(skills)} Skills, {len(roles)} roles")
    if package == "openai-plugin" and skills != {"angent"}:
        raise PackagingError("OpenAI must expose only ANGENT gateway")
    files[destination] = _read_template(repo, template)
    if package == "gemini-extension":
        files["gemini-extension.json"] = _manifest(version, "gemini")
    if package == "claude-code":
        files[".claude-plugin/plugin.json"] = _manifest(version, "claude")
    if package in ("gemini-extension", "claude-code"):
        for name in sorted(roles):
            path = f"extensions/angent-engineer/agents/{name}.md"
            files[f"agents/{name}.md"] = _agent_projection(path, source[path])
    if package == "openai-plugin":
        # No nested installable Engineer plugin. Keep original packaged source.
        assert "extensions/angent-engineer/plugin.json" not in files
        assert "extensions/angent-engineer/source-manifest.json" in files
        assert "plugin.json" in files and ".codex-plugin/plugin.json" in files
    files["INSTALL.md"] = DOCS[package].encode()
    return files


def _assemble_gemini_web(source: dict[str, bytes]) -> dict[str, bytes]:
    """Gemini Apps Web imports one root Skill, with reference texts inside it."""
    original = source["skills/angent/SKILL.md"].decode("utf-8")
    header = re.match(r"\A(---\n.*?\n---\n)", original, re.S)
    if header is None or re.search(r"^name:\s*angent\s*$", header.group(1), re.M) is None:
        raise PackagingError("Gemini Web requires ANGENT metadata in the root SKILL.md")
    intro = """
## Gemini Apps Web: one imported Skill

Gemini Apps imports one root ANGENT Skill. Its Core and task-specialist
reference texts under references/catalog are not independently discoverable.
Generic explanation remains owned by ANGENT Authoring and Reasoning.
The retired `ak-explain` identity remains only in the Engineer source
catalog outside this browser package. Load selected sections according to
the task using references/INDEX.md. Sixteen Engineer role definitions are
reference instructions, not running subagents.

Apply the complete ANGENT cognitive standard within the current conversation.
Use only tools provided by Gemini in this session. Do not claim that local
scripts, AgentKit CLI, durable files, delegation or network actions are
available just because their documentation is packaged here. Gemini Apps
does not support internet-dependent Skill scripts. The user must activate
ANGENT through Gemini Apps Skills when relevant; uploading the ZIP does not
guarantee automatic application to every conversation.

"""
    files: dict[str, bytes] = {"SKILL.md": (header.group(1) + intro + original[header.end():]).encode("utf-8")}
    names: set[str] = set()
    for path, payload in sorted(source.items()):
        if path.startswith("skills/"):
            if PurePosixPath(path).suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".sh", ".csv"}:
                continue
            relative = path[len("skills/"):]
            files["references/catalog/" + relative] = payload
            if re.fullmatch(r"[^/]+/SKILL\.md", relative):
                names.add(relative.split("/")[0])
            if path.startswith("skills/angent/references/"):
                files["references/" + path[len("skills/angent/references/"):]] = payload
        elif re.fullmatch(r"extensions/angent-engineer/agents/[a-z0-9-]+\.md", path):
            files["references/roles/" + PurePosixPath(path).name] = payload
    core = sorted(n for n in names if n.startswith("angent") and n not in FRONTEND_NAMES)
    engineer = sorted(n for n in names if n.startswith("ak-"))
    frontend = sorted(names & FRONTEND_NAMES)
    roles = sorted(p for p in files if re.fullmatch(r"references/roles/[a-z0-9-]+\.md", p))
    if len(core) != 12 or len(engineer) != EXPECTED_ENGINEER - len(SUPPRESSED_PUBLIC_ENGINEER) or frontend != sorted(FRONTEND_NAMES) or len(roles) != 16:

        raise PackagingError(f"Gemini Web library incomplete: {len(core)} Core, {len(engineer)} Engineer, {len(roles)} roles")
    index = ["# ANGENT reference library", "",
             "This is ONE imported Skill. Listed files are supporting reference",
             "instructions, not independently activated Gemini Web Skills.", "",
             "## Core", ""]
    index += [f"- [{n}](catalog/{n}/SKILL.md)" for n in core]
    index += ["", "## Frontend visual direction", ""]
    index += [f"- [{n}](catalog/{n}/SKILL.md)" for n in frontend]
    index += ["", "## Engineer", ""]
    index += [f"- [{n}](catalog/{n}/SKILL.md)" for n in engineer]
    index += ["", "## Roles", ""]
    index += [f"- [{PurePosixPath(p).stem}]({p.removeprefix('references/')})" for p in roles]
    index += ["", "Detailed references are beside the relevant skill files.", ""]
    files["references/INDEX.md"] = "\n".join(index).encode("utf-8")
    files["INSTALL.md"] = (
        "# Gemini Web upload instructions\n\n"
        "In gemini.google.com open Customize > Skills > Upload, and select\n"
        "angent-gemini-web.zip directly. Review the new ANGENT Skill and click\n"
        "Create. The ZIP has a root SKILL.md and reference material in\n"
        "references/. This does NOT load separate Skills. To use ANGENT,\n"
        "select it from Gemini Apps Skills in a conversation. Do not upload\n"
        "angent-gemini-skills.zip; that is the Gemini CLI workspace package.\n"
        "Official guide: https://support.google.com/gemini/answer/17094296\n"
    ).encode("utf-8")
    if sum(len(value) for value in files.values()) > 100_000_000:
        raise PackagingError("Gemini Apps upload exceeds 100 MB")
    return files


def _safe_target(base: Path, relative: str) -> Path:
    parts = PurePosixPath(relative)
    if parts.is_absolute() or ".." in parts.parts or "\\" in relative:
        raise PackagingError(f"Unsafe destination: {relative}")
    return base.joinpath(*parts.parts)


def _write_directory(root: Path, files: dict[str, bytes]) -> None:
    for name, content in sorted(files.items()):
        path = _safe_target(root, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def _zip(files: dict[str, bytes], path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, content in sorted(files.items()):
            entry = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(repo: Path, package_root: Path, dist_root: Path, selected: tuple[str, ...] = PACKAGES) -> dict[str, dict[str, object]]:
    """Build in staging, then install generated outputs; never follow symlinks."""
    source = collect_entries(repo)
    results = {}
    with tempfile.TemporaryDirectory(prefix="angent-packages-") as stage:
        tmp = Path(stage)
        for package in selected:
            files = assemble(repo, package, source)
            directory = tmp / "packages" / package
            _write_directory(directory, files)
            zipname = f"angent-{package}.zip"
            digest = _zip(files, tmp / "dist" / zipname)
            results[package] = {"files": len(files),
                                "skills": 1 if package in ("gemini-web", "openai-plugin") else EXPECTED_DISCOVERABLE,
                                "engineer_source_skills": EXPECTED_ENGINEER, "roles": 16, "sha256": digest}
        package_root.mkdir(parents=True, exist_ok=True)
        dist_root.mkdir(parents=True, exist_ok=True)
        for package in selected:
            target = package_root / package
            if target.is_symlink():
                raise PackagingError(f"Refusing symlink output: {target}")
            if target.exists():
                # Only named generated package directories are owned.
                if not target.is_dir():
                    raise PackagingError(f"Not a generated directory: {target}")
                shutil.rmtree(target)
            shutil.copytree(tmp / "packages" / package, target, symlinks=False)
            zipname = f"angent-{package}.zip"
            zip_target = dist_root / zipname
            if zip_target.is_symlink():
                raise PackagingError(f"Refusing symlink ZIP: {zip_target}")
            shutil.copy2(tmp / "dist" / zipname, zip_target)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Build all six platform packages")
    parser.add_argument("--only", choices=PACKAGES, help="Build one package")
    args = parser.parse_args()
    if args.only and args.all:
        parser.error("Choose either --all or --only")
    if not args.only and not args.all:
        parser.error("Specify --all or --only")
    selected = (args.only,) if args.only else PACKAGES
    try:
        report = build(ROOT, ROOT / "packages", ROOT / "dist", selected)
        print(json.dumps(report, indent=2, sort_keys=True))
    except (PackagingError, OSError, ValueError, KeyError) as exc:
        print(f"Package build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
