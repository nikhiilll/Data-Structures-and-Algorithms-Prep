def pathSum(root, targetSum):

    if not root:
        return []

    stack = [(root, targetSum - root.val, [root.val])]
    answer = []

    while stack:
        node, currentSum, currentPath = stack.pop()
        if not node.left and not node.right and currentSum == 0:
            answer.append(currentPath)
        if node.left:
            stack.append((node.left, currentSum + node.left.val, currentPath + [node.left.val]))
        if node.right:
            stack.append((node.right, currentSum + node.right.val, currentPath + [node.right.val]))
        
    return answer

