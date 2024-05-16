import operateCSV

def potion():
    # search monster inventory by user id
    item_monster = operateCSV.baca_csv(r"data\monster_inventory.csv")
    for row in user_data: # cek tiap baris dari data 'user.csv'
        atk_power       = row[2]
        def_power       = row[3]
        hp              = row[4]
        strength_potion     = atk_power + (atk_power * 0.05)
        resilience_potion   = def_power + (def_power * 0.05)
        if hpx > hp :
            healing_potion  = hp + (hp *0.25)
        else :
            healing_potion  = hpx + (hpx *0.25)
        
        return strength_potion, resilience_potion, healing_potion    
