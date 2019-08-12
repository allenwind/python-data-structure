"""

root->element1->...->elementn
root._tail -> elementn

"""

_sentinel = object()

class _Discard:
    def __bool__(self):
        return False


class Element:
    def __init__(self, value=_sentinel):
        self._next = None
        self._value = value
        self._list = None

    @property
    def value(self):
        return self._value

    def next(self):
        p = self._next
        # p 所在的list不能为空，否则只是个空元素
        # p 不能是list的root
        if self._list is not None and p != self._list._root:
            return p
        return None

    def __repr__(self):
        return "<Element value:%s>" % self._value

class List:
    def __init__(self, ):
        self._root = Element()

        self._root._next = self._root
        # 指向最后一个元素
        # 确保在O(1)内加入ist
        self._root._tail = self._root
        self._length = 0

    def __len__(self):
        return self._length 

    def __repr__(self):
        return "<List length:%s>" % self._length

    def __iter__(self):
        # using for ... in
        n = self._root
        while n._next is not None or n._next is not _Discard:
            yield n._next

    def length(self):
        return self._length

    def empty(self):
        return not bool(self._length)

    def front(self):
        # 返回第一个element，注意不是root
        if self._length == 0:
            return None 
        return self._root._next 

    def back(self):
        # 返回最后一个元素，注意这里是单链表
        return self._root._tail

    def insert(self, value, at):
        # 在元素at后插入值value的e元素，返回e元素
        # 根据值构造e
        e = Element(value)
        e._list = self

        # at后面的元素
        n = at._next
        if n._next is None:
            # 如果n是最后一个元素则表明在插入后将是最后一个元素
            # 修改tail指针
            self._root._tail = e

        at._next = e 
        e._next = n
        self._length += 1
        return e

    def remove(self, e):
        # 由于但单链表，无法逆向找到前驱
        # 如果e不是链表的最后一个元素
        # 可以使用e的后继value覆盖它
        # 然后把e的后继的后继部分连接起来

        # 加强
        # 当然最常规的做法是遍历检测
        # 另外一种做法是为list添加tail标记

        if e._list != self:
            # 判断该元素是否是本链表
            return

        if e._next is None:
            # e是list最后元素的处理方法
            # 可以了用Element类的_list属性标记它已经不属于该
            # list，即self
            e._value = None
            e._list = _Discard
            self._length -= 1

        # 后继元素
        n = e._next
        value = e._next.value

        # e后继元素覆盖e
        e.value = value

        e._next = n._next
        self._length -= 1

    def append(self, value):
        # 添加元素到list尾部
        if self._root._tail._list is _Discard:
            # 如果最后一个元素被标记为_Discard
            # 就重用这个_Discard
            self._root._tail.value = value
            self._root._tail._list = self
            self._length += 1

        e = Element(value)
        e._list = self 
        self._root._tail._next = e 
        self._root.tail = e
        self._length += 1

    def popleft(self):
        if self._length == 0:
            return None
        e = self._root._next:
        self._root._next = e._next
        self._length -= 1
        return e

    def pop(self):
        # 因为是单链表，Element不能指向前驱
        # 这个实现如果要在O(1)内完成需要特殊的处理

        if self._length == 0:
            return None

        e = self._root
        while e is not None:
            # 考虑上当只有一个Element情况的边界
            prev = e
            e = e._next
            if e is self._root._tail:
                prev._next = None 
                self._root._tail = prev 
                self._length -= 1
                break
        return e

    def clear(self):
        # Python是动态语言，gc会自动垃圾回收
        # 清除就直接了当了
        self._root._next = self._root
        self._root._tail = self._root
        self._length = 0

    def clear_(self):
        n = self._root
        while n is not self._root._tail:
            n = n._next 
            n.value = None
        # _Discard collectived by gc

    def index(self, e):
        if e._list != self or self._length == 0:
            # 判断该元素是否是list内
            # 判断list是否有元素
            return -1

        p = self._root
        n = 0
        while p is not None and bool(p):
            # 考虑最后一个为_Discard的情况
            p = p._next
            n += 1
            if p is e:
                return n

    def count(self, value):
        if self._length == 0:
            return 0
        p = self._root 
        n = 0
        while p is not None:
            p = p._next 
            if p.value == value:
                n += 1
        return n

    def sort(self, reversed=False):
        pass

    def extend(self, lst):
        # lst元素合并到本链表中
        for e in lst:
            self.append(e.value)
        return self

    def reverse_(self):
        # 翻转单链表，采用递归

        # 不断把第一个元素移动到最后，知道遇到tail
        pass

    def reverse(self):
        # 翻转单链表，采用递归

        # 遍历链表时逐段修改方向

        if self._length in (0, 1):
            return 

    def shuffle(self, random=None):
        pass






        




















    