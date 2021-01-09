def depthFirstSearch(self, array):
    """
    TC: O(V + E)
    SC: O(V)
    """
    node = self
    if not node:
        return array
    
    visited = set()
    stack = [node]

    while stack:
        node = stack.pop()
        visited.add(node)
        array.append(node.name)

        for neighbour in reversed(node.children):
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
    
    return array