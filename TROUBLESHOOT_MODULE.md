# ZENXHAT Quick Fix - Jika Module Error

## 🔧 Problem

```
ModuleNotFoundError: No module named 'zenxhat'
```

Biasanya terjadi karena:
- Folder nested terlalu dalam (ZENXHAT/ZENXHAT/ZENXHAT/...)
- Tidak di-run dari directory yang benar
- Virtual environment tidak aktif

---

## ✅ Solusi (3 Pilihan)

### **Option 1: Auto Fix (RECOMMENDED)**

```bash
# Jalankan script ini (otomatis benerin semua)
bash FIX_AND_SETUP.sh

# Test
source venv/bin/activate
python zenxhat/cli/main.py --help
```

---

### **Option 2: Manual Fix

**Step 1: Periksa directory**
```bash
pwd
# Output harus: .../ZENXHAT (not .../ZENXHAT/ZENXHAT/...)

# Jika nested, cd ke parent:
cd ..
```

**Step 2: List folder**
```bash
ls -la
# Harus ada: zenxhat/, README.md, requirements-termux.txt, etc
```

**Step 3: Setup venv**
```bash
python -m venv venv
source venv/bin/activate
```

**Step 4: Install deps**
```bash
pip install --no-cache-dir -r requirements-termux.txt
```

**Step 5: Test**
```bash
python zenxhat/cli/main.py --help
```

---

### **Option 3: Direct Run (No venv)**

```bash
# Setup deps global
pip install requests beautifulsoup4 click colorama python-dotenv

# Run direct
python zenxhat/cli/main.py whois google.com
```

---

## 🆘 Debug Checklist

- [ ] Current directory is correct: `pwd` shows `.../ZENXHAT` (single ZENXHAT)
- [ ] zenxhat folder exists: `ls zenxhat/`
- [ ] __init__.py files exist:
  ```bash
  ls zenxhat/__init__.py
  ls zenxhat/core/__init__.py
  ls zenxhat/modules/__init__.py
  ls zenxhat/cli/__init__.py
  ```
- [ ] Python can import: `python -c "import zenxhat; print('OK')"`
- [ ] Virtual env activated: `which python` shows `.../venv/bin/python`

---

## 📝 Correct Directory Structure

```
ZENXHAT/                           <-- You should be here
├── zenxhat/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── utils.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── whois_lookup.py
│   │   ├── dns_resolver.py
│   │   └── ...
│   └── cli/
│       ├── __init__.py
│       └── main.py
├── venv/                          <-- Virtual env here
├── README.md
├── requirements-termux.txt
└── FIX_AND_SETUP.sh
```

---

## 🎯 Step-by-Step Fix

```bash
# 1. Remove old venv if corrupted
rm -rf venv

# 2. Create new venv
python -m venv venv

# 3. Activate
source venv/bin/activate

# 4. Install deps
pip install --upgrade pip
pip install -r requirements-termux.txt

# 5. Test import
python -c "from zenxhat.cli.main import cli; print('SUCCESS')"

# 6. Run
python zenxhat/cli/main.py --help
```

---

## ✨ Common Fixes

### "No module named zenxhat"
```bash
# Make sure you're in right directory
cd $(pwd)  # Current ZENXHAT folder
ls zenxhat/  # Should exist
```

### "venv not activated"
```bash
source venv/bin/activate
# Prompt should change to: (venv) user@host:...$
```

### "pip: command not found"
```bash
apt install -y python
python -m pip install --upgrade pip
```

### "Permission denied"
```bash
chmod +x FIX_AND_SETUP.sh
bash FIX_AND_SETUP.sh
```

---

## 🚀 After Fix

```bash
# Always activate venv first
source venv/bin/activate

# Then run
python zenxhat/cli/main.py whois google.com
python zenxhat/cli/main.py dns github.com
python zenxhat/cli/main.py ipinfo 8.8.8.8
```

---

**Run `bash FIX_AND_SETUP.sh` dan semua akan otomatis teratasi! 🔧**
