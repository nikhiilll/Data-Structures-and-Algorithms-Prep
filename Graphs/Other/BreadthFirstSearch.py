from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        """
        TC: O(V + E)
        SC: O(V)
        """
        if not self:
            return array

        queue = deque([self])
        visited = set()

        while queue:
            node = queue.popleft()
            array.append(node.name)
            visited.add(node)

            for child in node.children:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        
        return array

        
