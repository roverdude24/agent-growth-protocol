#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/.agent-growth-protocol}"
SKILL_DIR="$HOME/.hermes/skills/autonomous-ai-agents/agent-growth-protocol"
SCRIPT_DIR="$HOME/.agent_growth/bin"
DATA_DIR="$HOME/.agent_growth"

mkdir -p "$(dirname "$REPO_DIR")" "$SKILL_DIR" "$SCRIPT_DIR" "$DATA_DIR"

if [ -d "$REPO_DIR/.git" ]; then
  git -C "$REPO_DIR" pull --ff-only
else
  rm -rf "$REPO_DIR"
  git clone https://github.com/roverdude24/agent-growth-protocol.git "$REPO_DIR"
fi

cp "$REPO_DIR/standalone/SKILL-standalone.md" "$SKILL_DIR/SKILL.md"
cp "$REPO_DIR/standalone/agent_growth.py" "$SCRIPT_DIR/agent_growth.py"
chmod +x "$SCRIPT_DIR/agent_growth.py"

python3 "$SCRIPT_DIR/agent_growth.py" init >/dev/null 2>&1
python3 "$SCRIPT_DIR/agent_growth.py" render-md >/dev/null

echo "Agent Growth Protocol (Standalone) installed."
echo "Database: $DATA_DIR/growth.db"
echo "Script:   $SCRIPT_DIR/agent_growth.py"
echo "Skill:    $SKILL_DIR/SKILL.md"
echo ""
echo "Quick start:"
echo "  python3 $SCRIPT_DIR/agent_growth.py report"
echo "  python3 $SCRIPT_DIR/agent_growth.py add-learning --topic tool:x --problem '...' --fix '...'"
echo "  python3 $SCRIPT_DIR/agent_growth.py session-start"
