"""All-target ZIP: contents, determinism, error handling."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("aggregate", ROOT / "scripts/package_all_targets.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class AllTargetsTests(unittest.TestCase):
    def fixture(self, path):
        for name in app.FILES:
            with zipfile.ZipFile(path / name, "w") as z:
                z.writestr("sample.txt", name)

    def test_complete_reproducible_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            self.fixture(p)
            digests = app.build(p)
            first = hashlib.sha256((p / app.COMBINED).read_bytes()).hexdigest()
            with zipfile.ZipFile(p / app.COMBINED) as z:
                self.assertEqual(set(z.namelist()), set(app.FILES) | {"SHA256SUMS"})
                self.assertIsNone(z.testzip())
                for name in app.FILES:
                    self.assertEqual(z.read(name), (p / name).read_bytes())
                    self.assertIn(digests[name] + "  " + name, z.read("SHA256SUMS").decode())
            app.build(p)
            self.assertEqual(first, hashlib.sha256((p / app.COMBINED).read_bytes()).hexdigest())

    def test_missing_and_invalid_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            with self.assertRaises(ValueError):
                app.build(p)
            self.fixture(p)
            (p / app.FILES[0]).write_bytes(b"no zip")
            with self.assertRaises(zipfile.BadZipFile):
                app.build(p)


if __name__ == "__main__":
    unittest.main()
