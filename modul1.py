import json
import os
import csv
import shutil
from collections import defaultdict

FILE_DATA = "keuangan.json"
FILE_BACKUP = "keuangan_backup.json"


def load_data():
    if not os.path.exists(FILE_DATA):
        return []
    with open(FILE_DATA, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def backup_data():
    if os.path.exists(FILE_DATA):
        shutil.copy(FILE_DATA, FILE_BACKUP)


def tampilkan_tabel(data):
    if not data:
        print("Tidak ada data")
        return

    print("No  Tanggal            Jenis     Kategori        Jumlah")
    print("-------------------------------------------------------")

    for i, t in enumerate(data, 1):
        print(
            str(i).ljust(3),
            t["tanggal"].ljust(17),
            t["jenis"].ljust(9),
            t["kategori"].ljust(14),
            t["jumlah"]
        )


def tambah_transaksi(data):
    tanggal = input("Tanggal: ").strip()
    jenis = input("Jenis income atau expense: ").strip().lower()
    kategori = input("Kategori: ").strip()

    try:
        jumlah = float(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka")
        return

    if not tanggal or not kategori or jenis not in ("income", "expense") or jumlah <= 0:
        print("Data tidak valid")
        return