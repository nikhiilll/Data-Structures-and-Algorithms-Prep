class BinaryTree:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, k):

    nodesDistanceK = []
    findDistanceFromNodeToTarget(tree, target, k, nodesDistanceK)
    return nodesDistanceK

def findDistanceFromNodeToTarget(node, target, k, nodesDistanceK):

    