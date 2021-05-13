class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self

        while True:
            if node.value > value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                    
                else:
                    node = node.right

        return self

    def contains(self, value):
        node = self

        while node:
            if node.value == value:
                return True
            if node.value < value:
                node = node.right
            else:
                node = node.left

        return False


    def remove(self, value, parentNode=None):

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
