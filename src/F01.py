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

def register(user, user_data, monster_data):
  print(">>> REGISTER")
  if user: # Jika user telah login
    print("Register gagal!")
    print(f"Anda telah login dengan username {user}, silakan lakukan 'LOGOUT' sebelum melakukan register.")
    print()
    return user, "-1", user_data, monster_inventory
    
  else: # Jika user belum login
    username = get_valid_username()
    password = get_valid_password()
    print()

    for row in user_data:  # cek tiap baris dari data 'user.csv'
      if username == row[1]:  # cek apakah username sudah terpakai
        print("Username telah terdaftar, silakan pilih username lain!")
        return user, "-1", user_data, monster_inventory

    if not password:
      print("Password tidak boleh kosong!")
      return user, "-1", user_data, monster_inventory

    new_user = [] # array untuk menampung data user baru saat register
  
    new_id = len(user_data)
    new_user.append(new_id)
    new_user.append(username)
    new_user.append(password)
    new_user.append('agent')
    new_user.append(str(0))

    merge_user = [] 
    for row in user_data:
      merge_user.append(row) 
        
    merge_user.append(new_user)

    print("Silahkan pilih salah satu monster sebagai monster awalmu:")
    for i in range(1, 6):
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

  # operateCSV.tulis_csv(r'data\user.csv', merge_user)
  # monster_data = operateCSV.baca_csv(r'data\monster.csv')
  return username, monster_id

# register("", operateCSV.baca_csv(r'data\user.csv'))