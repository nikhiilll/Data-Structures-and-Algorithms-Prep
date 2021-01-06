def flattenBinaryTree(root):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    ptr = [None]
    newHead = [None]

    def flattenBTHelper(newHead, ptr, node):

        if not node:
            return
        
        flattenBTHelper(newHead, ptr, node.left)
        if newHead[0] is None and ptr[0] is None:
            newHead[0] = node
            ptr[0] = node
        else:
            ptr[0].right = node
            node.left = ptr[0]
            ptr[0] = node
        flattenBTHelper(newHead, ptr, node.right)
    
        return

    flattenBTHelper(newHead, ptr, root)
    return newHead[0]