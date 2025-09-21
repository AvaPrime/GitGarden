import json, sys, os, glob

def e(msg): 
    print("[ERROR]", msg); 
    sys.exit(1)

def info(msg): 
    print("[OK]", msg)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="MANIFEST.json")
    ap.add_argument("--validate", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(args.manifest):
        e(f"Manifest not found: {args.manifest}")
    man = json.load(open(args.manifest))

    required_top = ["name","version","type","option","authors","license","files","run_instructions","manifest_ts"]
    for k in required_top:
        if k not in man:
            e(f"Manifest missing key: {k}")
    info("Manifest top-level keys present.")

    # Basic structure checks
    for path in ["commits/000_base_thread.md", "commits/001_branch_pr.md", "ethics/ethics_checklist.md"]:
        if not os.path.exists(path):
            e(f"Missing required file: {path}")
    info("Core files present.")

    runs = glob.glob("agent_runs/*.json")
    if len(runs) < 1:
        print("[WARN] No agent_runs/*.json found (ok for non-agent options)")
    else:
        info(f"Found {len(runs)} agent run(s).")

    print("Validation complete.")

if __name__ == "__main__":
    main()
