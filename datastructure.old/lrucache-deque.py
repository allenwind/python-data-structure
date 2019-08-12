# channel deque in go
# collections.deque in python

from collections import deque

class LRUCache:

    def __init__(self, size):
        self._size = size
        self._deque = deque([], size)
        self._map = dict()

    @property
    def size(self):
        return self._size

    def get(self, key):
        pass

    def set(self, key, value):
        pass

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        pass
    

