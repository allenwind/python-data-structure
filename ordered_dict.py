class OrderedDict:

    def __init__(self):
        self._root = dict()
        self._ordered = []

    def set(self, key, value):
        if key in self._root:
            return
        self._root[key] = value
        self._ordered.append(key)

    def get(self, key):
        return self._root.get(key, None)

    def delete(self, key):
        if key in self._root:
            del self._root[key]
            self._ordered.remove(key)

    def keys(self):
        return tuple(self._ordered)

    def values(self):
        return tuple([self._root[key] for key in self._ordered])

    def items(self):
        for key in self._ordered:
            yield key, self._root[key]

    def __repr__(self):
        return 'OrderedDict([{}])'.format(', '.join(str(item) for item in self.items()))