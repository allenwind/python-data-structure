def mirror_tree(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    root.left, root.right = root.right, root.left
    if root.left:
        mirror_tree(root.left)
    if root.right:
        mirror_tree(root.right)
    return root

