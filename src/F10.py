import sys
sys.path.append('src')

import operateCSV

def lihat_shop_monster():
  monster_data = operateCSV.baca_csv(r"data\monster.csv")
  monster_shop_data = operateCSV.baca_csv(r"data\monster_shop.csv")
    
  monster_info = {}
  for monster in monster_data[1:]:
    monster_info[monster[0]] = monster[1:]

  """
  print(monster_info)
  {'1': ['Pikachow', '125', '10', '600'], '2': ['Bulbu', '50', '50', '1200'], '3': ['Zeze', '300', '10', '100'], '4': ['Zuko', '100', '25', '800'], '5': ['Chacha', '80', '30', '700'], '6': ['Bulbasaur', '90', '20', '700']}
  """

  print("ID | Type         | ATK Power | DEF Power | HP   | Stok | Harga |")
  for item in monster_shop_data[1:]: 
    monster_id = item[0]
    stock = item[1]
    price = item[2]

    if monster_id in monster_info:
      monster_details = monster_info[monster_id]
      print(f"{monster_id:<2} | {monster_details[0]:<12} | {monster_details[1]:<9} | {monster_details[2]:<9} | {monster_details[3]:<4} | {stock:<4} | {price:<5} | ")


def lihat_shop_potion():
  item_shop_data = operateCSV.baca_csv(r"data\item_shop.csv")
        
  item_info = {}
  for i, item in enumerate(item_shop_data[1:], start=1): 
    item_info[str(i)] = item 

  print("ID | Type                | Stok | Harga |")
  for i, item in enumerate(item_shop_data[1:], start=1):
    stock = item[1]
    price = item[2]

    item_details = item_info[str(i)]
    print(f"{i:<2} | {item_details[0]:<19} | {stock:<4} | {price:<5} |")


# Agent
def beli_shop(beli, username, coin):
  user_data = operateCSV.baca_csv(r"data\user.csv")

  username_login = username

  # Mencari ID agent yang sedang login
  user_id = None
  user_oc = None
  for user_entry in user_data[1:]:
    if user_entry[1] == username_login:
      user_id = user_entry[0]
      user_oc = int(user_entry[4])
      break

  print("Jumlah O.W.C.A. Coin-mu sekarang ", coin, ".")
  if (beli == "monster"):
    monster_inventory = operateCSV.baca_csv(r"data\monster_inventory.csv")
    monster_data = operateCSV.baca_csv(r"data\monster.csv")
    monster_shop_data = operateCSV.baca_csv(r"data\monster_shop.csv")
    id_monster = input(">>> Masukkan id monster: ")
    for i, item in enumerate(monster_shop_data[1:], start=1): 
      if item[0] == id_monster:
        index = i
        break
    if index == -1:
      print("Monster dengan ID tersebut tidak ditemukan.")
      return
    
    if int(monster_shop_data[index][2]) > user_oc:
      print("OC-mu tidak cukup.")
      return

    if (int(monster_shop_data[index][1]) > 0):
      monster_name = ""
      for monster in monster_data[1:]:
        if monster[0] == id_monster:
          monster_name = monster[1]
          break

      for monster_entry in monster_inventory[1:]:
        if int(monster_entry[0]) == int(user_id) and monster_entry[1] == id_monster:
          print(f"Monster {monster_name} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
          return

      print(f"Berhasil membeli item: {monster_name}. Item sudah masuk ke inventory-mu!")
      monster_inventory.append([user_id, id_monster, 1])
      monster_shop_data[index][1] = str(int(monster_shop_data[index][1]) - 1)

      for user_entry in user_data[1:]:
        if user_entry[1] == username_login:
          user_entry[4] = str(int(user_entry[4]) - int(monster_shop_data[index][1]))

      coin -= int(monster_shop_data[index][1])

      return user_data, monster_inventory, monster_shop_data, coin
      # operateCSV.tulis_csv(r"data\monster_inventory.csv", monster_inventory)
      # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)
      # operateCSV.tulis_csv(r"data\user.csv", user_data)

    else:
      print("Stok habis.")

  elif (beli == "potion"):
    item_shop = operateCSV.baca_csv(r"data\item_shop.csv")
    item_inventory = operateCSV.baca_csv(r"data\item_inventory.csv")

    id_potion = input(">>> Masukkan id potion: ")
    jumlah = int(input(">>> Masukkan jumlah: "))
    potion_fixed = ["strength", "resilience", "healing"]
    
    for i, item in enumerate(item_shop[1:], start=1):
      if item[0] == potion_fixed[int(id_potion)-1]:
        index = i
        break
    else:
      print("Potion dengan ID tersebut tidak ditemukan.")
      return

    total = jumlah*int(item_shop[index][2])
    if int(total) > user_oc:
      print("OC-mu tidak cukup.")
      return
    
    if int(item_shop[index][1]) >= jumlah:
      print(f"Berhasil membeli item: {jumlah} Potion of {potion_fixed[index-1]}. Item sudah masuk ke inventory-mu!")

      found = False
      for item_entry in item_inventory[1:]:
        if item_entry[0] == user_id and item_entry[1] == potion_fixed[int(id_potion)-1]:
          item_entry[2] = str(int(item_entry[2]) + jumlah)
          found = True
          break
      
      if not found:
        item_inventory.append([user_id, potion_fixed[int(id_potion)-1], str(jumlah)])

      item_shop[index][1] = str(int(item_shop[index][1]) - jumlah)


      for user_entry in user_data[1:]:
        if user_entry[1] == username_login:
          user_entry[4] = str(int(user_entry[4]) - total)

      coin -= total

      return  user_data, item_inventory, item_shop, coin
      # operateCSV.tulis_csv(r"data\item_inventory.csv", item_inventory)
      # operateCSV.tulis_csv(r"data\item_shop.csv", item_shop)
      # operateCSV.tulis_csv(r"data\user.csv", user_data)


def shop_currency(username, role, coin):
  print("Irasshaimase! Selamat datang di SHOP!!")
  keluar = False
  while not keluar:
    aksi = input(">>> Pilih aksi (lihat/beli/keluar): ")
    if (aksi == "lihat"):
      lihat = input(">>> Mau lihat apa? (monster/potion): ")
      if (lihat == "monster"):
        lihat_shop_monster()
      elif (lihat == "potion"):
        lihat_shop_potion()
      else: print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "beli"):
      beli = input(">>> Mau beli apa? (monster/potion): ")
      if beli.lower() == "monster":
        user_data, monster_inventory, monster_shop, coin = beli_shop(beli, username, coin)
      elif beli.lower() == "potion":
        user_data, item_inventory, item_shop, coin = beli_shop(beli, username, coin)
      else:
        print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "keluar"):
      print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
      keluar = True
    else:
      print("Aksi tidak valid. Silakan pilih aksi lainnya.")
    
  return username, role, coin