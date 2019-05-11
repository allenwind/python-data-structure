import random
import string
import collections

import matplotlib.pyplot as plt

letters = string.ascii_letters

def strHash(string):
    R = 99
    M = 97
    hash = 0
    for i in string:
        hash = (R * hash + ord(i)) % M
    return hash

def test_strHash(max):
    result = []

    for _ in range(max):
        length = random.randint(1, 100)
        string = ''.join([random.choice(letters) for _ in range(length)])
        result.append(strHash(string))
    return collections.Counter(result)


if __name__ == '__main__':
    r = test_strHash(100000)
    x = r.keys()
    y = r.values()

    plt.bar(x, y)
    plt.show()


    
