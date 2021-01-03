from collections import deque

def topView(root):
    """
    TC: O(n)
    SC: O(n)
    """
    if not root:
        return
    
    hDepthMap = {}
    hDepth = 0
    queue = deque([(root, 0)])

    while queue:
        node = queue.popleft()
        hDepth = node[1]

        if hDepth not in hDepthMap:
            hDepthMap[hDepth] = node[0].data
        
        if node[0].left:
            queue.append((node[0].left, hDepth - 1))
        
        if node[0].right:
            queue.append((node[0].right, hDepth + 1))
    
    for k in sorted(hDepthMap):
        print(hDepthMap[k], end = "")

    
        