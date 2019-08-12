def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]

def test():
    r = lcp('abcdef', 'abc')
    print(r)

if __name__ == '__main__':
    test()
