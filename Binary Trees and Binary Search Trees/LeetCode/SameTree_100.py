def isSameTree(p, q):
    """
    TC: O(n)
    SC: Average Case - O(logn) | Worst Case - O(n)
    """
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return p == q

    #DFS Solution
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif node1 is None or node2 is None:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    
    return True