import glbfunc

#constants
uid=0
m_id=1
mlv=2

mo_id=0
type=1
atk=2
gua=3
hp=4
lv=1

monster=glbfunc.csv_reader('monster.csv')
monster_list=glbfunc.csv_parser(monster,';',11,5)

monstinv=glbfunc.csv_reader('monster_inventory.csv')
monstinv_list=glbfunc.csv_parser(monstinv,';',9,3)

user_monster=[['monster_id','monster_level']]
monster_invent=[['type','atk','def','hp','lv']]

def filter_monster(monsterinv_list,user):
    for data in monsterinv_list:
        if data[uid]==user:
            user_monster.append([data[m_id],data[mlv]])
    return user_monster

def monster_inventory(monster_list,user_monster):
    for monster in monster_list: 
       for usermon in user_monster:
            if monster[mo_id]==usermon[mo_id]:
                monster_invent.append([monster[type],monster[atk],monster[gua],monster[hp],usermon[lv]])
    return monster_invent

user=(input('uid: '))
print(monster_inventory(monster_list,filter_monster(monstinv_list,user)))