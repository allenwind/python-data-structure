from common import Stack, Queue

# 1. 两个栈实现队列
# 2. 两个队列实现栈

class QueueWithStack:

    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def push(self, item):
        self._stack1.push(item)

    def pop(self):
        if not self._stack2.empty():
            return self._stack2.pop()
        if self._stack1.empty():
            return None
        while not self._stack1.empty():
            item = self._stack1.pop()
            self._stack2.push(item)
        return self._stack2.pop()

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def emtpy(self):
        return self._stack1.empty() and self._stack2.empty()

class StackWithQueue:

    def __init__(self):
        self._queue1 = Queue()
        self._queue2 = Queue()
        self._top = None

    def empty(self):
        return self._queue1.empty() and self._queue2.empty()

    def push(self, item):
        self._queue1.push(item)
        self._top = item

    def pop(self):
        if self.empty():
            return None
        if self._queue1.empty():
            while len(self._queue2) != 1:
                item = self._queue2.pop()
                self._queue1.push(item)
                self._top = item
            return self._queue2.pop()
        else:
            while len(self._queue1) != 1:
                item = self._queue1.pop()
                self._queue2.push(item)
                self._top = item
            return self._queue1.pop()

    def __len__(self):
        return len(self._queue1) + len(self._queue2)

    def top(self):
        if self.empty():
            return None
        return self._top



        
