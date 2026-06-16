# ZENXHAT - OSINT Reconnaissance Toolkit

![ZENXHAT Logo](./assets/zenx-logo.png)

> **ZENXHAT** adalah toolkit OSINT (Open Source Intelligence) yang komprehensif untuk pengumpulan informasi dari sumber publik. Dirancang untuk penetration tester, security researchers, threat intelligence analyst, dan ethical hackers.

## ⚠️ DISCLAIMER & LEGAL

Toolkit ini **HANYA** untuk penggunaan yang sah dan etis:
- ✅ Penelitian keamanan (dengan izin pemilik sistem)
- ✅ Audit keamanan yang diotorisasi
- ✅ Threat intelligence gathering
- ✅ Pembelajaran cybersecurity
- ✅ Investigasi internal organisasi

❌ **DILARANG** untuk:
- Akses tidak sah ke sistem
- Spy atau surveillance tanpa izin
- Pengumpulan data pribadi untuk tujuan berbahaya
- Harassment atau stalking

**Pengguna bertanggung jawab penuh atas tindakan mereka. Pembuat tidak bertanggung jawab atas penyalahgunaan.**

---

## 🎯 Fitur Utama

### 1. **WHOIS & Domain Reconnaissance**
- Domain WHOIS lookup
- Registrar info extraction
- History tracking

### 2. **DNS Intelligence**
- DNS A, AAAA, MX, NS, TXT records
- Reverse DNS lookup
- Zone transfer detection
- DNS propagation checker

### 3. **Passive Subdomain Discovery**
- Certificate Transparency (crt.sh scraping)
- Public DNS records
- No active scanning — full passive mode

### 4. **IP & Geolocation**
- IP address information
- Geographic location data
- ASN lookup
- Reverse IP search

### 5. **Metadata Extraction**
- Image EXIF data
- PDF metadata
- Document properties
- Hidden metadata recovery

### 6. **Email & Username Reconnaissance**
- Email breach checking
- Social media profile finder
- Username OSINT aggregator

### 7. **Search Engine Aggregation**
- Google dorking results
- Advanced search operators
- Public API integration (Shodan, Censys, VirusTotal — optional)

### 8. **Port & Service Enumeration**
- Non-invasive service identification
- Public service databases
- CVE correlation

---

## 📦 Installation

### Requirements
- Python 3.8+
- pip (Python package manager)

### Quick Start

```bash
# Clone repository
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys (optional)
cp .env.example .env
# Edit .env with your API keys

# Run toolkit
python zenxhat.py --help
```

---

## 🚀 Usage Examples

### Domain Reconnaissance
```bash
python zenxhat.py whois example.com
python zenxhat.py dns example.com
python zenxhat.py subdomains example.com
```

### IP Intelligence
```bash
python zenxhat.py ip-info 8.8.8.8
python zenxhat.py reverse-ip 8.8.8.8
```

### Metadata Extraction
```bash
python zenxhat.py metadata extract image.jpg
python zenxhat.py metadata extract document.pdf
```

### Email Breach Checking
```bash
python zenxhat.py breach-check user@example.com
```

### Username Finder
```bash
python zenxhat.py username-search username
```

### Search Aggregation
```bash
python zenxhat.py search "target.com" --sources google,bing,crt
```

---

## 🔧 Configuration

Edit `.env` untuk menambahkan API keys (semua optional):

```env
# Optional API Keys
SHODAN_API_KEY=your_key_here
CENSYS_API_ID=your_id_here
CENSYS_API_SECRET=your_secret_here
VIRUSTOTAL_API_KEY=your_key_here
HUNTER_API_KEY=your_key_here
ABUSEIPDB_API_KEY=your_key_here
```

---

## 📂 Project Structure

```
ZENXHAT/
├── assets/
│   ├── zenx-logo.png
│   └── zenx-logo.svg
├── zenxhat/
│   ├── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── utils.py
│   ├── modules/
│   │   ├── whois_lookup.py
│   │   ├── dns_resolver.py
│   │   ├── subdomain_finder.py
│   │   ├── ip_geolocation.py
│   │   ├── metadata_extractor.py
│   │   ├── email_osint.py
│   │   ├── username_finder.py
│   │   └── search_aggregator.py
│   └── cli/
│       └── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Tools & Dependencies

| Tool | Purpose | License |
|------|---------|----------|
| python-whois | WHOIS lookup | MIT |
| dnspython | DNS resolution | ISC |
| requests | HTTP requests | Apache 2.0 |
| beautifulsoup4 | Web scraping (passive) | MIT |
| pillow | Image processing | HPND |
| click | CLI framework | BSD |
| python-dotenv | .env configuration | BSD |
| colorama | Colored terminal output | BSD |

---

## 📚 Documentation

- [Module Guide](./docs/modules.md) — Detailed module documentation
- [API Configuration](./docs/api-setup.md) — Setting up optional APIs
- [Examples](./docs/examples.md) — Real-world usage scenarios
- [Ethical Guidelines](./docs/ETHICS.md) — Terms & responsible disclosure

---

## 🔐 Responsible Disclosure

Jika Anda menemukan vulnerability pada toolkit ini:
1. **Jangan** publish secara publik
2. Email: zenCTRLalt@protonmail.com dengan detail vulnerability
3. Berikan 30 hari untuk patch sebelum disclosure

---

## 🤝 Contributing

Kontribusi terbuka! Lihat [CONTRIBUTING.md](./CONTRIBUTING.md) untuk pedoman.

```bash
# Fork & clone
git clone https://github.com/YOUR_USERNAME/ZENXHAT.git
git checkout -b feature/new-module
# ... make changes ...
git push origin feature/new-module
# Create Pull Request
```

---

## 📋 Roadmap

- [x] WHOIS lookup
- [x] DNS intelligence
- [x] Passive subdomain discovery
- [x] IP geolocation
- [x] Metadata extraction
- [ ] Advanced email osint
- [ ] Social media reconnaissance
- [ ] Shodan integration
- [ ] Censys integration
- [ ] Web UI dashboard
- [ ] Export reports (PDF, HTML, JSON)
- [ ] Database storage (SQLite)

---

## 📜 License

MIT License — Lihat [LICENSE](./LICENSE) untuk detail.

---

## ⭐ Support & Credits

Bila toolkit ini berguna, silakan beri ⭐ di GitHub!

**Dibuat oleh:** zenCTRLalt  
**Community-driven & ethical-first**

---

## 🌐 Social & Contact

- GitHub: [@zenCTRLalt](https://github.com/zenCTRLalt)
- Email: zenCTRLalt@protonmail.com

---

**"Information is power. Use it responsibly."** 🔍🛡️
