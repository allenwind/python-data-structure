from common import Stack

# 1. 带min的栈
# 2. 带max的栈
# 3. 带min、max的栈

class StackWithMin:
    
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def push(self, item):
        if self.empty():
            self._stack1.push(item)
            self._stack2.push(item)
            return
        self._stack1.push(item)
        if self._stack2.top() is None:
            self._stack2.push(item)
        elif self._stack2.top() > item:
            self._stack2.push(item)
        else:
            self._stack2.push(self._stack2.top())

    def pop(self):
        if self._stack1.empty():
            return None
        self._stack2.pop()
        return self._stack1.pop()

    def min(self):
        return self._stack2.top()

    def empty(self):
        return self._stack1.empty()

    def top(self):
        return self._stack1.top()

    def __len__(self):
        return len(self._stack1)

class StackWithMax(StackWithMin):

    def push(self, item):
        self._stack1.push(item)
        if self._stack2.top() is None:
            self._stack2.push(item)
        elif self._stack2.top() > item:
            self._stack2.push(self._stack2.top())
        else:
            self._stack2.push(item)

    def max(self):
        return self._stack2.top()

class StackWithMinAndMax:
    
    def __init__(self):
        self._stack = Stack()
        self._min = Stack()
        self._max = Stack()

    def empty(self):
        return self._stack.empty()

    def __len__(self):
        return len(self._stack)

    def top(self):
        return self._stack.top()

    def push(self, item):
        if self.empty():
            self._stack.push(item)
            self._min.push(item)
            self._max.push(item)
            return
        self._stack.push(item)
        if self._min.top() > item:
            self._min.push(item)
        else:
            self._min.push(self._min.top())
        if self._max.top() > item:
            self._max.push(self._max.top())
        else:
            self._max.push(item)

    def max(self):
        return self._max.top()

    def min(self):
        return self._min.top()

    def pop(self):
        if self.empty():
            return None
        self._min.pop()
        self._max.pop()
        return self._stack.pop()
