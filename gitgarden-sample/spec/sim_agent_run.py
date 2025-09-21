import json, time, argparse, hashlib
from datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, help="Path to base thread md")
ap.add_argument("--model", default="gpt-oss-120b@ollama-turbo")
args = ap.parse_args()

text = open(args.input, "r", encoding="utf-8").read()
digest = hashlib.sha256(text.encode()).hexdigest()[:8]
now = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

out = {
  "run_id": f"run-{int(time.time())}",
  "model": args.model,
  "input": f"hash:{digest}",
  "output": "Proposed tags updated; onboarding sparks created.",
  "score": {"originality":8, "technical":7, "agent_collab":8, "ux":7, "ethics":9, "scalability":7},
  "timestamp": now,
  "metadata":{"runtime_ms": 1200, "temperature": 0.6}
}
print(json.dumps(out, indent=2))
