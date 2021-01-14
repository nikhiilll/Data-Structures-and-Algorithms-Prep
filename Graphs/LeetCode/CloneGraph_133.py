from collections import deque

def cloneGraph(node):
    """
    TC: O(V + E)
    SC: O(V)
    """
    if not node:
        return
    
    createdNodes = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        currNode = queue.popleft()

        for neighbor in currNode.neighbors:
            if neighbor not in createdNodes:
                queue.append(neighbor)
                createdNodes[neighbor] = Node(neighbor.val)
            createdNodes[currNode].neighbors.append(createdNodes[neighbor])
        
    return createdNodes[node]