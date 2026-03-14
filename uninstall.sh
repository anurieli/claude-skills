#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="${HOME}/.claude"

echo "Removing symlinked skills and commands..."

# Remove skill symlinks that point into this repo
for skill_dir in "${REPO_DIR}"/skills/*/; do
  skill_name="$(basename "$skill_dir")"
  target="${CLAUDE_DIR}/skills/${skill_name}"

  if [ -L "$target" ]; then
    rm "$target"
    echo "  Removed: skills/${skill_name}"
  fi
done

# Remove command symlinks that point into this repo
for cmd_file in "${REPO_DIR}"/commands/*.md; do
  cmd_name="$(basename "$cmd_file")"
  target="${CLAUDE_DIR}/commands/${cmd_name}"

  if [ -L "$target" ]; then
    rm "$target"
    echo "  Removed: commands/${cmd_name}"
  fi
done

echo ""
echo "Done! Symlinks removed. Original files in this repo are untouched."
