import operateCSV

def login(user, role_type, coin, user_data):
  if user:
    print("Login gagal!")
    print(f"Anda telah login dengan username {user}, silakan lakukan logout sebelum melakukan login")
    return username, role, coin

  else: # belum login
    # user_data = operateCSV.baca_csv(r"data\file_csv\user.csv")

    berhasil = False
    while not(berhasil):
      username = input("Masukkan username: ")
      password = input("Masukkan password: ")
      for row in user_data[1:]:
        if username == row[1]:
          if password == row[2]:
              role = row[3]
              coin = row[4]
              print(f"Selamat datang kembali, {role} {username}!")
              print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
              berhasil = True
              return username, role, coin
      print("Input username atau password salah!")