# GitGarden Tools Pack (A + C)

This pack adds:
- `tools/normalize_submission.py` — parses raw AI replies (single text blob) into a normalized repo tree.
- `tools/update_dashboard.py` — updates a CSV scoreboard with weighted totals.
- `tools/run_all.sh` — one-command runner that sends prompts to Claude, Gemini, and Ollama, stores raw outputs, normalizes them, and updates the dashboard.

## Quick Use (from inside your unzipped `gitgarden-sample/`)
1. Copy the `tools/` folder into your repo root (next to MANIFEST.json).
2. Ensure `orchestration/*.sh` and `prompts/*.txt` exist (from the sample pack).
3. Export API keys (if using cloud models):
   - `export CLAUDE_API_KEY=...`
   - `export GEMINI_API_KEY=...`
4. Run:
   - `bash tools/run_all.sh`

Outputs:
- Raw model replies: `outputs/raw/<model>/<timestamp>.txt`
- Normalized repos: `outputs/normalized/<model>/<timestamp>/...`
- Dashboard: appends rows to `dashboard/sample.csv` (creates if missing)

## Notes
- Normalizer expects sections labeled: MANIFEST, README, COMMIT, AGENT_RUNS, ETHICS, DEMO_PLAN, SELF_SCORE.
- It is resilient to fenced code blocks and minor formatting noise.
- SELF_SCORE parsing supports either six numbers or `key: value` lines; weighted score uses rubric weights.
