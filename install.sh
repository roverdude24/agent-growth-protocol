#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/.hermes/vendor/agent-growth-protocol}"
SKILL_DIR="$HOME/.hermes/skills/autonomous-ai-agents/agent-growth-protocol"
SCRIPT_DIR="$HOME/.hermes/scripts"

mkdir -p "$(dirname "$REPO_DIR")" "$SKILL_DIR" "$SCRIPT_DIR" "$HOME/.hermes/memories/agent_growth"

if [ -d "$REPO_DIR/.git" ]; then
  git -C "$REPO_DIR" pull --ff-only
else
  rm -rf "$REPO_DIR"
  git clone https://github.com/roverdude24/agent-growth-protocol.git "$REPO_DIR"
fi

cp "$REPO_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$REPO_DIR/scripts/agent_growth.py" "$SCRIPT_DIR/agent_growth.py"
chmod +x "$SCRIPT_DIR/agent_growth.py"

python3 "$SCRIPT_DIR/agent_growth.py" render-md >/dev/null

echo "Agent Growth Protocol installed."
echo "Skill:  $SKILL_DIR/SKILL.md"
echo "Script: $SCRIPT_DIR/agent_growth.py"
echo "Run:    python3 ~/.hermes/scripts/agent_growth.py report"
