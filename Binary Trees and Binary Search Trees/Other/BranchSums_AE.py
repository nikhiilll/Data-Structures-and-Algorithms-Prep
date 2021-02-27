class BinaryTree:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def branchSums(root):
    """
    TC: O(n)
    SC: O(h)
    """
    result = []

    def branchSumsHelper(node, currentSum, result):

        if not node:
            return 0

        if not node.left and not node.right:
            result.append(currentSum + node.value)

        currentSum += node.value
        branchSumsHelper(node.left, currentSum, result)
        branchSumsHelper(node.right, currentSum, result)

    branchSumsHelper(root, 0, result)
    return result
