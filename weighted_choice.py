#带权选择
import bisect
import random

def weighted_choice(choices):

    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.uniform(0, total)
    i = bisect.bisect(cum_weights, x)
    return values[i]

#val1 -----
#val2 -
#val3 --
#then weighted_choice
