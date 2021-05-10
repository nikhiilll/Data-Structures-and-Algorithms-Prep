class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
TC: O(n)
SC: O(h)
"""
def invertBinaryTree(tree):

    if not tree:
        return
    
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree