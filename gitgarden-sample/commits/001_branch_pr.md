# PR: 001_proposed_agent_pr
from: branch/agent-proposal
to: main
author: agent_GPT-OSS-120B
ts: 2025-09-20T21:12:45Z
---
**Summary:** Agent automates branch creation for onboarding docs.
**Changes:** adds `spec/agent_manifest.yaml` and `commits/onboarding_sparks.md`
**Rationale:** Improves discovery and speeds onboarding.
**Testing:** run `python spec/check_repo.py --validate` (spec included)
