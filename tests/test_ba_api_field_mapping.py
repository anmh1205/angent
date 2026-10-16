"""Actual OpenAPI provider-to-UI mapping tests with negative contract fixtures."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from audit_api_field_mapping import perform
from validate_artifacts import audit

class FieldMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract=json.loads((BA/"examples/synthetic-fleet-openapi.json").read_text(encoding="utf8"))
        cls.mapping=json.loads((BA/"examples/synthetic-fleet-api-map.json").read_text(encoding="utf8"))
        cls.graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        cls.refs={a["id"] for a in cls.graph["artifacts"]}

    def test_explicit_mapping_and_source_graph(self):
        self.assertTrue(audit(self.graph)["ok"])
        result=perform(self.contract,self.mapping,self.refs)
        self.assertTrue(result["ok"])
        self.assertEqual(result["field_count"],2)
        self.assertEqual(result["mapped_fixture"],self.mapping["expected_ui"])
        self.assertEqual(result["source_link_check"],"ids-resolved-only")
        self.assertEqual(result["live_api_calls"],0)
        self.assertFalse(result["browser_bindings_verified"])
        self.assertFalse(result["writes_performed"])

    def test_reject_missing_api_field_and_unknown_contract(self):
        m=copy.deepcopy(self.mapping)
        m["fields"][0]["source"]="notKnownToOpenAPI"
        with self.assertRaisesRegex(ValueError,"OpenAPI source field"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["sample_response"].pop("vehicleId")
        with self.assertRaisesRegex(ValueError,"Source fixture field missing"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["operation"]["path"]="/vehicles/{vehicleId}/private"
        with self.assertRaisesRegex(ValueError,"No such OpenAPI operation"):
            perform(self.contract,m)

    def test_enum_missing_case_or_mismatched_expected_fails(self):
        m=copy.deepcopy(self.mapping)
        m["fields"][1]["cases"].pop("online")
        with self.assertRaisesRegex(ValueError,"Enum transform lacks"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["fields"][1]["cases"]["online"]="unknown"
        with self.assertRaisesRegex(ValueError,"Mapped output differs"):
            perform(self.contract,m)

    def test_reject_collisions_and_prototype_pollution(self):
        m=copy.deepcopy(self.mapping)
        m["fields"][1]["target"]="fleet.vehicleId"
        with self.assertRaisesRegex(ValueError,"Duplicate destination"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["fields"][1]["target"]="fleet.vehicleId.malicious"
        m["ui_field_types"].pop("fleet.connection")
        m["ui_field_types"]["fleet.vehicleId.malicious"]="string"
        with self.assertRaisesRegex(ValueError,"collides"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["fields"][0]["target"]="__proto__.admin"
        with self.assertRaisesRegex(ValueError,"Invalid/reserved"):
            perform(self.contract,m)

    def test_source_type_target_type_and_provenance(self):
        m=copy.deepcopy(self.mapping)
        m["sample_response"]["state"]="connecting"
        with self.assertRaisesRegex(ValueError,"Source sample violates"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["ui_field_types"]["fleet.connection"]="number"
        with self.assertRaisesRegex(ValueError,"Destination value"):
            perform(self.contract,m)
        m=copy.deepcopy(self.mapping)
        m["source_refs"]=["FR-NONEXISTENT"]
        with self.assertRaisesRegex(ValueError,"Unresolved"):
            perform(self.contract,m,self.refs)

    def test_invalid_openapi_version_and_malformed_paths_fail_closed(self):
        for bad_version in ("3.1evil", "3.10.0", "3.0.3", True, None):
            with self.subTest(version=bad_version):
                contract=copy.deepcopy(self.contract)
                contract["openapi"]=bad_version
                with self.assertRaisesRegex(ValueError,"OpenAPI 3.1"):
                    perform(contract,self.mapping)
        for bad_paths in ([], "routes", None):
            with self.subTest(paths=bad_paths):
                contract=copy.deepcopy(self.contract)
                contract["paths"]=bad_paths
                with self.assertRaisesRegex(ValueError,"paths must be an object"):
                    perform(contract,self.mapping)
        contract=copy.deepcopy(self.contract)
        contract["paths"][self.mapping["operation"]["path"]]=["invalid-path-item"]
        with self.assertRaisesRegex(ValueError,"path item must be an object"):
            perform(contract,self.mapping)

    def test_unsupported_transform_is_a_failure(self):
        m=copy.deepcopy(self.mapping)
        m["fields"][1]["transform"]="evaluate-javascript"
        with self.assertRaisesRegex(ValueError,"Unsupported field transform"):
            perform(self.contract,m)

if __name__=="__main__":
    unittest.main()
