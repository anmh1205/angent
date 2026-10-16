"""Next review generator preserves approved BA screen semantics and declares limits."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_next_prototype import generate_files

class NextBAPrototypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/authentication-screen-model.json").read_text(encoding="utf8"))

    def test_generated_app_contains_all_screens_and_is_explicitly_a_mock(self):
        generated=generate_files(self.model)
        self.assertEqual(set(generated),{
            "package.json","model.json","review-manifest.json","README.md",
            "app/layout.jsx","app/page.jsx","app/[screen]/page.jsx","app/globals.css"})
        meta=json.loads(generated["review-manifest.json"])
        self.assertEqual(meta["screens"],["login","recovery","home"])
        self.assertEqual(meta["mock_scenarios"],["success","invalid","locked","offline"])
        self.assertTrue(meta["simulation_only"])
        self.assertEqual(meta["execution_status"],"not-run")
        self.assertEqual(json.loads(generated["model.json"]),self.model)
        self.assertIn("next build",generated["package.json"])
        self.assertIn("No real authentication",generated["README.md"])

    def test_keyboard_route_focus_and_hydration_handshake(self):
        app=generate_files(self.model)["app/[screen]/page.jsx"]
        self.assertIn("setHydrated(true)",app)
        self.assertIn('data-angent-hydrated={hydrated ? "true" : "false"}',app)
        self.assertIn("disabled={!hydrated}",app)
        self.assertIn("heading.current?.focus()",app)
        self.assertIn("reportValidity()",app)
        self.assertIn("role=\\"alert\\"",app)

    def test_script_does_not_interpolate_untrusted_model_into_js(self):
        model=copy.deepcopy(self.model)
        model["screens"][0]["title"]='</script><img onerror="alert(1)">'
        model["screens"][0]["controls"][0]["label"]="'; process.exit(99); //"
        generated=generate_files(model)
        self.assertEqual(json.loads(generated["model.json"])["screens"][0]["title"],
                         model["screens"][0]["title"])
        self.assertNotIn("process.exit(99)",generated["app/[screen]/page.jsx"])
        self.assertNotIn("onerror=",generated["app/[screen]/page.jsx"])

    def test_bad_sources_and_password_values_fail_closed(self):
        broken=copy.deepcopy(self.model)
        broken["screens"][0]["controls"][1]["test_value"]="literal-password"
        with self.assertRaisesRegex(ValueError,"password"):
            generate_files(broken)
        broken=copy.deepcopy(self.model)
        broken["screens"][0]["controls"][2]["outcomes"]["locked"]={"type":"navigate","target":"nonexistent"}
        with self.assertRaisesRegex(ValueError,"Invalid BA screen model"):
            generate_files(broken)

if __name__=="__main__":
    unittest.main()
