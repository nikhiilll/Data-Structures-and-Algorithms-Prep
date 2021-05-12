def isSubTree(root, subRoot):

    dfsRoot = []
    stack = [root]
    nodeIndex = None

    while stack:
        node = stack.pop()
        if node is None:
            dfsRoot.append(node)
            continue
        dfsRoot.append(node.val)
        if node.val == subRoot.val:
            nodeIndex = len(dfsRoot) - 1
        stack.append(node.right)
        stack.append(node.left)
    
    if nodeIndex is None:
        return False
    
    stack = [subRoot]
    while stack and nodeIndex < len(dfsRoot):
        node = stack.pop()
        if not node and not dfsRoot[nodeIndex]:
            nodeIndex += 1
            continue
        if (not node and dfsRoot[nodeIndex]) or (node and not dfsRoot[nodeIndex]) or (node.val != dfsRoot[nodeIndex]):
            return False
        stack.append(node.right)
        stack.append(node.left)
        nodeIndex += 1
    
    return len(stack) == 0
