# ZENXHAT Quick Start Guide

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Internet connection

### Step 1: Clone Repository
```bash
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT
```

### Step 2: Create Virtual Environment
```bash
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

# On Termux (Android)
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Configuration (Optional)
```bash
cp .env.example .env
# Edit .env dengan API keys Anda (optional)
nano .env  # atau gunakan editor favorit
```

### Step 5: Test Installation
```bash
python -m zenxhat.cli.main --help
# atau
python zenxhat/cli/main.py --help
```

---

## 🚀 Quick Examples

### 1. WHOIS Lookup
```bash
python zenxhat/cli/main.py whois example.com
```

**Output:**
```json
{
  "domain": "example.com",
  "registrar": "VeriSign Global Registry Services",
  "creation_date": "1995-08-14",
  "expiration_date": "2025-08-13",
  "nameservers": ["a.iana-servers.net", "b.iana-servers.net"],
  "emails": ["..."]
}
```

### 2. DNS Lookup
```bash
python zenxhat/cli/main.py dns google.com
```

**Output:**
```json
{
  "domain": "google.com",
  "A_records": ["142.251.32.46"],
  "AAAA_records": ["2607:f8b0:4004:80a::200e"],
  "MX_records": [{"priority": 10, "mail_server": "smtp.google.com"}],
  "NS_records": ["ns1.google.com", "ns2.google.com", ...]
}
```

### 3. Subdomain Discovery (Passive)
```bash
python zenxhat/cli/main.py subdomains example.com
```

**Output:**
```json
{
  "domain": "example.com",
  "subdomains": [
    "mail.example.com",
    "www.example.com",
    "api.example.com",
    ...
  ],
  "count": 42
}
```

### 4. IP Geolocation
```bash
python zenxhat/cli/main.py ipinfo 8.8.8.8
```

**Output:**
```json
{
  "ip": "8.8.8.8",
  "country": "United States",
  "city": "Mountain View",
  "isp": "Google LLC",
  "timezone": "America/Los_Angeles"
}
```

### 5. Metadata Extraction
```bash
python zenxhat/cli/main.py metadata photo.jpg
```

**Output:**
```json
{
  "file_path": "photo.jpg",
  "exif_data": {
    "DateTime": "2024-01-15 14:30:45",
    "GPS": "37.4224° N, 122.0842° W",
    "Camera": "Canon EOS R5",
    "FocalLength": "50.0 mm"
  }
}
```

### 6. Email Breach Check
```bash
python zenxhat/cli/main.py breach user@example.com
```

**Output:**
```json
{
  "email": "user@example.com",
  "breached": false,
  "breach_count": 0
}
```

### 7. Username Search
```bash
python zenxhat/cli/main.py username john_doe
```

**Output:**
```json
{
  "username": "john_doe",
  "found_on": [
    {"platform": "GitHub", "url": "https://github.com/john_doe", "status": "found"},
    {"platform": "Twitter", "url": "https://twitter.com/john_doe", "status": "found"},
    {"platform": "Instagram", "url": "https://instagram.com/john_doe", "status": "found"}
  ]
}
```

---

## 📝 API Keys (Optional)

Untuk fitur advanced, dapatkan API keys gratis dari:

| Service | API Key | Purpose |
|---------|---------|----------|
| Shodan | https://www.shodan.io/ | Vulnerability scanning |
| Censys | https://censys.io/ | Certificate & IP data |
| VirusTotal | https://www.virustotal.com/ | Malware analysis |
| Hunter.io | https://hunter.io/ | Email finding |
| AbuseIPDB | https://www.abuseipdb.com/ | Malicious IPs |

### Setup API Keys
```bash
# Edit .env
nano .env

# Add your keys
SHODAN_API_KEY=your_key_here
CENSYS_API_ID=your_id
CENSYS_API_SECRET=your_secret
```

---

## 🔍 Advanced Usage

### Save Output to File
```bash
# Manually save
python zenxhat/cli/main.py whois example.com > results.json

# Or use Python
python -c "
from zenxhat.modules import WhoisLookup
from zenxhat.core.utils import save_output

whois = WhoisLookup()
result = whois.lookup('example.com')
save_output(result, 'whois_example')
"
```

### Chain Multiple Tools
```bash
# Bash script untuk automated reconnaissance
#!/bin/bash

TARGET=$1

echo "[*] Starting reconnaissance on $TARGET"
echo "[+] WHOIS lookup..."
python zenxhat/cli/main.py whois $TARGET

echo "[+] DNS lookup..."
python zenxhat/cli/main.py dns $TARGET

echo "[+] Subdomain enumeration..."
python zenxhat/cli/main.py subdomains $TARGET

echo "[+] Reconnaissance complete!"
```

---

## ⚙️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'zenxhat'"
**Solution:**
```bash
# Make sure you're in correct directory
cd ZENXHAT

# And activated venv
source venv/bin/activate

# Then test
python -c "import zenxhat; print('OK')"
```

### Issue: "Connection refused" or timeout
**Solution:**
```bash
# Check internet connection
ping 8.8.8.8

# Check firewall
# Some networks block external connections
# Try using VPN or different network
```

### Issue: "SSL Certificate error"
**Solution:**
```bash
# For testing only (NOT recommended for production)
# Edit .env and set
VERIFY_SSL=false

# Or in code
import urllib3
urllib3.disable_warnings()
```

---

## 📚 Next Steps

1. **Read Full Documentation**: [docs/modules.md](./modules.md)
2. **Check Examples**: [docs/examples.md](./examples.md)
3. **Learn Ethics**: [ETHICS.md](./ETHICS.md)
4. **Contribute**: See [CONTRIBUTING.md](../CONTRIBUTING.md)
5. **Report Issues**: [GitHub Issues](https://github.com/zenCTRLalt/ZENXHAT/issues)

---

## 🆘 Help & Support

- 📖 **GitHub Wiki**: https://github.com/zenCTRLalt/ZENXHAT/wiki
- 🐛 **Report Bug**: https://github.com/zenCTRLalt/ZENXHAT/issues
- 💬 **Discussions**: https://github.com/zenCTRLalt/ZENXHAT/discussions
- 📧 **Email**: zenCTRLalt@protonmail.com

---

**Happy Hunting! 🔍**
