import F15

def exit_program(username, coin, user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop):
    pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    if pilihan == 'y':
        F15.save(username, coin, user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop)
    elif pilihan == 'n':
        print("Keluar program tanpa menyimpan.")
    else:
        while pilihan not in ['y', 'n']:
            pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
            if pilihan == 'y':
                F15.save(username, coin, user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop)
            elif pilihan == 'n':
                print("Keluar program tanpa menyimpan.")
            else:
                continue

# Contoh penggunaan
# while True:
#     command = input(">>> ").upper()
#     if command == "EXIT":
#         exit_program(item_inventory, item_shop, monster_inventory, monster_shop, monster_data, user_data)
#         break
#     else:
#         print("Perintah tidak dikenali.")