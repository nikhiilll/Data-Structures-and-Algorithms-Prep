from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSortUtil(self, v, visited, stack):
        
        visited[v] = True

        for n in self.graph[v]:
            if not visited[n]:
                self.topologicalSortUtil(n, visited, stack)
        
        stack.append(v)
    
    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        
        return stack[::-1]
