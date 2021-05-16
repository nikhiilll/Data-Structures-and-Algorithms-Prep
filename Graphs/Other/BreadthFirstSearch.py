from collections import deque
"""
TC: O(v+e)
SC: O(v)
"""


def breadthFirstSearch(self, array):

    queue = deque([self])

    while queue:
        node = queue.popleft()
        array.append(node.name)
        for child in node.children:
            queue.append(child)

    return array
