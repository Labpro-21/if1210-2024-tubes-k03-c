import operateCSV

def login(user, role_type, coin):
  print(">>> LOGIN")
  if user:
    print("Login gagal!")
    print(f"Anda telah login dengan username {user}, silakan lakukan logout sebelum melakukan login")
    return user

  else: # belum login
    user_data = operateCSV.baca_csv(r"data\user.csv")

    berhasil = False
    while not(berhasil):
      username = input("Masukkan username: ")
      password = input("Masukkan password: ")
      for row in user_data: # cek tiap baris dari data 'user.csv'
        if username in row[1]:
          if password == row[2]:
              role = row[3]
              coin = row[4]
              print(f"Selamat datang kembali, {role} {username}!")
              print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
              berhasil = True
              return username, role, coin
      print("Input username atau password salah!")