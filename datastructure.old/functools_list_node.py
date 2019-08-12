import enum
import functools

NEXT = False
CURRENT = True

def Node(current_value, next_value):
    return lambda is_current: current_value \
           if is_current else next_value

def next_value(l):
    print(l(True))
    return l(False)

def print_list(l):
    while l:
        l = next_value(l)

def add_to_head(l, value):
    return Node(value, l)

# this problem 
def add_to_tail(l, value):
    a, b = _find_tail(l)
    prev = Node(value, a)
    return Node(prev, b)

def list_length(l):
    length = 0
    while l:
        l = l(False)
        length += 1
    return length

def find_index(l, index):
    for _ in range(index):
        l = l(False)
    return l(True)

def build_list(items):
    items.append(None)
    return functools.reduce(Node, reversed(items))

def test():
    l = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    return l
"""
class Node:

    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        self.key = Node(value)
        return self.key
"""
