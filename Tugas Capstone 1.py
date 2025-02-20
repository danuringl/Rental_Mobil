# DATA DUMMY
rental_mobil = [
    {"id": 1, "merk": "Toyota Avanza", "tahun": 2020, "harga": 350000},
    {"id": 2, "merk": "Honda Brio", "tahun": 2019, "harga": 300000},
    {"id": 3, "merk": "Suzuki Ertiga", "tahun": 2021, "harga": 370000}
]

# CREATE DATA
def tambah_mobil():
    id_mobil = len(rental_mobil) + 1
    merk = input("Masukkan merk mobil: ")
    tahun = int(input("Masukkan tahun mobil: "))
    harga = int(input("Masukkan harga sewa per hari: "))
    rental_mobil.append({"id": id_mobil, "merk": merk, "tahun": tahun, "harga": harga})
    print("Mobil berhasil ditambahkan!\n")

# READ DATA
def tampilkan_mobil():
    print("\nDaftar Mobil yang Tersedia:")
    for mobil in rental_mobil:
        print(f"ID: {mobil['id']}, Merk: {mobil['merk']}, Tahun: {mobil['tahun']}, Harga: {mobil['harga']}/hari")
    print()

# UPDATE DAATA
def update_mobil():
    tampilkan_mobil()
    id_mobil = int(input("Masukkan ID mobil yang ingin diperbarui: "))
    for mobil in rental_mobil:
        if mobil["id"] == id_mobil:
            mobil["merk"] = input("Masukkan merk baru: ")
            mobil["tahun"] = int(input("Masukkan tahun baru: "))
            mobil["harga"] = int(input("Masukkan harga sewa baru: "))
            print("Data mobil berhasil diperbarui!\n")
            return
    print("ID mobil tidak ditemukan!\n")

# DELETE DATA
def hapus_mobil():
    tampilkan_mobil()
    id_mobil = int(input("Masukkan ID mobil yang ingin dihapus: "))
    global rental_mobil
    rental_mobil = [mobil for mobil in rental_mobil if mobil["id"] != id_mobil]
    print("Mobil berhasil dihapus!\n")

# MENU UTAMA
def menu():
    while True:
        print("\n=== Sistem Rental Mobil ===")
        print("1. Tambah Mobil")
        print("2. Lihat Daftar Mobil")
        print("3. Update Mobil")
        print("4. Hapus Mobil")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_mobil()
        elif pilihan == "2":
            tampilkan_mobil()
        elif pilihan == "3":
            update_mobil()
        elif pilihan == "4":
            hapus_mobil()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan rental mobil!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Jalankan program
if __name__ == "__main__":
    menu()
