#!/bin/bash
# Recreate the workspace layout the scripts expect, as symlinks into this package.
#   bash tools/setup_workspace.sh /path/to/workspace
# Clone + patch the upstream repos into the same workspace first (see upstream/UPSTREAM.md);
# files that already exist in the workspace are left alone.
set -euo pipefail
PKG="$(cd "$(dirname "$0")/.." && pwd)"
WS="${1:?usage: setup_workspace.sh <workspace_dir>}"
mkdir -p "$WS"
tail -n +2 "$PKG/tools/workspace_layout.tsv" | while IFS=$'\t' read -r pkg ws; do
    dst="$WS/$ws"
    [ -e "$dst" ] && continue
    mkdir -p "$(dirname "$dst")"
    ln -s "$PKG/$pkg" "$dst"
done
echo "linked into $WS; now: export WORKSPACE=$WS and run scripts from there"
