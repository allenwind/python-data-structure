def number_of_sequence(sequence, number):
    n = len(sequence)

    i = 0
    for item in sequence:
        if item == number:
            break
        i += 1

    j = 0
    for item in reversed(sequence):
        if item == number:
            break
        j += 1
    return n - i - j

def get_first_k(sequence, n, k, start, end):
    if start > end:
        return -1
    middle_index = (start+end) // 2
    middle_number = sequence[middle_index]

    if middle_number == k:
        if (middle_index > 0 and sequence[middle_index-1] != k) or middle_index == 0:
            return middle_index
        else:
            end = middle_index - 1
    elif middle_number > k:
        end = middle_index - 1
    else:
        start = middle_index + 1
    return get_first_k(sequence, n, k, start, end)

def get_last_k(sequence, n, k, start, end):
    if start > end:
        return -1
    middle_index = (start+end) // 2
    middle_number = sequence[middle_index]

    if middle_number == k:
        if (middle_index < n - 1 and sequence[middle_index+1] != k) or middle_index == n-1:
            return middle_index
        else:
            start = middle_index + 1
    elif middle_number < k:
        start = middle_index + 1
    else:
        end = middle_index - 1
    return get_last_k(sequence, n, k, start, end)


def get_number_of_k(sequence, k):
    if not sequence:
        return 0
    n = len(sequence)
    first = get_first_k(sequence, n, k, 0, n-1)
    end = get_last_k(sequence, n, k, 0, n-1)

    print(first, end)
    if first > -1 and end > -1:
        return end - first + 1
    else:
        return 0

def main():
    import random
    seq = [random.choice(range(100)) for _ in range(2000)]
    seq.sort()
    print(seq)
    k = random.choice(seq)
    n = get_number_of_k(seq, k)
    print(n)
    print(seq.count(k))

if __name__ == '__main__':
    main()