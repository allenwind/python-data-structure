def find_subarray_of_greate_sum(array):
    if not array:
        return None
    i = j = 0
    subarray_sum = 0
    greate_subarray_sum = 0
    for p in range(len(array)):
        if subarray_sum <= 0:
            subarray_sum = array[p]
            i = p
        else:
            subarray_sum += array[p]
        if subarray_sum > greate_subarray_sum:
            greate_subarray_sum = subarray_sum
            j = p
    return array[i:j+1], greate_subarray_sum

def find_greate_sum_of_subarray(array):
    if not array:
        return None
    subarray_sum = 0
    greate_subarray_sum = 0
    for i in range(len(array)):
        if subarray_sum <= 0:
            subarray_sum = array[i]
        else:
            subarray_sum += array[i]
        if subarray_sum > greate_subarray_sum:
            greate_subarray_sum = subarray_sum
    return greate_subarray_sum

def find_create_sum_of_subarray_recursively(array):
    if not array:
        return 
    subarray_sum = 0
    greate_subarray_sum = 0
    for i in range(len(array)):
        if i == 0 or subarray_sum <= 0:
            subarray_sum = array[i]
        elif subarray_sum > 0:
            subarray_sum += array[i]
        if subarray_sum > greate_subarray_sum:
            greate_subarray_sum = subarray_sum
    return greate_subarray_sum

def main():
    array = [1, -2, 3, 10, -4, 7, 2, -5]


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    main()
