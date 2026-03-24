import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def whatsapp_bot():
    # Setup Driver Otomatis
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Aktifkan jika di server tanpa layar
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("https://web.whatsapp.com/")
    print("\n[!] Silakan scan QR Code di browser yang terbuka.")
    
    # Tunggu sampai login berhasil (mencari bar pencarian)
    wait = WebDriverWait(driver, 100)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))

    while True:
        names = input("\nMasukkan nama kontak/grup (pisahkan dengan koma jika banyak): ").split(',')
        msg = input("Masukkan pesan: ")
        count = int(input("Kirim berapa kali per orang? (Isi 1 jika tidak ingin spam): "))

        for name in [n.strip() for n in names]:
            try:
                print(f"[*] Mencari kontak: {name}")
                # Cari kontak di bar pencarian agar lebih akurat
                search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
                search_box.clear()
                search_box.send_keys(name)
                time.sleep(2)
                search_box.send_keys(Keys.ENTER)
                time.sleep(1)

                # Cari kotak pesan
                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                
                for i in range(count):
                    msg_box.send_keys(msg)
                    msg_box.send_keys(Keys.ENTER)
                    print(f"[+] Berhasil mengirim ke {name} ({i+1}/{count})")
                    time.sleep(0.5)

            except Exception as e:
                print(f"[!] Gagal mengirim ke {name}. Pastikan nama kontak benar.")

        again = input("\nKirim pesan lagi? (y/n): ")
        if again.lower() != 'y':
            print("Terima kasih telah menggunakan bot ini!")
            driver.quit()
            break

if __name__ == "__main__":
    whatsapp_bot()
