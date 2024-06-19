import os
import time
from termcolor import colored, cprint
os.system('cls')

film = {
    "Garfield": 50000,
    "Snow White": 45000,
    "Rapunzel": 40000,
    "Toy Story": 48000,
    "Frozen": 42000
}

tempat_duduk = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

def tampilkan_daftar_film():
    print("Daftar Film:")
    print(colored(("|{:<25}|{:<14}|".format("Judul Film","Harga Tiket")), "green", "on_red"))
    cprint("-" * 42, "yellow", "on_red")
    for judul, harga in film.items():
        cprint("{:<25} | Rp {:<10}|".format(judul, harga), "green", "on_red")

def tampilkan_tempat_duduk():
    print("Tempat Duduk yang Tersedia:")
    for row in tempat_duduk:
        print(" | ".join(row))

def pesan_tiket():
    tampilkan_daftar_film()
  
    while True:
        film_pilihan = input("Silakan pilih film: ")
        if film_pilihan in film:
            break
        else:
            print("Maaf, film tidak tersedia. Silakan pilih kembali.")
    
    while True:
        jumlah_tiket = int(input("Berapa banyak tiket yang ingin Anda pesan? "))
        if jumlah_tiket > 0:
            break
        else:
            print("Jumlah tiket harus lebih besar dari 0. Silakan masukkan kembali.")
    
    tampilkan_tempat_duduk()
    tempat_duduk_terpilih = []
    for _ in range(jumlah_tiket):
        while True:
            tempat = input("Tempat duduk pilihan Anda: ")
            if any(tempat in row for row in tempat_duduk):
                tempat_duduk_terpilih.append(tempat)
                for row in tempat_duduk:
                    if tempat in row:
                        row[row.index(tempat)] = "XX"
                break
            else:
                print("Maaf, tempat duduk tidak valid atau sudah dipilih. Silakan pilih kembali.")
    
    total_biaya = film[film_pilihan] * jumlah_tiket
    cprint("\nSedang memproses pemesanan...", "green")
    time.sleep(2)
   
    print("\n========= Struk Pembelian =========")
    print("Film:", film_pilihan)
    print("Jumlah Tiket:", jumlah_tiket)
    print("Tempat Duduk:", ', '.join(tempat_duduk_terpilih))
    print("Total Biaya: Rp", total_biaya)
    print("===================================")

    with open("pemesanan.txt", "a") as file:
        file.write(f"Film: {film_pilihan}, Jumlah Tiket: {jumlah_tiket}, Tempat Duduk: {', '.join(tempat_duduk_terpilih)}, Total Biaya: {total_biaya}\n")

def tampilkan_riwayat_pemesanan():
    print("\nRiwayat Pemesanan:")
    if os.path.exists("pemesanan.txt"):
        with open("pemesanan.txt", "r") as file:
            riwayat = file.readlines()
            if riwayat:
                for pesanan in riwayat:
                    print(pesanan, end="")
            else:
                print("Maaf, kamu belum mempunyai riwayat pemesanan.")
    else:
        print("Maaf, kamu belum mempunyai riwayat pemesanan.")

def main():
    while True:
        cprint("Selamat datang di layanan pemesanan tiket bioskop!", "blue", "on_green")
        print("\nMenu:")
        print("1. Pesan Tiket")
        print("2. Tampilkan Riwayat Pemesanan")
        print("3. Keluar")
        
        pilihan = input("Silakan pilih menu: ")
        
        if pilihan == "1":
            pesan_tiket()
        elif pilihan == "2":
            tampilkan_riwayat_pemesanan()
        elif pilihan == "3":
            cprint("Terima kasih telah menggunakan layanan kami. Sampai jumpa!", "blue", "on_green")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

main()
