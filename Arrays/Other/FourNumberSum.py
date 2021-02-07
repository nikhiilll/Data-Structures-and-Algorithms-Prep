def fourNumberSum(array, targetSum):
    
    result = []
    pairs = {}

    for i in range(1, len(array) - 1):

        for j in range(i + 1, len(array)):
            currentSum =  array[i] + array[j]
            diff = targetSum - currentSum
            if diff in pairs:
                for pair in pairs[diff]:
                    result.append(pair + ([array[i], array[j]]))

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in pairs:
                pairs[currentSum] = [[array[i], array[k]]]
            else:
                pairs[currentSum].append([array[i], array[k]])
    
    return result
