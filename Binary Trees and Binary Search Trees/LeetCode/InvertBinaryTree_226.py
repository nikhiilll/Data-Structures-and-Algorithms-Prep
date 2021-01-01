import collections

def invertTree(root):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    if not root:
        return
    
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root

    #DFS
    stack = [root]

    while stack:
        node = stack.pop()

        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)
    
    return root

    #BFS
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    
    return root