import sys
sys.path.append('src')
import F01, F10, F11, F12, F13
import operateCSV


(username, user_id, role, coin_count) = ('', '', '', 0)

berhenti = False
while not(berhenti):
  menu = input("")
  if menu.upper() == 'REGISTER':
    (user_dan_monster, role, coin_count) = (F01.register(username), 'agent', 0)
  elif menu.upper() == 'LOGIN':
    (username, role, coin_count) = (F02.login(username))
  elif menu.upper() == 'LOGOUT':
    (username, role, coin_count) = (F03.logout(username))
  elif (menu.upper() == "SHOP"):
    print(">>> SHOP")
    print()
    if username != '':
      if role == "admin":
        F12.shop_management()
      else: # role == "agent"
        F10.shop_currency(username)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu.upper() == "LABORATORY"):
    if username != '':
      if role == "agent":
        (username) = F11.laboratory(username)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")

  elif (menu.upper() == "MONSTER"):
    if username != '':
      if role == "admin":
        print(">>> MONSTER")
        F13.monster_management()
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
  elif (menu.upper() == "JACKPOT"):
    if username != '':
      if role == "admin":
        print(">>> JACKPOT")
        B04.jackpot(username)
    else:
      print("Anda belum masuk ke akun apapun, silakan login terlebih dahulu\n")
    
  else:
    print("Perintah tidak dikenal.")

