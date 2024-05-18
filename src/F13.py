import sys
sys.path.append('src')

import operateCSV

def maks(daftar):
    if not daftar:  
        return None
    max_val = daftar[0]  
    for item in daftar[1:]:
        if item > max_val:
            max_val = item
    return max_val


def ambil_id_terbawah(monster_data):
  ids = [int(monster[0]) for monster in monster_data[1:]]  
  if not ids:  
    return 1
  else:
    return maks(ids) + 1 


def lihat_monster():
  monster_data = operateCSV.baca_csv(r"data\monster.csv")

  print("ID | Type         | ATK Power | DEF Power | HP   |")
  for monster in monster_data[1:]:
      print(f"{monster[0]:<2} | {monster[1]:<12} | {monster[2]:<9} | {monster[3]:<9} | {monster[4]:<4} | ")


def tambah_monster():
  monster_data = operateCSV.baca_csv(r"data\monster.csv")
  print("Memulai pembuatan monster baru")
  while True:
    monster_name = input(">>> Masukkan Type / Nama : ")
    nama_terdaftar = False
    for monster in monster_data[1:]:
      if monster[1] == monster_name:
        print("Nama sudah terdaftar, coba lagi!")
        nama_terdaftar = True
        break
    if not nama_terdaftar:
      break

  while True:
    atk_power = input(">>> Masukkan ATK Power : ")
    if atk_power.isdigit():
      atk_power = int(atk_power)
      break
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
  
  while True:
    def_power = input(">>> Masukkan DEF Power (0-50) : ")
    if def_power.isdigit():
      def_power = int(def_power)
      if 0 <= def_power <= 50:
        break
      else:
        print("DEF Power harus bernilai 0-50, coba lagi!")
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
    
  while True:
    hp = input(">>> Masukkan HP : ")
    if hp.isdigit():
      hp = int(hp)
      break
    else:
      print("Masukkan input bertipe Integer, coba lagi!")
  
  print("Monster baru berhasil dibuat!")
  print("Type : ", monster_name)
  print("ATK Power : ", atk_power)
  print("DEF Power : ", def_power)
  print("HP : ", hp)

  monster_id_baru = ambil_id_terbawah(monster_data)

  print(">>> Tambahkan Monster ke database (Y/N) : ", end="")
  hapus_confirm = input()
  if (hapus_confirm.lower() == 'y'):
    print("Monster baru telah ditambahkan")
    monster_data.append([monster_id_baru,monster_name, atk_power, def_power, hp])
    return monster_data
    # operateCSV.tulis_csv(r"data\monster.csv", monster_data)
  else: # hapus_confirm == n
    print("Monster gagal ditambahkan!") 


def monster_management(username, role, coin):
  print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
  print("1. Tampilkan semua Monster")
  print("2. Tambah Monster baru")
  print("3. Keluar")
  keluar = False
  while not keluar:
    aksi = input(">>> Pilih Aksi : ")
    if (aksi == "1"):
      lihat_monster()
    elif (aksi == "2"):
      monster_data = tambah_monster()
    elif (aksi == "3"):
      print("Dadah, sampai jumpa lagi!")
      keluar = True
    else:
      print("Aksi tidak valid. Silakan pilih aksi lainnya.")

  return username, role, coin, monster_data