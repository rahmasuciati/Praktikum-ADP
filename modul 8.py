n = int(input("jumlah data")
for i in range n():
	tanggal = int(input("tanggal : "))
	keterangan = string(input("keterangan : "))
	jumlah = int(input("jumlah : "))
	tipe = string(input("tipe : "))
	
data_keuangan = open("data_keuangan.txt", "a")
data_keuangan.write("tanggal" + "," + "keterangan" + "," + "jumlah" + "," + "tipe" + ",")
data_keuangan.close()

print(f"| {tanggal:<7} | {keterangan:<7} | {jumlah:<7} | {tipe:<7} |)