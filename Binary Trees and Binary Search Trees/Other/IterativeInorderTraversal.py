def iterativeInOrderTraversal(tree, callback):
    
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
