def lowestCommonAncestor(root, p, q):
    """
    TC: O(n)
    SC: O(1)
    """
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root