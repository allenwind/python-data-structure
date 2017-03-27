#找出给定序列中的最长连续子序列，返回该序列以及长度 T(n)

def max_length_sequence(lst):
    last_before = 0
    last_after = 0
    last_length = 0
    before = 0
    middle = 0
    after = 1
    length = len(lst)
    for index in range(length-1):
        middle_number = lst[middle]
        after_number =  lst[after]
        if after_number-middle_number == 1:
            after += 1
            middle += 1
        else:
            if after - before > last_length:
                last_length = after - before
                #last_before = before
                #last_after = after
            else:
                last_before = after
                last_after = after
                after += 1
    return lst[last_before:last_after]

if __name__ == '__main__':
    test = [4, 3, 1, 5, 7, 8, 9, 3, 6, 2]
    result = max_length_sequence(test)
    print(result)

