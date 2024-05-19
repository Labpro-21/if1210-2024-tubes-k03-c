def logout(user, role, coin):
  if user:
    username = ""
    role = ""
    coin = 0
    return  username, role, coin
  else:
    print("Logout gagal!")
    print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")