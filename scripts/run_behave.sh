#!/usr/bin/env zsh
# Runner for behave tests. Uses isolated HOME to avoid user configs interfering.
set -e

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT_DIR"

mkdir -p results/junit
mkdir -p results/screenshots

# Build behave command: always include pretty output and create JSON + JUnit
BEHAVE_CMD=(behave -f pretty --junit --junit-directory results/junit -f json -o results/cucumber.json)

# Optional Allure: when ALLURE=true, attempt to add allure-behave formatter output
if [ "${ALLURE}" = "true" ]; then
  # ensure allure-behave installed in active env
  python - <<'PY'
import importlib,sys
try:
    importlib.import_module('allure_behave')
except Exception:
    sys.exit(2)
sys.exit(0)
PY
  if [ $? -ne 0 ]; then
    echo "allure-behave package not found; attempting to pip install it"
    pip install allure-behave || echo "pip install allure-behave failed; continuing without Allure formatter"
  fi
  # Add Allure formatter output directory
  BEHAVE_CMD+=( -f allure_behave.formatter:AllureFormatter -o results/allure-results )
fi

# Run behave in an isolated HOME to avoid user-level config interference
TMP_HOME=$(mktemp -d)
HOME="$TMP_HOME" "${BEHAVE_CMD[@]}" "$@"
EXIT_CODE=$?

echo "Behave finished with exit code: $EXIT_CODE"

if [ $EXIT_CODE -ne 0 ]; then
  echo "Tests failed (exit code $EXIT_CODE)"
  exit $EXIT_CODE
fi

echo "Runner completed successfully. Artifacts in results/"
exit 0
