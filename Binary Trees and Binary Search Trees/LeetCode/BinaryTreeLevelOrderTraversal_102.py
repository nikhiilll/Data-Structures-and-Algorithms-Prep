def levelOrder(root):
    """
    TC: O(n)
    SC: O(n)
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        tempNodes = []
        tempValues = []
        for element in queue:
            tempValues.append(element.val)
            if element.left:
                tempNodes.append(element.left)
            if element.right:
                tempNodes.append(element.right)
        result.append(tempValues)
        queue = tempNodes

    return result