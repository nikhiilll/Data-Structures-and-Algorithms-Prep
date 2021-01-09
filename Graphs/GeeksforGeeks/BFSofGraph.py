from collections import deque

def bfsOfGraph(V, adj):
    """
    TC: O(V+E)
    SC: O(V)
    """
    if V == 0:
        return []
    
    bfs = []
    queue = deque([0])
    visited = [False] * V

    while queue:
        node = queue.popleft()
        visited[node] = True
        bfs.append(node)

        for neighbour in adj[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

    return bfs
