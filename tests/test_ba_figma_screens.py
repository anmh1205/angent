"""Verify BA screen labels and controls survive translation into editable Figma node trees.

No assertion in these tests represents a live provider call or Figma write.
"""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_figma_screens import compile_screens,files

class EditableFigmaScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/authentication-screen-model.json").read_text(encoding="utf8"))

    def test_source_screen_and_control_inventory_is_preserved(self):
        plan=compile_screens(self.model)
        self.assertEqual(plan["sources"]["screen_count"],3)
        self.assertEqual(plan["runtime_status"],"not-run")
        self.assertFalse(plan["writes_performed"])
        self.assertEqual([x["source_id"] for x in plan["screens"]],["login","recovery","home"])
        for source,screen in zip(self.model["screens"],plan["screens"]):
            self.assertEqual(screen["source_id"],source["id"])
            controls=[x for x in screen["figma_tree"]["children"] if x["name"].startswith("control:")]
            self.assertEqual([x["name"] for x in controls],
                ["control:"+x["type"]+":"+x["id"] for x in source["controls"]])
            self.assertEqual([x["children"][0]["characters"].removeprefix("☐ ") for x in controls],
                             [x["label"] for x in source["controls"]])
            self.assertEqual([x["id"] for x in screen["controls"]],[x["id"] for x in source["controls"]])
        self.assertEqual(sum(len(x["controls"]) for x in plan["screens"]),9)

    def test_candidate_source_is_not_claimed_as_native_write(self):
        output=files(self.model)
        self.assertEqual(set(output),{"figma-screen-plan.json","figma-write.js"})
        self.assertIn("await figma.create(item.tree)",output["figma-write.js"])
        self.assertIn('WRITE_REQUESTED_NOT_YET_READ_BACK',output["figma-write.js"])
        plan=json.loads(output["figma-screen-plan.json"])
        self.assertEqual(plan["screens"][0]["controls"][2]["outcomes"]["locked"]["type"],"error")
        self.assertEqual(plan["runtime_status"],"not-run")
        self.assertTrue(plan["limitations"])

    def test_reject_invalid_model_and_keep_password_fixture_out(self):
        bad=copy.deepcopy(self.model)
        bad["screens"][0]["controls"][0]["id"]=bad["screens"][0]["controls"][1]["id"]
        with self.assertRaises(ValueError):
            compile_screens(bad)
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][1]["test_value"]="never-include-this-secret"
        out=files(data)
        self.assertNotIn("never-include-this-secret",out["figma-write.js"])
        self.assertNotIn("never-include-this-secret",out["figma-screen-plan.json"])

    def test_untrusted_control_label_remains_quoted(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][0]["label"]='"; console.log("INJECTED"); //'
        script=files(data)["figma-write.js"]
        self.assertIn(r'\"; console.log(\"INJECTED\"); //',script)
        self.assertNotIn('"; console.log("INJECTED"); //";',script)

if __name__=="__main__":
    unittest.main()
