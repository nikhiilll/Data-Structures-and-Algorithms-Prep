import collections

def levelOrderBottom(root):

    if not root:
        return []

    queue = collections.deque([ root ])
    result = []

    while queue:
        temp = []
        levels = []
        for element in queue:
            if not element:
                continue
            if element.left:
                levels.append(element.left)
            if element.right:
                levels.append(element.right)
            temp.append(element)
        result.append(temp)
        queue = levels
    
    return reversed(result)
        