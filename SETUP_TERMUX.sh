#!/bin/bash

# ZENXHAT Auto Setup Script untuk Termux
# Menjalankan: bash SETUP_TERMUX.sh

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     ZENXHAT - Automatic Setup untuk Termux (No Password)      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}[1/7]${NC} Update Termux packages..."
apt update -y > /dev/null 2>&1
apt upgrade -y > /dev/null 2>&1
echo -e "${GREEN}✓ Termux packages updated${NC}"

echo ""
echo -e "${BLUE}[2/7]${NC} Install development tools..."
apt install -y build-essential python-dev libssl-dev libffi-dev > /dev/null 2>&1
echo -e "${GREEN}✓ Development tools installed${NC}"

echo ""
echo -e "${BLUE}[3/7]${NC} Setup Git configuration..."
git config --global user.name "zenCTRLalt"
git config --global user.email "zzid3291@gmail.com"
git config --global credential.helper store
echo -e "${GREEN}✓ Git configured${NC}"

echo ""
echo -e "${BLUE}[4/7]${NC} Setup SSH key (no passphrase)..."
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -C "zzid3291@gmail.com" -N "" -f ~/.ssh/id_ed25519 > /dev/null 2>&1
    echo -e "${GREEN}✓ SSH key generated${NC}"
else
    echo -e "${GREEN}✓ SSH key already exists${NC}"
fi

echo ""
echo -e "${BLUE}[5/7]${NC} Configure Git to use SSH automatically..."
git config --global url."git@github.com:".insteadOf "https://github.com/"
echo -e "${GREEN}✓ Git SSH configured (HTTPS URLs will use SSH)${NC}"

echo ""
echo -e "${BLUE}[6/7]${NC} Upgrade pip & setuptools..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo -e "${GREEN}✓ Pip upgraded${NC}"

echo ""
echo -e "${BLUE}[7/7]${NC} Install ZENXHAT dependencies..."
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
echo "║          Git & SSH siap digunakan TANPA PASSWORD!             ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${YELLOW}📋 YOUR SSH PUBLIC KEY (copy ini):${NC}"
echo ""
cat ~/.ssh/id_ed25519.pub
echo ""
echo ""
echo -e "${YELLOW}🔐 NEXT STEPS (3 langkah):${NC}"
echo ""
echo "STEP 1: Copy SSH public key di atas (mulai dari 'ssh-ed25519' sampai email)"
echo ""
echo "STEP 2: Buka browser & login:"
echo -e "        ${GREEN}https://github.com/settings/ssh/new${NC}"
echo ""
echo "STEP 3: Paste SSH key & klik 'Add SSH key'"
echo ""
echo ""
echo -e "${YELLOW}🚀 SETELAH ITU, CLONE REPO TANPA PASSWORD:${NC}"
echo ""
echo -e "${GREEN}git clone https://github.com/zenCTRLalt/ZENXHAT.git${NC}"
echo -e "${GREEN}cd ZENXHAT${NC}"
echo -e "${GREEN}python zenxhat/cli/main.py --help${NC}"
echo ""
echo -e "${YELLOW}💡 KELEBIHAN:${NC}"
echo "  ✓ Git push/pull TANPA password"
echo "  ✓ Clone TANPA username/password"
echo "  ✓ SSH key aman & tidak expire"
echo "  ✓ Bisa setup sekali, gunakan forever"
echo ""
