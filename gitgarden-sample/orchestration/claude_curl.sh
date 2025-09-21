#!/usr/bin/env bash
# Usage: CLAUDE_API_KEY=... ./claude_curl.sh prompt.txt
set -euo pipefail
PROMPT_FILE=${1:-prompt.txt}
curl https://api.anthropic.com/v1/messages \  -H "x-api-key: ${CLAUDE_API_KEY}" \  -H "anthropic-version: 2023-06-01" \  -H "content-type: application/json" \  -d @- <<EOF
{{
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 4000,
  "messages": [{{"role":"user","content": $(jq -Rs . < "${{PROMPT_FILE}}")}}]
}}
EOF
