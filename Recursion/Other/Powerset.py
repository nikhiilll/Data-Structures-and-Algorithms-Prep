def powerset(array):

    powersets = [[]]
    for num in array:
        for i in range(len(powersets)):
            powersets.append(powersets[i] + [num])
    
    return powersets