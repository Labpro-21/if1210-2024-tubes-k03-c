import F00, math

#constants
u_id=0
u_m_id=1
u_i_type=0
u_i_q=1
u_m_lv=2

m_id=0
m_type=1
m_atk=2
m_gua=3
m_hp=4
m_lv=1

l_m_type=0
l_m_atk=1
l_m_gua=2
l_m_hp=3
l_m_lv=4

i_type=0
i_qty=1

# monster_arr=operateCSV.baca_csv(r'data\monster.csv')

#load stats monster untuk player
def player_statloader(list_monster : list,player_monster : int) -> list:
    loadedstat=[['atk','def','hp'],[int(list_monster[player_monster][l_m_atk])*(1+((int(list_monster[player_monster][l_m_lv])-1)*10)/100),int(list_monster[player_monster][l_m_gua])*(1+((int(list_monster[player_monster][l_m_lv])-1)*10)/100),int(list_monster[player_monster][l_m_hp])*(1+((int(list_monster[player_monster][l_m_lv])-1)*10)/100)]]
    return loadedstat

#load stats monster untuk enemy
def enemy_statloader(list_monster : list,enemy_monster : int, level : int) -> list:
    e_loadedstat=[['atk','def','hp'],[int(list_monster[enemy_monster][m_atk])*(1+((level-1)*10)/100),int(list_monster[enemy_monster][m_gua])*(1+((level-1)*10)/100),int(list_monster[enemy_monster][m_hp])*(1+((level-1)*10)/100)]]
    return e_loadedstat

#initialize high and low atk
def h_o_l(loaded_stat : list) -> list:
    hol=[['high','low'],[abs((math.floor(loaded_stat[1][0]*(1+(30/100))))),abs((math.floor(loaded_stat[1][0]*(1-(30/100)))))]]
    return hol

#menghitung turn
def turnCount(cond : bool,turn : int) -> int:
    if cond:
        turn+=1
    return turn

#menentukan rng monster lawan
def monsterRNG(monsterdat : list) -> int:
    chance=chanceRNG()
    if chance<999999: #chance 99.9999%
        monster=F00.RNG(1,(len(monsterdat)-1)) #for some reason klo lebih dr 13 overload idk need help here
        while monster==13:
            monster=F00.RNG(1,(len(monsterdat)-1))
    else: #chance==1000000 #chance 0.0001%
        monster=13
    return monster

#rng untuk chance
def chanceRNG() -> int:
    chance=F00.RNG(1,1000001)
    return chance

#menentukan rng level monster lawan
def monsterlvRNG() -> int:
    chance=chanceRNG()
    if chance<600000: #chance 60%
        r_lv=1
    elif chance<800000: #chance 20%
        r_lv=2
    elif chance<900000: #chance 10%
        r_lv=3
    elif chance<975000: #chance 7.5%
        r_lv=4
    else: #chance==1000000 #chance 2.5%
        r_lv=5
    return r_lv       

#menentukan rng attack
def attackRNG(low : int,high : int) -> int:
    return F00.RNG(low,high)

#menentukan rng OC
def ocRNG(level : int) -> int:
    if level==1: #chance 60%
        duit=F00.RNG(1,30)
    elif level==2: #chance 20%
        duit=F00.RNG(31,50)
    elif level==3: #chance 10%
        duit=F00.RNG(51,90)
    elif level==4: #chance 7.5%
        duit=F00.RNG(91,170)
    else: #level==5 chance 2.5%
        duit=F00.RNG(171,330)    
    return duit

#menampilkan musuh
def showMenu(loaded_stat : list, list_monster : list, enemy_rng : int, level : int, menu : str):
    print(f"""RAWRRR, Monster {list_monster[enemy_rng][m_type]} telah muncul !!!

Name      : {list_monster[enemy_rng][m_type]}
ATK Power : {math.floor(loaded_stat[1][0])}
DEF Power : {math.floor(loaded_stat[1][1])}
HP        : {math.floor(loaded_stat[1][2])}
Level     : {level}
""")

