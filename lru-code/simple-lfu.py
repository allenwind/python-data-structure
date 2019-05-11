import heapq
import functools

class Node:

    def __init__(self, key, value, priority):
        self.key = key
        self.value = value
        self.priority = priority

    def __eq__(self, node):
        return self.priority == node.priority

    @functools.total_ordering
    def __gt__(self, node):
        return self.priority > node.priority

    def __repr__(self):
        return '<Node key:{} value:{} freq:{}>'.format(self.key,
                                                       self.value,
                                                       self.priority)

class PriorityQueue:

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def put(self, node):
        heapq.heappush(self._queue, node)

    def get(self):
        if len(self) == 0:
            return None
        return heapq.heappop(self._queue)

    def heapify(self):
        heapq.heapify(self._queue)

class LFUCache:

    def __init__(self, size):
        self._size = size
        self._cache = PriorityQueue()
        self._map = dict()

    def __len__(self):
        return len(self._cache)

    def get(self, key):
        node = self._map.get(key, None)
        if node is not None:
            node.priority += 1
            self._cache.heapify()
        return node.value

    def set(self, key, value):
        if len(self._cache) > self._size:
            node = self._cache.get()
            self._map.pop(node.key)
        if key in self._map:
            self._map[key].value = value
            self._map[key].priority += 1
            self._cache.heapify()
        node = Node(key, value, 1)
        self._map[key] = node
        self._cache.put(node)
            
            
        
        
