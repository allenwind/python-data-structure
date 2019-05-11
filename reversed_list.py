class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def reversed_list(head):
    # 关于边界条件
    if head is None:
        return head
    # 其实下面的操作可以兼容这部分
    # 但卸载这里可以更快中断函数
    if head.next is None:
        return head

    p_prev = None
    p_node = head
    p_reversed_head = None

    while p_node != None:
        # 在翻转前保存下一节点，防止翻转时出现断链
        p_next = p_node.next
        if p_next is None:
            # 判断p_node是否为最后结点，如果是
            # 它就是翻转后链表的头结点
            p_reversed_head = p_node

        # 翻转p_prev和p_node
        p_node.next = p_prev
        # p_prev p_node 向后移动一个结点
        p_prev = p_node
        p_node = p_next

    return p_reversed_head

def test():
    values = list(range(1, 11))
    print(' '.join([str(v) for v in values]))

    head = Node(0)
    p_node = head
    for v in values:
        p_node.next = Node(v)
        p_node = p_node.next

    head = head.next
    reversed_list_head = reversed_list(head)
    p_node = reversed_list_head
    while p_node:
        print(p_node.value, end=' ')
        p_node = p_node.next

if __name__ == '__main__':
    test()
