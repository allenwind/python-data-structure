import collections
import random

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

def build_random_tree(values):
    nodes = set()
    for v in values:
        nodes.add(Node(v))
    while len(nodes) != 1:
        node1 = nodes.pop()
        node2 = nodes.pop()
        if random.choice([0, 1]):
            node1.left = node2
        else:
            node1.right = node2
        nodes.add(node1)
    return nodes.pop()
            
    
def build_banance_random_tree(values):
    pass
