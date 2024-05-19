import operateCSV
import testloader
import math
import glbfunc
import os

def finventory(user_data:list, username:str, puser_id : int, 
                monsterinv_list : list, user_monster : list,
                monster_invent : list, storage : list, user_inventory : list, 
                pdata_item_inventory : list, pmonster_data : list ):
# tampilan untuk header pada fungsi 
    item_user = testloader.get_uid(user_data, username)
    nama_user = item_user[1]
    coin_user = item_user[4]

    filter_monster = testloader.filter_monster(monsterinv_list, puser_id, user_monster)
    items_monster_inventory = glbfunc.search_monster_inventory(monster_invent,user_id)
    arr_list_inventory = []
    no_urut = 1

    for i in items_monster_inventory :
        monster_id = i[1]
        arr_item_inventory = [no_urut, puser_id, "monster", monster_id, '' ]
        arr_list_inventory.append(arr_item_inventory)
        no_urut += 1

    items_inventory = glbfunc.search_item_inventory(pdata_item_inventory, user_id)     
    filter_monster = testloader.filter_monster(monsterinv_list, puser_id, user_monster)
    type1 = filter_monster[0]
    
    for j in items_inventory :
        type1 = j[1]
        arr_item_inventory = [no_urut, puser_id, "potion", '', type1 ]
        arr_list_inventory.append(arr_item_inventory)
        no_urut += 1        

# menampilkan menu ----------------------------------------------------------------------------------------------
    print_monster = ""
    for item_inv in arr_list_inventory :
        no_urut     = item_inv[0]
        puser_id    = item_inv[1]
        type_inv    = item_inv[2]
        monster_id  = item_inv[3]
        type_id     = item_inv[4]
    
# ---------------------------------------
        if type_inv == "monster" : # Apabila mengandung monster    
            item_monster = testloader.filter_monster(monsterinv_list, puser_id, user_monster)
            items_monster_inventory = glbfunc.search_monster_inventory(monster_invent,user_id)
            for row in item_monster :
                nama    = row[1]
                hp      = row[4]  
            for row in items_monster_inventory :
                level   = row[2]          
            print_monster +=f'\n{no_urut}. Monster (Name : {nama}, Lvl : {level}, Hp : {hp})'
    
        elif type_inv == "potion" : # Apabila mengandung potion          
            (nama_type,type_qty)= testloader.filter_potion(type_id, puser_id, pdata_item_inventory)
            print_monster += f'\n{no_urut}. Potion (Type : {nama_type}, Qty : {type_qty})'
            no_urut += 1
    
    berhenti = False
    print_monster+='\nKetikkan 0 untuk keluar' # Agar keluar program
    while not(berhenti):
        print(f"""
    ======= INVENTORY LIST (User ID: {puser_id}, nama user = {nama_user}) ========
                    Jumlah O.W.C.A. Coin-mu sekarang {coin_user}
        
    {print_monster}        
    """)

        nomor = int(input("Ketikkan id untuk menampilkan detail item : "))
        if nomor ==0 :
            berhenti=True
        else:
            res_item_inventory = glbfunc.search_list_inventory(arr_list_inventory, nomor)
            type_inv    = res_item_inventory[2]
            monster_id  = res_item_inventory[1]
            type_id     = res_item_inventory[4]    
            nilai_hp    = testloader.filter_monster_hp(monster_id, pmonster_data)
            if type_inv == "monster" :
                item_monster            = testloader.filter_monster(monsterinv_list, puser_id, user_monster)
                items_monster_inventory = glbfunc.search_monster_inventory(monster_invent,user_id)
                for row in items_monster_inventory :
                    level = row[2]                
                for row in item_monster :
                    print(f"""
                Monster
                Name        :{row[1]}
                ATK Power   :{row[2]}
                DEF Power   :{row[3]}
                HP          :{row[4]}
                Level       :{level}
                    """)
            elif type_inv == "potion" :
                # items_inventory = glbfunc.search_item_inventory(pdata_item_inventory, user_id)
                (nama_type,type_qty)= testloader.filter_potion(type_id, puser_id, pdata_item_inventory)            
                print(f"""
            Potion
            Type        : {nama_type}
            Quantity    : {type_qty}
                """)
            os.system('pause')
        

