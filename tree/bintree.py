#基于list实现的二叉树
class BinTreeNode:

    def __init__(self, data, left=None, right=None):
        self._list

#利用list嵌套的方式
class BinTreeByList:

    def __init__(self, data, left=None, right=None):
        self._list = [data, left, right]

    def root(self):
        return self._list[0]

    def set_root(self, data):
        self._list[0] = data

    def is_empty(self):
        return self._list is None

    def left(self):
        return self._list[1]

    def right(self):
        return self._list[2]

    def set_left(self, tree):
        self._list[1] = tree

    def set_rigth(self, tree):
        self._list[2] = tree

class BinTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, btree):
        self.left = btree

    def set_right(self, btree):
        self.right = btree

    def __repr__(self):
        return '<Node(%s)>' % self.data

class BinTree(BinTreeNode):

    def __init__(self, data=None, left=None, right=None):
        self.root = BinTreeNode(data)
        self.root.left = left
        self.root.right = right

    def __repr__(self):
        return '<Tree(root->%s)>' % self.root.data

    def get_root(self):
        return self._root

    def is_empty(self):
        return self._root.data is None

    def num_nodes(self):
        pass

    def traversal(self):
        pass

    def forall(self, op):
        pass


class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def build_complete_tree(root, data, rest):
    #建立完全树
    root_value = data[0]
    root = BinTreeNode(root_value)
    for value in data[1:]:
        root.left = BinTreeNode(value)
        root.right = BinTreeNode(value)

def preorder_traver(tree):
    pass

def inorder_traver(tree):
    pass

def postorder_traver(tree):
    pass

def layer_traver(tree):
    pass
