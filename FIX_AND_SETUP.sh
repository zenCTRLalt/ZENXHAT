#!/bin/bash

# ZENXHAT - Fix & Setup Script
# Jalankan: bash FIX_AND_SETUP.sh

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║           ZENXHAT - Fix Nested Folder Problem                ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check current directory
echo -e "${BLUE}Current directory:${NC} $(pwd)"
echo ""

# Check if we're in nested ZENXHAT folder
if [[ $(pwd) == */ZENXHAT/ZENXHAT* ]]; then
    echo -e "${YELLOW}[!] Detected nested folder structure!${NC}"
    echo "    Moving to correct directory..."
    
    # Go up to parent ZENXHAT
    while [[ $(pwd) == */ZENXHAT/ZENXHAT* ]]; do
        cd ..
    done
    
    echo -e "${GREEN}✓ Moved to:${NC} $(pwd)"
fi

echo ""
echo -e "${BLUE}[1/5]${NC} Update system packages..."
apt update -y > /dev/null 2>&1
apt upgrade -y > /dev/null 2>&1
echo -e "${GREEN}✓ System updated${NC}"

echo ""
echo -e "${BLUE}[2/5]${NC} Install Python & tools..."
apt install -y python python-dev build-essential git > /dev/null 2>&1
echo -e "${GREEN}✓ Python installed${NC}"

echo ""
echo -e "${BLUE}[3/5]${NC} Create virtual environment..."
if [ -d "venv" ]; then
    echo -e "${YELLOW}Virtual env already exists, skipping...${NC}"
else
    python -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

echo ""
echo -e "${BLUE}[4/5]${NC} Activate virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

echo ""
echo -e "${BLUE}[5/5]${NC} Install ZENXHAT dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install --no-cache-dir \
  requests \
  beautifulsoup4 \
  click \
  colorama \
  python-dotenv \
  tabulate > /dev/null 2>&1
echo -e "${GREEN}✓ Dependencies installed${NC}"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                 ✨ SETUP COMPLETE! ✨                         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${YELLOW}📍 Working directory:${NC} $(pwd)"
echo ""
echo -e "${YELLOW}🚀 Next steps:${NC}"
echo ""
echo "1. Make sure you're in the ZENXHAT root directory"
echo ""
echo -e "${GREEN}pwd${NC}  # Should show: .../ZENXHAT (not .../ZENXHAT/ZENXHAT/...)"
echo ""
echo "2. Activate virtual environment (if not already active)"
echo ""
echo -e "${GREEN}source venv/bin/activate${NC}"
echo ""
echo "3. Test ZENXHAT"
echo ""
echo -e "${GREEN}python zenxhat/cli/main.py --help${NC}"
echo -e "${GREEN}python zenxhat/cli/main.py whois google.com${NC}"
echo ""
echo -e "${YELLOW}💡 If still getting module errors:${NC}"
echo ""
echo "1. Check directory structure:"
echo -e "   ${GREEN}ls -la zenxhat/${NC}"
echo ""
echo "2. Check __init__.py files exist:"
echo -e "   ${GREEN}ls -la zenxhat/__init__.py${NC}"
echo -e "   ${GREEN}ls -la zenxhat/core/__init__.py${NC}"
echo -e "   ${GREEN}ls -la zenxhat/modules/__init__.py${NC}"
echo -e "   ${GREEN}ls -la zenxhat/cli/__init__.py${NC}"
echo ""
echo -e "${YELLOW}📝 Manual test (if python command fails):${NC}"
echo ""
echo -e "${GREEN}python -c 'import sys; print(sys.path)'${NC}"
echo -e "${GREEN}python -c 'from zenxhat.core.logger import setup_logger; print(\"OK\")'${NC}"
echo ""
