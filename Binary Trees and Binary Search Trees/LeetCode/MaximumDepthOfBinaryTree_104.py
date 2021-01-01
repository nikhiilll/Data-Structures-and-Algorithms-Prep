def maxDepth(root):
    """
    TC: O(n)
    SC: Average case - O(logn) | Worst Case: O(n) -- In case all the nodes of the tree are on one side.
    """
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))