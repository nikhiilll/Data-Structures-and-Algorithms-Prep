"""
TC: O(n)
SC: O(h)
"""
def isSameTree(p, q):
        # if not p and not q:
        #     return True
        
        # if (not p and q) or (p and not q) or (p.val != q.val): 
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    stackP = [p]
    stackQ = [q]

    while stackP and stackQ:
        nodeP = stackP.pop()
        nodeQ = stackQ.pop()
        if not nodeP and not nodeQ:
            continue

        if (not nodeP and nodeQ) or (nodeP and not nodeQ) or (nodeP.val != nodeQ.val):
            return False
        stackP.append(nodeP.right)
        stackP.append(nodeP.left)
        stackQ.append(nodeQ.right)
        stackQ.append(nodeQ.left)
    
    return len(stackP) == len(stackQ)

    