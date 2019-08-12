class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Node<{}>".format(self.value)

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

def delete_node(p_head, node):
    if not p_head or not node:
        return False
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    elif p_head == node:
        p_head = None
        node = None
        return True
    else:
        p_node = p_head
        while p_node.next != node:
            p_node = p_node.next
        p_node.next = None
        return True
    return False

def main():
    p_head = build_linked_list([1, 2, 3, 4, 5])
    node_3 = p_head.next.next # Node<3>
    delete_node(p_head, node_3)
    for node in travel_list(p_head):
        print(node, end='\t')

    print('\n')
    print('delete last node')
    node_5 = p_head.next.next.next
    delete_node(p_head, node_5)
    for node in travel_list(p_head):
        print(node, end='\t')

if __name__ == '__main__':
    main()