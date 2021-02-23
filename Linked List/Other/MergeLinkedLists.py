# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):

    ptr1, ptr2, prevPtr1 = headOne, headTwo, None

    while ptr1 and ptr2:
        if ptr1.value < ptr2.value:
            prevPtr1 = ptr1
            ptr1 = ptr1.next
        else:
            if prevPtr1 is not None:
                prevPtr1.next = ptr2
            prevPtr1 = ptr2
            ptr2 = ptr2.next
            prevPtr1.next = ptr1
    
    if ptr1 is None:
        prevPtr1.next = ptr2

    return headOne if headOne.value < headTwo.value else headTwo
