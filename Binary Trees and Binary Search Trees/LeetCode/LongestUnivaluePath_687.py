def longestUnivaluePath(root):
    """
    TC: O(n)
    SC: O(logn)
    """
    if not root:
        return 0

    longestPath = 0
    def findLongPathAsBranch(node):
        if not node:
            return 0
        
        nonlocal longestPath

        leftLongPath = findLongPathAsBranch(node.left)
        rightLongPath = findLongPathAsBranch(node.right)
        longPathAsBranch = 0
        longPathAsRoot = 0

        if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
            longPathAsBranch = max(leftLongPath, rightLongPath) + 1
            longPathAsRoot = leftLongPath + rightLongPath + 2
        elif node.left and node.val == node.left.val:
            longPathAsBranch = leftLongPath + 1
        elif node.right and node.val == node.right.val:
            longPathAsBranch = rightLongPath + 1
        
        longestPath = max(longestPath, longPathAsBranch, longPathAsRoot)
        return longPathAsBranch
    
    findLongPathAsBranch(root)
    return longestPath


        