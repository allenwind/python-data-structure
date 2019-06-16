
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

#利用堆排序实现的优先队列
class PriorityQueue:

    def __init__(self, elist=None):
        self._elements = elist
        self.buildheap()

    def is_empty(self):
        return not self._elements

    def peek(self):
        if self.is_empty():
            raise
        return self._elements[0]

    def length(self):
        return len(self._elements)

    def enqueue(self, e):
        self._elements.append(None) #add a dummy element
        self.siftup(e, self.length()-1)

    def siftup(self, e, last):
        j = (last-1) // 2
        i = last
        while i > 0 and e < self._elements[j]:
            self._elements[i] = self._elements[j]
            i, j = j, (j-1)//2
        self._elements[i] = e

    def siftdown(self, e, begin, end):



class QueueByStack:
    #利用两个栈实现队列
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()
        self._left_side = True #mean _stack1
        self._size = 0

    def put(self, e):
        self._size += 1
        if self._left_side:
            self._stack1.push(e)
        else:
            self._stack2.push(e)

    def get(self):
        self._size -= 1
        if self._left_side:
            e = self._stack1.pop()
            while not self._stack1.is_empty():
                self._stack2.push(e)
                e = self._stack1.pop()
            self._left_size = False
            return e
        else:
            e = self._stack2.pop()
            while not self._stack2.is_empty():
                self._stack1.push(e)
                e = self._stack2.pop()
            return e

    def is_empty(self):
        return self._stack1.is_empty() and self._stack2.is_empty()

    def qsize(self):
        return self._size

    def full(self):
        pass

    def clear(self):
        if self._left_size:
            while self._stack1.is_empty():
                self._stack1.pop()
        else:
            while self._stack2.is_empty():
                self._stack2.pop()

































    
        

    