#selector monster player
def monSelect(player_monster_arr : list) -> int:
    print("============ MONSTER LIST ============")
    m_count=1
    for monster in player_monster_arr:
        if monster[l_m_type]!='type':
            print(f'{m_count}. {monster[l_m_type]}')
            m_count+=1
    print()
    slct=int(input('Pilih monster untuk bertarung: '))
    if slct in range(1,m_count):
        return slct      
    else:
        print('Pilihan nomor tidak tersedia!\n')
        return monSelect(player_monster_arr)

#display monster player    
def showMnst(player_monster_arr : list,player_monster : int, username : str):
    print(f"""        
RAWRRR, Agent {username} mengeluarkan monster {player_monster_arr[player_monster][l_m_type]} !!!
""")

#display status monster player      
def statShow(player_monster_arr : list,player_monster : int, loaded_stat : list):
    print(f"""Name      : {player_monster_arr[player_monster][l_m_type]}
ATK Power : {math.floor(loaded_stat[1][0])}
DEF Power : {math.floor(loaded_stat[1][1])}
HP        : {math.floor(loaded_stat[1][2])}
Level     : {player_monster_arr[player_monster][l_m_lv]}
""")

#display perintah player    
def display_playerTurn(turn_counter : int,player_monster_arr : list,player_monster : int):
    print(f"""============ TURN {turn_counter} ({player_monster_arr[player_monster][l_m_type]}) ============
1. Attack
2. Use Potion
3. Quit          
""")

#selector perintah player turn    
def playerTurn(turn_counter : int,player_monster_arr : list,player_monster : int) -> int:
    tslct=int(input('Pilih perintah: '))
    print()
    if tslct in [1,2,3]:
        return tslct
    else:
        print('Tidak ada perintah\n')
        return playerTurn(turn_counter,player_monster_arr,player_monster)

#mekanisme attack player
def playerHit(monster_arr : list,player_monster_arr : list, enemy_rng : int, player_monster : int, hitpoints : int, enemy_stat : list, level : int, attack : float) -> int:
        Pdmg=atkMech(attack,enemy_stat[1][1])
        hpl=dmgCalc(hitpoints,Pdmg)
        if hpl<=0:
            hpl=0
        print(f"""SCHWINKKK, {player_monster_arr[player_monster][l_m_type]} menyerang {monster_arr[enemy_rng][m_type]} !!!

Name      : {monster_arr[enemy_rng][m_type]}
ATK Power : {math.floor(enemy_stat[1][0])}
DEF Power : {math.floor(enemy_stat[1][1])}
HP        : {math.floor(hpl)}
Level     : {level}
""")
        return hpl,Pdmg

#mekanisme attack AI
def AITurn(turn_counter : int,monster_arr : list,player_monster_arr : list, enemy_rng : int, player_monster : int, player_stat : list, hitpoints : int, attack : float, buffs : list) -> int:
    Admg=atkMech(attack,player_stat[1][1])
    hpx=dmgCalc(hitpoints,Admg)
    if hpx<=0:
        hpx=0
    print(f"""============ TURN {turn_counter} ({monster_arr[enemy_rng][m_type]}) ============

SCHWINKKK, {monster_arr[enemy_rng][m_type]} menyerang {player_monster_arr[player_monster][l_m_type]} !!!

Name      : {player_monster_arr[player_monster][l_m_type]}
ATK Power : {math.floor(player_stat[1][0])*(1+buffs[1][0])}
DEF Power : {math.floor(player_stat[1][1])*(1+buffs[1][1])}
HP        : {math.floor(hpx)}
Level     : {player_monster_arr[player_monster][l_m_lv]}
""")
    return hpx,Admg

#tampilan potion menu
def potion_menu(player_inv : list, turn_counter : int,player_monster_arr : list,player_monster : int) -> int:
    if len(player_inv)==1:
        print("Anda tidak memiliki potion, silahkan beli terlebih dahulu di shop!\n")
        return playerTurn(turn_counter,player_monster_arr,player_monster)
    else:
        print("============ POTION LIST ============")
        i_counter=1
        for items in player_inv:
            if items[i_type]!='type':
                if items[i_type]=='Strength':
                    desc='Increases ATK Power by 15%'
                elif items[i_type]=='Resilience':
                    desc='Increases DEF Power by 10%'
                else: #items[i_type]=='Health':
                    desc='Restores Health by 20%'
                print(f'{i_counter}. {items[i_type]} Potion (Qty : {items[i_qty]}) - {desc}')
                i_counter+=1
        print(f'{i_counter}. Cancel\n')
        return i_counter

#selector dari potion menu
def potion_selector(i_counter : int) -> tuple[int,int]:
    pselect=int(input('Pilih perintah: '))
    print()
    if pselect not in range(1,i_counter+1):
        return potion_selector(i_counter)
    else:
        return pselect,i_counter

#penggunaan potion
def minum_potion(status : list, p_stat : list,p_hol : list, p_hp : list, player_inv : list, pselector : list, buffs : list) -> str:
    j=0
    pselect=pselector[0]
    for i in range(1,pselector[1]+1):
        j=i
    if pselector[0]==j:
        return 'gajadi'
    elif player_inv[pselect][i_type]=='Strength':
        if status[0]:
            print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
        elif player_inv[pselect][i_qty]=='0':
            print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n')
        else:
            p_hol[1][1],p_hol[1][0]=p_hol[1][1]*(1+0.15),p_hol[1][0]*(1+0.15)
            buffs[1][0]=0.15
            status[0]=True
            player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
            print('Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi monstermu dan gerakannya menjadi lebih cepat dan mematikan.\n')
        return 'jadi'
    elif player_inv[pselect][i_type]=='Resilience':
        if status[1]:
            print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
        elif player_inv[pselect][i_qty]=='0':
            print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n')
        else:
            p_stat[1][1]=p_stat[1][1]*(1+0.1)
            buffs[1][1]=0.1
            status[1]=True
            player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
            print('Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar monstermu yang membuatnya terlihat semakin tangguh dan sulit dilukai.\n')
        return 'jadi'
    elif player_inv[pselect][i_type]=='Health':
        if status[2]:
            print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
        elif player_inv[pselect][i_qty]=='0':
            print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n')
        else:
            status[2]=True
            player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
            temp_hp=p_hp*(1+0.2)
            if p_hp==p_stat[1][2]:
                print('HP mu sudah penuh, tidak perlu untuk memulihkan HP.\n')
            elif temp_hp>p_hp:
                temp_hp=p_stat[1][2]
                p_hp=temp_hp
                print('Kamu memulihkan HP monstermu.\n')
            else:
                p_hp=temp_hp
                print('Kamu memulihkan HP monstermu.\n')
        return 'jadi'

#ubah potion di inventory    
def ubah_potion(storage : list, userid : int, mobile_inv : list):
    for user_id in storage:
        if user_id[u_id]==userid:
            for item_type in mobile_inv:
                if user_id[1]==item_type[i_type]:
                    user_id[2]=item_type[i_qty]

#mekanisme perhitungan attack
def atkMech(atk : float,dfd : float) -> float:
    dmgCnt=abs(atk)*(1-abs((dfd/100)))
    abs(dmgCnt)
    return dmgCnt

#kalkulasi damage
def dmgCalc(hpx : int,damage : int) -> int:
    hp=int(hpx)
    hp-=damage
    return hp

