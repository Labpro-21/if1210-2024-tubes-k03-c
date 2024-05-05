def csv_read

def turnCount(cond):
    #kamus lokal
    #cond : bool
    #turn : int
    if cond:
        turn+=1
    return turn

def showMenu(monsta,monlist):
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

RAWRRR, Monster Zuko telah muncul !!!

Name      : Zuko
ATK Power : 20
DEF Power : 20
HP        : 100
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
    
def showMnst():
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

RAWRRR, Agent X mengeluarkan monster Pikachow !!!
""")
    
def statShow():
    print(f"""Name      : Pikachow
ATK Power : 25
DEF Power : 5
HP        : 120
Level     : 1""")
    
def turnMenu(turn_counter):
    print(f"""============ TURN {turn_counter} (Pikachow) ============
1. Attack
2. Use Potion
3. Quit""")
    tslct=int(input('Pilih perintah: '))
    if tslct == 1:


def atkMech(atk,dfd,buff_1,buff_2):
    atkCnt=atk*(1+buff_1)
    defCnt=dfd*(1+buff_2)
    dmgCnt=atkCnt*(1-defCnt)
    return dmgCnt

def dmgCalc(hp,damage):
    hp-=damage
    if hp%1!=0:
        return floor(hp)
    else:
        return hp
    
