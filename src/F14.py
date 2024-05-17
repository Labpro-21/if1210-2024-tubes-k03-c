import argparse
import os
import time
import sys
import operateCSV

# Fungsi load() akan dipanggil saat program dijalankan. Fungsi ini bertanggung jawab untuk memuat data dari folder yang ditentukan oleh argumen
def load() -> None:
    parser = argparse.ArgumentParser() # Ini adalah objek ArgumentParser dari modul argparse yang digunakan untuk mendefinisikan argumen yang akan diproses oleh program
    parser.add_argument("folder", help= 'path ke folder save data. Gunakan "default" untuk load data')
    args = parser.parse_args(args = None if sys.argv[1:] else ['--help'])

    namafolder = args.folder
    namafolder = os.path.join('data', namafolder)
    
    if not os.path.isdir(namafolder):
        sys.exit("Folder tidak ditemukan. Pastikan folder ada di ./data/, Usage : python main.py <nama_folder>!")
    
    print('Folder "{}" ditemukan.'.format(args.folder))

    print("Loading...")

    print("Selamat datang di program OWCA!")
    user_data = operateCSV.baca_csv(os.path.join(namafolder,"user_csv"))
    monster_data = operateCSV.baca_csv(os.path.join(namafolder,"monster.csv"))
    item_inventory_data = operateCSV.baca_csv(os.path.join(namafolder,"item_inventory.csv"))
    item_shop_data = operateCSV.baca_csv(os.path.join(namafolder,"item_shop.csv"))
    monster_inventory_data = operateCSV.baca_csv(os.path.join(namafolder,"monster_inventory.csv"))
    monster_shop_data = operateCSV.baca_csv(os.path.join(namafolder,"monster_shop.csv"))
    
    time.sleep(2)
    return user_data, monster_data, item_inventory_data, item_shop_data, monster_inventory_data, monster_shop_data