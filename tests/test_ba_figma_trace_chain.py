"""Cross-kit: source identity resolves in both real D2 and Reqwise payload generation.

This is evidence reference integrity, NOT a proof that the diagrams or runtime
Figma nodes represent the same approved business flow.
"""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
FIGMA=ROOT/"extensions/angent-figma"
sys.path.insert(0,str(BA/"scripts"))
sys.path.insert(0,str(FIGMA/"scripts"))
from validate_artifacts import audit
from build_d2 import compile_source
from to_reqwise_payload import compile_model

class BAFigmaTraceabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        cls.d2=json.loads((BA/"examples/d2-activity.json").read_text(encoding="utf8"))
        cls.figma=json.loads((FIGMA/"examples/rental-fleet-activity.json").read_text(encoding="utf8"))
        cls.ids={item["id"] for item in cls.graph["artifacts"]}

    def test_common_source_reference_without_canvas_write(self):
        self.assertTrue(audit(self.graph)["ok"])
        d2=compile_source(self.d2,evidence_ids=self.ids)
        payload=compile_model(self.figma,evidence_ids=self.ids)
        self.assertIn("FR-IVTS-01",d2)
        self.assertEqual(payload["source_link_check"],"ids-resolved-only")
        self.assertFalse(payload["writes_performed"])
        self.assertTrue(set(self.figma["source_refs"]) & set(self.d2["source_refs"]))
        self.assertEqual(payload["arguments"]["type"],"activity")

    def test_changed_requirements_fail_at_both_adapters(self):
        bad=deepcopy(self.d2)
        bad["source_refs"]=["FR-UNKNOWN-001"]
        with self.assertRaisesRegex(ValueError,"Unresolved evidence"):
            compile_source(bad,evidence_ids=self.ids)
        bad=deepcopy(self.figma)
        bad["source_refs"]=["FR-UNKNOWN-001"]
        with self.assertRaisesRegex(ValueError,"Unresolved evidence"):
            compile_model(bad,evidence_ids=self.ids)

    def test_invalid_source_graph_never_authorizes_link_check(self):
        graph=deepcopy(self.graph)
        graph["artifacts"][0]["depends_on"]=["DOES-NOT-EXIST"]
        self.assertFalse(audit(graph)["ok"])
        # Consumers must refuse that graph rather than infer approval from
        # the mere existence of its ID set.
        self.assertNotEqual(audit(graph)["errors"],[])

if __name__=="__main__":
    unittest.main()
