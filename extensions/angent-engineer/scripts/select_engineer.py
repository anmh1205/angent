#!/usr/bin/env python3
"""Select native AgentKit Engineer or ANGENT's portable fallback.

This helper is intentionally small and read-only. It does not install, enable,
disable, repair, or mutate either AgentKit or an agent harness.

The active harness/adapter is responsible for determining whether native
Engineer is actually usable in the current session. AgentKit CLI presence or a
cached Skill tree is not enough to prove that.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any

from verify_port import audit_port


SCHEMA_VERSION = 1
KIND = "angent.engineer_selection"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PLUGIN_FIELDS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
PLUGIN_NAME = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")

EXPECTED_SKILLS = frozenset([
    "ak-advise",
    "ak-agent-browser",
    "ak-agentize",
    "ak-agentkit",
    "ak-ai-artist",
    "ak-ai-multimodal",
    "ak-ak",
    "ak-ask",
    "ak-autoresearch",
    "ak-backend-development",
    "ak-better-auth",
    "ak-bootstrap",
    "ak-brainstorm",
    "ak-bro",
    "ak-chrome-profile",
    "ak-code-review",
    "ak-codex-goal",
    "ak-coding-level",
    "ak-context-engineering",
    "ak-cook",
    "ak-copywriting",
    "ak-cti-expert",
    "ak-databases",
    "ak-debug",
    "ak-deep-swe",
    "ak-deploy",
    "ak-design",
    "ak-devops",
    "ak-diagram",
    "ak-docs",
    "ak-docs-seeker",
    "ak-document-skills",
    "ak-enhance-ux-ax",
    "ak-excalidraw",
    "ak-explain",
    "ak-fable-thinking",
    "ak-find-skills",
    "ak-fix",
    "ak-folder-context",
    "ak-frontend-design",
    "ak-frontend-development",
    "ak-git",
    "ak-github",
    "ak-gkg",
    "ak-goal-warmup",
    "ak-google-adk-python",
    "ak-graphify",
    "ak-handoff",
    "ak-help",
    "ak-hyperframes",
    "ak-interview-docs",
    "ak-issue-to-plan",
    "ak-journal",
    "ak-llms",
    "ak-loop",
    "ak-markdown-novel-viewer",
    "ak-mcp-builder",
    "ak-media-processing",
    "ak-mermaidjs-v11",
    "ak-mintlify",
    "ak-mobile-development",
    "ak-orchestrate",
    "ak-page-builder",
    "ak-payment-integration",
    "ak-plan",
    "ak-plans-kanban",
    "ak-predict",
    "ak-preview",
    "ak-problem-solving",
    "ak-project-management",
    "ak-project-organization",
    "ak-react-best-practices",
    "ak-remotion",
    "ak-repomix",
    "ak-research",
    "ak-research-prompt",
    "ak-retro",
    "ak-review-pr",
    "ak-scenario",
    "ak-scout",
    "ak-security",
    "ak-shader",
    "ak-ship",
    "ak-shopify",
    "ak-show-off",
    "ak-skill-creator",
    "ak-sowat",
    "ak-stitch",
    "ak-sumup",
    "ak-tanstack",
    "ak-team",
    "ak-tech-graph",
    "ak-test",
    "ak-threejs",
    "ak-ui-styling",
    "ak-ui-ux-pro-max",
    "ak-vibe",
    "ak-watzup",
    "ak-web-frameworks",
    "ak-web-testing",
    "ak-webmcp",
    "ak-worktree",
    "ak-xia"
])
EXPECTED_AGENT_ROLES = frozenset([
    "advisor",
    "brainstormer",
    "code-reviewer",
    "code-simplifier",
    "debugger",
    "docs-manager",
    "explore",
    "fullstack-developer",
    "git-manager",
    "journal-writer",
    "kongming",
    "planner",
    "project-manager",
    "researcher",
    "tester",
    "ui-ux-designer"
])
EXPECTED_CATALOG_IDENTITY_SHA256 = "439bc625174a6e9e780f8f464b0129ccf9bfcb4ba5b63d7fa3734d0e05541ddc"


def _catalog_identity_digest(skills: set[str] | frozenset[str], agents: set[str] | frozenset[str]) -> str:
    payload = {
        "agent_roles": sorted(agents),
        "skills": sorted(skills),
    }
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _portable_manifest_valid(manifest: Any, expected_name: str) -> bool:
    if not isinstance(manifest, dict):
        return False
    if set(manifest) - PLUGIN_FIELDS:
        return False
    if manifest.get("$schema") != PLUGIN_SCHEMA:
        return False

    name = manifest.get("name")
    if (
        not isinstance(name, str)
        or name != expected_name
        or not 1 <= len(name) <= 64
        or not PLUGIN_NAME.fullmatch(name)
        or "--" in name
        or ".." in name
    ):
        return False

    for key in ("version", "description", "homepage", "repository", "license"):
        if key in manifest and not isinstance(manifest[key], str):
            return False

    author = manifest.get("author")
    if author is not None:
        if not isinstance(author, dict) or set(author) - {"name", "email", "url"}:
            return False
        if any(not isinstance(value, str) for value in author.values()):
            return False

    keywords = manifest.get("keywords")
    if keywords is not None and (
        not isinstance(keywords, list)
        or any(not isinstance(value, str) for value in keywords)
    ):
        return False

    if "extensions" in manifest and not isinstance(manifest["extensions"], dict):
        return False

    return True



def _run(command: list[str], timeout: float) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "completed": False,
            "exit_code": None,
            "error": type(exc).__name__,
        }

    return {
        "completed": True,
        "exit_code": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def _json_from_stdout(result: dict[str, Any]) -> Any | None:
    if not result.get("completed"):
        return None
    raw = result.get("stdout", "")
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def _detect_agentkit(doctor_mode: str, timeout: float) -> dict[str, Any]:
    ak = shutil.which("ak")
    info: dict[str, Any] = {
        "cli_present": bool(ak),
        "cli_path": ak,
        "version": None,
        "doctor": {
            "mode": doctor_mode,
            "completed": False,
            "healthy": None,
            "summary": None,
        },
    }

    if not ak:
        return info

    version_result = _run([ak, "--version"], timeout)
    if version_result.get("completed") and version_result.get("exit_code") == 0:
        version_text = version_result.get("stdout") or version_result.get("stderr")
        info["version"] = version_text or None

    if doctor_mode == "none":
        return info

    command = [ak, "doctor"]
    if doctor_mode == "offline":
        command.append("--offline")
    command.append("--json")

    doctor_result = _run(command, timeout)
    doctor: dict[str, Any] = {
        "mode": doctor_mode,
        "completed": bool(doctor_result.get("completed")),
        "exit_code": doctor_result.get("exit_code"),
        "healthy": None,
        "summary": None,
    }

    payload = _json_from_stdout(doctor_result)
    if isinstance(payload, dict):
        data = payload.get("data")
        if isinstance(data, dict):
            doctor["healthy"] = data.get("healthy")
            summary = data.get("summary")
            if isinstance(summary, dict):
                doctor["summary"] = {
                    key: summary.get(key)
                    for key in ("total", "ok", "warn", "fail", "skip")
                    if key in summary
                }
    elif doctor_result.get("completed"):
        doctor["parse_error"] = "doctor_stdout_not_json"

    info["doctor"] = doctor
    return info


def _fallback_info(plugin_root: Path) -> dict[str, Any]:
    manifest_path = plugin_root / "plugin.json"
    if not manifest_path.is_file():
        # In the unified ANGENT archive this internal catalog manifest is
        # reference data, not a second installable plugin.
        manifest_path = plugin_root / "source-manifest.json"
    skills_root = plugin_root / "skills"
    agents_root = plugin_root / "agents"

    manifest_valid = False
    plugin_name = None
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            plugin_name = manifest.get("name")
            manifest_valid = _portable_manifest_valid(
                manifest,
                "angent-engineer-fallback",
            )
        except (OSError, json.JSONDecodeError):
            pass

    actual_skills = {
        child.name
        for child in skills_root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    } if skills_root.is_dir() else set()

    actual_agents = {
        child.stem
        for child in agents_root.glob("*.md")
        if child.name != "README.md"
    } if agents_root.is_dir() else set()

    missing_skills = sorted(EXPECTED_SKILLS - actual_skills)
    unexpected_skills = sorted(actual_skills - EXPECTED_SKILLS)
    missing_agents = sorted(EXPECTED_AGENT_ROLES - actual_agents)
    unexpected_agents = sorted(actual_agents - EXPECTED_AGENT_ROLES)

    catalog_exact = not (
        missing_skills
        or unexpected_skills
        or missing_agents
        or unexpected_agents
    )
    expected_catalog_digest = _catalog_identity_digest(
        EXPECTED_SKILLS,
        EXPECTED_AGENT_ROLES,
    )
    actual_catalog_digest = _catalog_identity_digest(
        actual_skills,
        actual_agents,
    )
    baseline_digest_valid = (
        expected_catalog_digest == EXPECTED_CATALOG_IDENTITY_SHA256
    )
    structural_errors = audit_port(plugin_root)

    return {
        "plugin_path": str(plugin_root),
        "plugin_name": plugin_name,
        "plugin_manifest_valid": manifest_valid,
        "skills": len(actual_skills),
        "agent_roles": len(actual_agents),
        "expected_skills": len(EXPECTED_SKILLS),
        "expected_agent_roles": len(EXPECTED_AGENT_ROLES),
        "catalog_identity_sha256": actual_catalog_digest,
        "expected_catalog_identity_sha256": EXPECTED_CATALOG_IDENTITY_SHA256,
        "baseline_digest_valid": baseline_digest_valid,
        "missing_skills": missing_skills,
        "unexpected_skills": unexpected_skills,
        "missing_agent_roles": missing_agents,
        "unexpected_agent_roles": unexpected_agents,
        "catalog_exact": catalog_exact,
        "structural_check": "pass" if not structural_errors else "fail",
        "structural_errors": structural_errors[:12],
        "structural_error_count": len(structural_errors),
        "ready": manifest_valid and catalog_exact and baseline_digest_valid and not structural_errors,
    }

def _usable_value(raw: str | None) -> str:
    value = (raw or "unknown").strip().lower()
    aliases = {
        "1": "yes",
        "true": "yes",
        "usable": "yes",
        "0": "no",
        "false": "no",
        "unusable": "no",
        "": "unknown",
    }
    value = aliases.get(value, value)
    if value not in {"yes", "no", "unknown"}:
        raise ValueError(
            "native usability must be yes, no, or unknown "
            "(or a boolean-like equivalent)"
        )
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Select usable native AgentKit Engineer or ANGENT's portable "
            "fallback without mutating either environment."
        )
    )
    parser.add_argument(
        "--native-usable",
        choices=("yes", "no", "unknown"),
        default=None,
        help=(
            "Evidence from the active harness: yes only when native Engineer "
            "can actually be discovered/invoked in this session. Defaults to "
            "ANGENT_NATIVE_ENGINEER_USABLE or unknown."
        ),
    )
    parser.add_argument(
        "--doctor",
        choices=("none", "offline", "full"),
        default="offline",
        help="Optional read-only AgentKit health probe. Default: offline.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=8.0,
        help="Per-command timeout in seconds for AgentKit read-only probes.",
    )
    args = parser.parse_args()

    try:
        native_usable = _usable_value(
            args.native_usable
            if args.native_usable is not None
            else os.getenv("ANGENT_NATIVE_ENGINEER_USABLE")
        )
    except ValueError as exc:
        parser.error(str(exc))

    plugin_root = Path(__file__).resolve().parents[1]
    native = _detect_agentkit(args.doctor, args.timeout)
    native["usable"] = native_usable
    native["usability_evidence"] = (
        "active_harness"
        if args.native_usable is not None
        else (
            "environment"
            if os.getenv("ANGENT_NATIVE_ENGINEER_USABLE") is not None
            else "unproven"
        )
    )

    fallback = _fallback_info(plugin_root)

    if native_usable == "yes":
        mode = "native"
        reason = "active_harness_proved_native_engineer_usable"
    else:
        mode = "fallback"
        reason = (
            "active_harness_proved_native_engineer_unusable"
            if native_usable == "no"
            else "native_engineer_usability_unproven"
        )

    if mode == "fallback" and not fallback["ready"]:
        mode = "blocked"
        reason = "fallback_plugin_invalid_or_missing"

    result = {
        "schema_version": SCHEMA_VERSION,
        "kind": KIND,
        "mode": mode,
        "reason": reason,
        "native": native,
        "fallback": fallback,
        "policy": {
            "load_both": False,
            "cli_presence_proves_native_usability": False,
            "cached_files_prove_native_usability": False,
        },
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if mode in {"native", "fallback"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
