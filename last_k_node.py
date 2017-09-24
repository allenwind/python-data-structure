class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node<{}>'.format(self.value)

def build_linked_list(values):
    if not values:
        return None
    root = Node(values[0])
    p_node = root
    for value in values[1:]:
        p_node.next = Node(value)
        p_node = p_node.next
    return root

def travel_list(linked):
    while linked:
        yield linked
        linked = linked.next

def last_k_node(p_head, k):
    if not p_head:
        raise ValueError("p_head is None")
    if k <= 0:
        raise ValueError("k must be positive")
    p1 = p_head
    p2 = p_head

    n = 0
    for _ in range(k):
        p1 = p1.next
        n += 1
        if p1 is None and n != k-1:
            raise ValueError("p_head's length < k")
    while p1:
        p1 = p1.next
        p2 = p2.next
        n += 1
        if p1 is None:
            break
    return p2

def main():
    p_head = build_linked_list(range(10))
    node_9 = last_k_node(p_head, 1)
    print("last 1 node", node_9)

    node_6 = last_k_node(p_head, 4)
    print("last 4 node", node_6)

if __name__ == '__main__':
    main()
