#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$ROOT/scripts/build_workbooks.py" --check
python3 "$ROOT/scripts/sync_skills.py" --check
exec python3 "$ROOT/scripts/venture.py" init "$@"
