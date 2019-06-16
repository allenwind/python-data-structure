import collections

from binary_search_tree import BinarySearchTree

def print_tree_step(tree):
    stack = collections.deque()
    stack.append(tree)
    next_level_count = 0
    current_print_count = 1

    while len(stack):
        p_node = stack.popleft()
        print(p_node, end='\t')
        current_print_count -= 1
        if p_node.left is not None:
            next_level_count += 1
            stack.append(p_node.left)
        if p_node.right is not None:
            next_level_count += 1
            stack.append(p_node.right)
        if current_print_count == 0:
            current_print_count = next_level_count
            next_level_count = 0
            print('\n')

if __name__ == '__main__':
    tree = BinarySearchTree()
    for i in [8, 6, 10, 5, 7, 9, 11]:
        tree.insert(i, i)

    print_tree_step(tree._root)
