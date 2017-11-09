import random

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

def random_tree(order):
    pass

def insert(root, value):
    if root is None:
        return Node(value)
    side = random.choice([0, 1])
    pass

def build(preorder, inorder):
    if not preorder or not inorder or len(preorder) != len(inorder):
        return None
    root = Node(preorder[0])
    for index, value in enumerate(inorder):
        if root.value == value:
            break
    else:
        raise Exception("Invaid Input")
    root.left = build(preorder[1:index+1], inorder[:index])
    root.right = build(preorder[index+1:], inorder[index+1:])
    return root

def test():
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = build(preorder, inorder)
    return root

if __name__ == '__main__':
    tree = test()
