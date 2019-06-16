def search_recursive(bst, target):
    if not bst:
        return 
    if bst.key == target:
        return bst.value
    elif bst.key < target:
        search(bst.right, target)
    else:
        search(bst.left, target)

def search(bst, target):
    if not bst:
        return
    p_node = bst
    while p_node:
        if p_node.key == target:
            return p_node.value
        elif p_node.key < target:
            p_node = p_node.right
        else:
            p_node = p_node.left

def insert(bst, node):
    if not bst:
        return node
    p_node = bst
    while p_node:
        if p_node.key == target.key:
            p_node.value = target.value
            return bst
        elif p_node.key < target.key:
            if p_node.right is None:
                p_node.right = node
                return bst
            else:
                p_node = p_node.right
        else:
            if p_node.left is None:
                p_node.left = node
                return bst
            else:
                p_node = p_node.left

def insert_recursive(bst, node):
    pass

def _find_max(node):
    while node:


def delete(bst, key):
    if not bst:
        return False






    
