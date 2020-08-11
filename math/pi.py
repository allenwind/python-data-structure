import random
import math
import decimal

RAT = 4

def pi():
    
    Sq = 0
    Sh = 0
    m = 10000001
    for i in range(m):
        x, y = random.random(), random.random()
        if math.hypot(x-0.5, y-0.5) < 0.5:
            Sh += 1
        else:
            Sq += 1

    Sh = decimal.Decimal(str(Sh))
    m = decimal.Decimal(str(m))
    print(Sh)
    return Sh/m * RAT
        
