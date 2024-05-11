import glbfunc
import random
import math

# Inisialisasi data untuk membaca csv
# loading data monster
csv_file_monster = 'monster.csv'
data_monster =glbfunc.read_csv(csv_file_monster, ";")

# loading data monster_inventory.csv
csv_monster_inventory = 'monster_inventory.csv'
data_monster_inventory =glbfunc.read_csv(csv_monster_inventory, ";")

# loading data item_inventory.csv
csv_item_inventory = 'item_inventory.csv'
data_item_inventory =glbfunc.read_csv(csv_item_inventory, ";")

# loading data user.csv
csv_user = 'user.csv'
data_user =glbfunc.read_csv(csv_user, ";")

# fungsi F07
def finventory():
    user_id = 3
    monster_id = 2
    item_user = glbfunc.search_user(data_user, user_id)
    nama_user = item_user[1]
    coin_user = item_user[4]

    # search monster by user id
    item_monster = glbfunc.search_monster(data_monster, monster_id)
    # search monster inventory by user id
    items_monster_inventory = glbfunc.search_monster_inventory(data_monster_inventory, user_id)
    monster_id = item_monster[1]
    arr_list_inventory = []
    no_urut = 1

    for i in items_monster_inventory :
        monster_id = i[1]
        arr_item_inventory = [no_urut, user_id, "monster", monster_id, '' ]
        arr_list_inventory.append(arr_item_inventory)
        no_urut += 1
     # search monster inventory by user id
    items_inventory = glbfunc.search_item_inventory(data_item_inventory, user_id)  
    type1 = item_monster[1]
    for j in items_inventory :
        type1 = j[1]
        arr_item_inventory = [no_urut, user_id, "potion", '', type1 ]
        arr_list_inventory.append(arr_item_inventory)
        no_urut += 1        
# menampilkan menu ----------------------------------------------------------------------------------------------
    print_monster = ""
    for item_inv in arr_list_inventory :
        no_urut     = item_inv[0]
        user_id     = item_inv[1]
        type_inv    = item_inv[2]
        monster_id  = item_inv[3]
        type_id     = item_inv[4]
    # ---------------------------------------
        if type_inv == "monster" :
            res_monster = glbfunc.search_monster(data_monster, monster_id)
            print_monster +=f'{no_urut}. Monster (Name : {res_monster[1]}, Lvl : , Hp : {res_monster[4]})'
    
        elif type_inv == "potion" :
            res_potion = glbfunc.search_item_inventory(data_item_inventory, user_id)
            for item_res_potion in res_potion :
                type_posion = ""
                type_qty = "" 
                if item_res_potion[1].lower() == "strength" :
                    type_posion = glbfunc.ket_potion(item_res_potion[1].lower())
                    type_qty = item_res_potion[2]
                elif item_res_potion[1].lower() == "resilience" :
                    type_posion =  glbfunc.ket_potion(item_res_potion[1].lower())
                    type_qty = item_res_potion[2]
                elif item_res_potion[1].lower() == "healing" :
                    type_posion =  glbfunc.ket_potion(item_res_potion[1].lower())
                    type_qty = item_res_potion[2]
            print_monster += f'{no_urut}. Potion (Type : {type_posion}, Qty : {type_qty})'
            no_urut += 1

    print(f"""
======= INVENTORY LIST (User ID: {user_id}, nama user = {nama_user}) ========
                Jumlah O.W.C.A. Coin-mu sekarang {coin_user}
    
{print_monster}        
""")

    nomor = int(input("Ketikkan id untuk menampilkan detail item : "))
    # search list inventory (untuk mencari detail sesuai input pengguna)
    res_item_inventory = glbfunc.search_list_inventory(arr_list_inventory, nomor)
    type_inv    = res_item_inventory[2]
    monster_id  = res_item_inventory[3]
    type_id     = res_item_inventory[4]    
    if type_inv == "monster" :
        item_monster = glbfunc.search_monster(data_monster, monster_id)
        print(f"""
    Monster
    Name        :{item_monster[1]})
    ATK Power   :{item_monster[2]}
    DEF Power   :{item_monster[3]}
    HP          :{item_monster[4]}
    Level       :
        """)
    elif type_inv == "potion" :
        items_inventory = glbfunc.search_item_inventory(data_item_inventory, user_id) 
        print(f"""
    Potion
    Type        : {glbfunc.ket_potion(items_inventory[0][1].lower())}
    Quantity    : {items_inventory[0] [2]}
        """)

def fmonster () :
    # search monster by user id
    item_monster = glbfunc.search_monster(data_monster, monster_id)
    # search monster inventory by user id
    items_monster_inventory = glbfunc.search_monster_inventory(data_monster_inventory, user_id)
    var_type        = item_monster[1]
    atk_power_min   = (item_monster[2]) - (item_monster[2] * 0.3)
    atk_power_max   = (item_monster[2] * 2) - (item_monster[2] * 0.3) 
    def_power       = item_monster[3]
    hp              = item_monster[4]

def flevel () :
    for level in range(1, 6) :
        if level == 1:
            atk_power   = item_monster[2]
            def_power   = item_monster[3]
            hp          = item_monster[4]
        else:
            level_modifier = i * (10 / 100)
            atk_power = int(item_monster[2] * (1 + level_modifier))
            def_power = item_monster[3]
            return level_modifier

def potion():
    # search monster inventory by user id
    item_monster = glbfunc.search_monster(data_monster, monster_id)
    items_monster_inventory = glbfunc.search_monster_inventory(data_monster_inventory, user_id)
    atk_power       = item_monster[2]
    def_power       = item_monster[3]
    hp              = item_monster[4]
    strength_potion     = atk_power + (atk_power * 0.05)
    resilience_potion   = def_power + (def_power * 0.05)
    if hpx > hp :
        healing_potion  = hp + (hp *0.25)
    else :
        healing_potion  = hpx + (hpx *0.25)
    
    return strength_potion, resilience_potion, healing_potion    
    