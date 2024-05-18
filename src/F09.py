import F08, testloader

#fungsi arena
def arena(username : str, role : str, coins : int, menu : str, monster_data : list, player_monster_arr : list, player_inv_arr : list, potion_check : list, stage : int) -> tuple[str,str,int]:
    print(f'STAGE {stage}')
    (coin,win,damage_taken,damage_dealt,gained)=F08.battle(username, role, coins, menu, stage, monster_data, player_monster_arr, player_inv_arr, potion_check)
    return username,role,coin,damage_taken,damage_dealt,win,gained