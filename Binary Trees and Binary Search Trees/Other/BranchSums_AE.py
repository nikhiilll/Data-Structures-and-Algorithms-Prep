def branchSums(root):
    """
    TC: O(n)
    SC: O(n)
    """
    if not root:
        return []
    
    result = []
    return branchSumsHelper(root, result, 0)


def branchSumsHelper(node, result, parentSum):

    if not node:
        return result
    
    parentSum += node.value
    if node.left is None and node.right is None:
        result.append(parentSum)

    branchSumsHelper(node.left, result, parentSum)
    branchSumsHelper(node.right, result, parentSum)
    
    return result