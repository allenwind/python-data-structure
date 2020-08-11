import functools

# 输出排序后最小的字符串序列，问题33

def cmp(v1, v2):
    v1 = str(v1)
    v2 = str(v2)
    return int(v1+v2) - int(v2+v1)

def min_string_integer(values):
    values = sorted(values, key=functools.cmp_to_key(cmp))
    return values

def test():
    values = [3, 32, 321]
    v = min_string_integer(values)
    print(v)

if __name__ == '__main__':
    test()
    
