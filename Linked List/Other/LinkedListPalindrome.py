# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    """
    TC: O(n)
    SC: O(1)
    """
    length = 0
    ptr = head
    while ptr:
        length += 1
        ptr = ptr.next

    if length == 1:
        return True

    k = length // 2
    if length % 2 != 0:
        k += 1

    ptr = head
    for _ in range(1, k):
        ptr = ptr.next

    pp, pp1 = None, ptr.next

    while pp1:
        temp = pp1.next
        pp1.next = pp
        pp = pp1
        pp1 = temp

    ptr.next = pp
    ptr = head

    for _ in range(length // 2):
        if ptr.value != pp.value:
            return False
        ptr = ptr.next
        pp = pp.next

    return True
