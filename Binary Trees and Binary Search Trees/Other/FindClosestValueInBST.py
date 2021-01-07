def findClosestValueInBst(tree, target):
    """
    TC: Average Case - O(logn) | Worst Case - O(n)
    SC: O(1)
    """
    closestValue = float("inf")
    currentNode = tree

    while currentNode:
        closestValue = currentNode.value if abs(closestValue - target) > abs(currentNode.value - target) else closestValue
        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break
    
    return closestValue

