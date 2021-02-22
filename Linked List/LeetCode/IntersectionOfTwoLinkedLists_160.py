def getIntersectionNode(headA, headB):
    """
    TC: O(n)
    SC: O(1)
    """
    def countLength(ptr):

        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        
        return count
    
    if not headA or not headB:
        return None
    
    aL, bL = countLength(headA), countLength(headB)
    if aL > bL:
        headA, headB = headB, headA
    for _ in range(abs(aL - bL)):
        headB = headB.next
    
    while headA and headB and headA is not headB:
        headA, headB = headA.next, headB.next
    
    return headA
    
