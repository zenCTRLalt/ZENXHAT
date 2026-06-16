# ZENXHAT - Setup Paling Sederhana (Tanpa SSH, Tanpa API Key)

## 🚀 Setup 1 Menit

```bash
# 1. Clone repo
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT

# 2. Setup (hanya sekali)
bash SETUP_SIMPLE.sh

# 3. Done! Gunakan sekarang
python zenxhat/cli/main.py --help
```

**SELESAI! Tidak ada yang perlu dikonfigurasi lagi! 🎉**

---

## 📝 Keuntungan Setup Ini

✅ **TANPA Password** - Tidak ada yang disimpan
✅ **TANPA SSH Key** - Tidak perlu setup SSH
✅ **TANPA API Key** - Bisa pakai tanpa token
✅ **OFFLINE Mode** - Bisa digunakan offline
✅ **Super Simpel** - 3 command aja
✅ **Permanen** - Sekali setup, forever use

---

## 💡 Cara Kerja

### Download Sekali
```bash
git clone https://github.com/zenCTRLalt/ZENXHAT.git
```

### Setup Environment
```bash
bash SETUP_SIMPLE.sh
```

### Gunakan (Offline)
```bash
python zenxhat/cli/main.py whois domain.com
python zenxhat/cli/main.py metadata file.jpg
```

---

## 🎯 Contoh Penggunaan

### WHOIS Lookup (perlu internet)
```bash
python zenxhat/cli/main.py whois google.com
```

### DNS Resolution (perlu internet)
```bash
python zenxhat/cli/main.py dns github.com
```

### IP Geolocation (perlu internet)
```bash
python zenxhat/cli/main.py ipinfo 8.8.8.8
```

### Metadata Extraction (OFFLINE)
```bash
python zenxhat/cli/main.py metadata photo.jpg
python zenxhat/cli/main.py metadata document.pdf
```

### Username Search (perlu internet)
```bash
python zenxhat/cli/main.py username username_disini
```

---

## 🔍 Fitur Yang Tersedia

### ✓ Bisa Offline:
- Metadata extraction dari file lokal
- File analysis
- Utility functions

### ✓ Perlu Internet:
- WHOIS lookup
- DNS resolution
- IP geolocation
- Email breach check
- Username search
- Subdomain enumeration

---

## 📁 Struktur File

```
ZENXHAT/
├── zenxhat/
│   ├── core/          # Config, logger, utils
│   ├── modules/       # 8 OSINT tools
│   └── cli/           # Command line interface
├── assets/            # Logos & banners
├── docs/              # Documentation
├── requirements-termux.txt
├── SETUP_SIMPLE.sh    # Setup script ini
└── README.md
```

---

## 🆘 Troubleshooting

### Error: "pip: command not found"
```bash
# Install Python terlebih dahulu
apt install -y python
bash SETUP_SIMPLE.sh
```

### Error: "Module not found"
```bash
# Install ulang dependencies
pip install -r requirements-termux.txt
```

### Error: "Internet connection failed"
```bash
# Cek koneksi internet
ping 8.8.8.8

# Atau gunakan offline features (metadata extraction)
python zenxhat/cli/main.py metadata file.jpg
```

---

## 🎁 Bonus: Hybrid Setup (Jika Mau Pakai API Key)

Kalau nanti ingin pakai advanced features:

```bash
# 1. Copy .env.example ke .env
cp .env.example .env

# 2. Edit .env & add API keys (optional)
nano .env

# 3. Sekarang bisa pakai Shodan, Censys, VirusTotal, etc.
```

Tapi ini **totally optional** - toolkit bisa jalan tanpa API key!

---

## 📞 Support

Jika ada error:

1. Update Termux: `apt update && apt upgrade -y`
2. Reinstall: `bash SETUP_SIMPLE.sh`
3. Check Python: `python --version`
4. Check pip: `pip --version`

---

## ✨ Workflow Harian

```bash
# Day 1: Setup
cd ZENXHAT
bash SETUP_SIMPLE.sh

# Day 2+: Gunakan (no setup needed!)
python zenxhat/cli/main.py whois target.com
python zenxhat/cli/main.py dns target.com
python zenxhat/cli/main.py metadata screenshot.png
```

---

## 🔐 Keamanan Note

- ✅ Tidak ada credentials disimpan
- ✅ Tidak ada password stored
- ✅ Tidak ada token disimpan
- ✅ Semua local & offline-capable
- ✅ Open source & auditable

---

**Setup sekali, gunakan selamanya tanpa ribet! 🚀**
