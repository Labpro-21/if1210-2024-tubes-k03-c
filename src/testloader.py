import operateCSV

#constants
u_id=0
u_m_id=1
u_m_lv=2

m_id=0
m_type=1
m_atk=2
m_gua=3
m_hp=4
m_lv=1

monster=operateCSV.baca_csv(r'data\monster.csv')

monstinv=operateCSV.baca_csv(r'data\monster_inventory.csv')

user_monster=[['monster_id','monster_level']]
monster_invent=[['type','atk','def','hp','lv']]

#filter monster berdasarkan data user
def filter_monster(monsterinv_list : list,user : int) -> list:
    for data in monsterinv_list:
        if data[u_id]==user:
            user_monster.append([data[u_m_id],data[u_m_lv]])
    return user_monster

def monster_inventory(monster_list : list,user_monster : list) -> list:
    for monster in monster_list: 
       for usermon in user_monster:
            if monster[m_id]==usermon[m_id]:
                monster_invent.append([monster[m_type],monster[m_atk],monster[m_gua],monster[m_hp],usermon[m_lv]])
    return monster_invent


user=(input('uid: '))
print(monster_inventory(monster,filter_monster(monstinv,user)))