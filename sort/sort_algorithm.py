import random
#use for shuffle the list which use in sorting test.



def issorted(seq):
    return all([1 if seq[i]<=seq[i+1] else 0 for i in range(len(seq)-1)])

#or use lambda style.
#issorted = lambda seq: all([1 if seq[i]<=seq[i+1] else 0 for i in range(len(seq)-1)])
def exchange(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]

def select_sort(seq):
    length = len(seq)
    for i in range(length):
        for j in range(i+1, length):
            if seq[j] < seq[i]:
                min_ = j
            else:
                min_ = i
            seq[i], seq[min_] = seq[min_], seq[i]
    return seq
#具体分析：
#比较次数N^2/2
#交换次数N

def insert_sort(seq):
    length = len(seq)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq
#具体分析：
#

def shell_sort(seq):
    length = len(seq)
    h = 1
    while h < length//3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, length):
            for j in range(i, h+1, -h):
                if seq[j] < seq[j-h]:
                    seq[i], seq[j-h] = seq[j-h], seq[i]
        h = h // 3

    return seq

def bubble_sort(seq):
    length = len(seq)
    for i in range(length-1):
        for j in range(length-1-i):
            if seq[j] > seq[j+1]:
                exchange(seq, j, j+1)
    return seq

def radix_sort(seq):
    pass

def merge_sort(seq): #并归排序
    pass

def merge(left, right):
    pass


def heap_sort(seq):
    pass

def quick_sort(seq):
    #recursive method
    
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0] #基准
        return quick_sort([x for x in seq[1:] if x < pivot]) + \
              [pivot] + \
              quick_sort([x for x in seq[1:] if x >= pivot])

def quick_sort2(seq): #不用列表推导的方法
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort2(left) + [pivot] + sort(right)

#O(nlogn)

def sort_test(*funcs):
    seq = list(range(1000))
    random.shuffle(seq)
    for func in funcs:
        sort_list = func(seq)
        if issorted(sort_list):
            print('algorithm {} pass the test'.format(func.__name__))
        else:
            print('algorithm {} not pass'.format(func.__name__))

if __name__ == '__main__':
    pass

    #sort_test(select_sort, insert_sort, shell_sort, quick_sort)
