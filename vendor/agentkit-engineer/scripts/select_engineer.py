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


SCHEMA_VERSION = 1
KIND = "angent.engineer_selection"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PLUGIN_FIELDS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
PLUGIN_NAME = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")


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


def _catalog_identity_digest(
    skills: set[str],
    agents: set[str],
) -> str:
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


def _fallback_info(plugin_root: Path) -> dict[str, Any]:
    manifest_path = plugin_root / "plugin.json"
    catalog_path = plugin_root / "STABLE_CATALOG.json"
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

    catalog_valid = False
    expected_skill_ids: set[str] = set()
    expected_agent_roles: set[str] = set()
    catalog_meta: dict[str, Any] = {}
    if catalog_path.is_file():
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            public_skills = catalog.get("public_skills")
            portable_agents = catalog.get("portable_agent_roles")
            upstream = catalog.get("upstream")
            if (
                catalog.get("schema_version") == 1
                and isinstance(public_skills, list)
                and all(isinstance(value, str) for value in public_skills)
                and len(public_skills) == len(set(public_skills))
                and isinstance(portable_agents, list)
                and all(isinstance(value, str) for value in portable_agents)
                and len(portable_agents) == len(set(portable_agents))
                and isinstance(upstream, dict)
            ):
                expected_skill_ids = set(public_skills)
                expected_agent_roles = set(portable_agents)
                target_policy = catalog.get("target_policy")
                observed_registry = upstream.get("observed_registry_export")
                expected_digest = upstream.get("documented_identity_sha256")
                actual_expected_digest = _catalog_identity_digest(
                    expected_skill_ids,
                    expected_agent_roles,
                )
                catalog_meta = {
                    "channel": upstream.get("channel"),
                    "retrieved_at": upstream.get("retrieved_at"),
                    "documented_resolved_skills": upstream.get(
                        "documented_resolved_skills"
                    ),
                    "documented_resolved_agents": upstream.get(
                        "documented_resolved_agents"
                    ),
                    "documented_identity_sha256": expected_digest,
                    "computed_identity_sha256": actual_expected_digest,
                    "fallback_identity_target": (
                        target_policy.get("fallback_identity_target")
                        if isinstance(target_policy, dict)
                        else None
                    ),
                    "exact_upstream_package_parity": (
                        target_policy.get("exact_upstream_package_parity")
                        if isinstance(target_policy, dict)
                        else None
                    ),
                    "observed_registry_export": (
                        observed_registry
                        if isinstance(observed_registry, dict)
                        else None
                    ),
                }
                catalog_valid = (
                    catalog_meta["documented_resolved_skills"]
                    == len(expected_skill_ids)
                    and catalog_meta["documented_resolved_agents"]
                    == len(expected_agent_roles)
                    and isinstance(expected_digest, str)
                    and expected_digest == actual_expected_digest
                    and catalog_meta["fallback_identity_target"]
                    == "docs_stable_public_contract"
                    and catalog_meta["exact_upstream_package_parity"] is False
                )
        except (OSError, json.JSONDecodeError):
            pass

    actual_skill_ids: set[str] = set()
    if skills_root.is_dir():
        actual_skill_ids = {
            child.name
            for child in skills_root.iterdir()
            if child.is_dir() and (child / "SKILL.md").is_file()
        }

    actual_agent_roles: set[str] = set()
    if agents_root.is_dir():
        actual_agent_roles = {
            child.stem
            for child in agents_root.glob("*.md")
            if child.name != "README.md"
        }

    missing_skills = sorted(expected_skill_ids - actual_skill_ids)
    extra_skills = sorted(actual_skill_ids - expected_skill_ids)
    missing_agents = sorted(expected_agent_roles - actual_agent_roles)
    extra_agents = sorted(actual_agent_roles - expected_agent_roles)

    return {
        "plugin_path": str(plugin_root),
        "plugin_name": plugin_name,
        "plugin_manifest_valid": manifest_valid,
        "catalog_path": str(catalog_path),
        "catalog_valid": catalog_valid,
        "catalog": catalog_meta,
        "skills": len(actual_skill_ids),
        "agent_roles": len(actual_agent_roles),
        "expected_skills": len(expected_skill_ids),
        "expected_agent_roles": len(expected_agent_roles),
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
        "missing_agent_roles": missing_agents,
        "extra_agent_roles": extra_agents,
        "ready": (
            manifest_valid
            and catalog_valid
            and not missing_skills
            and not extra_skills
            and not missing_agents
            and not extra_agents
        ),
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
