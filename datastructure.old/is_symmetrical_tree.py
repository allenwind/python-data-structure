def is_symmetrical(root):
    return _do(root, root)

def _do(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    return _do(root1.left, root1.right) and _do(root2.left, root2.right)
