import random
from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

def build_linked_list(values):
    if not values:
        return None
    root = Node(values[0])
    p_node = root
    for value in values[1:]:
        p_node.next = Node(value)
        p_node = p_node.next
    return root

def find_min_node(lists):
    if not lists:
        return None
    _min = None
    index = 0
    for i, node in enumerate(lists):
        if _min is None:
            _min = node
        elif _min > node:
            _min = node
            index = i
    if _min.next:
        lists[index] = _min.next
    else:
        del lists[index]
    return _min

def merge_lists(lists):
    head = find_min_node(lists)
    p_node = head
    while lists:
        p_node.next = find_min_node(lists)
        p_node = p_node.next
    return head

def travel_list(linked):
    while linked:
        yield linked
        linked = linked.next

def testing():
    l1 = build_linked_list(sorted(random.sample(range(20), 10)))
    l2 = build_linked_list(sorted(random.sample(range(20), 10)))
    l3 = build_linked_list(sorted(random.sample(range(20), 10)))
    head = merge_lists([l1, l2, l3])
    for i in travel_list(head):
        print(i, end=' ')

if __name__ == '__main__':
    testing()
