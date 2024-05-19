import sys
sys.path.append('src')

import B04, F01, F02, F03, F04, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16
import operateCSV, testloader

user_data, monster_data, item_inventory, item_shop, monster_inventory, monster_shop = F14.load()

# user_data = operateCSV.baca_csv(r"data\user.csv")
# monster_data = operateCSV.baca_csv(r'data\monster.csv')
# item_inventory = operateCSV.baca_csv(r'data\item_inventory.csv')
# item_shop = operateCSV.baca_csv(r'data\item_shop.csv')
# monster_inventory = operateCSV.baca_csv(r'data\monster_inventory.csv')
# monster_shop = operateCSV.baca_csv(r'data\monster_shop.csv')

#dependencies array for loading datas
user_monster=[['monster_id','monster_level']]
#mobile inventories
player_monster_arr=[['type','atk','def','hp','lv']]
player_inv_arr=[['type','quantity']]
#potion state
potion_check=[False,False,False]
#mobile inventory load state
loaded=False

(username, user_id, role, coin, win) = ('', '', '', 0, False)

berhenti = False
while not(berhenti):
  menu = input(">>> ").upper()
  if menu == 'REGISTER':
    (username, monster_id, role, coin) = (F01.register(username, user_data, monster_data), 'agent', 0)
  elif menu == 'LOGIN':
    (username, role, coin) = (F02.login(username, role, coin))
  elif menu == 'LOGOUT':
    (username, role, coin) = (F03.logout(username, role, coin))
  elif menu == "HELP":
    if username != '':
      F04.help(username,role)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu.\n")
  elif menu == "INVENTORY":
    if username != '':
      if role == "agent":
        F07.finventory()
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "SHOP"):
    print()
    if username != '':
      if role == "admin":
        (username, role, coin, monster_shop, item_shop) = (F12.shop_management(username, role, coin))
      elif role =='agent':
        (username, role, coin, user_data, monster_inventory, monster_shop, item_inventory, item_shop) = (F10.shop_currency(username, role, coin))
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "LABORATORY"):
    if username != '':
      if role == "agent":
        (username, role, coin, user_data, monster_inventory) = (F11.laboratory(username, role, coin))
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "BATTLE"):
    if username != '':
      if role == "agent":
        #find uid
        userid=testloader.get_uid(user_data,username)
        if not loaded: 
          #load datas to mobile inventory
          # print(player_inv_arr)
          player_monster_arr=(testloader.monster_inventory(monster_data,testloader.filter_monster(monster_inventory,userid,user_monster),player_monster_arr))
          # print(monster_inventory)
          # print(monster_data)
          player_inv_arr=(testloader.filter_item(item_inventory,userid,player_inv_arr))
          loaded=True
          # print(player_inv_arr)
        (username, role, coin) = (F08.battle(username, role, coin, menu, 0, monster_data, player_monster_arr, player_inv_arr, potion_check))
        #reset potion states
        potion_check=[False,False,False]
        #change item in item_inventory from mobile inventory 
        F08.ubah_potion(item_inventory,userid,player_inv_arr)
        # print(item_inventory)
        #unload
        user_monster=[['monster_id','monster_level']]
        player_monster_arr=[['type','atk','def','hp','lv']]
        player_inv_arr=[['type','quantity']]
        loaded=False
        # print(player_inv_arr)
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "ARENA"):
    if username != '':
      if role == "agent":
        #find uid
        userid=testloader.get_uid(user_data,username)
        stage=1
        alive=True
        total_taken=0
        total_dealt=0
        total_oc=0
        while (not stage>5) and alive:
          if not loaded: 
            #load datas to mobile inventory
            player_monster_arr=(testloader.monster_inventory(monster_data,testloader.filter_monster(monster_inventory,userid,user_monster),player_monster_arr))
            player_inv_arr=(testloader.filter_item(item_inventory,userid,player_inv_arr))
            loaded=True
          (username,role,coin,damage_taken,damage_dealt,win,gained) = (F09.arena(username, role, coin, menu, monster_data, player_monster_arr, player_inv_arr, potion_check, stage))
          #reset potion states
          potion_check=[False,False,False]
          #change item in item_inventory from mobile inventory 
          F08.ubah_potion(item_inventory,userid,player_inv_arr)
          #unload
          user_monster=[['monster_id','monster_level']]
          player_monster_arr=[['type','atk','def','hp','lv']]
          player_inv_arr=[['type','quantity']]
          loaded=False
          if win:
            stage+=1
            if stage>5:
              print('Selamat, kamu berhasil menamatkan sesi Arena!!!')
            else: #stage<=5 and stage>0
              print(f'Lanjut ke stage {stage}.\n')
            total_taken+=damage_taken
            total_dealt+=damage_dealt
            total_oc+=gained
          else:
            alive=False
            total_taken+=damage_taken
            total_dealt+=damage_dealt
            total_oc+=gained
        print(f"""============== STATS ==============
    Total hadiah      : {total_oc} OC
    Jumlah stage      : {stage-1}
    Damage diberikan  : {total_dealt}
    Damage diterima   : {total_taken}
    """)
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "MONSTER"):
    if username != '':
      if role == "admin":
        (username, role, coin, monster_data) = (F13.monster_management(username, role, coin))
      elif role=='agent':
        print("Maaf, Anda bukan seorang admin! Anda tidak memiliki hak untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "JACKPOT"):
    if username != '':
      if role == "agent":
        coin, monster_inventory = B04.jackpot(username, coin)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "SAVE"):
    F15.save(user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop)

  elif (menu == "EXIT"):
    F16.exit_program(user_data, monster_data, monster_inventory, monster_shop, item_inventory, item_shop)

  else:
    print("Perintah tidak dikenal.")

