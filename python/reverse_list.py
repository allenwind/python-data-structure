def _reversed(p_head):
    p_node = p_head
    if p_head.next is None:
        return p_node, p_head
    node, p_head = _reversed(p_node.next)
    node.next = p_node
    return p_node, p_head

def reverse_list_recursively(p_head):
    if p_head is None:
        return 
    p_node, p_head = _reversed(p_head)
    p_node.next = None
    return p_head