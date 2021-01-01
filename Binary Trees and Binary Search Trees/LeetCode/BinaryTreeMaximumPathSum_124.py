def maxPathSum(root):

    maxPathSum = float("-inf")

    def findMaxPath(node):

        if node is None:
            return 0

        nonlocal maxPathSum

        leftSum = findMaxPath(node.left)
        rightSum = findMaxPath(node.right)
        maxSumAsBranch = max(max(leftSum, rightSum) + node.val, node.val)
        maxSumAsRoot = max(maxSumAsBranch, leftSum + rightSum + node.val)
        maxPathSum = max(maxPathSum, maxSumAsRoot)

        return maxSumAsBranch
    
    findMaxPath(root)
    return maxPathSum