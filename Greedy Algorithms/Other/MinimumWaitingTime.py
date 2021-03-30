def minimumWaitingTime(queries):
    """
    TC: O(nlogn)
    SC: O(1)
    """
    if not queries:
        return 0
    
    queries.sort()
    runningWaitingTime = 0
    totalWaitingTime = 0

    for q in queries:
        totalWaitingTime += runningWaitingTime
        runningWaitingTime += q
    
    return totalWaitingTime