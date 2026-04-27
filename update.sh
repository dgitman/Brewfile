#!/bin/bash
set -euo pipefail

BREWFILE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BREWFILE_PATH="$BREWFILE_DIR/Brewfile"

cd "$BREWFILE_DIR"

brew bundle dump --describe --file "$BREWFILE_PATH" -f
git add Brewfile Brewfile.lock.json

if git diff --cached --quiet; then
  echo "Brewfile is already up to date."
  exit 0
fi

git commit -m "Brewfile update"
git push
