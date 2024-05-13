import sys
sys.path.append('src')

import F00, operateCSV

def jackpot(username):
  user_data = operateCSV.baca_csv("user.csv")

  username_login = username

  # Mencari ID agent yang sedang login
  user_id = None
  user_oc = None
  for user_entry in user_data[1:]:
    if user_entry[1] == username_login:
      user_id = user_entry[0]
      user_oc = int(user_entry[4])
      break

  if user_id:
    monster_inventory = operateCSV.baca_csv("monster_inventory.csv")
    monster_data = operateCSV.baca_csv("monster.csv")
  
  print("""
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
  $$$$$$$$$$$$$  Apakah Anda siap untuk menguji keberuntungan? $$$$$$$$$$$$$
  $$$$$$$$$$$$$     Menangkan Mewtwo dengan 400 OC saja !!!  $$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  """)

  item_jackpot = ["Topi", "Pedang", "Koin", "Potion", "Monster"]
  print()
  print("==== DAFTAR ITEM ====")
  print("1. Topi: 50 OC")
  print("2. Pedang: 100 OC")
  print("3. Koin: 200 OC")
  print("4. Potion: 300 OC")
  print("5. Monster: 500 OC")
  print()
  print(">>> Mulai bermain (Y/N): ", end="")
  play_confirm = input().upper()

  if play_confirm == "Y":
    if 400 <= user_oc:
      user_oc -= 400
      all_item = []
      item1 = item_jackpot[F00.RNG(0,4)]
      item2 = item_jackpot[F00.RNG(0,4)]
      item3 = item_jackpot[F00.RNG(0,4)]

      all_item.append(item1)
      all_item.append(item2)
      all_item.append(item3)

      print("Anda Mendapatkan: ")
      print(f"""
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$     {item1}    |    {item2}    |    {item3}    $$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      """)

      if item1 == item2 and item1 == item3:
        monster_random_id = RNG(1, len(monster_data)-1)
        reward_monster = monster_data[monster_random_id][1]

        for monster_entry in monster_inventory[1:]:
          if int(monster_entry[0]) == int(user_id) and monster_entry[1] == id_monster:
            print(f"Monster {reward_monster} sudah ada dalam inventory-mu!")
            reward = 0
            for item in all_item:
              if item == "Topi":
                reward += 50
              elif item == "Pedang":
                reward += 100
              elif item == "Koin":
                reward += 200
              elif item == "Potion":
                reward += 300
              elif item == "Monster":
                reward += 500
            print(f"Hadiah akan diubah menjadi {reward} OC.")
          else:
            print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {reward_monster}.")
            print("Monster telah ditambahkan ke inventory Anda.")
            monster_inventory.append([user_id, id_monster, 1])

      else:
        reward = 0
        for item in all_item:
          if item == "Topi":
            reward += 50
          elif item == "Pedang":
            reward += 100
          elif item == "Koin":
            reward += 200
          elif item == "Potion":
            reward += 300
          elif item == "Monster":
            reward += 500
        print(f"{reward} OC telah ditambahkan ke akun Anda! ")
        
        for user_entry in user_data[1:]:
          if user_entry[1] == username_login:
            user_entry[4] = str(int(user_entry[4]) + reward)


      operateCSV.tulis_csv("user.csv", user_data)
      operateCSV.tulis_csv("monster_inventory.csv", monster_inventory)
    else:
      print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
      return

  else:
    print("Jackpot dibatalkan.")