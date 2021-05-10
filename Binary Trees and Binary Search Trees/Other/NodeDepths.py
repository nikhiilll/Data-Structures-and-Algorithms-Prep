class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
TC: O(n)
SC: O(h)
"""
def nodeDepths(root):

    if not root:
        return 0
    
    depth = [0]
    nodeDepthsHelper(root.left, 0, depth)
    nodeDepthsHelper(root.right, 0, depth)
    return depth[0]

def nodeDepthsHelper(node, parentDepth, depth):

    if not node:
        return 
    
    currentDepth = parentDepth + 1
    depth[0] += currentDepth
    
    nodeDepthsHelper(node.left, currentDepth, depth)
    nodeDepthsHelper(node.right, currentDepth, depth)


def nodeDepths(root, currentDepth = 0):

    if not root:
        return 0
    return currentDepth + nodeDepths(root.left, currentDepth + 1) + nodeDepths(root.right, currentDepth + 1) 
