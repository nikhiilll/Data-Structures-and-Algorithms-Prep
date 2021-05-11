class BinaryTree:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

"""
TC: O(n)
SC: O(h)
"""
def heightBalancedBinaryTree(tree):

    return isBalanced(tree)[1]

def isBalanced(node):

    if not node:
        return (0, True)
    
    leftHeight, isLeftBalanced = isBalanced(node.left)
    rightHeight, isRightBalanced = isBalanced(node.right)

    if isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1:
        return (max(leftHeight, rightHeight) + 1, True)
    else:
        return (-1, False)