"""Optional real Bruno CLI integration: execute generated requests against localhost.

Run explicitly with:
  BRUNO_CLI_COMMAND="npx --yes --package=@usebruno/cli@4.2.1 -- bru" \
      python -m unittest discover -s tests -p test_bruno_cli_integration.py -v
CI environments without the CLI remain unaffected; a skip is not a pass.
"""
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit,parse_qs
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_bruno import compile_collection

class MockVehicleApi(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed=urlsplit(self.path)
        mode=parse_qs(parsed.query).get("mode",[""])[0]
        if parsed.path!="/vehicles/demo-001/status":
            status,result=404,{"error":"NOT_FOUND"}
        elif mode=="ok":
            status,result=200,{"vehicleId":"demo-001","state":"online"}
        elif mode=="denied":
            status,result=403,{"error":"ACCESS_DENIED"}
        elif mode=="offline":
            status,result=503,{"error":"TELEMETRY_UNAVAILABLE"}
        else:
            status,result=400,{"error":"BAD_MODE"}
        payload=json.dumps(result).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
    def do_POST(self):
        try:
            size=int(self.headers.get("Content-Length","0"))
            body=json.loads(self.rfile.read(size))
            if (self.path=="/vehicles/demo-001/diagnostics/ack"
                    and body.get("code")=="P0100"
                    and body.get("operator")=="synthetic-test"):
                status,result=201,{"vehicleId":"demo-001","ack":"recorded"}
            else:
                status,result=422,{"error":"INVALID_DIAGNOSTIC_ACK"}
        except (ValueError,TypeError,AttributeError):
            status,result=400,{"error":"INVALID_JSON"}
        payload=json.dumps(result).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self,*args):
        pass

@unittest.skipUnless(os.environ.get("BRUNO_CLI_COMMAND"),"Real Bruno CLI not configured (not an execution pass)")
class BrunoCliIntegration(unittest.TestCase):
    def test_generated_requests_execute_and_assert(self):
        server=ThreadingHTTPServer(("127.0.0.1",0),MockVehicleApi)
        worker=threading.Thread(target=server.serve_forever,daemon=True)
        worker.start()
        try:
            model=json.loads((BA/"examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))
            model["environment"]["baseUrl"]="http://127.0.0.1:"+str(server.server_port)
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)
                generated=compile_collection(model)
                for filename,source in generated.items():
                    path=root/filename
                    path.parent.mkdir(parents=True,exist_ok=True)
                    path.write_text(source,encoding="utf8")
                cmd=shlex.split(os.environ["BRUNO_CLI_COMMAND"])+["run","requests","--env","Mock"]
                resolved=shutil.which(cmd[0])
                if resolved is None:
                    self.fail("Configured Bruno CLI executable not found: "+cmd[0])
                cmd[0]=resolved
                result=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=180,encoding="utf8",errors="replace")
                self.assertEqual(result.returncode,0,"Bruno CLI execution failed:\n"+result.stdout[-3000:]+"\n"+result.stderr[-2000:])
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=5)

if __name__=="__main__":
    unittest.main()
