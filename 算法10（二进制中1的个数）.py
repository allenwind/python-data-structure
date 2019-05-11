def number_of_one(n):
    c = 0
    while n:
        n = (n-1) & n
        c += 1
    return c

def number_of_one_with_bin(n):
    n = bin(n)[2:]
    c = 0
    for i in n:
        if i == '1':
            c += 1
    return c