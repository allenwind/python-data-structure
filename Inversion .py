def reverse_number(num):
    s = str(num)
    c = 0
    for i, n in enumerate(s):
        for j in range(i):
            if int(s[j]) > int(n):
                c += 1
    return c

def test():
    print(reverse_number(32514))

if __name__ == '__main__':
    test()
