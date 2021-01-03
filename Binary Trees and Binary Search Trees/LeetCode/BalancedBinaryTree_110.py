def isBalanced(root):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    def check(root):
        if not root:
            return (0, True)
        lDepth, lBalanced = check(root.left)
        rDepth, rBalanced = check(root.right)
        return max(lDepth, rDepth) + 1, lBalanced and rBalanced and abs(lDepth - rDepth) < 2
    
    return check(root)[1]
