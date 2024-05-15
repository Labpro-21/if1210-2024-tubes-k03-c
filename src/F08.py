import glbfunc
import random
import math

monster_arr=glbfunc.csv_reader('monster.csv')
monsterl=glbfunc.csv_parser(monster_arr,';',6,5)

item_arr=glbfunc.csv_reader('item_inventory.csv')
iteml=glbfunc.csv_parser(item_arr,';',6,3)

def hploader(monsterl,p_mon,e_mon):
    loadedhp=[['enemy hp','player hp'],[int(monsterl[e_mon][4]),int(monsterl[p_mon][4])]]
    return loadedhp

def turnCount(cond,turn):
    #kamus lokal
    #cond : bool
    #turn : int
    if cond:
        turn+=1
    return turn

def monsterRNG():
    return random.randint(1,5)

def showMenu(monsta,e_num):
    #kamus lokal
    print(f"""BATTLE
                       
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

RAWRRR, Monster {monsta[e_num][1]} telah muncul !!!

Name      : {monsta[e_num][1]}
ATK Power : {monsta[e_num][2]}
DEF Power : {monsta[e_num][3]}
HP        : {monsta[e_num][4]}
Level     : 1

============ MONSTER LIST ============
1. Chacha
2. Pikachow
3. Zeze
""")

def monSelect():
    slct=int(input('Pilih monster untuk bertarung: '))
    if slct not in [1,2,3]:
        print('Pilihan nomor tidak tersedia!')
        monSelect()
    else:
        return slct
    
def showMnst(monster,monnum):
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

RAWRRR, Agent X mengeluarkan monster {monster[monnum][1]} !!!
""")
    
def statShow(monster,monnumb):
    print(f"""Name      : {monster[monnumb][1]}
ATK Power : {monster[monnumb][2]}
DEF Power : {monster[monnumb][3]}
HP        : {monster[monnumb][4]}
Level     : 1""")
    
def playerTurn(turn_counter,monsterP,mnumb):
    print(f"""============ TURN {turn_counter} ({monsterP[mnumb][1]}) ============
1. Attack
2. Use Potion
3. Quit""")
    tslct=int(input('Pilih perintah: '))
    if tslct not in [1,2,3]:
        print('Tidak ada perintah')
        playerTurn(turn_counter,monsterP,mnumb)
    else:
        return tslct

def playerHit(monsterE,monsterP,mnumb,e_numb,hp):
        hpl=dmgCalc(hp,atkMech(monsterP[mnumb][2],monsterE[e_numb][3],0,0))
        if hpl<=0:
            hpl=0
        print(f"""SCHWINKKK, {monsterP[mnumb][1]} menyerang {monsterE[e_numb][1]} !!!

Name      : {monsterE[e_numb][1]}
ATK Power : {monsterE[e_numb][2]}
DEF Power : {monsterE[e_numb][3]}
HP        : {hpl}
Level     : 1
""")
        return hpl

def AITurn(turn_counter,monsterE,monsterP,mnumb,e_numb,hp):
    hpx=dmgCalc(hp,atkMech(monsterE[e_numb][2],monsterP[mnumb][3],0,0))
    if hpx<=0:
        hpx=0
    print(f"""============ TURN {turn_counter} ({monsterE[e_numb][1]}) ============

SCHWINKKK, {monsterE[e_numb][1]} menyerang {monsterP[mnumb][1]} !!!

Name      : {monsterP[mnumb][1]}
ATK Power : {monsterP[mnumb][2]}
DEF Power : {monsterP[mnumb][3]}
HP        : {hpx}
Level     : 1
""")
    return hpx

def atkMech(atk,dfd,buff_1,buff_2):
    atkCnt=int(atk)*(1+(buff_1/100))
    defCnt=int(dfd)*(1+(buff_2/100))
    dmgCnt=atkCnt*(1-(defCnt/100))
    return dmgCnt

def dmgCalc(hpx,damage):
    hp=int(hpx)
    hp-=damage
    if hp%1!=0:
        return math.floor(hp)
    else:
        return hp
    
def battle():
    #initial turn
    turn=1
    #fight = true
    fight=True
    #win = false
    win=False
    #testing ground
    enum=monsterRNG()
    showMenu(monsterl,enum)
    monster_number=monSelect()
    #load hp
    temphp=hploader(monsterl,monster_number,enum)
    enemyhp=temphp[1][0]
    playerhp=temphp[1][1]
    showMnst(monsterl,monster_number)
    statShow(monsterl,monster_number)
    command=playerTurn(turn,monsterl,monster_number)
    while command!=3 and fight:
        if command==1:
            enemyhp=playerHit(monsterl,monsterl,monster_number,enum,enemyhp)
        if command==2:
            print('belom ada')
        if enemyhp<=0:
            win=True
            break
        playerhp=AITurn(turn,monsterl,monsterl,monster_number,enum,playerhp)
        if playerhp<=0:
            win=False
            break
        command=playerTurn(turn,monsterl,monster_number)
        turn=turnCount(True,turn)
    if win:
        print('Menang yey')
    elif command==3:
        print('cih kabur')
    else:
        print('Yah Kalah')


battle()