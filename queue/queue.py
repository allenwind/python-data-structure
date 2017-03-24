class Full(Exception):
    pass

class Empty(Exception):
    pass


class Queue:
    
    def __init__(self, maxsize=0):
        pass

    def qsize(self):
        pass

    def is_empty(self):
        pass

    def full(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

    def clear(self):
        pass

class PriorityQueue(Queue):
    pass

class LifoQueue(Queue):
    pass


class StackByQueue:

    def __init__(self):
        self._queue1 = Queue()
        self._queue2 = Queue()
        self._left_side = True #mean 1
        self._top = None

    def is_empty(self):
        return self._queue1.is_empty() and self._queue2.is_empty()

    def push(self, e):
        self._top = e
        if self._left_side:
            self._queue1.put(e)
        else:
            self._queue2.put(e)

    def pop(self):
        top = None
        if self._left_side:
            e = self._queue1.get()
            top = e
            while self._queue1.is_empty():
                self._queue2.put(e)
                e = self._queue1.get()
            self._left_side = False
            self._top = top
            return e
        else:
            e = self._queue2.get()
            top = e
            while self._queue2.is_empty():
                self._queue1.put(e)
                e = self._queue2.get()
            self._top = top
            return e

    def top(self):
        return self._top

        


