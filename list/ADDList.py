
#扩展链表时使用
class ListAppend:
    def pop(self):
        pass

    def pop_last(self):
        pass

    def filter(self):
        pass

    def sort(self):
        pass

#线性表的连续区域实现
class List:

    def __init__(self):
        self._list = [] #像C语言中的数组，也可以指定分配空间[None]*100

    def is_empty(self):
        return self.len(self._list) == 0

    def len_(self): #内置方法
        return len(self._list)

    def len(self):
        count = 0
        for elem in self._list:
            count += 1
        return count
        
    def prepend(self, elem):
        self._list = [elem] + self._list

    def append(self, elem):
        self._list = self._list + [elem]

    def insert_(self, elem, i): #内置方法
        self._list.insert(i, elem)

    def insert(self, elem, i):
        self._list = self._list[:i] + [elem] + self._list[i:]
        
    def del_first(self):
        self.delete(0)

    def del_last(self):
        self.delete(-1)

    def delete(self, index):
        self._list = self._list[:index] + self._list[index+1:]

    def search_(self, elem): #内置方法
        return elem in self._list

    def search(self, ele):
        for item in self._list:
            if ele == item:
                return Treu
        return False

    def forall(self, op):
        for item in self._list:
            op(item)


#单链表线性表实现

class LNode:
    def __init__(self, value):
        self._next = None
        self._value = value
            
class LinkList:

    def __init__(self):
        self._head = None
        self._tail = None #用来扩充，头可以指向尾部

    def is_empty(self):
        return self._head is None

    def len(self):
        if self.is_empty():
            return 0
        p = self._head
        count = 1
        while p._next is not None:
            p = p._next
            count += 1
        return count
            
    def prepend(self, elem):
        node = LNode(elem)
        node._next = self._head
        self._head = node

    def append(self, elem):
        if self.is_empty():
            self._head = LNode(elem)
            return
        p = self._head
        while p._next is not None:
            p = p._next
        p._next = LNode(elem)
        
    def insert(self, elem, i):
        if self.is_empty():
            self._head = LNode(elem)
            return
        p = self._head
        count = 1
        while p._next is not None:
            p = p._next
            count += 1
            if count == i:
                node = LNode(elem)
                tail = p._next
                node._next = tail
                p._next = node
                return
        self.append(elem) #i索引大于链表长度，插到表尾部

    def del_first(self):
        if self.is_empty():
            return -1
        tail = self._head._next
        self._head = tail

    def del_last(self):
        if self.is_empty():
            return -1
        p = self._head
        while p._next is not None:
            pre = p
            p = p._next
            
        pre._next = None

    def delete(self, i):
        if self.is_empty():
            return -1
        p = self._head
        count = 1
        while p._next is not None:
            pre = p
            p = p._next
            count += 1
            if count == i:
                pre._next = p._next
                return
        return -1
     
    def search(self, elem):
        p = self._head
        count = 0
        while p is not None:
            count += 1
            if p._value == elem:
                return count-1
        return -1

    def forall(self, op):
        p = self._head
        while p is not None:
            p = p._next
            op(p.value)

class DLNode:
    def __init__(self, elem):
        self._value = elem
        self._prev = None
        self._next = None


#双链表线性表实现
class DLinkList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def len(self):
        p = self._head
        count = 0
        while p is not None:
            count += 1
            return count

    def prepend(self, elem):
        if self.is_empty():
            self._head = DLNode(elem)
            return
        tail = self._head._next
        node = DLNode(elem)
        node._next = tail
        tail._prev = node
        self._head = node

    def append(self, elem):
        p = self._head
        while p is not None:
            p = p._next

        node = DLNode(elem)
        node._prev = p
        p._next = node

    def insert(self, elem, i):
        p = self._head
        count = 0
        while p is not None:
            count += 1
            if count == i:
                tail = p._next
                node = DLNode(elem)
                p._next = node
                node._prev = p
                node._next = tail
                tail._prev = node
                return
            p = p._next
                
    def del_first(self):
        if self.is_empty():
            return -1
        tail = self._head._next
        tail._prev = None
        self._head = tail

    def del_last(self):
        p = self._head
        while p is not None:
            pre = p
            p = p._next
        pre._next = None

    def delete(self, i):
        p = self._head
        count = 0
        while p is not None:
            count += 1
            pre = p
            p = p._next
            if count == i:
                pre._next = p
                p._prev = pre
                return
        return -1
                
    def search(self, elem):
        p = self._head
        count = 0
        while p is not None:
            count += 1
            if p._value == elem:
                return count
            p = p._next
        return -1
            
    def forall(self, op):
        p = self._head
        while p is not None:
            op(p._value)
            

#循环链表，最后一个元素指向第一个Node
class CircleList:

    def __init__(self):
        self._list = []

    def is_empty(self):
        return self.len(self._list) == 0

    def len(self):
        count = 0
        for item in self._list:
            count += 1
        return count

    def prepend(self, elem):
        pass

    def append(self, elem):
        pass

    def insert(self, elem, i):
        pass

    def del_first(self):
        pass

    def del_last(self):
        pass

    def delete(self, i):
        pass

    def search(self, elem):
        pass

    def forall(self, op):
        pass

class CircleLinkList:

    def __init__(self):
        self._head = None
        sefl._tail = None #记录尾部

    def is_empty(self):
        return self._head is None

    def len(self):
        p = self._head
        first = p #标记第一个元素
        count = 0
        while p is not None:
            p = p._next
            count += 1
            if p == first:
                break
        return count

    def prepend(self, elem):
        node = LNode(elem)
        if self._head is None:
            node._next = self._head
            self._head = node
        else:
            node._next = self._head._next
            self._head = node
            

    def append(self, elem):
        pass

    def circle(self, i):
        #旋转链表，i为正数，向前旋转位数
        p = self._head
        count = 0
        while p is not None:
            count += 1
            if count == i:
                self._head = p
            p = p._next

class CircleDLinkLint:
    pass


#链表相关操作


#使用两队列实现栈








    

    
