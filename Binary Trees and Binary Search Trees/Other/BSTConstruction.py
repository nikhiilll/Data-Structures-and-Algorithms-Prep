class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """
    TC: Average Case - O(logn) | Worst Case - O(n)
    SC: O(1)
    """
    def insert(self, value):
        currentNode = self
        while True:
            if currentNode.value > value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break
        
        return self

    """
    TC: Average Case - O(logn) | Worst Case - O(n)
    SC: O(1)
    """
    def contains(self, value):
        currentNode = self

        while currentNode:
            if currentNode.value > value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                return True
        
        return False

    """
    TC: Average Case - O(logn) | Worst Case - O(n)
    SC: O(1)
    """
    def remove(self, value, parentNode = None):

        currentNode = self
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left and currentNode.right:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right else currentNode.left
            
                break
        
        return self
        
    def getMinValue(self):
        currentNode = self
        while currentNode.left:
            currentNode = currentNode.left
        
        return currentNode.value