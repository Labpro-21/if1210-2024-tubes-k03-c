import os
from operateCSV import tulis_csv

def save(username, coin, user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop): 
    folder_parent = ".\data"
    folder_name = input("Masukkan nama folder: ")
    folder_path = os.path.join(folder_parent, folder_name)

    if os.path.exists(folder_path):
        print(f"Folder {folder_path} sudah ada.")
    else :
        os.makedirs(folder_path)
        print(f"Membuat folder {folder_path}...")

    for user_entry in user_data[1:]:
        if user_entry[1] == username:
            user_entry[4] = str(coin)
            break


    tulis_csv(os.path.join(folder_parent, folder_name, "user.csv"), user_data)
    tulis_csv(os.path.join(folder_parent, folder_name, "monster.csv"), monster_data)
    tulis_csv(os.path.join(folder_parent, folder_name, "monster_shop.csv"), monster_shop)
    tulis_csv(os.path.join(folder_parent, folder_name, "monster_inventory.csv"), monster_inventory)
    tulis_csv(os.path.join(folder_parent, folder_name, "item_shop.csv"), item_shop)
    tulis_csv(os.path.join(folder_parent, folder_name, "item_inventory.csv"), item_inventory)