#!/usr/bin/env python3
"""Execute a generated Bruno collection against a loopback HTTP fixture.

Requires an installed Bruno CLI; no requests leave localhost. A passing exit
code alone is insufficient: confirm all three expected requests reached mock.
"""
from __future__ import annotations
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from threading import Thread
from urllib.parse import urlsplit,parse_qs

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_bruno import compile_collection

class MockFleet(BaseHTTPRequestHandler):
    calls=[]
    ack_events=[]
    def log_message(self,*args):
        return
    def do_GET(self):
        p=urlsplit(self.path)
        mode=parse_qs(p.query).get("mode",[""])[0]
        self.__class__.calls.append((self.command,p.path,mode))
        if p.path!="/vehicles/demo-001/status":
            status,body=404,{"error":"NOT_FOUND"}
        elif mode=="ok":
            status,body=200,{"vehicleId":"demo-001","state":"online"}
        elif mode=="denied":
            status,body=403,{"error":"ACCESS_DENIED"}
        elif mode=="offline":
            status,body=503,{"error":"TELEMETRY_UNAVAILABLE"}
        else:
            status,body=400,{"error":"BAD_SCENARIO"}
        bodybytes=json.dumps(body).encode("utf8")
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(bodybytes)))
        self.end_headers()
        self.wfile.write(bodybytes)
    def do_POST(self):
        p=urlsplit(self.path)
        length=int(self.headers.get("Content-Length","0"))
        raw=self.rfile.read(length)
        try:
            payload=json.loads(raw)
        except ValueError:
            payload=None
        self.__class__.calls.append((self.command,p.path,"ack"))
        if p.path=="/vehicles/demo-001/diagnostics/ack" and payload=={"code":"P0100","operator":"synthetic-test"}:
            self.__class__.ack_events.append(payload)
            status,body=201,{"vehicleId":"demo-001","ack":"recorded"}
        else:
            status,body=422,{"error":"INVALID_ACK"}
        message=json.dumps(body).encode("utf8")
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(message)))
        self.end_headers()
        self.wfile.write(message)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cli",default="bru",help="Path to locally installed bru executable")
    args=p.parse_args()
    exe=shutil.which(args.cli)
    if exe is None:
        print(json.dumps({"ok":False,"test_executed":False,"reason":"Bruno CLI is not installed: "+args.cli}))
        return 2
    MockFleet.calls=[]
    MockFleet.ack_events=[]
    server=ThreadingHTTPServer(("127.0.0.1",0),MockFleet)
    thread=Thread(target=server.serve_forever,daemon=True)
    thread.start()
    try:
        model=json.loads((ROOT/"extensions/angent-ba/examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))
        model["environment"]["baseUrl"]="http://127.0.0.1:"+str(server.server_port)
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            for relative,body in compile_collection(model).items():
                target=folder/relative
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(body,encoding="utf8")
            command=[exe,"run","--env","Mock"]
            try:
                result=subprocess.run(command,cwd=folder,capture_output=True,text=True,timeout=90,errors="replace")
            except (OSError,subprocess.TimeoutExpired) as exc:
                print(json.dumps({"ok":False,"reason":str(exc)}))
                return 1
            visited=sorted(set(MockFleet.calls))
            expected=sorted([("GET","/vehicles/demo-001/status",s) for s in ("ok","denied","offline")] +
                            [("POST","/vehicles/demo-001/diagnostics/ack","ack")])
            expected_tests=sum(1+len(req.get("expected_json",{})) for req in model["requests"])
            expected_marker=str(expected_tests)+"/"+str(expected_tests)
            ok=(result.returncode==0 and visited==expected and len(MockFleet.calls)==4 and
                len(MockFleet.ack_events)==1 and expected_marker in result.stdout)
            print(json.dumps({"ok":ok,"test_executed":True,"cli_exit":result.returncode,
                              "calls":visited,"requested":len(MockFleet.calls),"mock_side_effects":len(MockFleet.ack_events),
                              "passing_tests_expected":expected_tests,
                              "stdout_tail":result.stdout[-2800:],"stderr_tail":result.stderr[-1800:]},ensure_ascii=False))
            return 0 if ok else 1
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)

if __name__=="__main__":
    raise SystemExit(main())
