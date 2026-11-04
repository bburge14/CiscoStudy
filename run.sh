#!/usr/bin/env bash
# Launch the CiscoStudy platform locally.
set -euo pipefail
cd "$(dirname "$0")"

# (Re)generate the question JSON from the authored source if the tool is present.
if [ -f tools/build_content.py ]; then
  python3 tools/build_content.py >/dev/null
fi

# Install runtime deps on first run (harmless if already satisfied).
python3 -m pip install -q -r requirements.txt || true

exec python3 -m streamlit run app.py "$@"
