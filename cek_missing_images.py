import os
import re
from datetime import datetime

# Lokasi file dan folder (relatif terhadap lokasi script ini)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ITEMS_LUA = os.path.join(BASE_DIR, "items.lua")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_TXT = os.path.join(BASE_DIR, "hasil_cek_missing_images.txt")


def baca_items(path):
    """Baca items.lua dan ambil pasangan (name, image) dari tiap item."""
    with open(path, "r", encoding="utf-8") as f:
        isi = f.read()

    items = []
    # Ambil setiap definisi item: name = '...' ... image = '...'
    pola = re.compile(
        r"name\s*=\s*'([^']+)'.*?image\s*=\s*'([^']+)'",
        re.DOTALL,
    )
    # Proses baris per baris supaya tiap item cocok satu-satu
    for baris in isi.splitlines():
        m = re.search(r"name\s*=\s*'([^']+)'.*?image\s*=\s*'([^']+)'", baris)
        if m:
            nama = m.group(1)
            gambar = m.group(2)
            items.append((nama, gambar))
    return items


def daftar_gambar(folder):
    """Kumpulkan semua nama file gambar yang ada di folder (lowercase)."""
    if not os.path.isdir(folder):
        return set()
    return {nama.lower() for nama in os.listdir(folder)}


def main():
    items = baca_items(ITEMS_LUA)
    gambar_tersedia = daftar_gambar(IMAGES_DIR)

    missing = []
    for nama, gambar in items:
        if gambar.lower() not in gambar_tersedia:
            missing.append((nama, gambar))

    total = len(items)
    total_missing = len(missing)

    baris_output = []
    baris_output.append("=" * 60)
    baris_output.append("LAPORAN CEK ITEM TANPA GAMBAR (MISSING IMAGES)")
    baris_output.append("Tanggal: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    baris_output.append("=" * 60)
    baris_output.append("")
    baris_output.append(f"Total item di items.lua : {total}")
    baris_output.append(f"Total gambar tersedia   : {len(gambar_tersedia)}")
    baris_output.append(f"Total item TANPA gambar : {total_missing}")
    baris_output.append("")
    baris_output.append("-" * 60)

    if missing:
        baris_output.append("DAFTAR ITEM YANG GAMBARNYA TIDAK ADA:")
        baris_output.append("-" * 60)
        baris_output.append(f"{'NO':<5}{'NAMA ITEM':<30}{'FILE GAMBAR YANG DICARI'}")
        baris_output.append("-" * 60)
        for i, (nama, gambar) in enumerate(missing, start=1):
            baris_output.append(f"{i:<5}{nama:<30}{gambar}")
    else:
        baris_output.append("SEMUA ITEM MEMILIKI GAMBAR. TIDAK ADA YANG MISSING.")

    baris_output.append("-" * 60)

    hasil = "\n".join(baris_output)

    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(hasil + "\n")

    # Tampilkan juga di terminal
    print(hasil)
    print()
    print(f"Hasil disimpan ke: {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
