# 第一题
# 思路
# 不难发现规律，假设给定数组的长度为length，那么最小数的索引为length-1，最大数的索引为0
# 次小数索引为length-2，次大数索引为1，依次....
# 因此，索引序列过程为：length-1, 0, length-2, 1, ...

def re_sorting(array):
    reverse = False
    length = len(array)
    index = 0
    while index <= length - 1:
        if not reverse:
            yield array[length-1]
            length -= 1
            reverse = True
        else:
            yield array[index]
            index += 1
            reverse = False
            

def solve(array):
    arr = []
    for v in re_sorting(array):
        arr.append(v)
    return arr

def testing():
    array = [7, 6, 5, 4, 3, 2, 1]
    result = solve(array)
    print(result)


# 另外还有通过数据结构的设计，可以依次访问最大、最小，然后删除最大最小，然后依次访问最大最小来实现
# 目标队列的输出，也就是使用红黑树或BST树可以解决

if __name__ == '__main__':
    testing()

        
