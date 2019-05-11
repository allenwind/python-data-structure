import sys
import functools
import numpy

sys.setrecursionlimit(10000)

# 1. 递归
# 2. 递归+备忘录
# 3. 循环
# 4. 数学定理
# 5. 尾递归

def fib(n):
    if n < 0:
        raise Exception("n must be zero or positive")
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

def cache(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(n):
        if n in _cache:
            return _cache[n]
        r = func(n)
        _cache[n] = r
        return r 
    return wrapper

@cache
def fib_with_cache(n):
    if n < 0:
        raise Exception("n must zero or positive")
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

@functools.lur_cache(maxsize=2000)
def fib_with_lru_cache(n):
    if n < 0:
        raise Exception("n must zero or positive")
    if n in (0, 1):
        return n 
    return fib(n-1) + fib(n-2)

def fib_with_loop(n):
    if n < 0:
        raise Exception("n must be zero or positive")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b

def fib_with_numpy(n):
    if n <= 0:
        return 1
    c = _array = numpy.array([[1, 1], [1, 0]])
    for _ in range(n-1):
        c = c @ _array 
    return c[0][0]

def _tail(n, c, a, b):
    if c == n-1:
        return b
    c += 1
    a, b = b, a + b
    return _tail(n, c, a, b)

def fib_tail(n):
    if n < 0:
        raise Exception("n must be zero or positive")
    if n in (0, 1):
        return 1
    c = 0
    a = b = 1
    return _tail(n, c, a, b)





