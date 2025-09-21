# GitGarden — AI Submission Sample (Option B: Agent Integration)

## Elevator pitch
GitGarden treats conversations as version-controlled artifacts. This sample demonstrates an **agent** that proposes branches and opens PRs to improve onboarding docs.

## Contents
- MANIFEST.json — machine-readable submission manifest
- commits/ — base thread + PR branch
- agent_runs/ — three example run stubs
- spec/ — repo format, validation hints, and tiny simulators
- ethics/ — short checklist
- orchestration/ — API templates for Claude, Gemini, and Ollama
- dashboard/ — CSV schema for comparing submissions

## Run steps (local)
1. Inspect commits: `less commits/*.md`
2. Validate manifest: `python spec/check_repo.py --manifest MANIFEST.json`
3. Simulate an agent run: `python spec/sim_agent_run.py --input commits/000_base_thread.md`
4. (Optional) Dry-run curl templates in `orchestration/` after inserting API keys.

## Authors & License
Authors: AI:gpt-oss-120b (example), Human: Phoenix  
License: MIT
