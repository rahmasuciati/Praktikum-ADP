daftar_barang = [
    ["  Telur",        3000, 150],
    ["  Kopi",         3000, 35],
    ["  Mie",          4000, 155],
    ["  Sabun",      5000, 300],
    ["  Gas",          28000, 30],
    ["  Beras",      40000, 46]
]

print("\n                                                                           ")
print("------DAFTAR BARANG TOKO KELONTONG RAHMA------")
print("\n                                                                           ")

print("  Nama Barang\tHarga\tStok")
for barang in daftar_barang:
    print(f"{barang[0]}\t\t{barang[1]}\t{barang[2]}")


keuntungan = []
for barang in daftar_barang:
    keuntungan.append((barang[1] - barang[2]) * barang[2])

nama_barang_terbesar = daftar_barang[keuntungan.index(max(keuntungan))][0]
nama_barang_terkecil = daftar_barang[keuntungan.index(min(keuntungan))][0]
total_keuntungan = sum(keuntungan)

print("\n==============================================")
print("\n  Barang dengan keuntungan terbesar:", nama_barang_terbesar)
print("\n                                                                           ")
print("\n  Barang dengan keuntungan terkecil:", nama_barang_terkecil)
print("\n                                                                           ")
print("\n  Total keuntungan:", total_keuntungan)
print("\n==============================================")
