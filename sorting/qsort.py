import random

def qsort(a):
    random.shuffle(a)
    sort(a, 0, len(a)-1)

def sort(a, lo, hi):
    if hi <= lo:
        return
    j = partition(a, lo, hi)
    sort(a, lo, j-1)
    sort(a, j+1, hi)

def partition(a, lo, hi):
    i = lo
    j = hi + 1
    v = a[lo]
    while True:
        while True:
            i += 1
            if a[i] >= v:
                break
            if i == hi:
                break
        while True:
            j -= 1
            if v >= a[j]:
                break
            if j == lo:
                break
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[lo], a[j] = a[j], a[lo]
    return j