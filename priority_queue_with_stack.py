import random

class Stack:
    def __init__(self):
        self._s = []
        self._n = 0

    def push(self, item):
        self._n += 1
        self._s.append(item)

    def pop(self):
        self._n -= 1
        return self._s.pop()

    def empty(self):
        return len(self._s) == 0

    def top(self):
        if self.empty():
            return None
        return self._s[-1]

    def __len__(self):
        return self._n

class StackWithMin:

    def __init__(self):
        self._common = Stack()
        self._min = Stack()

    def push(self, item):
        self._common.push(item)
        if self._min.empty():
            self._min.push(item)
        else:
            if self._min.top() >= item:
                self._min.push(item)
            else:
                self._min.push(self._min.top())

    def pop(self):
        self._min.pop()
        return self._common.pop()

    def min(self):
        return self._min.top()

    def __len__(self):
        return len(self._common)

class PriorityQueue:

    def __init__(self):
        self._q = StackWithMin()

    def push(self, item):
        self._q.push(item)

    def get(self):
        item = self._q.min()
        self._q.pop()
        return item

    def __len__(self):
        return len(self._q)

def main():
    queue = PriorityQueue()
    seq = random.sample(range(10), 10)
    for item in seq:
        queue.push(item)
    
    print(seq)
    while len(queue) != 0:
        print(queue.get())

if __name__ == '__main__':
    main()
