class IntTrie:

    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def insert(self, key, value):
        p = self
        while key != 0:
            if key & 1 == 0:
                if p.left is None:
                    p.left = self.__class__()
                p = p.left
            else:
                if p.right is None:
                    p.right = self.__class__()
                p = p.right
            key = key >> 1
        p.value = value
        return self

    def search(self, key):
        p = self
        while key != 0:
            if key & 1 == 0:
                p = p.left
            else:
                p = p.right
            key = key >> 1
        if p is not None:
            return p.value
        else:
            return None

def maskbit(key, mask):
    return key & ~(mask-1)

def match(key, tree):
    return not tree.is_leaf() and \
           maskbit(key, tree.mask) == tree.prefix

def is_zero(key, mask):
    return key & (mask>>1) == 0

def lcp(p1, p2):
    diff = p1 ^ p2
    mask = 1
    while diff != 0:
        diff = diff >> 1
        mask = mask << 1
    return maskbit(p1, mask), mask

def branch(t1, t2):
    pass


class IntPatricia:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._prefix = None
        self._mask = None

    def is_leaf(self):
        return !(self.left or self.right)

    def replace(self, left, right):
        if self.left == left:
            self.left = right
        else:
            self.right = right

    @property
    def prefix(self):
        if self._prefix is None:
            return self.key
        else:
            return self._prefix

    def insert(self, key, value):
        pass

    
