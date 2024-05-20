def help(username,role):
    print ("")
    print ("="*10+"HELP"+"="*10)
    print ("")
    if role == "agent":
        print (f"Halo {role} {username} Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print (" "*5+"1. Logout : Keluar dari akun yang sedang digunakan")
        print (" "*5+"2. Inventory : Melihat owca coin yang dimiliki dan item-item yang dimiliki oleh Agent")
        print (" "*5+"3. Battle : Memulai peraturangan melawan monster")
        print (" "*5+"4. Arena : Meningkatkan kemampuan agen dan para monster serta mendapatkan owca coin")
        print (" "*5+"5. Shop : Tempat Agent membeli monster dan potion.")
        print (" "*5+"6. Laboratory : Upgrade monster yang dimiliki di inventory")
        print (" "*5+"7. Save : Menyimpan data game")
        print (" "*5+"8. Jackpot : GACHA GAS")
        print (" "*5+"9. Keluar : Yah.. selesai sudah")

    elif role == "admin":
        print (f"Halo {role} Berikut adalah hal-hal yang dapat kamu lakukan:")
        print (" "*5+"1. Logout : Keluar dari akun yang sedang digunakan")
        print (" "*5+"2. Shop : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print (" "*5+"3. Monster : Melakukan manajemen pada monster, dapat menambah monster baru")
        print (" "*5+"4. Save : Menyimpan data game")
        print (" "*5+"5. Keluar : Yah.. selesai sudah")