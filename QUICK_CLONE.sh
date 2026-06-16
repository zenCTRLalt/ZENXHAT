#!/bin/bash

# Script untuk clone ZENXHAT tanpa password (after SSH key setup)

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║          ZENXHAT - Clone Tanpa Password                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}Cloning ZENXHAT repository...${NC}"
echo ""

# Clone menggunakan HTTPS (akan dikonversi ke SSH otomatis)
git clone https://github.com/zenCTRLalt/ZENXHAT.git

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Clone berhasil!${NC}"
    echo ""
    echo -e "${YELLOW}Setup environment:${NC}"
    echo ""
    cd ZENXHAT
    
    echo -e "${BLUE}Creating virtual environment...${NC}"
    python -m venv venv
    source venv/bin/activate
    
    echo -e "${BLUE}Installing dependencies...${NC}"
    pip install --no-cache-dir -r requirements-termux.txt
    
    echo ""
    echo -e "${GREEN}✓ Setup complete!${NC}"
    echo ""
    echo -e "${YELLOW}Test ZENXHAT:${NC}"
    echo -e "${GREEN}python zenxhat/cli/main.py banner${NC}"
    echo -e "${GREEN}python zenxhat/cli/main.py whois google.com${NC}"
    echo ""
else
    echo -e "${RED}✗ Clone gagal!${NC}"
    echo "Pastikan SSH key sudah di-setup dengan SETUP_TERMUX.sh"
    exit 1
fi
