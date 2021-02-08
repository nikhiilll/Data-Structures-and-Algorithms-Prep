def isOutOfOrder(i, array):

    if i == 0:
        return array[i] > array[i + 1]
    elif i == len(array) - 1:
        return array[i] < array[i - 1]
    else:
        return array[i - 1] > array[i] or array[i + 1] < array[i]

def subarraySort(array):

    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        if isOutOfOrder(i, array):
            minOutOfOrder = min(minOutOfOrder, array[i])
            maxOutOfOrder = max(maxOutOfOrder, array[i])
    
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    
    leftIndex = 0
    while minOutOfOrder >= array[leftIndex]:
        leftIndex += 1
    rightIndex = len(array) - 1
    while maxOutOfOrder <= array[rightIndex]:
        rightIndex -= 1
    
    return [leftIndex, rightIndex]