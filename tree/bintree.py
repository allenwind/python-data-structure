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
    if tree is None:
        return 
    print(tree.data)
    preorder_traver(tree.left)
    preorder_traver(tree.right)

def inorder_traver(tree):
    pass

def postorder_traver(tree):
    pass

def layer_traver(tree):
    pass

def deep_traver(tree):
    pass


#create binary tree by list

def Tree(data, *subtrees):
    return [data].extend(subtrees)

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    return tree[i+1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    tree[i+1] = subtree

#use this method to build class Tree


#线索二叉树的实现


#二叉树类 from book
class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild





#森林转二叉树
def fs_to_bintree():
    pass

#需要优先队列实现
def huffmantree(weights):
    pass

def huffmancode(codes):
    pass