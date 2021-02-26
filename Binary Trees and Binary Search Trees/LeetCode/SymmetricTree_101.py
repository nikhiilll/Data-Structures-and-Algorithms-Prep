def isSymmetric(root):

    if not root:
        return False
    

    def isSymmetricHelper(node1, node2):

        if not node1 and not node2:
            return True
        elif (not node1 and node2) or (node1 and not node2):
            return False
        else:
            return isSymmetricHelper(node1.left, node2.right) and isSymmetricHelper(node1.right, node2.left) and node1.val == node2.val


    return isSymmetricHelper(root.left, root.right)