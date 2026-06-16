#!/bin/bash

# ZENXHAT Simple Setup - Tanpa SSH, Tanpa API Key
# Cukup: bash SETUP_SIMPLE.sh

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     ZENXHAT - Simple Setup (No SSH, No API Key)               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}[1/4]${NC} Update Termux packages..."
apt update -y > /dev/null 2>&1
apt upgrade -y > /dev/null 2>&1
echo -e "${GREEN}✓ Updated${NC}"

echo ""
echo -e "${BLUE}[2/4]${NC} Install Python & dev tools..."
apt install -y python build-essential libssl-dev > /dev/null 2>&1
echo -e "${GREEN}✓ Installed${NC}"

echo ""
echo -e "${BLUE}[3/4]${NC} Upgrade pip & setuptools..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo -e "${GREEN}✓ Upgraded${NC}"

echo ""
echo -e "${BLUE}[4/4]${NC} Install ZENXHAT dependencies..."
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
echo "║               ✨ SETUP COMPLETE! ✨                           ║"
echo "║          ZENXHAT siap digunakan OFFLINE                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${YELLOW}🚀 Gunakan ZENXHAT:${NC}"
echo ""
echo -e "${GREEN}python zenxhat/cli/main.py --help${NC}"
echo -e "${GREEN}python zenxhat/cli/main.py whois google.com${NC}"
echo -e "${GREEN}python zenxhat/cli/main.py dns github.com${NC}"
echo -e "${GREEN}python zenxhat/cli/main.py ipinfo 8.8.8.8${NC}"
echo ""
echo -e "${YELLOW}✨ Keuntungan:${NC}"
echo "  ✓ Tidak perlu password"
echo "  ✓ Tidak perlu SSH key"
echo "  ✓ Tidak perlu API key"
echo "  ✓ Bisa offline sepenuhnya"
echo "  ✓ Setup sekali, pakai selamanya"
echo ""
echo -e "${YELLOW}📝 Catatan:${NC}"
echo "  - Beberapa fitur membutuhkan internet (DNS, WHOIS, geolocation)"
echo "  - Metadata extraction & local processing bisa offline"
echo "  - API keys opsional jika ingin fitur advanced"
echo ""
