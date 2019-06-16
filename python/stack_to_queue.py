class Stack:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._q.pop()

    def empty(self):
        return len(self._q) == 0

    def top(self):
        return self._q[-1]

class Queue:

    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()

    def put(self, item):
        self._s1.push(item)
        
    def get(self):
        if self._s2.empty():
            while not self._s1.empty():
                item = self._s1.pop()
                self._s2.push(item)
        if self._s2.empty():
            return None
        return self._s2.pop()

    def length(self):
        return len(self._s1._q) + len(self._s2._q)

def test():
    q = Queue()
    for i in range(10):
        q.put(i)

    while q.length() != 0:
        print(q.get())




'''
abc
---

---
cb-

d--
cb-

de-
cb-
'''