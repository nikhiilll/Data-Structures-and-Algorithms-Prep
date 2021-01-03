from collections import deque

def rightView(root):
    '''
    :param root: root of given tree.
    :return: the right view of tree,
    '''
    if not root:
        return []
        
    queue = deque([root])
    rView = []

    while queue:
        rView.append(queue[0].data)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return rView