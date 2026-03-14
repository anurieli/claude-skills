#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="${HOME}/.claude"

echo "Installing Claude skills and commands from: ${REPO_DIR}"

# Ensure target directories exist
mkdir -p "${CLAUDE_DIR}/skills"
mkdir -p "${CLAUDE_DIR}/commands"

# Install skills (symlink each skill directory)
for skill_dir in "${REPO_DIR}"/skills/*/; do
  skill_name="$(basename "$skill_dir")"
  target="${CLAUDE_DIR}/skills/${skill_name}"

  if [ -L "$target" ]; then
    echo "  Updating symlink: skills/${skill_name}"
    rm "$target"
  elif [ -d "$target" ]; then
    echo "  Skipping skills/${skill_name} (already exists as a directory, not a symlink)"
    continue
  fi

  ln -s "$skill_dir" "$target"
  echo "  Linked: skills/${skill_name}"
done

# Install commands (symlink each command file)
for cmd_file in "${REPO_DIR}"/commands/*.md; do
  cmd_name="$(basename "$cmd_file")"
  target="${CLAUDE_DIR}/commands/${cmd_name}"

  if [ -L "$target" ]; then
    echo "  Updating symlink: commands/${cmd_name}"
    rm "$target"
  elif [ -f "$target" ]; then
    echo "  Skipping commands/${cmd_name} (already exists as a file, not a symlink)"
    continue
  fi

  ln -s "$cmd_file" "$target"
  echo "  Linked: commands/${cmd_name}"
done

echo ""
echo "Done! Installed skills and commands into ${CLAUDE_DIR}"
echo "To update later: git pull && ./install.sh"
