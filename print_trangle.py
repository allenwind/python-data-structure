

def refine(result, length=30):
    string = ''.join([str(i) for i in result]).center(length)
    print(string)

def count(result):
    length = len(result)
    r = []
    for i in range(1, length):
        r.append(result[i-1]+result[i])
    return r


def print_result(deep):
    result = [1]
    loop = 0
    refine(result)
    while True:
        result = [1] + result + [1]
        refine(result)
        result = count(result)
        loop += 1
        if loop == deep:
            break
        

