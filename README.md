![preview1](https://r2.fivemanage.com/WX5Hv6yMgODTgG2WF6rml/images/backgroundgithub.png)

# Cek Missing Images - RSG Inventory

Script Python sederhana untuk mengecek item di file `items.lua` (RSGShared.Items) yang **tidak memiliki file gambar** di folder `images/`. Hasil pengecekan disimpan dalam bentuk file `.txt` yang mudah dibaca.

## Fitur

- Membaca seluruh item dari `items.lua` (mengambil pasangan `name` dan `image`).
- Membandingkan nama file gambar dengan file yang ada di folder `images/`.
- Menampilkan daftar item yang gambarnya **tidak ditemukan**.
- Menyimpan laporan lengkap ke `hasil_cek_missing_images.txt`.
- Pengecekan nama file **tidak case-sensitive** (huruf besar/kecil dianggap sama).

## Struktur Folder

```
cek-missing-images-rsg-inventory/
├── cek_missing_images.py          # Script utama
├── items.lua                      # File item yang dicek
├── hasil_cek_missing_images.txt   # Hasil output (otomatis dibuat)
└── images/                        # Folder berisi semua gambar item
    ├── bread.png
    ├── water.png
    └── ...
```

## Persyaratan

- **Python 3.6** atau lebih baru.
- Tidak butuh library tambahan (hanya modul bawaan Python: `os`, `re`, `datetime`).

Cek apakah Python sudah terpasang:

```powershell
python --version
```

Jika belum ada, unduh dari [python.org/downloads](https://www.python.org/downloads/) dan saat instalasi centang **"Add Python to PATH"**.

## Cara Pemasangan

1. Salin/letakkan semua file dalam satu folder yang sama seperti struktur di atas.
2. Pastikan file `items.lua` dan folder `images/` berada **sejajar** dengan `cek_missing_images.py`.
3. Tidak ada instalasi library tambahan yang diperlukan.

## Cara Menjalankan

Buka terminal (PowerShell) di dalam folder project, lalu jalankan:

```powershell
python cek_missing_images.py
```

Hasil akan:
- Ditampilkan langsung di terminal, dan
- Disimpan otomatis ke file `hasil_cek_missing_images.txt`.

## Contoh Output

```
============================================================
LAPORAN CEK ITEM TANPA GAMBAR (MISSING IMAGES)
Tanggal: 2026-07-30 11:03:44
============================================================

Total item di items.lua : 178
Total gambar tersedia   : 252
Total item TANPA gambar : 11

------------------------------------------------------------
DAFTAR ITEM YANG GAMBARNYA TIDAK ADA:
------------------------------------------------------------
NO   NAMA ITEM                     FILE GAMBAR YANG DICARI
------------------------------------------------------------
1    fieldbandage                  fieldbandage.png
2    birdpost                      birdpost.png
...
------------------------------------------------------------
```

## Catatan

- Jika sebuah item terdeteksi "missing", cek dulu apakah penyebabnya karena **salah ketik nama file** (misalnya `splitpoint` vs `split_point`, atau `intertwined` vs `interwined`), bukan benar-benar gambar yang hilang.
- Untuk menambah gambar yang kurang, cukup letakkan file `.png` dengan nama yang **sama persis** seperti nilai `image` di `items.lua` ke dalam folder `images/`.
- Jalankan ulang script kapan saja setelah menambah/menghapus item atau gambar untuk memperbarui laporan.

## Cara Kerja Singkat

1. Script membaca `items.lua` baris per baris dan mengambil nilai `name` serta `image` dari tiap item menggunakan regex.
2. Semua nama file di folder `images/` dikumpulkan menjadi satu daftar.
3. Setiap `image` dari item dicek keberadaannya di daftar gambar.
4. Item yang gambarnya tidak ditemukan dimasukkan ke laporan dan ditulis ke file `.txt`.
