#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/.hermes/vendor/agent-growth-protocol}"
SKILL_DIR="$HOME/.hermes/skills/autonomous-ai-agents/agent-growth-protocol"

mkdir -p "$(dirname "$REPO_DIR")" "$SKILL_DIR" "$HOME/.hermes/memories"

if [ -d "$REPO_DIR/.git" ]; then
  git -C "$REPO_DIR" pull --ff-only
else
  rm -rf "$REPO_DIR"
  git clone https://github.com/roverdude24/agent-growth-protocol.git "$REPO_DIR"
fi

cp "$REPO_DIR/hermes/SKILL.md" "$SKILL_DIR/SKILL.md"

echo "Agent Growth Policy (Hermes-native) installed."
echo "Skill: $SKILL_DIR/SKILL.md"
echo "This is a thin policy layer — uses Hermes hooks, memory, and cron natively."
