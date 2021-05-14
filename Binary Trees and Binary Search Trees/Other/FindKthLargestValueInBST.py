class BST:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
"""
TC: O(n)
SC: O(h)
"""
def findKthLargestValueInBst(tree, k):

    found = [False]
    kthLargest = [None]

    findKthLargestValueInBstHelper(tree, 0, k, found, kthLargest)
    return kthLargest[0]

def findKthLargestValueInBstHelper(node, currentK, k, found, kthLargest):

    if not node:
        return currentK
    
    if found[0]:
        return
    
    currentK = findKthLargestValueInBstHelper(node.right, currentK, k, found, kthLargest)
    if found[0]:
        return
    currentK += 1
    if currentK == k:
        found[0] = True
        kthLargest[0] = node.value
        return
    
    return findKthLargestValueInBstHelper(node.left, currentK, k, found, kthLargest)
    

def reverseInOrderTraversal(node, k, nodesVisited, previousValue):

    if node is None or nodesVisited >= k:
        return
    
    reverseInOrderTraversal(node.right, k, nodesVisited, previousValue)
    if nodesVisited < k:
        nodesVisited += 1
        previousValue = node.value
        reverseInOrderTraversal(node.left, k, nodesVisited, previousValue)