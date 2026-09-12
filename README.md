# Mini_Project_1_Awang-Farid-Al-Buhari

NAMA: AWANG FARID AL BUHARI
NIM : 2609116003

# Sistem Catatan Pengeluaran Uang Kas Angkatan

## Deskripsi Program
Program ini adalah aplikasi simpel berbasis teks (Command Line) yang dibuat untuk membantu bendahara atau pengurus angkatan dalam mencatat pengeluaran uang kas. Daripada mencatat manual di buku yang rawan hilang, program ini mengolah pembukuan kas angkatan jadi lebih rapi, digital, dan gampang dipantau.

## Tujuan
1. Praktis: Memudahkan bendahara mencatat, mengedit, dan menghapus riwayat pengeluaran kas tanpa repot.

2. Transparan: Menampilkan rekap total pengeluaran uang kas secara akurat biar semua teman angkatan tahu uangnya dipakai untuk apa saja.

3. Aman dari Error: Mencegah program crash jika ada salah ketik (misalnya mengetik huruf di bagian yang harusnya angka).


## Fitur Program
1. Menampilkan seluruh catatan pengeluaran
2. Menambahkan catatan pengeluaran
3. Mengubah data pengeluaran
4. Menghapus data pengeluaran
5. Menghitung total pengeluaran
6. Keluar dari program

## Struktur Data
1. List (Wadah Utama): Data disimpan di dalam variabel bertipe List bernama daftar_pengeluaran. List dipakai karena sifatnya fleksibel (mutable), jadi datanya bisa kita tambah, ubah, atau hapus kapan saja saat program jalan.

2. Tuple (Isi Data): Setiap 1 baris pengeluaran dibungkus menggunakan Tuple yang isinya ada 3 elemen:

A. Keperluan / Barang: Nama barang atau kegiatan yang dibeli/disewa.

B. Penanggung Jawab (PJ): Nama teman yang memegang/mengurus pengeluaran tersebut.

C. Nominal Biaya: Jumlah uang kas yang dikeluarkan (berupa angka).


## Alur Program
### 1. Inisialisasi Data & Menampilkan Menu Utama

- Program dimulai dengan menyiapkan variabel daftar_pengeluaran yang berisi data awal transaksi.

- Program memasuki perulangan (looping) while True dan menampilkan 6 pilihan menu utama ke layar.

### 2. Menerima Input Pilihan Pengguna

- Pengguna diminta memasukkan angka pilihan (1–6).

- Program akan memeriksa angka yang diinput:

### 3. Eksekusi Menu Sesuai Pilihan

- Pilihan 1 (Tampilkan Seluruh Catatan):

 *Program mengecek apakah daftar_pengeluaran kosong.

 *Jika ada isinya, program menampilkan seluruh daftar pengeluaran dalam bentuk tabel rapi.

- Pilihan 2 (Tambah Catatan Baru):

 *Pengguna menginput nama keperluan, PJ, dan nominal uang.

 *Program memvalidasi agar input tidak boleh kosong dan nominal harus berupa angka lebih dari 0.

 *Jika valid, data baru ditambahkan ke daftar_pengeluaran.

- Pilihan 3 (Ubah Data):

 *Program menampilkan daftar pengeluaran beserta nomor urutnya.

 *Pengguna memilih nomor data yang ingin diubah.

 *Jika nomor ditemukan, pengguna menginput data pembaruan (keperluan, PJ, nominal baru).

 *Jika valid, data lama pada posisi tersebut diperbarui.

- Pilihan 4 (Hapus Data):

 *Program menampilkan daftar pengeluaran.

 *Pengguna memilih nomor data yang ingin dihapus.

 *Jika nomor valid, data tersebut dihapus dari daftar_pengeluaran menggunakan perintah .pop().

- Pilihan 5 (Hitung Total Pengeluaran):

 *Program menjumlahkan seluruh nominal pengeluaran secara otomatis (sum()) dan menghitung total transaksi (len()), lalu menampilkan hasilnya.

- Pilihan 6 (Keluar):

 *Program menampilkan pesan terima kasih dan menghentikan perulangan menggunakan perintah break.

### 4. Penanganan Input Tidak Valid (Validation & Error Handling)

- Jika pengguna memilih angka di luar 1–6, program menampilkan pesan error dan kembali ke menu utama.

- Jika pengguna salah memasukkan huruf pada input yang meminta angka (seperti nominal atau nomor data), sistem try-except akan menangkap error tersebut agar program tidak mendadak crash.

