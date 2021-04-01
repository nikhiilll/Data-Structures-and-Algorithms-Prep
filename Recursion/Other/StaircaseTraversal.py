def staircaseTraversal(height, maxSteps, currentHeight = 0):
    """
    TC: O(k ^ n)
    SC: O(n)
    """
    if height == currentHeight:
        return 1
    if height < currentHeight:
        return 0
    
    noOfWays = 0
    for i in range(1, maxSteps + 1):
        noOfWays += staircaseTraversal(height, maxSteps, currentHeight + i)
    
    return noOfWays