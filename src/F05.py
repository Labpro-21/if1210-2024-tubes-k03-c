def level_modifier(level : int, attribute : int ):
    for level in range(1, 6) :
        if level == 1:
            attribute = attribute
        else :
            attribute += attribute*(((level - 1)*10)/100)
        return attribute

def attack_power(atk_power : int):
    min_power = atk_power * 0.7
    max_power = atk_power * 1.3
    if max_power > 100 :
        max_power = 100 
    return max_power, min_power

def atk_calculation(atk_power : int, def_power : int):
    atk_power_modifier = atk_power - (atk_power * (def_power*0.01))
    return atk_power_modifier

def hp_calculation(atk_power : int, hp : int, def_power : int):
    hp_modifier = hp - atk_calculation(atk_power, def_power)
    return hp_modifier