### 5. Program Selesai

- Perulangan berhenti saat pengguna memilih menu 6, dan proses program dinyatakan selesai.

## Flowchart
<img width="867" height="1110" alt="flowchart mini project DDPpp drawio" src="https://github.com/user-attachments/assets/97af8889-6454-452d-9f86-76ad64f56e3f" />

## Validasi
Untuk mencegah program crash atau menyimpan data yang asal-asalan, program ini dilengkapi dengan beberapa lapis pengecekan (validation & error handling):
### Mencegah Input Kosong:
Pada menu Tambah (Menu 2) dan Ubah (Menu 3), nama keperluan dan PJ diperiksa menggunakan .strip(). Jika pengguna hanya menekan Enter tanpa mengetik apa pun atau hanya menginput spasi, sistem akan menolak data tersebut dan memberikan pesan peringatan.
### Penanganan Error Angka (try-except ValueError):
Saat pengguna diminta menginput nominal uang atau memilih nomor urut data (menu 2, 3, dan 4), sistem dibungkus dengan perintah try-except. Jika pengguna tidak sengaja memasukkan huruf atau simbol (misal: "seribu" atau "10k"), program tidak akan crash melainkan menampilkan pesan [GAGAL] Input harus berupa angka!.
### Pencegahan Nominal Nol atau Negatif:
Sistem memastikan bahwa nominal pengeluaran kas harus lebih besar dari 0 (nominal > 0). Pengguna tidak bisa memasukkan nominal 0 atau angka minus.
### Validasi Jangkauan Nomor Data (Index Out of Range):
Pada menu Ubah (Menu 3) dan Hapus (Menu 4), sistem mengecek apakah nomor data yang dipilih pengguna benar-benar ada di dalam daftar (0 <= nomor < len(daftar_pengeluaran)). Jika pengguna memilih nomor yang tidak ada (misalnya memilih nomor 10 padahal data cuma ada 2), program akan menginfokan bahwa nomor data tidak ditemukan. 
### Validasi Pilihan Menu Utama:
Di menu utama, jika pengguna memasukkan pilihan selain angka 1 sampai 6 (misalnya ketik angka 9 atau huruf 'a'), sistem akan menolak input tersebut dan meminta pengguna memilih ulang angka 1–6


## Contoh Output
### 1. Menampilkan Data
<img width="637" height="655" alt="Screenshot 2026-09-12 120823" src="https://github.com/user-attachments/assets/489e919d-146b-4a07-8ffb-50f93e129ff0" />

### 2. Menambah Data
<img width="441" height="170" alt="Screenshot 2026-09-12 121053" src="https://github.com/user-attachments/assets/a39524a8-72fa-4a96-8af8-fca26d895593" />

### 3. Mengubah Data
<img width="490" height="321" alt="Screenshot 2026-09-12 121326" src="https://github.com/user-attachments/assets/46df1246-133c-483f-be54-f83fbefd4635" />

### 4. Menghapus Data
<img width="600" height="212" alt="Screenshot 2026-09-12 121604" src="https://github.com/user-attachments/assets/5676068c-4f31-445a-b34f-76dca33dbc0f" />

### 5. Menghitung Total
<img width="448" height="128" alt="Screenshot 2026-09-12 121743" src="https://github.com/user-attachments/assets/770391d7-38f8-4196-aa93-a563d6610ecc" />

### 6. Input Tidak Valid
<img width="612" height="108" alt="Screenshot 2026-09-12 121859" src="https://github.com/user-attachments/assets/85af1cf7-8b49-46ae-af5c-7c452dd24502" />

### 7. Screenshot Lengkap Output
<img width="1920" height="1080" alt="Screenshot (95)" src="https://github.com/user-attachments/assets/317f3c4c-fb48-478b-99b6-ad85124646de" />

<img width="1920" height="1080" alt="Screenshot (96)" src="https://github.com/user-attachments/assets/8328363c-bce0-4bb2-a761-9235393f8bbf" />

<img width="1920" height="1080" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/d76ef2fe-a29a-48cf-af13-ff06373e4a99" />

<img width="1920" height="1080" alt="Screenshot (98)" src="https://github.com/user-attachments/assets/54fbdee5-debd-4abc-bbe5-1944b4109701" />


## Teknologi
- Python
- List dan Tuple
- Conditional Statement
- Perulangan while
- Exception Handling

