def isSubtree(s, t):
    """
    TC: O(nm)
    SC: O(n*logm)
    """
    def isIdentical(root1, root2):

        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return (root1.val == root2.val) and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

    #Could have also used the same tree solution from LC Question no 100.
    # def isSameTree(p, q):
    # if p and q:
    #     return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    # else:
    #     return p == q

    stack = [s]
    while stack:
        node = stack.pop()
        if node.val == t.val:
            if(isIdentical(node, t)):
                return True
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return False