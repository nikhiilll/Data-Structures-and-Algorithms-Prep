def binaryTreePaths(root):
    """
    TC: O(n)
    SC: O(E), where 
    """
            
    result = []

    def rootToLeafPaths(node, result, parentPath):

        if not node:
            return

        if parentPath != "":
            parentPath += "->" + str(node.val)
        else:
            parentPath = str(node.val)
        if node.left is None and node.right is None:
            result.append(parentPath)
        else:
            rootToLeafPaths(node.left, result, parentPath)
            rootToLeafPaths(node.right, result, parentPath)
        return

    rootToLeafPaths(root, result, "")
    return result