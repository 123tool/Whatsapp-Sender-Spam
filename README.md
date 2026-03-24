# 🚀 WhatsApp Sender Spam

Script Python sederhana untuk mengirim pesan otomatis (bulk send) atau spam chat ke beberapa kontak sekaligus menggunakan Selenium. Bisa dijalankan di Windows, Linux, maupun MacOS.

## ✨ Fitur
- **Multi-User**: Kirim pesan ke banyak kontak sekaligus hanya dengan dipisahkan koma.
- **Spam Mode**: Mengirim pesan yang sama berkali-kali ke satu kontak.
- **Auto-Driver**: Tidak perlu download `chromedriver` manual (menggunakan `webdriver-manager`).
- **Stable Selector**: Menggunakan XPATH yang lebih dinamis dibanding class name.

## 🛠️ Persyaratan Sistem
1. **Python 3.7+**
2. **Google Chrome** versi terbaru.
3. Koneksi Internet.

## 📥 Instalasi

### Windows / Linux / MacOS
1. Clone repository ini:
   ```bash
   git clone [https://github.com/123tool/Whatsapp-Sender-Spam.git]
   cd Whatsapp-Sender-Spam
   python whatsapp_bot.py
2. Install library yang dibutuhkan:
```bash
   pip install selenium webdriver-manager

Termux (Android) :
​Catatan: Menjalankan Selenium di Termux memerlukan instalasi package tur-repo dan chromium.

pkg update && pkg upgrade
pkg install python chromium chromedriver
pip install selenium
python whatsapp_bot.py

