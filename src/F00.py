import time

def RNG(x, y):
    # Set konstanta
    a = 22695477
    c = 1
    m = 2 ** 31 
    seed = int(time.time_ns())

    random = 0
    if x == 1:
        for i in range(165 * 145):
            random = (a * i * seed + c) % m  # Implementasi LCG
        hasil = (random % (y - x + 1)) + x  # Supaya output ada di rentang nilai x sampai y
    elif x == 0:
        for i in range(165 * 145):
            random = (a * i * seed + c) % m  # Implementasi LCG
        hasil = (random % (y - x + 1)) + x  # Supaya output ada di rentang nilai x sampai y
    return hasil

