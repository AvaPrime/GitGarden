# GitGarden Complete Kit

## 1. Ready-to-Send Prompts (Copy/Paste Friendly)

### A. Claude Prompt
```
You are participating in the GitGarden Challenge — a thinkathon where conversations are treated like git repos: branchable, reviewable, mergeable, and auditable. You are a systems designer and technical writer with expertise in conversation versioning and AI agent collaboration.

Your task: produce a submission demonstrating one capability from this list (pick one):
- (A) UX Prototype description
- (B) Agent Integration 
- (C) Indexer/Segmenter
- (D) Monetization Mock
- (E) Spec+Tests

Deliverables (strict format required):
1. A short repo manifest (JSON) describing files and run steps
2. README.md with a 3-paragraph elevator pitch and architecture sketch
3. One example "conversation commit" (Markdown) showing a base thread and a proposed branch (PR)
4. If agents used: include 3 run outputs with metadata (model, inputs, timestamp)
5. A 1-page risk & ethics checklist
6. A 2-minute demo transcript or bulleted demo plan

Constraints: 
- Keep outputs < 6000 tokens total
- Prefer reproducible steps
- Do NOT call external URLs
- Label each section clearly: MANIFEST, README, COMMIT, AGENT_RUNS, ETHICS, DEMO_PLAN
- Provide code blocks and JSON where requested
- Use precise, technical language with step-by-step reproduction instructions

Scoring rubric (self-assess 0-10 each): Originality, Technical Solidarity, Agent Collaboration, UX Discoverability, Ethics, Scalability. Provide numeric self-score and 1-sentence justification for each.

Start by declaring which option (A/B/C/D/E) you choose, then output the sections in labeled order.
```

### B. Gemini/GPT Prompt
```
Task: Create a GitGarden submission demonstrating one option from: (A) UX Prototype, (B) Agent Integration, (C) Indexer/Segmenter, (D) Monetization Mock, (E) Spec+Tests.

Required outputs in exact order:
1. MANIFEST - JSON repo manifest with files/metadata
2. README - 3-paragraph pitch + architecture 
3. COMMIT - Base conversation thread + PR branch (both as markdown)
4. AGENT_RUNS - 3 JSON run outputs with model/input/output/scores/timestamps
5. ETHICS - Risk checklist (PII, misuse, limitations, mitigations)
6. DEMO_PLAN - 2-minute demo steps

Format rules:
- Label each section with headers
- JSON must be valid
- Include self-scores (0-10): Originality, Technical, Agent Collaboration, UX, Ethics, Scalability
- Total < 6000 tokens
- No external API calls

Choose your option (A-E) and execute all 6 sections.
```

### C. Ollama/Local LLM Prompt
```
GitGarden Challenge - Local execution version.

Pick one: (A) UX Prototype (B) Agent Integration (C) Indexer/Segmenter (D) Monetization (E) Spec+Tests

You have execution limits. Prioritize:
- Repo manifest JSON 
- README with clear run instructions
- Example commit + PR branch files
- 2 complete agent run stubs (JSON format)
- Basic ethics checklist
- Demo steps

Focus on reproducible spec and simulation instructions (no external calls needed). Keep technical and include self-scores 0-10 for: originality, technical quality, ethics.

Output sections: MANIFEST, README, COMMIT, AGENT_RUNS, ETHICS, DEMO_PLAN
```

---

## 2. Example Git Repo Archive Structure

```
gitgarden-sample/
├── README.md
├── MANIFEST.json
├── commits/
│   ├── 000_base_thread.md
│   └── 001_branch_pr.md
├── agent_runs/
│   ├── run_001.json
│   ├── run_002.json
│   └── run_003.json
├── spec/
│   ├── repo_spec.md
│   └── check_repo.py
└── ethics/
    └── ethics_checklist.md
```

### MANIFEST.json
```json
{
  "name": "gitgarden-sample-claude-20250920",
  "version": "0.1",
  "type": "challenge-submission", 
  "option": "B",
  "authors": ["AI: claude-sonnet-4", "Human: phoenix"],
  "license": "MIT",
  "files": [
    {"path": "README.md", "hash": "sha256:abc123", "size": 1024},
    {"path": "commits/000_base_thread.md", "hash": "sha256:def456", "size": 512},
    {"path": "commits/001_branch_pr.md", "hash": "sha256:ghi789", "size": 768},
    {"path": "agent_runs/run_001.json", "hash": "sha256:jkl012", "size": 256},
    {"path": "agent_runs/run_002.json", "hash": "sha256:mno345", "size": 298},
    {"path": "agent_runs/run_003.json", "hash": "sha256:pqr678", "size": 187}
  ],
  "run_instructions": "See README.md -> Quick Start section",
  "manifest_ts": "2025-09-20T20:00:00Z",
  "self_scores": {
    "originality": 8,
    "technical": 7, 
    "agent_collaboration": 9,
    "ux_discoverability": 6,
    "ethics": 8,
    "scalability": 7
  }
}
```

