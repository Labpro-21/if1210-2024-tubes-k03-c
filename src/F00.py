import time

def RNG(x,y):
    # Set konstanta
    a = 22695477
    c = 1
    m = 2 ** 31
    seed = int(time.time_ns())

    random = 0
    if x == 1 :
        for i in range (165*145):
            random += (a *i* seed + c) % m
        hasil = (random % y) + x
    elif x == 0 :
        for i in range (165*145):
            random += (a *i* seed + c) % m
        hasil = (random % y+1) + x
    return hasil