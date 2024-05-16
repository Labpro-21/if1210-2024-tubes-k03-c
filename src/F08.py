import operateCSV, F00, math, testloader

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

monster_arr=operateCSV.baca_csv(r'data\monster.csv')

potion_check=[False,False,False]

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
    hol=[['high','low'],[(math.floor(loaded_stat[1][0]*(1+(30/100)))),(math.floor(loaded_stat[1][0]*(1-(30/100))))]]
    return hol

#menghitung turn
def turnCount(cond : bool,turn : int) -> int:
    if cond:
        turn+=1
    return turn

#menentukan rng monster lawan
def monsterRNG() -> int:
    return F00.RNG(1,10)

#menentukan rng level monster lawan
def monsterlvRNG() -> int:
    chance=F00.RNG(1,1000001)
    if chance<600000:
        r_lv=1
    elif chance<800000:
        r_lv=2
    elif chance<900000:
        r_lv=3
    elif chance<999999:
        r_lv=4
    else: #chance==1000000
        r_lv=5
    return r_lv
    
        

#menentukan rng attack
def attackRNG(low : int,high : int) -> int:
    return F00.RNG(low,high)

#menentukan rng OC
def ocRNG() -> int:
    return F00.RNG(5,500)

#menampilkan musuh
def showMenu(loaded_stat : list, list_monster : list, enemy_rng : int, level : int, menu : str):
    #kamus lokal
    print(f"""{menu}
                       
           _/\----/\   
          /         \     /\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__

RAWRRR, Monster {list_monster[enemy_rng][m_type]} telah muncul !!!

Name      : {list_monster[enemy_rng][m_type]}
ATK Power : {math.floor(loaded_stat[1][0])}
DEF Power : {math.floor(loaded_stat[1][1])}
HP        : {math.floor(loaded_stat[1][2])}
Level     : {level}
""")

def monSelect(player_monster_arr : list) -> int:
    print("============ MONSTER LIST ============")
    m_count=1
    for monster in player_monster_arr:
        if monster[l_m_type]!='type':
            print(f'{m_count}. {monster[l_m_type]}')
            m_count+=1
    slct=int(input('Pilih monster untuk bertarung: '))
    if slct in range(1,m_count):
        return slct      
    else:
        print('Pilihan nomor tidak tersedia!')
        return monSelect(player_monster_arr)
    
def showMnst(player_monster_arr : list,player_monster : int, username : str):
    print(f"""
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

RAWRRR, Agent {username} mengeluarkan monster {player_monster_arr[player_monster][l_m_type]} !!!
""")
      
def statShow(player_monster_arr : list,player_monster : int, loaded_stat : list):
    print(f"""Name      : {player_monster_arr[player_monster][l_m_type]}
ATK Power : {math.floor(loaded_stat[1][0])}
DEF Power : {math.floor(loaded_stat[1][1])}
HP        : {math.floor(loaded_stat[1][2])}
Level     : {player_monster_arr[player_monster][l_m_lv]}""")
    
def display_playerTurn(turn_counter : int,player_monster_arr : list,player_monster : int):
    print(f"""============ TURN {turn_counter} ({player_monster_arr[player_monster][l_m_type]}) ============
1. Attack
2. Use Potion
3. Quit
          """)
    
def playerTurn(turn_counter : int,player_monster_arr : list,player_monster : int) -> int:
    tslct=int(input('Pilih perintah: '))
    if tslct in [1,2,3]:
        return tslct
    else:
        print('Tidak ada perintah')
        return playerTurn(turn_counter,player_monster_arr,player_monster)

def playerHit(monster_arr : list,player_monster_arr : list, enemy_rng : int, player_monster : int, hitpoints : int, enemy_stat : list, level : int, attack : float) -> int:
        hpl=dmgCalc(hitpoints,atkMech(attack,enemy_stat[1][1]))
        if hpl<=0:
            hpl=0
        print(f"""SCHWINKKK, {player_monster_arr[player_monster][l_m_type]} menyerang {monster_arr[enemy_rng][m_type]} !!!

Name      : {monster_arr[enemy_rng][m_type]}
ATK Power : {math.floor(enemy_stat[1][0])}
DEF Power : {math.floor(enemy_stat[1][1])}
HP        : {math.floor(hpl)}
Level     : {level}
""")
        return hpl

def AITurn(turn_counter : int,monster_arr : list,player_monster_arr : list, enemy_rng : int, player_monster : int, player_stat : list, hitpoints : int, attack : float, buffs : list) -> int:
    hpx=dmgCalc(hitpoints,atkMech(attack,player_stat[1][1]))
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
    return hpx

