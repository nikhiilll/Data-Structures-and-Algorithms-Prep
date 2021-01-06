def iterativeInOrderTraversal(tree, callback):
    """
    TC: O(n)
    SC: O(1)
    """
    previousNode = None
    currentNode = tree

    while currentNode:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right else currentNode.parent
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right else currentNode.parent
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode
