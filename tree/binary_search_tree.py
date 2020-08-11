from functools import total_ordering

class Queue:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        if self.empty():
            return None
        item = self._q[0]
        del self._q[0]
        return item

    def empty(self):
        return len(self._q) == 0

    def __len__(self):
        return len(self._q)

class Stack(Queue):

    def pop(self):
        if self.empty():
            return None
        return self._q.pop()

    def top(self):
        if self.empty():
            return None
        return self._q[-1]

@total_ordering
class Node:

    def __init__(self, key, value, n):
        self.key = key
        self.value = value
        self.left = None
        self.right = None 
        self.parent = None
        self.n = n

    def __gt__(self, node):
        return self.key > node.key

    def __eq__(self, node):
        return self.key == node.key

    def __repr__(self):
        return 'Node<{}:{}>'.format(self.key, self.value)

class BinarySearchTree:

    def __init__(self):
        self._root = None

    def __repr__(self):
        key = self._root.key if self._root else None
        value = self._root.value if self._root else None
        return 'Node<{}:{}>'.format(key, value)

    def size(self):
        return self._size(self._root)

    def _size(self, node):
        if node is None:
            return 0
        return node.n

    def search(self, key):
        return self._search(self._root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if node.key > key:
            self._search(node.left, key)
        elif node.key < key:
            self._search(node.right, key)
        else:
            return node.value

    def search_and_set(self, key, default):
        pass

    def _search_and_set(self, node, key, default):
        pass

    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value, 1)
        if node.key > key:
            node.left = self._insert(node.left, key, value)
        elif node.key < key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self):
        return self._min(self._root).key

    def _min(self, node):
        if self._root is None:
            return None
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self):
        return self._max(self._root).key

    def _max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node
        return self._max(node.right)

    def delete_max(self):
        self._root = self._delete_max(self._root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left
        node.left = self._delete_max(node.left)
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_min(self):
        self._root = self._delete(self._root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        self._root = self._delete(self._root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_and_return(self, key):
        self._root, target = self._delete_and_return(self._root, key)
        return target.value

    def _delete_and_return(self, node, key):
        if node is None:
            return None, node
        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left, node
            if node.left is None:
                return node.right, node
            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node, t

    @property
    def root(self):
        return self._root

    def morror_tree(self):
        '''
        反转bst
        '''
        self._morror_tree(self._root)
        return self.root

    def _morror_tree(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            self._morror_tree(root.left)
        if root.right:
            self._morror_tree(root.right)

class TreeIterMixin:

    def preorder_traverse(self):
        for x in self._preorder(self._root):
            yield x

    def _preorder(self, node):
        if node:
            yield node
            for x in self._preorder(node.left):
                yield x
            for x in self._preorder(node.right):
                yield x

    def inorder_traverse(self):
        for x in self._inorder(self._root):
            yield x

    def _inorder(self, node):
        if node:
            for x in self._inorder(node.left):
                yield x
            yield node
            for x in self._inorder(node.right):
                yield x

    def postorder_traverse(self):
        for x in self._inorder(self._root):
            yield x

    def _postorder(self, node):
        if node:
            for x in self._preorder(node.left):
                yield x
            for x in self._preorder(node.right):
                yield x
            yield node

    def depth_first_order_traverse(self):
        if self._root:
            stack = Stack()
            stack.push(self._root)
            while not stack.empty():
                node = stack.pop()
                if node.left:
                    stack.push(node.left)
                if node.right:
                    stack.push(node.right)
                yield node

    def breadth_first_order_traverse(self):
        if self._root:
            queue = Queue()
            queue.push(self._root)
            while not queue.empty():
                node = queue.pop()
                if node.left:
                    queue.push(node.left)
                if node.right:
                    queue.push(node.right)
                yield node

class Dict(TreeIterMixin, BinarySearchTree):

    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            self.insert(key, value)

    def clear(self):
        self._root = None

    def copy(self):
        tree = BinarySearchTree()
        for x in self.breadth_first_order_traverse():
            tree.insert(x.key, x.value)
        return tree

    def fromkeys(self, seq, value):
        tree = BinarySearchTree()
        for key in seq:
            tree.insert(key, value)
        return tree

    def get(self, k, d=None):
        value = self.search(k)
        return value if value else k

    def items(self):
        return [(node.key, node.value) for node in self.inorder_traverse()]

    def keys(self):
        return [node.key for node in self.inorder_traverse()]

    def values(self):
        return [node.value for node in self.inorder_traverse()]

    def pop(self, k, d=None):
        value = self.delete_and_return(d)
        return value if value else d

    def popitem(self):
        if not self._root:
            raise KeyError("dict is empty")
        key = self._root.key
        value = self.delete_and_return(key)
        return (key, value)

    def setdefault(self, k, d=None):
        value = self.get(k, d)
        if value is d and d is not None:
            self.insert(k, d)
        return value

    def update(self, dict, **kwargs):
        for key, value in dict.items():
            self.insert(key, value)
        for key, value in kwargs.items():
            self.insert(key, value)

    def __len__(self):
        return self.size()

    def __bool__(self):
        return bool(self._root)

    def __contains__(self, key):
        return bool(self.search(key))

    def __delitem__(self, key):
        self.delete(key)

    def __repr__(self):
        return str(dict(self.items()))

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        value = self.search(key)
        if not value:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        value = self.delete_and_return(key)
        if not value:
            raise KyeError(key)

class PriorityQueue(BinarySearchTree):

    def push(self, priority, item):
        self.insert(priority, item)

    def pop(self):
        _min = self.min()
        if _min:
            self.delete_min()
        return _min

def make_dict(size):
    import random
    import string
    d = Dict()
    for _ in range(size):
        key = ''.join(random.sample(string.ascii_letters, random.randint(1, 1)))
        value = random.randint(1, 10000)
        d.insert(key, value)
    return d

def tree_to_list(root):
    node_iter = root.inorder_traverse()
    p_node = next(node_iter)
    head = p_node
    for node in node_iter:
        p_node.right = node
        p_node.left = None
        node.left = p_node
        p_node = node
    return head

def test():
    import random
    
    nums = list(range(1, 11))
    t = Dict()
    random.shuffle(nums)
    for v in nums:
        t.insert(v, v)

    head = tree_to_list(t)
    while head:
        print(head)
        head = head.right

if __name__ == '__main__':
    test()
        
    



