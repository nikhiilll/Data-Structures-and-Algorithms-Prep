class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
TC: O(n)
SC: O(h)
"""
def binaryTreeDiameter(tree):

    _, maxDiameter = binaryTreeDiameterHelper(tree)
    return maxDiameter

def binaryTreeDiameterHelper(node):
    
    if not node:
        return (0, 0)
    
    leftBranch, leftDiameter = binaryTreeDiameterHelper(node.left)
    rightBranch, rightDiameter = binaryTreeDiameterHelper(node.right)

    maxDiameter = max(leftDiameter, rightDiameter, leftBranch + rightBranch)
    maxBranch = max(leftBranch, rightBranch) + 1

    return (maxBranch, maxDiameter)
