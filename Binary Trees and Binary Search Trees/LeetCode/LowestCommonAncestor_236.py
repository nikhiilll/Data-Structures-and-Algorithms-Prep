def lowestCommonAncestor(root, p, q):

    if not root:
        return
    
    def lcaHelper(node, nodeP, nodeQ):

        if not node:
            return (0, None)
        
        leftResult = lcaHelper(node.left, nodeP, nodeQ)
        if leftResult[0] == 2:
            return leftResult
        
        rightResult = lcaHelper(node.right, nodeP, nodeQ)
        if rightResult[0] == 2:
            return rightResult
        
        nodesFound = leftResult[0] + rightResult[0] + int(node is nodeP) + int(node is nodeQ)
        return(nodesFound, node if nodesFound == 2 else None)
    
    return lcaHelper(root, p, q)[1]
        
