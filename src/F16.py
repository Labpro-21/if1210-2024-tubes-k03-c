def save():
    # Implementasi logika penyimpanan perubahan (F15)
    print("Menyimpan perubahan...")
    # Logika penyimpanan disini

def exit_program():
    pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    if pilihan == 'y':
        save()
    elif pilihan == 'n':
        print("Keluar program tanpa menyimpan.")
    else:
        while pilihan not in ['y', 'n']:
            pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
            if pilihan == 'y':
                save()
            elif pilihan == 'n':
                print("Keluar program tanpa menyimpan.")
            else:
                continue

# Contoh penggunaan
while True:
    command = input(">>> ").upper()
    if command == "EXIT":
        exit_program()
        break
    else:
        print("Perintah tidak dikenali.")
