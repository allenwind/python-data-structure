from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, key):
        self.key = key
        self._next = []

    def __repr__(self):
        return 'Node<{}>'.format(self.key)

    def __eq__(self, key):
        return self.key == key

    def __gt__(self, key):
        return self.key > key

class Trie:

    def __init__(self):
        self._root = Node(None)

    def clear(self):
        self._root = Node(None)

    def insert(self, string):
        nodes = self._root._next
        for key in string:
            try:
                index = nodes.index(key)
                node = nodes[index]
                nodes = node._next
            except ValueError:
                node = Node(key)
                nodes.append(node)
                nodes = node._next

    def search(self, string):
        nodes = self._root._next
        for key in string:
            try:
                index = nodes.index(key)
                node = nodes[index]
                nodes = node._next
            except ValueError:
                return False
        return True

    def find_prefix(self, prefix):
        nodes = self._root._next
        for key in prefix:
            try:
                index = nodes.index(key)
                node = nodes[index]
                nodes = node._next
            except ValueError:
                return []
        child_prefix = ''
        child_keys = []
        self._prefix(nodes, child_prefix, child_keys)
        return [prefix+key for key in child_keys]

    def _prefix(self, nodes, prefix, keys):
        if not nodes:
            keys.append(prefix)
            return
        else:
            for node in nodes:
                prefix = prefix + node.key
                self._prefix(node._next, prefix, keys)

    def keys(self):
        return self.find_prefix('')

'''
trie tree，字典树，前缀匹配树
结点的设计可以使用多重链表，但出于性能的考虑，
这里只用字典。
'''
from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, key):
        self.key = key
        self.next = None
        self.child = None

    def __repr__(self):
        return 'Node<{}>'.format(self.key)

    def __eq__(self, key):
        return self.key == key

    def __gt__(self, key):
        return self.key > key

class Trie:

    def __init__(self):
        self._root = Node(None)

    def insert(self, prefix):
        node = self._root
        prefix = list(prefix)
        self._insert(node, prefix)

    def _insert(self, node, prefix):
        if not prefix:
            return
        if node.key == None:
            node.key = prefix[0]
            node.child = Node(None)
            self._insert(node.child, prefix[1:])
        if node.key == prefix[0]:
            if node.child:
                self._insert(node.child, prefix[1:])
            else:
                node.child = Node(None)
                self._insert(node.child, prefix[1:])
        else:
            node = self._find_node(node, prefix[0])
            self._insert(node, prefix[1:])

    def _find_node(self, node, key):
        while node.next:
            if node.next.key == key:
                if node.child:
                    return node.child
                else:
                    node.child = Node(None)
                    return node.child
            else:
                node = node.next
        node.next = Node(key)
        node.next.child = Node(None)
        return node.next.child

    def search(self, string):
        node = self._root
        for key in string:
            if node.key == key:
                if node.child:
                    node = node.child
                else:
                    return False
            else:
                if node.next:
                    node = node.next
                else:
                    return False
        else:
            return True


class TrieNode:

    def __init__(self, key):
        self.key = key
        self.next = []

    def __repr__(self):
        return 'Node<{}>'.format(self.key)



class TrieTree:

    def __init__(self):
        self._root = Node('root')

    def get(self, string):
        x = self._get(self._root, string, 0)
        if x is None:
            return None
        return x.val

    def _get(self, node, key, d):
        if node is None:
            return 
        if d == len(key):
            return node
        c = key[d]
        return self._get(c.next[c], key, d+1)

    def put(self, key, value):
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node, key, value, d):
        if node is None:
            return TrieNode()
        if d == len(key):
            node.key = value
            return node
        c = key[d]
        x.next[c] = put(x.next[c], key, value,d+1)
        return x

def main():
    t = Trie()
    words = [
        'blue',
        'blur',
        'car',
        'cat',
        'caw',
        'coin',
    ]
    for w in words:
        t.insert(w)
    return t


   