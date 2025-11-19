#!/usr/bin/env bash
set -e

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT_DIR"

if ! command -v allure >/dev/null 2>&1; then
  echo "Allure CLI not found in PATH. Install it or run in CI where it's available."
  exit 0
fi

if [ ! -d "results/allure-results" ]; then
  echo "No Allure results found at results/allure-results. Ensure tests ran with ALLURE=true."
  exit 0
fi

mkdir -p results/allure-report
allure generate results/allure-results -o results/allure-report --clean
echo "Allure report generated at results/allure-report"
