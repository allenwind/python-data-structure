# 这个实现参考自golang的container/list库

class Element:

    def __init__(self, value, next_=None, prev=None, list_=None):
        self._value = value
        self._next = next_
        self._prev = prev
        self._list = list_

    def __repr__(self):
        return "<Element value:%s>" % self._value

    def next(self):
        p = self._next 
        if self._list is not None and p != self._list._root:
            return p 
        return None 

    def prev(self):
        p = self._prev 
        if self._list is not None and p != self._list._root:
            return p
        return None

class List:

    def __init__(self, root=None):
        self._root = root 
        self._len = 0

    def init(self):
        self._root = Element()
        self._root._next = self._root 
        self._root._prev = self._root
        self._len = 0
        return self

    def len(self):
        return self._len

    def front(self):
        if self.len() == 0:
            return None 
        return self._root._next 

    def back(self):
        if self.len() == 0:
            return None 
        return self._root._prev

    def __repr__(self):
        return "<List-len:%s>" % self.len()
                                  
    def _lazyinit(self):
        if self._root._next is None:
            self.init()

    def _insert(self, e, at):
        n = at._next 
        at._next = e
        e._prev = at 
        e._next = n 
        n._prev = e 
        e._list = self
        self._len += 1
        return e

    def _insertValue(self, value, at):
        e = Element(value=value)
        return self._insert(e, at)

    def _remove(self, e):
        e._prev._next = e._next 
        e._next._prev = e._prev 
        e._next = None 
        e._prev = None 
        e._list = None 
        self._len -= 1
        return e

    def __len__(self):
        return self.len()

    def remove(self, e):
        if e._list == self:
            self._remove(e)
        return e._value

    def push_front(self, value):
        self._lazyinit()
        return self._insertValue(value, self._root)

    appendleft = push_front

    def push_back(self, value):
        self._lazyinit()
        return self._insertValue(value,  self._root._prev)

    append = push_back

    def insert_before(self, value, mark):
        if mark._list != self:
            return None 
        return self._insertValue(value, mark._prev)

    def insert_after(self, value, mark):
        if mark._list != self:
            return None 
        return self._insertValue(value, mark)

    def move_to_front(self, e):
        if e._list != self or self._root._next == e:
            return 
        self._insert(self._remove(e), self._root)

    def move_to_back(self, e):
        if e._list != self or self._root._prev == e:
            return 
        self._insert(self._remove(e), self._root._prev)

    def move_before(self, e, mark):
        if e._list != self or e == mark or mark._list != self:
            return 
        self._insert(self._remove(e), mark._prev)

    def move_after(self, e, mark):
        if e._list != self and e == mark and mark._list != self:
            return 
        self._insert(self._remove(e), mark)

    def push_back_list(self, lst):
        self._lazyinit()
        i = lst.len()
        e = lst.front()
        while i > 0:
            i -= 1
            e = e.next()
            self._insertValue(e._value, self._root._prev)

    extend = push_back_list

    def push_front_list(self, lst):
        self._lazyinit()
        i = lst.len()
        e = lst.back()
        while i > 0:
            i -= 1
            e = e.prev()
            self._insertValue(e._value, self._root)

    extendleft = push_front_list

    def __iter__(self):
        if self.len() == 0:
            return
        cursor = self._root._next
        while cursor._value:
            yield cursor._value
            cursor = cursor._next

    def split(self, e):
        # 在元素e出分割list
        pass

    def find(self, e):
        pass

    def index(self, e):
        pass

    def sort(self):
        pass

    @classmethod
    def new(cls):
        l = cls().init()
        return l

def new_list(size):
    l = List().init()
    for i in range(size):
        l.append(i)
    return l
    






