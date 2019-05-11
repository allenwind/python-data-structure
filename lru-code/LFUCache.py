import reprlib

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 
        self.prev = None
        self.freq = 0
        self.list = None
        self.freq_node = None

    def __repr__(self):
        return '<Node({}:{}):{}>'.format(self.key, self.value, self.freq)

class NodeList:

    def __init__(self):
        self.root = Node(None, None) # 拿一个空结点做哨兵结点，next、prev分别指向链表的head、tail
        self.root.next = self.root
        self.root.prev = self.root
        self.freq_node = None
        self.length = 0

    def __len__(self):
        return self.length

    @property
    def tail(self):
        if len(self) == 0:
            return None
        return self.root.prev

    def insert(self, e, at):
        n = at.next
        at.next = e
        e.prev = at
        e.next = n
        n.prev = e
        e.list = self
        self.length += 1

    def remove(self, e):
        e.prev.next = e.next
        e.next.prev = e.prev
        e.next = None
        e.prev = None
        e.list = None
        self.length -= 1
        return e

    def add_to_tail(self, e):
        self.insert(e, self.root.prev)

    def __iter__(self):
        e = self.root.next
        while e and e != self.root:
            yield e
            e = e.next

    def __next__(self):
        for e in iter(self):
            yield e

    def __repr__(self):
        return '<List({})>'.format(reprlib.repr([node for node in self]))

class FreqNode:

    def __init__(self, freq, freq_node_list):
        self.node_list = NodeList()
        self.freq = freq
        self.freq_node_list = freq_node_list
        self._next = None
        self._prev = None

    def __len__(self):
        return len(self.node_list)

    def __repr__(self):
        return '<FreqNode({})>'.format(repr(self.node_list))

    @property
    def next(self):
        p = self._next
        if p is not None and p != self.freq_node_list.root:
            return p
        return None

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        p = self._prev
        if p is not None and p != self.freq_node_list.root:
            return p
        return None

    @prev.setter
    def prev(self, node):
        self._prev = node

    def move_to_prev_freq_node(self, e):
        e.freq += 1
        e = self.remove(e)
        if self.prev is None:
            self.freq_node_list.add_to_head(FreqNode(e.freq, self.freq_node_list))
        if e.freq == self.prev.freq:
            self.prev.add_to_tail(e)
        elif e.freq < self.prev.freq:
            self.freq_node_list.insert(FreqNode(e.freq, self.freq_node_list), self.prev)
            self.prev.add_to_tail(e)

        if len(self.node_list) == 0:
            self.freq_node_list.remove(self)
        
    @property
    def tail(self):
        return self.node_list.tail
    
    def remove(self, e):
        return self.node_list.remove(e)
    
    def insert(self, e, at):
        self.node_list.insert(e, at)
        
    def add_to_tail(self, e):
        self.node_list.add_to_tail(e)

class FreqNodeList:

    def __init__(self):
        self.root = FreqNode(None, None)
        self.root.prev = self.root
        self.root.next = self.root
        self.length = 0

    def insert(self, e, at):
        n = at.next
        at.next = e
        e.prev = at
        e.next = n
        n.prev = e
        e.freq_node_list = self
        self.length += 1

    def remove(self, e):
        e.prev.next = e.next
        e.next.prev = e.prev
        e.next = None
        e.prev = None
        e.freq_node_list = None
        self.length -= 1
        return e

    @property
    def tail(self):
        if len(self) == 0:
            return None
        return self.root.prev

    @property
    def head(self):
        if len(self) == 0:
            return None
        return self.root.prev

    def __len__(self):
        return self.length

    def __iter__(self):
        e = self.root.next
        while e and e != self.root:
            yield e
            e = e.next

    def __next__(self):
        for e in iter(self):
            yield e

    def __repr__(self):
        return '<FreqNodeList({})>'.format(reprlib.repr([node for node in self]))

    def add_to_tail(self, e):
        self.insert(e, self.root.prev)

    def add_to_head(self, e):
        self.insert(e, self.root)

class LFUCache:

    def __init__(self, size=10):
        self.cache = dict()
        self.freq_node_list = FreqNodeList()
        self.size = size

    def put(self, key, value):
        pass

    def get(self, key):
        node = self.cache.get(key, None)
        if node:
            node.freq_node.move_to_prev_freq_node(node)
            return node.value

def main():
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.get(1)
    c.get(2)
    c.put(3, 3)
    c.put(4, 4)
    c.get(4)
    c.get(3)

if __name__ == '__main__':
    main()
