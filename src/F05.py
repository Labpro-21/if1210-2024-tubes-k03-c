def level_modifier(monsterinv_list : list, user_id : int, user_monster : list ):
    item_monster = testloader.filter_monster(monsterinv_list, user_id, user_monster)
    # base attribut ada pada monster.csv
    for row in item_monster :
        atk_power   = row[2]
        def_power   = row[3]
        hp          = row[4]
    for level in range(1, 6) :
        if level == 1:
            return atk_power, def_power, hp
        else :
            atk_power_new = atk_power*(((level - 1)*10)/100)
            def_power_new = def_power*(((level - 1)*10)/100)
            hp_new        = hp*(((level - 1)*10)/100)
            return atk_power_new, def_power_new, hp_new

def attack_power(monsterinv_list : list, user_id : int, user_monster : list ):
    item_monster = testloader.filter_monster(monsterinv_list, user_id, user_monster)
    for row in item_monster :
        atk_power   = row[2]

    min_power = atk_power * 0.7
    max_power = atk_power * 1.3
    if max_power > 100 :
        max_power = 100 
    return max_power, min_power

def atk_calculation(monsterinv_list : list, user_id : int, user_monster : list ):
    item_monster = testloader.filter_monster(monsterinv_list, user_id, user_monster)
    for row in item_monster :
        atk_power   = row[2]
        def_power   = row[3]
    atk_power_modifier = atk_power - (atk_power * (def_power*0.01))
    return atk_power_modifier, atk_power, def_power

def hp_calculation(monsterinv_list : list, user_id : int, user_monster : list ):
    item_monster = testloader.filter_monster(monsterinv_list, user_id, user_monster)
    # base attribut ada pada monster.csv
    for row in item_monster :
        atk_power   = row[2]
        def_power   = row[3]
        hp          = row[4]
    hp_modifier = hp - atk_calculation(atk_power, def_power)
    return hp_modifier
