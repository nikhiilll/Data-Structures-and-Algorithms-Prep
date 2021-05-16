"""
TC: O(v + e)
SC: O(v)
"""


def depthFirstSearch(self, array):

    if not self:
        return array

    stack = [self]
    while stack:
        node = stack.pop()
        array.append(node.name)
        for i in range(len(node.children) - 1, -1, -1):
            stack.append(node.children[i])

    return array
