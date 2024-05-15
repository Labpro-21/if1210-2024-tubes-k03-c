import time

def RNG(x, y):
    # Set konstanta
    a = 22695477
    c = 1
    m = 2 ** 31 
    seed = int(time.time_ns())

    random = 0
    for i in range(50000):
        random = (a * i * seed + c) % m 
    hasil = (random % (y - x + 1)) + x  
    
    return hasil
