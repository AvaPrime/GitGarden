#!/usr/bin/env bash
# One-command runner: sends prompts to Claude, Gemini, and Ollama, then normalizes outputs.
set -euo pipefail

ROOT="$(pwd)"
OUT_RAW="${ROOT}/outputs/raw"
OUT_NORM="${ROOT}/outputs/normalized"
PROMPTS_DIR="${ROOT}/prompts"
ORCH_DIR="${ROOT}/orchestration"

mkdir -p "${OUT_RAW}" "${OUT_NORM}"

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

run_model() {
  local model="$1" prompt_file="$2" cmd="$3"
  local stamp="$(ts)"
  local out_file="${OUT_RAW}/${model}/${stamp}.txt"
  mkdir -p "$(dirname "${out_file}")"
  echo "[*] Running ${model} ..."
  # Execute command which must print to stdout
  eval "${cmd}" > "${out_file}"
  echo "[OK] Raw saved -> ${out_file}"
  # Normalize
  python tools/normalize_submission.py --input "${out_file}" --model "${model}" --outdir "outputs" --dashboard_csv "dashboard/sample.csv"
}

# Commands — edit models or endpoints as needed
# Require: CLAUDE_API_KEY, GEMINI_API_KEY; Ollama local assumed.
CLAUDE_CMD='CLAUDE_API_KEY=${CLAUDE_API_KEY} bash "${ORCH_DIR}/claude_curl.sh" "${PROMPTS_DIR}/claude.txt"'
GEMINI_CMD='GEMINI_API_KEY=${GEMINI_API_KEY} bash "${ORCH_DIR}/gemini_curl.sh" "${PROMPTS_DIR}/gemini.txt"'
OLLAMA_CMD='bash "${ORCH_DIR}/ollama_local.sh" "${PROMPTS_DIR}/ollama.txt"'

# Run selected models
[[ -n "${CLAUDE_API_KEY:-}" ]] && run_model "claude-sonnet" "${PROMPTS_DIR}/claude.txt" "${CLAUDE_CMD}" || echo "[skip] CLAUDE_API_KEY not set"
[[ -n "${GEMINI_API_KEY:-}" ]] && run_model "gemini-2.0-flash" "${PROMPTS_DIR}/gemini.txt" "${GEMINI_CMD}" || echo "[skip] GEMINI_API_KEY not set"
run_model "ollama-llama3.1-70b" "${PROMPTS_DIR}/ollama.txt" "${OLLAMA_CMD}" || true

echo "[DONE] See outputs/normalized and dashboard/sample.csv"
