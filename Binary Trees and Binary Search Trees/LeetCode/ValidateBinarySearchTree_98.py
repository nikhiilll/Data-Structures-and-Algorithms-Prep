def isValidBST(root, minValue = float("-inf"), maxValue = float("inf")):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    if not root:
        return True
    elif minValue < root.val < maxValue:
        return isValidBST(root.left, minValue, root.val) and isValidBST(root.right, root.val, maxValue)
    else:
        return False