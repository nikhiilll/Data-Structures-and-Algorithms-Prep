def maxPathSum(tree):
    """
    TC: O(n)
    SC: O(h)
    """
    if tree is None:
        return 0

    maxSum = [float("-inf")]
    findMaxPathSum(tree, maxSum)
    return maxSum[0]

def findMaxPathSum(node, maxSum):

    if not node:
        return 0
    
    leftBranchSum = findMaxPathSum(node.left, maxSum)
    rightBranchSum = findMaxPathSum(node.right, maxSum)

    maxSumAsBranch = max(leftBranchSum, rightBranchSum) + node.value
    maxSumAsRoot = max(leftBranchSum + rightBranchSum + node.value, node.value)
    maxSumThroughNode = max(maxSumAsBranch, maxSumAsRoot)
    maxSum[0] = max(maxSum[0], maxSumThroughNode)

    return maxSumAsBranch
