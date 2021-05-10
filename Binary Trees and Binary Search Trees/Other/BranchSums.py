class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
TC: O(n)
SC: O(n)
"""
def branchSums(root):

    if not root:
        return []

    branchSumsList = []
    branchSumsHelper(root, 0, branchSumsList)
    return branchSumsList

def branchSumsHelper(node, parentSum, branchSumsList):

    if not node:
        return 0
    
    if not node.left and not node.right:
        branchSumsList.append(node.value + parentSum)
        return
    
    branchSumsHelper(node.left, parentSum + node.value, branchSumsList)
    branchSumsHelper(node.right, parentSum + node.value, branchSumsList)