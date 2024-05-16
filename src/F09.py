import F08,testloader

def arena(username : str, role : str, coin : int, menu : str):
    stage=1
    while (not stage==5) and F08.win:
        print(f'STAGE {stage}')
        F08.battle(username,role,coin,testloader.userdat, 'ARENA', stage)
        if F08.win:
            stage+=1
    return username,role,coin
        