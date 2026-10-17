"""Real source-byte and filesystem boundary regressions for package inputs."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("source_boundary", ROOT / "scripts/package_unified.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)
sys.path.insert(0, str(ROOT / "scripts"))
import build_packages
import package_all_targets


class SourceBoundaryTests(unittest.TestCase):
    def test_archive_bytes_do_not_inherit_host_zip_metadata(self):
        original = zipfile.ZipInfo
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            results = []
            for host in (0, 3):
                class HostZipInfo(original):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.create_system = host
                root = base / str(host)
                root.mkdir()
                with mock.patch.object(zipfile, "ZipInfo", HostZipInfo):
                    build_packages._zip({"SKILL.md": b"portable\n"}, root / "target.zip")
                    # Exercise the aggregate with identical independent inputs.
                    for name in package_all_targets.FILES:
                        (root / name).write_bytes((root / "target.zip").read_bytes())
                    package_all_targets.build(root)
                    results.append(((root / "target.zip").read_bytes(),
                                    (root / package_all_targets.COMBINED).read_bytes()))
            self.assertEqual(results[0], results[1])
            with zipfile.ZipFile(base / "0/target.zip") as archive:
                info = archive.getinfo("SKILL.md")
                self.assertEqual(info.create_system, 3)
                self.assertEqual(info.external_attr >> 16, 0o100644)

    def test_all_profiles_match_between_lf_and_crlf_checkouts(self):
        paths = package._tracked(ROOT)
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            lf, crlf = Path(a), Path(b)
            for path in paths:
                payload = package._safe_file(ROOT, path)
                for target, windows in ((lf, False), (crlf, True)):
                    destination = target / path
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    variant = payload.replace(b"\n", b"\r\n") if windows and destination.suffix.lower() in package.TEXT_SUFFIXES else payload
                    destination.write_bytes(variant)
            left = package.collect_entries(lf, paths)
            right = package.collect_entries(crlf, paths)
            self.assertEqual(left, right)
            for profile in build_packages.PACKAGES:
                with self.subTest(profile=profile):
                    self.assertEqual(build_packages.assemble(lf, profile, left),
                                     build_packages.assemble(crlf, profile, right))
            # Actual archive bytes, including order/metadata/compression, also match.
            za, zb = lf / "a.zip", crlf / "b.zip"
            build_packages._zip(package.gateway_entries(left), za)
            build_packages._zip(package.gateway_entries(right), zb)
            self.assertEqual(za.read_bytes(), zb.read_bytes())

    def test_canonical_text_preserves_local_edits_and_binary_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            text = root / "SKILL.md"
            text.write_bytes("---\nname: demo\n---\nSửa\n".encode())
            expected = package._safe_file(root, "SKILL.md")
            text.write_bytes(expected.replace(b"\n", b"\r\n"))
            self.assertEqual(package._safe_file(root, "SKILL.md"), expected)
            text.write_bytes(expected + b"local edit\r\n")
            self.assertEqual(package._safe_file(root, "SKILL.md"), expected + b"local edit\n")
            raw = b"\x89PNG\r\n\x00\xff"
            (root / "image.png").write_bytes(raw)
            self.assertEqual(package._safe_file(root, "image.png"), raw)

    def test_parent_link_and_leaf_link_are_rejected(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            root, external = Path(d), Path(outside)
            (external / "SKILL.md").write_text("outside", encoding="utf-8")
            (root / "inside.md").write_text("inside", encoding="utf-8")
            try:
                (root / "parent").symlink_to(external, target_is_directory=True)
                (root / "leaf.md").symlink_to(root / "inside.md")
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")
            for name in ("parent/SKILL.md", "leaf.md"):
                with self.subTest(name=name), self.assertRaises(package.PackagingError):
                    package._safe_file(root, name)

    @unittest.skipUnless(os.name == "nt", "Windows junction boundary")
    def test_parent_junction_is_rejected(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            root, external = Path(d), Path(outside)
            (external / "SKILL.md").write_text("outside", encoding="utf-8")
            junction = root / "junction"
            # Fixed executable and argument list; no user-controlled shell command.
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(external)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            try:
                with self.assertRaises(package.PackagingError):
                    package._safe_file(root, "junction/SKILL.md")
            finally:
                junction.rmdir()  # Remove only the verified link, never its target.

    def test_unsafe_paths_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            for name in ("../escape.md", "/absolute.md", "C:/escape.md", "a\\b.md", ""):
                with self.subTest(name=name), self.assertRaises(package.PackagingError):
                    package._safe_file(Path(d), name)


if __name__ == "__main__":
    unittest.main()
