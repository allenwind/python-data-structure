class Node:

    def __init__(self, value):
        self.value =  value
        self.left = None
        self.right = None 

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

def tree_depth(tree):
    if not tree:
        return 0
    left = tree_depth(tree.left)
    right = tree_depth(tree.right)
    if left > right:
        left += 1
        return left
    else:
        right += 1
        return right

def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    print(tree_depth(root))

if __name__ == '__main__':
    main()