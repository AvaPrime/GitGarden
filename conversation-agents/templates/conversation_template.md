# Conversation Template

## Metadata
- **Conversation ID**: `{conversation_id}`
- **Title**: `{conversation_title}`
- **Created**: `{timestamp}`
- **Participants**: `{participant_list}`
- **Topic**: `{main_topic}`
- **Status**: `{status}` (active/paused/completed/archived)

## Conversation Flow

### Initial Setup
```json
{
  "moderator_agent": "conversation-flow-moderator-v1",
  "analyzer_agent": "semantic-branch-analyzer-v1", 
  "synthesizer_agent": "consensus-synthesis-agent-v1",
  "conversation_rules": {
    "max_participants": 10,
    "time_limit": 3600,
    "moderation_level": "standard",
    "branch_threshold": 0.7
  }
}
```

### Discussion Phases

#### Phase 1: Topic Introduction
- **Objective**: Establish shared understanding of the topic
- **Duration**: 10-15 minutes
- **Moderator Actions**:
  - Welcome participants
  - Present topic and objectives
  - Establish ground rules
  - Invite initial perspectives

#### Phase 2: Perspective Gathering
- **Objective**: Collect diverse viewpoints and evidence
- **Duration**: 20-30 minutes
- **Analyzer Actions**:
  - Track emerging themes
  - Identify potential branches
  - Monitor semantic relationships
  - Flag areas of convergence/divergence

#### Phase 3: Deep Exploration
- **Objective**: Explore key areas in detail
- **Duration**: 15-25 minutes
- **Agent Coordination**:
  - Moderator guides focus areas
  - Analyzer identifies branch points
  - Synthesizer prepares integration strategies

#### Phase 4: Synthesis & Resolution
- **Objective**: Build consensus and resolve conflicts
- **Duration**: 10-20 minutes
- **Synthesizer Actions**:
  - Present synthesis proposals
  - Facilitate conflict resolution
  - Guide consensus building
  - Generate final agreements

## Conversation Branches

### Branch Template
```markdown
### Branch: {branch_name}
- **Created**: {timestamp}
- **Trigger**: {branching_reason}
- **Participants**: {branch_participants}
- **Status**: {active/merged/abandoned}

#### Discussion Points
1. {point_1}
2. {point_2}
3. {point_3}

#### Outcomes
- **Consensus Level**: {percentage}
- **Key Insights**: {insights_list}
- **Action Items**: {action_items}
```

## Participant Tracking

### Participant Template
```json
{
  "participant_id": "{unique_id}",
  "name": "{display_name}",
  "role": "{role}",
  "expertise_areas": ["{area_1}", "{area_2}"],
  "participation_metrics": {
    "messages_sent": 0,
    "questions_asked": 0,
    "evidence_provided": 0,
    "agreements_made": 0,
    "conflicts_initiated": 0
  },
  "engagement_level": "high/medium/low",
  "communication_style": "{style_description}"
}
```

## Message Structure

### Standard Message Format
```json
{
  "message_id": "{unique_id}",
  "timestamp": "{iso_timestamp}",
  "participant_id": "{sender_id}",
  "content": "{message_content}",
  "message_type": "statement/question/evidence/agreement/disagreement",
  "branch_id": "{current_branch}",
  "references": ["{referenced_message_ids}"],
  "semantic_tags": ["{tag_1}", "{tag_2}"],
  "sentiment": "{positive/neutral/negative}",
  "confidence": 0.85
}
```

## Agent Interventions

### Moderator Interventions
- **Flow Management**: Redirect off-topic discussions
- **Participation Balance**: Encourage quiet participants
- **Conflict De-escalation**: Manage heated exchanges
- **Time Management**: Keep discussion on schedule

### Analyzer Interventions
- **Branch Identification**: Suggest when to create new branches
- **Semantic Clarification**: Request clarification on ambiguous terms
- **Pattern Recognition**: Highlight recurring themes or arguments
- **Relationship Mapping**: Show connections between ideas

### Synthesizer Interventions
- **Consensus Building**: Propose areas of agreement
- **Conflict Resolution**: Mediate disagreements
- **Summary Generation**: Provide periodic summaries
- **Decision Facilitation**: Guide toward actionable outcomes

## Quality Metrics

### Conversation Health
- **Participation Balance**: Distribution of contributions
- **Semantic Coherence**: Logical flow and consistency
- **Conflict Resolution Rate**: Successfully resolved disagreements
- **Consensus Achievement**: Level of final agreement
- **Actionable Outcomes**: Concrete next steps identified

### Agent Performance
- **Moderator Effectiveness**: Flow management success
- **Analyzer Accuracy**: Correct branch and pattern identification
- **Synthesizer Success**: Consensus building achievement
- **Coordination Quality**: Inter-agent collaboration effectiveness

## Conversation Commit

### Commit Structure
```json
{
  "commit_id": "{unique_hash}",
  "timestamp": "{iso_timestamp}",
  "summary": "{brief_description}",
  "changes": {
    "new_branches": ["{branch_ids}"],
    "merged_branches": ["{branch_ids}"],
    "consensus_points": ["{agreements}"],
    "unresolved_conflicts": ["{conflicts}"]
  },
  "participants": ["{participant_ids}"],
  "agent_actions": {
    "moderator": ["{actions}"],
    "analyzer": ["{actions}"],
    "synthesizer": ["{actions}"]
  },
  "metrics": {
    "duration": 1800,
    "message_count": 45,
    "branch_count": 3,
    "consensus_level": 0.82
  }
}
```

## Export Formats

### Summary Report
- Executive summary of key outcomes
- Participant contributions overview
- Consensus areas and remaining disagreements
- Recommended next steps
- Lessons learned and process improvements

### Technical Log
- Complete message history with metadata
- Agent intervention log with reasoning
- Branch creation and merge history
- Performance metrics and analytics
- Error log and system events

### Action Plan
- Concrete next steps with ownership
- Timeline and milestones
- Success criteria and metrics
- Follow-up conversation scheduling
- Resource requirements and dependencies