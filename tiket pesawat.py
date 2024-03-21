print("PEMESANAN TIKET PESAWAT ONLINE")
print("kode penerbangan      tujuan      harga")
print("_________________________________________")
print("001                   Jakarta     1.000.000")
print("002                   Bandung     1.500.000")
print("003                   Aceh        2.000.000")
print("_________________________________________")
print("")
Nama          : input("nama pembeli : ")
Usia          : input("usia pembeli : ")
Nomor         : input("nomor handphone : ")
Jenis_kelamin : input("jenis kelamin")
Asal          : input("asal kota")
Jurusan       : input("kode tujuan penerbangan")
Kelas         : input("kelas yang dipilih")
Tujuan        : []
Harga         : []
if Jurusan=="001":
   tujuan.append("Jakarta")
   harga=1000000
elif Jurusan=="002":
     tujuan.append("Bandung")
     harga = 1500000
elif Jurusan=="003": 
     tujuan.append("Aceh")
     harga=2000000
else :
    tujuan.append("kode salah")
Jumlah = int(input("jumlah_kursi : ")) 
print()
if Jumlah > 3:
    potongan = (Jumlah*Harga)*0.25
else :
    potongan = 0 
    
total = int(Jumlah*Harga-potongan)
print("____________________________________________")

print("Nama pembeli : ", Nama)
print("Usia pembeli : ", Usia)
print("Jenis kelamin : ", Jenis_kelamin)
print("Nomor handphone : ", Nomor)
print("Asal kota : ", Asal)
print("Kota tujuan : ", Tujuan)
print("Jumlah kursi : ", Jumlah)
print("____________________________________________")
print("Harga tiket : ", Harga)
print("potongan : ", potongan)
print("____________________________________________")
print("PEMBAYARAN")
print("Jumlah bayar : Rp.", total)

print("____________________________________________")
print("______________TERIMAKASIH___________________")
