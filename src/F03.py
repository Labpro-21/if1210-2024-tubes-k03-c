def logout(user, role, coin):
  if user:
    username = ""
    role = ""
    coin = 0
    print("Berhasil logout!")
    return  username, role, coin
  else:
    print("Logout gagal!")
    print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")