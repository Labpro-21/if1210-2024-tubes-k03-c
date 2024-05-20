import os
import time

def save_data_to_csv(data, folder_name):
    # Membuat folder data jika belum ada
    data_folder_path = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)

    # Memeriksa apakah folder_name tidak kosong
    while True:
        if folder_name == "":
            print("Nama folder tidak boleh kosong!")
            folder_name = input("Masukkan nama folder: ")
        else:
            break

    # Membuat subfolder sesuai input pengguna
    save_path = os.path.join(data_folder_path, folder_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print("Saving...")
        time.sleep(2)
        print(f"Membuat folder baru: {folder_name}")
        time.sleep(1)
    else:
        if not os.listdir(save_path):
            print(f"Folder '{folder_name}' ditemukan tetapi kosong.")
            print("Menaruh file baru di dalam folder tersebut.")

    # Menyimpan data ke dalam file CSV
    for key, value in data.items():
        file_path = os.path.join(save_path, f"{key}.csv")
        with open(file_path, 'w') as file:
            # Menulis headers
            headers = ','.join(value[0].keys()) + '\n'
            file.write(headers)

            # Menulis data
            for row in value:
                line = ','.join(map(str, row.values())) + '\n'
                file.write(line)
        
        print(f"Data dari variabel '{key}' berhasil disimpan dalam file '{key}.csv' di subfolder '{folder_name}'")

# Contoh 6 variabel dengan data
# Menyimpan data ke dalam folder data sesuai input pengguna

def save(a,b,c,d,e,f):
    folder_name = input("Masukkan nama folder: ")
    data = {'item_inventory': a, 'item_shop': b, 'monster_inventory': c, 'monster_shop': d, 'monster': e, 'user': f}
    save_data_to_csv(data, folder_name)

# Contoh penggunaan
# save(var_1, var_2, var_3, var_4, var_5, var_6)