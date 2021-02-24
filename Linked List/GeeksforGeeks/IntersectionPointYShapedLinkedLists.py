def intersectionPoint(head1, head2):
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
    
    l1, l2 = countLength(head1), countLength(head2)
    if l2 < l1:
        head1, head2 = head2, head1
        l1, l2 = l2, l1
    
    ptr1, ptr2 = head1, head2
    for _ in range(abs(l2 - l1)):
        ptr2 = ptr2.next
    
    while ptr1 and ptr2 and ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1.data
