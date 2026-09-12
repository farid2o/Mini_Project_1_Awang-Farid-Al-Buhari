daftar_pengeluaran = [
    ("sewa sound system", "budi", 500000),
    ("sewa tenda", "andi", 300000),
]

def tampilkan_menu():
    """Fungsi untuk menampilkan menu utama."""
    print("\n" + "="*48)
    print("SISTEM CATATAN PENGELUARAN UANG KAS ANGKATAN")
    print("="*48)
    print("1. Tampilkan seluruh catatan pengeluaran")
    print("2. Tambah catatan pengeluaran baru")
    print("3. ubah data pengeluaran")
    print("4. Hapus data pengeluaran")
    print("5. hitung total pengeluaran uang kas")
    print("6. Keluar")
    print("="*48)

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        print("\n--- DAFTAR PENGELUARAN UANG KAS ---")
        if not daftar_pengeluaran:
            print("Belum ada catatan pengeluaran.")
        else:
            print(f"{'No.':<4} | {'Keperluan / Barang':<25} | {'PJ':<12} | {'Nominal (Rp)':<12}")
            print("-"*60)
            for i, item in enumerate(daftar_pengeluaran, start=1):
                keperluan, pj, nominal = item
                print(f"{i:<4} | {keperluan:<25} | {pj:<12} | Rp{nominal:,.0f}")

    elif pilihan == "2":
        print("\n--- TAMBAH CATATAN PENGELUARAN BARU ---")
        keperluan = input("Masukkan keperluan/barang: ").strip()
        pj = input("Masukkan penanggung jawab (PJ): ").strip()

        if not keperluan or not pj:
            print("Keperluan dan PJ tidak boleh kosong.")
            continue

        try:
            nominal = int(input("Masukkan nominal pengeluaran (Rp): ").strip())
            if nominal > 0:
                daftar_pengeluaran.append((keperluan, pj, nominal))
                print("Catatan pengeluaran berhasil ditambahkan.")
            else:
                print("\n[GAGAL] Nominal pengeluaran harus lebih dari 0!")
        except ValueError:
            print("\n[GAGAL] Nominal pengeluaran harus berupa angka!")

    elif pilihan == "3":
        print("\n--- UBAH DATA PENGELUARAN ---")
        if not daftar_pengeluaran:
            print("[INFO] Tidak ada data pengeluaran untuk diubah.")
        else:
            for i, item in enumerate(daftar_pengeluaran, start=1):
                print(f"{i}. {item[0]} (PJ: {item[1]}, Nominal: Rp{item[2]:,.0f})")

            try:
                nomor = int(input("Masukkan nomor data yang ingin diubah: ").strip()) -1

                if 0 <= nomor < len(daftar_pengeluaran):
                    print("\n--- MASUKKAN DATA PEMBARUAN ---")
                    keperluan_baru = input("Masukkan keperluan/barang baru: ").strip()
                    pj_baru = input("Masukkan PJ baru: ").strip()

                    if not keperluan_baru or not pj_baru:
                        print("\n[GAGAL] Keperluan dan PJ tidak boleh kosong!")
                        continue

                    nominal_baru = input("Masukkan nominal pengeluaran baru (Rp): ").strip()
                    if not nominal_baru:
                        print("\n[GAGAL] Nominal pengeluaran tidak boleh kosong!")
                        continue

                    try:
                        nominal_baru = int(nominal_baru)
                        if nominal_baru > 0:
                            daftar_pengeluaran[nomor] = (keperluan_baru, pj_baru, nominal_baru)
                            print("\n[BERHASIL] Data pengeluaran berhasil diubah.")
                        else:
                            print("\n[GAGAL] Nominal pengeluaran harus lebih dari 0!")
                    except ValueError:
                        print("\n[GAGAL] Nominal pengeluaran harus berupa angka!")
                else:
                    print("\n[GAGAL] Nomor data tidak ditemukan!")
            except ValueError:
                print("\n[GAGAL] Input nomor dan nominal harus berupa angka!")

    elif pilihan == "4":
        print("\n--- HAPUS DATA PENGELUARAN ---")
        if not daftar_pengeluaran:
            print("[INFO] Tidak ada data pengeluaran untuk dihapus.")
        else:
            for i, item in enumerate(daftar_pengeluaran, start=1):
                print(f"{i}. {item[0]} (PJ: {item[1]}, Nominal: Rp{item[2]:,.0f})")

            try:
                nomor = int(input("Masukkan nomor data yang ingin dihapus: ").strip()) -1

                if 0 <= nomor < len(daftar_pengeluaran):
                    terhapus = daftar_pengeluaran.pop(nomor)
                    print(f"\n[BERHASIL] Data pengeluaran '{terhapus[0]}' berhasil dihapus.")
                else:
                    print("\n[GAGAL] Nomor data tidak ditemukan!")
            except ValueError:
                print("\n[GAGAL] Input nomor harus berupa angka!")

    elif pilihan == "5":
        print("\n--- TOTAL PENGELUARAN UANG KAS ---")
        if not daftar_pengeluaran:
            print("[INFO] Tidak ada data pengeluaran untuk dihitung.")
        else:
            total_pengeluaran = sum(item[2] for item in daftar_pengeluaran)
            jumlah_transaksi = len(daftar_pengeluaran)

            print(f"total transaksi pengeluaran  : {jumlah_transaksi} Transaksi")
            print(f"total pengeluaran uang kas   : Rp{total_pengeluaran:,.0f}")

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan sistem catatan pengeluaran uang kas.")
        break


    else:
        print("\n[GAGAL] Pilihan menu tidak valid! Silakan pilih menu antara 1-6.")