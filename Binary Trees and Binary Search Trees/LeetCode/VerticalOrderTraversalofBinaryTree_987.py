import collections

def verticalTraversal(root):

    if not root:
        return []

    queue = collections.deque([(root, 0)])
    verticalLevel = collections.defaultdict(list)

    while queue:
        newLevel = collections.deque([])
        tempDict = collections.defaultdict(list)
        
        while queue:
            node, level = queue.popleft()
            tempDict[level].append(node.val)
            if node.left:
                newLevel.append((node.left, level - 1))
            if node.right:
                newLevel.append((node.right, level + 1))
        
        for level in tempDict:
            verticalLevel[level].extend(sorted(tempDict[level]))
        queue = newLevel
    
    return [verticalLevel[k] for k in sorted(verticalLevel)]