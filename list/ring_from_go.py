class Ring:
    def __init__(self, next=None, prev=None, value=None):
        self._next = next 
        self._prev = prev 
        self._value = value

    def _init(self):
        self._next = self 
        self._prev = self
        return self 

    def next(self):
        if self._next is None:
            return self._init()
        return self._next 

    def prev(self):
        if self._next is None:
            return r._init()
        return self._prev 

    def move(self, n):
        # 旋转链表
        if self._next is None:
            return self._init()

        if n < 0:
            while n < 0:
                n += 1
                self = self._prev
        elif n > 0:
            while n > 0:
                n -= 1
                self = self._next
        
        return self

    def link(self, s=None):
        n = self.next()
        if s is not None:
            p = self.prev()
            self._next = s
            s._next = self 
            n._prev = p 
            p._next = n
        return n

    def unlink(self, n):
        if n <= 0:
            return None 
        return self.link(self.move(n+1))

    def len(self):
        n = 0 
        if self is not None:
            n = 1
            p = self.next()
            while p != self:
                p = p._next 
                n += 1
        return n

    def do(self, func):
        if self is not None:
            func(self._value)
            p = self.next()
            while p != self:
                p = p._next 
                func(p._value)

def new_ring(n):
    if n <= 0:
        return None 
    r = Ring()
    p = r 
    i = 1
    while i < n:
        i += 1
        p._next = Ring(prev=p)
        p = p._next 
    p._next = r
    r._prev = p
    return r


