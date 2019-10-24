import random
import string

class Node:

    def __init__(self, value=0):
        self.value = value
        self.kids = []

def gen_random_tree(root, deep, width):
	if deep == 0:
		return

	w = random.randint(1, width)
	vs = random.sample(string.ascii_letters, w)
	for v in vs:
		root.kids.append(Node(v))

	for n in root.kids:
		gen_random_tree(n, deep-1, width)

def gen_all_paths(tree, prefix, paths):
	if len(tree.kids) == 0:
		paths.append(prefix+"."+tree.value)
		return

	for n in tree.kids:
		p = prefix + "." + tree.value
		gen_all_paths(n, p, paths)

def main():
	root = Node("root")
	gen_random_tree(root, deep=15, width=2)
	prefix = ">"
	paths = []
	gen_all_paths(root, prefix, paths)

	for i in paths:
		print(i)

if __name__ == "__main__":
	main()