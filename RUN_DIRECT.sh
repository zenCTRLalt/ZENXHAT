#!/bin/bash

# ZENXHAT - Direct Run Script (Bypass virtual env)
# Jalankan: bash RUN_DIRECT.sh <command>

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║              ZENXHAT - Direct Run (No venv)                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Install dependencies directly if needed
echo "Installing dependencies..."
pip install --no-cache-dir \
  requests \
  beautifulsoup4 \
  click \
  colorama \
  python-dotenv \
  tabulate > /dev/null 2>&1

echo ""
echo "Running ZENXHAT..."
echo ""

# Run ZENXHAT
python zenxhat/cli/main.py "$@"
