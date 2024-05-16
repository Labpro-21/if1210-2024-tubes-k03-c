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
  for item in monster_shop_data[1:]:  # Skip header row
    monster_id = item[0]
    stock = item[1]
    price = item[2]
    # Fetching monster info using monster ID from monster_info dictionary
    if monster_id in monster_info:
      monster_details = monster_info[monster_id]
      print(f"{monster_id:<2} | {monster_details[0]:<12} | {monster_details[1]:<9} | {monster_details[2]:<9} | {monster_details[3]:<4} | {stock:<4} | {price:<5} | ")


def lihat_shop_potion():
  item_shop_data = operateCSV.baca_csv(r"data\item_shop.csv")
        
  item_info = {}
  for i, item in enumerate(item_shop_data[1:], start=1):  # Skip header row
    item_info[str(i)] = item  # ID berurutan naik dari 1

  print("ID | Type                | Stok | Harga |")
  for i, item in enumerate(item_shop_data[1:], start=1):  # Skip header row
    stock = item[1]
    price = item[2]
    # Fetching item info using item ID from item_info dictionary
    item_details = item_info[str(i)]
    print(f"{i:<2} | {item_details[0]:<19} | {stock:<4} | {price:<5} |")


def tambah(tambah):
  if (tambah.lower() == "monster"):
    monster_data = operateCSV.baca_csv(r"data\monster.csv")
    monster_shop_data = operateCSV.baca_csv(r"data\monster_shop.csv")

    id_monster_shop = []
    for monster_shop in monster_shop_data[1:]:
      id_monster_shop.append(monster_shop[0])

    """
    print(id_monster_shop)
    ['1', '2', '3', '5']
    """

    print("ID | Type         | ATK Power | DEF Power | HP   |")
    for monster in monster_data[1:]:
      if monster[0] not in id_monster_shop:
        print(f"{monster[0]:<2} | {monster[1]:<11}  | {monster[2]:<9} | {monster[3]:<9} | {monster[4]:<4} |")
        

    monster_id = input(">>> Masukkan id monster: ")
    monster_index = None
    for index, monster in enumerate(monster_data):
      if monster[0] == monster_id:
        monster_index = index
        break

    # Mengecek apakah indeks ditemukan
    if monster_index is None:
      print("ID monster tidak valid.")
      return

    if monster_id in id_monster_shop: # mengecek apakah monster_id ada dalam daftar monster yang belum ada di toko
      print("Monster sudah ada di toko.")
      return
    
    stock = input(">>> Masukkan stok awal: ")
    price = input(">>> Masukkan harga: ")
    
    print(monster_data[monster_index][1], "berhasil ditambahkan ke dalam shop!")
    monster_shop_data.append([monster_id, stock, price])

    return monster_shop_data
    # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)
  
  elif (tambah.lower() == "potion"):
    potion_shop_data = operateCSV.baca_csv(r"data\item_shop.csv")

    potion_fixed = ["Strength", "Resilience", "Healing"]
    print("ID | Type         |")
    for potion_index in range(len(potion_fixed)):
      potion_type = potion_fixed[potion_index]  # Dapatkan jenis potion berdasarkan indeks
      if potion_type not in [potion[0] for potion in potion_shop_data[1:]]:
        print(f"{potion_index+1:<2} | {potion_type:<11}  |") 
    
    potion_id = input(">>> Masukkan id potion: ")
    if potion_id in [potion[0] for potion in potion_shop_data]: 
      print("Potion sudah ada di toko.")
    else:
      stock = input(">>> Masukkan stok awal: ")
      price = input(">>> Masukkan harga: ")
    
    # Menambahkan data baru ke dalam list potion_shop_data
    potion_shop_data.append([potion_fixed[int(potion_id)-1], stock, price])
    # Menulis kembali data ke dalam file "potion_shop.csv"
    return potion_shop_data
    # operateCSV.tulis_csv(r"data\item_shop.csv", potion_shop_data)

