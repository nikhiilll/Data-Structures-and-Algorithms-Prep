def isCyclic(self, V, adj):
    """
    TC: O(V + E)
    SC: O(V)
    """
    visited = ["White"] * V

    def isCyclicHelper(node, visited, adj):

        if visited[node] == "Black":
            return False

        visited[node] = "Gray"
        for neighbour in adj[node]:
            if visited[neighbour] == "Gray":
                return True
            elif visited[neighbour] == "White" and isCyclicHelper(neighbour, visited, adj):
                return True
        
        visited[node] = "Black"
        return False

    for node in range(V):
        if visited[node] == "White":
            if isCyclicHelper(node, visited, adj):
                return True
    
    return False
