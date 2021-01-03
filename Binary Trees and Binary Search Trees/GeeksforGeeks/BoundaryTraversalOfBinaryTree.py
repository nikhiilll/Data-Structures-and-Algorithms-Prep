def printBoundaryView(root):

    if not root:
        return []

    boundary = [root.data]

    def printLeftMostNodes(node, boundary):

        if not node:
            return
        if node.left:
            boundary.append(node.data)
            printLeftMostNodes(node.left, boundary)
        elif node.right:
            boundary.append(node.data)
            printLeftMostNodes(node.right, boundary)
    
    def printRightMostNodes(node, boundary):

        if not node:
            return
        if node.right:
            printRightMostNodes(node.right, boundary)   
            boundary.append(node.data)
        elif node.left:
            printRightMostNodes(node.left, boundary)   
            boundary.append(node.data)
    
    def printLeafNodes(node, boundary):

        if not node:
            return
        elif not node.left and not node.right:
            boundary.append(node.data)
            return
        else:
            printLeafNodes(node.left, boundary)
            printLeafNodes(node.right, boundary)
    
    printLeftMostNodes(root.left, boundary)
    printLeafNodes(root, boundary)
    printRightMostNodes(root.right, boundary)

    return boundary

