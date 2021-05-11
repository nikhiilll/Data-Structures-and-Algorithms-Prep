class BinaryTree:

    def __init__(self, value, left = None, right = None, parent = None):

        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
def findSuccessor(tree, node):
    if not node:
        return None

    if node.right:
        return leftMostChild(node.right)

    return rightMostParent(node)

def leftMostChild(node):

    currentNode = node
    while currentNode.left:
        currentNode = currentNode.left

    return currentNode

def rightMostParent(node):

    currentNode = node
    while currentNode.parent and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent   