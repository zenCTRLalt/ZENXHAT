# ZENXHAT untuk Termux (Android) - Setup Otomatis TANPA Password

## 🚀 Setup Cepat (1 Command)

Semua setup dilakukan otomatis **TANPA password & username**!

### Step 1: Download & Setup (Copy-Paste)

```bash
# Clone repo dulu (boleh pakai HTTPS, akan otomatis jadi SSH)
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT

# Jalankan script setup (1 command)
bash SETUP_TERMUX.sh
```

### Step 2: Setup SSH Key di GitHub (2 menit)

Script akan menampilkan SSH public key Anda:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB...
```

**Lakukan ini:**

1. **Copy** SSH key dari terminal (mulai dari `ssh-ed25519` sampai email)
2. **Buka** https://github.com/settings/ssh/new di browser
3. **Login** ke GitHub (jika belum)
4. **Paste** SSH key ke box "Key"
5. **Title**: `Termux-ZENXHAT`
6. **Click** "Add SSH key"

### Step 3: Selesai! Gunakan ZENXHAT

```bash
# Clone repo tanpa password
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT

# Gunakan ZENXHAT
python zenxhat/cli/main.py --help
python zenxhat/cli/main.py whois google.com
python zenxhat/cli/main.py dns github.com
```

---

## 📋 Apa yang Script Setup Lakukan

```
[1/7] ✓ Update Termux packages
[2/7] ✓ Install build tools
[3/7] ✓ Setup Git config (username & email)
[4/7] ✓ Generate SSH key ED25519 (no passphrase)
[5/7] ✓ Configure Git to use SSH automatically
[6/7] ✓ Upgrade pip
[7/7] ✓ Install ZENXHAT dependencies
```

**Hasil:**
- ✅ Git configured dengan SSH key
- ✅ HTTPS URLs otomatis jadi SSH
- ✅ Clone/Push/Pull TANPA password
- ✅ Python environment ready
- ✅ Dependencies installed

---

## 🔐 Keamanan

| Aspek | Status |
|-------|--------|
| Password disimpan? | ❌ TIDAK |
| Token disimpan? | ❌ TIDAK |
| SSH key disimpan aman? | ✅ YA (di ~/.ssh/) |
| Expire? | ❌ TIDAK |
| Perlu setup ulang? | ❌ TIDAK (permanen) |

---

## 📝 Manual Commands (Jika Script Error)

Jika script gagal, jalankan manual:

```bash
# 1. Update
apt update && apt upgrade -y

# 2. Install tools
apt install -y git build-essential python-dev

# 3. Setup Git
git config --global user.name "zenCTRLalt"
git config --global user.email "zzid3291@gmail.com"

# 4. Generate SSH key (Enter 3x)
ssh-keygen -t ed25519 -C "zzid3291@gmail.com"

# 5. View SSH key
cat ~/.ssh/id_ed25519.pub

# 6. Add ke GitHub: https://github.com/settings/ssh/new

# 7. Configure Git untuk SSH auto
git config --global url."git@github.com:".insteadOf "https://github.com/"

# 8. Install pip deps
pip install --no-cache-dir -r requirements-termux.txt
```

---

## 🆘 Troubleshooting

### "SSH key not found"
```bash
# Cek SSH key ada?
ls -la ~/.ssh/

# Generate jika tidak ada
ssh-keygen -t ed25519 -C "zzid3291@gmail.com" -N ""
```

### "Permission denied (publickey)"
```bash
# SSH key belum ditambah ke GitHub
# Pastikan sudah:
# 1. Copy ~/.ssh/id_ed25519.pub
# 2. Paste ke https://github.com/settings/ssh/new
# 3. Klik "Add SSH key"
```

### "fatal: could not read Username"
```bash
# Git belum dikonfigurasi
git config --global user.name "zenCTRLalt"
git config --global user.email "zzid3291@gmail.com"
```

### Dependencies install stuck
```bash
# Gunakan requirements-termux.txt (minimal)
pip install -r requirements-termux.txt

# Install satu-satu jika error
pip install requests
pip install beautifulsoup4
pip install click
```

---

## 📚 Usage Examples

```bash
# WHOIS lookup
python zenxhat/cli/main.py whois google.com

# DNS resolution
python zenxhat/cli/main.py dns github.com

# Find subdomains
python zenxhat/cli/main.py subdomains facebook.com

# IP geolocation
python zenxhat/cli/main.py ipinfo 8.8.8.8

# Check email breach
python zenxhat/cli/main.py breach user@example.com

# Search username
python zenxhat/cli/main.py username github_username
```

---

## 🎯 Workflow Termux + ZENXHAT

```bash
# 1. Clone repo (setup sekali saja)
bash SETUP_TERMUX.sh        # Setup SSH + dependencies

# 2. Setup SSH key di GitHub (2 menit)
#    - Copy public key
#    - Paste ke https://github.com/settings/ssh/new

# 3. Clone & use
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT
python zenxhat/cli/main.py --help

# 4. Push changes (tanpa password!)
git add .
git commit -m "Update: deskripsi"
git push origin main    # <-- TANPA PASSWORD!
```

---

## ✨ Kelebihan Sistem Ini

✅ **Sekali setup, selamanya bisa pakai**
✅ **TANPA password atau token**
✅ **TANPA username saat clone/push**
✅ **SSH key aman & terenkripsi**
✅ **Tidak pernah expire**
✅ **Termux-native & fast**
✅ **Bisa di-backup & restore**

---

## 📞 Support

Jika ada masalah:

1. Cek SSH key setup: `ls -la ~/.ssh/`
2. Test git: `git config --list`
3. Test SSH: `ssh -T git@github.com`
4. Lihat log: `git clone -v https://github.com/...`

---

**Happy coding! 🚀**

Setup sekali, gunakan selamanya tanpa password! 🔐
