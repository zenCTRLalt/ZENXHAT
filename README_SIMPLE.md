# ZENXHAT - Simplest Setup Ever

## 🎯 TL;DR

```bash
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT
bash SETUP_SIMPLE.sh
python zenxhat/cli/main.py whois google.com
```

**DONE! 4 command aja! 🎉**

---

## ❓ Mengapa Simple Setup?

### ✗ Complex Setup (yang lain):
- Setup SSH key
- Configure credentials
- Setup API tokens
- Multiple environment variables
- Complicated workflows

### ✓ Simple Setup (ZENXHAT):
- Clone repo
- Run setup script
- Done!
- No configuration needed
- Just use it!

---

## 🚀 Installation (Copy-Paste)

### Step 1: Clone
```bash
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT
```

### Step 2: Setup
```bash
bash SETUP_SIMPLE.sh
```

### Step 3: Use
```bash
python zenxhat/cli/main.py --help
```

**That's it! Zero configuration! 🎊**

---

## 📚 Quick Examples

### Domain Info
```bash
python zenxhat/cli/main.py whois example.com
```

### DNS Records
```bash
python zenxhat/cli/main.py dns example.com
```

### Find Subdomains
```bash
python zenxhat/cli/main.py subdomains example.com
```

### IP Location
```bash
python zenxhat/cli/main.py ipinfo 8.8.8.8
```

### Check Email Breach
```bash
python zenxhat/cli/main.py breach user@example.com
```

### Extract Photo Metadata
```bash
python zenxhat/cli/main.py metadata photo.jpg
```

### Search Username
```bash
python zenxhat/cli/main.py username github_username
```

---

## 💻 What Script Does

```
SETUP_SIMPLE.sh runs:
├─ Update system
├─ Install Python
├─ Upgrade pip
└─ Install Python packages

Result:
✓ Python environment ready
✓ All dependencies installed
✓ ZENXHAT ready to use
✓ No configuration needed
```

---

## 🎁 Features

### ✓ No Password
### ✓ No SSH Key
### ✓ No API Key (optional)
### ✓ Offline capable
### ✓ Super simple
### ✓ Zero config
### ✓ Works on Termux

---

## 🔄 Workflow

```
1. Clone repo (1 time)
   ↓
2. Run setup (1 time)
   ↓
3. Use ZENXHAT (many times)
   ↓
4. Done!
```

---

## 📱 Termux Users

```bash
# Same 3 commands!
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT
bash SETUP_SIMPLE.sh

# Now use it
python zenxhat/cli/main.py whois google.com
```

---

## ❓ FAQ

**Q: Butuh SSH key?**
A: Tidak! Cukup git clone.

**Q: Butuh API key?**
A: Tidak! Semua optional & tidak dibutuhkan.

**Q: Butuh password?**
A: Tidak! Tidak ada yang disimpan.

**Q: Bisa offline?**
A: Ya! Metadata extraction & local processing bisa offline.

**Q: Berapa lama setup?**
A: 1-2 menit (tergantung internet speed).

---

## 🆘 Help

### Setup error?
```bash
bash SETUP_SIMPLE.sh
```

### Module error?
```bash
pip install -r requirements-termux.txt
```

### Python error?
```bash
apt install -y python
bash SETUP_SIMPLE.sh
```

---

## ✨ Summary

🎯 **Simplest toolkit setup ever**
🚀 **Works instantly**
💡 **No configuration needed**
🔐 **Zero credentials stored**
🌍 **Works everywhere (Termux, Linux, WSL)**

---

**Just clone, setup, and use! 🎉**
