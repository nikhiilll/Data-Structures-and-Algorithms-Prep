class BinaryTree:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeHelper(node):

    if not node:
        return (True, 0)
    
    isLeftBalanced, leftHeight = binaryTreeHelper(node.left)
    if not isLeftBalanced:
        return(False, -1)

    isRightBalanced, rightHeight = binaryTreeHelper(node.right)
    if not isRightBalanced:
        return(False, -1)

    isBalanced = abs(leftHeight - rightHeight) < 2
    return (isBalanced, max(leftHeight, rightHeight) + 1)

def heightBalancedBinaryTree(tree):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    isBalanced, _ = binaryTreeHelper(tree)
    return isBalanced