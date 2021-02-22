class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    """
    TC: O(n or m)
    SC: O(n or m)
    """
    head = ptr = LinkedList(0)
    ptr1, ptr2 = linkedListOne, linkedListTwo

    carry = 0
    while ptr1 or ptr2 or carry != 0:
        value1 = ptr1.value if ptr1 else 0
		value2 = ptr2.value if ptr2 else 0
		
		unitSum = value1 + value2 + carry
        carry = unitSum // 10
        ptr.next = LinkedList(unitSum % 10)
        ptr = ptr.next
		
		ptr1 = ptr1.next if ptr1 else None
		ptr2 = ptr2.next if ptr2 else None
		
    
    return head.next

