def sumRootToLeaf(root, partialPathSum = 0):

    if not root:
        return 0
    
    partialPathSum = partialPathSum * 2 + root.val
    if not root.left and not root.right:
        return partialPathSum
    
    return(sumRootToLeaf(root.left, partialPathSum) + sumRootToLeaf(root.right, partialPathSum))