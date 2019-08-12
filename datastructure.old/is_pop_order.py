class Stack:

    def __init__(self):
        self._s = []

    def push(self, item):
        self._s.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._s.pop()

    def empty(self):
        return len(self._s) == 0

    def top(self):
        if self.empty():
            return None
        self._s[-1]

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkStack:

    def __init__(self):
        self._top = None

    def empty(self):
        return self._top is None

    def push(self, item):
        if self._top is None:
            self._top = Node(item)
        else:
            node = Node(item)
            node.next = self._top
            self._top = node

    def pop(self):
        if self.empty():
            return None
        node = self._top
        self._top = node.next
        return node.value

    def top(self):
        return self._top.value

    def __iter__(self):
        while not self.empty():
            yield self.pop()

def is_pop_order(stack_push_order, stack_pop_order):
    pass