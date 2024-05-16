import testloader
import operateCSV
def fmonster () :
    # search monster by user id
    item_monster    = testloader.filter_monster(operateCSV.baca_csv(r"data\monster.csv"), monster_id)
    var_type        = item_monster[1]
    atk_power_min   = (item_monster[2]) - (item_monster[2] * 0.3)
    atk_power_max   = (item_monster[2] * 2) - (item_monster[2] * 0.3) 
    def_power       = item_monster[3]
    hp              = item_monster[4]
    return var_type, atk_power_min, atk_power_max, def_power, hp

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
