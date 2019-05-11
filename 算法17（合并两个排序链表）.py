import random
from common import build_linked_list, traverse_list

# 1. 合并两个排序链表
# 2. 合并多个排序链表

def merge_two_sorted_list(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = None
    if l1.value > l2.value:
        head = l2
        head.next = merge_two_sorted_list(l1, l2.next)
    else:
        head = l1
        head.next = merge_two_sorted_list(l1.next, l2)
    return head

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

def merge_sorted_lists(lists):
    head = find_min_node(lists)
    p_node = head
    while lists:
        p_node.next = find_min_node(lists)
        p_node = p_node.next
    return head

def testing():
    l1 = build_linked_list(sorted(random.sample(range(10), 5)))
    l2 = build_linked_list(sorted(random.sample(range(10), 5)))

    for n in traverse_list(l1):
        print(n)
    print('='*10)
    for n in traverse_list(l2):
        print(n)
    print('='*10)
    l = merge_two_sorted_list(l1, l2)
    for n in traverse_list(l):
        print(n)

def testing2():
    l1 = build_linked_list(sorted(random.sample(range(20), 5)))
    l2 = build_linked_list(sorted(random.sample(range(20), 5)))
    l3 = build_linked_list(sorted(random.sample(range(20), 5)))
    head = merge_lists([l1, l2, l3])
    for i in traverse_list(head):
        print(i, end=' ')

if __name__ == '__main__':
    testing()
    print('='*10)
    testing2()
