class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def diameterHelper(node):

    if not node:
        return (0, 0)
    
    leftBranchPath, leftBranchDiameter = diameterHelper(node.left)
    rightBranchPath, rightBranchDiameter = diameterHelper(node.right)

    maxBranchPath = max(leftBranchPath, rightBranchPath)
    pathAsRoot = leftBranchPath + rightBranchPath + 1
    maxDiameter = max(leftBranchDiameter, rightBranchDiameter, pathAsRoot, maxBranchPath)

    return (maxBranchPath, maxDiameter)

def binaryTreeDiameter(tree):

    if not tree:
        return -1
    
    return diameterHelper(tree)[1]
