class BST:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):

    if not preOrderTraversalValues:
        return None
    
    if len(preOrderTraversalValues) == 1:
        return BST(preOrderTraversalValues[0])
    
    currentRootNode = BST(preOrderTraversalValues[0])
    rightNode = 1
    while rightNode < len(preOrderTraversalValues):
        if preOrderTraversalValues[rightNode] >= currentRootNode.value:
            break
        rightNode += 1
    
    currentRootNode.left = reconstructBst(preOrderTraversalValues[1:rightNode])
    currentRootNode.right = reconstructBst(preOrderTraversalValues[rightNode:])

    return currentRootNode

    