def potion_menu(player_inv : list, turn_counter : int,player_monster_arr : list,player_monster : int) -> int:
    if len(player_inv)==1:
        print("Anda tidak memiliki potion, silahkan beli terlebih dahulu di shop!")
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
        i_counter+=1
        print(f'{i_counter}. Cancel')
        return i_counter

def potion_selector(i_counter : int) -> int:
    pselect=int(input('Pilih perintah: '))
    if pselect not in range(1,i_counter+1):
        return potion_selector(i_counter)
    else:
        return pselect

def minum_potion(status : list, p_stat : list,p_hol : list, p_hp : list, player_inv : list, pselect : int, buffs : list):
    if player_inv[pselect][i_type]=='Strength':
            if status[0]:
                print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
            elif player_inv[pselect][i_qty]=='0':
                print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else:
                p_hol[1][1],p_hol[1][0]=p_hol[1][1]*(1+0.15),p_hol[1][0]*(1+0.15)
                buffs[1][0]=0.15
                status[0]=True
                player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
                print('Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi monstermu dan gerakannya menjadi lebih cepat dan mematikan.')
    elif player_inv[pselect][i_type]=='Resilience':
            if status[1]:
                print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
            elif player_inv[pselect][i_qty]=='0':
                print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else:
                p_stat[1][1]=p_stat[1][1]*(1+0.1)
                buffs[1][1]=0.1
                status[1]=True
                player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
                print('Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar monstermu yang membuatnya terlihat semakin tangguh dan sulit dilukai.')
    elif player_inv[pselect][i_type]=='Health':
            if status[2]:
                print(f'Monstermu menolak ramuan yang kamu berikan seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
            elif player_inv[pselect][i_qty]=='0':
                print(f'Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else:
                status[2]=True
                player_inv[pselect][i_qty]=str(int(player_inv[pselect][i_qty])-1)
                temp_hp=p_hp*(1+0.2)
                if p_hp==p_stat[1][2]:
                    print('HP mu sudah penuh, tidak perlu untuk memulihkan HP.')
                elif temp_hp>p_hp:
                    temp_hp=p_stat[1][2]
                    p_hp=temp_hp
                    print('Kamu memulihkan HP monstermu.')
                else:
                    p_hp=temp_hp
                    print('Kamu memulihkan HP monstermu.')



def atkMech(atk : float,dfd : float) -> float:
    dmgCnt=atk*(1-(dfd/100))
    return dmgCnt

def dmgCalc(hpx : int,damage : int) -> int:
    hp=int(hpx)
    hp-=damage
    return hp
    
def battle(username : str, role : str, coin : int, userdat : list, menu : str, stage : int) -> tuple[str,str,int]:
    #find uid
    userid=testloader.get_uid(userdat,username)
    #load datas
    player_monster_arr=(testloader.monster_inventory(testloader.monster,testloader.filter_monster(testloader.monstinv,userid)))
    player_inv_arr=(testloader.filter_item(testloader.storage,userid))
    #initiate buff array
    buffs=[['atk','def'],[0,0]]
    print(player_inv_arr)
    #initial turn
    turn=1
    #fight = trues
    fight=True
    #win = false
    win=False
    #testing ground
    #initialize enemy monster rng, enemy level, and load enemy stats
    enum=monsterRNG()
    if menu=='ARENA':
        e_level=stage
    else:
        e_level=monsterlvRNG()
    e_stat=enemy_statloader(monster_arr,enum,e_level)
    #display enemy battle begins
    showMenu(e_stat,monster_arr,enum,e_level,menu)
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
            e_hp=playerHit(monster_arr,player_monster_arr,enum,monster_number,e_hp,e_stat,e_level,p_attack)
        if command==2:
            minum_potion(potion_check,p_stat,p_hol,p_hp,player_inv_arr,potion_selector(potion_menu(player_inv_arr,turn,player_monster_arr,monster_number)),buffs)
        if e_hp<=0:
            win=True
            break
        e_attack=attackRNG(e_hol[1][1],e_hol[1][0])
        p_hp=AITurn(turn,monster_arr,player_monster_arr,enum,monster_number,p_stat,p_hp,e_attack,buffs)
        if p_hp<=0:
            win=False
            break
        display_playerTurn(turn,player_monster_arr,monster_number)
        command=playerTurn(turn,player_monster_arr,monster_number)
        turn=turnCount(True,turn)
    if win:
        coin+=ocRNG()
        print(f'Kamu berhasil menang dan mendapatkan OC sebanyak {coin}')
        return username,role,coin
    elif command==3:
        print('Kamu berhasil kabur.')
        return username,role,coin,win
    else:
        print(f'Sayang sekali, kamu telah dikalahkan oleh {monster_arr[enum][m_type]}')
        return username,role,coin,win

battle('Agen_P','agent',0,testloader.userdat, 'BATTLE', 1)