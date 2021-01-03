from collections import deque

def rightSideView(root):
    """
    TC: O(n)
    SC: O(n)
    """
    if not root:
        return []
        
    queue = deque([root])
    rView = []

    while queue:
        rView.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return rView
    