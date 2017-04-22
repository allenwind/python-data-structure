class Dict(object):

    def __init__(self):
        self.keys = list()
        self.values = list()

    def set(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def __setitem__(self, key, value):
        self.set(key, value)

    def get(self, key, default=None):
        for index, item in enumerate(self.keys):
            if item == key:
                return self.values[index]
            else:
                return default 

    