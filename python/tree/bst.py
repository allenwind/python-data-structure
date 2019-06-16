#若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
#若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
#任意节点的左、右子树也分别为二叉查找树；
#没有键值相等的节点。

#操作方法：查找、插入、删除

#查找
#在二叉搜索树b中查找x的过程为：
#若b是空树，则搜索失败，否则：
#若x等于b的根节点的数据域之值，则查找成功；否则：
#若x小于b的根节点的数据域之值，则搜索左子树；否则：
#查找右子树。

#插入
#向一个二叉搜索树b中插入一个节点s的算法，过程为：
#若b是空树，则将s所指结点作为根节点插入，否则：
#若s->data等于b的根节点的数据域之值，则返回，否则：
#若s->data小于b的根节点的数据域之值，则把s所指节点插入到左子树中，否则：
#把s所指节点插入到右子树中。（新插入节点总是叶子节点）



#在二叉查找树删去一个结点，分三种情况讨论：
#若*p结点为叶子结点，即PL（左子树）和PR（右子树）均为空树。由于删去叶子结点不破坏整棵树的结构，则只需修改其双亲结点的指针即可。
#若*p结点只有左子树PL或右子树PR，此时只要令PL或PR直接成为其双亲结点*f的左子树（当*p是左子树）或右子树（当*p是右子树）即可，作此修改也不破坏二叉查找树的特性。
#若*p结点的左子树和右子树均不空。在删去*p之后，为保持其它元素之间的相对位置不变，
#可按中序遍历保持有序进行调整，可以有两种做法：其一是令*p的左子树为*f的左/右（依*p是*f的左子树还是右子树而定）子树，*s为*p左子树的最右下的结点，而*p的右子树为*s的右子树；其二是令*p的直接前驱（in-order predecessor）或直接后继（in-order successor）替代*p，然后再从二叉查找树中删去它的直接前驱（或直接后继）。

import time
import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insert_node(root.left, node)
        else:
            if root.right == None:
                root.right = node 
            else:
                insert_node(root.right, node)

def find_min(root, parent):
    if root.left:
        return find_min(root.left, root)
    else:
        return [parent, root]

#递归方法
def delete_node(root, data):
    if root.data == data: #数据在根节点
        if root.right and root.left:
            #前驱
            psuccessor, successor = find_min(root.right, root)

            if psuccessor.left == successor:
                psuccessor.left = successor.right
            else:
                psuccessor.right = successor.right
            successor.left = root.left
            successor.right = root.right
            return successor
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        if root.data > data:
            if root.left:
                root.left = delete_node(root.left, data)
        else:
            if root.right:
                root.right = delete_node(root.left, data)
    return root

def find_node(root, data): #返回数据所在的节点
    if root is None:
        return False
    if root.data == data:
        return True
    if root.data > x:
        find_node(root.left, data)
    else:
        find_node(root.right, data)

def print_tree(tree):
    while tree.data:
        print(tree.data, end='\n')
        while tree.left or tree.right:
            if tree.left:
                print(tree.left.data)
                tree = tree.left
            else:
                print(tree.right.data)
                tree = tree.right

#中序遍历
def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    yield root.data
    inorder_traversal(root.right)

#后序遍历
def proorder_traversal(root):
    if not root:
        return 
    inorder_traversal(root.left)
    inorder_traversal(root.right)
    yield root.data

#前序遍历
def order_traversal(root):
    if not root:
        return
    yield root.data
    inorder_traversal(root.left)
    inorder_traversal(root.right)


def add_node(node_count):
    root_data = random.randint(1, 100)
    root = Node(root_data)
    for _ in range(node_count):
        data = random.randint(1, 100)
        node = Node(data)
        insert_node(root, node)
    return root

#晚点把类方法实现
class BST:

    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            self.root = Node(data)

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            if self.root.data > node.data:
                if self.root.left == None:
                    self.left = node
                else:
                    self.root.left
