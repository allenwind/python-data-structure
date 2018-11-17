import time
import random

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]

# 插入排序
def insert_sort(l):
    # 遍历所有元素
    for i in range(1, len(l)):
        # 每个元素与前面的元素对比
        # 如果前面元素较大就交互
        for j in range(i-1, -1, -1):
            if l[j] > l[j+1]:
                swap(l, j, j+1)
    return l

# 希尔排序
def shell_sort(l):
    pass

# 选择排序
def select_sort(l):
    for i in range(len(l)):
        mininum = l[i]
        for j in range(i+1, len(l)):
            if l[j] < mininum:
                l[j], mininum = mininum, l[j]
        # 每次找到最小的放到前面
        l[i] = mininum
    return l

def stack_sort(l):
    pass

def bubble_sort(l):
    pass

def quick_sort_(l, start, end):
    if start < end:
        i, j, pivot = start, end, l[start]
        while i < j:
            while i < j and l[j] > pivot:
                j = j - 1
            if i < j:
                l[i] = l[j]
                i += 1

            while i < j and l[i] < pivot:
                i += 1
            if i < j:
                l[j] = l[i]
                j = j - 1
        l[i] = pivot
        quick_sort_(l, start, i-1)
        quick_sort_(l, i+1, end)
    

# 快速排序
def quick_sort(l):
    random.shuffle(l)
    start = 0
    end = len(l) - 1
    _quick(l, start, end)

def _quick(l, lo, hi):
    if lo >= hi:
        return
    j = _partition(l, lo, hi)
    _quick(l, lo, j-1)
    _quick(l, j+1, h1)

def _partition(l, start, end):
    i = start
    j = end + 1
    v = l[start]
    while True:
        while l[i+1] < v:
            i += 1
            if i == end:
                break
        while v < l[j-1]:
            j -= 1
            if j == start:
                break
        swap(l, i, j)
    swap(l, start, j)
    return j
        

def merge_sort(l):
    pass

def radix_sort(l):
    pass
