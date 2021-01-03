from collections import deque

def zigzagLevelOrder(root):

    if not root:
        return []

    result = []
    queue = deque([root])
    counter = 0

    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if counter % 2 == 0:
            result.append(temp)
        else:
            result.append(temp[::-1])
        counter += 1
    
    return result
