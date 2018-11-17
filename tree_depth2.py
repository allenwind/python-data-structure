def tree_depth(root):
    if root is None:
        return 0
    n_left = tree_depth(root.left)
    n_right = tree_depth(root.right)

    return (n_left+1) if n_left > n_right else (n_rigth+1)
