def minHeightBst(array):

    return minHeightBSTHelper(array, 0, len(array) - 1)


def minHeightBSTHelper(array, start, end):

    if start > end:
        return None

    mid = (start + end) // 2
    midNode = BST(array[mid])
    midNode.left = minHeightBSTHelper(array, start, mid - 1)
    midNode.right = minHeightBSTHelper(array, mid + 1, end)
    return midNode


class BST:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
