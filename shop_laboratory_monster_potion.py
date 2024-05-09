def custom_split(text, delimiter):
  result = []
  start = 0
  for i in range(len(text)):  # Iterate through character indices
    char = text[i]
    if char == delimiter:
      result.append(text[start:i])
      start = i + 1
  # Add the last substring after the last delimiter
  result.append(text[start:])
  return result


def tulis_csv(filename, data):
  with open(filename, 'w', newline='') as file:
    for row in data:
      csv_row = ""
      # iterasi/loop tiap elemen tiap baris
      for index, element in enumerate(row):
                csv_row += str(element)
                if index < len(row) - 1:
                    csv_row += ';'
      # tambah newline
      csv_row += '\n'
      file.write(csv_row)


def baca_csv(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # hapus newline character
            if line[len(line)-1] == '\n':
                line = line[:len(line)-1]
            # split dengan ;
            row = custom_split(line, ";")
            data.append(row)
    return data


def maks(daftar):
    if not daftar:  # Jika daftar kosong, kembalikan None
        return None
    max_val = daftar[0]  # Anggap elemen pertama sebagai nilai maksimum awal
    for item in daftar[1:]:  # Mulai dari indeks kedua karena kita sudah menganggap indeks pertama sebagai nilai maksimum awal
        if item > max_val:
            max_val = item
    return max_val


def ambil_id_terbawah(monster_data):
  ids = [int(monster[0]) for monster in monster_data[1:]]  # Ambil semua ID kecuali header
  if not ids:  # Jika tidak ada ID, gunakan 1 sebagai ID awal
    return 1
  else:
    return maks(ids) + 1  # ID baru adalah nilai maksimum ditambah 1


# Agent and Admin
def lihat_shop_monster():
  monster_data = baca_csv("monster.csv")
  monster_shop_data = baca_csv("monster_shop.csv")
    
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
  item_shop_data = baca_csv("item_shop.csv")
        
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


# Agent
def beli_shop():
  user_data = baca_csv("user.csv")

  username_login = "Agen_P"

  # Mencari ID agent yang sedang login
  user_id = None
  user_oc = None
  for user_entry in user_data[1:]:
    if user_entry[1] == username_login:
      user_id = user_entry[0]
      user_oc = int(user_entry[4])
      break
  
  print("Jumlah O.W.C.A. Coin-mu sekarang ", user_oc, ".")
  beli = input(">>> Mau beli apa? (monster/potion): ")
  if (beli == "monster"):
    id_monster = input(">>> Masukkan id monster: ")
    
    
  else: # beli == potion


# Admin
def tambah():
  tambah = input(">>> Mau tambah apa? (monster/potion): ")
  if (tambah.lower() == "monster"):
    monster_data = baca_csv("monster.csv")
    monster_shop_data = baca_csv("monster_shop.csv")

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
    # Menulis kembali data ke dalam file "monster_shop.csv"
    tulis_csv("monster_shop.csv", monster_shop_data)
  
  elif (tambah.lower() == "potion"):
    potion_shop_data = baca_csv("item_shop.csv")

    potion_fixed = ["strength", "resilience", "healing"]
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
    tulis_csv("item_shop.csv", potion_shop_data)
  
  else:
    print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")


def ubah():
  ubah = input(">>> Mau ubah apa? (monster/potion): ")
  if (ubah.lower() == "monster"):
    monster_data = baca_csv("monster.csv")
    monster_shop_data = baca_csv("monster_shop.csv")
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
      tulis_csv("monster_shop.csv", monster_shop_data)

    elif stok_baru:
      monster_shop_data[index][1] = stok_baru
      print(monster_name, "telah berhasil diubah dengan stok baru sejumlah", stok_baru, "!")
      tulis_csv("monster_shop.csv", monster_shop_data)

    elif harga_baru:
      monster_shop_data[index][2] = harga_baru
      print(monster_name, "telah berhasil diubah dengan harga baru", harga_baru, "!")
      tulis_csv("monster_shop.csv", monster_shop_data)
    
  elif (ubah.lower() == "potion"):
    potion_shop_data = baca_csv("item_shop.csv")
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
      tulis_csv("item_shop.csv", potion_shop_data)

    elif stok_baru:
      potion_shop_data[index][1] = stok_baru
      print(potion_shop_data[index][0], "telah berhasil diubah dengan stok baru sejumlah", stok_baru, "!")
      tulis_csv("item_shop.csv", potion_shop_data)

    elif harga_baru:
      potion_shop_data[index][2] = harga_baru
      print(potion_shop_data[index][0], "telah berhasil diubah dengan harga baru", harga_baru, "!")
      tulis_csv("item_shop.csv", potion_shop_data)
  
  else:
    print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")


def hapus():
  hapus = input(">>> Mau hapus apa? (monster/potion): ")
  if (hapus.lower() == "monster"):
    monster_data = baca_csv("monster.csv")
    monster_shop_data = baca_csv("monster_shop.csv")
    lihat_shop_monster()
    id_monster = input(">>> Masukkan id monster: ")
    index = -1
    for i, item in enumerate(monster_shop_data[1:], start=1):  # Skip header row
      if item[0] == id_monster:
        index = i
        break
    if index == -1:
      print("Monster dengan ID tersebut tidak ditemukan.")
      return

    monster_id = monster_shop_data[index][0]
    monster_name = ""
    for monster in monster_data[1:]:  # Skip header row
      if monster[0] == monster_id:
        monster_name = monster[1]
        break

    print("Apakah Anda yakin ingin menghapus", monster_name,"dari shop (y/n)? ", end="")
    hapus_confirm = input()
    if (hapus_confirm.lower() == 'y'):
      print(monster_name,"telah berhasil dihapus dari shop!")
      monster_shop_data = monster_shop_data[:index] + monster_shop_data[index+1:]
      tulis_csv("monster_shop.csv", monster_shop_data)
    else: # hapus_confirm == n
      print("Penghapusan dibatalkan.") 

  elif (hapus == "potion"):
    potion_shop_data = baca_csv("item_shop.csv")
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
      tulis_csv("item_shop.csv", potion_shop_data)
    else:
      print("Penghapusan dibatalkan.")    

  else:
    print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")


def lihat_monster():
  monster_data = baca_csv("monster.csv")

  print("ID | Type         | ATK Power | DEF Power | HP   |")
  for monster in monster_data[1:]:  # Skip header row
      print(f"{monster[0]:<2} | {monster[1]:<12} | {monster[2]:<9} | {monster[3]:<9} | {monster[4]:<4} | ")


def tambah_monster():
  monster_data = baca_csv("monster.csv")
  print("Memulai pembuatan monster baru")
  while True:
    monster_name = input(">>> Masukkan Type / Nama : ")
    nama_terdaftar = False
    for monster in monster_data[1:]:
      if monster[1] == monster_name:
        print("Nama sudah terdaftar, coba lagi!")
        nama_terdaftar = True
        break
    if not nama_terdaftar:
      break

  while True:
    atk_power = input(">>> Masukkan ATK Power : ")
    if atk_power.isdigit():
      atk_power = int(atk_power)
      break
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
  
  while True:
    def_power = input(">>> Masukkan DEF Power (0-50) : ")
    if def_power.isdigit():
      def_power = int(def_power)
      if 0 <= def_power <= 50:
        break
      else:
        print("DEF Power harus bernilai 0-50, coba lagi!")
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
    
  while True:
    hp = input(">>> Masukkan HP : ")
    if hp.isdigit():
      hp = int(hp)
      break
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
  
  print("Monster baru berhasil dibuat!")
  print("Type : ", monster_name)
  print("ATK Power : ", atk_power)
  print("DEF Power : ", def_power)
  print("HP : ", hp)

  monster_id_baru = ambil_id_terbawah(monster_data)

  print(">>> Tambahkan Monster ke database (Y/N) : ", end="")
  hapus_confirm = input()
  if (hapus_confirm.lower() == 'y'):
    print("Monster baru telah ditambahkan")
    monster_data.append([monster_id_baru,monster_name, atk_power, def_power, hp])
    # Menulis kembali data ke dalam file "monster.csv"
    tulis_csv("monster.csv", monster_data)
  else: # hapus_confirm == n
    print("Monster gagal ditambahkan!") 


def shop_currency(monster_shop, item_shop, coin):
  print("Irasshaimase! Selamat datang di SHOP!!")
  aksi = input(">>> Pilih aksi (lihat/beli/keluar): ")
  if (aksi == "lihat"):
    lihat = input(">>> Mau lihat apa? (monster/potion): ")
    if (lihat == "monster"):
      lihat_shop_monster()
    elif (lihat == "potion"): # lihat potion
      lihat_shop_potion()
    else: print("Input tidak valid. Silakan masukkan 'monster' atau 'potion'.")
  elif (aksi == "beli"):
    beli_shop()


def laboratory():
  user_data = baca_csv("user.csv")

  username_login = "Agen_P"

  # Mencari ID agent yang sedang login
  user_id = None
  user_oc = None
  for user_entry in user_data[1:]:
    if user_entry[1] == username_login:
      user_id = user_entry[0]
      user_oc = int(user_entry[4])
      break

  if user_id:
    monster_inventory = baca_csv("monster_inventory.csv")
    monster_data = baca_csv("monster.csv")

    print(">>> LABORATORY")
    print()
    print("Selamat datang di Lab Dokter Asep !!!")
    print()
    print("============ MONSTER LIST ============")

    i = 1
    found = False
    monster_invent_id = []
    for monster_entry in monster_inventory[1:]:
      if int(monster_entry[0]) == int(user_id):
        found = True
        if found:
          monster_id = monster_entry[1]
          monster_level = monster_entry[2]
          monster_name = ""

          for monster in monster_data[1:]:
            if monster[0] == monster_id:
              monster_name = monster[1]
              break
          
          monster_invent_id.append(monster_id)

          print(f"{i}. {monster_name} (ID: {monster_id}) (Level: {monster_level})")
        i += 1
        found = False
    
    print()
    print("============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 300 OC")
    print("2. Level 2 -> Level 3: 500 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
    print()
    upgrade_monster_no = input(">>> Pilih monster: ")

    if upgrade_monster_no.isdigit():  # Input validation
      upgrade_monster_no = int(upgrade_monster_no)
      if upgrade_monster_no in range(1, len(monster_invent_id) + 1):
        upgrade_monster_no = monster_invent_id[upgrade_monster_no - 1]

        for monster_entry in monster_inventory[1:]:
          if int(monster_entry[0]) == int(user_id) and      upgrade_monster_no == monster_entry[1]:
            monster_level = int(monster_entry[2])
            monster_name = ""
            for monster in monster_data[1:]:
              if monster[0] == upgrade_monster_no:
                monster_name = monster[1]
                break

            if monster_level == 5:
              print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
            else:
              upgrade_price = {1: 300, 2: 500, 3: 800, 4: 1000}
              next_level = monster_level + 1
              print(f"{monster_name} akan di-upgrade ke level {next_level}")
              print(f"Harga untuk melakukan upgrade {monster_name} adalah {upgrade_price[monster_level]} OC")
              print(">>> Lanjutkan upgrade (Y/N): ", end="")
              upgrade_confirm = input().upper()

              if upgrade_confirm == "Y":
              # Check if user has sufficient OC for the upgrade
                if upgrade_price[monster_level] <= user_oc:
                  user_oc -= upgrade_price[monster_level]
                  monster_level += 1
                  print(f"Selamat, {monster_name} berhasil di-upgrade ke level {monster_level}!")

                  for user_entry in user_data[1:]:
                    if user_entry[0] == user_id:
                      user_entry[4] = str(user_oc)  
                      break

                  for monster_entry in monster_inventory[1:]:
                    if int(monster_entry[0]) == int(user_id) and int(monster_entry[1]) == int(upgrade_monster_no):
                      monster_entry[2] = str(monster_level)  
                      break
                  """
                  print(monster_inventory)
                  [['user_id', 'monster_id', 'level'], ['2', '1', '1'], ['3', '2', '3'], ['3', '3', '1'], ['4', '4', '1'], ['5', '5', '5']]
                  """
                  tulis_csv("user.csv", user_data)
                  tulis_csv("monster_inventory.csv", monster_inventory)

                else:
                  print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
              else:
                print("Upgrade dibatalkan.")
            break
        else:
          print("ID monster tidak valid.")
    else:
      print("Input harus berupa angka.")


def shop_management():
  print("Irasshaimase! Selamat datang kembali, Mr. Yanto!")
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
      tambah()
    elif (aksi == "ubah"):
      ubah()
    elif (aksi == "hapus"):
      hapus()
    elif (aksi == "keluar"):
      print("Dadah Mr. Yanto, sampai jumpa lagi!")
      keluar = True
    else: # input diluar yang diminta
      print("Aksi tidak valid. Silakan pilih aksi lainnya.")


def monster_management():
  print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
  print("1. Tampilkan semua Monster")
  print("2. Tambah Monster baru")
  print("3. Keluar")
  keluar = False
  while not keluar:
    aksi = input(">>> Pilih Aksi : ")
    if (aksi == "1"):
      lihat_monster()
    elif (aksi == "2"):
      tambah_monster()
    elif (aksi == "3"):
      print("Dadah, sampai jumpa lagi!")
      keluar = True
    else:
      print("Aksi tidak valid. Silakan pilih aksi lainnya.")

menu = input("")
if (menu == "SHOP"):
  print(">>> SHOP")
  print()
  shop()

elif (menu == "LABORATORY"):
  laboratory()

elif (menu == "MONSTER"):
  print(">>> MONSTER")
  monster_management()