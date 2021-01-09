def hasSingleCycle(array):

    noOfElementsVisited = 0
    currentIndex = 0

    while noOfElementsVisited < len(array):

        if noOfElementsVisited > 0 and currentIndex == 0:
            return False
        
        noOfElementsVisited += 1
        nextIndex = currentIndex + array[currentIndex]

        if nextIndex < 0 or nextIndex >= len(array):
            nextIndex = nextIndex % len(array)
        
        currentIndex = nextIndex
    
    return currentIndex == 0