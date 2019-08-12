from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node<{}:{}>'.format(self.key, self.value)

    def __eq__(self, node):
        return self.key == node.key

    def __gt__(self, node):
        return self.key > node.key

class LinkedHashMap:

    def __init__(self):
        self._map = dict()
        self._head = None
        self._tail = None

    def get(self, key):
        return self._map.get(key, None)

    def set(self, key, value):
        node = self._map.get(key, None)
        if node:
            node.value = value
            return
        node = Node(key, value)
        self._map[key] = node
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

    def delete(self, key):
        node = self._map.pop(key, None)
        if node:
            if node.prev is None and node.next is None:
                self._head = None
                self._tail = None
            elif node.prev is None:
                self._head = node.next
                node.next.prev = node.prev
            elif node.next is None:
                self._tail = node.prev
                node.prev.next = node.next
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def _traverse_linked_list(self):
        p_node = self._head
        while p_node:
            yield p_node
            p_node = p_node.next

    def keys(self):
        for node in self._traverse_linked_list():
            yield node.key

    def values(self):
        for node in self._traverse_linked_list():
            yield node.value

    def items(self):
        for node in self._traverse_linked_list():
            yield node.key, node.value

    def __repr__(self):
        return 'LinkedHashMap([{}])'.format(', '.join(str(item) for item in self.items()))

def testing():
    m = LinkedHashMap()
    m.set('a', 1)
    m.set('b', 2)
    m.set('c', 3)
    print(m)
    print(m.get('a'))
    print(m.get('b'))
    print(m.get('c'))

    print(m.delete('a'))
    m.set('d', 4)
    print(m.delete('c'))
    print(m)

    print(list(m.items()))
    print(list(m.keys()))
    print(list(m.values()))

if __name__ == '__main__':
    testing()


