class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def validateBst(node, minValue=float("-inf"), maxValue=float("inf")):

    if not node:
        return True
    
    if node.value < minValue or node.value >= maxValue:
        return False
    
    return validateBst(node.left, minValue, node.value) and validateBst(node.right, node.value, maxValue)