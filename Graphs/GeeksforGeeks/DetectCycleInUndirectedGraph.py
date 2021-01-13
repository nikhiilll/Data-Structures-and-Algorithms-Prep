def isCyclic(self, V, adj):
    """
    TC: O(V + E)
    SC: O(V)
    """
    visited = [False] * V

    def isCyclicHelper(node, visited, adj, parent):

        visited[node] = True

        for neighbour in adj[node]:
            if not visited[neighbour] and isCyclicHelper(neighbour, visited, adj, node):
                return True
            elif parent != neighbour:
                return True
        
        return False

    for node in range(V):
        if not visited[node]:
            if isCyclicHelper(node, visited, adj, -1):
                return True
    
    return False
