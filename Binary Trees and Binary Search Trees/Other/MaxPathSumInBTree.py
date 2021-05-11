def maxPathSum(tree):

    return maxPathSumHelper(tree)[1]

"""
TC: O(n)
SC: O(h)
"""
def maxPathSumHelper(node):

    if not node:
        return (0, float("-inf"))
    
    leftPathBranchSum, leftPathMaxSum = maxPathSumHelper(node.left)
    rightPathBranchSum, rightPathMaxSum = maxPathSumHelper(node.right)
    maxBranch = max(leftPathBranchSum, rightPathBranchSum)

    maxBranchSum = max(maxBranch + node.value, node.value)
    maxPathSumAsRoot = max(leftPathBranchSum + rightPathBranchSum + node.value, maxBranchSum)
    maxPathSum = max(leftPathMaxSum, rightPathMaxSum, maxPathSumAsRoot)


    return(maxBranchSum, maxPathSum)