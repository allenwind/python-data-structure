
class EmptyError(Exception):
    pass

#顺序表实现
class Stack:

    def __init__(self):
        self._stack = []

    def is_empty(self):
        return self._stack == []

    def push(self, elem):
        self._stack + [elem]

    def pop(self):
        elem = self._stack[-1]
        del self._stack[-1]
        return elem

    def top(self):
        if self.is_empty():
            raise EmptyError()
        return self._stack[-1]

class Node:
    def __init__(self, elem):
        self._value = elem
        self._next = None

#栈的链表实现
class LStack:

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self.is_empty():
            raise EmptyError()
        return self._top._value

    def push(self, elem):
        node = Node(elem)
        node._next = self._top
        self._top = node

    def pop(self):
        if self.is_empty():
            raise EmptyError()
        p = self._top
        self._top = p._next
        return p._value






























    
        

    
