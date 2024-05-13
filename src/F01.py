from F00 import RNG
import operateCSV

def cek_karakter(username):
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    for char in username:
        if char not in valid_characters:
            return False
    return True

def get_valid_username():
    while True:
        username = input("Masukkan username: ")
        if cek_karakter(username):
            return username
        else:
            print("Username hanya boleh dibentuk oleh alfabet, angka, nomor, strip, dan underscore!")

def get_valid_password():
    while True:
        password = input("Masukkan password: ")
        if len(password) >= 8:
            return password
        else:
            print("Password harus terdiri dari minimal 8 karakter!")

def register(user):
  user_data = operateCSV.baca_csv("user.csv")
  print(">>> REGISTER")
  if user: # Jika user telah login
    print("Register gagal!")
    print(f"Anda telah login dengan username {user}, silakan lakukan 'LOGOUT' sebelum melakukan register.")
    print()
    return user
    
  else: # Jika user belum login
    username = get_valid_username()
    password = get_valid_password()
    print()

    for row in user_data:  # cek tiap baris dari data 'user.csv'
      if username == row[1]:  # cek apakah username sudah terpakai
        print("Username telah terdaftar, silakan pilih username lain!")
        return user

    if not password:
      print("Password tidak boleh kosong!")
      return user
        
    new_user = [] # array untuk menampung data user baru saat register

    for i in range(1, len(user_data)):
      if str(F00.RNG(1, 100)) not in user_data[i][0]:
        new_user.append(str(F00.RNG(1, 100)))
        new_user.append(username)
        new_user.append(password)
        new_user.append('agent')
        new_user.append(str(0))

    user_gabung = [] # array untuk menampung data user lama dan user baru
    for row in csv_user:
      user_gabung.append(row) # tampung data user lama
        
    user_gabung.append(new_user) # tambah data user baru

    operateCSV.tulis_csv('user.csv', user_gabung)
    monster_data = operateCSV.baca_csv('monster.csv') 

    print("Silahkan pilih salah satu monster sebagai monster awalmu:")
    for i in range(1, 4):
      print(f"{i}. {monster_data[i][1]}")
  
    pilih = int(input("Monster pilihanmu: "))
    if pilih in range(1,4):
      monster_id = monster_data[pilih][0]
      monster_name = ""
      for monster_entry in monster_data[1:]:
        if monster_entry[0] == monster_id:
          monster_name = monster_entry[1]
          break
      if monster_name:
        print(f"Selamat datang, Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_name}!")
      else:
        print("Monster tidak ditemukan.")
    else:
      print("Pilihan monster tidak valid.")
  

  return username, monster_id

