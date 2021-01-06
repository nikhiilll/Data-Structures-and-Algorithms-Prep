def nodeDepths(root, currentDepth = 0):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    if not root:
        return 0
    return currentDepth + nodeDepths(root.left, currentDepth + 1) + nodeDepths(root.right, currentDepth + 1) 