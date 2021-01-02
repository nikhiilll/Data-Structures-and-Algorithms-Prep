import collections

def levelOrder(root):
    """
    TC: O(n)
    SC: O(n)
    """
    queue = collections.deque([ root ])
    result = []

    while queue:
        node = queue.popleft()
        if not node:
            # result.append("N")
            continue
        result.append(node.data)
        queue.append(node.left)
        queue.append(node.right)
    
    return result
        
