def hasSingleCycle(array):

    numOfElementsVisited = 0
    currentIdx = 0

    while numOfElementsVisited < len(array):
        if numOfElementsVisited > 0 and currentIdx == 0:
            return False

        numOfElementsVisited += 1
        jump = array[currentIdx]
        nextIdx = (currentIdx + jump) % len(array)
        if nextIdx < 0:
            nextIdx += len(array)

        currentIdx = nextIdx

    return currentIdx == 0
