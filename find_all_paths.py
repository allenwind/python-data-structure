import random

def gen_random_trees():
	pass

def find_all_paths(tree):
	nodes = tree.keys()
	for node in nodes:
		find_all_paths(node)