def battle(username : str, role : str, coins : int,menu : str, stage : int, monsterdat : list, player_monster_arr : list, player_inv_arr : list, potion_check : list) -> tuple[str,str,int,bool]:
    #initiate buff array
    coin=int(coins)
    buffs=[['atk','def'],[0,0]]
    #initiate damage taken and dealt
    damage_taken=0
    damage_dealt=0
    #initial turn
    turn=1
    #fight = trues
    fight=True
    #win = false
    win=False
    #testing ground
    #initialize enemy monster rng, enemy level, and load enemy stats
    enum=monsterRNG(monsterdat)
    if menu=='ARENA':
        e_level=stage
    else:
        e_level=monsterlvRNG()
    e_stat=enemy_statloader(monsterdat,enum,e_level)
    #display enemy battle begins
    showMenu(e_stat,monsterdat,enum,e_level,menu)
    #player select monster
    monster_number=monSelect(player_monster_arr)
    #load player monster stats
    p_stat=player_statloader(player_monster_arr,monster_number)
    #load high and low atk stat for calculation
    e_hol=h_o_l(e_stat)
    p_hol=h_o_l(p_stat)
    #initialize temporary changeable variable untuk hp
    e_hp=e_stat[1][2]
    p_hp=p_stat[1][2]
    #show player monster
    showMnst(player_monster_arr,monster_number,username)
    statShow(player_monster_arr,monster_number,p_stat)
    display_playerTurn(turn,player_monster_arr,monster_number)
    command=playerTurn(turn,player_monster_arr,monster_number)
    while command!=3 and fight:
        if command==1:
            p_attack=attackRNG(p_hol[1][1],p_hol[1][0])
            # print(p_attack)
            (e_hp,Pdmg)=playerHit(monsterdat,player_monster_arr,enum,monster_number,e_hp,e_stat,e_level,p_attack)
            # print(Pdmg)
        if command==2:
            while True:
                potion_command=minum_potion(potion_check,p_stat,p_hol,p_hp,player_inv_arr,potion_selector(potion_menu(player_inv_arr,turn,player_monster_arr,monster_number)),buffs)
                if potion_command=='gajadi':
                    display_playerTurn(turn,player_monster_arr,monster_number)
                    command=playerTurn(turn,player_monster_arr,monster_number)
                    if command==1:
                        p_attack=attackRNG(p_hol[1][1],p_hol[1][0])
                        # print(p_attack)
                        (e_hp,Pdmg)=playerHit(monsterdat,player_monster_arr,enum,monster_number,e_hp,e_stat,e_level,p_attack)
                        # print(Pdmg)
                        break
                    elif command==3:
                        break
                else:
                    Pdmg=0 
                    break
        if command==3:
            damage_taken+= Admg
            damage_dealt+=Pdmg
            break
        if e_hp<=0:
            win=True
            break
        e_attack=attackRNG(e_hol[1][1],e_hol[1][0])
        # print(e_attack)
        (p_hp,Admg)=AITurn(turn,monsterdat,player_monster_arr,enum,monster_number,p_stat,p_hp,e_attack,buffs)
        # print(Admg)
        damage_taken+=Admg
        damage_dealt+=Pdmg
        if p_hp<=0:
            win=False
            break
        display_playerTurn(turn,player_monster_arr,monster_number)
        command=playerTurn(turn,player_monster_arr,monster_number)
        turn=turnCount(True,turn)
    if win:
        if stage==1:
            gained=30
        elif stage==2:
            gained=50
        elif stage==3:
            gained=90
        elif stage==4:
            gained=170
        elif stage==5:
            gained=330
        else : #stage==0
            gained=ocRNG(e_level)
        print(f'Kamu berhasil menang dan mendapatkan OC sebanyak {gained}.\n')
        coin+=gained
        if menu=='ARENA':
            return coin,win,damage_dealt,damage_taken,gained
        else:
            return username,role,coin
    elif command==3:
        gained=0
        print('Kamu mengakhiri pertandingan.\n')
        if menu=='ARENA':
            return coins,win,damage_dealt,damage_taken,gained
        else:
            return username,role,coin
    else:
        gained=0
        print(f'Sayang sekali, kamu telah dikalahkan oleh {monsterdat[enum][m_type]}.\n')
        if menu=='ARENA':
            return coins,win,damage_dealt,damage_taken,gained
        else:
            return username,role,coin