import csv
import os

file = "nilai.csv"

if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        tulis = csv.writer(f)
        tulis.writerow(["No", "Nama", "Nilai"])


while True:
    print("\n=== SISTEM NILAI MAHASISWA ===")
    print("1. Tampilkan daftar nilai")
    print("2. Tambah nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n=== DATA NILAI ===")

        with open(file, "r") as f:
            baca = csv.reader(f)
            for data in baca:
                print(data[0], data[1], data[2])

    elif pilihan == "2":
        nama = input("Nama mahasiswa: ")
        nilai = input("Nilai: ")
        with open(file, "r") as f:
            jumlah_data = sum(1 for baris in f) - 1

        no = jumlah_data + 1

        with open(file, "a", newline="") as f:
            tulis = csv.writer(f)
            tulis.writerow([no, nama, nilai])

        print("Data berhasil ditambahkan!")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
