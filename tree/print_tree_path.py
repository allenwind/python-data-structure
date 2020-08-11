import random
import string

class Node:

    def __init__(self, value=0):
        self.value = value
        self.kids = []

    def is_leaf(self):
        return len(self.kids) == 0

def gen_random_tree(deep, width):
    def _gen_random_tree(root, deep, width):
        if deep == 0:
            return

        w = random.randint(1, width)
        vs = random.sample(string.ascii_letters, w)
        for v in vs:
            root.kids.append(Node(v))

        for n in root.kids:
            _gen_random_tree(n, deep-1, width)
    
    root = Node(value="root")
    _gen_random_tree(root, deep, width)
    return root

def gen_all_paths(tree):
    def _gen_all_paths(tree, prefix, paths):
        if tree.is_leaf():
            paths.append(prefix+"."+tree.value)
            return

        for n in tree.kids:
            p = prefix + "." + tree.value
            _gen_all_paths(n, p, paths)

    prefix = ">"
    paths = []
    _gen_all_paths(tree, prefix, paths)
    return paths

def main():
    root = gen_random_tree(deep=15, width=2)
    paths = gen_all_paths(root)

    for i in paths:
        print(i)

if __name__ == "__main__":
    main()