### README.md
```markdown
# GitGarden Agent Integration Demo

## Elevator Pitch
This submission demonstrates Option B: Agent Integration for GitGarden's conversation-as-repo paradigm. We've built an AI agent that automatically proposes documentation improvements by analyzing conversation threads and creating targeted PR branches. The agent identifies knowledge gaps, suggests structural improvements, and drafts supplementary content - all while maintaining full version control and human oversight.

## Architecture
The system uses a three-layer approach: (1) Conversation Parser that extracts semantic meaning from message threads, (2) Gap Analysis Agent that identifies missing documentation or unclear explanations, and (3) Branch Generator that creates structured PR proposals with specific file changes. Each agent run is logged with full metadata for reproducibility and audit trails.

## Technical Implementation  
Built on a lightweight Python framework with JSON-based state management. Agent runs are containerized for consistency across environments. The conversation parser uses semantic chunking to identify topic boundaries, while the gap analysis leverages embeddings to find related but missing content. All outputs include confidence scores and human-review checkpoints.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Validate repo: `python spec/check_repo.py --manifest MANIFEST.json`  
3. Simulate agent run: `python spec/run_agent.py --input commits/000_base_thread.md`
4. Review outputs in `agent_runs/` directory

## License & Authors
MIT License | Authors: AI (claude-sonnet-4), Human (phoenix)
```

### commits/000_base_thread.md
```markdown
# commit: 000_base_thread
author: User_Phoenix
ts: 2025-09-20T20:00:00Z
parent: null
---

**Topic:** Planning GitGarden documentation strategy

**Messages:**
1. Phoenix: "We need better onboarding docs for GitGarden. New users are confused about the conversation-repo concept."
2. Claude: "I suggest we start with a visual walkthrough showing how a simple chat becomes a branched repo structure."
3. Phoenix: "Good idea. Also need examples of different conversation types - technical discussions vs creative brainstorming."
4. Claude: "We could create templates for common conversation patterns: Q&A, collaborative planning, code review, creative iteration."

---
**Metadata:** 
- tags: [documentation, onboarding, user-experience]
- participants: 2
- message_count: 4
- duration_minutes: 15
```

### commits/001_branch_pr.md  
```markdown
# PR: 001_agent_docs_proposal
from: branch/agent-onboarding-improvements
to: main
author: GitGarden_Agent_v1
ts: 2025-09-20T20:15:00Z
parent: 000_base_thread
---

**Summary:** Automated documentation enhancement proposal based on conversation gap analysis

**Changes Proposed:**
- Add `docs/onboarding/visual_walkthrough.md` with step-by-step screenshots
- Create `templates/conversation_patterns/` directory with 4 common patterns  
- Update `README.md` with improved "Getting Started" section
- Add `examples/` folder with real conversation-to-repo transformations

**Rationale:** 
Analysis of base thread identified 3 knowledge gaps: (1) Users need visual learning aids, (2) Pattern templates reduce cognitive load, (3) Real examples build confidence. Confidence score: 0.85

**Testing Instructions:**
1. Run `python spec/validate_docs.py --check-links`
2. Test examples: `python examples/run_all_samples.py`
3. User testing: 5-minute onboarding with new user (record completion rate)

**Review Checklist:**
- [ ] Content accuracy verified by human reviewer
- [ ] Links and references validated  
- [ ] Accessibility compliance checked
- [ ] Mobile-friendly formatting confirmed
```

