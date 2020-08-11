#实现线性表， 连续储存方法，区别与链表方法


#线性表的实现-->顺序表 这种方式类似于C语言中的数组
class List(object):
    def __init__(self):
        self._list = []

    @classmethod
    def create(cls, list):
        cls._list = []
        cls._list.extend(list)
        return cls()

    def is_empty(self):
        pass

    def length(self):
        pass

    def prepend(self, element):
        pass

    def append(self, element):
        pass

    def insert(self, index, element):
        pass

    def del_first(self):
        pass

    def del_last(self):
        pass

    def delete(self, index):
        pass

    def search(self, element):
        pass

    def forall(self, operate):
        pass
