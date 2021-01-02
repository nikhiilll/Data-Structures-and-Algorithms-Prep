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
        maxPathAsRoot = max(maxPathAsBranch, leftBranchLength + rightBranchLength + 1)
        maxPath = max(maxPath, maxPathAsRoot)

        return maxPathAsBranch
    
    findMaxPath(root)
    return maxPath