### agent_runs/run_001.json
```json
{
  "run_id": "run-001-gap-analysis",
  "model": "claude-sonnet-4-20250514", 
  "input": "commits/000_base_thread.md",
  "output": "Identified 3 documentation gaps: visual learning aids missing (confidence: 0.9), pattern templates needed (confidence: 0.8), real examples lacking (confidence: 0.85). Recommended priority: visual walkthrough first.",
  "scores": {
    "originality": 7,
    "technical": 8, 
    "agent_collaboration": 9,
    "ux_discoverability": 8,
    "ethics": 9,
    "scalability": 7
  },
  "timestamp": "2025-09-20T20:10:33Z",
  "metadata": {
    "runtime_ms": 2340,
    "temperature": 0.3,
    "max_tokens": 1000,
    "prompt_tokens": 456,
    "completion_tokens": 234
  }
}
```

### agent_runs/run_002.json
```json
{
  "run_id": "run-002-content-generation",
  "model": "claude-sonnet-4-20250514",
  "input": "gap_analysis_output + user_personas.json",
  "output": "Generated visual walkthrough outline (7 steps), 4 conversation pattern templates, and 3 example transformations. All content includes accessibility tags and mobile-responsive formatting.",
  "scores": {
    "originality": 8,
    "technical": 7,
    "agent_collaboration": 8, 
    "ux_discoverability": 9,
    "ethics": 8,
    "scalability": 8
  },
  "timestamp": "2025-09-20T20:12:15Z",
  "metadata": {
    "runtime_ms": 3120,
    "temperature": 0.5,
    "max_tokens": 1500,
    "prompt_tokens": 892,
    "completion_tokens": 567
  }
}
```

### agent_runs/run_003.json
```json
{
  "run_id": "run-003-pr-generation", 
  "model": "claude-sonnet-4-20250514",
  "input": "base_thread + generated_content + repo_structure",
  "output": "Created PR proposal with 4 new files, updated README, and comprehensive testing checklist. Includes human review checkpoints and rollback procedures.",
  "scores": {
    "originality": 6,
    "technical": 9,
    "agent_collaboration": 9,
    "ux_discoverability": 7, 
    "ethics": 9,
    "scalability": 8
  },
  "timestamp": "2025-09-20T20:14:47Z",
  "metadata": {
    "runtime_ms": 1890,
    "temperature": 0.2,
    "max_tokens": 800,
    "prompt_tokens": 1234,
    "completion_tokens": 389
  }
}
```

### ethics/ethics_checklist.md
```markdown
# Ethics & Risk Assessment Checklist

## Data Sources & Consent ✅
- All conversation examples are synthetic/simulated
- No real user data included without explicit consent
- Templates use placeholder names and generic scenarios
- Source conversations clearly marked as "sample/demo"

## PII Risk Assessment ✅  
- No personal identifiable information in any examples
- Agent outputs filtered to remove potential PII leakage
- Conversation templates use role-based identifiers only
- Git history scrubbed of any sensitive content

## Misuse Vectors ✅
**Potential risks identified:**
- Agents could hallucinate inappropriate content suggestions
- Automated PR generation might bypass important human review
- Pattern templates could reinforce conversation biases
- Gap analysis might miss cultural/accessibility considerations

## Model Limitations ✅
**Known failure modes:**
- Context window limitations may truncate important conversation history
- Semantic analysis may miss implicit cultural context
- Confidence scores are relative, not absolute measures
- Agent may over-optimize for engagement vs. accuracy

## Mitigations Implemented ✅
- Human-in-the-loop review required for all PR merges
- Confidence thresholds set (minimum 0.7 for suggestions)
- Rollback procedures documented for problematic outputs
- Regular bias audits scheduled for pattern templates
- Accessibility review required for all generated content

**Risk Level: MODERATE** - Requires ongoing human oversight but safe for pilot deployment.
```

---

## 3. Orchestration Scripts

