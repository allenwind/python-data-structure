#大数据的外部排序实现
#只写下大概框架，有时间具体实现

def read_data(path):
    pass

def save_data(path):
    pass

def sorting(data):
    pass

def bigdata_sorting(path):
    fd = open(path, 'r')

    path_set = []
    max_line = 1000

    #分块排序
    while True:
        loop = 0
        numbers = []
        while True:
            loop += 1
            numbers.append(fd.readline())
            if loop >= max_line:
                break

        numbers = sorting(numbers)
        filename = save_data(numbers)
        path_set.append(filename)

    #指针find min

    pass






