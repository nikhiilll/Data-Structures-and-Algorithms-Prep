def removeDuplicatesFromLinkedList(linkedList):
    """
    TC: O(n)
    SC: O(1)
    """
    ptr = linkedList

    while ptr:
        nextPtr = ptr.next
        while nextPtr and nextPtr.value == ptr.value:
            nextPtr = nextPtr.next
        ptr.next = nextPtr
        ptr = nextPtr
    
    return linkedList
