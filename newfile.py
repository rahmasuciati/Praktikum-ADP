def diketahui(kecepatan_awal, percepatan, waktu):
    """
  Fungsi untuk menghitung kecepatan akhir dan jarak tempuh dalam GLBB.

 Args:
        kecepatan_awal (float): Kecepatan awal benda (m/s).
        percepatan (float): Percepatan benda (m/s^2).
        waktu (float): Waktu (s).

  Returns:
         tuple: Tuple yang berisi kecepatan akhir (m/s) dan jarak yang ditempuh (m).
    """
    kecepatan_akhir = kecepatan_awal + percepatan * waktu
    jarak = kecepatan_awal * waktu + 0.5 * percepatan * waktu ** 2

    return kecepatan_akhir, jarak

def main():
    print("Menghitung Kecepatan Akhir dan Jarak Tempuh Benda Dalam GLBB")
    print("=" * 60)

    data = []
    n = int(input("Masukkan jumlah inputan: "))

    for i in range(n):
        print(f"\nInputan ke-{i + 1}")
        kecepatan_awal = float(input("Masukkan kecepatan awal (m/s): "))
        percepatan = float(input("Masukkan percepatan (m/s^2): "))
        waktu = float(input("Masukkan waktu (s): "))

        kecepatan_akhir, jarak = diketahui(kecepatan_awal, percepatan, waktu)
        data.append((kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak))

    print("\nTabel Hasil Perhitungan")
    print("=" * 70)
    print("| No | Kecepatan Awal | Percepatan | Waktu | Kecepatan Akhir | Jarak |")
    print("|----|----------------|------------|-------|-----------------|-------|")

    for i, (kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak) in enumerate(data, 1):
        print(f"|{i:3d} |{kecepatan_awal:10.2f}      |{percepatan:7.2f}     |{waktu:5.2f}  | {kecepatan_akhir:10.2f}      |{jarak:5.2f}  |")

    print("=" * 70)

if __name__ == "__main__":
    main()