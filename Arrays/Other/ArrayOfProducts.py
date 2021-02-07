def arrayOfProducts(array):
    """
    TC: O(n)
    SC: O(n)
    """
    result = [1] * len(array)
    runningProduct = 1

    for i in range(len(array)):
        result[i] = runningProduct
        runningProduct *= array[i]
    
    runningProduct = 1
    for i in range(len(array) - 1, -1, -1):
        result[i] *= runningProduct
        runningProduct *= array[i]
    
    return result