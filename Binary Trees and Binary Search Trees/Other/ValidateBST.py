def validateBst(tree):

    if not tree:
        return False
    
    return isValidBstNode(tree.left, float("-inf"), tree.value) and isValidBstNode(tree.right, tree.value, float("inf")) 
    
    
def isValidBstNode(node, minValue, maxValue):

    if not node:
        return True
    
    if minValue < node.value < maxValue:
        return  isValidBstNode(node.left, minValue, node.value) and isValidBstNode(node.right, node.value, maxValue)
    else:
        return False