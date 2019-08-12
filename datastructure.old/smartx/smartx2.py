# 第二题
# 思路，其实就是二分查找的二维运用

# 测试使用的数据


matrix = [2, 4, 6, 8, 3, 7, 9, 16, 12, 13, 14, 19]

def find_number(matrix, number):
    #rows = len(matrix) - 1
    #cols = len(matrix[0]) - 1
    rows = 3
    cols = 4
    return _find(matrix, rows, cols, number)

def _find(matrix, rows, cols, number):
    if rows > 0 and cols > 0:
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if (matrix[row * cols + col] == number):
                return True
            elif matrix[row * cols + col] > number:
                col -= 1
            else:
                row += 1
    return False

def testing():
    number = 5
    r = find_number(matrix, number)
    print(r)

    number = 6
    r = find_number(matrix, number)
    print(r)

if __name__ == '__main__':
    testing()
            
