#!/usr/bin/env bash
# Usage: GEMINI_API_KEY=... ./gemini_curl.sh prompt.txt
set -euo pipefail
PROMPT_FILE=${1:-prompt.txt}
curl -sS "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}" \  -H 'Content-Type: application/json' \  -d @- <<EOF
{{
  "contents": [{{"parts":[{{"text": $(jq -Rs . < "${{PROMPT_FILE}}") }}]}}]
}}
EOF
