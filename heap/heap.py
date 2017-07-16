def sort(q):
    n = len(q)
    k = n // 2
    while k >= 1:
        k -= 1
        sink(q, k, n)
    while n > 1:
        n = n - 1
        exch(q, 1, n)
        sink(q, 1, n+1)

def sink(q, k, n):
    while 2*k < n:
        j = 2 * k
        if j < n and less(q, j, j+1):
            j += 1
        if not less(q, k, j):
            break
        exch(q, k, j)
        k = j

def less(q, i, j):
    return q[i-1] < q[j-1]

def exch(q, i, j):
    q[j-1], q[j-1] = q[j-1], q[i-1]

def test():
    import random
    q = [random.randint(1, 100) for _ in range(20)]
    print(q)
    sort(q)
    print(q)

if __name__ == '__main__':
    test()