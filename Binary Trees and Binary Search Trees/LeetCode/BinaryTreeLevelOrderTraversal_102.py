from collections import deque
"""
TC: O(n)
SC: O(h)
"""
def levelOrder(root):

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        currentLevel = []
        for i in range(len(queue)):
            node = queue.popleft()
            currentLevel.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(currentLevel)
    
    return result