# GitGarden Conversation Agents

A multi-agent system designed for version-controlled conversations and collaborative discourse management.

## 🎯 Overview

The GitGarden Conversation Agents system enables structured, version-controlled conversations through a collaborative multi-agent approach. This system treats conversations like code repositories, with branching, merging, and commit-style tracking of discourse evolution.

## 🤖 Agent Architecture

### Core Agents

| Agent | Version | Purpose |
|-------|---------|---------|
| **Moderator** | `conversation-flow-moderator-v1` | Maintains discussion flow and enforces conversation rules |
| **Analyzer** | `semantic-branch-analyzer-v1` | Evaluates branch proposals and semantic relationships |
| **Synthesizer** | `consensus-synthesis-agent-v1` | Resolves merge conflicts and establishes consensus |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git 2.30+
- GitGarden toolkit

### Installation
```bash
# Clone the conversation agents
git clone <repository-url>
cd conversation-agents

# Initialize conversation environment
python setup.py install
```

### Basic Usage
```bash
# Initialize a new conversation thread
python -m conversation_agents init --topic "Your Discussion Topic"

# Deploy agents for collaborative discourse
python -m conversation_agents run --config configs/default.json

# Generate conversation commit
python -m conversation_agents commit --message "Consensus reached on topic X"
```

## 📋 Execution Flow

The system follows a structured 5-step execution process:

1. **Initialize Conversation Thread**
   - Create proper metadata structure
   - Set up version control for discourse
   - Define conversation parameters

2. **Deploy Moderator Agent**
   - Maintain discussion flow
   - Enforce conversation rules
   - Monitor participant engagement

3. **Trigger Analyzer Agent**
   - Evaluate branch proposals
   - Analyze semantic relationships
   - Identify conversation patterns

4. **Execute Synthesizer Agent**
   - Resolve merge conflicts in discourse
   - Establish consensus points
   - Generate unified perspectives

5. **Generate Commit Metadata**
   - Create comprehensive diff reports
   - Track version changes
   - Document conversation evolution

## 📁 Project Structure

```
conversation-agents/
├── agents/                 # Agent implementations
│   ├── moderator/         # Flow moderation logic
│   ├── analyzer/          # Semantic analysis tools
│   └── synthesizer/       # Consensus building algorithms
├── configs/               # Configuration files
│   ├── default.json       # Default agent settings
│   └── custom/           # Custom configurations
├── templates/             # Conversation templates
│   ├── discussion.md      # Discussion thread template
│   └── consensus.md       # Consensus document template
├── runs/                  # Execution logs and results
└── docs/                  # Additional documentation
```

## 🔧 Configuration

### Agent Configuration
Each agent can be configured through JSON files in the `configs/` directory:

```json
{
  "moderator": {
    "rules_enforcement": "strict",
    "flow_control": "adaptive",
    "intervention_threshold": 0.7
  },
  "analyzer": {
    "semantic_depth": "deep",
    "relationship_mapping": true,
    "pattern_detection": "advanced"
  },
  "synthesizer": {
    "consensus_algorithm": "weighted_voting",
    "conflict_resolution": "mediated",
    "output_format": "structured"
  }
}
```

## 📊 Conversation Tracking

The system maintains detailed logs of conversation evolution:

- **Branch Points**: Where discussions diverge
- **Merge Events**: Consensus achievement moments  
- **Conflict Resolution**: How disagreements were resolved
- **Participant Contributions**: Individual input tracking
- **Semantic Evolution**: How ideas developed over time

## 🛡️ Ethics & Safety

This system includes built-in ethical safeguards:

- **Bias Detection**: Monitors for discriminatory patterns
- **Harassment Prevention**: Automatic intervention for toxic behavior
- **Privacy Protection**: Anonymization options for sensitive discussions
- **Consent Management**: Explicit agreement for conversation recording

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [GitGarden Core](../README.md) - Main GitGarden toolkit
- [Agent Orchestration](../orchestration/) - Multi-agent coordination tools
- [Conversation Analytics](../analytics/) - Discourse analysis utilities

---

**Version**: 0.1.0  
**Last Updated**: January 21, 2025  
**Maintainers**: GitGarden Community