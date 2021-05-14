class BST:

    def __init__(self, value, greaterThan=0):
        self.value = value
        self.greaterThan = greaterThan
        self.left = 0
        self.right = 0


def rightSmallerThan(array):

    smallerThan = [0] * len(array)
    root = BST(float("-inf"), -1)

    for i in range(len(array) - 1, -1, -1):
        currentNode = root
        parentNode = None
        greaterThan = 0
        while currentNode:
            if currentNode.value >= array[i]:
                parentNode = currentNode

                if currentNode.value == array[i]:
                    greaterThan += currentNode.greaterThan
                    currentNode.greaterThan += 1
                    break
                currentNode.greaterThan += 1
                currentNode = currentNode.left
            else:
                greaterThan += currentNode.greaterThan + 1
                parentNode = currentNode
                currentNode = currentNode.right

        smallerThan[i] = greaterThan
        node = BST(array[i], 0)
        if parentNode.value > node.value:
            parentNode.left = node
        elif parentNode.value < node.value:
            parentNode.right = node

    return smallerThan
