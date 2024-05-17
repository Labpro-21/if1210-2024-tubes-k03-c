def help(username,role):
    print ("")
    print ("="*10+"HELP"+"="*10)
    print ("")
    if role == "Agent":
        print (f"Halo {role} {username} Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print (" "*5+"1. Logout : Keluar dari akun yang sedang digunakan")
        print (" "*5+"2. Monster : Melihat owca-dex yang dimiliki oleh Agent")
        print (" "*5+"3. Inventory : Melihat owca coin yang dimiliki dan item-item yang dimiliki oleh Agent")
        print (" "*5+"4. Battle : Memulai peraturangan melawan monster")
        print (" "*5+"5. Arena : Meningkatkan kemampuan agen dan para monster serta mendapatkan owca coin")
        print (" "*5+"6. Shop : Tempat Agent membeli monster dan potion.")
        print (" "*5+"7. Laboratory : Upgrade monster yang dimiliki di inventory")
        print (" "*5+"8. Save : Menyimpan data game")
    elif role == "Admin":
        print (f"Halo {role} Berikut adalah hal-hal yang dapat kamu lakukan:")
        print (" "*5+"1. Logout : Keluar dari akun yang sedang digunakan")
        print (" "*5+"2. Shop Management : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print (" "*5+"3. Monster Management : Melakukan manajemen pada monster, dapat menambah monster baru")
    else:
        print ("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print (" "*5+"1. Login : Masuk ke dalam akun yang sudah terdaftar")
        print (" "*5+"2. Register : Membuat akun baru")