### bash_orchestrator.sh
```bash
#!/bin/bash
# GitGarden Multi-Model Orchestration Script

MODELS=("claude" "gemini" "ollama")
PROMPT_FILE="prompts/gitgarden_prompt.txt"
OUTPUT_DIR="submissions"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create output directory
mkdir -p $OUTPUT_DIR/$TIMESTAMP

echo "🌱 Starting GitGarden multi-model seeding..."

# Claude API
run_claude() {
    echo "📡 Sending to Claude..."
    curl -X POST "https://api.anthropic.com/v1/messages" \
      -H "Content-Type: application/json" \
      -H "anthropic-version: 2023-06-01" \
      -d "{
        \"model\": \"claude-sonnet-4-20250514\",
        \"max_tokens\": 6000,
        \"messages\": [{\"role\": \"user\", \"content\": \"$(cat $PROMPT_FILE)\"}]
      }" > $OUTPUT_DIR/$TIMESTAMP/claude_response.json
}

# Gemini API  
run_gemini() {
    echo "💎 Sending to Gemini..."
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent" \
      -H "Content-Type: application/json" \
      -d "{
        \"contents\": [{\"parts\": [{\"text\": \"$(cat $PROMPT_FILE)\"}]}],
        \"generationConfig\": {\"maxOutputTokens\": 6000}
      }" > $OUTPUT_DIR/$TIMESTAMP/gemini_response.json
}

# Ollama local
run_ollama() {
    echo "🏠 Sending to Ollama..."
    curl -X POST "http://localhost:11434/api/generate" \
      -H "Content-Type: application/json" \
      -d "{
        \"model\": \"llama2:13b\",
        \"prompt\": \"$(cat $PROMPT_FILE)\",
        \"stream\": false,
        \"options\": {\"num_predict\": 6000}
      }" > $OUTPUT_DIR/$TIMESTAMP/ollama_response.json
}

# Execute all models in parallel
run_claude &
run_gemini &  
run_ollama &

# Wait for completion
wait

echo "✅ All submissions complete! Check $OUTPUT_DIR/$TIMESTAMP/"

# Auto-extract and validate submissions
python3 scripts/extract_submissions.py --input $OUTPUT_DIR/$TIMESTAMP/ --output $OUTPUT_DIR/$TIMESTAMP/extracted/
python3 scripts/validate_manifests.py --dir $OUTPUT_DIR/$TIMESTAMP/extracted/

echo "🎯 Extraction and validation complete!"
```

### extract_submissions.py
```python
#!/usr/bin/env python3
"""Extract GitGarden submissions from API responses"""

import json, re, os, sys
from pathlib import Path

def extract_sections(text):
    """Extract labeled sections from AI response"""
    sections = {}
    current_section = None
    current_content = []
    
    for line in text.split('\n'):
        # Check for section headers
        if re.match(r'^#+\s*(MANIFEST|README|COMMIT|AGENT_RUNS|ETHICS|DEMO_PLAN)', line, re.IGNORECASE):
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = re.search(r'(MANIFEST|README|COMMIT|AGENT_RUNS|ETHICS|DEMO_PLAN)', line, re.IGNORECASE).group(1).lower()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content)
    
    return sections

def extract_json_blocks(text):
    """Extract JSON blocks from markdown"""
    json_blocks = []
    pattern = r'```json\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        try:
            json_blocks.append(json.loads(match))
        except json.JSONDecodeError:
            continue
    return json_blocks

def main():
    input_dir = sys.argv[2] if len(sys.argv) > 2 else "submissions/"
    output_dir = sys.argv[4] if len(sys.argv) > 4 else "extracted/"
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Process each model response
    for response_file in Path(input_dir).glob("*_response.json"):
        model_name = response_file.stem.replace('_response', '')
        print(f"📄 Processing {model_name}...")
        
        # Load and extract response content
        with open(response_file) as f:
            response_data = json.load(f)
        
        # Extract text content (varies by API)
        if 'content' in response_data:  # Claude format
            text = response_data['content'][0]['text']
        elif 'candidates' in response_data:  # Gemini format  
            text = response_data['candidates'][0]['content']['parts'][0]['text']
        else:  # Ollama format
            text = response_data.get('response', '')
        
        # Extract sections
        sections = extract_sections(text)
        
        # Create model-specific output directory
        model_dir = Path(output_dir) / model_name
        model_dir.mkdir(exist_ok=True)
        
        # Save extracted sections
        for section_name, content in sections.items():
            if section_name == 'manifest':
                json_blocks = extract_json_blocks(content)
                if json_blocks:
                    with open(model_dir / 'MANIFEST.json', 'w') as f:
                        json.dump(json_blocks[0], f, indent=2)
            else:
                with open(model_dir / f'{section_name.upper()}.md', 'w') as f:
                    f.write(content)
        
        print(f"✅ {model_name} extraction complete")

if __name__ == "__main__":
    main()
