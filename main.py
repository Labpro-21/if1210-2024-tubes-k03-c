import sys
sys.path.append('src')

import B04, F01, F02, F03, F07, F08, F10, F11, F12, F13
import operateCSV, testloader

user_data, monster_data, item_inventory, item_shop, monster_inventory, monster_shop = F14.load()

# user_data = operateCSV.baca_csv(r"data\user.csv")
# monster_data = operateCSV.baca_csv(r'data\monster.csv')
# item_inventory = operateCSV.baca_csv(r'data\item_inventory.csv')
# item_shop = operateCSV.baca_csv(r'data\item_shop.csv')
# monster_inventory = operateCSV.baca_csv(r'data\monster_inventory.csv')
# monster_shop = operateCSV.baca_csv(r'data\monster_shop.csv')

(username, user_id, role, coin, win) = ('', '', '', 0, False)

berhenti = False
while not(berhenti):
  menu = input(">>> ").upper()
  if menu == 'REGISTER':
    (username, monster_id, role, coin) = (F01.register(username, user_data, monster_data), 'agent', 0)
  elif menu == 'LOGIN':
    (username, role, coin) = (F02.login(username, role, coin))
    print(username, role, coin)
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
    print(">>> SHOP")
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
        (username, role, coin) = (F08.battle(username, role, coin))
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "ARENA"):
    if username != '':
      if role == "agent":
        (username, role, coin) = (F08.battle(username, role, coin))
      elif role=='admin':
        print("Maaf, Anda bukan seorang agen! Anda tidak memiliki izin untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "MONSTER"):
    if username != '':
      if role == "admin":
        print(">>> MONSTER")
        (username, role, coin, monster_data) = (F13.monster_management(username, role, coin))
      elif role=='agent':
        print("Maaf, Anda bukan seorang admin! Anda tidak memiliki hak untuk menggunakan perintah ini.")
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "JACKPOT"):
    if username != '':
      if role == "agent":
        print(">>> JACKPOT")
        coin, monster_inventory = B04.jackpot(username, coin)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "SAVE"):
    F15.save(item_inventory, item_shop, monster_inventory, monster_shop, monster_data, user_data)

  elif (menu == "EXIT"):
    F16.exit_program()

  else:
    print("Perintah tidak dikenal.")

