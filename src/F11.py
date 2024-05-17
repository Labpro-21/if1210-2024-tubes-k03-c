import sys
sys.path.append('src')

import operateCSV

def laboratory(username, role, coin):
  user_data = operateCSV.baca_csv(r"data\user.csv")

  username_login = username

  # Mencari ID agent yang sedang login
  user_id = None
  # user_oc = None
  for user_entry in user_data[1:]:
    if user_entry[1] == username_login:
      user_id = user_entry[0]
      # user_oc = int(user_entry[4])
      break

  if user_id:
    monster_inventory = operateCSV.baca_csv(r"data\monster_inventory.csv")
    monster_data = operateCSV.baca_csv(r"data\monster.csv")

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
                if upgrade_price[monster_level] <= coin:
                  # user_oc -= upgrade_price[monster_level]
                  coin -= upgrade_price[monster_level]
                  monster_level += 1
                  print(f"Selamat, {monster_name} berhasil di-upgrade ke level {monster_level}!")

                  # for user_entry in user_data[1:]:
                  #   if user_entry[0] == user_id:
                  #     user_entry[4] = str(user_oc)  
                  #     break

                  for monster_entry in monster_inventory[1:]:
                    if int(monster_entry[0]) == int(user_id) and int(monster_entry[1]) == int(upgrade_monster_no):
                      monster_entry[2] = str(monster_level)  
                      break
                  """
                  print(monster_inventory)
                  [['user_id', 'monster_id', 'level'], ['2', '1', '1'], ['3', '2', '3'], ['3', '3', '1'], ['4', '4', '1'], ['5', '5', '5']]
                  """

                  # operateCSV.tulis_csv(r"data\user.csv", user_data)
                  # operateCSV.tulis_csv(r"data\monster_inventory.csv", monster_inventory)

                else:
                  print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
              else:
                print("Upgrade dibatalkan.")
            break
    else:
      print("ID monster tidak valid.")
  return username, role, coin, user_data, monster_inventory