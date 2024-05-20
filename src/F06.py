
def Strength_Potion(atk_power):
    atk_modifier = atk_power + (0.05 * (atk_power))
    return atk_modifier

def Resilience_Potion(def_power):
    def_modifier = def_power + (0.25 * (def_power))
    return def_modifier

def Healing_Potion(hp):
    hp_modifier += (0.25 * hp)
    if hp_modifier > hp:
        hp_modifier = hp
    return hp_modifier
