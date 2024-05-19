import operateCSV
import glbfunc #NK

#constants
u_id=0
u_n=1
u_m_id=1
u_i_type=1
u_i_q=0
u_m_lv=2

m_id=0
m_type=1
m_atk=2
m_gua=3
m_hp=4
m_lv=1

#monster=operateCSV.baca_csv(r'data\monster.csv')
#monstinv=operateCSV.baca_csv(r'data\monster_inventory.csv')
#storage=operateCSV.baca_csv(r'data\item_inventory.csv')
#userdat=operateCSV.baca_csv(r'data\user.csv')


#filter monster berdasarkan data user
def filter_monster(monsterinv_list : list,user : int, user_monster : list) -> list:
    result_user_monster = []
    for data in monsterinv_list:
        if data[u_id]==user:
            result_user_monster.append([data[m_id],data[m_type],data[m_atk],data[m_gua],data[m_hp]])
    return result_user_monster

def filter_monster_hp(pmonster_id : int, pmonster_data : list) :
    result_hp = 0
    for data in pmonster_data:
        if data[m_id]==pmonster_id:
            result_hp = data[m_hp]
            break
    return result_hp    

#filter item berdasarkan data user
def filter_item(storage : list, user_id : int, user_inventory : list) -> list:
    for item in storage:
        if item[u_id]==user_id:
            user_inventory.append([item[u_i_type],item[u_i_q]])
    return user_inventory

def filter_potion(monster_type : str ,user_id : int, user_inventory : list) :
    res_potion = ['nama_tipe','qty']
    nama_type=''
    qty=0
    for user_inv in user_inventory:        
        if user_inv[u_id] == user_id and user_inv[1] == monster_type:
            nama_type = glbfunc.ket_potion(monster_type)
            qty=user_inv[2]
            break
    return nama_type,qty
            
#mengisi monster inventory setelah di filter
def monster_inventory(monster_list : list,user_monster : list, monster_invent : list) -> list:
    r_monster_invent=[]
    for monster in monster_list: 
       for usermon in user_monster:
            if monster[0]==usermon[1]:
                r_monster_invent.append([monster[m_type],monster[m_atk],monster[m_gua],monster[m_hp],usermon[m_lv]])
    return r_monster_invent

def get_uid(user_data : list, username: str) -> int:
    for user in user_data:
        if user[u_n]==username:
            break
    return user[0]

def get_storage(items_monster_inventory:list, user_id:int, data_monster:list):

   # item_monster = glbfunc.search_monster(data_monster, monster_id)
    arr_list_inventory = []
    no_urut = 1
    for i in items_monster_inventory :
        monster_id = i[1]
        arr_item_inventory = [no_urut, user_id, "monster", monster_id, '' ]
        arr_list_inventory.append(arr_item_inventory)
        no_urut += 1
    return arr_list_inventory    


#formatnya
#[['type', 'atk', 'def', 'hp', 'lv'], ['Pikachow', '125', '10', '600', '1'], ['Bulbu', '50', '50', '1200', '4'], ['Zeze', '300', '10', '100', 
#'1'], ['Chacha', '80', '30', '700', '2'], ['Bulbasaur', '90', '20', '700', '1'], ['Mio', '9999', '9999', '9999', '5']]
