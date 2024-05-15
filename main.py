import sys
sys.path.append('src')
import F01, F10, F11, F12, F13
import operateCSV

user_data = operateCSV.baca_csv(r"data\user.csv")
monster_data = operateCSV.baca_csv(r'data\monster.csv')
item_inventory = operateCSV.baca_csv(r'data\item_inventory.csv')
item_shop = operateCSV.baca_csv(r'data\item_shop.csv')
monster_inventory = operateCSV.baca_csv(r'data\monster_inventory.csv')
monster_shop = operateCSV.baca_csv(r'data\monster_shop.csv')

(username, user_id, role, coin) = ('', '', '', 0)

berhenti = False
while not(berhenti):
  menu = input("").upper()
  if menu == 'REGISTER':
    (user_dan_monster, role, coin) = (F01.register(username, user_data), 'agent', 0)
  elif menu == 'LOGIN':
    (username, role, coin) = (F02.login(username, role, coin))
  elif menu == 'LOGOUT':
    (username, role, coin) = (F03.logout(username, role, coin))
  elif (menu == "SHOP"):
    print(">>> SHOP")
    print()
    if username != '':
      if role == "admin":
        (username, role, coin, monster_shop, item_shop) = (F12.shop_management(username, role, coin))
      else: # role == "agent"
        (username, role, coin, user_data, monster_inventory, monster_shop, item_inventory, item_shop) = (F10.shop_currency(username, role, coin))
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "LABORATORY"):
    if username != '':
      if role == "agent":
        (username, role, coin, user_data, monster_inventory) = (F11.laboratory(username, role, coin))
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu == "MONSTER"):
    if username != '':
      if role == "admin":
        print(">>> MONSTER")
        (username, role, coin, monster_data) = (F13.monster_management(username, role, coin))
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu == "JACKPOT"):
    if username != '':
      if role == "admin":
        print(">>> JACKPOT")
        coin, monster_inventory = B04.jackpot(username, coin)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
    
  else:
    print("Perintah tidak dikenal.")

