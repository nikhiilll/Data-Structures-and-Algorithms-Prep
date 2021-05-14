"""
TC: O(logn + k)
SC: O(logn)
"""


def kthSmallest(root, k):

    previousValue = [float("-inf")]
    visitedNodes = [0]

    def kthSmallestFinder(node, previousValue, visitedNodes, k):

        if not node:
            return

        kthSmallestFinder(node.left, previousValue, visitedNodes, k)
        if visitedNodes[0] < k:
            visitedNodes[0] += 1
            previousValue[0] = node.val
            kthSmallestFinder(node.right, previousValue, visitedNodes, k)

    kthSmallestFinder(root, previousValue, visitedNodes, k)
    return previousValue[0]
