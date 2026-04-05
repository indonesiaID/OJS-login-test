# 🔐 OJS Login Tester (CSV + CSRF + Role Detection)

Tool sederhana berbasis Python untuk melakukan pengujian login pada sistem **Open Journal Systems (OJS)** menggunakan daftar username & password dari file CSV.

---

## ✨ Fitur

* ✅ Support input dari file `.csv`
* 🔐 Auto ambil **CSRF Token**
* 🔑 Login checker (Success / Failed)
* 🎭 Deteksi role user:

  * Site Administrator
  * Journal Manager
  * Section Editor
  * Assistant
  * Author
  * Reviewer
  * Reader
* 💾 Auto save hasil login sukses ke file `.txt`
* 🎨 Output berwarna (Hijau = Success, Merah = Failed)

---

## 📂 Struktur File

```
project/
│── main.py
│── list.csv
│── result_success.txt
```

---

## 📥 Format CSV

Contoh file `list.csv`:

```
username,password
admin,admin123
user,test123
bangrizal,12345678
```

---

## ⚙️ Instalasi

### 1. Install Python (jika belum ada)

```
sudo apt install python3
```

### 2. Install dependencies

```
pip install requests
```

> Jika menggunakan Kali Linux / Debian terbaru:

```
pip install requests --break-system-packages
```

atau gunakan virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install requests
```

---

## 🚀 Cara Menjalankan

```
python3 main.py
```

---

## 🧪 Contoh Output

```
[✔] SUCCESS: admin:admin123 | ROLE: MANAGER
[✘] FAILED : user:test123
[✔] SUCCESS: bangrizal:12345678 | ROLE: AUTHOR
```

---

## 📄 Output File

Hasil login sukses akan otomatis tersimpan di:

```
result_success.txt
```

Contoh isi:

```
admin:admin123 | MANAGER
bangrizal:12345678 | AUTHOR
```

---

## ⚠️ Catatan Penting

* CSRF Token bersifat **dinamis**, script akan mengambil otomatis setiap request.
* Deteksi role berdasarkan **keyword HTML**, sehingga tidak selalu 100% akurat.
* Beberapa sistem mungkin memiliki proteksi tambahan:

  * CAPTCHA
  * Rate limiting
  * WAF / Firewall

---

## ⚖️ Disclaimer

Tool ini dibuat hanya untuk:

* 🔬 Pembelajaran
* 🛠️ Pengujian keamanan (pentest)
* 🐞 Bug bounty (dengan izin resmi)

**Dilarang digunakan untuk aktivitas ilegal atau tanpa izin.**

---

## 👨‍💻 Author

* Dibuat untuk kebutuhan testing & automation login OJS

---

## ⭐ Support

Jika project ini membantu, jangan lupa:

* ⭐ Star repository
* 🍴 Fork
* 🛠️ Improve & contribute

---
