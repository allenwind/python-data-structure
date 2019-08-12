import functools
from collections import OrderedDict

class LRUCache:

    def __init__(self, size=100):
        self._size = size
        self._od = OrderedDict()

    def move_to_tail(self, key):
        self._od.move_to_end(key, last=True)

    def get(self, key):
        value = self._od.get(key, None)
        if value is not None:
            self.move_to_tail(key)
            return value

    def set(self, key, value):
        temp = self._od.get(key, None)
        if temp is not None:
            self._od[key] = value
            self.move_to_tail(key)
            return
            
        if self._size == len(self._od):
            # first_key = next(iter(self._od.keys())) # the oldest key
            # self._od.pop(first_key)
            self._od.popitem(last=False)
        self._od[key] = value
        self.move_to_tail(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return key in self._od

    def __repr__(self):
        return str(self._od)

def lru_cache(maxsize=100):
    _cache = LRUCache(maxsize)
    def cache(func):
        @functools.wraps(func)
        def wrapper(key):
            if key in _cache:
                return _cache[key]
            value = func(key)
            _cache[key] = value
            return value
        return wrapper
    return cache

def fib(n):
    if n < 0:
        raise ValueError("n must be zero or positive")
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=1000)
def fib_with_lru(n):
    if n < 0:
        raise ValueError("n must be zero or positive")
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)   

import time

def main():
    start = time.time()
    fib(33)
    end = time.time()
    print(fib.__name__, 'elapsed time is {}'.format(end-start))
    start = time.time()
    fib_with_lru(33)
    end = time.time()
    print(fib_with_lru.__name__, 'elapsed time is {}'.format(end-start))

if __name__ == '__main__':
    main()








    
        
