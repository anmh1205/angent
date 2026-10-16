"""Validate ANGENT Kit Adapters and derive a stable, package-only capability registry.

No YAML dependency, no runtime broker, no persisted task state. Inputs are
source file bytes, so the same inventory feeds every target build.
"""
from __future__ import annotations

import json
import re


class HubError(ValueError):
    """An invalid kit contract or unsafe inventory."""


_SLUG = re.compile(r"angent-[a-z0-9]+(?:-[a-z0-9]+)*\Z")
_SKILL = re.compile(r"[a-z][a-z0-9-]*\Z")
_CAPABILITY = re.compile(r"[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)+\Z")
_MANIFEST = re.compile(r"extensions/(angent-[a-z0-9-]+)/extension\.json\Z")
_SOURCE_SKILL = re.compile(r"extensions/(angent-[a-z0-9-]+)/skills/([a-z][a-z0-9-]*)/SKILL\.md\Z")
_SOURCE_ROLE = re.compile(r"extensions/(angent-[a-z0-9-]+)/agents/([a-z][a-z0-9-]*)\.md\Z")


def _fail(message: str) -> None:
    raise HubError(message)


def _fields(obj: object, required: set[str], label: str) -> dict:
    if not isinstance(obj, dict) or set(obj) != required:
        _fail(f"{label}: expected exactly {sorted(required)}")
    return obj


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        _fail(f"{label}: expected nonempty string")
    return value


def _count(value: object, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        _fail(f"{label}: invalid count")
    return value


def build_registry(entries: dict[str, bytes]) -> dict:
    """Compile discovered kit skill identities from validated extension manifests."""
    manifest_paths = sorted(p for p in entries if _MANIFEST.fullmatch(p))
    source_ids = {m.group(1) for p in entries if (m := _SOURCE_SKILL.fullmatch(p))}
    manifests = {m.group(1) for p in manifest_paths if (m := _MANIFEST.fullmatch(p))}
    if not manifest_paths or source_ids != manifests:
        _fail(f"Every kit Skill requires a manifest: skills={sorted(source_ids)} manifests={sorted(manifests)}")
    extensions = []
    published = set()
    providers: dict[str, list[dict]] = {}
    for path in manifest_paths:
        try:
            m = json.loads(entries[path])
        except (ValueError, UnicodeError) as exc:
            raise HubError(f"Invalid manifest JSON: {path}") from exc
        _fields(m, {"schema_version", "id", "name", "kind", "authority",
                    "description", "source", "skills", "roles", "runtime", "capabilities"}, path)
        extid = path.split("/")[1]
        if type(m["schema_version"]) is not int or m["schema_version"] != 1:
            _fail(f"{extid}: incompatible contract version")
        if not _SLUG.fullmatch(m["id"]) or m["id"] != extid:
            _fail(f"{extid}: manifest identity mismatch")
        _text(m["name"], f"{extid}.name")
        _text(m["description"], f"{extid}.description")
        if m["kind"] not in ("direct", "mapped", "bridged") or m["authority"] != "specialist":
            _fail(f"{extid}: invalid kind or authority")
        source = _fields(m["source"], {"origin", "type", "license"}, f"{extid}.source")
        for field in source:
            _text(source[field], f"{extid}.source.{field}")
        spec = _fields(m["skills"], {"directory", "expose", "exclude", "expected_source_count"},
                       f"{extid}.skills")
        if spec["directory"] != "skills" or spec["expose"] != "all":
            _fail(f"{extid}: unsupported skill discovery mode")
        excludes = spec["exclude"]
        if not isinstance(excludes, list) or any(not isinstance(x, str) or not _SKILL.fullmatch(x) for x in excludes) or len(excludes) != len(set(excludes)):
            _fail(f"{extid}: invalid exclusion list")
        declared = {name for p in entries if (match := _SOURCE_SKILL.fullmatch(p))
                    if match.group(1) == extid for name in [match.group(2)]}
        if len(declared) != _count(spec["expected_source_count"], f"{extid}.skills.count", 1):
            _fail(f"{extid}: source Skill count changed")
        if not set(excludes) <= declared:
            _fail(f"{extid}: excluded Skill missing")
        for skill in declared:
            body = entries[f"extensions/{extid}/skills/{skill}/SKILL.md"].decode("utf-8")
            if not re.search(r"^name:\s*" + re.escape(skill) + r"\s*$", body, re.M):
                _fail(f"{extid}: invalid Skill frontmatter name: {skill}")
        active = sorted(declared - set(excludes))
        if not active or published.intersection(active):
            _fail(f"{extid}: empty or colliding public Skill identities")
        published.update(active)
        role_spec = _fields(m["roles"], {"directory", "expected_count"}, f"{extid}.roles")
        if role_spec["directory"] != "agents":
            _fail(f"{extid}: invalid role directory")
        roles = sorted(match.group(2) for p in entries if (match := _SOURCE_ROLE.fullmatch(p))
                       if match.group(1) == extid)
        if len(roles) != _count(role_spec["expected_count"], f"{extid}.roles.count"):
            _fail(f"{extid}: role count changed")
        rt = _fields(m["runtime"], {"native", "fallback", "selection", "exclusive"}, f"{extid}.runtime")
        if rt["native"] is not None:
            _text(rt["native"], f"{extid}.runtime.native")
        if rt["fallback"] not in ("portable", "none") or type(rt["exclusive"]) is not bool:
            _fail(f"{extid}: invalid runtime mode")
        _text(rt["selection"], f"{extid}.runtime.selection")
        caps = m["capabilities"]
        if not isinstance(caps, list) or not caps:
            _fail(f"{extid}: no capabilities")
        seen = set()
        for cap in caps:
            _fields(cap, {"id", "entry", "when"}, f"{extid}.capability")
            if not isinstance(cap["id"], str) or not _CAPABILITY.fullmatch(cap["id"]) or cap["id"] in seen:
                _fail(f"{extid}: invalid/duplicate capability identity")
            seen.add(cap["id"])
            if cap["entry"] not in active:
                _fail(f"{extid}: capability references missing/excluded Skill {cap['entry']}")
            _text(cap["when"], f"{extid}.capability.when")
            providers.setdefault(cap["id"], []).append({
                "extension": extid, "entry": cap["entry"], "when": cap["when"]})
        extensions.append({
            "id": extid, "name": m["name"], "kind": m["kind"], "authority": "specialist",
            "description": m["description"], "source": source,
            "source_skill_count": len(declared), "skills": active, "roles": roles,
            "runtime": rt, "capabilities": sorted(caps, key=lambda x: x["id"]),
        })
    # All registered files must have one extension-owned source path.
    for p in entries:
        if p.startswith("extensions/") and p.endswith("/extension.json") and p not in manifest_paths:
            _fail(f"Invalid manifest location: {p}")
    return {
        "schema_version": 1,
        "extensions": extensions,
        "published_skills": sorted(published),
        "capabilities": [{"id": cap, "providers": sorted(providers[cap], key=lambda x: x["extension"])}
                         for cap in sorted(providers)],
    }
