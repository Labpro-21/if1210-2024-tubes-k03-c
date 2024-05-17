import F08

#fungsi arena
def arena(username : str, role : str, coin : int, menu : str, monster_data : list, player_monster_arr : list, player_inv_arr : list, potion_check : list) -> tuple[str,str,int]:
    stage=1
    alive=True
    total_taken=0
    total_dealt=0
    total_oc=0
    while (not stage==5) and alive:
        print(f'STAGE {stage}')
        (coins,win,damage_taken,damage_dealt,gained)=F08.battle(username, role, coin, menu, stage, monster_data, player_monster_arr, player_inv_arr, potion_check)
        if win:
            stage+=1
            print(f'Lanjut ke stage {stage}.]\n')
        else:
            alive=False
        total_taken+=damage_taken
        total_dealt+=damage_dealt
        total_oc+=gained
    print(f"""============== STATS ==============
Total hadiah      : {total_oc} OC
Jumlah stage      : {stage}
Damage diberikan  : {total_dealt}
Damage diterima   : {total_taken}
""")
    return username,role,coins
        