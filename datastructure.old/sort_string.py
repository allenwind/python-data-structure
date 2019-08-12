def _permutation(s, r):
    if len(s) == 1:
        r.append(s)
        return r
    for i in _permutation(s[1:], r):
        r.append(i+s[0])
        r.append(s[0]+i)

def sort_string(s):
    if not s:
        return None
    r = []
    _permutation(s, r)
    return r

def permutation(s):
    if not s:
        return None
    _permutaion()

def main():
    r = sort_string('abc')
    print(r)

if __name__ == '__main__':
    main()