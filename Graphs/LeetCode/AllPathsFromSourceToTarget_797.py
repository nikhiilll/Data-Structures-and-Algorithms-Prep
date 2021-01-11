def allPathsSourceTarget(self, graph):

    def dfs(currentNode, currentPath):
        if currentNode == len(graph) - 1:
            result.append(currentPath)
        else:
            for i in graph[currentNode]:
                dfs(i, currentPath + [i])
    result = []
    dfs(0, [0])
    return result
