import operateCSV

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

monster=operateCSV.baca_csv(r'data\monster.csv')
monstinv=operateCSV.baca_csv(r'data\monster_inventory.csv')
storage=operateCSV.baca_csv(r'data\item_inventory.csv')
userdat=operateCSV.baca_csv(r'data\user.csv')


#filter monster berdasarkan data user
def filter_monster(monsterinv_list : list,user : int, user_monster : list) -> list:
    for data in monsterinv_list:
        if data[u_id]==user:
            user_monster.append([data[u_m_id],data[u_m_lv]])
    return user_monster

#filter item berdasarkan data user
def filter_item(storage : list, user : int, user_inventory : list) -> list:
    for item in storage:
        if item[u_id]==str(user):
            user_inventory.append([item[u_i_type],item[u_i_q]])
    return user_inventory
            
#mengisi monster inventory setelah di filter
def monster_inventory(monster_list : list,user_monster : list, monster_invent : list) -> list:
    for monster in monster_list: 
       for usermon in user_monster:
            if monster[m_id]==usermon[m_id]:
                monster_invent.append([monster[m_type],monster[m_atk],monster[m_gua],monster[m_hp],usermon[m_lv]])
    return monster_invent

def get_uid(user_data : list,username: str) -> int:
    for user in user_data:
        if user[u_n]==username:
            break
    return user[0]
#formatnya
#[['type', 'atk', 'def', 'hp', 'lv'], ['Pikachow', '125', '10', '600', '1'], ['Bulbu', '50', '50', '1200', '4'], ['Zeze', '300', '10', '100', 
#'1'], ['Chacha', '80', '30', '700', '2'], ['Bulbasaur', '90', '20', '700', '1'], ['Mio', '9999', '9999', '9999', '5']]