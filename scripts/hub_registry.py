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


def _texts(value: object, label: str, minimum: int = 0) -> list[str]:
    if not isinstance(value, list) or len(value) < minimum:
        _fail(f"{label}: expected a string list")
    for item in value:
        _text(item, label)
    if len(value) != len(set(value)):
        _fail(f"{label}: duplicate values")
    return value


def _method_cards(manifest: dict, active: list[str], entries: dict[str, bytes]) -> list[dict]:
    """Keep uncurated methods visible without inventing invocation/output contracts."""
    extid = manifest["id"]
    declared = {}
    for card in manifest.get("methods", []):
        _fields(card, {"entry", "summary", "capabilities", "domains", "aliases",
                       "invocation", "outputs", "requires"}, f"{extid}.method")
        entry = card["entry"]
        if not isinstance(entry, str) or entry not in active or entry in declared:
            _fail(f"{extid}: missing/excluded/duplicate method entry: {entry}")
        _text(card["summary"], f"{entry}.summary")
        for field in ("capabilities", "domains", "aliases", "outputs", "requires"):
            _texts(card[field], f"{entry}.{field}", 1 if field in ("capabilities", "domains", "outputs") else 0)
        if any(not _CAPABILITY.fullmatch(c) for c in card["capabilities"]):
            _fail(f"{entry}: invalid semantic capability")
        if any(not _SKILL.fullmatch(d) for d in card["domains"]):
            _fail(f"{entry}: invalid soft domain label")
        if card["invocation"] not in ("automatic", "explicit"):
            _fail(f"{entry}: invalid invocation condition")
        declared[entry] = card
    cards = []
    for entry in active:
        source_path = f"extensions/{extid}/skills/{entry}/SKILL.md"
        body = entries[source_path].decode("utf-8")
        description = re.search(r"^description:[ \t]*(.+)$", body, re.M)
        if description is None:
            _fail(f"{entry}: missing discovery description")
        card = declared.get(entry)
        cards.append({
            "id": f"{extid}:{entry}", "extension": extid, "entry": entry,
            "contract_status": "declared" if card else "inspect-required",
            "summary": card["summary"] if card else description.group(1).strip(),
            "capabilities": card["capabilities"] if card else
                            sorted(c["id"] for c in manifest["capabilities"] if c["entry"] == entry),
            "domains": card["domains"] if card else [],
            "aliases": card["aliases"] if card else [],
            "invocation": card["invocation"] if card else "inspect-required",
            "outputs": card["outputs"] if card else [],
            "requires": card["requires"] if card else [],
            "source": source_path,
        })
    return cards


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
    methods = []
    for path in manifest_paths:
        try:
            m = json.loads(entries[path])
        except (ValueError, UnicodeError) as exc:
            raise HubError(f"Invalid manifest JSON: {path}") from exc
        fields = {"schema_version", "id", "name", "kind", "authority",
                  "description", "source", "skills", "roles", "runtime", "capabilities"}
        if isinstance(m, dict) and m.get("schema_version") == 2:
            fields.add("methods")
        _fields(m, fields, path)
        extid = path.split("/")[1]
        if type(m["schema_version"]) is not int or m["schema_version"] not in (1, 2):
            _fail(f"{extid}: incompatible contract version")
        if not isinstance(m["id"], str) or not _SLUG.fullmatch(m["id"]) or m["id"] != extid:
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
        if "methods" in m and (not isinstance(m["methods"], list) or not m["methods"]):
            _fail(f"{extid}: methods must be a nonempty list")
        cards = _method_cards(m, active, entries)
        methods.extend(cards)
        # Compatibility capability routes and richer method contracts share one
        # semantic namespace; several methods in one kit may serve a capability.
        for cap in caps:
            providers.setdefault(cap["id"], []).append({
                "extension": extid, "entry": cap["entry"], "when": cap["when"]})
        for card in cards:
            for capability in card["capabilities"]:
                route = providers.setdefault(capability, [])
                if not any(p["extension"] == extid and p["entry"] == card["entry"] for p in route):
                    route.append({"extension": extid, "entry": card["entry"], "when": card["summary"]})
        extensions.append({
            "id": extid, "name": m["name"], "kind": m["kind"], "authority": "specialist",
            "description": m["description"], "source": source,
            "source_skill_count": len(declared), "skills": active, "roles": roles,
            "runtime": rt, "capabilities": sorted(
                [{"id": cid, "entry": p["entry"], "when": p["when"]}
                 for cid, route in providers.items() for p in route if p["extension"] == extid],
                key=lambda x: (x["id"], x["entry"])),
        })
    # All registered files must have one extension-owned source path.
    for p in entries:
        if p.startswith("extensions/") and p.endswith("/extension.json") and p not in manifest_paths:
            _fail(f"Invalid manifest location: {p}")
    return {
        "schema_version": 2,
        "extensions": extensions,
        "published_skills": sorted(published),
        "method_cards": {c["entry"]: "methods/" + c["entry"] + ".json" for c in methods},
        "capabilities": [{"id": cap, "providers": sorted(providers[cap], key=lambda x: (x["extension"], x["entry"]))}
                         for cap in sorted(providers)],
    }


def method_entries(entries: dict[str, bytes]) -> dict[str, bytes]:
    """Generate small inspectable cards plus a no-Python global discovery escape."""
    output = {}
    index = ["# Specialist method discovery", "",
             "Search all entries when a domain guess misses. A match is a candidate, not activation or permission.",
             "Inspect its method card and binding before loading the method. Uncurated contracts require source inspection.", ""]
    for path in sorted(p for p in entries if _MANIFEST.fullmatch(p)):
        m = json.loads(entries[path])
        active = sorted(match.group(2) for p in entries if (match := _SOURCE_SKILL.fullmatch(p))
                        if match.group(1) == m["id"] and match.group(2) not in m["skills"]["exclude"])
        for card in _method_cards(m, active, entries):
            entry = card["entry"]
            output[f"hub/methods/{entry}.json"] = (json.dumps(card, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
            index.append(f"- [{entry}](methods/{entry}.json) ({card['invocation']}): {card['summary']}")
    output["hub/catalog.md"] = ("\n".join(index) + "\n").encode()
    return output
