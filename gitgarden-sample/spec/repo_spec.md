# GitGarden Repo Spec (v0.1)

- MANIFEST.json with fields: name, version, type, option, authors, license, files[], run_instructions, manifest_ts.
- commits/: ordered markdown files with headers and metadata.
- agent_runs/: JSON files with run_id, model, input, output, score{{...}}, timestamp, metadata.
- ethics/: ethics_checklist.md required.
- spec/: may contain check_repo.py and sim_agent_run.py.
