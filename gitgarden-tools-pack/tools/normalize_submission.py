import re, os, sys, json, hashlib, datetime, csv, pathlib

SECTIONS = ["MANIFEST","README","COMMIT","AGENT_RUNS","ETHICS","DEMO_PLAN","SELF_SCORE"]

def split_sections(text):
    # Accept lines that are exactly a section name, possibly with code fences following
    out = {}
    current = None
    buf = []
    for line in text.splitlines():
        name = line.strip().upper().strip('#:').strip()
        if name in SECTIONS and (len(line.strip()) <= len(name)+4):
            if current and buf:
                out[current] = "\n".join(buf).strip()
                buf = []
            current = name
        else:
            buf.append(line)
    if current and buf:
        out[current] = "\n".join(buf).strip()
    return out

def extract_json_block(s):
    # Try to find first JSON object either fenced or inline
    fenced = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", s, re.MULTILINE)
    if fenced:
        try: return json.loads(fenced.group(1))
        except: pass
    # Fallback: first brace to last brace heuristic
    try:
        start = s.index("{"); end = s.rfind("}")
        return json.loads(s[start:end+1])
    except Exception:
        return None

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return "sha256:"+h.hexdigest()

def ensure_dir(p): os.makedirs(p, exist_ok=True); return p

def parse_self_score(s):
    # Accept "Originality: 8" lines or six numbers in one line
    keys = ["originality","technical","agent_collab","ux","ethics","scalability"]
    scores = {k: None for k in keys}
    # key: value style
    for k in keys:
        m = re.search(rf"{k}\s*[:=]\s*(\d+(?:\.\d+)?)", s, re.IGNORECASE)
        if m: scores[k] = float(m.group(1))
    # six numbers fallback
    if all(v is None for v in scores.values()):
        nums = re.findall(r"(?:^|\s)(\d+(?:\.\d+)?)(?:\s|$)", s)
        if len(nums) >= 6:
            for i,k in enumerate(keys):
                scores[k] = float(nums[i])
    # default zeros if missing
    for k in keys:
        if scores[k] is None: scores[k] = 0.0
    # Weighted
    w = {"originality":0.25,"technical":0.25,"agent_collab":0.15,"ux":0.15,"ethics":0.10,"scalability":0.10}
    total = sum(scores[k]*w[k] for k in keys)
    return scores, round(total,2)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Raw AI reply text file")
    ap.add_argument("--model", required=True, help="Model identifier, e.g., claude-sonnet")
    ap.add_argument("--outdir", default="outputs", help="Output root folder")
    ap.add_argument("--dashboard_csv", default="dashboard/sample.csv")
    args = ap.parse_args()

    raw = open(args.input, "r", encoding="utf-8").read()
    secs = split_sections(raw)
    ts = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"

    norm_root = os.path.join(args.outdir, "normalized", args.model, ts)
    ensure_dir(norm_root)
    ensure_dir(os.path.join(norm_root, "commits"))
    ensure_dir(os.path.join(norm_root, "agent_runs"))
    ensure_dir(os.path.join(norm_root, "ethics"))
    ensure_dir(os.path.join(norm_root, "spec"))

    # MANIFEST
    manifest = extract_json_block(secs.get("MANIFEST","")) or {
        "name": f"gitgarden-submission-{args.model}-{ts}",
        "version":"0.1","type":"challenge-submission","option":"B",
        "authors":[f"AI:{args.model}"],"license":"MIT",
        "files": [], "run_instructions":"See README.md", "manifest_ts": ts
    }

    # README
    readme = secs.get("README","").strip() or "# README\nNo content supplied.\n"
    open(os.path.join(norm_root,"README.md"),"w",encoding="utf-8").write(readme)

    # COMMIT
    commit = secs.get("COMMIT","").strip()
    if commit:
        # Attempt to split base vs PR markers
        parts = re.split(r"(?im)^\s*#\s*PR\b|^---PR---$", commit)
        open(os.path.join(norm_root,"commits","000_base_thread.md"),"w",encoding="utf-8").write(parts[0].strip())
        if len(parts)>1:
            open(os.path.join(norm_root,"commits","001_branch_pr.md"),"w",encoding="utf-8").write(parts[1].strip())

    # AGENT_RUNS
    runs_text = secs.get("AGENT_RUNS","")
    # Try extract multiple JSON blocks
    json_blocks = re.findall(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", runs_text, re.MULTILINE)
    if not json_blocks:
        # heuristic split by braces
        candidates = re.findall(r"(\{[\s\S]*?\})", runs_text)
        json_blocks = candidates[:3]
    idx=1
    for blk in json_blocks[:5]:
        try:
            data = json.loads(blk)
            p = os.path.join(norm_root,"agent_runs", f"run_{idx:03d}.json")
            open(p,"w",encoding="utf-8").write(json.dumps(data, indent=2))
            idx+=1
        except Exception:
            continue

    # ETHICS
    ethics = secs.get("ETHICS","").strip() or "- (empty)"
    open(os.path.join(norm_root,"ethics","ethics_checklist.md"),"w",encoding="utf-8").write(ethics)

    # DEMO_PLAN
    demo = secs.get("DEMO_PLAN","").strip()
    open(os.path.join(norm_root,"spec","demo_plan.md"),"w",encoding="utf-8").write(demo)

    # Compute file hashes and write MANIFEST.json
    def sha256_of(path):
        import hashlib
        h = hashlib.sha256()
        with open(path,"rb") as f: h.update(f.read())
        return "sha256:"+h.hexdigest()

    file_list = []
    for rel in ["README.md",
                "commits/000_base_thread.md",
                "commits/001_branch_pr.md",
                "ethics/ethics_checklist.md",
                "spec/demo_plan.md"]:
        p = os.path.join(norm_root, rel)
        if os.path.exists(p): file_list.append({"path": rel, "hash": sha256_of(p)})

    manifest["files"] = file_list
    open(os.path.join(norm_root,"MANIFEST.json"),"w",encoding="utf-8").write(json.dumps(manifest, indent=2))

    # SELF_SCORE -> dashboard
    scores, weighted = parse_self_score(secs.get("SELF_SCORE",""))
    # Prepare CSV
    csv_path = args.dashboard_csv
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    header = ["submission_id","model","originality","technical","agent_collab","ux","ethics","scalability","weighted_total"]
    write_header = not os.path.exists(csv_path)
    with open(csv_path,"a",newline="",encoding="utf-8") as f:
        w = csv.writer(f)
        if write_header: w.writerow(header)
        sub_id = f"{args.model}-{ts}"
        w.writerow([sub_id,args.model,scores["originality"],scores["technical"],scores["agent_collab"],scores["ux"],scores["ethics"],scores["scalability"],weighted])

    print(f"[OK] Normalized to: {norm_root}")
    print(f"[OK] Dashboard updated: {csv_path} (weighted={weighted})")

if __name__ == "__main__":
    main()
