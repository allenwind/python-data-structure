# 迭代器在多线程下安全吗？

import time
import threading
import itertools

class Fib:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.b
        self.a, self.b = self.b, self.a + self.b
        return value

# 原理上，一样要迭代切片前的部分

def slice_test():
    fib = Fib()
    for i in itertools.islice(fib, 10, 20):
        print(i)

def task(fib):
    for i in fib:
        print(i, end='\n')

def main():
    fib = Fib()
    t1 = threading.Thread(target=task, args=(fib,))
    t2 = threading.Thread(target=task, args=(fib,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    slice_test()
    
    
