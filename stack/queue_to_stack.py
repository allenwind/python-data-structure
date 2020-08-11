class Queue:

    def __init__(self):
        self._q = []

    def empty(self):
        return len(self._q) == 0

    def push(self, item):
        self._q.append(item)

    def get(self):
        item = self._q[0]
        del self._q[0]
        return item

class Stack:

    def __init__(self):
        self._q1 = Queue()
        self._q2 = Queue()
        self._top = None

    def empty(self):
        return self._q1.empty() and self._q1.empty()

    def push(self, item):
        self._q1.push(item)
        self._top = item

    def pop(self):
        if self._q1.empty():
            while not self._q2.empty():
                item = self._q2.get()
                if self._q2.empty():
                    return item
                else:
                    self._q1.push(item)
                    self._top = item
        else:
            while not self._q1.empty():
                item = self._q1.get()
                if self._q1.empty():
                    return item
                else:
                    self._q2.push(item)
                    self._top = item

    def top(self):
        if self.empty():
            return None
        return self._top
