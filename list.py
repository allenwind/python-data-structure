class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.list = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

class List:

    def __init__(self):
        self.root = Node(None)
        self.root.next = self.root
        self.root.prev = self.root
        self.length = 0

    def __len__(self):
        return self.length

    def front(self):
        if len(self) == 0:
            return None
        return l.root.next

    def back(self):
        if len(self) == 0:
            return None
        return l.root.prev

    def _insert(self, node, at):
        n = at.next
        at.next = node
        node.prev = at
        node.next = n
        n.prev = node
        node.list = self.root
        self.length += 1
        return node

    def insert(self, value, at):
        node = Node(value)
        return self._insert(node, at)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        node.list = None
        self.length -= 1
        return node

    def remove(self, node):
        if node.list == self.list:
            self._remove(node)
        return node.value

    def appendleft(self, value):
        return self.insert(value, self.root)

    def append(self, value):
        return self.insert(value, self.root.prev)

    def insert_before(self, value, target):
        if target.list != self.list:
            return None
        return self.insert(value, target)

    def insert_after(self, value, target):
        if target.list != self.root:
            return None
        return self.insert(value, target)

    def move_to_front(self, node):
        if node.list != self.root or self.root.next == node:
            return
        self.insert(self.remove(node), self.root)

    def move_to_back(self, node):
        if node.list != self.root or self.root.next == node:
            return
        self.insert(self.remove(node), self.root.prev)

    def __iter__(self):
        node = self.root.next
        while node:
            yield node
            node = node.next
            









