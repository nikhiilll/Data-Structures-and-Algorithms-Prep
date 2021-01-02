from collections import deque

def reverseLevelOrder(root):

    queue = deque([root])
    result = []

    while queue:
        temp = []
        levels = []
        for element in queue:
            temp.append(element.data)
            if element.left:
                levels.append(element.left)
            if element.right:
                levels.append(element.right)
        result.append(temp)
        queue = levels

    finalresult = []
    for element in reversed(result):
        finalresult.extend(element)

    return finalresult    
