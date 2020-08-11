class Dict(object):

    def __init__(self):
        self._keys = list()
        self._values = list()

    def set(self, key, value):
        self._keys.append(key)
        self._values.append(value)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return key in self._keys

    def get(self, key, default=None):
        for index, item in enumerate(self._keys):
            if item == key:
                return self._values[index]
            else:
                return default

    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self.set(key, value) 

    def keys(self):
        return self._keys 

    def values(self):
        return self._values

#这种实现方法有很多问题

    