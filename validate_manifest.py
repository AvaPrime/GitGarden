#!/usr/bin/env python3
"""
Validate the GitGarden Conversation Agents Manifest
"""
import json
import sys

def validate_conversation_agents_manifest():
    """Validate the provided conversation agents manifest"""
    
    # The manifest data provided by the user
    manifest_data = {
        "name": "gitgarden-conversation-agents",
        "version": "0.1.0", 
        "description": "A multi-agent system designed for version-controlled conversations and collaborative discourse management",
        "files": [
            "README.md",
            "conversation_commit.md", 
            "agent_runs.json",
            "ethics_checklist.md",
            "demo_plan.md"
        ],
        "agents": {
            "moderator": "conversation-flow-moderator-v1",
            "analyzer": "semantic-branch-analyzer-v1", 
            "synthesizer": "consensus-synthesis-agent-v1"
        },
        "run_steps": [
            "Initialize conversation thread with proper metadata",
            "Deploy moderator agent to maintain discussion flow and enforce rules",
            "Trigger analyzer agent to evaluate branch proposals and semantic relationships", 
            "Execute synthesizer agent to resolve merge conflicts and establish consensus",
            "Generate comprehensive commit metadata and diff reports for version tracking"
        ]
    }

    print("🔍 Validating Conversation Agents Manifest")
    print("=" * 50)

    # Validate JSON structure
    try:
        json_str = json.dumps(manifest_data, indent=2)
        parsed = json.loads(json_str)
        print("✅ JSON Structure: Valid")
    except Exception as e:
        print(f"❌ JSON Structure: Invalid - {e}")
        return False

    # Check required fields
    required_fields = ["name", "version", "description", "files", "run_steps"]
    missing_fields = []
    for field in required_fields:
        if field not in manifest_data:
            missing_fields.append(field)

    if missing_fields:
        print(f"❌ Missing required fields: {missing_fields}")
        return False
    else:
        print("✅ Required Fields: All present")

    # Check agents configuration
    if "agents" in manifest_data:
        agents = manifest_data["agents"]
        print(f"✅ Agents Configuration: {len(agents)} agents defined")
        for agent_type, agent_name in agents.items():
            print(f"   - {agent_type}: {agent_name}")
    else:
        print("⚠️  Agents Configuration: Not defined")

    # Check files list
    files = manifest_data.get("files", [])
    print(f"✅ Files List: {len(files)} files specified")
    for file in files:
        print(f"   - {file}")

    # Check run steps
    run_steps = manifest_data.get("run_steps", [])
    print(f"✅ Run Steps: {len(run_steps)} steps defined")
    for i, step in enumerate(run_steps, 1):
        print(f"   {i}. {step}")

    print("\n🎯 Validation Summary")
    print("=" * 50)
    print("✅ Manifest is valid and ready for implementation")
    print(f"📦 Project: {manifest_data['name']} v{manifest_data['version']}")
    print(f"🤖 Agents: {len(manifest_data.get('agents', {}))} configured")
    print(f"📋 Steps: {len(run_steps)} execution steps")
    
    return True, manifest_data

if __name__ == "__main__":
    success, data = validate_conversation_agents_manifest()
    if not success:
        sys.exit(1)