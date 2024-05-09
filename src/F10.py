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
