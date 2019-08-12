def string_to_binary(string):
    u = string.encode('utf-8')
    r = []
    for i in u:
        r.append(bin(i)[2:])
    return ''.join(r)

def integer_to_binary(integer):
    pass
