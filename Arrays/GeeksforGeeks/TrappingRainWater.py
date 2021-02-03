def trappingWater(arr, n):
    """
    TC: O(n)
    SC: O(n)
    """
    leftArray = [-1] * n
    rightArray = [-1] * n

    calculateLeftArray(leftArray, arr, n)
    calculateRightArray(rightArray, arr, n)

    result = 0
    for i in range(n):
        if leftArray[i] != -1 and rightArray[i] != -1:
            result += (min(leftArray[i], rightArray[i]) - arr[i])
    
    return result


def calculateLeftArray(leftArray, arr, n):

    leftHigh = 0
    for i in range(n):
        if leftHigh > arr[i]:
            leftArray[i] = leftHigh
        leftHigh = max(leftHigh, arr[i])
    
def calculateRightArray(rightArray, arr, n):

    rightHigh = 0
    for i in range(n - 1, -1, -1):
        if rightHigh > arr[i]:
            rightArray[i] = rightHigh
        rightHigh = max(rightHigh, arr[i])