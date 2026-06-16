# ZENXHAT Setup Guide untuk Termux

## ⚡ TL;DR - Setup Instan

```bash
# 1. Clone
git clone https://github.com/zenCTRLalt/ZENXHAT.git
cd ZENXHAT

# 2. Run setup (otomatis semuanya)
bash SETUP_TERMUX.sh

# 3. Buka GitHub & add SSH key
# Copy key dari output, paste ke: https://github.com/settings/ssh/new

# 4. Done! Clone tanpa password:
git clone https://github.com/zenCTRLalt/ZENXHAT.git
```

---

## 🔍 Detail Penjelasan

### Apa yang Dilakukan Script?

**SETUP_TERMUX.sh** melakukan:

1. **Update Termux** - Dapatkan packages terbaru
2. **Install Build Tools** - C compiler, Python dev headers
3. **Configure Git** - Username & email
4. **Generate SSH Key** - ED25519 (modern & aman)
5. **Configure Git SSH** - HTTPS URLs jadi SSH otomatis
6. **Upgrade Pip** - Package manager Python
7. **Install Dependencies** - ZENXHAT requirements

### Hasil Akhir

```
Git configured dengan SSH key ED25519
       ↓
HTTPS URLs otomatis jadi SSH
       ↓
Clone/Push/Pull TANPA password
       ↓
Python environment ready
       ↓
ZENXHAT siap digunakan!
```

---

## 🎯 Step-by-Step

### Step 1: Jalankan Setup Script

```bash
cd ZENXHAT
bash SETUP_TERMUX.sh
```

**Output:**
```
[1/7] ✓ Termux packages updated
[2/7] ✓ Development tools installed
[3/7] ✓ Git configured
[4/7] ✓ SSH key generated
[5/7] ✓ Git SSH configured
[6/7] ✓ Pip upgraded
[7/7] ✓ Dependencies installed

✨ SETUP COMPLETE! ✨

📋 YOUR SSH PUBLIC KEY:
ss-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB...
```

### Step 2: Add SSH Key ke GitHub

1. **Copy SSH key** dari output (mulai dari `ssh-ed25519`)
2. **Buka** https://github.com/settings/ssh/new
3. **Paste** ke field "Key"
4. **Title**: `Termux-ZENXHAT`
5. **Click** "Add SSH key"

### Step 3: Clone Tanpa Password

```bash
git clone https://github.com/zenCTRLalt/ZENXHAT.git
# <-- TANPA minta username/password!

cd ZENXHAT
python zenxhat/cli/main.py --help
```

---

## 🔐 SSH Key vs Password

### Sebelum Setup
```
git clone https://github.com/user/repo.git
Username: user
Password: <minta token atau password>
^ MEREPOTKAN!
```

### Setelah Setup
```
git clone https://github.com/user/repo.git
^ LANGSUNG CLONE TANPA MINTA!
```

**Cara kerjanya:**
- Git config punya rule: HTTPS → SSH otomatis
- SSH key sudah setup & aman
- GitHub percaya SSH key Anda
- Semua otomatis!

---

## 📁 File-File yang Dibuat Script

Setelah jalankan `SETUP_TERMUX.sh`:

```
~/.ssh/id_ed25519          # Private key (JANGAN share!)
~/.ssh/id_ed25519.pub     # Public key (di-paste ke GitHub)
~/.gitconfig              # Git configuration
```

---

## ✅ Verifikasi Setup Berhasil

```bash
# 1. Check SSH key
ls -la ~/.ssh/
# Output harus ada: id_ed25519 dan id_ed25519.pub

# 2. Check git config
git config --global user.name
git config --global user.email
# Output: zenCTRLalt dan zzid3291@gmail.com

# 3. Test SSH connection
ssh -T git@github.com
# Output: Hi zenCTRLalt! You've successfully authenticated...

# 4. Clone tanpa password
git clone https://github.com/zenCTRLalt/test.git
# Harus bisa tanpa minta password!
```

---

## 🆘 Problem & Solution

### Error: "SSH key not found"

**Cause:** Script gagal generate SSH key

**Fix:**
```bash
ssh-keygen -t ed25519 -C "zzid3291@gmail.com" -N ""
# Enter Enter Enter (no passphrase)

cat ~/.ssh/id_ed25519.pub
# Copy & paste ke GitHub
```

### Error: "Permission denied (publickey)"

**Cause:** SSH key belum di-add ke GitHub

**Fix:**
```bash
# 1. Copy public key
cat ~/.ssh/id_ed25519.pub

# 2. Buka https://github.com/settings/ssh/new
# 3. Paste key
# 4. Click "Add SSH key"

# 5. Test
ssh -T git@github.com
```

### Error: "fatal: could not read Username"

**Cause:** Git belum di-config

**Fix:**
```bash
git config --global user.name "zenCTRLalt"
git config --global user.email "zzid3291@gmail.com"
```

### Error: "pip: command not found"

**Cause:** Python tidak terinstall

**Fix:**
```bash
apt install -y python

# Atau update Termux
apt update && apt upgrade -y
```

---

## 💡 Tips & Tricks

### Backup SSH Key
```bash
# Simpan key di safe place
cp ~/.ssh/id_ed25519 ~/backup/
cp ~/.ssh/id_ed25519.pub ~/backup/
```

### Restore SSH Key (device baru)
```bash
# Copy file ke ~/.ssh/
cp backup/id_ed25519 ~/.ssh/
cp backup/id_ed25519.pub ~/.ssh/

# Set permissions
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### Multiple SSH Keys (jika butuh)
```bash
# Generate key baru
ssh-keygen -t ed25519 -C "other@email.com" -f ~/.ssh/id_ed25519_other

# Config ~/.ssh/config
Host github-other
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_other

# Clone dengan key spesifik
git clone git@github-other:user/repo.git
```

---

## 📚 Reference

- **SSH Key Types**: ED25519 (modern), RSA (legacy)
- **Key Location**: `~/.ssh/id_ed25519`
- **Public Key**: `~/.ssh/id_ed25519.pub`
- **GitHub SSH**: https://github.com/settings/ssh
- **Test SSH**: `ssh -T git@github.com`

---

## 🎯 Workflow Setelah Setup

```bash
# Day 1: Setup (1 kali saja)
bash SETUP_TERMUX.sh
# Add SSH key ke GitHub

# Day 2+: Pakai ZENXHAT (TANPA password!)
git clone https://github.com/.../ZENXHAT.git
cd ZENXHAT

# Develop
python zenxhat/cli/main.py whois google.com

# Push changes
git add .
git commit -m "Fitur baru"
git push origin main    # <-- TANPA PASSWORD!
```

---

## ✨ Summary

✅ **Setup Script** - Otomatis semua
✅ **SSH Key** - Modern ED25519
✅ **TANPA Password** - Selamanya!
✅ **TANPA Username** - Git ingat semuanya
✅ **Aman** - Key tersimpan encrypted
✅ **Permanen** - Tidak expire

**ONE-TIME SETUP, LIFETIME USE! 🔐**
