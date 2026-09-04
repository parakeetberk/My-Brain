#!/usr/bin/env bash
# Build the ops dashboard from whatever is currently in pipeline/raw/.
# Refreshing pipeline/raw/ itself needs the warehouse connector — see
# docs/ARCHITECTURE.md and pipeline/queries.json.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 pipeline/build.py
python3 pipeline/publish.py
echo
echo "Next: publish build/parakeet_ops_dashboard.html to the artifact URL."