def ubah(ubah):
  if (ubah.lower() == "monster"):
    monster_data = operateCSV.baca_csv(r"data\monster.csv")
    monster_shop_data = operateCSV.baca_csv(r"data\monster_shop.csv")
    lihat_shop_monster()
    id_monster = input("Masukkan id monster: ")
    index = -1
    for i, item in enumerate(monster_shop_data[1:], start=1):  # Skip header row
      if item[0] == id_monster:
        index = i
        break
    if index == -1:
      print("Monster dengan ID tersebut tidak ditemukan.")
      return
    stok_baru = input("Masukkan stok baru: ")
    harga_baru = input("Masukkan harga baru: ")

    monster_id = monster_shop_data[index][0]
    monster_name = ""
    for monster in monster_data[1:]:  # Skip header row
      if monster[0] == monster_id:
        monster_name = monster[1]
        break

    if stok_baru and harga_baru:
      monster_shop_data[index][1] = stok_baru
      monster_shop_data[index][2] = harga_baru
      print(monster_name, "telah berhasil diubah dengan stok baru sejumlah", stok_baru, " dan dengan harga baru", harga_baru, "!")
      return monster_shop_data
      # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)

    elif stok_baru:
      monster_shop_data[index][1] = stok_baru
      print(monster_name, "telah berhasil diubah dengan stok baru sejumlah", stok_baru, "!")
      return monster_shop_data
      # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)

    elif harga_baru:
      monster_shop_data[index][2] = harga_baru
      print(monster_name, "telah berhasil diubah dengan harga baru", harga_baru, "!")
      return monster_shop_data
      # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)
    
  elif (ubah.lower() == "potion"):
    potion_shop_data = operateCSV.baca_csv(r"data\item_shop.csv")
    lihat_shop_potion()
    id_potion = input("Masukkan id potion: ")
    index = int(id_potion)  # Karena ID berdasarkan urutan dari atas ke bawah
    if index < 1 or index >= len(potion_shop_data):
        print("Potion dengan ID tersebut tidak ditemukan.")
        return
    stok_baru = input("Masukkan stok baru: ")
    harga_baru = input("Masukkan harga baru: ")
    
    if stok_baru and harga_baru:
      potion_shop_data[index][1] = stok_baru
      potion_shop_data[index][2] = harga_baru
      print(potion_shop_data[index][0], "telah berhasil diubah dengan stok baru sejumlah", stok_baru, " dan dengan harga baru", harga_baru, "!")
      return potion_shop_data
      # operateCSV.tulis_csv(r"data\item_shop.csv", potion_shop_data)

    elif stok_baru:
      potion_shop_data[index][1] = stok_baru
      print(potion_shop_data[index][0], "telah berhasil diubah dengan stok baru sejumlah", stok_baru, "!")
      return potion_shop_data
      # operateCSV.tulis_csv(r"data\item_shop.csv", potion_shop_data)

    elif harga_baru:
      potion_shop_data[index][2] = harga_baru
      print(potion_shop_data[index][0], "telah berhasil diubah dengan harga baru", harga_baru, "!")
      return potion_shop_data
      # operateCSV.tulis_csv(r"data\item_shop.csv", potion_shop_data)

def hapus(hapus):
  if (hapus.lower() == "monster"):
    monster_data = operateCSV.baca_csv(r"data\monster.csv")
    monster_shop_data = operateCSV.baca_csv(r"data\monster_shop.csv")
    lihat_shop_monster()
    id_monster = input(">>> Masukkan id monster: ")
    index = -1
    for i, item in enumerate(monster_shop_data[1:], start=1): 
      if item[0] == id_monster:
        index = i
        break
    if index == -1:
      print("Monster dengan ID tersebut tidak ditemukan.")
      return

    monster_id = monster_shop_data[index][0]
    monster_name = ""
    for monster in monster_data[1:]: 
      if monster[0] == monster_id:
        monster_name = monster[1]
        break

    print("Apakah Anda yakin ingin menghapus", monster_name,"dari shop (y/n)? ", end="")
    hapus_confirm = input()
    if (hapus_confirm.lower() == 'y'):
      print(monster_name,"telah berhasil dihapus dari shop!")
      monster_shop_data = monster_shop_data[:index] + monster_shop_data[index+1:]
      return monster_shop_data
      # operateCSV.tulis_csv(r"data\monster_shop.csv", monster_shop_data)
    else: # hapus_confirm == n
      print("Penghapusan dibatalkan.") 

  elif (hapus == "potion"):
    potion_shop_data = operateCSV.baca_csv(r"data\item_shop.csv")
    lihat_shop_potion()
    id_potion = input("Masukkan id potion: ")
    index = int(id_potion)
    if index < 1 or index >= len(potion_shop_data):
      print("Potion dengan ID tersebut tidak ditemukan.")
      return
    print("Apakah Anda yakin ingin menghapus", potion_shop_data[index][0],"dari shop (y/n)? ", end="")
    hapus_confirm = input()
    if (hapus_confirm.lower() == 'y'):
      print(potion_shop_data[index][0], "telah berhasil dihapus dari shop!")
      potion_shop_data = potion_shop_data[:index] + potion_shop_data[index+1:]
      return potion_shop_data
      # operateCSV.tulis_csv(r"data\item_shop.csv", potion_shop_data)
    else:
      print("Penghapusan dibatalkan.")    

  else:
    print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")


def shop_management(username, role, coin):
  print(f"Irasshaimase! Selamat datang kembali, {username}!")
  keluar = False
  while not keluar:
    aksi = input("\n>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
    if (aksi == "lihat"):
      lihat = input(">>> Mau lihat apa? (monster/potion): ")
      if (lihat == "monster"):
        lihat_shop_monster()
      elif (lihat == "potion"): # lihat potion
        lihat_shop_potion()
      else: print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "tambah"):
      tambah_input = input(">>> Mau tambah apa? (monster/potion): ")
      if tambah_input.lower() == "monster":
        monster_shop = tambah(tambah_input)
      elif tambah_input.lower() == "potion":
        item.shop = tambah(tambah_input)
      else:
        print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "ubah"):
      ubah_input = input(">>> Mau ubah apa? (monster/potion): ")
      if ubah_input.lower() == "monster":
        monster_shop = ubah(ubah_input)
      elif ubah_input.lower() == "potion":
        item.shop = ubah(ubah_input)
      else:
        print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "hapus"):
      hapus_input = input(">>> Mau hapus apa? (monster/potion): ")
      if hapus_input.lower() == "monster":
        monster_shop = hapus(hapus_input)
      elif hapus_input.lower() == "potion":
        item.shop = hapus(hapus_input)
      else:
        print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
    elif (aksi == "keluar"):
      print(f"Dadah {username}, sampai jumpa lagi!")
      keluar = True
    else: # input diluar yang diminta
      print("Aksi tidak valid. Silakan pilih aksi lainnya.")

  return username, role, coin, monster_shop, item_shop