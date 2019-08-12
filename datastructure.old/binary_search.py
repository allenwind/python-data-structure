def search(list, n):
    start = 0
    end = len(list)
    while start < end:
        mid = (start+end) // 2
        if n == list[mid]:
            return mid
        elif n < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1