class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class RedisDict:
    pass

class LRUCache:

    def __init__(self, size=10):
        # 两哨兵结点
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = size
        self._map = dict()

    def move_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def _delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        node = self._map.get(key, None)
        if node:
            self._delete(node)
            self.move_to_tail(node)
            return node.value

    def set(self, key, value):
        node = self._map.get(key, None)
        if node:
            node.value = value
            self._delete(node)
            self.move_to_tail(node)
            return

        if self.size == len(self._map):
            node = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self._map.pop(node.key)
        node = Node(key, value)
        self.move_to_tail(node)
        self._map[key] = node

def testing():
    cache = LRUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.get(1)
    cache.set(3, 3)
    cache.get(2)
    cache.set(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

if __name__ == '__main__':
    # for testing
    testing()





