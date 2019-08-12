class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

def build_ring_list(numbers):
    if not numbers:
        return None
    root = Node(numbers[0])
    p_node = root
    for value in numbers[1:]:
        p_node.next = Node(value)
        p_node = p_node.next
    p_node.next = root
    return root

def last_remaining_number(ring, m):
    p_node = ring
    n = 0
    while p_node:
        if p_node == p_node.next:
            return p_node
        n += 1
        if n == m - 1:
            p_node.next = p_node.next.next
            n = 0
        p_node = p_node.next

def _cycle(numbers, m):
    loop = 0
    while len(numbers) > 1:
        for item in numbers:
            loop += 1
            if loop == m:
                loop = 0
                yield index

def last_remaining_number_with_generator(numbers, m):
    for index in _cycle(numbers, m):
        del numbers[index]
    return numbers[0]