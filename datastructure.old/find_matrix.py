def find_number(matrix, number):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    return _find(matrix, rows, cols, number)

def _find(matrix, rows, cols, number):
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == number:
            return True
        elif matrix[row][col] > number:
            col -= 1
        else:
            row += 1
    return False

def testing():
    matrix = [[2, 4, 6, 8], [3, 7, 9, 16], [12, 13, 14, 19]]
    n = 5
    print(find_number(matrix, n))

    n = 6
    print(find_number(matrix, n))

if __name__ == '__main__':
    testing()
