def buildTree(preorder, inorder):
    """
    TC: O(n)
    SC: O(n + logn)
    """
    inorderDict = {}
    for i, num in enumerate(inorder):
        inorderDict[num] = i

    preorderIter = iter(preorder)

    def build(start, end):
        if start > end:
            return None
        rootValue = next(preorderIter)
        root = TreeNode(rootValue)
        rootIndex = inorderDict[rootValue]
        root.left = build(start, rootIndex - 1)
        root.right = build(rootIndex + 1, end)
        return root
    
    return build(0, len(inorder) - 1)