def findSuccessor(tree, node):

    traversal = []
    inOrderTraversal(tree, traversal)

    for i, n in enumerate(traversal):
        if i == len(traversal) - 1:
            return
        elif n == node:
            return traversal[i]
    
    return None

def inOrderTraversal(node, traversal):

    if not node:
        return

    inOrderTraversal(node.left, traversal)
    traversal.append(node)
    inOrderTraversal(node.right, traversal)
