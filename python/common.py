from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

    def __eq__(self, node):
        return self.value == node.value

    def __gt__(self, node):
        return self.value > node.value

@total_ordering
class DNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

    def __eq__(self, node):
        return self.value == node.value

    def __gt__(self, node):
        return self.value > node.value

class Queue:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        if self.empty():
            return None
        item = self._q[0]
        del self._q[0]
        return item

    def empty(self):
        return len(self._q) == 0

    def __len__(self):
        return len(self._q)

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

    def __len__(self):
        return len(self._s)

    def top(self):
        if self.empty():
            return None
        return self._s[-1]

class LinkedQueue:
    
    def __init__(self):
        self._root = None
        self._tail = None
        self.length = 0

    def push(self, node):
        self.length += 1
        if self._root is None:
            self._root = node
            self._tail = self._root
        else:
            self._tail.next = node
            self._tail = self._tail.next

    def pop_node(self, node):
        if self._root is None or node is None:
            return
        self.length += 1
        if self._root is node:
            self._root = None
            return
        p_node = self._root
        while p_node.next != node:
            p_node = p_node.next
        p_node.next = node.next
        return node

    def pop(self):
        if self.empty():
            return
        node = self._root
        self._root = node.next
        return node

    def __len__(self):
        return self.length

    def empty(self):
        return s.length == 0


class LinkedStack:
    
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, node):
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self._top is None:
            return
        node = self._top
        self._top = node.next
        self._size -= 1
        return node

    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

def build_linked_list(items):
    if not items:
        return None
    head = Node(items[0])
    p_node = head
    for item in items[1:]:
        p_node.next = Node(item)
        p_node = p_node.next
    return head

def traverse_list(list):
    p_node = list
    while p_node:
        yield p_node
        p_node = p_node.next


