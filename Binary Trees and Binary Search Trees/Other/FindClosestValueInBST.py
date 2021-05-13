class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
TC: Worst Case: O(n) | Average Case: O(logn)
SC: O(1)
"""
def findClosestValueInBst(tree, target):

    closestValue = float("inf")
    node = tree

    while node:
        if not node:
            break
        closestValue = node.value if abs(node.value - target) < abs(closestValue - target) else closestValue
        if target == node.value:
            return node.value       
        elif target < node.value:
            node = node.left
        else:
            node = node.right
    
    return closestValue if closestValue != float("inf") else -1
        