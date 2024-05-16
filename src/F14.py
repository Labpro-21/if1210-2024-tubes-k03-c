import argparse
import os
import time
import sys
import parser_csv

# Fungsi load() akan dipanggil saat program dijalankan. Fungsi ini bertanggung jawab untuk memuat data dari folder yang ditentukan oleh argumen
def load() -> None:
    parser = argparse.ArgumentParser() # Ini adalah objek ArgumentParser dari modul argparse yang digunakan untuk mendefinisikan argumen yang akan diproses oleh program
    parser.add_argument("folder", help= 'path ke folder save data. Gunakan "default" untuk load data')
    args = parser.parse_args(args = None if sys.argv[1:] else ['--help'])

    trackload = os.path.join(os.getcwd(), "data", args.folder)
    # Ini adalah jalur lengkap ke folder penyimpanan data yang akan dimuat. Jalur ini dibuat berdasarkan jalur saat ini (os.getcwd()) dan nama folder yang diberikan oleh pengguna.
    
    if not os.path.isdir(trackload):
        sys.exit("Folder tidak ditemukan. Pastikan folder ada di ./data/, Usage : python main.py <nama_folder>!")

    print('Folder "{}" ditemukan.'.format(args.folder))

    print("Loading...")

    print("Selamat datang di program OWCA!")

    parser_csv.parse(trackload)
    time.sleep(2)
    return
