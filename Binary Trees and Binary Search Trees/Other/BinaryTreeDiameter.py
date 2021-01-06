def binaryTreeDiameter(tree):
    """
    TC: O(n)
    SC: O(h)
    """
    if not tree:
        return -1
    
    maxDiameter = [0]
    findMaxDiameter(tree, maxDiameter)
    return maxDiameter[0]

def findMaxDiameter(node, maxDiameter):

    if not node:
        return 0
    
    leftDiameter = findMaxDiameter(node.left, maxDiameter)
    rightDiameter = findMaxDiameter(node.right, maxDiameter)
    diameterAsBranch = max(leftDiameter, rightDiameter)
    diameterAsRoot = leftDiameter + rightDiameter
    maxDiameter[0] = max(maxDiameter[0], diameterAsBranch, diameterAsRoot)

    return diameterAsBranch + 1