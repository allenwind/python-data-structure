def find_unique_number(seq):
    data = {}
    for item in seq:
        if item not in data:
            data[item] = 1
        else:
            data[item] += 1

    for item in seq:
        if data[item] == 1:
            return item

if __name__ == '__main__':
    import random
    seq = [random.choice(range(10)) for _ in range(20)]
    r = find_unique_number(seq)
    print(seq)
    print(r)

