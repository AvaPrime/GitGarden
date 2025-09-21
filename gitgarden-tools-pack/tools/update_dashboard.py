import csv, sys

def weighted_total(row):
    o = float(row["originality"]); t=float(row["technical"]); a=float(row["agent_collab"])
    ux=float(row["ux"]); e=float(row["ethics"]); s=float(row["scalability"])
    return round(0.25*o+0.25*t+0.15*a+0.15*ux+0.10*e+0.10*s,2)

def main(csv_path):
    rows=[]
    with open(csv_path, newline="", encoding="utf-8") as f:
        r=csv.DictReader(f)
        for row in r:
            row["weighted_total"]=weighted_total(row)
            rows.append(row)
    rows.sort(key=lambda r: float(r["weighted_total"]), reverse=True)
    print("Rank,Submission,Model,Weighted")
    for i,row in enumerate(rows,1):
        print(i,row["submission_id"],row["model"],row["weighted_total"])
if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python tools/update_dashboard.py dashboard/sample.csv"); sys.exit(1)
    main(sys.argv[1])