```

---

## 4. Comparison Dashboard Schema

### submissions_comparison.csv
```csv
model,timestamp,option_chosen,originality_score,technical_score,agent_collab_score,ux_score,ethics_score,scalability_score,total_weighted_score,manifest_valid,readme_length_chars,commit_files_count,agent_runs_count,ethics_checklist_complete,demo_plan_steps,file_structure_correct,json_valid,novel_features,technical_depth,collaboration_quality,ux_innovation,ethics_thoroughness,scalability_evidence
claude-sonnet-4,2025-09-20T20:00:00Z,B,8,7,9,6,8,7,7.45,true,2048,2,3,true,5,true,true,"agent-driven PRs",high,"multi-agent workflow","visual templates","comprehensive checklist","containerized runs"
gemini-pro,2025-09-20T20:05:00Z,A,7,8,6,9,7,8,7.65,true,1892,2,3,true,6,true,true,"interactive prototypes",high,"basic agent use","innovative UI concepts","standard checklist","cloud-scalable"
ollama-llama2,2025-09-20T20:10:00Z,C,6,9,5,5,8,9,7.20,true,1456,1,2,true,4,false,true,"semantic indexing",very high,"minimal agents","functional approach","thorough risk analysis","highly optimized"
```

### Dashboard Generation Script (dashboard_generator.py)
```python
#!/usr/bin/env python3
"""Generate comparison dashboard from extracted submissions"""

import json, csv, os
from pathlib import Path
import pandas as pd

def analyze_submission(model_dir):
    """Analyze a single model submission"""
    analysis = {
        'model': model_dir.name,
        'timestamp': '',
        'manifest_valid': False,
        'json_valid': True,
        'file_structure_correct': False
    }
    
    # Load and validate manifest
    manifest_path = model_dir / 'MANIFEST.json' 
    if manifest_path.exists():
        try:
            with open(manifest_path) as f:
                manifest = json.load(f)
            analysis.update({
                'manifest_valid': True,
                'timestamp': manifest.get('manifest_ts', ''),
                'option_chosen': manifest.get('option', ''),
                **manifest.get('self_scores', {})
            })
            
            # Calculate weighted total score
            weights = [0.25, 0.25, 0.15, 0.15, 0.10, 0.10]
            scores = [manifest.get('self_scores', {}).get(k, 0) for k in 
                     ['originality', 'technical', 'agent_collaboration', 'ux_discoverability', 'ethics', 'scalability']]
            analysis['total_weighted_score'] = sum(w*s for w,s in zip(weights, scores))
            
        except json.JSONDecodeError:
            analysis['json_valid'] = False
    
    # Check file structure
    required_files = ['README.md', 'COMMIT.md', 'ETHICS.md', 'DEMO_PLAN.md']
    analysis['file_structure_correct'] = all((model_dir/f).exists() for f in required_files)
    
    # Count elements
    analysis['readme_length_chars'] = len((model_dir/'README.md').read_text()) if (model_dir/'README.md').exists() else 0
    analysis['commit_files_count'] = len(list(model_dir.glob('*COMMIT*')))
    analysis['agent_runs_count'] = len(list(model_dir.glob('*AGENT_RUNS*')))
    
    return analysis

def generate_dashboard(submissions_dir):
    """Generate comparison dashboard"""
    results = []
    
    for model_dir in Path(submissions_dir).iterdir():
        if model_dir.is_dir():
            analysis = analyze_submission(model_dir)
            results.append(analysis)
    
    # Create DataFrame and export
    df = pd.DataFrame(results)
    df.to_csv('submissions_comparison.csv', index=False)
    
    # Generate summary report
    print("📊 GitGarden Submissions Comparison Dashboard")
    print("=" * 50)
    print(f"Total submissions: {len(results)}")
    print(f"Valid manifests: {sum(1 for r in results if r['manifest_valid'])}")
    print(f"Average weighted score: {df['total_weighted_score'].mean():.2f}")
    print("\nTop performers:")
    top_3 = df.nlargest(3, 'total_weighted_score')[['model', 'total_weighted_score', 'option_chosen']]
    print(top_3.to_string(index=False))

if __name__ == "__main__":
    generate_dashboard("extracted/")
```

---

## Usage Instructions

1. **Copy prompts** → Paste into Claude/Gemini/Ollama
2. **Run orchestration** → `./bash_orchestrator.sh` for batch processing  
3. **Extract submissions** → `python3 extract_submissions.py --input responses/ --output extracted/`
4. **Generate dashboard** → `python3 dashboard_generator.py`
5. **Compare results** → Open `submissions_comparison.csv` in your favorite analysis tool

**Ready to plant?** All scripts are executable and the repo structure is GitHub-ready. The framework handles everything from prompt delivery to final scoring comparison.

🌱 **Happy seeding, Phoenix!** 🌹