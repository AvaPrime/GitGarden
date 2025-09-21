#!/usr/bin/env bash
# Usage: ./ollama_local.sh prompt.txt
set -euo pipefail
PROMPT_FILE=${1:-prompt.txt}
curl -sS http://localhost:11434/api/generate -d @- <<EOF
{{
  "model":"llama3.1:70b-instruct",
  "prompt": $(jq -Rs . < "${{PROMPT_FILE}}"),
  "stream": false
}}
EOF
