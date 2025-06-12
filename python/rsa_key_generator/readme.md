
# 🔐 RSA Key Generator & Validator (Python GUI)

A simple Python GUI application to generate **encrypted RSA key pairs** and **validate** that a private key matches its public key.

---

## ✨ Fitur

- ✅ Membuat **RSA private key** terenkripsi (dengan passphrase)
- ✅ Membuat **RSA public key** pasangan dari private key
- ✅ Menentukan lokasi penyimpanan file
- ✅ Memilih ukuran key: 2048, 3072, 4096 bit
- ✅ Validasi pasangan private dan public key
- ✅ Menyimpan hasil sebagai file `.pem`
- ✅ Antarmuka pengguna grafis (GUI) menggunakan Tkinter

---

## 🛠 Kebutuhan Sistem

- Python 3.7 atau lebih tinggi
- Paket yang dibutuhkan:
  - `cryptography`
  - `tkinter` (bawaan Python, umumnya sudah tersedia)

### Instalasi Dependensi

```bash
pip install cryptography
```

---

## 🚀 Cara Menjalankan

```bash
```
> - `rsa_generate.py` → untuk pembuatan key
> - `rsa_validate.py` → untuk validasi key

---

## 📦 Konversi ke File `.exe`

Untuk menjadikan aplikasi ini sebagai executable file (.exe), gunakan PyInstaller:

### Langkah-langkah:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Jalankan perintah build:

```bash
pyinstaller --onefile --windowed rsa_gui.py --name rsa-keygen
```

Hasil build akan berada di folder `dist/`.

---

## 🔐 Catatan Keamanan

- Private key dienkripsi menggunakan **passphrase** yang dimasukkan pengguna
- Jangan bagikan passphrase Anda
- Simpan private key Anda di tempat yang aman

---

## ✅ Validasi RSA Key Pair

Aplikasi juga menyediakan fungsi untuk memastikan bahwa **private key** dan **public key** benar-benar berpasangan:

- Private key digunakan untuk mendekripsi data yang dienkripsi menggunakan public key
- Validasi dilakukan dengan mengenkripsi string acak menggunakan public key dan mendekripsi menggunakan private key

---

## 📚 Referensi

- [RFC 8017 - PKCS #1: RSA Cryptography Specifications](https://datatracker.ietf.org/doc/html/rfc8017)
- [Cryptography.io Documentation](https://cryptography.io/en/latest/)
- [PyCryptodome](https://www.pycryptodome.org/)
- [Wikipedia - RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

---