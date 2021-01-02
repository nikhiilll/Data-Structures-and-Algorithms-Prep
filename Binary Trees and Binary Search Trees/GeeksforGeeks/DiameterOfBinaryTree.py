def diameter(root):

    if not root:
        return 0
    
    maxPath = float("-inf")

    def findMaxPath(node):

        nonlocal maxPath
        if not node:
            return 0
        
        leftBranchLength = findMaxPath(node.left)
        rightBranchLength = findMaxPath(node.right)
        maxPathAsBranch = max(leftBranchLength, rightBranchLength) + 1
        maxPathAsRoot = leftBranchLength + rightBranchLength
        maxPath = max(maxPath, maxPathAsRoot)

        return maxPathAsBranch
    
    findMaxPath(root)
    return maxPath