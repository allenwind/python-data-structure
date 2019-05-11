from common import Stack

# 1. 使用栈反转链表
# 2. 使用递归反转链表
# 3. 使用三指针扫描

def reversed_list_wit_stack(head):
    if not head:
        return None
    p_node = head
    stack = Stack()
    while p_node:
        stack.push(p_node)
        p_node = p_node.next

    head = stack.pop()
    p_node = head
    while not stack.empty():
        p_node.next= stack.pop()
        p_node = p_node.next
    return head

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





