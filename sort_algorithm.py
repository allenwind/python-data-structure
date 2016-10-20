import random
#use for shuffle the list which use in sorting test.



def issorted(list_):
    return all([1 if list_[i]<=list_[i+1] else 0 for i in range(len(list_)-1)])

#or use lambda style.
#issorted = lambda list_: all([1 if list_[i]<=list_[i+1] else 0 for i in range(len(list_)-1)])
def exchange(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]

def select_sort(list_):
    length = len(list_)
    for i in range(length):
        for j in range(i+1, length):
            if list_[j] < list_[i]:
                min_ = j
            else:
                min_ = i
            list_[i], list_[min_] = list_[min_], list_[i]
    return list_
#具体分析：
#比较次数N^2/2
#交换次数N

def insert_sort(list_):
    length = len(list_)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if list_[j] < list_[j-1]:
                list_[j], list_[j-1] = list_[j-1], list_[j]
    return list_
#具体分析：
#

def shell_sort(list_):
    length = len(list_)
    h = 1
    while h < length//3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, length):
            for j in range(i, h+1, -h):
                if list_[j] < list_[j-h]:
                    list_[i], list_[j-h] = list_[j-h], list_[i]
        h = h // 3

    return list_

def sort_test(*funcs):
    list_ = list(range(1000))
    random.shuffle(list_)
    for func in funcs:
        sort_list = func(list_)
        if issorted(sort_list):
            print('algorithm {} pass the test'.format(func.__name__))
        else:
            print('algorithm {} not pass'.format(func.__name__))

if __name__ == '__main__':

    sort_test(select_sort, insert_sort, shell_sort)














    
